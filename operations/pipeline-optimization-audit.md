# Pipeline Optimization Audit

Date: 2026-08-27

Scope: Reduce token use and model spend in the Career Ops application-package workflow while preserving the current quality bar: truthful sourcing, one-page ATS-safe resumes, strong recruiter readability, cover-letter quality, validation, tracker updates, and F-1 risk handling.

This is not an application package. It is a design audit for the pipeline itself.

## Executive Recommendation

The current pipeline should become a mostly deterministic retrieval, scoring, and validation system with small-model calls only for narrow judgment tasks. The expensive model should stop being the default orchestrator for every source read, keyword judgment, and quality gate.

Recommended architecture:

1. Keep the existing repo rules and validator, but make them machine-readable.
2. Add a local ATS alignment engine that combines lexical exact-term coverage, weighted phrase extraction, TF-IDF/BM25-style matching, and semantic embedding similarity.
3. Add a source-evidence index builder so profile/project evidence is retrieved before the model sees it.
4. Add Langfuse tracing for every LLM call, retrieval step, validation result, cost, latency, and final score.
5. Add LiteLLM only if we want a provider/model router and budget caps across OpenAI, Anthropic, Gemini, local models, or future cheap APIs.
6. Add a small eval set with Promptfoo or Pydantic Evals before changing prompts or model tiers.
7. Use OpenAI Batch API and prompt caching for low-urgency repeated scoring or corpus-indexing work.

The highest-return first build is local scoring, not agentic auto-apply. Tools like Tsenta are useful to study at the public product level, but the repo should not copy or bypass proprietary systems. Publicly visible product features suggest that the durable moat is speed plus receipts plus ATS coverage. For this repo, the immediate moat should be quality-controlled tailoring with cheap deterministic evidence retrieval.

## Current Repo Findings

Local inspection:

- `automation/analyze_application_keywords.py` is deterministic and useful, but it is mostly exact-term coverage against a fixed term list plus optional role-specific terms.
- `automation/validate_application_package.py` is strong on artifact completeness, ATS-safe LaTeX structure, one-page PDF validation, score consistency, F-1 submitted-artifact exclusions, and application-answer voice checks.
- `automation/application_package_brief.py` already supports compact package audits and avoids dumping whole artifacts.
- `automation/audit_token_hotspots.py` exists and is useful. Running it on 2026-08-27 showed 506 scanned text files and 415,648 total words.
- The largest context sink is `application-packages/` at 292,662 words. `job-search/` has 62,605 words, `profile/` has 29,762 words, and `AGENTS.md` alone has 9,684 words.
- There is no project dependency manifest found via `rg --files` / `find` for `requirements*.txt`, `pyproject.toml`, or `package.json`.
- Local Python imports available now: `sklearn`, `numpy`, `pandas`, `sentence_transformers`, `spacy`, `openai`.
- Local Python imports missing now: `langfuse`, `litellm`, `rank_bm25`, `keybert`, `yake`.

Implication: we can prototype a local semantic/lexical scorer immediately using installed packages, then optionally add pinned dependencies for Langfuse, LiteLLM, BM25, and keyword extraction.

## Public Tool Decomposition

This section reverse-engineers only from public product pages and docs. It does not rely on private behavior, hidden APIs, protected code, or bypassing product controls.

### Tsenta

Public claims point to four core capabilities:

- Find: monitor large numbers of company career pages and ATS sources directly.
- Prep: read the JD, identify ATS/recruiter keywords, tailor resume and cover letter from true user background, and show a diff before submission.
- Apply: fill ATS forms and upload documents across many ATSes.
- Track: store receipts, route replies, and update application status.

Useful ideas for this repo:

- Store a receipt for every generated package: JD source, resume version, cover letter version, application answers, score, validation result, and tracker status.
- Add a review gate for high-risk fields like sponsorship, authorization, relocation, salary, and application questions.
- Separate matching from writing. Matching should be cheap and deterministic.

Not recommended:

- Do not build unsupervised auto-submit yet. Aryan's F-1/OPT constraints and application-question nuance make review more valuable than pure volume.
- Do not attempt proprietary ATS bypassing. Use public ATS APIs, browser automation only with user approval, and normal form workflows.

Sources:

- https://tsenta.com/
- https://tsenta.com/ai-agent
- https://tsenta.com/ai-disclosure
- https://www.ycombinator.com/companies/tsenta

### Jobscan, Resume Worded, SkillSyncer, Rezi

