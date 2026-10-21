"""Gmail integration for monitoring job-related emails.
Uses Gmail API with OAuth2. Supports push (Pub/Sub) and pull (polling) modes.
"""

from __future__ import annotations

import base64
import json
import os
import re
import time
from dataclasses import dataclass, field
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Optional

import httpx
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from .core import REPO, now_iso, write_json

# Gmail API scopes - readonly is sufficient for monitoring
SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly",
    "https://www.googleapis.com/auth/gmail.metadata",
]

# Token storage
TOKEN_DIR = REPO / ".local-workspace/gmail"
TOKEN_PATH = TOKEN_DIR / "token.json"
CREDENTIALS_PATH = TOKEN_DIR / "credentials.json"

# Job-related email patterns
JOB_KEYWORDS = [
    "application", "applied", "interview", "offer", "rejection", "rejected",
    "phone screen", "onsite", "technical screen", "hiring", "recruiter",
    "talent acquisition", "next steps", "schedule", "calendly", "meeting",
    "assessment", "coding challenge", "take home", "whiteboard", "panel",
    "final round", "reference check", "background check", "congratulations",
    "unfortunately", "not moving forward", "other candidates", "position filled",
]

COMPANY_EMAIL_PATTERNS = [
    r".*@.*\.greenhouse\.io",
    r".*@.*\.lever\.co",
    r".*@.*\.ashbyhq\.com",
    r".*@.*\.smartrecruiters\.com",
    r".*@.*\.workable\.com",
    r".*@.*\.icims\.com",
    r".*@.*\.jobvite\.com",
    r".*@.*\.bamboohr\.com",
    r".*@.*\.myworkdayjobs\.com",
    r".*@.*\.taleo\.net",
    r".*@.*\.oraclecloud\.com",
    r".*@.*\.successfactors\.com",
    r".*@.*\.careers\..*",
    r".*@.*\.jobs\..*",
    r".*@.*\.hiring\..*",
    r".*@.*\.talent\..*",
    r".*@.*\.recruiting\..*",
    r".*@.*\.people\..*",
    r".*@.*\.hr\..*",
]

# Status inference from email content
STATUS_KEYWORDS = {
    "applied": ["application received", "application submitted", "thank you for applying", "confirmation"],
    "screening": ["phone screen", "initial screen", "recruiter call", "screening call"],
    "interviewing": ["interview", "onsite", "technical", "panel", "final round", "schedule", "calendly"],
    "offer": ["offer", "congratulations", "pleased to offer", "offer letter"],
    "rejected": ["unfortunately", "not moving forward", "other candidates", "position filled", "declined"],
    "withdrawn": ["withdraw", "withdrawn", "no longer interested"],
}


@dataclass
class GmailMessage:
    id: str
    thread_id: str
    subject: str
    from_email: str
    from_name: str
    date: str
    snippet: str
    body_text: str
    body_html: str
    labels: list[str]
    is_job_related: bool = False
    inferred_status: Optional[str] = None
    company: Optional[str] = None
    role: Optional[str] = None

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "thread_id": self.thread_id,
            "subject": self.subject,
            "from_email": self.from_email,
            "from_name": self.from_name,
            "date": self.date,
            "snippet": self.snippet,
            "body_text": self.body_text[:5000],  # Truncate for storage
            "labels": self.labels,
            "is_job_related": self.is_job_related,
            "inferred_status": self.inferred_status,
            "company": self.company,
            "role": self.role,
        }


@dataclass
class GmailConfig:
    enabled: bool = True
    poll_interval_seconds: int = 300  # 5 minutes
    max_results_per_poll: int = 50
    lookback_days: int = 7
    labels_to_watch: list[str] = field(default_factory=lambda: ["INBOX"])
    sender_filters: list[str] = field(default_factory=list)  # Additional sender patterns
    auto_update_tracker: bool = True
    webhook_url: Optional[str] = None  # For push notifications


