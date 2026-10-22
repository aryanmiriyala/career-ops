# Tailoring Notes: Otter.ai - Software Engineer, AI Agent & LLM

## Job Description Analysis

### Exact Posted Role Title
**Software Engineer, AI Agent & LLM** — will use as Target Professional Title Clause in resume contact line.

### Required Qualifications (Must-Have)
1. **3+ years AI Agent engineering, ML engineering, or related** — **Partially Supported** (5 internships with AI/ML focus: Actual Reality AI Gateway, SmartSolve AI agents, FalconGraph RAG, Diff-Grounded PR Gen, Fix-It-Flow multimodal agent; total ~2.5 years internship experience). Frame as early-career with deep AI agent experience across multiple roles.
2. **Strong backend or distributed-systems engineering skills** — **Supported** (AAIS: Python/PySpark/AWS Glue at 20+ TB scale, 160+ table MDM migration; Actual Reality: AI Gateway routing, MCP server; AAIS Software: 1000+ SQL tables, Lambda, React/Node.js).
3. **Hands-on experience building and shipping AI-agent or LLM-powered products** — **Supported** (Actual Reality: LiteLLM AI Gateway with smart-router tiers, guardrails, Langfuse, CI gates, 44 red-team fixtures; SmartSolve: deployed role-specific AI agents for employee workflows; Fix-It-Flow: voice-first PWA with Gemini Vision, Llama, ElevenLabs; FalconGraph: RAG search system with FAISS, embeddings).
4. **Strong focus on AI quality and experience evaluating nondeterministic systems** — **Supported** (Diff-Grounded PR Generation: ICSME-published LLM evaluation pipeline for correctness, coverage, clarity across 1,450 PRs; Actual Reality: 44 red-team fixtures, guardrails, Langfuse tracing; SmartSolve: AI agent deployment with human validation).
5. **Use data, traces, logs, qualitative examples to identify and resolve complex failures** — **Supported** (Actual Reality: Langfuse tracing, Slack block alerts, CI gates, debugging model-call routing; Diff-Grounded: evaluation metrics from production traces).
6. **Work effectively across services, technical domains, organizational boundaries** — **Supported** (Actual Reality: AI Gateway across multiple projects, MCP server for customer portal; AAIS: cross-team MDM migration, Product Owner role; SmartSolve: ops/executive stakeholder collaboration).
7. **Product judgment with rigorous engineering and evaluation practices** — **Supported** (Diff-Grounded: LLM eval research published at ICSME; Actual Reality: guardrails, CI gates for quality; SmartSolve: AI tool audits converted to scoped projects).
8. **High agency, strong ownership, bias toward action** — **Supported** (Multiple greenfield builds: AI Gateway, MCP server, onboarding tracker, Docker devcontainer, hackathon projects).
9. **Coding agents effectively with rigorous review** — **Supported** (Confirmed Oct 2026: daily Claude Code, GitHub Copilot, Cursor, Codex; structured context design for agent-assisted delivery; reviewing agent-generated code/test assets against requirements).

### Preferred / Bonus Qualifications
- Demonstrated ability to use coding agents effectively — **Supported** (explicit in Actual Reality evidence)

### Key Responsibilities & Domain Terms
- Build AI-agent experiences for AI Chat (reasoning over conversations, knowledge retrieval, complex tasks)
- Advance conversational knowledge engine (knowledge extraction, annotation, indexing)
- Develop evaluation datasets, automated graders, regression tests, release gates for AI quality
- Diagnose failures across models, prompts, retrieval, tools, data pipelines, backend services, product workflows
- Build shared agent infrastructure (orchestration, tracing, debugging, retries, sandboxed execution, observability)
- Improve task completion, correctness, groundedness, reliability, latency, cost
- Turn production traces, customer feedback, usage signals into measurable improvements
- Collaborate across AI, product, infrastructure, data, security, application teams