Public product docs converge on these scoring dimensions:

- Hard skills and keywords from the JD.
- Job title and seniority alignment.
- Education and degree match when the JD specifies it.
- Soft skills and role language.
- Resume parseability, file format, sections, dates, contact info, and formatting.
- Bullet quality, measurable achievements, active voice, filler language, and word count.
- Missing keyword suggestions and scan history.

Important lesson: real ATS systems do not expose a universal employer score. These products use heuristic scores as feedback tools. Our internal `Job Alignment & Evidence Score` should stay explicitly internal and should become more reproducible.

Sources:

- https://support.jobscan.co/hc/en-us/articles/42869628183699-What-exactly-is-being-checked-Can-you-rate-my-resume
- https://www.jobscan.co/resume-scanner
- https://resumeworded.com/llm-info
- https://skillsyncer.com/features
- https://skillsyncer.com/pricing
- https://www.rezi.ai/rezi-docs/the-rezi-score-explained

## Tooling Candidates

### Langfuse

Use for observability, prompt management, evals, datasets, traces, and cost tracking. Langfuse docs state that traces can include LLM calls, retrieval, embeddings, API calls, and tool calls. It also supports dashboards, alerts, model usage, cost tracking, custom scores, prompt management, experiments, and self-hosting.

Best fit here:

- Trace each application package run as one session.
- Add spans for JD parsing, eligibility check, keyword extraction, evidence retrieval, resume drafting, cover letter drafting, validation, score calculation, and tracker update.
- Attach custom scores: lexical coverage, semantic coverage, evidence-grounding confidence, unsupported-term count, validator pass/fail, page utilization, final alignment score.
- Track cost by model and stage.

Risk:

- Adds an external service or local self-hosting burden.
- For sensitive career data, self-hosting or careful masking is preferable.

Sources:

- https://langfuse.com/docs
- https://langfuse.com/docs/observability/features/token-and-cost-tracking

### LiteLLM

Use only if we need model routing, provider abstraction, spend tracking, budget controls, and fallbacks across many model providers. LiteLLM docs describe spend tracking across many LLMs and custom pricing definitions.

Best fit here:

- Route low-risk calls to cheap models.
- Reserve expensive models for final writing or hard evidence judgment.
- Add per-run and per-stage spend caps.
- Send usage data to Langfuse if using the Langfuse integration path.

Risk:

- Adds another moving part. If this repo mostly runs inside Codex today, LiteLLM is useful only after we create standalone scripts that call model APIs directly.

Source:

- https://github.com/BerriAI/litellm-docs/blob/main/docs/proxy/cost_tracking.md

### Promptfoo

Use for prompt and model regression testing. Promptfoo docs position it as an open-source CLI/library for evals, red-teaming, caching, concurrency, CI, custom providers, and assertions including deterministic checks, embeddings similarity, and LLM rubrics.

Best fit here:

- Evaluate resume-summary prompts, keyword-map extraction prompts, cover-letter prompts, and application-answer prompts against saved package examples.
- Compare cheap model outputs against current high-quality outputs before changing defaults.
- Keep local, repeatable eval cases.

Sources:

- https://www.promptfoo.dev/docs/intro/
- https://www.promptfoo.dev/docs/configuration/expected-outputs/

### Pydantic Evals

Use if we want Python-native evals instead of YAML-driven evals. Pydantic docs describe datasets, cases, experiments, and evaluators, including deterministic and LLM-as-judge evaluators. Agentic evaluators can check tool-call behavior when OpenTelemetry spans are available.

Best fit here:

- Code-first tests for "given this JD and evidence index, did the pipeline select the right evidence and omit unsupported claims?"
- Regression tests for source-grounding and F-1 blocker handling.

Sources:

- https://pydantic.dev/docs/ai/evals/evals/
- https://pydantic.dev/docs/ai/evals/evaluators/agentic/

### Sentence Transformers

Use for local semantic matching. The installed local environment already has `sentence_transformers`. Its docs support semantic textual similarity and semantic search using embeddings plus cosine similarity.

Best fit here:

- Embed JD requirement chunks and profile evidence chunks.
- Retrieve likely evidence before opening large files.
- Score adjacent evidence when exact wording is missing, such as "data pipelines" vs "ETL workflows" or "auth/session reliability" vs "authentication middleware."

Risk:

- Semantic similarity can over-credit unsupported claims. It should propose evidence candidates, not write resume claims by itself.

Sources:

