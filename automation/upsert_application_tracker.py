#!/usr/bin/env python3
"""Append or update one row in operations/application-tracker.md.

The script reads the tracker internally so Codex does not need to load the full
Markdown table into model context for routine application-package creation.
"""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path


TRACKER_PATH = Path("operations/application-tracker.md")

FIELDS = [
    "Status",
    "Company",
    "Role",
    "Location",
    "Date Added",
    "Last Update",
    "Deadline",
    "Resume Path",
    "Cover Letter Path",
    "Job Link",
    "Referral Status",
    "Referral Target / Source",
    "Next Referral Follow-up",
    "Notes",
]


def clean_cell(value: str) -> str:
    return " ".join(value.replace("|", "/").split()) if value else "TBD"


def row_from_values(values: dict[str, str]) -> str:
    return "| " + " | ".join(clean_cell(values.get(field, "")) for field in FIELDS) + " |"


def split_row(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def find_table_bounds(lines: list[str]) -> tuple[int, int]:
    header_index = next(
        (index for index, line in enumerate(lines) if line.startswith("| Status | Company | Role |")),
        -1,
    )
    if header_index == -1:
        raise SystemExit("Could not find application tracker table header")

    separator_index = header_index + 1
    if separator_index >= len(lines) or not lines[separator_index].startswith("|---"):
        raise SystemExit("Could not find application tracker table separator")

    end_index = separator_index + 1
    while end_index < len(lines) and lines[end_index].startswith("|"):
        end_index += 1
    return separator_index + 1, end_index


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Append or update one application tracker row.")
    parser.add_argument("--tracker", default=str(TRACKER_PATH), help="Tracker Markdown path")
    parser.add_argument("--status", required=True)
    parser.add_argument("--company", required=True)
    parser.add_argument("--role", required=True)
    parser.add_argument("--location", default="TBD")
    parser.add_argument("--date-added", default="")
    parser.add_argument("--last-update", default="")
    parser.add_argument("--deadline", default="Not listed")
    parser.add_argument("--resume-path", default="TBD")
    parser.add_argument("--cover-letter-path", default="TBD")
    parser.add_argument("--job-link", default="Not provided")
    parser.add_argument("--referral-status", default="Not started")
    parser.add_argument("--referral-target", default="Not identified yet")
    parser.add_argument("--next-referral-follow-up", default="TBD")
    parser.add_argument("--notes", default="")
    parser.add_argument(
        "--insert-top",
        action=argparse.BooleanOptionalAction,
        default=True,
        help="Insert new rows at the top of the table after the separator",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    tracker = Path(args.tracker)
    today = date.today().isoformat()

    values = {
        "Status": args.status,
        "Company": args.company,
        "Role": args.role,
        "Location": args.location,
        "Date Added": args.date_added or today,
        "Last Update": args.last_update or today,
        "Deadline": args.deadline,
        "Resume Path": args.resume_path,
        "Cover Letter Path": args.cover_letter_path,
        "Job Link": args.job_link,
        "Referral Status": args.referral_status,
        "Referral Target / Source": args.referral_target,
        "Next Referral Follow-up": args.next_referral_follow_up,
        "Notes": args.notes,
    }

    lines = tracker.read_text(encoding="utf-8").splitlines()
    start, end = find_table_bounds(lines)

    target_company = args.company.casefold().strip()
    target_role = args.role.casefold().strip()
    new_row = row_from_values(values)

    for index in range(start, end):
        cells = split_row(lines[index])
        if len(cells) >= 3 and cells[1].casefold() == target_company and cells[2].casefold() == target_role:
            lines[index] = new_row
            tracker.write_text("\n".join(lines) + "\n", encoding="utf-8")
            print(f"UPDATED: {args.company} - {args.role}")
            return 0

    insert_index = start if args.insert_top else end
    lines.insert(insert_index, new_row)
    tracker.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"ADDED: {args.company} - {args.role}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