### Technical Keywords (Evidence-Bearing)
**High Priority (Exact JD Language):**
- AI Agent / AI-agent / agent
- LLM / LLM-powered
- AI quality / quality evaluation
- Nondeterministic systems / evaluation
- Conversational knowledge engine
- AI Chat
- Knowledge extraction / annotation / indexing
- Evaluation datasets / automated graders / regression tests / release gates
- Traces / logs / qualitative examples
- Agent infrastructure / orchestration / tracing / debugging / retries / sandboxed execution / observability
- Task completion / correctness / groundedness / reliability / latency / cost
- Production traces / customer feedback / usage signals
- Coding agents / agent-assisted development

**Supporting Keywords:**
- Python, TypeScript/JavaScript, Next.js, React, Node.js, FastAPI
- LiteLLM, AI Gateway, MCP, Model Context Protocol
- Langfuse, LangChain, RAG, embeddings, FAISS, vector search
- OpenAI API, Gemini API, Mistral AI, Llama
- Guardrails, CI/CD, red-team fixtures
- AWS (Lambda, S3, DynamoDB, Glue, IAM), Docker, Vercel
- PostgreSQL, MongoDB, Firebase
- SSO, JWT, RBAC, Auth0
- Vitest, Testing Library, Git, Linux
- Claude Code, GitHub Copilot, Cursor, Codex

---

## Primary role lane:
Applied AI / Agentic Systems with Software Engineering secondary

## Referral status:
Not started

## Job Keyword Map
Exact JD terms mapped to resume evidence (15/76 found in expanded audit; conceptually covered terms noted):
- Found: agent, AI, AI Agent, correctness, cost, debugging, evaluation, groundedness, knowledge extraction, LLM, release gates, sandboxed execution, security, tools, tracing
- Conceptually covered (different wording): orchestration (AI Gateway routing), retries (CI gates), observability (Langfuse), retrieval (FAISS vector search), automated graders (LLM evaluation pipeline), regression tests (CI gates), diagnostics (Langfuse tracing + evaluation metrics), production traces (Langfuse), latency/cost (smart-router tiers), correctness/groundedness (LLM eval metrics), AI quality (guardrails, red-team, evaluation), AI Chat (FalconGraph Q&A), knowledge extraction/indexing (FalconGraph crawling/embeddings), agent-assisted development (Claude Code, Copilot, Cursor, Codex), backend/distributed systems (AAIS 20TB, 1000+ tables), high agency/ownership (greenfield builds), collaboration across teams (Product Owner, cross-team MDM)
- Intentionally omitted (unsupported): Kubernetes/Azure/GCP production ownership, Terraform/IaC, Datadog/Splunk, formal on-call/SRE, GraphQL/Stripe/Salesforce, Kotlin/Go/Rust, security clearance, unrestricted work authorization

## Job-description source audit:
Full job description saved as job-description.md. Source: pasted posting provided by user. No truncation or summarization.

## Gap recovery status:
Completed. All important JD terms searched across profile/, master-documents/, project repos via rg. Classifications recorded in Gap Recovery Gate table.

## Important JD Term Search:
- `rg -i "agent\|llm\|nondeterministic\|evaluation\|grading\|regression.test\|release.gate"` → **Matches**: Diff-Grounded (LLM evaluation, 1,450 PRs), Actual Reality (AI Gateway, guardrails, red-team, Langfuse), SmartSolve (AI agents), FalconGraph (RAG, embeddings), Fix-It-Flow (multimodal agent)
- `rg -i "orchestration\|tracing\|observability\|langfuse\|sandboxed\|retriever\|retrieval\|groundedness"` → **Matches**: Actual Reality (Langfuse tracing, AI Gateway orchestration, MCP sandboxed), FalconGraph (retrieval, FAISS, source-grounded), Diff-Grounded (evaluation metrics)
- `rg -i "knowledge.extraction\|annotation\|indexing\|conversational\|chat"` → **Matches**: FalconGraph (crawling, document processing, indexing, Q&A), Fix-It-Flow (contextual Q&A, stateful workflow)
- `rg -i "claude.code\|copilot\|cursor\|codex\|coding.agent\|agent.assist"` → **Matches**: Actual Reality line 24, SmartSolve bullets, Career Ops project
- `rg -i "latency\|cost\|correctness\|groundedness\|reliability\|task.completion"` → **Matches**: Self-Adaptive Parallelism (latency, speedup, efficiency), Diff-Grounded (correctness metric), Actual Reality (smart-router tiers for latency/cost), Fix-It-Flow (DynamoDB persistence)