- https://www.sbert.net/docs/sentence_transformer/usage/semantic_textual_similarity.html
- https://www.sbert.net/examples/sentence_transformer/applications/semantic-search/README.html

### scikit-learn TF-IDF

Use for cheap lexical matching. scikit-learn documents cosine similarity as the normalized dot product and notes it is common for TF-IDF document similarity.

Best fit here:

- Build a deterministic JD-to-resume and JD-to-evidence lexical score.
- Extract n-gram overlap and missing phrase coverage without an LLM.
- Detect keyword stuffing by comparing repeated terms against unique evidence-bearing terms.

Source:

- https://scikit-learn.org/stable/modules/metrics.html

### BM25

BM25 is a stronger lexical retrieval model than raw substring matching for ranking evidence chunks. `rank_bm25` is not installed locally, but its GitHub docs show an easy Python package with Okapi BM25 and variants.

Best fit here:

- Rank profile/project chunks for each JD requirement.
- Replace model-driven "find me evidence" source reads with a deterministic top-k retrieval step.

Source:

- https://github.com/dorianbrown/rank_bm25

### KeyBERT / YAKE

Use for keyword extraction if the built-in repeated-phrase extraction becomes insufficient. KeyBERT uses BERT embeddings and cosine similarity to identify representative keyphrases. YAKE is statistical and corpus-independent.

Best fit here:

- Extract JD keyword candidates before classification into required, preferred, title, education, domain, tools, and unsupported terms.

Risk:

- They add dependencies and may produce noisy phrases. Start with sklearn n-grams and spaCy noun chunks first.

Sources:

- https://github.com/MaartenGr/KeyBERT
- https://liaad.github.io/yake/docs/Documentation/core/yake

### BAML / Instructor / Structured Outputs

Use structured-output tooling only if JSON reliability becomes a problem. BAML publicly positions itself as a DSL for reliable typed LLM outputs across models. OpenAI native Structured Outputs may already be enough if direct API scripts are built.

Best fit here:

- Job keyword map schema.
- Gap recovery schema.
- Tailoring-note section schema.
- Application-question answer schema.

Source:

- https://docs.boundaryml.com/home

## OpenAI Cost Levers

Official OpenAI documentation currently recommends the GPT-5.6 family this way:

- `gpt-5.6-sol`: flagship model for complex professional work.
- `gpt-5.6-terra`: balance intelligence and cost.
- `gpt-5.6-luna`: cost-sensitive high-volume workloads.

The model page lists current prices as:

- `gpt-5.6-sol`: $4 input / $20 output per million tokens.
- `gpt-5.6-terra`: $2 input / $12 output per million tokens.
- `gpt-5.6-luna`: $0.20 input / $1.20 output per million tokens.
- `text-embedding-3-small`: $0.02 per million tokens.

Prompt caching can reduce latency and input cost when requests share a stable prefix. Official docs state cached input can be discounted up to 90%, caching is enabled by default for supported models, and cache reuse requires the rendered prompt prefix to match. The docs also recommend keeping stable developer instructions and shared reference material first, placing changing content later, keeping tool definitions stable, and using stable cache keys.

The Batch API is useful for low-urgency work. Official docs state it runs asynchronous API requests and search snippets state a 24-hour completion window with a 50% discount. This fits nightly embedding refreshes, benchmark/eval runs, and bulk application-package audits, not interactive drafting.

Sources:

- https://developers.openai.com/api/docs/models
- https://developers.openai.com/api/docs/models/text-embedding-3-small
- https://developers.openai.com/api/docs/guides/prompt-caching
- https://developers.openai.com/api/reference/resources/batches

## Proposed Pipeline Redesign

### Stage 0: Package Intake

Inputs:

- Full JD text or URL.
- Optional application questions.
- Optional company/product/referral context.

Outputs:

- `job-description.md`.
- `run.json` with package ID, source URL, timestamp, and mode.

LLM use:

- None required for saved JD.
- Cheap model only if extracting metadata from messy pasted text fails.

### Stage 1: Deterministic JD Parsing

Use local code first:

- Normalize text.
- Detect title, company, location, employment type, internship/full-time signal, visa/sponsorship constraints, clearance constraints, degree constraints, salary/location constraints.
- Extract tools and hard skills from a curated ontology plus n-gram frequencies.
- Extract responsibilities and domain terms via noun chunks and repeated phrase scoring.
- Separate boilerplate from evidence-bearing terms.

Potential implementation:

