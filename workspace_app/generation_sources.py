"""Bounded requirement-aware retrieval from canonical sources, never old packages."""
import re
from pathlib import Path

from .core import digest, tokens

POLICY_PATHS = ['AGENTS.md', 'profile/ats-recruiter-resume-guide.md', 'profile/resume-targeting-guide.md',
                'profile/cover-letter-guide.md', 'templates/canonical-resume.tex',
                'templates/canonical-visual-system.md', 'templates/tailoring-notes-template.md',
                'templates/canonical-cover-letter.md', 'templates/reusable-application-prompt.md']
SOURCE_PATHS = ['profile/evidence-index.md', 'profile/experience-master.md', 'profile/projects-master.md',
                'profile/skills-master.md', 'profile/bullet-bank.md',
                'master-documents/master-resume/resume.tex', 'master-documents/master-resume/resume-expanded.tex']


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


def retrieve(root, requirements, max_chars=35000):
    chunks = source_chunks(root)
    selected, searched, used = {}, [], 0
    for req in requirements.requirements:
        query = set(tokens(req.term + ' ' + req.quote))
        ranked = sorted(chunks, key=lambda c: len(query & set(tokens(c['heading'] + ' ' + c['text']))), reverse=True)
        matches = [c for c in ranked if query & set(tokens(c['heading'] + ' ' + c['text']))][:3]
        ids = []
        for chunk in matches:
            if chunk['id'] not in selected and used + len(chunk['text']) <= max_chars:
                selected[chunk['id']] = chunk
                used += len(chunk['text'])
            if chunk['id'] in selected:
                ids.append(chunk['id'])
        searched.append({'requirement_id': req.id, 'term': req.term, 'searched_locations': SOURCE_PATHS,
                         'candidate_ids': ids, 'needs_source_review': not ids})
    # Preserve resume chronology and source metadata even when not lexical winners.
    for chunk in chunks:
        if chunk['source'] in {'profile/evidence-index.md', 'master-documents/master-resume/resume.tex'}:
            if chunk['id'] not in selected and used + len(chunk['text']) <= max_chars:
                selected[chunk['id']] = chunk
                used += len(chunk['text'])
    return {'evidence': list(selected.values()), 'searches': searched, 'characters': used,
            'scope': 'Canonical indexed sources only. Unrecorded project/repository evidence needs human recovery.'}


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
