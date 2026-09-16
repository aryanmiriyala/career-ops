import os
import asyncio
import threading
import time
from contextlib import asynccontextmanager
from pathlib import Path
from typing import Literal
from urllib.parse import urlsplit

from fastapi import FastAPI, HTTPException, Query, Request, Response
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel, Field, field_validator
from starlette.middleware.trustedhost import TrustedHostMiddleware

from .auth import Auth, SupabaseAuth
from .core import IntakeStore, JobIndex, REPO, board
from .providers import probe, statuses
from .scans import Scans


class Login(BaseModel):
    email: str = Field(min_length=3, max_length=200)
    password: str = Field(min_length=12, max_length=200)

    @field_validator("email")
    @classmethod
    def email_format(cls, value):
        if "@" not in value or " " in value:
            raise ValueError("Invalid email")
        return value


class Intake(BaseModel):
    company: str = Field(min_length=1, max_length=150)
    title: str = Field(min_length=1, max_length=200)
    jd: str = Field(min_length=100, max_length=80000)
    mode: Literal["faithful", "balanced", "aggressive"] = "balanced"
    url: str = Field(default="", max_length=2000)

    @field_validator("company", "title", "jd")
    @classmethod
    def nonblank(cls, value):
        if not value.strip():
            raise ValueError("Must not be blank")
        return value.strip()


class ScanRequest(BaseModel):
    company_limit: int = Field(default=20, ge=0, le=500)


