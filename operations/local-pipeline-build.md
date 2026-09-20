# Local Pipeline Build

## Current Boundary

Local-only is the active development target. React/Vite serves a compiled UI through FastAPI on loopback. The local launcher requires no Supabase or hosting account. Cloud deployment is deferred, not a prerequisite. Retain the existing tested frontend rather than rewriting it to vanilla JavaScript without a functional benefit.

## Responsibilities

| Component | Responsibility | Model calls |
| --- | --- | --- |
| Discovery CLI | Fetch configured employer ATS boards, broad ATS sources, and supplemental public feeds; apply deterministic review filters | None |
| Report index | Parse, deduplicate, cache, filter, and sort saved postings | None |
| Scan manager | Run one bounded process, report progress/coverage, support cancellation | None |
| Application intake | Preserve selected full JD and retrieve bounded source-linked evidence candidates | None |
| Draft engine | Requirements extraction, evidence-linked writing, one bounded repair, and stage caching | Budgeted |
| Validation and release | Canonical rendering, parser checks, score arithmetic, factual traceability, human approval, package validation, and tracker update | Deterministic checks plus bounded editorial judgment |

## Implemented Local Workflow

- One local launch command with direct job-board entry, no login, and loopback binding.
- Cached job report parsing with source-change invalidation.
- Source/layer coverage and scan progress in the job board.
- Real discovery scan to populate recent matches; no paid APIs or model calls.
- Balanced and Aggressive generation modes with the same truthful evidence boundary.
- Explicit provider/model routes, run token budgets, local usage ledgers, and no silent fallback.
- Metadata-only Langfuse tracing that excludes source and generated document text.
- Deterministic requirement coverage plus independently reviewed experience, impact, and risk categories.
- Canonical one-page resume and cover-letter compilation with a required human release review.
- Final publication to the normal application-package directory and bounded tracker update.
- Backend fixtures and desktop/mobile regression tests.

## Next Milestone

The repository audit and concrete generation contract are recorded in
[Local Application Generation Architecture](local-generation-architecture.md).
It includes the master-document viewer, stage responsibilities, output preferences,
score/waiver enforcement gaps, token controls, and implementation acceptance tests.

Run the first real selected-job package through both Balanced and Aggressive modes, perform the factual/visual/editorial release review, and record a human comparison of accuracy, writing quality, JD alignment, and provider token use. Use that review as the beginning of a representative evaluation set.

Build a representative evaluation set before changing model routing. Token reduction is measurable; preservation of writing quality must be demonstrated with evidence checks, deterministic document gates, and human review. Do not claim equivalent quality solely from a smaller prompt or an internal alignment score.

Automatic application submission, live posting-liveness verification, and scheduled refresh remain intentionally out of scope. Generation approval marks a package `Ready`, not `Applied`. Discovery results remain leads until Aryan selects a posting and starts an application run.