- `automation/extract_job_requirements.py`
- Output `job-keyword-map.json` and `expanded-keywords.txt`.

LLM use:

- `gpt-5.6-luna` or equivalent cheap model for ambiguous requirement classification only.

### Stage 2: Evidence Retrieval

Build an indexed local corpus from:

- `profile/evidence-index.md`
- targeted sections of `profile/experience-master.md`
- targeted sections of `profile/projects-master.md`
- `profile/skills-master.md`
- selected project repos when explicitly routed or when a term search points there

Use:

- exact match for tools
- TF-IDF n-gram cosine for lexical similarity
- BM25 once dependency is added
- sentence-transformers embeddings for semantic candidates

Output:

- `evidence-match-report.json`
- A compact table for each JD requirement: exact match, semantic candidates, source file, line/section, confidence, and whether the term can be used in submitted artifacts.

LLM use:

- None for retrieval.
- Cheap model to classify "supported", "likely built but undocumented", or "unsupported" from retrieved evidence.
- Expensive model only when evidence conflicts or is high-risk.

### Stage 3: ATS Alignment Score

Replace the current mostly manual score with a reproducible calculation:

- 30 points keyword coverage: required tools, hard skills, exact title/domain phrases, weighted by JD importance.
- 20 points semantic evidence coverage: requirement chunks have matching evidence chunks above threshold.
- 20 points experience relevance: role lane, internship/work evidence, recency, employer-backed bullets.
- 15 points impact and recruiter readability: action verbs, concrete system, method, scope, result, no vague responsibility-only bullets.
- 10 points formatting and parseability: one-page PDF, text extraction, canonical layout, no tables/graphics/hidden text, section markers.
- 5 points risk handling: F-1 gate, unsupported claims omitted, source limitations recorded.

Store both the machine score and final strategist override:

- `ats-alignment.json`: deterministic scores and explanations.
- `tailoring-notes.md`: final internal score, with any human/LLM override justified.

LLM use:

- None for deterministic base.
- Cheap model for bullet readability classification.
- Strong model for final override only if the deterministic result and human judgment disagree.

### Stage 4: Drafting

Resume generation should use retrieved evidence capsules, not broad profile reads.

Inputs to the model:

- JD metadata and keyword map.
- Top evidence candidates with source IDs.
- Canonical resume constraints in compact machine-readable form.
- Existing master resume sections only when required.

LLM use:

- `gpt-5.6-terra` or equivalent mid-tier for resume and cover-letter drafting.
- `gpt-5.6-sol` only for unusually hard applications: senior mismatch, eligibility risk, sparse evidence, application questions with high stakes, or final strategy pass.

### Stage 5: Validation

Keep current validator, but add:

- `job-keyword-map.json` exists and is referenced.
- `evidence-match-report.json` exists.
- `ats-alignment.json` score math matches tailoring notes.
- LLM usage and cost summary exists when direct API scripts are used.
- "No broad source dump" gate: package notes should record retrieval inputs instead of entire source files.

LLM use:

- None.

### Stage 6: Observability And Evals

Trace the full run:

- `application_package_id`
- mode
- model per stage
- prompt version
- input/output/cached tokens
- cost
- latency
- retrieved sources
- deterministic scores
- validator output
- final status

Add eval datasets:

- 10 completed strong packages across lanes.
- 5 packages with known gaps.
- 5 F-1/sponsorship blocker examples.
- 5 application-question examples.

Metrics:

- unsupported claim count must be zero.
- validator pass must be true.
- one-page resume must be true.
- exact hard-skill coverage target by lane.
- semantic requirement coverage target.
- final answer avoids banned application-answer phrasing.
- token budget per package.
- cost per package.

Use Promptfoo for quick model/prompt matrix tests. Use Pydantic Evals if we want Python-native regression tests that share repo helper functions.

## Model Routing Policy

Suggested default routing:

- Deterministic Python: JD parsing, keyword extraction, source retrieval, ATS score, validator, tracker update.
- Local sentence-transformers: semantic matching and evidence retrieval.
- `text-embedding-3-small`: optional persistent embeddings if local embeddings are too slow or inconsistent.
- Cheap model such as `gpt-5.6-luna`: JD cleanup, keyword classification, simple gap labels, application tracker summaries, first-pass package briefs.
- Mid-tier model such as `gpt-5.6-terra`: resume bullet drafting, cover-letter drafting, application-answer drafting.
- Strong model such as `gpt-5.6-sol`: final recruiter-strategy pass, hard eligibility decisions, difficult evidence conflicts, final package QA.
- Batch API: nightly package audits, eval suites, bulk keyword-map generation, embedding refreshes.