class GmailClient:
    """Gmail API client for job email monitoring."""

    def __init__(self, config: GmailConfig, root: Path = REPO):
        self.config = config
        self.root = root
        self.service = None
        self.credentials = None
        self._last_poll_time: Optional[datetime] = None
        self._history_id: Optional[str] = None

    def authenticate(self) -> bool:
        """Authenticate with Gmail API using OAuth2."""
        TOKEN_DIR.mkdir(parents=True, exist_ok=True)

        if TOKEN_PATH.exists():
            self.credentials = Credentials.from_authorized_user_file(
                str(TOKEN_PATH), SCOPES
            )

        if not self.credentials or not self.credentials.valid:
            if self.credentials and self.credentials.expired and self.credentials.refresh_token:
                self.credentials.refresh(Request())
            else:
                if not CREDENTIALS_PATH.exists():
                    print(f"Gmail credentials not found at {CREDENTIALS_PATH}")
                    print("Download OAuth2 credentials from Google Cloud Console and save as credentials.json")
                    return False
                flow = InstalledAppFlow.from_client_secrets_file(
                    str(CREDENTIALS_PATH), SCOPES
                )
                self.credentials = flow.run_local_server(port=0)

            # Save token
            TOKEN_PATH.write_text(self.credentials.to_json())

        self.service = build("gmail", "v1", credentials=self.credentials)
        return True

    def get_profile(self) -> dict:
        """Get user profile info."""
        return self.service.users().getProfile(userId="me").execute()

    def build_query(self, since: Optional[datetime] = None) -> str:
        """Build Gmail search query for job-related emails."""
        parts = []

        # Date filter
        if since:
            date_str = since.strftime("%Y/%m/%d")
            parts.append(f"after:{date_str}")
        elif self.config.lookback_days:
            date_str = (datetime.now() - timedelta(days=self.config.lookback_days)).strftime("%Y/%m/%d")
            parts.append(f"after:{date_str}")

        # Labels
        for label in self.config.labels_to_watch:
            parts.append(f"label:{label}")

        # Job keywords (OR)
        if JOB_KEYWORDS:
            kw = " OR ".join(f'"{k}"' for k in JOB_KEYWORDS[:10])  # Limit for query length
            parts.append(f"({kw})")

        # Company email patterns (OR)
        if COMPANY_EMAIL_PATTERNS:
            # Use from: with common ATS domains
            ats_domains = [
                "greenhouse.io", "lever.co", "ashbyhq.com", "smartrecruiters.com",
                "workable.com", "icims.com", "jobvite.com", "bamboohr.com",
                "myworkdayjobs.com", "taleo.net", "careers.", "jobs."
            ]
            from_parts = [f"from:{d}" for d in ats_domains]
            parts.append(f"({' OR '.join(from_parts)})")

        # Additional sender filters
        for sender in self.config.sender_filters:
            parts.append(f"from:{sender}")

        return " ".join(parts)

    def list_messages(self, query: str, max_results: int = 50, page_token: Optional[str] = None) -> dict:
        """List messages matching query."""
        return self.service.users().messages().list(
            userId="me",
            q=query,
            maxResults=max_results,
            pageToken=page_token,
        ).execute()

    def get_message(self, msg_id: str, format: str = "full") -> dict:
        """Get full message details."""
        return self.service.users().messages().get(
            userId="me", id=msg_id, format=format
        ).execute()

    def get_thread(self, thread_id: str) -> dict:
        """Get full thread."""
        return self.service.users().threads().get(
            userId="me", id=thread_id
        ).execute()

    def parse_message(self, msg: dict) -> GmailMessage:
        """Parse Gmail message into structured object."""
        headers = {h["name"]: h["value"] for h in msg.get("payload", {}).get("headers", [])}

        subject = headers.get("Subject", "")
        from_header = headers.get("From", "")
        date_header = headers.get("Date", "")

        # Parse from name and email
        from_match = re.match(r'"?([^"<]+)"?\s*<([^>]+)>', from_header)
        if from_match:
            from_name, from_email = from_match.groups()
        else:
            from_name, from_email = "", from_header

        # Extract body
        body_text, body_html = self._extract_body(msg.get("payload", {}))

        # Check if job-related
        is_job, inferred_status, company, role = self._analyze_job_relevance(
            subject, from_email, from_name, body_text, body_html
        )

        return GmailMessage(
            id=msg["id"],
            thread_id=msg["threadId"],
            subject=subject,
            from_email=from_email.lower(),
            from_name=from_name.strip(),
            date=date_header,
            snippet=msg.get("snippet", ""),
            body_text=body_text,
            body_html=body_html,
            labels=msg.get("labelIds", []),
            is_job_related=is_job,
            inferred_status=inferred_status,
            company=company,
            role=role,
        )

    def _extract_body(self, payload: dict) -> tuple[str, str]:
        """Recursively extract text and HTML body from message payload."""
        text_parts = []
        html_parts = []

        def extract(part):
            mime_type = part.get("mimeType", "")
            data = part.get("body", {}).get("data", "")

            if mime_type == "text/plain" and data:
                text_parts.append(base64.urlsafe_b64decode(data).decode("utf-8", errors="replace"))
            elif mime_type == "text/html" and data:
                html_parts.append(base64.urlsafe_b64decode(data).decode("utf-8", errors="replace"))
            elif mime_type.startswith("multipart/"):
                for subpart in part.get("parts", []):
                    extract(subpart)

        extract(payload)
        return "\n".join(text_parts), "\n".join(html_parts)

    def _analyze_job_relevance(
        self, subject: str, from_email: str, from_name: str, body_text: str, body_html: str
    ) -> tuple[bool, Optional[str], Optional[str], Optional[str]]:
        """Analyze if email is job-related and infer status/company/role."""
        full_text = f"{subject} {from_name} {from_email} {body_text} {body_html}".lower()

        # Check for ATS sender patterns
        is_ats_sender = any(re.search(p, from_email) for p in COMPANY_EMAIL_PATTERNS)

        # Check for job keywords
        keyword_matches = sum(1 for kw in JOB_KEYWORDS if kw in full_text)

        is_job = is_ats_sender or keyword_matches >= 2

        if not is_job:
            return False, None, None, None

        # Infer status
        inferred_status = None
        for status, keywords in STATUS_KEYWORDS.items():
            if any(kw in full_text for kw in keywords):
                inferred_status = status
                break

        # Extract company from sender
        company = None
        if is_ats_sender:
            # Try to extract company from ATS subdomain
            for pattern in [r"([^.]+)\.greenhouse\.io", r"([^.]+)\.lever\.co", r"([^.]+)\.ashbyhq\.com"]:
                match = re.search(pattern, from_email)
                if match:
                    company = match.group(1).replace("-", " ").title()
                    break
        else:
            # Try from domain
            domain_match = re.search(r"@([^.]+)\.", from_email)
            if domain_match:
                company = domain_match.group(1).replace("-", " ").title()

        # Extract role from subject
        role = None
        role_patterns = [
            r"(?:for|position|role)\s*:?\s*([^,\n]+)",
            r"(?:software|data|ml|ai|full.stack|backend|frontend)\s+(?:engineer|developer|scientist)",
        ]
        for pattern in role_patterns:
            match = re.search(pattern, subject, re.IGNORECASE)
            if match:
                role = match.group(1).strip() if match.groups() else match.group(0).strip()
                break

        return True, inferred_status, company, role

    def poll_once(self, since: Optional[datetime] = None) -> list[GmailMessage]:
        """Single poll for new job-related messages."""
        query = self.build_query(since)
        messages = []

        result = self.list_messages(query, max_results=self.config.max_results_per_poll)
        for msg_ref in result.get("messages", []):
            msg = self.get_message(msg_ref["id"])
            parsed = self.parse_message(msg)
            if parsed.is_job_related:
                messages.append(parsed)

        self._last_poll_time = datetime.now(timezone.utc)
        return messages

    def start_push_watch(self, topic_name: str) -> dict:
        """Set up Gmail push notifications via Pub/Sub.
        Requires: Google Cloud project, Pub/Sub topic, push endpoint.
        """
        if not self.config.webhook_url:
            raise ValueError("webhook_url required for push watch")

        request = {
            "labelIds": self.config.labels_to_watch,
            "topicName": topic_name,
        }
        return self.service.users().watch(userId="me", body=request).execute()

    def stop_push_watch(self) -> dict:
        """Stop Gmail push notifications."""
        return self.service.users().stop(userId="me").execute()


