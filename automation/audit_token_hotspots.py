#!/usr/bin/env python3
"""Summarize likely token-heavy source areas without printing large files."""

from __future__ import annotations

import argparse
import re
from collections import Counter
from pathlib import Path


DEFAULT_PATHS = [
    "AGENTS.md",
    "profile",
    "templates",
    "automation",
    "master-documents",
    "operations",
    "job-search",
    "application-packages",
]

TEXT_SUFFIXES = {
    ".csv",
    ".json",
    ".md",
    ".py",
    ".tex",
    ".txt",
    ".yaml",
    ".yml",
}


def word_count(path: Path) -> int:
    text = path.read_text(encoding="utf-8", errors="replace")
    return len(re.findall(r"\S+", text))


def iter_text_files(paths: list[Path]) -> list[Path]:
    files: list[Path] = []
    for path in paths:
        if path.is_file() and path.suffix.lower() in TEXT_SUFFIXES:
            files.append(path)
        elif path.is_dir():
            files.extend(
                child
                for child in path.rglob("*")
                if child.is_file()
                and child.suffix.lower() in TEXT_SUFFIXES
                and ".git" not in child.parts
            )
    return sorted(set(files))


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Report top token hotspots by file and directory without dumping file contents."
    )
    parser.add_argument("paths", nargs="*", default=DEFAULT_PATHS)
    parser.add_argument("--top", type=int, default=25)
    args = parser.parse_args()

    paths = [Path(path) for path in args.paths]
    counts: list[tuple[int, Path]] = []
    for file_path in iter_text_files(paths):
        try:
            counts.append((word_count(file_path), file_path))
        except OSError:
            continue

    by_dir: Counter[str] = Counter()
    for count, file_path in counts:
        top_dir = file_path.parts[0] if len(file_path.parts) > 1 else file_path.name
        by_dir[top_dir] += count

    total_words = sum(count for count, _ in counts)
    print("# Token Hotspot Audit")
    print()
    print(f"Files scanned: {len(counts)}")
    print(f"Total words: {total_words}")
    print()
    print("## Largest Directories")
    for directory, count in by_dir.most_common(12):
        print(f"- {directory}: {count} words")
    print()
    print("## Largest Files")
    for count, file_path in sorted(counts, reverse=True)[: args.top]:
        print(f"- {count} words: {file_path}")
    print()
    print("Use this report to choose targeted `rg`/`sed` reads instead of broad file dumps.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
