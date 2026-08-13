#!/usr/bin/env python3
"""Deterministic keyword coverage helper for application packages.

This is not an ATS score. It reports exact-term coverage so the model can use a
small, reproducible summary during the alignment pass instead of rereading large
source files.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
from collections import Counter
from pathlib import Path


TECH_TERMS = [
    "AI",
    "API",
    "APIs",
    "AWS",
    "AWS Glue",
    "AWS Lambda",
    "Azure",
    "C",
    "C#",
    "C++",
    "CI/CD",
    "CSS",
    "Databricks",
    "Docker",
    "DynamoDB",
    "E-Verify",
    "ETL",
    "Express",
    "FastAPI",
    "Firebase",
    "Git",
    "GraphQL",
    "HTML",
    "IAM",
    "Java",
    "JavaScript",
    "Kafka",
    "Kubernetes",
    "LLM",
    "LLMs",
    "LangChain",
    "Linux",
    "MongoDB",
    "MySQL",
    "Next.js",
    "Node.js",
    "OpenAI",
    "Oracle",
    "PostgreSQL",
    "PySpark",
    "Python",
    "RAG",
    "RBAC",
    "REST",
    "REST APIs",
    "React",
    "S3",
    "SQL",
    "SSO",
    "Spark",
    "Supabase",
    "TypeScript",
    "Vercel",
    "authentication",
    "authorization",
    "cloud",
    "data engineering",
    "data pipelines",
    "data structures",
    "debugging",
    "distributed systems",
    "machine learning",
    "monitoring",
    "observability",
    "prompt engineering",
    "security",
    "testing",
    "unit tests",
]

STOPWORDS = {
    "and",
    "are",
    "for",
    "from",
    "have",
    "into",
    "not",
    "our",
    "that",
    "the",
    "their",
    "this",
    "with",
    "will",
    "you",
    "your",
}

EXCLUDED_PHRASES = {
    "base salary",
    "employment company",
    "equal opportunity",
    "job description",
    "offer employment",
    "salary range",
    "u.s. export",
}


def read_text(path: Path) -> str:
    if path.suffix.lower() == ".pdf" and shutil.which("pdftotext"):
        proc = subprocess.run(["pdftotext", str(path), "-"], text=True, capture_output=True, check=False)
        if proc.returncode == 0:
            return proc.stdout
    return path.read_text(encoding="utf-8", errors="replace")


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def contains_term(text: str, term: str) -> bool:
    escaped = re.escape(term)
    if re.fullmatch(r"[A-Za-z0-9+#./-]+", term):
        pattern = rf"(?<![A-Za-z0-9+#./-]){escaped}(?![A-Za-z0-9+#./-])"
    else:
        pattern = escaped
    return re.search(pattern, text, re.IGNORECASE) is not None


def extract_repeated_phrases(text: str) -> list[str]:
    words = [
        word.lower()
        for word in re.findall(r"[A-Za-z][A-Za-z+#./-]{2,}", text)
        if word.lower() not in STOPWORDS
    ]
    phrases: Counter[str] = Counter()
    for size in (2, 3):
        for index in range(0, max(0, len(words) - size + 1)):
            phrase_words = words[index : index + size]
            if any(word in STOPWORDS for word in phrase_words):
                continue
            phrases[" ".join(phrase_words)] += 1
    return [
        phrase
        for phrase, count in phrases.most_common(30)
        if count >= 2 and phrase not in EXCLUDED_PHRASES
    ]


def extract_terms(jd_text: str, extra_terms: list[str]) -> list[str]:
    terms = {term for term in TECH_TERMS if contains_term(jd_text, term)}
    terms.update(term.strip() for term in extra_terms if term.strip())
    terms.update(extract_repeated_phrases(jd_text))
    return sorted(terms, key=lambda item: (item.lower(), item))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Report exact keyword coverage for one application package.")
    parser.add_argument("application_dir", help="Path like application-packages/Company/Role")
    parser.add_argument("--resume", default="", help="Optional resume PDF/TEX path; defaults to resume.pdf then resume.tex")
    parser.add_argument("--term", action="append", default=[], help="Extra exact term to check; may be repeated")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    app_dir = Path(args.application_dir)
    jd_path = app_dir / "job-description.md"
    if not jd_path.is_file():
        raise SystemExit(f"Missing job-description.md in {app_dir}")

    if args.resume:
        resume_path = Path(args.resume)
    elif (app_dir / "resume.pdf").is_file():
        resume_path = app_dir / "resume.pdf"
    else:
        resume_path = app_dir / "resume.tex"

    if not resume_path.is_file():
        raise SystemExit(f"Missing resume artifact: {resume_path}")

    jd_text = normalize(read_text(jd_path))
    resume_text = normalize(read_text(resume_path))
    terms = extract_terms(jd_text, args.term)

    found = [term for term in terms if contains_term(resume_text, term)]
    missing = [term for term in terms if term not in found]

    print("# Keyword Coverage Report")
    print()
    print(f"Application: {app_dir}")
    print(f"Resume source: {resume_path}")
    print(f"JD terms checked: {len(terms)}")
    print(f"Found in resume: {len(found)}")
    print(f"Missing from resume: {len(missing)}")
    print()
    print("## Found")
    for term in found:
        print(f"- {term}")
    print()
    print("## Missing")
    for term in missing:
        print(f"- {term}")
    print()
    print("Note: This is exact-term coverage only, not an ATS score or employer decision predictor.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
