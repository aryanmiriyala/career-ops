# Local Application Generation Architecture

Audit date: 2026-09-15 (local time).
Status: Implementation specification, not an implemented generation engine.
Scope: local-only application generation and master-document viewing. No cloud,
authentication, automatic submission, or historical-package ingestion is required.
This document supersedes cloud-first implementation sequencing, not AGENTS.md.

## Audited Sources

- AGENTS.md: pipeline separation, work modes, evidence, layout, scoring, gates.
- profile/ats-recruiter-resume-guide.md and profile/resume-targeting-guide.md.
- profile/cover-letter-guide.md and the evidence-index.md routing structure.
- templates/canonical-resume.tex, canonical-visual-system.md,
  tailoring-notes-template.md, reusable-application-prompt.md.
- master-documents/README.md and ready-to-send/README.md; document filenames.
- automation/validate_application_package.py, validate_resume_pdf.py,
  analyze_application_keywords.py, and automation/README.md.
- workspace_app/core.py, api.py, providers.py and current frontend flow.
- operations/local-pipeline-build.md and pipeline-architecture-discovery.md.

No prior application packages, full tracker, API key values, or untracked personal
drafts were read. This is a contract/code audit, not a visual audit of old PDFs or
a benchmark of model quality. Existing research links were not revalidated here.

## Actual Implementation Gap

The app saves full-JD intakes and ranks up to 18 lexical source excerpts. It does
not draft documents, execute a generation run, calculate alignment judgments,
compile submission artifacts, expose master documents, or emit Langfuse traces.
The CLI validators and canonical templates exist; a reusable content-to-document
renderer and application orchestrator still need implementation.

Specific risks to fix before connecting generation:

1. Evidence intake reads four profile files, skips table rows and short lines,
   and lacks evidence-index routing and requirement-by-requirement gap recovery.
   A retrieval miss must not be classified as unsupported experience.
2. Intake identity excludes source hashes. An identical intake can return a saved
   brief even after source evidence changes. Stable intake identity and versioned
   run identity must be separate.
3. Faithful/Balanced/Aggressive are stored values, not implemented drafting policies.
4. Provider diagnostics are not a generation adapter or budget controller.
5. The package validator checks written Pass markers, not proof of factual or
   editorial review. The notes template pre-fills Pass labels; new runs must start
   pending and generate notes from actual completed gate records.
6. Score validation checks sums and category presence, but does not enforce unique
   categories, exact 40/25/15/10/10 maxima, or earned <= available per category.
   The sub-90 check accepts the waiver heading, which already exists in the notes
   template, without establishing a substantive waiver or user decision.
7. Existing eligibility keyword matches need negation/context fixtures. A matched
   word is not by itself a reliable eligibility determination.

## Required Output Preferences

| Area | Contract to preserve |
| --- | --- |
| Sources | Canonical profile/evidence index, master sources, verified project evidence; no historical packages unless explicitly selected |
| Resume | Exactly one page by default, US Letter, 11pt Computer Modern, canonical geometry/macros, text-only single column |
| Prioritization | One primary lane; reverse-chronological experience; experience before lower-value project detail |
| Bullets | Action, individual contribution, method when relevant, context and outcome; normally <=2 rendered lines; no invented metrics |
| Experience depth | Normally >=11 experience bullets; fewer requires a reasoned waiver, not filler |
| Summary/title | Summary omitted by default; if used <=2 sentences and <=2 rendered lines; truthful posted title once visibly |
| Private work | Public-safe system/workflow language, no ticket dumps, confidential customer details or unexplained internal names |
| Cover letter | One page, canonical letter format, warm/personal/technical, 1-2 deep proof points, not a prose copy of the resume |
| Personalization | Verified company facts and real motivation; ask only when missing context materially weakens the letter |
| Gaps | Supported/use now; undocumented/ask and update source; unsupported/omit, after targeted recovery search |
| Eligibility | Explicit blockers stop finalization unless explicitly overridden for permitted reasons; ambiguity remains internal |
| Submission content | No visa/sponsorship discussion unless requested; employer format instructions override defaults |
| Answers | When supplied, application questions receive their own grounded human-voice check |

Faithful keeps original claims and metrics with light rephrasing. Balanced permits
stronger truthful alignment. Aggressive permits substantial curation and rewriting
of verified evidence, never synthetic projects, metrics, credentials or experience.

## Local Components

- Keep React/TypeScript/Vite/Tailwind/Radix and Bun for the UI.
- Keep FastAPI/Pydantic for typed endpoints and validation.
- Add one Python application engine shared by CLI and UI; prompts stay server-side.
- Use canonical package folders for artifacts and immutable run/revision manifests.
- Start with a single local worker, durable checkpoints, atomic manifest writes,
  a per-package lock, cancellation, explicit interruption state and bounded retries.
- Use local derived evidence search; SQLite FTS5 is optional when justified, not a
  required replacement for existing files. Semantic search can suggest evidence,
  but cannot certify it.
- Keep keys server-side. No autonomous paid fallback. Local usage logs precede
  optional redacted Langfuse integration; telemetry outages must not lose artifacts.

## Generation Stages