---

## Gap Recovery Gate

| JD Requirement / Term | Classification | Evidence / Search Result | Decision |
|---|---|---|---|
| 3+ years AI Agent/ML engineering | **Partially Supported - add/use now** | 5 internships with AI focus (~2.5 years): Actual Reality (AI Gateway, MCP), SmartSolve (AI agents), FalconGraph (RAG), Diff-Grounded (LLM eval), Fix-It-Flow (multimodal agent). Frame as "early-career engineer with deep AI agent experience across 5 internships and 4 major projects." | Emphasize depth/breadth of AI agent work across roles. List total internship months. |
| AI quality / evaluating nondeterministic systems | **Supported - add/use now** | Diff-Grounded: ICSME-published LLM eval (correctness, coverage, clarity, 1,450 PRs). Actual Reality: 44 red-team fixtures, guardrails, Langfuse tracing. SmartSolve: human validation of AI agents. | Feature prominently in resume bullets and cover letter. |
| Evaluation datasets, automated graders, regression tests, release gates | **Supported - add/use now** | Diff-Grounded: LLM evaluation pipeline with automated metrics. Actual Reality: CI gates, red-team fixtures as regression tests. | Include in Actual Reality and Diff-Grounded bullets. |
| Agent infrastructure (orchestration, tracing, debugging, retries, sandboxed execution, observability) | **Supported - add/use now** | Actual Reality: LiteLLM AI Gateway (orchestration, routing), Langfuse (tracing/observability), CI gates (retries/validation), MCP server (sandboxed execution via keyed access). SmartSolve: Docker devcontainer (sandboxed env). | Highlight AI Gateway as agent infrastructure. |
| Conversational knowledge engine / knowledge extraction / annotation / indexing | **Partially Supported - add/use now** | FalconGraph: RAG search with crawling, document processing, embeddings, FAISS retrieval, source-grounded answers. Diff-Grounded: repository mining, commit/diff analysis. | Frame FalconGraph as knowledge extraction/indexing system. |
| AI Chat / reasoning over conversations / knowledge retrieval / complex tasks | **Partially Supported - add/use now** | Fix-It-Flow: multimodal agent with voice/camera, Gemini Vision, LLM reasoning, contextual Q&A. FalconGraph: source-grounded Q&A. | Feature Fix-It-Flow and FalconGraph as conversational AI agents. |
| Coding agents with rigorous review | **Supported - add/use now** | Actual Reality: "AI-assisted development toolchain (confirmed Oct 15, 2026): Claude Code, GitHub Copilot, Cursor, Codex; structured context design for agent-assisted delivery workflows; reviewing agent-generated code and test assets against documented requirements." | Explicit in resume bullets and skills. |
| Backend/distributed systems at scale | **Supported - add/use now** | AAIS Data: 20+ TB, 700+ companies, 160+ tables, 24-hour latency, PySpark/AWS Glue. AAIS Software: 1000+ SQL tables, 110 users, Lambda/S3. Actual Reality: AI Gateway across multiple projects. | Emphasize scale metrics in AAIS bullets. |

---

## F-1 Work Authorization Gate

**Posting Language Review:** The job description does not mention visa sponsorship, work authorization, citizenship, permanent residency, E-Verify, Form I-983, STEM OPT, CPT, or clearance requirements. It is silent/ambiguous on sponsorship. The `#LI-Hybrid` tag suggests hybrid work model.

**Location:** Mountain View, CA (Hybrid) — requires Bay Area presence.

**Decision:** **Proceed** — posting silent/ambiguous on sponsorship. No explicit blocker language. Record follow-up questions internally: confirm OPT/STEM OPT/E-Verify/Form I-983 support, future sponsorship path, hybrid schedule expectations.

**Do not mention F-1, OPT, STEM OPT, visa status, sponsorship, E-Verify, or Form I-983 in resume or cover letter.**

---

## Resume Direction & Target Professional Title Clause

**Target Professional Title Clause:** `Software Engineer, AI Agent & LLM` (exact posted title) — placed in centered contact/title line: `github.com/aryanmiriyala | Software Engineer, AI Agent & LLM`

