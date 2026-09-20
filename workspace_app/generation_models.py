"""Strict contracts for model content, scoring, and human release decisions."""
from typing import Literal

from pydantic import BaseModel, ConfigDict, Field, model_validator


class Record(BaseModel):
    model_config = ConfigDict(extra='forbid')


class Requirement(Record):
    id: str = Field(min_length=1, max_length=60)
    term: str = Field(min_length=1, max_length=160)
    quote: str = Field(min_length=1, max_length=1500)
    priority: Literal['required', 'preferred', 'responsibility']


class Requirements(Record):
    lane: str = Field(min_length=1, max_length=200)
    title: str = Field(min_length=1, max_length=200)
    requirements: list[Requirement] = Field(min_length=1, max_length=60)
    eligibility: Literal['no_explicit_blocker', 'uncertain', 'blocked']
    eligibility_quotes: list[str] = Field(max_length=15)
    eligibility_reason: str = Field(min_length=1, max_length=2000)


class Claim(Record):
    text: str = Field(min_length=1, max_length=2000)
    evidence_ids: list[str] = Field(min_length=1, max_length=12)


class Entry(Record):
    name: str = Field(min_length=1, max_length=160)
    title: str = Field(max_length=160)
    dates: str = Field(max_length=100)
    location: str = Field(max_length=150)
    evidence_ids: list[str] = Field(min_length=1, max_length=12)
    bullets: list[Claim] = Field(min_length=1, max_length=20)


class Gap(Record):
    requirement_id: str
    decision: Literal['supported', 'undocumented', 'unsupported']
    evidence_ids: list[str] = Field(max_length=12)
    rationale: str = Field(min_length=10, max_length=1500)


class ResumeDraft(Record):
    target_title: str = Field(min_length=1, max_length=200)
    strategy: str = Field(min_length=20, max_length=2500)
    summary: list[Claim] = Field(max_length=1)
    experience: list[Entry] = Field(min_length=1, max_length=10)
    projects: list[Entry] = Field(max_length=4)
    skills: list[Claim] = Field(min_length=1, max_length=5)
    gaps: list[Gap] = Field(min_length=1, max_length=60)


class LetterDraft(Record):
    paragraphs: list[Claim] = Field(min_length=3, max_length=4)


class PackageDraft(Record):
    resume: ResumeDraft
    cover_letter: LetterDraft


class Judgment(Record):
    earned: int = Field(ge=0)
    rationale: str = Field(min_length=20, max_length=2500)
    evidence_ids: list[str] = Field(min_length=1, max_length=30)


class Review(Record):
    experience: Judgment
    impact: Judgment
    risk: Judgment
    supported_requirement_ids: list[str] = Field(max_length=60)
    unsupported_claims: list[str] = Field(max_length=50)
    editorial_issues: list[str] = Field(max_length=50)
    eligibility: Literal['no_explicit_blocker', 'uncertain', 'blocked']
    eligibility_reason: str = Field(min_length=10, max_length=2000)

    @model_validator(mode='after')
    def bounded_score_categories(self):
        limits = {'experience': 25, 'impact': 15, 'risk': 10}
        for name, limit in limits.items():
            if getattr(self, name).earned > limit:
                raise ValueError(f'{name} score exceeds {limit}')
        return self


class RunRequest(Record):
    intake_id: str = Field(pattern=r'^[a-f0-9]{24}$')
    provider: Literal['zai', 'openrouter', 'groq', 'gemini', 'opencode', 'mistral', 'featherless'] = 'zai'
    model: str = Field(default='glm-4.7-flash', min_length=1, max_length=160, pattern=r'^[\w./:@+-]+$')
    review_provider: Literal['zai', 'openrouter', 'groq', 'gemini', 'opencode', 'mistral', 'featherless'] = 'zai'
    review_model: str = Field(default='glm-4.7-flash', min_length=1, max_length=160, pattern=r'^[\w./:@+-]+$')
    max_output_tokens: int = Field(default=6000, ge=1000, le=12000)
    token_budget: int = Field(default=240000, ge=10000, le=500000)
    motivation: str = Field(default='', max_length=5000)
    company_context: str = Field(default='', max_length=5000)
    allow_paid: bool = False
    refresh_drafts: bool = False


class Approval(Record):
    factual_review: str = Field(min_length=30, max_length=3000)
    visual_review: str = Field(min_length=30, max_length=3000)
    editorial_review: str = Field(min_length=30, max_length=3000)
    sub90_waiver: str = Field(default='', max_length=3000)
    experience_waiver: str = Field(default='', max_length=3000)
    confirmed: Literal[True]
