#!/usr/bin/env python3
"""Validate a standalone one-page resume PDF for parser safety and page fill."""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


MAX_UNUSED_BOTTOM_POINTS = 24.0
WARN_UNUSED_BOTTOM_POINTS = 20.0
MAX_RESUME_PARSE_BYTES = int(2.5 * 1024 * 1024)
REQUIRED_TEXT_MARKERS = [
    "Aryan Miriyala",
    "aryanmiriyala@gmail.com",
    "Education",
    "Experience",
    "Technical Skills",
]


def run_command(command: list[str]) -> tuple[int, str, str]:
    proc = subprocess.run(command, text=True, capture_output=True, check=False)
    return proc.returncode, proc.stdout, proc.stderr


def local_name(tag: str) -> str:
    return tag.rsplit("}", 1)[-1]


def check_pdf(path: Path, errors: list[str], warnings: list[str]) -> None:
    if not path.is_file():
        errors.append(f"resume PDF does not exist: {path}")
        return

    if path.stat().st_size > MAX_RESUME_PARSE_BYTES:
        errors.append("resume PDF exceeds the conservative 2.5 MB ATS parser-size target")

    if not shutil.which("pdfinfo"):
        warnings.append("pdfinfo not found; skipped page-count validation")
    else:
        code, stdout, stderr = run_command(["pdfinfo", str(path)])
        if code != 0:
            errors.append(f"pdfinfo failed: {stderr.strip()}")
        else:
            match = re.search(r"^Pages:\s+(\d+)", stdout, re.MULTILINE)
            if not match:
                errors.append("could not determine PDF page count")
            elif int(match.group(1)) != 1:
                errors.append(f"resume PDF must be exactly 1 page; found {match.group(1)}")

    if not shutil.which("pdftotext"):
        warnings.append("pdftotext not found; skipped text extraction and page-utilization checks")
        return

    code, stdout, stderr = run_command(["pdftotext", str(path), "-"])
    if code != 0:
        errors.append(f"pdftotext failed: {stderr.strip()}")
    else:
        for marker in REQUIRED_TEXT_MARKERS:
            if marker not in stdout:
                errors.append(f"resume PDF text missing expected marker: {marker}")

    code, stdout, stderr = run_command(["pdftotext", "-bbox", str(path), "-"])
    if code != 0:
        warnings.append(f"pdftotext -bbox failed; skipped page-utilization check: {stderr.strip()}")
        return

    try:
        root = ET.fromstring(stdout)
    except ET.ParseError as exc:
        warnings.append(f"could not parse pdftotext -bbox output; skipped page-utilization check: {exc}")
        return

    page = next((element for element in root.iter() if local_name(element.tag) == "page"), None)
    if page is None:
        warnings.append("pdftotext -bbox output had no page node; skipped page-utilization check")
        return

    try:
        page_height = float(page.attrib["height"])
    except (KeyError, ValueError):
        warnings.append("pdftotext -bbox output had no usable page height; skipped page-utilization check")
        return

    max_y = 0.0
    for word in page.iter():
        if local_name(word.tag) != "word":
            continue
        try:
            max_y = max(max_y, float(word.attrib["yMax"]))
        except (KeyError, ValueError):
            continue

    if max_y <= 0:
        warnings.append("pdftotext -bbox output had no word positions; skipped page-utilization check")
        return

    unused_bottom = page_height - max_y
    if unused_bottom > MAX_UNUSED_BOTTOM_POINTS:
        errors.append(
            "resume PDF appears underfilled: "
            f"{unused_bottom:.1f}pt ({unused_bottom / 72:.2f}in) of unused bottom space"
        )
    elif unused_bottom > WARN_UNUSED_BOTTOM_POINTS:
        warnings.append(
            "resume PDF is close to the bottom-space limit: "
            f"{unused_bottom:.1f}pt ({unused_bottom / 72:.2f}in) unused"
        )


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a standalone one-page resume PDF.")
    parser.add_argument("resume_pdf", help="Path to a one-page resume PDF")
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []
    path = Path(args.resume_pdf)
    check_pdf(path, errors, warnings)

    for warning in warnings:
        print(f"WARN: {warning}")

    if errors:
        print(f"FAIL: {path}")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"PASS: {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