class JobEmailProcessor:
    """Process job-related emails and update application tracker."""

    def __init__(self, gmail_client: GmailClient, root: Path = REPO):
        self.gmail = gmail_client
        self.root = root
        self.tracker_path = root / "operations" / "application-tracker.md"
        self.processed_ids_path = root / ".local-workspace/gmail" / "processed_ids.json"
        self.processed_ids = self._load_processed_ids()

    def _load_processed_ids(self) -> set:
        if self.processed_ids_path.exists():
            try:
                return set(json.loads(self.processed_ids_path.read_text()))
            except (json.JSONDecodeError, OSError):
                pass
        return set()

    def _save_processed_ids(self):
        self.processed_ids_path.parent.mkdir(parents=True, exist_ok=True)
        self.processed_ids_path.write_text(json.dumps(list(self.processed_ids)))

    def process_messages(self, messages: list[GmailMessage]) -> dict[str, int]:
        """Process messages and update tracker. Returns stats."""
        stats = {"new": 0, "updated": 0, "skipped": 0}

        for msg in messages:
            if msg.id in self.processed_ids:
                stats["skipped"] += 1
                continue

            # Try to match to existing application
            match = self._match_to_application(msg)

            if match:
                # Update existing application
                if self.gmail.config.auto_update_tracker and msg.inferred_status:
                    self._update_tracker_status(match, msg.inferred_status, msg)
                stats["updated"] += 1
            else:
                # New potential application from email
                self._log_new_job_email(msg)
                stats["new"] += 1

            self.processed_ids.add(msg.id)

        self._save_processed_ids()
        return stats

    def _match_to_application(self, msg: GmailMessage) -> Optional[dict]:
        """Match email to existing application in tracker."""
        if not self.tracker_path.exists():
            return None

        lines = self.tracker_path.read_text().splitlines()
        for line in lines:
            if not line.startswith("|") or "Status" in line or "---" in line:
                continue
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) < 11:
                continue

            company, role = cells[1], cells[2]

            # Match by company and/or role
            company_match = msg.company and msg.company.lower() in company.lower()
            role_match = msg.role and msg.role.lower() in role.lower()
            email_match = msg.from_email and msg.from_email in cells[10]  # Job Link column

            if company_match or role_match or email_match:
                return {
                    "company": company,
                    "role": role,
                    "status": cells[0],
                    "job_link": cells[10],
                    "line": line,
                }
        return None

    def _update_tracker_status(self, match: dict, new_status: str, msg: GmailMessage):
        """Update application tracker with new status from email."""
        if not self.tracker_path.exists():
            return

        lines = self.tracker_path.read_text().splitlines()
        today = datetime.now().isoformat()[:10]

        for i, line in enumerate(lines):
            if match["line"] in line:
                cells = [c.strip() for c in line.strip("|").split("|")]
                if len(cells) >= 11:
                    # Update status
                    cells[0] = new_status.capitalize()
                    # Update last update
                    cells[5] = today
                    # Add note about email
                    note = cells[10] if len(cells) > 10 else ""
                    email_note = f"Gmail: {msg.subject[:50]} ({msg.date[:10]})"
                    cells[10] = f"{note}; {email_note}" if note else email_note
                    lines[i] = "| " + " | ".join(cells) + " |"
                    break

        self.tracker_path.write_text("\n".join(lines) + "\n")

    def _log_new_job_email(self, msg: GmailMessage):
        """Log job-related email that doesn't match existing application."""
        log_path = self.root / ".local-workspace/gmail" / "job_emails.log"
        log_path.parent.mkdir(parents=True, exist_ok=True)

        entry = {
            "timestamp": now_iso(),
            "message_id": msg.id,
            "subject": msg.subject,
            "from": msg.from_email,
            "inferred_status": msg.inferred_status,
            "company": msg.company,
            "role": msg.role,
        }
        with log_path.open("a") as f:
            f.write(json.dumps(entry) + "\n")


