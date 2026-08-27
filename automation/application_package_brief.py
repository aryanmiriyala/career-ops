#!/usr/bin/env python3
"""Compact application-package summary for low-token audits.

Use this before opening full package files during Existing-Package Audit or
small Patch work. It reports artifact status, default keyword coverage, and
optional exact-term coverage across submitted-facing text.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
from pathlib import Path


SUBMITTED_TEXT_FILES = (
    "resume.tex",
    "cover-letter.md",
    "application-questions.md",
    "application-answers.md",
)

PDF_FILES = ("resume.pdf", "cover-letter.pdf")


def run_command(command: list[str]) -> tuple[int, str]:
    proc = subprocess.run(command, text=True, capture_output=True, check=False)
    output = proc.stdout.strip()
    if proc.returncode != 0 and proc.stderr.strip():
        output = f"{output}\n{proc.stderr.strip()}".strip()
    return proc.returncode, output


def read_text(path: Path) -> str:
    if path.suffix.lower() == ".pdf" and shutil.which("pdftotext"):
        code, output = run_command(["pdftotext", str(path), "-"])
        if code == 0:
            return output
    if path.is_file():
        return path.read_text(encoding="utf-8", errors="replace")
    return ""


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().lower()


def contains_term(text: str, term: str) -> bool:
    return normalize(term) in text


def pdf_pages(path: Path) -> str:
    if not path.is_file():
        return "missing"
    if not shutil.which("pdfinfo"):
        return "present"
    code, output = run_command(["pdfinfo", str(path)])
    if code != 0:
        return "present, pdfinfo failed"
    match = re.search(r"^Pages:\s*(\d+)", output, re.MULTILINE)
    if not match:
        return "present, page count unknown"
    return f"{match.group(1)} page(s), {path.stat().st_size} bytes"


def load_terms(args: argparse.Namespace) -> list[str]:
    terms = list(args.term)
    if args.term_file:
        terms.extend(
            line.strip()
            for line in args.term_file.read_text(encoding="utf-8", errors="replace").splitlines()
            if line.strip() and not line.lstrip().startswith("#")
        )
    return sorted(dict.fromkeys(terms), key=str.lower)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("package_dir", type=Path)
    parser.add_argument("--term", action="append", default=[], help="Exact term to check")
    parser.add_argument("--term-file", type=Path, help="One exact term per line")
    parser.add_argument(
        "--skip-default-analyzer",
        action="store_true",
        help="Skip automation/analyze_application_keywords.py",
    )
    args = parser.parse_args()

    app_dir = args.package_dir
    if not app_dir.is_dir():
        raise SystemExit(f"Package directory not found: {app_dir}")

    print(f"# Application Package Brief\n")
    print(f"Package: {app_dir}")

    print("\n## Artifact Status")
    for name in ("job-description.md", "tailoring-notes.md", *SUBMITTED_TEXT_FILES):
        path = app_dir / name
        status = f"present, {path.stat().st_size} bytes" if path.is_file() else "missing"
        print(f"- {name}: {status}")
    for name in PDF_FILES:
        print(f"- {name}: {pdf_pages(app_dir / name)}")

    if not args.skip_default_analyzer:
        analyzer = Path(__file__).with_name("analyze_application_keywords.py")
        if analyzer.is_file():
            print("\n## Default Keyword Analyzer")
            code, output = run_command(["python3", str(analyzer), str(app_dir)])
            print(output if output else f"Analyzer exited with code {code}")

    terms = load_terms(args)
    if terms:
        text_by_source = {
            name: normalize(read_text(app_dir / name))
            for name in (*PDF_FILES, "cover-letter.md", "application-questions.md", "application-answers.md")
            if (app_dir / name).is_file()
        }
        combined_text = " ".join(text_by_source.values())

        print("\n## Requested Exact Terms")
        for term in terms:
            sources = [name for name, text in text_by_source.items() if contains_term(text, term)]
            status = ", ".join(sources) if sources else "missing"
            print(f"- {term}: {status}")
        found = sum(1 for term in terms if contains_term(combined_text, term))
        print(f"\nRequested-term coverage: {found}/{len(terms)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
