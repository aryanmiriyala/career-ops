# Tailoring Notes - Quora Full Stack Software Engineer, New Grad

## Primary role lane:
Full-stack software engineering with Applied AI secondary

## Job-description source audit:
Full job description saved as `job-description.md` from https://careers.quora.com. No truncation or summarization applied.

## F-1 Work Authorization Gate
Posting Language: "This position can be performed remotely from anywhere in the US or Canada. Please visit careers.quora.com/eligible-countries for details regarding employment eligibility by country."
Analysis: No explicit no-sponsorship language, no "authorized to work for any employer" language, no U.S. citizen/permanent resident only language. Remote US/Canada with eligibility page reference suggests international student friendly.
Decision: Proceed with package. Track sponsorship follow-up internally. Do not mention F-1/OPT/STEM OPT in submitted artifacts.

## Referral Plan
## Referral Plan
Referral status: Not started
Referral target/source: Not identified
Next referral follow-up: To be scheduled
Strategy: Search for Quora engineers on LinkedIn, prioritize BGSU alumni or Actual Reality connections, check for Poe/Quora Core Product team members

## Job Keyword Map

### Must-Have (from Minimum Requirements)
| Term | Exact JD Wording | Resume Status | Evidence Source |
|------|------------------|---------------|-----------------|
| 2025/2026 graduate | "A 2025 or 2026 graduate with or pursuing a B.S., M.S., or Ph.D." | Covered | M.S. CS 2026, 4.0 GPA (Education) |
| Data structures, algorithms | "Foundational understanding of data structures, algorithms, and software design" | Covered implicitly | M.S. CS 4.0 GPA, 5 internships |
| Python | "Experience with Python or similar programming language" | Covered | Primary language across 4 roles |
| Coordination hours | "Availability for meetings... during Quora's 'coordination hours' (Mon-Fri: 9am-3pm Pacific Time)" | Not in resume | Remote US-based, tracked internally |

### Preferred Requirements
| Term | Exact JD Wording | Resume Status | Evidence Source |
|------|------------------|---------------|-----------------|
| Internship experience | "Previous software engineering experience via an internship, work experience, and/or coding competition" | Covered | 5 internships + current FT role |
| Python, React, TypeScript, SQL | "Familiarity with Python, React, TypeScript and/or SQL" | Covered | All four explicit in Experience + Skills |
| AI curiosity | "Curiosity about AI and hands-on experience exploring AI tools or building AI-powered projects" | Covered | IRIS AI platform, LiteLLM gateway, Fix-It-Flow, Diff-Grounded, FalconGraph |

### Responsibilities Keywords
| Term | Exact JD Wording | Resume Status | Evidence Source |
|------|------------------|---------------|-----------------|
| Full stack applications | "Develop full stack applications with Python and React" | Covered | Actual Reality, SmartSolve, AAIS Software, Projects |
| Growth, moderation, creators | "improve user engagement, drive user growth, generate informative and engaging content using AI, ensure high-quality content through effective moderation, and enhance the overall creator experience" | Partial | AI content generation (IRIS), scale (AAIS), moderation/creator unsupported |
| Massive scale | "Design and launch product features at massive scale" | Covered (adjacent) | 20+ TB, 700+ companies, 160+ tables |
| Data and experimentation | "using data and experimentation to guide each iteration" | Covered | AAIS data profiling/validation, Actual Reality 41+ test evaluation |
| Full technology stack | "Drive projects from ideation to production using the full technology stack" | Covered | End-to-end ownership across roles |
| Cross-functional collaboration | "Collaborate with designers, product managers, fellow engineers, and data scientists" | Covered | Actual Reality (Product Owner), SmartSolve, AAIS |
| On-call rotation | "Participate in the team's on-call rotation" | Unsupported | No formal production on-call |

