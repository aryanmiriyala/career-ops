# Application Pipeline Architecture Discovery

Date: 2026-09-13

Status: Research and proposed design, not an implemented migration. Complements `pipeline-optimization-audit.md`. Public upstream documentation and selected source were inspected; upstream applications were not executed or benchmarked. Links to moving branches are research references, not pinned dependencies.

## Recommendation

Deployment requirement: AWS, confirmed by Aryan after the initial discovery. Build a Python application engine with a React review interface, deployable on AWS and runnable locally for development. Keep the existing canonical LaTeX renderer and PDF checks. Make retrieval, state transitions, rendering, arithmetic, caching, and budget enforcement software responsibilities. Use bounded model calls for requirements interpretation, evidence selection when ambiguous, writing, and independent editorial review.

Quality preservation must be demonstrated on a fixed evaluation set. Neither cheaper models, more agents, semantic similarity, nor a high internal score establishes equivalent quality by itself.

## Current State: Implemented Versus Discussed

Implementation checkpoint after this research: the local `workspace_app/` API and `web/` frontend now provide a recent-job board, bounded lexical evidence intake, provider diagnostics, and local/Supabase authentication integration. The frontend uses React, TypeScript, Vite, Tailwind CSS, Radix-backed controls, and Bun tooling. See [workspace setup](../workspace_app/README.md) and [frontend decisions](../web/README.md). Live Supabase sign-in still requires project configuration. Model drafting, stage caching, independent evaluation, document generation in the UI, and AWS deployment remain pending. The observations below describe the repository before that first application increment.

- Implemented: exact-term analyzer, compact package brief, PDF/package validators, token-hotspot inventory, tracker upsert, canonical templates, profile evidence index, and an environment-variable template.
- Discussed but not implemented in the inspected automation: structured evidence retrieval, standalone model-call runner, stage caching, enforced run budgets, Langfuse integration, model regression evaluations, and a web frontend.
- No dependency manifest was found in the bounded repository search. Introduce a pinned Python project environment before adding runtime dependencies.
- The hotspot script counts repository words. It does not measure actual prompts, outputs, reasoning tokens, or billed usage. Repository size is not evidence that every file is sent for every job.
- `validate_application_package.py:187` verifies written gate markers. `check_score_consistency` verifies score arithmetic, not the underlying relevance judgments. Keep these checks, but add independently produced evidence and evaluation results.
- `MIN_ALIGNMENT_SCORE = 90` and the waiver requirement can create repeated revision work. The current rule remains in force. A proposed replacement should distinguish document readiness from unavoidable role-fit gaps rather than requiring rewriting until a target score appears.
- Earlier conversation requested retiring the tracker, but the current supplied instructions and repository still require it. This research recommends package-local manifests and a directory-backed UI; the eventual migration must reconcile all affected instructions and templates together. No tracker rule was changed here.

## Upstream Lessons

### Santifer's Career Ops

The requested `santifer/career-ops` currently redirects to `career-ops-hq/career-ops`. Its architecture keeps files canonical and SQLite derived. Borrow that boundary for package folders and a rebuildable search index. Its budget guide documents spend tiers, pre-screening, interrupted-run resumption, and standalone provider runners. These are useful operational patterns, but its core still includes substantial prompt-driven evaluation.

The inspected `openai-eval.mjs` passes shared instructions, evaluation logic, CV, profile, and JD into a budgeted prompt builder; records token usage; and saves results in code. It also attempts provider-dependent prompt caching. The request shown has no explicit output-token cap. Therefore, do not copy this runner as our complete cost-control design. The imported context-budget helper could not be fetched during this pass, so its trimming behavior was not verified.