class GmailMonitor:
    """High-level monitor combining client and processor."""

    def __init__(self, config: GmailConfig, root: Path = REPO):
        self.config = config
        self.root = root
        self.client = GmailClient(config, root)
        self.processor = JobEmailProcessor(self.client, root)
        self._running = False

    def start(self) -> bool:
        """Start monitoring."""
        if not self.client.authenticate():
            return False

        self._running = True
        print(f"Gmail monitor started. Polling every {self.config.poll_interval_seconds}s")

        # Initial sync
        self.sync()

        # Poll loop
        while self._running:
            try:
                time.sleep(self.config.poll_interval_seconds)
                self.sync()
            except KeyboardInterrupt:
                break
            except Exception as e:
                print(f"Poll error: {e}")
                time.sleep(60)  # Back off on error

        return True

    def stop(self):
        """Stop monitoring."""
        self._running = False

    def sync(self) -> dict:
        """Single sync: fetch and process new messages."""
        since = self.client._last_poll_time
        messages = self.client.poll_once(since=since)

        if messages:
            stats = self.processor.process_messages(messages)
            print(f"Processed {len(messages)} job emails: {stats}")
            return stats

        return {"new": 0, "updated": 0, "skipped": 0}

    def get_recent_job_emails(self, days: int = 7) -> list[GmailMessage]:
        """Get all job emails from last N days."""
        since = datetime.now(timezone.utc) - timedelta(days=days)
        return self.client.poll_once(since=since)