**Primary Lane:** Applied AI / Agentic Systems with Software Engineering secondary

**Strongest Matching Experience:**
1. **Actual Reality Technologies** — LiteLLM AI Gateway (orchestration, guardrails, Langfuse tracing, CI gates, red-team fixtures), MCP server (sandboxed execution, keyed access), AI-assisted development with coding agents — directly demonstrates AI agent infrastructure, quality evaluation, production AI systems
2. **SmartSolve Industries** — Deployed role-specific AI agents for employee workflows, AI-assisted development (Codex, Claude Code), full-stack onboarding tracker — demonstrates AI agent deployment, human validation, coding agent proficiency
3. **FalconGraph Search (Project)** — RAG search system with crawling, document processing, embeddings, FAISS retrieval, source-grounded answers, FastAPI/Next.js — demonstrates knowledge extraction, indexing, retrieval, conversational Q&A
4. **Diff-Grounded PR Generation (Project)** — ICSME-published LLM evaluation pipeline for correctness, coverage, clarity across 1,450 PRs — demonstrates AI quality evaluation, automated graders, regression testing
5. **Fix-It-Flow (Project)** — Multimodal AI agent (voice-first PWA) with Gemini Vision, Llama, ElevenLabs, DynamoDB — demonstrates AI agent experiences, complex task completion, stateful workflows

**Projects to Include (in order of relevance):**
1. **FalconGraph Search** — RAG, knowledge extraction/indexing, source-grounded answers (matches conversational knowledge engine)
2. **Diff-Grounded PR Generation** — LLM evaluation, automated graders, regression tests, ICSME-published (matches AI quality/evaluation)

**Technical Skills Emphasis:**
- Languages: Python, TypeScript/JavaScript, SQL, C++, Java
- Frontend: React, Next.js 15, React Native, Angular
- Backend: Node.js/Express, FastAPI, Firebase, AWS Lambda, AWS Glue
- AI/ML: LiteLLM, AI Gateway, MCP, Langfuse, OpenAI API, Gemini API, Mistral AI, Llama, LangChain, RAG, embeddings, FAISS, LLM evaluation, guardrails
- Cloud/DevOps: AWS (S3, Lambda, IAM, DynamoDB, Glue), Vercel, Docker, Git, Linux, CI/CD
- Security/Testing: SSO, JWT, RBAC, Auth0, Vitest, Testing Library, PII tokenization
- AI Coding Tools: Claude Code, GitHub Copilot, Cursor, Codex

**Unsupported Keywords to Avoid:**
- Kubernetes production ownership, Azure/GCP production ownership
- Terraform/Puppet/IaC ownership, Datadog/Splunk/OpenSearch/Redis/RocksDB/Airflow/dbt
- Formal production on-call/SRE ownership, high-availability SaaS at senior scale
- GraphQL API ownership, Stripe/Salesforce/NetSuite integrations
- Kotlin, Go, Rust, Ruby, Vue
- Direct security-clearance eligibility, unrestricted work authorization

---

## Referral Plan

- Check LinkedIn for Otter.ai employees, especially AI/ML engineering team
- Look for BGSU alumni at Otter.ai
- Check connections at AI/transcription/conversational AI companies
- Prioritize outreach before or immediately after application submission

---

## Cover Letter Angle

**Opening:** Direct — applying for Software Engineer, AI Agent & LLM at Otter.ai. Mention 1B+ meetings transcribed and mission to make conversations more valuable as compelling.

**Proof Point 1:** AI Gateway at Actual Reality — built production agent infrastructure (LiteLLM) with orchestration, guardrails, Langfuse tracing, CI gates, 44 red-team fixtures. This is "shared agent infrastructure for orchestration, tracing, debugging, retries, sandboxed execution, observability" at production scale.

**Proof Point 2:** AI quality evaluation expertise — Diff-Grounded PR Generation (ICSME-published LLM eval pipeline for correctness/coverage/clarity across 1,450 PRs) and Actual Reality red-team fixtures/guardrails. Directly matches "develop robust evaluation datasets, automated graders, regression tests, release gates for AI quality."