| Stage | Responsibility | Durable result |
| --- | --- | --- |
| Intake | Save complete JD and user motivation/questions; distinguish source text from instructions | job-description.md, intake metadata |
| Requirements | Extract exact title, required/preferred terms, lane and quoted constraints | requirements.json |
| Eligibility | Assess quoted requirements; block explicit conflicts, request review for uncertainty | eligibility.json |
| Evidence | Route through evidence index, retrieve claims, search important missing terms; retain provenance | evidence-selection.json, gaps.json |
| Strategy | Select strongest evidence, experience/project allocation, title and letter angle | strategy.json |
| Draft | Produce typed resume sections and letter paragraphs with evidence IDs, not arbitrary LaTeX or shell code | resume-content.json, cover-letter-content.json |
| Grounding | Check IDs, metric attribution, dates and factual support; independently review prose entailment | grounding.json |
| Render | Escape model text into fixed templates; compile with timeout, no shell escape, restricted file access | resume.tex/pdf, cover-letter.md/pdf or requested DOCX |
| Evaluate | Run exact-term and expanded keyword checks, PDF/package checks, independent editorial review | alignment.json, validation.json, editorial-review.json |
| Repair | Fix only failed content; at most one automatic targeted repair, then needs_review | revised affected artifacts |
| Finalize | Render notes from actual gate results; publish only verified artifact revisions | tailoring-notes.md, run.json |

Stages use pending/running/succeeded/failed/blocked/stale states. A run can be
cancelled, interrupted, need review, or become ready. Ready never means an online
application was submitted. Downloading a draft must not silently mark it ready.

Use the established application-packages/<Company>/<Role>/ filenames for final
outputs; keep working stages under versioned run directories. Generated artifacts
remain local unless explicitly authorized for Git. Do not publish drafts as masters.

## Scoring And Readiness

Display three separate reports: parser/layout validity, alignment/evidence, and
editorial/grounding review. The discovery heuristic is none of these.

Preserve the internal Job Alignment & Evidence Score weights:
keyword coverage 40; experience relevance 25; impact/evidence 15;
formatting/ATS parsing 10; risk/gap handling 10.

Exact-term coverage is deterministic but not the full rubric. Version the scoring
rubric and requirement weights; link each judgment to requirements and evidence.
Code calculates totals and enforces category bounds. A reviewer supplies the
non-mechanical judgments, with rationale, instead of the writer awarding itself a
target score. This remains an internal estimate, not an employer ATS prediction.

Keep the >=90 readiness rule or a substantive Sub-90 Readiness Waiver. Never loop
until a score reaches 90, invent claims, or allow a score to override a failed hard
gate. After the bounded repair, unresolved issues require explicit review. Human
visual/editorial checks remain separate where automation cannot establish a pass.

## UI Areas

1. Job board: leads only; selecting Generate package creates an explicit intake.
2. Master documents: read-only PDF preview, source/text view, download, modified
   time and source identity for the canonical one-page resume, expanded resume/CV,
   master letter template, and ready-to-send exports. Show missing/stale PDFs
   honestly. Serve allowlisted document IDs, reject traversal and symlink escapes;
   do not expose a generic filesystem endpoint or copy masters into frontend assets.
3. Application workspace: JD/context, evidence and gaps, resume, cover letter,
   questions when present, quality report, final files and run history. Include
   edits, PDF preview, source-linked diffs, cancel/resume and affected-stage reruns.
4. Run settings: tailoring mode, provider/model, input/output budgets, measured
   usage, estimated-versus-reported cost, cache hits and failed-stage detail.

The master library is not the full evidence corpus. Expanded master content and
profile/project sources remain available to recover evidence absent from one page.

## Token And Quality Controls

Cache by JD, selected evidence/source hashes, policy/template/prompt/schema versions,
mode and model settings. Invalidate only downstream dependencies. Read the full JD
for extraction once; subsequent stages receive relevant requirements and evidence,
not historical packages, full profile files, chat history, or the entire rulebook.
Do not silently truncate uncovered must-have requirements to satisfy a token cap.

Enforce input/output limits and a per-run budget including retries and fallbacks.
Start with approximately four bounded model tasks: requirements, resume strategy/
draft, cover letter, independent editorial review. This is a design target, not a
fixed quality guarantee. Persist uncertain billing after interruption. A source
change invalidates affected drafts; a letter-only edit must not regenerate a resume.

## Build Order And Acceptance

1. Implement policy/gate schemas and regression tests, tighten waiver/score checks,
   and reconcile rule dependencies. Do not change substantive resume preferences.
2. Add the read-only master library and package-workspace shell with honest states.
3. Build one full-JD-to-package vertical slice behind both CLI and UI, using mocked
   provider fixtures first and one explicitly chosen real role for quality review.
4. Connect scoring, PDF checks, editorial review, targeted repair and final downloads.
5. Prove cache reuse, failure recovery, budget caps and source-change invalidation.
   Compare quality across role lanes and failure cases before cheaper-model routing.

Acceptance includes zero invented claims in the reviewed fixture set; exact page
and source checks; no generic cover-letter output accepted without review; genuine
sub-90 waivers; no automatic pass markers; malicious JD/model text treated as data;
an unchanged rerun making no generation calls; and a cover-letter edit leaving the
resume unchanged. Test desktop/mobile previews and downloads with synthetic data.
Finite tests reduce risk but cannot guarantee perfect future writing.

## Outstanding Policy Conflict

Earlier conversation requested retiring the tracker. Current supplied AGENTS.md
still mandates tracker updates and defaults requested completed packages to Applied.
Until explicitly reconciled, that contract remains in force. Proposed migration:
package manifests drive the app, generation readiness and actual submission become
separate fields, and tracker retirement updates AGENTS.md, guides, reusable prompts,
templates and tooling together. Do not silently implement either interpretation.
