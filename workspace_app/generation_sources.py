"""Bounded requirement-aware retrieval from canonical sources, never old packages."""
import re
from pathlib import Path
from typing import Any

from .core import digest, tokens
from .bm25_retrieval import build_bm25_index, retrieve_bm25

POLICY_PATHS = ['AGENTS.md', 'profile/ats-recruiter-resume-guide.md', 'profile/resume-targeting-guide.md',
                'profile/cover-letter-guide.md', 'templates/canonical-resume.tex',
                'templates/canonical-visual-system.md', 'templates/tailoring-notes-template.md',
                'templates/canonical-cover-letter.md', 'templates/reusable-application-prompt.md']
SOURCE_PATHS = ['profile/evidence-index.md', 'profile/experience-master.md', 'profile/projects-master.md',
                'profile/skills-master.md', 'profile/bullet-bank.md',
                'master-documents/master-resume/resume.tex', 'master-documents/master-resume/resume-expanded.tex']


# Module-level cache for BM25 index
_bm25_index_cache: dict[str, Any] = {}


def snapshot(root):
    paths = POLICY_PATHS + SOURCE_PATHS
    return {p: digest((root / p).read_text()) for p in paths if (root / p).is_file()}


def source_chunks(root):
    chunks = []
    for name in SOURCE_PATHS:
        path = root / name
        if not path.is_file() or path.is_symlink():
            continue
        content = path.read_text()
        heading, buffer, start = '', [], 1
        def flush():
            if buffer:
                text = '\n'.join(buffer).strip()
                if text:
                    chunks.append({'id': digest(name + ':' + str(start) + ':' + text)[:20],
                                   'source': name, 'line': start, 'heading': heading, 'text': text,
                                   'source_hash': digest(content)})
        for n, line in enumerate(content.splitlines(), 1):
            if line.startswith('#'):
                flush()
                heading, buffer, start = line.lstrip('# '), [], n + 1
            elif len('\n'.join(buffer)) > 1600 or (not line.strip() and buffer):
                flush()
                buffer, start = ([line] if line.strip() else []), n
            else:
                if not buffer:
                    start = n
                buffer.append(line)
        flush()
    return chunks


def get_bm25_index(root: Path):
    """Get or build BM25 index, cached by source snapshot hash."""
    snap = snapshot(root)
    snap_hash = digest(str(sorted(snap.items())))
    if snap_hash not in _bm25_index_cache:
        _bm25_index_cache[snap_hash] = build_bm25_index(root)
    return _bm25_index_cache[snap_hash]


def retrieve(root, requirements, max_chars=35000):
    """Retrieve evidence using BM25 ranking (replaces lexical overlap)."""
    index = get_bm25_index(root)
    return retrieve_bm25(root, requirements, index, max_chars=max_chars)


def validate_requirements(requirements, jd):
    normalize = lambda text: ' '.join(text.casefold().split())
    ids = [r.id for r in requirements.requirements]
    if len(ids) != len(set(ids)):
        raise ValueError('Duplicate requirement IDs')
    for req in requirements.requirements:
        if normalize(req.quote) not in normalize(jd) or normalize(req.term) not in normalize(jd):
            raise ValueError('Requirement term or quotation was not found in the full JD')
    for quote in requirements.eligibility_quotes:
        if normalize(quote) not in normalize(jd):
            raise ValueError('Eligibility quotation was not found in the full JD')
    if requirements.eligibility == 'blocked' and not requirements.eligibility_quotes:
        raise ValueError('Eligibility blocker needs a source quotation')


def grounding_checks(resume, letter, evidence):
    known = {e['id']: e for e in evidence['evidence']}
    errors = []
    claims = list(resume.summary) + list(resume.skills) + list(letter.paragraphs)
    for entry in resume.experience + resume.projects:
        claims.extend(entry.bullets)
        if any(e not in known for e in entry.evidence_ids):
            errors.append('Unknown entry evidence ID: ' + entry.name)
            continue
        source = ' '.join(known[e]['heading'] + ' ' + known[e]['text'] for e in entry.evidence_ids).casefold()
        for label, value in [('name', entry.name), ('title', entry.title), ('dates', entry.dates), ('location', entry.location)]:
            if value and ' '.join(value.casefold().split()) not in ' '.join(source.split()):
                errors.append(f'Unverified entry {label}: {value}')
    bullet_texts = [claim.text.casefold().strip() for claim in claims]
    if len(bullet_texts) != len(set(bullet_texts)):
        errors.append('Duplicate submitted claims are not allowed')
    for claim in claims:
        if any(e not in known for e in claim.evidence_ids):
            errors.append('Unknown claim evidence ID: ' + claim.text[:80])
            continue
        source = ' '.join(known[e]['text'] for e in claim.evidence_ids)
        numbers = re.findall(r'\b\d[\d,]*(?:\.\d+)?\s*(?:%|\+|TB|GB|MB)?', claim.text)
        for number in numbers:
            if number.replace(',', '').replace(' ', '') not in source.replace(',', '').replace(' ', ''):
                errors.append('Unverified number in claim: ' + number)
    return errors
