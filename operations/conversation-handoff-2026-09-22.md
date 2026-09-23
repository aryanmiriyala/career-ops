# Career Ops Conversation Handoff

Last updated: 2026-09-22

This is the continuation brief for the Career Ops local application. Read this
file together with the root `AGENTS.md` before changing code. Repository state is
the authority when this brief and an older chat recollection differ.

## Continuation Prompt

Use this in a new chat:

> Continue the Career Ops local application from
> `operations/conversation-handoff-2026-09-22.md`. Read the root `AGENTS.md`,
> inspect current Git state, and continue from repository state rather than
> rebuilding the project. Do not read or commit unrelated untracked personal
> files. The immediate milestone is the first real Balanced versus Aggressive
> application-package evaluation, followed by fixes demonstrated by that test.

## Product Goal

Build a trustworthy, token-efficient local career operations application that:

1. Discovers a broad set of recent United States job postings and exposes direct
   posting links, companies, dates, locations, sources, and screening reasons.
2. Lets Aryan select a specific posting and preserve the full job description.
3. Generates a high-quality tailored one-page resume and one-page cover letter
   from verified source material.
4. Produces a transparent internal Job Alignment & Evidence Score, gap analysis,
   validation results, and improvement pass.
5. Stores approved application packages under the existing repository convention
   instead of treating the LLM or chat history as infrastructure.
6. Keeps token use bounded through narrow context, structured stages, caching,
   deterministic code, and explicit provider/model routing.

Quality cannot be traded for lower token use. Lower cost must be demonstrated
alongside factual accuracy, writing quality, recruiter readability, and valid PDFs.

## Non-Negotiable Decisions

- Keep Job Discovery and Application Package Generation as separate pipelines.
- A discovered lead becomes an application only after Aryan selects it.
- Use canonical `profile/` and `master-documents/` evidence. Historical application
  packages are outputs, not default source material.
- Never invent experience, projects, tools, metrics, credentials, titles, scope,
  ownership, or outcomes.
- Aggressive alignment means maximum truthful JD terminology, evidence curation,
  and ordering. It does not permit synthetic claims.
- The resume is exactly one page unless an employer requests a CV or longer form.
- Scores are internal alignment estimates, not predictions of an employer's ATS.
- No silent model fallback, retry loop, or paid route.
- A model must not grade and release its own output without independent review,
  deterministic checks, and a human release gate.
- Final application files follow
  `application-packages/<Company>/<Role>/` conventions.
- Keep the app local-only for now. AWS and Supabase remain future deployment/auth
  options, not current prerequisites.
- Keep React/TypeScript/Vite/Tailwind/Radix, FastAPI/Pydantic, and Bun. Aryan was
  open to vanilla HTML, but there was no functional reason to discard the tested
  frontend.
- Make small coherent commits and do not include unrelated user files.

## Why This Architecture Exists

The original workflow made one large LLM context perform source retrieval,
strategy, writing, ATS analysis, validation, orchestration, and state tracking.
It repeatedly consumed broad profile/history context and made quality difficult to
measure. The replacement assigns those responsibilities to code:

- deterministic discovery and filtering;
- bounded requirement-aware evidence retrieval;
- typed model inputs and outputs;
- fixed rendering templates;
- deterministic grounding and exact-term checks;
- independent bounded review;
- a single targeted repair;
- persisted run state, cache, usage ledger, and artifacts;
- explicit human approval before final publication.

The desired shape was informed by ResumeTailor's BYOK approach and
Faithful/Balanced/Aggressive modes, but this repository implementation was built
from its own rules and source material. Do not attempt to recover private server
code or credentials from another product.

## Current Stack