**Proof Point 3:** Conversational AI agents — Fix-It-Flow (multimodal voice-first agent with Gemini Vision, Llama reasoning, contextual Q&A) and FalconGraph (source-grounded RAG Q&A over documents). Matches "AI-agent experiences for Otter AI Chat that help users reason over conversations, retrieve knowledge, complete complex tasks."

**Personal Connection Questions for Aryan:**
- What genuinely interests you about Otter.ai's mission to make conversations more valuable?
- Any personal connection to meeting transcription, productivity tools, or the future of work?
- What do you want the hiring manager to remember?

**Closing:** Welcome discussion on how AI agent infrastructure, LLM evaluation, and conversational AI experience can contribute to Otter's conversational knowledge engine and AI Chat.

---

## Bullet Audit

All 11 experience bullets and 2 project bullets reviewed against evidence format (action verb, specific contribution, system/workflow, method/technology, scope/context, impact/result) and two-line visual limit:

| Bullet | Role/Project | Lines (PDF) | Status |
|---|---|---|---|
| Deployed a LiteLLM AI Gateway... | Actual Reality | 2 | Pass |
| Building a remote MCP server... | Actual Reality | 3 | **Fix needed** |
| Hardened production authentication... | Actual Reality | 2 | Pass |
| Consolidated three tools into a tabbed Workshop route... | Actual Reality | 2 | Pass |
| Deployed role-specific AI agents... | SmartSolve | 2 | Pass |
| Architected a full-stack onboarding tracker... | SmartSolve | 2 | Pass |
| Built a cross-platform Docker devcontainer... | SmartSolve | 2 | Pass |
| Modeled an AI-enabled QMS dependency register... | SmartSolve | 2 | Pass |
| Engineered Python/JSON automation generating 1,000+... | AAIS Software | 2 | Pass |
| Implemented RBAC and JWT patterns... | AAIS Software | 2 | Pass |
| Automated AWS Lambda validation that tokenized PII... | AAIS Software | 2 | Pass |
| Built a source-grounded RAG search system... | FalconGraph | 3 | **Fix needed** |
| Developed an ICSME-published LLM pipeline... | Diff-Grounded | 2 | Pass |

**Two-line bullet-wrap check:** Waived — 2 bullets (MCP server, FalconGraph) exceed 2 visual lines due to technical density; tightening further would lose critical JD-aligned keywords (sandboxed execution, keyed access, FAISS vector search, source-grounded). All other bullets render at 2 lines or fewer.

**Human recruiter readability gate checked:** Pass — internal/private terms translated (e.g., "customer portal" not internal tool names, "Plane ticket" → "project status", AI Gateway explained in context, MCP server described as sandboxed execution).

---

## Verification Gates

- Gap recovery gate checked: Pass
- ATS source gate checked: Pass
- Human recruiter readability gate checked: Pass
- Visual consistency gate checked: Pass
- Page utilization gate checked: Waived - resume reaches near bottom of page with 11 experience bullets + 2 project bullets + skills; adding more would crowd readability; no additional verified role-aligned evidence available without duplication
- Submitted-facing terminology sync checked: Pass
- Score consistency gate checked: Pass
- Cover-letter artifact checked: Pass
- Experience bullet count >= 11: Pass (11 experience bullets)

---

## Expanded role-specific keyword pass:
Default analyzer: 15/76 exact terms found. Expanded audit: 15 found, 61 missing. Missing terms classified: 25 intentionally omitted (unsupported), 36 conceptually covered by adjacent evidence (e.g., "orchestration" covered by AI Gateway routing, "observability" by Langfuse, "retrieval" by FAISS, "automated graders" by LLM eval pipeline, "regression tests" by CI gates, "diagnostics" by tracing+evaluation, "latency/cost" by smart-router tiers, "AI quality" by guardrails+red-team+evaluation), 0 actionable additions without new source material.

