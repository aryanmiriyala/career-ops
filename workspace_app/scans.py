"""One bounded subprocess at a time; scan artifacts remain in job-search."""

import json
import subprocess
import sys
import threading
import uuid

from .core import now_iso, write_json


class Scans:
    def __init__(self, root):
        self.root = root
        self.state_path = root / ".local-workspace/scan.json"
        self.lock = threading.Lock()
        self.process = None
        self.state = {"status": "idle"}
        if self.state_path.exists():
            self.state = json.loads(self.state_path.read_text())
            if self.state["status"] in {"running", "cancelling"}:
                self.state.update(status="interrupted", message="Server restarted. Partial results may be available.")
                write_json(self.state_path, self.state)

    def snapshot(self):
        with self.lock:
            return dict(self.state)

    def start(self, company_limit):
        with self.lock:
            if self.state["status"] in {"running", "cancelling"}:
                raise ValueError("A discovery scan is already running.")
            identifier = uuid.uuid4().hex[:12]
            results = self.root / "job-search/results" / now_iso()[:10] / f"workspace-{identifier}"
            self.state = {"status": "running", "id": identifier, "started_at": now_iso(),
                          "company_limit": company_limit, "results_dir": str(results.relative_to(self.root)),
                          "llm_calls": 0, "message": "Scanning configured ATS boards and public feeds."}
            write_json(self.state_path, self.state)
            threading.Thread(target=self._run, args=(results, company_limit), daemon=True).start()
            return dict(self.state)

    def _run(self, results, company_limit):
        log_path = self.root / ".local-workspace/scan.log"
        try:
            with log_path.open("w") as log:
                with self.lock:
                    if self.state["status"] == "cancelling":
                        self.state.update(status="cancelled", finished_at=now_iso())
                        write_json(self.state_path, self.state)
                        return
                    self.process = subprocess.Popen([
                        sys.executable, "job-search/src/job_discovery.py", "run-pipeline", "--dry-run",
                        "--company-limit", str(company_limit), "--results-dir", str(results)
                    ], cwd=self.root, stdout=log, stderr=log)
                    process = self.process
                try:
                    code = process.wait(timeout=1200)
                    status = "completed" if code == 0 else "failed"
                except subprocess.TimeoutExpired:
                    process.kill()
                    process.wait()
                    status = "timed_out"
            with self.lock:
                if status == "completed" and (results / "run-state.json").exists():
                    summary = json.loads((results / "run-state.json").read_text())
                    self.state.update(fetched_jobs=summary.get("fetched_jobs", 0), source_errors=summary.get("source_errors", 0))
                    if summary.get("source_errors"):
                        status = "completed_with_warnings"
                if self.state["status"] == "cancelling":
                    status = "cancelled"
                self.state.update(status=status, finished_at=now_iso(), message="Scan ended. Results include only postings returned by the configured sources.")
                write_json(self.state_path, self.state)
                self.process = None
        except (OSError, ValueError):
            with self.lock:
                self.state.update(status="failed", finished_at=now_iso(), message="Could not start the discovery command.")
                write_json(self.state_path, self.state)

    def cancel(self):
        with self.lock:
            if self.state["status"] == "running":
                self.state["status"] = "cancelling"
                write_json(self.state_path, self.state)
                if self.process:
                    self.process.terminate()
            return dict(self.state)
