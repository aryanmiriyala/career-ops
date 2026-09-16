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
| Draft engine, pending | Requirements interpretation and grounded writing using bounded inputs | Budgeted |
| Validation, existing CLI / pending UI integration | Canonical document rendering, parser checks, arithmetic, factual traceability and editorial review | Deterministic checks plus bounded editorial judgment |

## This Increment

- One local launch command with direct job-board entry, no login, and loopback binding.
- Cached job report parsing with source-change invalidation.
- Source/layer coverage and scan progress in the job board.
- Real discovery scan to populate recent matches; no paid APIs or model calls.
- Backend fixtures and desktop/mobile regression tests.

## Next Milestone

Implement an explicit selected-job application run with a persisted manifest and stage statuses. Cache stages by full JD hash, verified source hashes, template/prompt versions, model identity, and tailoring mode. Never reuse a result after its inputs change. Limit repair attempts; persist failures for review rather than silently producing a ready package. Use confirmed source claims, not historical application outputs, as evidence.

Build a representative evaluation set before changing model routing. Token reduction is measurable; preservation of writing quality must be demonstrated with evidence checks, deterministic document gates, and human review. Do not claim equivalent quality solely from a smaller prompt or an internal alignment score.

No generation engine, automatic application submission, live posting-liveness verification, scheduled refresh, or Langfuse trace integration is enabled by this increment. Existing canonical application-generation rules remain in force. Discovery results are leads, not confirmed open roles or completed applications.
