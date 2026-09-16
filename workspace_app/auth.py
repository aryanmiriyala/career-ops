"""Single-owner local sessions and optional Supabase-managed identity."""

import hashlib
import hmac
import secrets
import sqlite3
import time
import base64
import json
import os
import threading
from urllib.parse import urlsplit
from pathlib import Path

import httpx

from .providers import credentials


class SupabaseAuth:
    def __init__(self, root):
        self.root = root
        self.cache = {}
        self.lock = threading.Lock()

    def config(self):
        if os.environ.get("CAREER_OPS_LOCAL_ONLY") == "1":
            return {"mode": "local"}
        values = credentials(self.root)
        url = (values.get("SUPABASE_URL") or "").rstrip("/")
        key = values.get("SUPABASE_PUBLISHABLE_KEY") or values.get("SUPABASE_ANON_KEY") or ""
        if not url and not key:
            return {"mode": "local"}
        valid_key = key.startswith("sb_publishable_")
        if not valid_key and len(key) < 4000:
            try:
                payload = key.split(".")[1]
                valid_key = json.loads(base64.urlsafe_b64decode(payload + "=" * (-len(payload) % 4)))["role"] == "anon"
            except (ValueError, IndexError, KeyError, TypeError):
                pass
        try:
            parsed = urlsplit(url)
            valid_url = parsed.scheme == "https" and bool(parsed.hostname) and not parsed.username and not parsed.password and parsed.path in {"", "/"} and not parsed.query and not parsed.fragment
        except ValueError:
            valid_url = False
        allowed = (values.get("SUPABASE_ALLOWED_EMAIL") or "").lower().strip()
        if not valid_url or not valid_key or not allowed:
            return {"mode": "supabase", "configured": False, "message": "Set a Supabase HTTPS URL, publishable/anon key, and allowed owner email in .env."}
        return {"mode": "supabase", "configured": True, "url": url, "publishable_key": key}

    def user(self, token, client=None):
        config = self.config()
        if not config.get("configured") or not token or len(token) > 16000:
            return None
        allowed = (credentials(self.root).get("SUPABASE_ALLOWED_EMAIL") or "").lower().strip()
        fingerprint = hashlib.sha256((token + config["url"] + allowed).encode()).hexdigest()
        with self.lock:
            previous = self.cache.get(fingerprint)
            if previous and previous[0] > time.time():
                return previous[1]
        owned = client is None
        client = client or httpx.Client(timeout=8, follow_redirects=False)
        try:
            # Auth server validates the access token, including legacy HS256 projects.
            response = client.get(config["url"] + "/auth/v1/user", headers={"apikey": config["publishable_key"], "Authorization": f"Bearer {token}"})
            if response.status_code != 200:
                return None
            user = response.json()
            if not isinstance(user, dict) or not user.get("id") or not user.get("email_confirmed_at") or (user.get("email") or "").lower() != allowed:
                return None
            identity = {"email": user["email"], "id": user["id"]}
            with self.lock:
                self.cache = {k: v for k, v in self.cache.items() if v[0] > time.time()}
                self.cache[fingerprint] = (time.time() + 30, identity)
            return identity
        except (httpx.HTTPError, ValueError, TypeError):
            return None
        finally:
            if owned:
                client.close()

    def forget(self, token):
        # Clear the small cache on sign-out; Supabase owns refresh-token revocation.
        with self.lock:
            self.cache.clear()


class Auth:
    def __init__(self, directory: Path):
        directory.mkdir(parents=True, exist_ok=True)
        self.path = directory / "auth.sqlite"
        with self.connection() as db:
            db.executescript("""
                CREATE TABLE IF NOT EXISTS owner (id INTEGER PRIMARY KEY CHECK (id=1), email TEXT NOT NULL, salt TEXT NOT NULL, hash TEXT NOT NULL);
                CREATE TABLE IF NOT EXISTS sessions (hash TEXT PRIMARY KEY, expires REAL NOT NULL);
            """)
        self.path.chmod(0o600)

    def connection(self):
        return sqlite3.connect(self.path, timeout=10)

    def owner(self):
        with self.connection() as db:
            row = db.execute("SELECT email FROM owner WHERE id=1").fetchone()
            return row[0] if row else None

    def password_hash(self, password, salt):
        return hashlib.scrypt(password.encode(), salt=bytes.fromhex(salt), n=16384, r=8, p=1).hex()

    def setup(self, email, password):
        salt = secrets.token_hex(16)
        hashed = self.password_hash(password, salt)
        with self.connection() as db:
            try:
                db.execute("INSERT INTO owner VALUES (1, ?, ?, ?)", (email.lower().strip(), salt, hashed))
                return True
            except sqlite3.IntegrityError:
                return False

    def login(self, email, password):
        with self.connection() as db:
            row = db.execute("SELECT email, salt, hash FROM owner WHERE id=1").fetchone()
        if not row:
            return None
        matched = hmac.compare_digest(self.password_hash(password, row[1]), row[2])
        if not matched or email.lower().strip() != row[0]:
            return None
        token = secrets.token_urlsafe(32)
        with self.connection() as db:
            db.execute("DELETE FROM sessions WHERE expires < ?", (time.time(),))
            db.execute("INSERT INTO sessions VALUES (?, ?)", (hashlib.sha256(token.encode()).hexdigest(), time.time() + 43200))
        return token

    def valid(self, token):
        if not token:
            return False
        with self.connection() as db:
            return db.execute("SELECT 1 FROM sessions WHERE hash=? AND expires>?", (hashlib.sha256(token.encode()).hexdigest(), time.time())).fetchone() is not None

    def logout(self, token):
        with self.connection() as db:
            db.execute("DELETE FROM sessions WHERE hash=?", (hashlib.sha256(token.encode()).hexdigest(),))