def create_app(root: Path = REPO):
    auth = Auth(root / ".local-workspace")
    supabase = SupabaseAuth(root)
    scans = Scans(root)
    intakes = IntakeStore(root)
    job_index = JobIndex(root)
    attempts = {}
    attempt_lock = threading.Lock()
    probe_lock = threading.Lock()

    @asynccontextmanager
    async def lifespan(app):
        yield
        scans.cancel()

    app = FastAPI(title="Career Ops Local", docs_url=None, redoc_url=None, openapi_url=None, lifespan=lifespan)
    app.add_middleware(TrustedHostMiddleware, allowed_hosts=["localhost", "127.0.0.1", "[::1]", "testserver"])

    @app.exception_handler(RequestValidationError)
    async def validation_error(request, exc):
        # Pydantic errors may include raw input values, including login passwords.
        return JSONResponse({"detail": "Invalid input. Check required fields and length limits."}, status_code=422)

    @app.middleware("http")
    async def security(request: Request, call_next):
        if request.method not in {"GET", "HEAD", "OPTIONS"}:
            origin = request.headers.get("origin")
            if origin and urlsplit(origin).netloc != request.headers.get("host"):
                return JSONResponse({"detail": "Cross-origin writes are not allowed."}, status_code=403)
            try:
                if int(request.headers.get("content-length", "0")) > 100000:
                    return JSONResponse({"detail": "Request too large."}, status_code=413)
            except ValueError:
                return JSONResponse({"detail": "Invalid request length."}, status_code=400)
        if request.url.path.startswith("/api/") and request.url.path not in {"/api/health", "/api/auth/config", "/api/auth/session", "/api/auth/setup", "/api/auth/login"}:
            if supabase.config()["mode"] == "supabase":
                token = request.headers.get("authorization", "").removeprefix("Bearer ")
                valid = await asyncio.to_thread(supabase.user, token)
            else:
                valid = auth.valid(request.cookies.get("career_session"))
            if not valid:
                return JSONResponse({"detail": "Sign in to continue."}, status_code=401)
        response = await call_next(request)
        response.headers["Cache-Control"] = "no-store" if request.url.path.startswith("/api/") else "no-cache"
        response.headers["X-Content-Type-Options"] = "nosniff"
        response.headers["Referrer-Policy"] = "no-referrer"
        response.headers["X-Frame-Options"] = "DENY"
        return response

    @app.get("/api/health")
    def health():
        return {"status": "ok", "mode": "local"}

    @app.get("/api/auth/session")
    def session(request: Request):
        if supabase.config()["mode"] == "supabase":
            identity = supabase.user(request.headers.get("authorization", "").removeprefix("Bearer "))
            return {"authenticated": bool(identity), "setup_required": False, "email": identity["email"] if identity else None}
        logged_in = auth.valid(request.cookies.get("career_session"))
        return {"authenticated": logged_in, "setup_required": auth.owner() is None,
                "email": auth.owner() if logged_in else None}

    @app.get("/api/auth/config")
    def auth_config():
        return supabase.config()

    def sign_in(body, response):
        token = auth.login(body.email, body.password)
        if not token:
            raise HTTPException(401, "Email or password is incorrect.")
        response.set_cookie("career_session", token, httponly=True, samesite="strict", max_age=43200, path="/")
        return {"authenticated": True, "email": auth.owner()}

    @app.post("/api/auth/setup")
    def setup(body: Login, response: Response):
        if supabase.config()["mode"] != "local":
            raise HTTPException(403, "Local registration is disabled when Supabase is configured.")
        if not auth.setup(body.email, body.password):
            raise HTTPException(409, "Owner account already exists. Sign in instead.")
        return sign_in(body, response)

    @app.post("/api/auth/login")
    def login(body: Login, response: Response, request: Request):
        if supabase.config()["mode"] != "local":
            raise HTTPException(403, "Sign in through Supabase.")
        peer = request.client.host
        with attempt_lock:
            recent = [t for t in attempts.get(peer, []) if t > time.time() - 900]
            if len(recent) >= 8:
                raise HTTPException(429, "Too many attempts. Try again in 15 minutes.")
            attempts[peer] = recent + [time.time()]
        result = sign_in(body, response)
        with attempt_lock:
            attempts.pop(peer, None)
        return result

    @app.post("/api/auth/logout")
    def logout(request: Request, response: Response):
        supabase.forget(request.headers.get("authorization", ""))
        auth.logout(request.cookies.get("career_session", ""))
        response.delete_cookie("career_session")
        return {"authenticated": False}

    @app.get("/api/providers")
    def providers():
        return statuses(root)

    @app.post("/api/providers/{provider}/check")
    def check_provider(provider: str):
        if not probe_lock.acquire(blocking=False):
            raise HTTPException(409, "Another provider check is running.")
        try:
            return probe(root, provider)
        except ValueError:
            raise HTTPException(404, "Unknown provider")
        finally:
            probe_lock.release()

    @app.get("/api/jobs")
    def jobs(q: str = Query("", max_length=200), hours: int = Query(48, ge=0, le=87600),
             basis: Literal["posted", "discovered"] = "posted", scope: Literal["all", "shortlist", "review", "blocked"] = "all",
             source: str = "", page: int = Query(1, ge=1), page_size: int = Query(30, ge=1, le=100)):
        return board(root, q, hours, basis, scope, source, page, page_size, index=job_index)

    @app.get("/api/scans/current")
    def scan_status():
        return scans.snapshot()

    @app.post("/api/scans")
    def start_scan(body: ScanRequest):
        try:
            return scans.start(body.company_limit)
        except ValueError as exc:
            raise HTTPException(409, str(exc))

    @app.post("/api/scans/cancel")
    def cancel_scan():
        return scans.cancel()

    @app.get("/api/intakes")
    def list_intakes():
        return intakes.list()

    @app.post("/api/intakes")
    def create_intake(body: Intake):
        return intakes.create(body.company, body.title, body.jd, body.mode, body.url)

    @app.get("/api/intakes/{identifier}")
    def get_intake(identifier: str):
        result = intakes.get(identifier)
        if result is None:
            raise HTTPException(404, "Intake not found.")
        return result

    dist = REPO / "web/dist"
    if dist.exists():
        app.mount("/", StaticFiles(directory=dist, html=True), name="web")
    return app


app = create_app(Path(os.environ.get("CAREER_OPS_ROOT", REPO)))
