"""Start the loopback-only workspace without cloud authentication dependencies."""

import argparse
import os
from pathlib import Path
import socket
import subprocess
import sys


def main():
    root = Path(__file__).resolve().parents[1]
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--port", type=int, default=8765)
    args = parser.parse_args()
    if not 1024 <= args.port <= 65535:
        parser.error("Port must be between 1024 and 65535.")
    python = root / ".venv/bin/python"
    if not python.exists():
        parser.error("Create .venv and install requirements-workspace.txt first.")
    if not (root / "web/dist/index.html").exists():
        parser.error("Build the frontend first: cd web && bun install --frozen-lockfile && bun run build")
    for port in range(args.port, min(args.port + 20, 65536)):
        with socket.socket() as sock:
            try:
                sock.bind(("127.0.0.1", port))
            except OSError:
                continue
        break
    else:
        parser.error("No available local port. Choose another with --port.")
    env = {**os.environ, "CAREER_OPS_LOCAL_ONLY": "1", "CAREER_OPS_ROOT": str(root)}
    print(f"Career Ops: http://127.0.0.1:{port} (local account; no Supabase required)", flush=True)
    return subprocess.call([str(python), "-m", "uvicorn", "workspace_app.api:app", "--host", "127.0.0.1", "--port", str(port)], cwd=root, env=env)


if __name__ == "__main__":
    sys.exit(main())
