# Tailoring Notes - Fireflies.ai Junior AI Engineer

## Job Description Summary
- **Company:** Fireflies.ai
- **Role:** Junior AI Engineer
- **Location:** Remote, based in United States
- **Salary:** $80–90K/yr
- **Work Authorization:** US work authorization required, Open to candidates with OPT
- **Apply by:** November 19, 2026

## Primary role lane:
Applied AI/Junior AI Engineer with LLM evaluation, RAG, and AI Gateway infrastructure emphasis.

## ## F-1 Work Authorization Gate
**Status:** PROCEED
- Job posting explicitly states: "Open to candidates with OPT"
- No blocker language (no-sponsorship, citizen-only, permanent-resident-only, authorization-for-any-employer, clearance-only)
- Remote US-based role compatible with F-1 OPT/STEM OPT
- No work-authorization language in submitted artifacts

## ## Referral Plan
**Referral status:** Not started
**Referral Target / Source:** Not identified yet
**Next Referral Follow-up:** To be scheduled

## ## Job Keyword Map
Built from full job description:
- **Exact Posted Title:** Junior AI Engineer
- **Required Skills:** Python, PyTorch, TensorFlow, LangChain, LlamaIndex, vector databases (Pinecone, Chroma, Supabase pgvector), RAG, OpenAI, Anthropic, LLM, fine-tuning, model evaluation, prompt engineering
- **Responsibilities:** AI & LLM Integration, Model Pipeline Development, Data Engineering & Preprocessing, Collaboration & Testing, Research & Prototyping
- **Backend/Tools:** RESTful APIs, Git, backend integration
- **Domain:** Machine learning, NLP, data engineering, AI integration
- **Work Authorization:** OPT, STEM OPT (internal tracker only)

## Job-description source audit:
Full employer-provided role text saved in `job-description.md`. No summarization or truncation. Metadata block added above posting.

## ## Gap Recovery Gate
**Gap recovery status:** Completed and documented below.

## Important JD Term Search:
Searched `profile/evidence-index.md`, `profile/projects-master.md`, `profile/experience-master.md`, `profile/skills-master.md` for:
- Pinecone, Chroma, Supabase pgvector → ChromaDB (RAG App Review), FAISS (FalconGraph), LlamaIndex (IRIS) found; Pinecone/Supabase not used
- Anthropic / Claude API → No production usage found
- Fine-tuning → No production fine-tuning found; evaluation adjacent only
- NLP, Machine learning → Covered by Diff-Grounded PR, RAG App Review, FalconGraph, MarioRL
- Vector database → FAISS, ChromaDB, LlamaIndex usage verified

**Classifications:**
- Supported - add/use now: Python, PyTorch, TensorFlow, LangChain, LlamaIndex, RAG, OpenAI, LLM, prompt engineering, RESTful APIs, Git, backend integration, data engineering, AI integration, machine learning, NLP, Junior AI Engineer title
- Unsupported - omit: Pinecone, Supabase pgvector, Anthropic, fine-tuning, OPT/STEM OPT (internal only)

## ## Bullet Audit
**Two-line bullet-wrap check:** Pass - All experience and project bullets render as ≤2 visual PDF lines in compiled resume (verified via `pdftotext -layout`).

## ## Scoring Methodology
Internal readiness estimate (not a predicted ATS score).

## Job Alignment & Evidence Score: 94/100

Internal estimate only; not a predicted ATS score.

## Score breakdown
- Keyword coverage: 36/40
- Experience relevance: 24/25
- Impact and evidence: 14/15
- Formatting and ATS parsing: 10/10
- Risk and gap handling: 10/10

## Expanded role-specific keyword pass:
Expanded audit covered: LiteLLM, AI/model gateway, guardrails, Langfuse, MCP, Gemini API, Mistral AI, Playwright, Node.js, Next.js, PostgreSQL, Drizzle ORM, SSO, AWS Glue/S3/Lambda/IAM, PySpark, Docker, Codex/Claude Code/Copilot/Cursor, CI/CD, ChromaDB, FAISS, embeddings, vector search, Sentence Transformers - all found in resume.

## Strong matches
- Exact role title in header
- Python, PyTorch, TensorFlow, LangChain, LlamaIndex, RAG, OpenAI API
- LLM evaluation pipelines (41+ test suites, LLM-as-judge, ICSME-published)
- AI Gateway infrastructure (LiteLLM, guardrails, Langfuse, routing tiers, MCP)
- Vector search (FAISS, ChromaDB, embeddings)
- RAG systems (FalconGraph, IRIS)
- AI-assisted development (Codex, Claude Code, Copilot, Cursor)
- Data engineering at scale (20+ TB, 160+ tables, PySpark, AWS Glue)
- Full-stack (Next.js, React, PostgreSQL, FastAPI, Node.js)
- 5 internships + current FT role, 4.0 GPA MS/BS CS

## Gaps / intentionally omitted unsupported keywords
- Pinecone (vector DB) - ChromaDB + FAISS cover competency
- Supabase pgvector - not used
- Anthropic / Claude API - no production usage
- Fine-tuning - evaluation only, no training
- Direct "Large Language Model" phrase - "LLM" used throughout

## Recommended improvements
None - score ≥ 90.

## Verification Gates Record
- Gap recovery gate checked: Pass
- ATS source gate checked: Pass
- Human recruiter readability gate checked: Pass
- Visual consistency gate checked: Pass
- Page utilization gate checked: Pass
- Submitted-facing terminology sync checked: Pass
- Score consistency gate checked: Pass
- Cover-letter artifact checked: Pass

## Validation Results
- Resume PDF: 1 page, 101KB, text-extractable
- Cover letter PDF: 1 page, 41KB, text-extractable
- `automation/analyze_application_keywords.py` completed

## Files Created
- `job-description.md`
- `resume.tex` / `resume.pdf`
- `cover-letter.md` / `cover-letter.tex` / `cover-letter.pdf`
- `tailoring-notes.md` (this file)

## Next Steps
1. Run `python3 automation/validate_application_package.py application-packages/Fireflies.ai/Junior-AI-Engineer`
2. Commit and push
3. Update tracker status to "Applied" when submitted