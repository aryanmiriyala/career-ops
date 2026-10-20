"""BM25-based retrieval for job requirements against canonical sources."""
from __future__ import annotations

import math
import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from .core import digest, tokens


@dataclass
class BM25Chunk:
    id: str
    source: str
    line: int
    heading: str
    text: str
    source_hash: str
    token_counts: Counter
    length: int


class BM25Index:
    """BM25 index over source chunks for efficient retrieval."""

    def __init__(self, chunks: list[BM25Chunk], k1: float = 1.5, b: float = 0.75):
        self.chunks = chunks
        self.k1 = k1
        self.b = b
        self.N = len(chunks)
        self.avgdl = sum(c.length for c in chunks) / max(1, self.N)
        self.idf = self._compute_idf()

    def _compute_idf(self) -> dict[str, float]:
        """Compute IDF scores for all terms."""
        df = Counter()
        for chunk in self.chunks:
            for term in set(chunk.token_counts.keys()):
                df[term] += 1
        return {
            term: math.log((self.N - freq + 0.5) / (freq + 0.5) + 1)
            for term, freq in df.items()
        }

    def score(self, query_terms: set[str], chunk: BM25Chunk) -> float:
        """Compute BM25 score for a query against a chunk."""
        score = 0.0
        for term in query_terms:
            if term not in chunk.token_counts:
                continue
            tf = chunk.token_counts[term]
            idf = self.idf.get(term, 0)
            denom = tf + self.k1 * (1 - self.b + self.b * chunk.length / self.avgdl)
            score += idf * tf * (self.k1 + 1) / denom
        return score

    def search(self, query_terms: set[str], top_k: int = 10) -> list[tuple[float, BM25Chunk]]:
        """Search for top-k chunks matching query terms."""
        scored = [(self.score(query_terms, c), c) for c in self.chunks]
        scored.sort(key=lambda x: x[0], reverse=True)
        return [(s, c) for s, c in scored[:top_k] if s > 0]


def build_bm25_index(root: Path) -> BM25Index:
    """Build BM25 index from canonical source files."""
    SOURCE_PATHS = [
        "profile/evidence-index.md",
        "profile/experience-master.md",
        "profile/projects-master.md",
        "profile/skills-master.md",
        "profile/bullet-bank.md",
        "master-documents/master-resume/resume.tex",
        "master-documents/master-resume/resume-expanded.tex",
    ]

    chunks = []
    for name in SOURCE_PATHS:
        path = root / name
        if not path.is_file() or path.is_symlink():
            continue
        content = path.read_text()
        heading, buffer, start = "", [], 1

        def flush():
            if buffer:
                text = "\n".join(buffer).strip()
                if text:
                    chunk_tokens = tokens(heading + " " + text)
                    chunks.append(BM25Chunk(
                        id=digest(name + ":" + str(start) + ":" + text)[:20],
                        source=name,
                        line=start,
                        heading=heading,
                        text=text,
                        source_hash=digest(content),
                        token_counts=Counter(chunk_tokens),
                        length=len(chunk_tokens),
                    ))

        for n, line in enumerate(content.splitlines(), 1):
            if line.startswith("#"):
                flush()
                heading, buffer, start = line.lstrip("# "), [], n + 1
            elif len("\n".join(buffer)) > 1600 or (not line.strip() and buffer):
                flush()
                buffer, start = ([line] if line.strip() else []), n
            else:
                if not buffer:
                    start = n
                buffer.append(line)
        flush()

    return BM25Index(chunks)


def retrieve_bm25(
    root: Path,
    requirements: Any,
    index: BM25Index | None = None,
    max_chars: int = 15000,
    top_k_per_req: int = 5,
) -> dict[str, Any]:
    """Retrieve evidence using BM25 ranking."""
    if index is None:
        index = build_bm25_index(root)

    selected = {}
    searched = []
    used = 0

    for req in requirements.requirements:
        query_terms = set(tokens(req.term + " " + req.quote))
        results = index.search(query_terms, top_k=top_k_per_req)

        ids = []
        for score, chunk in results:
            if chunk.id not in selected and used + len(chunk.text) <= max_chars:
                selected[chunk.id] = chunk
                used += len(chunk.text)
            if chunk.id in selected:
                ids.append(chunk.id)

        searched.append({
            "requirement_id": req.id,
            "term": req.term,
            "searched_locations": [c.source for c in index.chunks],
            "candidate_ids": ids,
            "needs_source_review": not ids,
            "bm25_scores": [s for s, _ in results[:3]],
        })

    # Always include key structural sources
    for chunk in index.chunks:
        if chunk.source in {"profile/evidence-index.md", "master-documents/master-resume/resume.tex"}:
            if chunk.id not in selected and used + len(chunk.text) <= max_chars:
                selected[chunk.id] = chunk
                used += len(chunk.text)

    return {
        "evidence": [
            {
                "id": c.id,
                "source": c.source,
                "line": c.line,
                "heading": c.heading,
                "text": c.text,
                "source_hash": c.source_hash,
            }
            for c in selected.values()
        ],
        "searches": searched,
        "characters": used,
        "scope": "Canonical indexed sources only. BM25-ranked retrieval. Unrecorded project/repository evidence needs human recovery.",
    }