Do not use an expensive model for:

- reading the full tracker
- reading historical package directories
- computing exact keyword coverage
- finding terms in source files
- checking PDF page count
- counting bullets
- checking generated artifacts

## Implementation Plan

### Phase 1: Local ATS scorer, no new paid API dependency

Build:

- `automation/extract_job_requirements.py`
- `automation/build_evidence_index.py`
- `automation/score_application_alignment.py`
- `automation/requirements.txt` or `pyproject.toml`

Use installed packages first:

- `sklearn` for TF-IDF and cosine similarity.
- `sentence_transformers` for semantic similarity.
- `spacy` for noun chunks/entities if the installed model exists, otherwise use regex/n-grams.

Expected value:

- Large reduction in model context because the model receives retrieved evidence instead of broad source files.
- More reproducible ATS score.
- Better missing-keyword reporting without stuffing unsupported terms.

### Phase 2: Langfuse instrumentation

Build:

- optional dependency group for `langfuse`
- `automation/llm_observability.py`
- `.env.example` entries for `LANGFUSE_PUBLIC_KEY`, `LANGFUSE_SECRET_KEY`, `LANGFUSE_HOST`
- trace wrappers around any direct LLM scripts
- custom scores for validator, lexical coverage, semantic coverage, final score, and unsupported-term count

Expected value:

- Know cost per application package.
- Identify which stage consumes tokens.
- Compare prompt versions and model tiers over time.

### Phase 3: Eval harness

Build either:

- `evals/promptfooconfig.yaml`

or:

- `automation/evals/` with Pydantic Evals cases

Start with 20-25 frozen examples from existing packages, but store only compact inputs and expected outcomes. Do not use full historical packages as default source context.

Expected value:

- We can test cheaper models before using them in production package generation.
- Prompt changes become measurable.

### Phase 4: Optional LiteLLM router

Build only after direct API scripts exist:

- LiteLLM config with model aliases: `cheap`, `draft`, `judge`, `embed`.
- Budget caps per run.
- Provider fallback policy.
- Langfuse integration for trace/cost visibility.

Expected value:

- Easier multi-provider tests.
- Hard spend caps.
- Model changes without editing pipeline scripts.

## Data Model Proposal

Add package-local generated files:

- `job-keyword-map.json`
- `expanded-keywords.txt`
- `evidence-match-report.json`
- `ats-alignment.json`
- `run-cost.json`
- `application-receipt.md`

Suggested `ats-alignment.json` shape:

```json
{
  "version": "career-ops-ats-score-v1",
  "package": "application-packages/Company/Role",
  "scores": {
    "keyword_coverage": 0,
    "semantic_evidence": 0,
    "experience_relevance": 0,
    "impact_readability": 0,
    "formatting_ats": 0,
    "risk_handling": 0,
    "total": 0
  },
  "requirements": [
    {
      "term": "Python",
      "category": "hard_skill",
      "jd_weight": 3,
      "resume_exact": true,
      "evidence_status": "supported",
      "evidence_sources": ["profile/evidence-index.md#AAIS"],
      "semantic_score": 0.91
    }
  ],
  "unsupported_terms": [],
  "notes": []
}
```

## Risks And Guardrails

- Semantic matching must not become claim generation. It should retrieve candidates and label confidence, not authorize unverified resume claims alone.
- Scores must remain internal. Public ATS tools themselves describe scores as practical feedback, not actual employer decisions.
- F-1 and sponsorship logic should stay deterministic and conservative.
- Langfuse traces may contain sensitive resume and application material. Use self-hosting or masking if this becomes more than local experimentation.
- Commercial tool feature claims may be marketing-heavy. Use them as product hints, not ground truth.
- Adding dependencies without pinning versions will reduce reproducibility. Add a manifest before relying on them.

## Final Recommendation

Start with Phase 1. It provides the biggest cost and token reduction without introducing external services. Then add Langfuse to measure actual spend. Only add LiteLLM once there are standalone LLM-calling scripts to route.

The practical target should be:

- 70-85% of package work done by deterministic scripts and local embeddings.
- cheap model for extraction/classification.
- mid-tier model for first drafts.
- strong model only for final strategy and hard cases.
- every run measured for tokens, cost, latency, validation, and score drift.

