"""Deterministic job description parsing - extracts requirements, skills, eligibility without LLM."""
from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from .generation_models import Requirement, Requirements


@dataclass
class ParsedJD:
    title: str
    company: str
    location: str
    required_skills: list[str]
    preferred_skills: list[str]
    responsibilities: list[str]
    domain_terms: list[str]
    eligibility_status: str  # 'no_explicit_blocker', 'uncertain', 'blocked'
    eligibility_quotes: list[str]
    eligibility_reason: str
    raw_text: str


# Visa/work authorization blocker patterns
BLOCKER_PATTERNS = [
    r"no\s+(?:visa|work\s+visa|employment\s+visa|sponsorship|H-?1B|immigration)\s+(?:sponsor|support|provide)",
    r"cannot\s+sponsor",
    r"unable\s+to\s+sponsor",
    r"does\s+not\s+sponsor",
    r"no\s+sponsorship",
    r"without\s+sponsorship",
    r"independent\s+work\s+authorization",
    r"authorized\s+to\s+work\s+for\s+any\s+employer",
    r"work\s+authorization\s+for\s+any\s+employer",
    r"U\.?S\.?\s+citizen\s+only",
    r"permanent\s+resident\s+only",
    r"green\s+card\s+required",
    r"must\s+be\s+a\s+U\.?S\.?\s+citizen",
    r"must\s+have\s+permanent\s+residency",
    r"clearance\s+required",
    r"security\s+clearance",
    r"no\s+CPT|no\s+OPT|no\s+STEM\s+OPT",
    r"cannot\s+hire\s+(?:international|F-?1|students?)",
]

SPONSORSHIP_AVAILABLE_PATTERNS = [
    r"visa\s+sponsorship\s+(?:available|provided|offered)",
    r"H-?1B\s+sponsor",
    r"will\s+sponsor",
    r"sponsor\s+(?:visa|H-?1B)",
    r"STEM\s+OPT\s+(?:eligible|supported|welcome)",
    r"E-?Verify\s+(?:participates?|eligible)",
    r"Form\s+I-983",
    r"OPT\s+(?:eligible|supported|welcome)",
    r"CPT\s+(?:eligible|supported)",
    r"international\s+students?\s+welcome",
]