| Area | Current implementation |
| --- | --- |
| Frontend | React, TypeScript, Vite, Tailwind CSS, Radix primitives, Lucide icons |
| Frontend tooling | Bun with `web/bun.lock` and pinned Bun version |
| Backend | FastAPI, Pydantic, local filesystem state |
| Documents | Fixed LaTeX templates, `pdflatex -no-shell-escape`, Poppler checks |
| Discovery | Existing Python ATS/public-feed discovery CLI and report index |
| Model transport | OpenAI-compatible HTTP adapters with typed JSON output |
| Observability | Local usage ledger and metadata-only Langfuse integration |
| Current operation | Loopback-only local app, no login required |
| Future deployment | AWS remains the preferred eventual target; not implemented |

Supabase authentication code exists but is intentionally bypassed by the local
launcher. Do not reintroduce login into the local workflow unless requested.

## Implemented User Workflow

### Job Discovery

- The default discovery command remains
  `python3 job-search/src/job_discovery.py run-pipeline`.
- The local UI can run bounded discovery in the background and browse saved jobs.
- The board is restricted to recognized U.S. locations.
- It exposes company, title, dates, location, source, screening status, and direct
  posting link.
- Current structured sources include configured direct ATS targets, broad
  Greenhouse, Lever, Ashby, and Workday scans, plus supplemental public feeds such
  as Arbeitnow and RemoteOK.
- Broad ATS scanning rotates through configured board directories. A 100-board UI
  run is a batch per broad source, not all available companies.
- iCIMS, Workable, Oracle, SAP SuccessFactors, ADP, BambooHR, Jobvite, and many
  company-specific pages remain adapter/backlog sources until reliable ingestion
  exists.
- Discovery uses zero LLM calls. Screening labels are heuristics, not application
  review status or personalized ATS scores.

### Application Intake

- Selecting a job opens a saved full-JD intake.
- Inputs live under `.local-workspace/intakes/`.
- Deterministic evidence candidates appear before generation.
- Intake modes are Faithful, Balanced, and Aggressive.
- Explicit eligibility blocker language is surfaced and independently checked by
  generation before drafting.

### Package Generation

The engine in `workspace_app/generation_engine.py` executes these stages:

1. Extract exact quoted requirements and eligibility constraints.
2. Retrieve bounded source-linked evidence and search gaps.
3. Draft a typed resume under the selected mode policy.
4. Draft a synchronized typed cover letter.
5. Reject unknown evidence IDs, mismatched entry metadata, unsupported numbers,
   and duplicate submitted claims.
6. Run an independent review for relevance, impact, risk, unsupported claims, and
   editorial issues.
7. Render fixed resume and cover-letter templates and compile PDFs.
8. Calculate alignment and run one targeted repair when required.
9. Require factual, visual, and editorial human review.
10. Run the repository package validator, publish final artifacts, and update the
    application tracker as `Ready`.

Runs are stored under `.local-workspace/generation-runs/`. Matching inputs reuse a
stage cache. The UI includes an explicit option to regenerate writing stages while
reusing requirement extraction.

### Alignment Modes

- **Faithful:** original verified claims and metrics with light rephrasing.
- **Balanced:** verified evidence curated for the role with natural exact-JD
  language where supported. This is the normal default.
- **Aggressive:** strongest defensible JD alignment through substantial curation,
  reordering, and exact supported terminology. Factual boundaries are unchanged.

Do not implement the earlier ResumeTailor wording that allowed synthetic metrics.
It conflicts with this repository's truthfulness and interview-defensibility rules.

### Scoring

The internal score totals 100:

| Category | Points | Source |
| --- | ---: | --- |
| Exact requirement coverage | 40 | Deterministic PDF exact-term check |
| Experience relevance | 25 | Independent bounded review |
| Impact and evidence | 15 | Independent bounded review |
| Formatting and ATS parsing | 10 | One-page compilation and text extraction |
| Risk and gap handling | 10 | Independent bounded review |

Code calculates the total and enforces category bounds. A score below 90 requires
a substantive waiver. A score cannot override failed grounding, eligibility,
formatting, or package-validation gates.

## Generated Artifacts

Working artifacts remain in the local run directory. After approval, final package
files include:

