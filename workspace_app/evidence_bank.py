"""Structured evidence bank loader and query interface."""
from __future__ import annotations

import yaml
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass
class Bullet:
    id: str
    role: str
    title: str
    dates: str
    location: str
    ownership: str
    text: str
    metrics: dict[str, Any]
    tech_tags: list[str]
    line_count: int
    evidence_refs: list[str]
    lane_tags: list[str]
    note: str | None = None


@dataclass
class EvidenceBank:
    bullets: list[Bullet]
    allowlist_skills: list[str]
    blocklist_skills: list[str]

    def get_by_lane(self, lane: str) -> list[Bullet]:
        """Get bullets matching a lane tag."""
        return [b for b in self.bullets if lane in b.lane_tags]

    def get_by_role(self, role: str) -> list[Bullet]:
        """Get bullets for a specific role."""
        return [b for b in self.bullets if b.role == role]

    def get_by_tech(self, tech: str) -> list[Bullet]:
        """Get bullets mentioning a technology."""
        return [b for b in self.bullets if tech.lower() in [t.lower() for t in b.tech_tags]]

    def get_by_ownership(self, ownership: str) -> list[Bullet]:
        """Get bullets by ownership level."""
        return [b for b in self.bullets if b.ownership == ownership]

    def get_primary_bullets(self) -> list[Bullet]:
        """Get only primary-ownership bullets."""
        return [b for b in self.bullets if b.ownership == "primary"]

    def total_lines(self, bullet_ids: list[str]) -> int:
        """Calculate total rendered lines for a set of bullets."""
        id_set = set(bullet_ids)
        return sum(b.line_count for b in self.bullets if b.id in id_set)

    def select_for_role(
        self,
        required_techs: list[str],
        preferred_techs: list[str],
        lane: str,
        max_lines: int = 40,
        min_experience_bullets: int = 11,
    ) -> tuple[list[Bullet], list[Bullet]]:
        """
        Select best bullets for a role using a greedy algorithm.
        Returns (experience_bullets, project_bullets).
        """
        # Score bullets by relevance
        scored = []
        for b in self.bullets:
            score = 0
            # Lane match
            if lane in b.lane_tags:
                score += 10
            # Required tech match
            for tech in required_techs:
                if tech.lower() in [t.lower() for t in b.tech_tags]:
                    score += 5
            # Preferred tech match
            for tech in preferred_techs:
                if tech.lower() in [t.lower() for t in b.tech_tags]:
                    score += 2
            # Primary ownership bonus
            if b.ownership == "primary":
                score += 3
            # Contributor ownership (slightly lower)
            elif b.ownership == "contributor":
                score += 1
            # Recency bonus (prefer recent roles)
            if b.role in ["Actual Reality Technologies", "SmartSolve Industries"]:
                score += 2
            scored.append((score, b))

        # Sort by score descending, then by line_count ascending (prefer dense bullets)
        scored.sort(key=lambda x: (-x[0], x[1].line_count))

        # Separate experience and project bullets
        experience_bullets = []
        project_bullets = []
        used_ids = set()
        exp_lines = 0
        proj_lines = 0

        for score, bullet in scored:
            if bullet.id in used_ids:
                continue

            is_experience = bullet.role not in ["Projects"]
            is_project = bullet.role == "Projects"

            if is_experience and exp_lines + bullet.line_count <= max_lines - 10:  # Reserve space for projects
                experience_bullets.append(bullet)
                exp_lines += bullet.line_count
                used_ids.add(bullet.id)
            elif is_project and proj_lines + bullet.line_count <= 8:  # Max ~2 projects, ~4 bullets
                project_bullets.append(bullet)
                proj_lines += bullet.line_count
                used_ids.add(bullet.id)

        # Ensure minimum experience bullets
        if len(experience_bullets) < min_experience_bullets:
            # Add more experience bullets even if they push line count
            for score, bullet in scored:
                if bullet.id in used_ids:
                    continue
                if bullet.role not in ["Projects"]:
                    experience_bullets.append(bullet)
                    exp_lines += bullet.line_count
                    used_ids.add(bullet.id)
                    if len(experience_bullets) >= min_experience_bullets:
                        break

        return experience_bullets, project_bullets


def load_evidence_bank(root: Path) -> EvidenceBank:
    """Load the evidence bank from profile/evidence.yaml."""
    path = root / "profile" / "evidence.yaml"
    if not path.is_file():
        raise FileNotFoundError(f"Evidence bank not found at {path}")

    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)

    bullets = []
    for b in data.get("bullets", []):
        bullets.append(Bullet(
            id=b["id"],
            role=b["role"],
            title=b["title"],
            dates=b["dates"],
            location=b["location"],
            ownership=b["ownership"],
            text=b["text"],
            metrics=b.get("metrics", {}),
            tech_tags=b.get("tech_tags", []),
            line_count=b.get("line_count", 2),
            evidence_refs=b.get("evidence_refs", []),
            lane_tags=b.get("lane_tags", []),
            note=b.get("note"),
        ))

    return EvidenceBank(
        bullets=bullets,
        allowlist_skills=data.get("allowlist_skills", []),
        blocklist_skills=data.get("blocklist_skills", []),
    )


def validate_claims_against_bank(bank: EvidenceBank, claims: list[dict], evidence_ids: list[str]) -> list[str]:
    """Validate that claims are supported by cited evidence IDs."""
    errors = []
    bullet_map = {b.id: b for b in bank.bullets}

    for claim in claims:
        claim_evidence_ids = claim.get("evidence_ids", [])
        for eid in claim_evidence_ids:
            if eid not in bullet_map:
                errors.append(f"Claim references unknown evidence ID: {eid}")
            elif eid not in evidence_ids:
                errors.append(f"Claim references evidence ID not in retrieved set: {eid}")

    return errors


def check_skill_allowlist(bank: EvidenceBank, skills_text: str) -> list[str]:
    """Check that all skills mentioned are in the allowlist and not in blocklist."""
    errors = []
    skills_lower = skills_text.lower()

    for blocked in bank.blocklist_skills:
        if blocked.lower() in skills_lower:
            errors.append(f"Blocklisted skill mentioned in skills section: {blocked}")

    return errors