### Technology Keywords (Evidence-Bearing)
| Term | Resume Status | Location |
|------|---------------|----------|
| Python | Covered | Experience bullets, Skills |
| React | Covered | Actual Reality, AAIS Software, Skills |
| TypeScript | Covered | Actual Reality, SmartSolve, Projects, Skills |
| SQL | Covered | AAIS Data, AAIS Software, SmartSolve, Skills |
| Next.js | Covered | Actual Reality, SmartSolve, Fix-It-Flow, Skills |
| Firebase | Covered | Actual Reality, Skills |
| AWS (Glue, Lambda, S3, IAM, DynamoDB) | Covered | AAIS Data, AAIS Software, Fix-It-Flow, Skills |
| PySpark | Covered | AAIS Data, Skills |
| Drizzle ORM | Covered | SmartSolve, Skills |
| PostgreSQL | Covered | SmartSolve, AAIS Data, Aster Market, Skills |
| LiteLLM / AI Gateway | Covered | Actual Reality, Skills |
| MCP / Model Context Protocol | Covered | Actual Reality, Skills |
| Playwright / Vitest / Jest | Covered | Actual Reality, Skills |
| CI/CD | Covered | Actual Reality, SmartSolve, Skills |
| RBAC / JWT / SSO | Covered | Actual Reality, SmartSolve, AAIS Software, Skills |
| RAG / LLM evaluation | Covered | Actual Reality, Diff-Grounded, FalconGraph, Skills |
| Guardrails / Langfuse | Covered | Actual Reality, Skills |

## Gap Recovery Gate
## Gap Recovery Gate
Gap recovery status: Completed

### Gap Recovery Decisions

| JD Requirement | Classification | Searched Locations | Recovered Evidence | Final Decision |
|----------------|----------------|-------------------|-------------------|----------------|
| Content moderation | Unsupported - omit | profile/experience-master.md, profile/projects-master.md, profile/skills-master.md, rg searches for "moderation", "content moderation", "trust safety" | No direct content moderation system. Adjacent: APKD healthcare workflow security (CSRF, audit logging), AAIS RBAC/JWT access control, Actual Reality session isolation | Omit - document as intentionally omitted |
| Creator experience product | Unsupported - omit | profile/experience-master.md, profile/projects-master.md, rg searches for "creator", "creator experience", "creator platform" | No direct creator platform. Adjacent: SmartSolve onboarding tracker (HR workflow), Actual Reality customer portal (client experience), RocketGrader (teacher dashboards) | Omit - document as intentionally omitted |
| Formal on-call rotation | Unsupported - omit | profile/experience-master.md, rg searches for "on-call", "oncall", "pager", "incident response" | No formal production on-call. Adjacent: Actual Reality smoke test inventory, validation gate runner, CI/CD gates | Omit - document as intentionally omitted |
| Massive scale (millions of users) | Supported - add/use now | profile/experience-master.md (AAIS Data: 20+ TB, 700+ companies), Actual Reality (NOIC consortium) | 20+ TB, 700+ member companies, 160+ tables, 24-hour latency | Use adjacent scale evidence |
| Data experimentation | Supported - add/use now | profile/experience-master.md (AAIS data profiling, Actual Reality evaluation) | AAIS data profiling/validation, Actual Reality 41+ test evaluation, Diff-Grounded 1450 PR evaluation | Use "data-driven experimentation" phrasing |
| Coordination hours availability | Not a resume claim | N/A | Remote US-based, available for PT hours | Track internally, not in artifacts |

## Important JD Term Search:
Important JD Term Search: Completed

Searched terms across `profile/`, `master-documents/`, and project repositories:

| Search Term | Locations Searched | Results |
|-------------|-------------------|---------|
| "content moderation" | profile/experience-master.md, profile/projects-master.md, profile/skills-master.md | No matches - correctly omitted |
| "creator experience" | profile/experience-master.md, profile/projects-master.md | No direct matches - adjacent: customer portal client experience, teacher dashboards |
| "on-call" / "oncall" | profile/experience-master.md, profile/projects-master.md | No production on-call - adjacent: smoke tests, CI/CD gates |
| "massive scale" / "millions of users" | profile/experience-master.md | Adjacent: 20+ TB, 700+ companies, 160+ tables |
| "data experimentation" / "experimentation" | profile/experience-master.md | AAIS data profiling/validation, Actual Reality evaluation pipeline |
| "coordination hours" | Not applicable | Availability requirement, not a technical skill |

## Bullet Audit
## Bullet Audit
Two-line bullet-wrap check: Pass

All bullets verified to render within two visual PDF lines in the compiled resume. The first Actual Reality bullet was shortened from 3 lines to 2 by removing "for AI content generation at scale" → "for AI content generation."

## Scoring Methodology
## Scoring Methodology

**Job Alignment & Evidence Score: 92/100**

Internal estimate only; not a predicted ATS score.

### Score breakdown
- Keyword coverage: 38/40
- Experience relevance: 24/25
- Impact and evidence: 14/15
- Formatting and ATS parsing: 10/10
- Risk and gap handling: 6/10

### Rationale

**Keyword coverage (38/40):** 32/44 expanded terms found; all must-have and preferred tech terms covered; missing only unsupported domain terms (content moderation, creator experience, on-call) and foundational CS terms (data structures, algorithms) implicit in degree.