- `job-description.md`
- `requirements.json`
- `eligibility.json`
- `evidence-selection.json`
- `gaps.json`
- `strategy.json`
- `resume-content.json`
- `resume.tex`
- `resume.pdf`
- `cover-letter-content.json`
- `cover-letter.md`
- `cover-letter.pdf`
- `editorial-review.json`
- `alignment.json`
- `validation.json`
- `tailoring-notes.md`
- `run.json`

The master-document UI exposes only allowlisted canonical files. It is not a
general filesystem browser.

## Provider And Token Policy

The app recognizes configuration for Z.ai, OpenRouter, Groq, Gemini, OpenCode Zen,
Mistral, Featherless, and Langfuse. Never print or copy key values into documents,
logs, commits, or chat.

- `zai/glm-4.7-flash` is the only route currently permitted without the explicit
  paid/quota-backed checkbox.
- Other configured routes require explicit approval for each run.
- There is no automatic provider fallback.
- Each call reserves against the run token budget and records reported usage,
  served model, latency, and uncertain billing state locally.
- Langfuse receives metadata only: run ID, stage, model, latency, and usage. It
  must not receive JD, profile, prompt, resume, or cover-letter content.
- The last bounded Z.ai synthetic probe succeeded with HTTP 200 and 17 total
  tokens. This proved route access, not long-form generation quality.

Provider promotions and free quotas can change. Verify current terms before making
pricing claims. Do not infer that a configured key means a route is free.

## Important Files

- `AGENTS.md`: binding pipeline and quality rules.
- `workspace_app/README.md`: current local setup and behavior.
- `workspace_app/generation_engine.py`: staged orchestrator and release flow.
- `workspace_app/generation_models.py`: strict generation/review contracts.
- `workspace_app/generation_sources.py`: source snapshots, retrieval, grounding.
- `workspace_app/generation_transport.py`: routes, budgets, ledger, telemetry.
- `workspace_app/generation_render.py`: fixed resume/letter rendering.
- `workspace_app/api.py`: local API, artifact and master-document endpoints.
- `web/src/main.tsx`: job board, application workspace, documents, providers.
- `automation/validate_application_package.py`: final package gate.
- `operations/local-generation-architecture.md`: original detailed design audit.
- `operations/local-pipeline-build.md`: concise current milestone record.
- `job-search/`: discovery tooling, configuration, inbox, history, reports.

The status header and implementation-gap section in
`operations/local-generation-architecture.md` predate implementation. Treat its
contracts as useful but its statement that generation is unimplemented as stale.

## Verification Completed

At the end of implementation on 2026-09-20:

- 51 backend tests passed.
- 2 Playwright workflows passed on desktop and mobile.
- The frontend production build passed.
- Synthetic generation tests compiled one-page resume and cover-letter PDFs.
- Tests covered stage-cache reuse, forced writing refresh, one repair maximum,
  score-waiver enforcement, approval, publication, and tracker integration.
- A bounded live Z.ai `glm-4.7-flash` route check passed.

Re-run verification after code or dependency changes:

```sh
.venv/bin/python -m unittest discover -s workspace_app/tests -v
cd web && bun run build && bun run test:e2e
```

The Playwright suite uses synthetic temporary data and does not access real keys,
profile content, browser sessions, or application packages.

## Git State At Handoff

Branch: `main`

`main` is five commits ahead of `origin/main`:

```text
8eaade4 Document local application generation workflow
8a9eedd Add application generation workspace
d09933e Expose generation and master document APIs
e4310a1 Build staged application package generator
200dad4 Add grounded generation contracts and model transport
```

An attempted direct push was blocked by the execution environment's remote-write
policy. The remote is configured as `git@github.com:aryanmiriyala/career-ops.git`.
Obtain explicit confirmation before pushing to `origin/main` and do not work around
an approval rejection.

The following untracked paths existed at handoff and were not read or committed by
the implementation work:

```text
application-packages/8x/
master-documents/building-answer.txt
master-documents/master-resume/role-bullets.txt
master-documents/origins-answer.txt
master-documents/story.txt
```