# Common skill/tech terms to look for
SKILL_PATTERNS = {
    "languages": [
        r"\bPython\b", r"\bJava\b", r"\bJavaScript\b", r"\bTypeScript\b", r"\bC\+\+\b",
        r"\bC#\b", r"\bGo\b", r"\bRust\b", r"\bRuby\b", r"\bPHP\b", r"\bSwift\b",
        r"\bKotlin\b", r"\bScala\b", r"\bR\b", r"\bSQL\b", r"\bNoSQL\b",
    ],
    "frontend": [
        r"\bReact\b", r"\bNext\.js\b", r"\bAngular\b", r"\bVue\b", r"\bSvelte\b",
        r"\bHTML\b", r"\bCSS\b", r"\bTailwind\b", r"\bRedux\b", r"\bZustand\b",
        r"\bWebpack\b", r"\bVite\b", r"\bGraphQL\b", r"\bREST\b",
    ],
    "backend": [
        r"\bNode\.js\b", r"\bExpress\b", r"\bFastAPI\b", r"\bDjango\b", r"\bFlask\b",
        r"\bSpring\s+Boot\b", r"\bSpringBoot\b", r"\b\.NET\b", r"\bASP\.NET\b",
        r"\bMicroservices?\b", r"\bAPI\b", r"\bRESTful\b", r"\bgRPC\b",
    ],
    "cloud": [
        r"\bAWS\b", r"\bAzure\b", r"\bGCP\b", r"\bGoogle\s+Cloud\b",
        r"\bLambda\b", r"\bEC2\b", r"\bS3\b", r"\bRDS\b", r"\bDynamoDB\b",
        r"\bCloudFormation\b", r"\bTerraform\b", r"\bKubernetes\b", r"\bK8s\b",
        r"\bDocker\b", r"\bECS\b", r"\bEKS\b", r"\bCloudRun\b",
    ],
    "data": [
        r"\bPySpark\b", r"\bSpark\b", r"\bHadoop\b", r"\bKafka\b", r"\bAirflow\b",
        r"\bdbt\b", r"\bSnowflake\b", r"\bRedshift\b", r"\bBigQuery\b",
        r"\bPostgreSQL\b", r"\bMySQL\b", r"\bMongoDB\b", r"\bCassandra\b",
        r"\bRedis\b", r"\bElasticsearch\b", r"\bETL\b", r"\bELT\b",
    ],
    "ai_ml": [
        r"\bLLM\b", r"\bRAG\b", r"\bLangChain\b", r"\bLlamaIndex\b",
        r"\bOpenAI\b", r"\bAnthropic\b", r"\bClaude\b", r"\bGemini\b", r"\bMistral\b",
        r"\bPyTorch\b", r"\bTensorFlow\b", r"\bHugging\s+Face\b",
        r"\bMachine\s+Learning\b", r"\bDeep\s+Learning\b", r"\bNLP\b",
        r"\bComputer\s+Vision\b", r"\bGenerative\s+AI\b", r"\bAgent\b",
    ],
    "tools": [
        r"\bGit\b", r"\bGitHub\b", r"\bGitLab\b", r"\bCI/CD\b", r"\bJenkins\b",
        r"\bGitHub\s+Actions\b", r"\bDocker\b", r"\bKubernetes\b",
        r"\bLinux\b", r"\bBash\b", r"\bVim\b", r"\bVS\s+Code\b",
    ],
}

ALL_SKILL_PATTERNS = []
for cat_patterns in SKILL_PATTERNS.values():
    ALL_SKILL_PATTERNS.extend(cat_patterns)


def extract_title_company(jd_text: str) -> tuple[str, str]:
    """Extract job title and company from JD."""
    lines = jd_text.splitlines()
    title = "Unknown Role"
    company = "Unknown Company"

    # Look for common patterns in first 20 lines
    for line in lines[:20]:
        line = line.strip()
        if not line:
            continue
        # Title patterns
        if any(kw in line.lower() for kw in ["software engineer", "data engineer", "ai engineer",
                                                "full stack", "backend", "frontend", "ml engineer",
                                                "intern", "new grad", "entry level"]):
            if len(line) < 100 and not line.endswith(":"):
                title = line
                break

    # Company often appears near title or in "About [Company]" section
    for line in lines[:30]:
        line = line.strip()
        if line.lower().startswith("about ") and len(line) < 80:
            company = line[6:].strip()
            break
        if line.lower().startswith("company:") or line.lower().startswith("employer:"):
            company = line.split(":", 1)[1].strip()
            break

    return title, company


def extract_location(jd_text: str) -> str:
    """Extract location from JD."""
    # Look for location patterns
    patterns = [
        r"(?:location|based in|office in)\s*[:\-]\s*([^\n]+)",
        r"\b(Remote|Hybrid|On-site|Onsite)\b",
        r"\b[A-Z][a-z]+,\s*[A-Z]{2}\b",  # City, ST
        r"\bUnited States\b", r"\bUSA\b", r"\bU\.S\.\b",
    ]

    for pattern in patterns:
        match = re.search(pattern, jd_text, re.IGNORECASE)
        if match:
            return match.group(1).strip() if match.groups() else match.group(0)

    return "Not specified"


