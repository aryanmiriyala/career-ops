"""Credentials stay inside the transport; public diagnostics never contain values."""

import os
import time
from pathlib import Path

import httpx
from dotenv import dotenv_values


PROVIDERS = {
    "openrouter": ("OpenRouter", ("OPENROUTER_API_KEY", "OPEN_ROUTER_KEY"), "https://openrouter.ai/api/v1/key"),
    "groq": ("Groq", ("GROQ_API_KEY",), "https://api.groq.com/openai/v1/models"),
    "gemini": ("Gemini", ("GEMINI_API_KEY", "GOOGLE_API_KEY"), "https://generativelanguage.googleapis.com/v1beta/models"),
    "zai": ("Z.ai", ("ZAI_API_KEY", "ZAI_KEY"), "https://api.z.ai/api/paas/v4/chat/completions"),
    "opencode": ("OpenCode Zen", ("OPENCODE_API_KEY",), "https://opencode.ai/zen/v1/models"),
    "mistral": ("Mistral", ("MISTRAL_API_KEY",), "https://api.mistral.ai/v1/models"),
    "featherless": ("Featherless", ("FEATHERLESS_API_KEY",), "https://api.featherless.ai/v1/models"),
}


def credentials(root: Path) -> dict:
    return {**dotenv_values(root / ".env", interpolate=False), **os.environ}


def statuses(root: Path) -> dict:
    values = credentials(root)
    rows = []
    for key, (name, aliases, _) in PROVIDERS.items():
        rows.append({"id": key, "name": name, "configured": any(bool(values.get(a)) for a in aliases),
                     "variables": list(aliases), "check_kind": "synthetic_free_inference" if key == "zai" else "connection"})
    return {"providers": rows, "langfuse_configured": all([
        values.get("LANGFUSE_PUBLIC_KEY"), values.get("LANGFUSE_SECRET_KEY"),
        values.get("LANGFUSE_HOST") or values.get("LANGFUSE_BASE_URL")]),
        "langfuse_connected": False, "generation_enabled": False}


def probe(root: Path, provider: str, client=None) -> dict:
    if provider not in PROVIDERS:
        raise ValueError("Unknown provider")
    _, aliases, url = PROVIDERS[provider]
    values = credentials(root)
    key = next((values[a] for a in aliases if values.get(a)), None)
    if not key:
        return {"status": "missing_key", "message": "No key configured."}
    started = time.monotonic()
    headers = {"Authorization": f"Bearer {key}"}
    if provider == "gemini":
        headers = {"x-goog-api-key": key}
    owned = client is None
    client = client or httpx.Client(timeout=30, follow_redirects=False)
    try:
        if provider == "zai":
            response = client.post(url, headers=headers, json={
                "model": "glm-4.7-flash", "max_tokens": 32,
                "thinking": {"type": "disabled"},
                "messages": [{"role": "user", "content": "Connection test with synthetic data. Reply with OK."}],
            })
        else:
            response = client.get(url, headers=headers)
        result = {"http_status": response.status_code, "latency_ms": round((time.monotonic() - started) * 1000)}
        if response.status_code != 200:
            return {**result, "status": "failed", "message": {
                401: "Credentials rejected.", 403: "Access denied.", 402: "Provider requires credits.",
                429: "Rate limited. No retry or paid fallback was made."
            }.get(response.status_code, "Provider request failed. No retry was made.")}
        result.update(status="reachable", message="Endpoint reachable. This does not establish generation access or free quota.")
        if provider == "zai":
            body = response.json()
            choices = body.get("choices", [])
            if not choices or not choices[0].get("message", {}).get("content"):
                return {**result, "status": "failed", "message": "Provider returned no usable completion."}
            usage = body.get("usage", {})
            result.update(status="verified", message="Free-model synthetic completion succeeded.",
                          model="glm-4.7-flash", usage={k: usage[k] for k in ("prompt_tokens", "completion_tokens", "total_tokens") if isinstance(usage.get(k), int)})
        return result
    except (httpx.HTTPError, ValueError, TypeError, KeyError, IndexError):
        return {"status": "failed", "message": "Connection or response error. Provider details omitted to protect credentials."}
    finally:
        if owned:
            client.close()