Assume these belong to Aryan or another process. Inspect or commit them only when
Aryan explicitly identifies their purpose. The handoff file itself will add one
new tracked documentation commit after this recorded state.

## Security Note

Login credentials for the external ResumeTailor site were shared earlier in the
conversation. They are intentionally absent from this repository and handoff.
Aryan said they would be changed. If they have not been rotated, rotate them. Do
not request or store third-party login credentials to continue this project.

## Known Limitations And Open Decisions

1. No real job package has completed the full UI generation and human approval
   flow. Synthetic correctness tests do not prove real writing quality.
2. Balanced and Aggressive have not yet been compared on the same real posting.
3. The first real long-form Z.ai run may expose JSON-schema, output-limit, writing,
   LaTeX density, or evidence-retrieval issues absent from fixtures.
4. Intake snapshots retain their original brief. Source-aware run caching exists,
   but automatic intake-brief refresh after profile edits remains limited.
5. Exact-term coverage is intentionally only 40% of the internal score and is not
   a complete ATS simulation.
6. Model review still involves probabilistic judgment. Human factual and editorial
   review remains mandatory.
7. Generation uses an in-process thread and local filesystem. It is not suitable
   for multi-instance cloud deployment without a durable task queue and object
   storage.
8. Job refresh is manual. Posting-liveness checks and scheduled discovery are not
   implemented.
9. More ATS adapters are needed for broader coverage.
10. Package approval currently updates the Markdown tracker to `Ready`. Earlier
    conversation considered retiring the tracker, while `AGENTS.md` still requires
    tracker updates. Follow `AGENTS.md` until this policy is explicitly changed
    across instructions, templates, and tooling.
11. `operations/local-generation-architecture.md` should be updated from design
    status to implemented status after the first real evaluation.
12. AWS/Supabase deployment should wait until local quality and cost are measured.

## Immediate Next Milestone

Do not add more architecture before exercising the implementation. Use one real,
currently relevant U.S. posting selected by Aryan:

1. Confirm the full posting is still available and preserve it in an intake.
2. Run Balanced mode using the explicitly selected provider/model.
3. Inspect requirements, eligibility, evidence, gaps, strategy, token usage, resume,
   cover letter, score breakdown, and validator output.
4. Render and visually inspect both PDFs at full-page scale.
5. Correct factual, layout, or writing problems demonstrated by the run.
6. Run Aggressive mode against the same frozen JD and source snapshot.
7. Compare claim accuracy, recruiter readability, exact requirement coverage,
   score rationale, page use, model calls, tokens, latency, and estimated cost.
8. Complete the human approval gates only if every claim is defensible.
9. Verify final publication and tracker behavior.
10. Save a small evaluation record before changing model routing or prompts.

The preferred first benchmark should test a role aligned with substantial verified
experience, not an edge case with obvious eligibility blockers or many unsupported
requirements.

## Definition Of A Trustworthy First Release

- Discovery provides enough recent U.S. leads to be useful and clearly reports
  source failures and coverage limits.
- A selected posting moves through intake, generation, review, PDFs, validation,
  package storage, and tracker update without manual file surgery.
- Every submitted claim is supported and interview-defensible.
- Both PDFs are one page, readable, balanced, and parser-valid.
- Balanced writing is natural and role-specific.
- Aggressive mode improves supported JD alignment without keyword stuffing or
  factual inflation.
- Score arithmetic and rationale match the artifacts.
- Repeated identical work uses cached stages; explicit regeneration is observable.
- Usage records show where tokens were spent.
- Failures stop in a clear reviewable state rather than silently releasing output.
- Human review, not a numeric score, remains the final release authority.

## Local Start Procedure

From the repository root:

```sh
git status --short
git log --oneline -10
cd web && bun run build && cd ..
.venv/bin/python automation/run_workspace.py --port 8767
```

Open `http://127.0.0.1:8767`. The prior server is not assumed to survive between
chat sessions. If the port is occupied, use another loopback port. Do not expose
the local server through a public proxy or tunnel.