def extract_skills(jd_text: str) -> tuple[list[str], list[str]]:
    """Extract required and preferred skills from JD."""
    text_lower = jd_text.lower()
    found_skills = set()

    for pattern in ALL_SKILL_PATTERNS:
        if re.search(pattern, jd_text, re.IGNORECASE):
            # Normalize the match
            match = re.search(pattern, jd_text, re.IGNORECASE)
            if match:
                skill = match.group(0)
                # Clean up
                skill = skill.strip(".,;:()[]{}")
                found_skills.add(skill)

    # Separate required vs preferred based on context
    required = []
    preferred = []

    for skill in found_skills:
        # Check context around skill
        skill_pos = jd_text.lower().find(skill.lower())
        context_start = max(0, skill_pos - 100)
        context_end = min(len(jd_text), skill_pos + 100)
        context = jd_text[context_start:context_end].lower()

        required_indicators = ["required", "must have", "must-have", "essential", "mandatory", "need"]
        preferred_indicators = ["preferred", "nice to have", "nice-to-have", "plus", "bonus", "desired", "ideal"]

        is_required = any(ind in context for ind in required_indicators)
        is_preferred = any(ind in context for ind in preferred_indicators)

        if is_required and not is_preferred:
            required.append(skill)
        elif is_preferred and not is_required:
            preferred.append(skill)
        else:
            # Default to required if mentioned in requirements section
            required.append(skill)

    return required, preferred


def extract_responsibilities(jd_text: str) -> list[str]:
    """Extract responsibilities from JD."""
    responsibilities = []

    # Look for responsibility sections
    resp_patterns = [
        r"(?:responsibilities|duties|what you'll do|what you will do|role overview|key responsibilities)\s*[:\n](.*?)(?:\n\n|\n[A-Z][a-z]+:|\Z)",
        r"(?:you will|you'll be|the role involves|this role)\s+(.*?)(?:\.\s+[A-Z]|\n\n|\Z)",
    ]

    for pattern in resp_patterns:
        matches = re.findall(pattern, jd_text, re.IGNORECASE | re.DOTALL)
        for match in matches:
            # Split into individual responsibilities
            items = re.split(r"[\n•\-\*]\s*|\.\s+", match)
            for item in items:
                item = item.strip(" .\n\t•-*")
                if len(item) > 20 and len(item) < 500:
                    responsibilities.append(item)

    # Deduplicate
    seen = set()
    unique = []
    for r in responsibilities:
        key = r.lower()[:50]
        if key not in seen:
            seen.add(key)
            unique.append(r)

    return unique[:15]  # Limit


def extract_domain_terms(jd_text: str) -> list[str]:
    """Extract domain-specific terms from JD."""
    domain_keywords = [
        "insurance", "healthcare", "fintech", "banking", "payments", "e-commerce",
        "manufacturing", "logistics", "supply chain", "retail", "education",
        "cybersecurity", "security", "compliance", "audit", "risk",
        "machine learning", "artificial intelligence", "data science", "analytics",
        "devops", "site reliability", "platform engineering", "infrastructure",
        "mobile", "ios", "android", "embedded", "iot", "real-time",
        "streaming", "batch processing", "data warehouse", "data lake",
        "microservices", "distributed systems", "high availability", "scalability",
    ]

    found = []
    text_lower = jd_text.lower()
    for term in domain_keywords:
        if term in text_lower:
            found.append(term)

    return found


def extract_eligibility(jd_text: str) -> tuple[str, list[str], str]:
    """Extract visa/work authorization eligibility from JD."""
    quotes = []
    text_lower = jd_text.lower()

    # Check for blockers
    for pattern in BLOCKER_PATTERNS:
        match = re.search(pattern, jd_text, re.IGNORECASE)
        if match:
            quotes.append(match.group(0))
            return "blocked", quotes, f"Explicit blocker found: {match.group(0)}"

    # Check for sponsorship signals
    sponsorship_signals = []
    for pattern in SPONSORSHIP_AVAILABLE_PATTERNS:
        match = re.search(pattern, jd_text, re.IGNORECASE)
        if match:
            sponsorship_signals.append(match.group(0))

    if sponsorship_signals:
        quotes.extend(sponsorship_signals)
        return "no_explicit_blocker", quotes, f"Sponsorship signals found: {'; '.join(sponsorship_signals)}"

    # Check for any work authorization mention
    auth_mentions = re.findall(r"(?:work\s+authorization|visa|sponsorship|OPT|CPT|STEM\s+OPT|E-?Verify|I-983)", jd_text, re.IGNORECASE)
    if auth_mentions:
        quotes.extend(auth_mentions[:5])
        return "uncertain", quotes, f"Work authorization mentioned but unclear: {'; '.join(set(auth_mentions))}"

    return "uncertain", [], "No explicit work authorization language found in posting"