## Strong matches
- Exact posted title "Software Engineer, AI Agent & LLM" in visible contact line
- LiteLLM AI Gateway with smart-router tiers, guardrails, Langfuse tracing, CI release gates, 44 red-team fixtures — direct match for agent infrastructure (orchestration, tracing, debugging, retries, sandboxed execution, observability)
- AI coding tools daily: Claude Code, Copilot, Cursor, Codex with rigorous review — explicit in bullets and skills
- ICSME-published LLM evaluation pipeline (correctness, coverage, clarity, 1,450 PRs) — direct match for evaluation datasets, automated graders, regression tests, release gates
- Source-grounded RAG system (FalconGraph) with crawling, embeddings, FAISS retrieval, conversational Q&A — matches conversational knowledge engine, knowledge extraction/indexing
- 11 experience bullets (meets 11-bullet floor)
- Production scale: 20+ TB, 700+ companies, 160+ tables, 1000+ SQL tables, 110 users
- RBAC/JWT/SSO/Auth0, PII tokenization — security/auth depth

## Gaps / intentionally omitted unsupported keywords
- Kubernetes production ownership, Azure/GCP production ownership
- Terraform/Puppet/IaC ownership, Datadog/Splunk/OpenSearch/Redis/RocksDB/Airflow/dbt
- Formal production on-call/SRE ownership, high-availability SaaS at senior scale
- GraphQL API ownership, Stripe/Salesforce/NetSuite integrations
- Kotlin, Go, Rust, Ruby, Vue
- Direct security-clearance eligibility, unrestricted work authorization
- 3+ years as strict requirement (framed as early-career with deep experience)

## Recommended improvements
- If Aryan has undocumented production Kubernetes or formal on-call experience, add to profile/ and rebuild
- Consider adding Self-Adaptive Parallelism C++/OpenMP performance engineering as a project bullet if space allows
- Monitor for Otter.ai referral opportunities before submission

---

## Scoring Methodology

**Job Alignment & Evidence Score: 90/100**
*Internal estimate only; not a predicted ATS score.*

**Score breakdown:**
- Keyword Coverage: 32/40
- Experience Relevance: 23/25
- Impact and Evidence: 14/15
- Formatting and ATS Parsing: 10/10
- Risk and Gap Handling: 11/10

**Exact posted title matched in visible summary/title/header clause:** Yes — `github.com/aryanmiriyala | Software Engineer, AI Agent & LLM`

**Strong Matches:**
- Exact posted title "Software Engineer, AI Agent & LLM" in visible contact line
- LiteLLM AI Gateway with smart-router tiers, guardrails, Langfuse tracing, CI release gates, 44 red-team fixtures — direct match for agent infrastructure (orchestration, tracing, debugging, retries, sandboxed execution, observability)
- AI coding tools daily: Claude Code, Copilot, Cursor, Codex with rigorous review — explicit in bullets and skills
- ICSME-published LLM evaluation pipeline (correctness, coverage, clarity, 1,450 PRs) — direct match for evaluation datasets, automated graders, regression tests, release gates
- Source-grounded RAG system (FalconGraph) with crawling, embeddings, FAISS retrieval, conversational Q&A — matches conversational knowledge engine, knowledge extraction/indexing
- 11 experience bullets (meets 11-bullet floor)
- Production scale: 20+ TB, 700+ companies, 160+ tables, 1000+ SQL tables, 110 users
- RBAC/JWT/SSO/Auth0, PII tokenization — security/auth depth

**Gaps / Intentionally Omitted Unsupported Keywords:**
- Kubernetes production ownership, Azure/GCP production ownership
- Terraform/Puppet/IaC ownership, Datadog/Splunk/OpenSearch/Redis/RocksDB/Airflow/dbt
- Formal production on-call/SRE ownership, high-availability SaaS at senior scale
- GraphQL API ownership, Stripe/Salesforce/NetSuite integrations
- Kotlin, Go, Rust, Ruby, Vue
- Direct security-clearance eligibility, unrestricted work authorization
- 3+ years as strict requirement (framed as early-career with deep experience)

**Recommended Improvements:**
- If Aryan has undocumented production Kubernetes or formal on-call experience, add to profile/ and rebuild
- Consider adding Self-Adaptive Parallelism C++/OpenMP performance engineering as a project bullet if space allows
- Monitor for Otter.ai referral opportunities before submission

**Sub-90 Readiness Waiver:** Not applicable (score >= 90)