Sources: [architecture](https://github.com/career-ops-hq/career-ops/blob/main/ARCHITECTURE.md), [budget guide](https://github.com/career-ops-hq/career-ops/blob/main/docs/RUNNING_ON_A_BUDGET.md), [runner source](https://github.com/career-ops-hq/career-ops/blob/main/openai-eval.mjs).

### Resume Matcher

Its documented stack separates FastAPI/Python/LiteLLM from Next.js/React, with JSON storage and Playwright PDF rendering. This is a relevant reference for a tailoring application with a real UI and provider abstraction. Borrow the API/frontend separation; retain our tested LaTeX layout instead of migrating rendering as part of the same change. Its README does not establish comparative resume quality or cost savings for our inputs.

Source: [repository and stack](https://github.com/srbhr/Resume-Matcher).

### Reactive Resume

Useful as a review/editing UX reference: live preview, section ordering, structured exports, and template handling. Our first UI should expose evidence, section edits, and a final PDF preview while keeping the canonical layout fixed. A full general-purpose resume designer would add scope without addressing model usage.

Source: [repository](https://github.com/reactive-resume/reactive-resume).

### Tailor Resume

Its documented flow separates parsing, a typed profile, gap analysis, and LaTeX rendering, and shares pipeline logic between CLI and web runtime. Borrow typed intermediate data and one engine behind multiple interfaces. Do not adopt its 20-word truncation policy or seniority-vocabulary scoring: these can lose meaningful evidence and do not match our early-career lanes. Its test-count and no-fabrication claims were not independently validated here.

Sources: [repository](https://github.com/narendranathe/tailor-resume), [architecture](https://github.com/narendranathe/tailor-resume/blob/main/ARCHITECTURE.md).

## Proposed Responsibilities

| Stage | Owner | Saved result |
| --- | --- | --- |
| Intake | Python saves full JD, metadata, source hash | job-description.md |
| Requirements | One schema-constrained call plus deterministic checks; retain source quotes | requirements.json |
| Eligibility | Explicit-rule checks with source excerpts; ambiguous cases require review | eligibility.json |
| Evidence retrieval | Local lexical ranking, optional embeddings, requirement-by-requirement fallback search | evidence-selection.json |
| Strategy | Select role angle and evidence under coverage and page constraints; bounded model judgment where needed | strategy.json |
| Drafting | Model writes structured resume content and cover-letter paragraphs using selected evidence IDs | resume-content.json, cover-letter-content.json |
| Grounding | Validate IDs, dates, metric units and attribution; review whether prose is supported by cited evidence | grounding.json |
| Rendering | Code escapes text and fills fixed templates, then compiles | Existing TEX/MD/PDF outputs |
| Evaluation | Existing checks plus independent editorial rubric | validation.json, review.json |
| Repair | At most one targeted automatic repair, followed by revalidation; otherwise needs_review | New artifact revision |
| Packaging | Code renders notes and records versions, costs, gates, and hashes | tailoring-notes.md, run.json |

Model stages receive task-specific rules, the relevant requirement excerpts, and verified evidence, not all of AGENTS.md or chat history. JD extraction still sees the full posting once; compact representations retain references to the original. Do not silently drop an uncovered important requirement to fit a token budget.

Keep job discovery independent. Selecting a lead creates an application intake; generation does not trigger another discovery run.

## Evidence and Quality

Index canonical facts with stable evidence IDs, source path/section, source hash, dates, tools, contribution, metric value/unit/context, and public-safe wording. Treat the index as derived from verified profile/source documents. A profile change invalidates dependent selections and drafts. Historical packages are excluded by default.

Use lexical retrieval first, with explicit aliases for terms such as React/ReactJS. Add semantic candidates when lexical recall misses adjacent experience. Reserve coverage for each important requirement and perform targeted source recovery for misses. Embedding similarity suggests candidates; it does not prove experience. An ID citation alone also does not prove that a rewritten claim follows from its source.

Separate three outputs: factual/format validity, role-fit coverage, and editorial quality. Code can check invented numeric values, missing IDs, dates, file completeness, arithmetic, and PDF geometry. Human or model review is still needed for exaggeration, causal claims, role ownership, relevance, and natural cover-letter voice. Compute report totals from structured results rather than asking the writer to award itself points.

Cover-letter inputs need their own compact brief: selected proof points, user motivation, and verified company facts with URLs. Resume-only context is insufficient for a personal letter. Cache company research with source dates and refresh when facts may have changed. Do not invent personal enthusiasm or connection.

Maintain Faithful, Balanced, and Aggressive as evidence-selection and phrasing policies. All three preserve verified facts and metrics. Aggressive may substantially reorder and curate verified projects, but does not invent projects or numerical results. Keep tailoring mode independent from provider/model spend tier.

## Technology Choices

| Add | Purpose and boundary |
| --- | --- |
| FastAPI + Pydantic | Typed API and stage contracts around existing Python checks; schema validation does not establish truth |
| React + TypeScript + Vite + TanStack Query | Review interface hosted on AWS Amplify Hosting; same UI runs locally |
| SQLite FTS5 | Rebuildable evidence search snapshot in workers; not the shared cloud job-state database |
| Sentence Transformers, optional | Local semantic retrieval over small evidence chunks; cache by source and embedding-model version |
| LiteLLM SDK | Provider normalization and controlled fallback; keep budget enforcement in our engine, no proxy deployment initially |
| Langfuse | Per-stage usage, latency, prompt version and evaluation visibility; retain a local usage record and redact sensitive text |
| Pydantic Evals + pytest | Python-native quality comparisons plus deterministic contract, cache, and failure-path tests |
| Existing LaTeX + Poppler checks | Preserve submission layout and parsing behavior; add deterministic template filling |

Official references: [FastAPI](https://fastapi.tiangolo.com/), [TanStack Query](https://tanstack.com/query/latest/docs/framework/react/overview), [SQLite FTS5](https://www.sqlite.org/fts5.html), [Sentence Transformers](https://sbert.net/examples/sentence_transformer/applications/semantic-search/README.html), [LiteLLM routing](https://docs.litellm.ai/docs/routing), [Langfuse usage tracking](https://langfuse.com/docs/observability/features/token-and-cost-tracking), [Pydantic Evals](https://pydantic.dev/docs/ai/evals/evals/).

Start with OpenRouter and the user's Featherless balance as candidate backends, evaluated per stage. Featherless documents a compatible API. Select explicit model/provider versions for comparisons and record the actual serving model. Free endpoints are useful experiments, but availability or quality failures must pause or follow an explicitly configured fallback budget. Do not silently switch a free run to paid generation.

Source: [Featherless quickstart](https://featherless.ai/docs/quickstart-guide).

Defer LangGraph, multi-agent teams, Redis/Celery, a dedicated vector service, and multiple evaluation frameworks. The initial workflow is a small persisted sequence with a bounded repair branch. AWS Step Functions handles cloud task lifecycle as described below; the Python engine owns the application stages.

## AWS Deployment Target

Assumption: a private, low-volume application for Aryan initially. Proposed deployment, not provisioned resources. AWS hosting does not require switching inference to Bedrock; keep the existing external provider choices.

| Component | AWS service | Responsibility |
| --- | --- | --- |
| React static app | Amplify Hosting | Build and serve the UI over HTTPS |
| Authentication | Supabase Auth | User-selected identity provider; API verifies the user and restricts access to the owner; career data stays in AWS |
| Short API requests | API Gateway HTTP API + Lambda | Intake, edits, start/cancel jobs, status, authorized download URLs; adapt FastAPI to the Lambda event interface |
| Job lifecycle | Step Functions Standard | Start and monitor one Fargate task per package run, bounded timeout and failure handling |
| Generation worker | ECS Fargate standalone task, image in ECR | Python engine, provider calls, LaTeX and Poppler; exits when finished |
| Canonical artifacts | Private, versioned S3 bucket | Profile snapshots, JDs, stage results, TEX/MD/PDF artifacts, manifests and cache results |
| Operational state | DynamoDB on-demand | Job state, concurrency leases, idempotency keys and atomic budget reservations |
| Provider credentials | Secrets Manager | Runtime server-side access through IAM roles |
| Operations | CloudWatch and AWS Budgets | Logs, errors, operational metrics and infrastructure cost alerts; Langfuse remains for model traces |

Request flow: browser authenticates with Supabase, API verifies the Supabase identity, saves input and creates a run, then starts a named Step Functions execution and returns a run ID. Step Functions uses ECS `runTask.sync`; the worker checkpoints stages in S3 and updates DynamoDB status. The frontend polls status and obtains short-lived download URLs after authorization. Cancellation records intent and stops execution/task with reconciliation of any already-incurred model usage.

Authentication update: Aryan prefers Supabase Auth and wants to avoid Vercel. Keep React/Vite and FastAPI. Use AWS Amplify Hosting for static frontend deployment; using Supabase Auth does not require deploying the API or application database on Supabase. Supabase necessarily maintains its own identity records. Cognito remains an all-AWS alternative, but do not implement two cloud identity systems. The local prototype retains an offline single-owner mode solely for loopback development. [Supabase authentication documentation](https://supabase.com/docs/guides/auth/passwords).

Use one worker for the whole package initially, not one container per stage. Preserve stage checkpoints so reruns resume successful work. Use DynamoDB conditional writes for lease acquisition and guarded state transitions. Duplicate start requests and worker retries must not launch uncontrolled repeated generation. A crash after a provider accepted a request can leave uncertain billing; record that uncertainty rather than claiming exactly-once inference.

S3 object prefixes preserve `application-packages/<Company>/<Role>/` organization, with immutable run/revision identifiers beneath it. S3 is object storage, not a shared POSIX filesystem. Workers download a run snapshot into temporary local directories, compile there, upload artifacts, then publish a completed manifest. The local repository becomes an explicit import/export workspace; do not create two silently diverging sources of truth. DynamoDB operational records are authoritative while a job is active; artifact manifests remain durable package records.

SQLite can still supply a small, versioned read-only evidence index downloaded from S3. Do not share a writable SQLite file across cloud workers. Regenerate index snapshots when verified profile data changes. A managed vector database or RDS is unnecessary for this initial scope.

Fargate accommodates the existing compilation environment and variable model latency. Standard Lambda invocations have a 15-minute maximum; Lambda remains suitable for short API work. Step Functions supports waiting for ECS/Fargate tasks. App Runner is an alternative API host, but its ephemeral storage and 120-second HTTP request limit do not suit running the complete package in an HTTP handler.

Cost controls: no always-on generation workers; conservative concurrency; bounded task runtime, model retries and output limits; lifecycle rules for temporary artifacts; limited log retention. Price network egress, public IPv4 or NAT/VPC endpoints, image storage, authentication and telemetry alongside compute. Choose the network design during infrastructure review so fixed networking costs do not dominate light usage. AWS budget alerts are not synchronous hard spend caps; enforce model budgets inside the engine. No free-tier or monthly-price guarantee is assumed.

Infrastructure should be defined in one reproducible IaC stack, proposed AWS CDK in TypeScript, with a deployment preview and CI tests before provisioning. Region, monthly infrastructure budget and domain remain deployment-time choices. First verify identical fixture outputs locally and in the worker container, then test cloud checkpoint recovery, concurrent requests, authorization, and actual billed usage.

Sources: [Amplify Hosting](https://docs.aws.amazon.com/amplify/latest/userguide/welcome.html), [Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools.html), [Step Functions with ECS/Fargate](https://docs.aws.amazon.com/step-functions/latest/dg/connect-ecs.html), [S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html), [DynamoDB conditional writes](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.ConditionExpressions.html), [Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html), [Lambda limits](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html), [App Runner runtime limits](https://docs.aws.amazon.com/apprunner/latest/dg/develop.html).

## Token and Reliability Controls

1. Persist stage inputs/results; resume from the last successful stage after a crash. Use input fingerprints and atomic writes, with a per-package lock. Interrupted requests with uncertain billing must not be reported as free.
2. Key caches on stage, source hashes, prompt/schema/policy versions, model/provider, and generation settings. Invalidate only downstream dependents. Store failures separately from successful cached outputs.
3. Distinguish application-result caching (no call on a hit) from provider prompt caching (a call with potentially discounted input). Verify cache usage in returned telemetry; provider caching is not universally supported. See [OpenRouter caching documentation](https://openrouter.ai/docs/guides/best-practices/prompt-caching).
4. Check input size before every call; set output limits and model-specific reasoning limits where supported. Reserve worst-case expected cost before scheduling calls. Include retries, fallbacks, and concurrent calls in the same run budget.
5. Count prompt, completion, cached, and reasoning usage according to each provider's schema without double counting. Preserve raw usage and distinguish measured from estimated cost. Unknown prices must not become zero-cost records.
6. Rerun only affected work. Editing a cover-letter sentence should not trigger JD extraction, evidence retrieval, or resume generation. Each edit marks affected validation results stale until recomputed.
7. Start with roughly four model calls: requirements, resume draft/selection, cover letter, independent editorial review. Allow one repair. These are initial design targets, not measured performance guarantees; difficult strategy cases may need a separate bounded call.
8. Keep API keys server-side. Trace metadata and usage by default; uploading full personal source text to observability should be configurable. Restrict model output to content fields, not shell commands or arbitrary LaTeX.

## Frontend Scope

The initial screen should be the usable package workspace: directory-backed package list, JD intake, mode selector, model/budget settings, evidence checklist, editable resume/letter sections, source-linked diff, PDF preview, and separate validation/fit/review results. Show stage progress, cache hits, actual token usage, and remaining budget. Provide cancel, resume, and retry-failed-stage controls.

The UI calls the same engine as the CLI. It does not construct a second set of prompts. On AWS, S3 package manifests supply artifact records and DynamoDB supplies active job state; local development uses directory packages. A generated package is not proof of submission.

## Build Sequence and Acceptance

1. Establish measurement and fixtures. Add pinned dependencies, typed run/evidence records, local token accounting, and a fixed set of representative JDs with verified evidence. Use user-designated historical packages only if explicitly named; otherwise create independent fixtures.
2. Implement retrieval and standalone generation behind a CLI. Keep existing outputs compatible and generate notes from structured records. Demonstrate that an unchanged rerun makes zero generation calls and a letter edit does not regenerate the resume.
3. Compare models/prompts on approximately 20-30 diverse cases, including weak fit, unsupported tools, ambiguous eligibility, metric attribution, long JDs, and personal cover letters. Measure cost per accepted package, review effort, grounding failures, requirement recall, readability, and PDF validity. Repeat stochastic cases and keep a held-out subset.
4. Require zero known invented claims and all hard gates passing on the evaluation set. Use blinded pairwise human review for the writing baseline; an LLM judge is supplementary. Passing the finite suite reduces regression risk but cannot guarantee flawless future writing.
5. Build the frontend against the proven engine. Then reconcile tracker removal and rule ownership across AGENTS.md, reusable prompts, templates, and affected tooling in one coherent maintenance pass.

The next useful implementation is a measured vertical slice from one JD to one validated package. No savings percentage or per-package price can be responsibly claimed before that baseline exists.