def parse_jd(jd_text: str, company: str = "", title: str = "") -> ParsedJD:
    """Parse a job description into structured data."""
    if not title:
        title, extracted_company = extract_title_company(jd_text)
        if not company and extracted_company != "Unknown Company":
            company = extracted_company
    if not company:
        _, company = extract_title_company(jd_text)

    location = extract_location(jd_text)
    required_skills, preferred_skills = extract_skills(jd_text)
    responsibilities = extract_responsibilities(jd_text)
    domain_terms = extract_domain_terms(jd_text)
    eligibility_status, eligibility_quotes, eligibility_reason = extract_eligibility(jd_text)

    return ParsedJD(
        title=title,
        company=company,
        location=location,
        required_skills=required_skills,
        preferred_skills=preferred_skills,
        responsibilities=responsibilities,
        domain_terms=domain_terms,
        eligibility_status=eligibility_status,
        eligibility_quotes=eligibility_quotes,
        eligibility_reason=eligibility_reason,
        raw_text=jd_text,
    )


def parsed_jd_to_requirements(parsed: ParsedJD) -> Requirements:
    """Convert ParsedJD to Requirements model for the pipeline."""
    requirements = []
    req_id = 1

    # Required skills
    for skill in parsed.required_skills:
        requirements.append(Requirement(
            id=f"R{req_id}",
            term=skill,
            quote=skill,
            priority="required",
        ))
        req_id += 1

    # Preferred skills
    for skill in parsed.preferred_skills:
        requirements.append(Requirement(
            id=f"R{req_id}",
            term=skill,
            quote=skill,
            priority="preferred",
        ))
        req_id += 1

    # Responsibilities
    for resp in parsed.responsibilities:
        # Extract key terms from responsibility
        terms = re.findall(r"\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b", resp)
        for term in terms[:3]:  # Top 3 terms per responsibility
            if len(term) > 3:
                requirements.append(Requirement(
                    id=f"R{req_id}",
                    term=term,
                    quote=resp[:200],
                    priority="responsibility",
                ))
                req_id += 1

    # Domain terms
    for term in parsed.domain_terms:
        requirements.append(Requirement(
            id=f"R{req_id}",
            term=term,
            quote=term,
            priority="responsibility",
        ))
        req_id += 1

    # Determine lane from title
    title_lower = parsed.title.lower()
    if any(kw in title_lower for kw in ["data engineer", "data engineering"]):
        lane = "Data engineering"
    elif any(kw in title_lower for kw in ["ai engineer", "ml engineer", "machine learning", "agent"]):
        lane = "Applied AI / Agentic systems"
    elif any(kw in title_lower for kw in ["full stack", "fullstack", "software engineer", "backend", "frontend"]):
        lane = "Full-stack / Software engineering"
    elif any(kw in title_lower for kw in ["security", "devops", "platform", "infrastructure", "sre"]):
        lane = "Cloud / Platform / Security"
    elif any(kw in title_lower for kw in ["analyst", "business analyst", "product analyst", "operations"]):
        lane = "Analyst / Business operations"
    else:
        lane = "Software engineering"

    return Requirements(
        lane=lane,
        title=parsed.title,
        requirements=requirements,
        eligibility=parsed.eligibility_status,
        eligibility_quotes=parsed.eligibility_quotes,
        eligibility_reason=parsed.eligibility_reason,
    )