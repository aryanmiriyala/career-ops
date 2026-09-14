"""File-backed board and bounded evidence intake, independent of the HTTP interface."""

import csv
import hashlib
import importlib.util
import json
import math
import re
import sys
import threading
import uuid
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit


REPO = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("career_job_discovery", REPO / "job-search/src/job_discovery.py")
discovery = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = discovery
spec.loader.exec_module(discovery)
SOURCE_FILES = ("experience-master.md", "projects-master.md", "skills-master.md", "bullet-bank.md")
STOP = set("a an and the to of in for with on as is be are we you our your will or this that from by at have has into using work experience required role team ability skills".split())


def now_iso():
    return datetime.now(timezone.utc).isoformat()


def digest(text):
    return hashlib.sha256(text.encode()).hexdigest()


def write_json(path: Path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(path.name + "." + uuid.uuid4().hex + ".tmp")
    temporary.write_text(json.dumps(value, indent=2), encoding="utf-8")
    temporary.replace(path)


def safe_url(value):
    try:
        parsed = urlsplit(value.strip())
        if parsed.scheme not in {"http", "https"} or not parsed.hostname or parsed.username or parsed.password:
            return ""
        query = [(k, v) for k, v in parse_qsl(parsed.query) if not k.lower().startswith("utm_") and k.lower() not in {"ref", "source"}]
        return urlunsplit((parsed.scheme, parsed.netloc.lower(), parsed.path, urlencode(query), ""))
    except ValueError:
        return ""


def timestamp(value, reference=None):
    if not value:
        return None
    try:
        dt = discovery.parse_posted_datetime(value, reference)
        return dt.isoformat() if dt else None
    except (ValueError, OverflowError):
        return None


def load_jobs(root: Path):
    inbox = root / "job-search/jobs-inbox.csv"
    paths = ([inbox] if inbox.exists() else []) + sorted((root / "job-search/results").glob("**/jobs.csv"))
    merged = {}
    issues = []
    for path in paths:
        try:
            with path.open(encoding="utf-8-sig", newline="") as handle:
                for row in csv.DictReader(handle):
                    url = safe_url(row.get("url") or "")
                    if not url:
                        continue
                    pulled = timestamp(row.get("pulled_at") or row.get("first_discovered_at") or "")
                    observed = timestamp(row.get("last_seen_at") or "") or pulled
                    reference = datetime.fromisoformat(observed) if observed else None
                    raw_posted = row.get("posted_at") or ""
                    # Relative dates must be anchored to the original scan, never today's page load.
                    posted = timestamp(raw_posted, reference) if reference or re.match(r"^\d{4}-\d{2}-\d{2}", raw_posted) else None
                    flags = [s.strip() for s in re.split(r"[,;|]", row.get("flags") or "") if s.strip()]
                    score = row.get("fit_score") or ""
                    item = {"id": digest(url)[:20], "url": url, "company": row.get("company") or "Unknown company",
                            "title": row.get("title") or row.get("position") or "Untitled role",
                            "location": row.get("location") or "Not specified", "source": row.get("source") or discovery.detect_source(url),
                            "posted_at": posted, "posted_raw": raw_posted, "first_seen_at": pulled,
                            "last_seen_at": timestamp(row.get("last_seen_at") or "") or pulled,
                            "flags": flags, "score": int(score) if score.isdigit() else None,
                            "status": "blocked" if "work_auth_blocker" in flags else row.get("status") or "inbox",
                            "notes": row.get("notes") or "", "report": str(path.relative_to(root))}
                    previous = merged.get(url)
                    if previous:
                        firsts = [v for v in (previous["first_seen_at"], pulled) if v]
                        if (item["last_seen_at"] or "") < (previous["last_seen_at"] or ""):
                            previous["first_seen_at"] = min(firsts) if firsts else None
                            continue
                        item["first_seen_at"] = min(firsts) if firsts else None
                    merged[url] = item
        except (OSError, csv.Error, UnicodeError):
            issues.append(str(path.relative_to(root)))
    return list(merged.values()), issues


def board(root: Path, q="", hours=48, basis="posted", scope="all", source="", page=1, page_size=30):
    items, issues = load_jobs(root)
    now = datetime.now(timezone.utc)
    selected = []
    for item in items:
        if q.casefold() not in " ".join([item["company"], item["title"], item["location"]]).casefold():
            continue
        if source and source != item["source"]:
            continue
        if scope == "shortlist" and item["status"] not in {"shortlist", "inbox"}:
            continue
        if scope == "review" and item["status"] != "review":
            continue
        if scope == "blocked" and item["status"] != "blocked":
            continue
        date = item["posted_at"] if basis == "posted" else item["first_seen_at"]
        if hours and (not date or not 0 <= (now - datetime.fromisoformat(date)).total_seconds() <= hours * 3600):
            continue
        selected.append(item)
    field = "posted_at" if basis == "posted" else "first_seen_at"
    selected.sort(key=lambda item: (item[field] or "", item["score"] or 0), reverse=True)
    return {"jobs": selected[(page - 1) * page_size:page * page_size], "total": len(selected),
            "stored": len(items), "undated": sum(not i["posted_at"] for i in items),
            "sources": sorted({i["source"] for i in items}), "issues": issues,
            "last_seen_at": max((i["last_seen_at"] or "" for i in items), default="") or None}


def tokens(text):
    return [t for t in re.findall(r"[a-z0-9][a-z0-9+#./-]*", text.lower()) if len(t) > 1 and t not in STOP]


def evidence_brief(root: Path, jd: str, max_chars=18000):
    chunks = []
    for name in SOURCE_FILES:
        path = root / "profile" / name
        if not path.is_file():
            continue
        content = path.read_text(encoding="utf-8")
        heading = ""
        for number, line in enumerate(content.splitlines(), 1):
            if line.startswith("#"):
                heading = line.lstrip("# ").strip()
            elif len(line.strip()) >= 50 and not line.startswith("|"):
                body = line.strip()
                chunks.append({"id": digest(f"{name}:{number}:{body}")[:16], "source": f"profile/{name}",
                               "line": number, "heading": heading, "text": body,
                               "source_hash": digest(content), "terms": Counter(tokens(heading + " " + body))})
    queries = list(dict.fromkeys(tokens(jd)))
    frequencies = Counter(t for c in chunks for t in c["terms"])
    for chunk in chunks:
        chunk["score"] = sum(math.log(1 + len(chunks) / (1 + frequencies[t])) for t in queries if t in chunk["terms"])
    chosen, used, duplicates = [], 0, set()
    for chunk in sorted(chunks, key=lambda c: c["score"], reverse=True):
        normalized = " ".join(chunk["text"].split()).casefold()
        if chunk["score"] <= 0 or normalized in duplicates or used + len(chunk["text"]) > max_chars:
            continue
        chosen.append({k: v for k, v in chunk.items() if k != "terms"})
        duplicates.add(normalized)
        used += len(chunk["text"])
        if len(chosen) >= 18:
            break
    covered = set(tokens(" ".join(c["heading"] + " " + c["text"] for c in chosen)))
    return {"evidence": chosen, "unmatched_terms": [t for t in queries if t not in covered][:50],
            "characters": used, "estimated_tokens": math.ceil(used / 4), "llm_calls": 0,
            "notice": "Lexical candidates only. Missing matches are not proof of unsupported experience; source review and gap recovery are still required."}


class IntakeStore:
    def __init__(self, root):
        self.root = root
        self.directory = root / ".local-workspace/intakes"
        self.lock = threading.Lock()

    def create(self, company, title, jd, mode, url=""):
        fingerprint = digest(json.dumps([company.strip(), title.strip(), jd.strip(), mode, url]))[:24]
        with self.lock:
            path = self.directory / fingerprint / "intake.json"
            if path.exists():
                return json.loads(path.read_text())
            result = {"id": fingerprint, "company": company.strip(), "title": title.strip(), "mode": mode,
                      "url": safe_url(url), "created_at": now_iso(), "status": "needs_evidence_review", "jd": jd.strip()}
            result["brief"] = evidence_brief(self.root, jd)
            filters = json.loads((self.root / "job-search/config/filters.json").read_text())
            _, flags = discovery.classify_work_authorization(jd.lower(), company, filters, frozenset())
            result["flags"] = flags
            if "work_auth_blocker" in flags:
                result["status"] = "eligibility_blocked"
            path.parent.mkdir(parents=True, exist_ok=True)
            (path.parent / "job-description.md").write_text(jd.strip() + "\n", encoding="utf-8")
            write_json(path, result)
            return result

    def list(self):
        rows = []
        for path in self.directory.glob("*/intake.json"):
            try:
                row = json.loads(path.read_text())
                rows.append({k: v for k, v in row.items() if k not in {"jd", "brief"}})
            except (ValueError, OSError):
                continue
        return sorted(rows, key=lambda r: r["created_at"], reverse=True)

    def get(self, identifier):
        if not re.fullmatch(r"[a-f0-9]{24}", identifier):
            return None
        path = self.directory / identifier / "intake.json"
        return json.loads(path.read_text()) if path.is_file() else None
