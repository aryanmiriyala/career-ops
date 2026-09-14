import csv
import json
import tempfile
import threading
import unittest
from datetime import datetime, timedelta, timezone
from pathlib import Path
from unittest.mock import Mock, patch

import httpx
from fastapi.testclient import TestClient

from workspace_app.api import create_app
from workspace_app.auth import Auth, SupabaseAuth
from workspace_app.core import IntakeStore, board, discovery, evidence_brief, load_jobs, safe_url
from workspace_app.providers import probe, statuses
from workspace_app.scans import Scans


def fixture(root):
    (root / "job-search/config").mkdir(parents=True)
    (root / "job-search/config/filters.json").write_text(json.dumps({"work_authorization_policy": {
        "sponsorship_blocker_terms": ["no visa sponsorship"]}}))
    (root / "profile").mkdir()
    (root / "profile/experience-master.md").write_text("# Experience\n## Example internship\n- Built Python data pipelines with SQL validation to process 500 synthetic records for a classroom project.\n")
    (root / "profile/projects-master.md").write_text("# Projects\n## Example app\n- Built a React interface with accessible forms and automated component tests for a synthetic sample dataset.\n")


def csv_file(path, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=sorted({k for row in rows for k in row}))
        writer.writeheader()
        writer.writerows(rows)


class WorkspaceTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        fixture(self.root)
        self.client = TestClient(create_app(self.root))
        self.owner = {"email": "owner@example.test", "password": "synthetic-password-123"}

    def tearDown(self):
        self.client.close()
        self.tmp.cleanup()

    def login(self):
        return self.client.post("/api/auth/setup", json=self.owner)

    def test_private_endpoints_require_login(self):
        for route in ("/api/providers", "/api/jobs", "/api/intakes", "/api/scans/current"):
            self.assertEqual(self.client.get(route).status_code, 401)

    def test_first_run_setup_only_once(self):
        self.assertTrue(self.client.get("/api/auth/session").json()["setup_required"])
        result = self.login()
        self.assertEqual(result.status_code, 200)
        self.assertIn("HttpOnly", result.headers["set-cookie"])
        self.assertIn("SameSite=strict", result.headers["set-cookie"])
        self.assertEqual(self.client.post("/api/auth/setup", json=self.owner).status_code, 409)
        self.assertTrue(self.client.get("/api/auth/session").json()["authenticated"])

    def test_logout_revokes_session(self):
        self.login()
        cookie = self.client.cookies.get("career_session")
        self.client.post("/api/auth/logout")
        self.assertFalse(Auth(self.root / ".local-workspace").valid(cookie))
        self.assertEqual(self.client.get("/api/jobs").status_code, 401)

    def test_password_and_session_stored_hashed(self):
        self.login()
        raw = (self.root / ".local-workspace/auth.sqlite").read_bytes()
        self.assertNotIn(self.owner["password"].encode(), raw)
        self.assertNotIn(self.client.cookies.get("career_session").encode(), raw)

    def test_password_validation_never_echoes_input(self):
        response = self.client.post("/api/auth/setup", json={"email": "a", "password": "SECRET"})
        self.assertEqual(response.status_code, 422)
        self.assertNotIn("SECRET", response.text)

    def test_login_failure_and_rate_limit(self):
        self.login()
        for _ in range(8):
            self.assertEqual(self.client.post("/api/auth/login", json={**self.owner, "password": "wrong-password-here"}).status_code, 401)
        self.assertEqual(self.client.post("/api/auth/login", json=self.owner).status_code, 429)

    def test_cross_origin_write_rejected(self):
        self.assertEqual(self.client.post("/api/auth/setup", json=self.owner, headers={"origin": "https://evil.example"}).status_code, 403)

    def test_same_origin_setup_allowed(self):
        self.assertEqual(self.client.post("/api/auth/setup", json=self.owner, headers={"origin": "http://testserver"}).status_code, 200)

    def test_untrusted_host_rejected(self):
        self.assertEqual(self.client.get("/api/auth/session", headers={"host": "evil.example"}).status_code, 400)

    def test_secret_status_supports_existing_aliases_without_exposure(self):
        (self.root / ".env").write_text("ZAI_KEY=do-not-print-this\nOPENCODE_API_KEY=private-sentinel\n")
        result = statuses(self.root)
        self.assertTrue(next(p for p in result["providers"] if p["id"] == "zai")["configured"])
        self.assertNotIn("do-not-print-this", json.dumps(result))
        self.assertNotIn("private-sentinel", json.dumps(result))

    def test_provider_error_body_not_exposed(self):
        (self.root / ".env").write_text("ZAI_KEY=secret-sentinel\n")
        client = Mock()
        client.post.return_value = httpx.Response(401, text="Authorization secret-sentinel")
        result = probe(self.root, "zai", client)
        self.assertEqual(result["status"], "failed")
        self.assertNotIn("secret-sentinel", json.dumps(result))
        self.assertEqual(client.post.call_count, 1)

    def test_provider_metadata_is_not_reported_as_inference(self):
        (self.root / ".env").write_text("OPENCODE_API_KEY=test-secret\n")
        client = Mock()
        client.get.return_value = httpx.Response(200, json={"data": []})
        self.assertEqual(probe(self.root, "opencode", client)["status"], "reachable")
        client.post.assert_not_called()

    def test_synthetic_zai_probe_is_bounded(self):
        (self.root / ".env").write_text("ZAI_KEY=test-secret\n")
        client = Mock()
        client.post.return_value = httpx.Response(200, json={"choices": [{"message": {"content": "OK"}}], "usage": {"total_tokens": 20}})
        result = probe(self.root, "zai", client)
        self.assertEqual(result["status"], "verified")
        payload = client.post.call_args.kwargs["json"]
        self.assertEqual(payload["model"], "glm-4.7-flash")
        self.assertEqual(payload["max_tokens"], 32)
        self.assertNotIn("profile", str(payload))

    def test_bad_urls_rejected(self):
        for url in ("javascript:alert(1)", "file:///etc/passwd", "https://user:secret@example.com"):
            self.assertEqual(safe_url(url), "")
        self.assertEqual(safe_url("https://example.com/jobs/1?utm_source=x&id=42"), "https://example.com/jobs/1?id=42")

    def test_recent_filter_does_not_relabel_old_or_undated_jobs(self):
        now = datetime.now(timezone.utc)
        csv_file(self.root / "job-search/jobs-inbox.csv", [
            {"company": "Fresh", "position": "Engineer", "url": "https://example.com/1", "posted_at": (now - timedelta(hours=2)).isoformat(), "pulled_at": now.isoformat()},
            {"company": "Old", "position": "Engineer", "url": "https://example.com/2", "posted_at": (now - timedelta(days=50)).isoformat(), "pulled_at": now.isoformat()},
            {"company": "Unknown", "position": "Engineer", "url": "https://example.com/3", "posted_at": "", "pulled_at": now.isoformat()},
        ])
        self.assertEqual(board(self.root)["total"], 1)
        self.assertEqual(board(self.root, basis="discovered")["total"], 3)
        self.assertEqual(board(self.root, hours=0)["total"], 3)

    def test_relative_posted_date_anchored_to_last_scan(self):
        csv_file(self.root / "job-search/results/old/jobs.csv", [{"company": "A", "title": "Role", "url": "https://example.com/1", "posted_at": "2 days ago", "pulled_at": "2026-01-01T00:00:00Z", "last_seen_at": "2026-02-01T00:00:00Z"}])
        rows, _ = load_jobs(self.root)
        self.assertEqual(rows[0]["posted_at"], "2026-01-30T00:00:00+00:00")

    def test_future_dates_excluded(self):
        csv_file(self.root / "job-search/jobs-inbox.csv", [{"url": "https://example.com/1", "posted_at": "2099-01-01T00:00:00Z"}])
        self.assertEqual(board(self.root)["total"], 0)

    def test_duplicate_url_uses_latest_metadata_and_earliest_discovery(self):
        csv_file(self.root / "job-search/jobs-inbox.csv", [{"url": "https://example.com/1?utm_source=a", "position": "Old", "pulled_at": "2026-01-01"}])
        csv_file(self.root / "job-search/results/new/jobs.csv", [{"url": "https://example.com/1", "title": "New", "pulled_at": "2026-02-01", "flags": "work_auth_blocker", "status": "shortlist"}])
        result = board(self.root, hours=0)
        self.assertEqual(result["total"], 1)
        self.assertEqual(result["jobs"][0]["title"], "New")
        self.assertTrue(result["jobs"][0]["first_seen_at"].startswith("2026-01-01"))
        self.assertEqual(board(self.root, hours=0, scope="shortlist")["total"], 0)

    def test_evidence_bounded_and_excludes_historical_packages(self):
        historical = self.root / "application-packages/Secret/Role"
        historical.mkdir(parents=True)
        (historical / "resume.tex").write_text("Python HISTORICAL_SENTINEL" * 50)
        result = evidence_brief(self.root, "Python SQL data pipelines", max_chars=160)
        self.assertLessEqual(result["characters"], 160)
        self.assertNotIn("HISTORICAL_SENTINEL", json.dumps(result))
        self.assertEqual(result["llm_calls"], 0)

    def test_intake_idempotent_and_full_posting_preserved(self):
        store = IntakeStore(self.root)
        jd = "Python SQL pipelines and data validation. " * 6
        a = store.create("Example", "Role", jd, "balanced")
        b = store.create("Example", "Role", jd, "balanced")
        self.assertEqual(a["id"], b["id"])
        self.assertEqual(len(store.list()), 1)
        self.assertEqual((store.directory / a["id"] / "job-description.md").read_text().strip(), jd.strip())
        self.assertFalse((self.root / "application-packages").exists())
        self.assertFalse((self.root / "operations/application-tracker.md").exists())

    def test_intake_with_explicit_blocker_is_not_ready(self):
        result = IntakeStore(self.root).create("Example", "Role", "Python data engineer. No visa sponsorship is available.", "balanced")
        self.assertEqual(result["status"], "eligibility_blocked")

    def test_intake_api_roundtrip_and_path_validation(self):
        self.login()
        body = {"company": "Example", "title": "Engineer", "jd": "Python engineering position with SQL data pipelines and validation. " * 3}
        result = self.client.post("/api/intakes", json=body)
        self.assertEqual(result.status_code, 200)
        self.assertEqual(self.client.get('/api/intakes/' + result.json()["id"]).status_code, 200)
        self.assertIsNone(IntakeStore(self.root).get("../../.env"))

    def test_invalid_mode_rejected(self):
        self.login()
        body = {"company": "Example", "title": "Engineer", "jd": "Python " * 30, "mode": "fabricate"}
        self.assertEqual(self.client.post("/api/intakes", json=body).status_code, 422)

    def test_scan_restart_marked_interrupted(self):
        path = self.root / ".local-workspace/scan.json"
        path.write_text(json.dumps({"status": "running"}))
        self.assertEqual(Scans(self.root).snapshot()["status"], "interrupted")

    def test_duplicate_scan_prevented_without_starting_process(self):
        scans = Scans(self.root)
        with patch("workspace_app.scans.threading.Thread"):
            scans.start(5)
            with self.assertRaises(ValueError):
                scans.start(5)
            self.assertEqual(scans.cancel()["status"], "cancelling")

    def test_original_pipeline_default_scope_preserved(self):
        self.assertEqual(discovery.build_parser().parse_args(["run-pipeline"] ).company_limit, 0)
        self.assertEqual(discovery.build_parser().parse_args(["run-pipeline", "--company-limit", "5"]).company_limit, 5)

    def test_supabase_configuration_disables_local_auth(self):
        (self.root / ".env").write_text("SUPABASE_URL=https://test.supabase.co\nSUPABASE_PUBLISHABLE_KEY=sb_publishable_synthetic\nSUPABASE_ALLOWED_EMAIL=owner@example.test\n")
        self.assertEqual(self.client.get("/api/auth/config").json()["mode"], "supabase")
        self.assertEqual(self.login().status_code, 403)

    def test_supabase_does_not_publish_secret_key(self):
        (self.root / ".env").write_text("SUPABASE_URL=https://test.supabase.co\nSUPABASE_PUBLISHABLE_KEY=sb_secret_DO_NOT_EXPOSE\nSUPABASE_ALLOWED_EMAIL=owner@example.test\n")
        result = self.client.get("/api/auth/config")
        self.assertNotIn("DO_NOT_EXPOSE", result.text)
        self.assertFalse(result.json()["configured"])

    def test_supabase_missing_allowlist_fails_closed(self):
        (self.root / ".env").write_text("SUPABASE_URL=https://test.supabase.co\nSUPABASE_PUBLISHABLE_KEY=sb_publishable_synthetic\n")
        self.assertFalse(self.client.get("/api/auth/config").json()["configured"])
        self.assertFalse(self.client.get("/api/auth/session").json()["authenticated"])

    def test_supabase_validates_confirmed_owner_with_auth_server(self):
        (self.root / ".env").write_text("SUPABASE_URL=https://test.supabase.co\nSUPABASE_PUBLISHABLE_KEY=sb_publishable_synthetic\nSUPABASE_ALLOWED_EMAIL=owner@example.test\n")
        remote = SupabaseAuth(self.root)
        client = Mock()
        client.get.return_value = httpx.Response(200, json={"id": "owner-id", "email": "stranger@example.test", "email_confirmed_at": "2026-01-01"})
        self.assertIsNone(remote.user("untrusted", client))
        client.get.return_value = httpx.Response(200, json={"id": "owner-id", "email": "owner@example.test"})
        self.assertIsNone(remote.user("unconfirmed", client))
        client.get.return_value = httpx.Response(200, json={"id": "owner-id", "email": "owner@example.test", "email_confirmed_at": "2026-01-01"})
        self.assertEqual(remote.user("valid-synthetic", client)["id"], "owner-id")
        self.assertEqual(client.get.call_args.args[0], "https://test.supabase.co/auth/v1/user")

    def test_supabase_unavailable_fails_closed(self):
        (self.root / ".env").write_text("SUPABASE_URL=https://test.supabase.co\nSUPABASE_PUBLISHABLE_KEY=sb_publishable_synthetic\nSUPABASE_ALLOWED_EMAIL=owner@example.test\n")
        client = Mock()
        client.get.side_effect = httpx.ConnectError("network down")
        self.assertIsNone(SupabaseAuth(self.root).user("synthetic", client))


if __name__ == "__main__":
    unittest.main()