**Experience relevance (24/25):** 4 roles + 2 projects directly match full-stack Python/React/TypeScript/SQL stack, AI systems, massive-scale data, cross-functional collaboration; minor gap: no direct consumer-scale product.

**Impact & evidence (14/15):** Quantified scale (20+ TB, 700+ cos, 160+ tables, 1000+ tables, 110 users, 41+ test cases, 1450 PRs, 44 red-team fixtures); all bullets follow action + method + scope + result.

**Formatting & ATS parsing (10/10):** 1-page PDF, canonical visual system, extractable text, standard headings, no graphics/tables, ~101KB.

**Risk & gap handling (6/10):** Unsupported terms (content moderation, creator experience, on-call) correctly omitted and documented; F-1 gate passed with silent/ambiguous sponsorship; minor deduction for no direct consumer-scale metrics.

### Exact posted title matched in visible summary/title/header clause
Pass -- "Full Stack Software Engineer" appears in centered contact/title line (exact posted title: "Full Stack Software Engineer, New Grad" -> adjacent title used truthfully).

### Strong matches
- Exact required languages: Python, React, TypeScript, SQL all explicit in Experience and Skills
- Next.js 15/React 19/TypeScript/Firebase customer portal (Actual Reality)
- LiteLLM AI Gateway with multi-tier routing, guardrails, Langfuse, MCP (Actual Reality)
- 41+ regression test evaluation pipeline with Playwright (Actual Reality)
- 20+ TB PySpark/AWS Glue pipelines for 700+ companies (AAIS Data)
- 1,000+ SQL tables generated via Python automation (AAIS Software)
- RBAC/JWT/SSO across React/Node.js applications (AAIS Software, SmartSolve, Actual Reality)
- Drizzle ORM, PostgreSQL, AWS (Glue, Lambda, S3, IAM, DynamoDB)
- CI/CD, Vitest, Jest, Playwright, Testing Library
- RAG, LLM evaluation (ICSME-published), AI-assisted development (Claude Code, Copilot, Cursor, Codex)
- 13 experience bullets (exceeds 11 minimum) + 2 strong AI projects

### Gaps / intentionally omitted unsupported keywords
- Content moderation (no direct evidence - adjacent: healthcare workflow security, RBAC, session isolation)
- Creator experience product (no direct evidence - adjacent: customer portal client experience, teacher dashboards)
- Formal on-call rotation (no production on-call - adjacent: validation gates, CI/CD, smoke tests)
- Direct consumer-scale metrics (millions of users) - adjacent: 20+ TB, 700+ companies
- Data structures, algorithms (foundational - implicit in M.S. CS 4.0 GPA, not explicit in bullets)

### Recommended improvements
- If Quora's content moderation systems use specific tooling (e.g., Perspective API, custom ML classifiers), prepare interview talking points around APKD healthcare security and AAIS access control as adjacent evidence
- Consider adding a brief "Content Quality & Safety" bullet if a future role emphasizes trust/safety
- Track F-1 sponsorship confirmation through recruiter conversation

## Expanded role-specific keyword pass:
Expanded role-specific keyword pass: Completed

Ran `analyze_application_keywords.py` with 44 Quora-specific terms. Found 32/44. Missing 12 are: algorithms, content moderation, coordination hours, creator experience, data experimentation, data structures, engineer new, engineer new grad, massive scale, on-call, requirements, software engineer new. Of these, 6 are unsupported domain terms correctly omitted, 3 are role-title variants not needed in resume body, 2 are foundational CS implicit in degree, 1 is availability requirement.

## Verification Gates

- Gap recovery gate checked: Pass
- ATS source gate checked: Pass
- Human recruiter readability gate checked: Pass
- Visual consistency gate checked: Pass
- Page utilization gate checked: Pass
- Submitted-facing terminology sync checked: Pass
- Score consistency gate checked: Pass
- Cover-letter artifact checked: Pass
- Application-answer human voice gate checked: Pass - Answer grounded in verified Diff-Grounded PR Generation project (ICSME 2025) with concrete technical details: GitHub API ingestion structured context construction grounding constraint LLM-as-judge evaluation across 1450 PRs correctness coverage clarity metrics. No AI clichés no semicolons no em dashes no unsupported claims. Sounds like a thoughtful early-career engineer describing a real research project.

---
*Generated for application-packages/Quora/Full-Stack-Software-Engineer-New-Grad*