def create_gmail_credentials_guide() -> str:
    """Generate setup guide for Gmail API credentials."""
    return """# Gmail API Setup Guide

## 1. Create Google Cloud Project
1. Go to https://console.cloud.google.com/
2. Create new project or select existing: "Career Ops"
3. Enable Gmail API: APIs & Services > Library > Gmail API > Enable

## 2. Create OAuth2 Credentials
1. Go to APIs & Services > Credentials
2. Create Credentials > OAuth client ID
3. Application type: Desktop app
4. Name: "Career Ops Gmail Monitor"
5. Download JSON as `credentials.json`
6. Place at: `.local-workspace/gmail/credentials.json`

## 3. Configure OAuth Consent Screen
1. APIs & Services > OAuth consent screen
2. User Type: External
3. App name: Career Ops
4. Authorized domains: (your domain or leave blank for localhost)
5. Scopes: Add `gmail.readonly`, `gmail.metadata`
5. Test users: Add your Gmail address

## 4. Run Initial Authentication
```bash
python3 -m workspace_app.gmail_integration --auth
```
This will open browser for consent and save token.json.

## 5. Run Monitor
```bash
# One-time sync
python3 -m workspace_app.gmail_integration --sync

# Continuous monitoring
python3 -m workspace_app.gmail_integration --monitor
```

## 6. Push Notifications (Optional - Advanced)
For real-time updates instead of polling:
1. Create Pub/Sub topic in Google Cloud
2. Set up push endpoint (Cloud Run, Cloud Function, or ngrok tunnel)
3. Configure `webhook_url` in GmailConfig
4. Call `client.start_push_watch(topic_name)`

## Security Notes
- Token stored locally at `.local-workspace/gmail/token.json`
- Only `gmail.readonly` scope - cannot send/modify/delete emails
- Revoke access anytime at https://myaccount.google.com/permissions
"""


# CLI Entry Point
def main():
    import argparse

    parser = argparse.ArgumentParser(description="Gmail Job Email Monitor")
    parser.add_argument("--auth", action="store_true", help="Run OAuth authentication flow")
    parser.add_argument("--sync", action="store_true", help="Run one-time sync")
    parser.add_argument("--monitor", action="store_true", help="Run continuous monitor")
    parser.add_argument("--days", type=int, default=7, help="Lookback days for sync")
    parser.add_argument("--interval", type=int, default=300, help="Poll interval seconds")
    parser.add_argument("--guide", action="store_true", help="Print setup guide")
    args = parser.parse_args()

    if args.guide:
        print(create_gmail_credentials_guide())
        return 0

    config = GmailConfig(
        poll_interval_seconds=args.interval,
        lookback_days=args.days,
    )

    monitor = GmailMonitor(config)

    if args.auth:
        if monitor.client.authenticate():
            print("Authentication successful!")
            print(f"Token saved to {TOKEN_PATH}")
        return 0

    if args.sync:
        if monitor.client.authenticate():
            stats = monitor.sync()
            print(f"Sync complete: {stats}")
        return 0

    if args.monitor:
        if monitor.client.authenticate():
            monitor.start()
        return 0

    parser.print_help()
    return 1


if __name__ == "__main__":
    raise SystemExit(main())