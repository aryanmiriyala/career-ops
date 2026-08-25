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
    "Angular",
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
    "Jenkins",
    "Kafka",
    "Kubernetes",
    "LLM",
    "LLMs",
    "LangChain",
    "Linux",
    "Maven",
    "MongoDB",
    "MySQL",
    "Next.js",
    "Node.js",
    "Open Shift",
    "OpenAI",
    "OpenShift",
    "Oracle",
    "PostgreSQL",
    "PySpark",
    "Python",
    "RAG",
    "RBAC",
    "REST",
    "REST APIs",
    "React",
    "ReactJS",
    "S3",
    "SQL",
    "SSO",
    "Spark",
    "Spring Boot",
    "Springboot",
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
    "logging",
    "monitoring",
    "observability",
    "prompt engineering",
    "security",
    "testing",
    "unit tests",
]

JD_RESPONSIBILITY_TERMS = [
    "AI-powered tools",
    "API concepts",
    "application issues",
    "build and deployment tools",
    "content rights",
    "code reviews",
    "cross-functional teams",
    "data integration",
    "data layers",
    "data persistence",
    "deployment tools",
    "business requirement",
    "full-stack software applications",
    "Generative AI APIs",
    "controls",
    "failover",
    "front-end web application",
    "governance",
    "high-volume",
    "intelligent automation",
    "issue resolution",
    "Jenkins pipeline",
    "machine learning models",
    "maintainable",
    "messaging",
    "NoSQL",
    "object-oriented programming",
    "optimized for performance",
    "peer reviews",
    "performance tuning",
    "Product Owner",
    "production incidents",
    "product requirements",
    "requirements",
    "release engineering",
    "RESTful services",
    "risk",
    "scalable",
    "secure coding",
    "rights management",
    "service requests",
    "source control",
    "stakeholders",
    "supply chain",
    "system configurations",
    "testing and deployment",
    "UI",
    "user stories",
]

IMPORTANT_TERMS = sorted(set(TECH_TERMS + JD_RESPONSIBILITY_TERMS), key=lambda item: (item.lower(), item))

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
    "advance technological",
    "base salary",
    "disney entertainment",
    "disney entertainment espn",
    "disney media",
    "entertainment espn",
    "entertainment espn product",
    "espn product",
    "espn product technology",
    "employment company",
    "equal opportunity",
    "job description",
    "offer employment",
    "product technology",
    "salary range",
    "u.s. export",
    "works across",
}

REPEATED_PHRASE_ANCHOR_WORDS = {
    "ai",
    "api",
    "apis",
    "application",
    "applications",
    "automation",
    "build",
    "cloud",
    "content",
    "control",
    "data",
    "deployment",
    "engineering",
    "engineer",
    "incidents",
    "integration",
    "machine",
    "management",
    "production",
    "requirements",
    "requests",
    "reviews",
    "rights",
    "service",
    "software",
    "source",
    "supply",
    "testing",
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
        and any(word in REPEATED_PHRASE_ANCHOR_WORDS for word in phrase.split())
    ]


def extract_terms(jd_text: str, extra_terms: list[str]) -> list[str]:
    terms = {term for term in IMPORTANT_TERMS if contains_term(jd_text, term)}
    terms.update(term.strip() for term in extra_terms if term.strip())
    terms.update(extract_repeated_phrases(jd_text))
    deduped_terms: list[str] = []
    seen_normalized: set[str] = set()
    for term in sorted(terms, key=lambda item: (item.lower(), item)):
        normalized_term = term.lower()
        if normalized_term in seen_normalized:
            continue
        seen_normalized.add(normalized_term)
        deduped_terms.append(term)
    return deduped_terms


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Report exact keyword coverage for one application package.")
    parser.add_argument("application_dir", help="Path like application-packages/Company/Role")
    parser.add_argument("--resume", default="", help="Optional resume PDF/TEX path; defaults to resume.pdf then resume.tex")
    parser.add_argument("--term", action="append", default=[], help="Extra exact term to check; may be repeated")
    parser.add_argument(
        "--term-file",
        action="append",
        default=[],
        help="File containing extra exact terms, one per line; blank lines and # comments are ignored",
    )
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
    extra_terms = list(args.term)
    for term_file in args.term_file:
        term_file_path = Path(term_file)
        if not term_file_path.is_file():
            raise SystemExit(f"Missing term file: {term_file_path}")
        for line in term_file_path.read_text(encoding="utf-8", errors="replace").splitlines():
            term = line.strip()
            if term and not term.startswith("#"):
                extra_terms.append(term)

    terms = extract_terms(jd_text, extra_terms)

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
