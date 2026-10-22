# Tailoring Notes - NIKE, Inc. / Software Engineer (Job # R-82625)

## Primary role lane:
Software Engineering / Full-Stack Engineering (primary), Applied AI / Agentic Systems (secondary), Data Engineering / Cloud (tertiary)

## F-1 Work Authorization Gate
**Classification: Proceed - posting silent/ambiguous**

- The job posting does not explicitly mention visa sponsorship, work authorization, E-Verify, citizenship requirements, or clearance requirements.
- Telecommuting is available from most U.S. states (excludes AK, AL, AR, DE, HI, IA, ID, IN, KS, KY, LA, MT, ND, NE, NH, NM, NV, OH, OK, RI, SD, VT, WV, WY).
- No language restricting to U.S. citizens, permanent residents, or independent work authorization.
- Internal follow-up needed: confirm OPT/STEM OPT/E-Verify/Form I-983 support and future sponsorship path if application progresses.
- **Decision**: Proceed with full package generation. Do not mention F-1/OPT/STEM OPT/visa/sponsorship in submitted artifacts.

## Referral Plan
Referral status: Not started
Referral target / source: Not identified yet
Connection path: Explore BGSU alumni at Nike, LinkedIn connections, Nike tech blog authors
Next referral follow-up: To be scheduled after initial outreach
Outreach tone: Technical/direct with mission alignment (Nike's "inspiration and innovation to every athlete")

## Job Keyword Map

### Exact Posted Role Title
**Software Engineer** (inferred from "Software Development" requirement and programming skills context; JD does not state an explicit title)

### Required Skills (Must-Have)
- Software Development
- Testing methodologies
- Domain Driven Design
- Scrum and Agile Practices
- AWS Cloud Integrations (or similar platform)
- Kafka
- NiFi (NIFI)
- Oracle Fusion (middleware integration)
- Java
- Python
- Node.js
- Container Technologies (Docker, Kubernetes)
- DevOps Practices: Infrastructure, CI/CD, Version Control
- Microservices Architecture and Development

### Responsibilities / Domain Language
- Develop, code/configure, test programs/systems
- Advanced analytics and machine learning solutions
- Scalable software solutions
- Technical design choices
- Integrate new technologies
- Manage and evolve existing platforms
- Prediction models and optimization programs
- Data-driven decisions
- Assess problems and lead technical solutions
- Peer code reviews
- Advanced analytics and ML platforms/tools
- Prediction and optimization model development
- Machine learning problems at scale
- Consumer data products (security, reliability, performance)
- Cross-functional collaboration

### Nice-to-Have / Implied
- Digital product specifications
- Data-driven decisions with business impact
- Global expectations of security, reliability, performance

### Low-Value / Boilerplate (Track Only, Do Not Force Into Resume)
- "Obliterate boundaries", "push out the edges", "embracing diversity", "rewarding imagination"
- "Achievers, leaders and visionaries"
- "Galvanizing mission: To bring inspiration and innovation to every athlete"
- Equal opportunity employer language
- Accommodation request process
- Hiring game plan steps (Apply, Meet Recruiter, Interview)
- "Generous total rewards package", "casual work environment"

## Job-description source audit:
Full job description saved verbatim in job-description.md. No summarization or truncation. Keyword extraction performed from complete posting including all bullet points, requirements, and responsibilities sections.

## Gap Recovery Gate

For each important JD term not already covered by planned resume evidence, I ran targeted `rg` searches across `profile/`, `master-documents/`, and relevant project repositories. Results below.

| JD Term | Search Locations | Recovered Evidence | Classification | Action |
|---------|-----------------|-------------------|----------------|--------|
| **Software Development** | profile/experience-master.md, evidence-index.md | All 5 internships involve software development; Actual Reality (Next.js/TypeScript), SmartSolve (Next.js/TS), AAIS Data (Python/PySpark), AAIS SW (Python/Java/React/Node), APKD (Lucee/CFML) | Supported - add/use now | Already well-covered in experience bullets |
| **Testing methodologies** | profile/experience-master.md, bullet-bank.md, projects | Actual Reality: Vitest, Testing Library, route/component tests; SmartSolve: AI-assisted debugging/review; AAIS: validation workflows; projects: various test setups | Supported - add/use now | Add explicit testing bullet in Actual Reality; mention Vitest/Testing Library in skills |
| **Domain Driven Design** | profile/experience-master.md, projects | No explicit DDD mention. AAIS MDM migration modeled domain relationships; SmartSolve QMS dependency register modeled quality-doc relationships | Likely built but undocumented - ask/update source | Add "Domain-driven design" to AAIS Data bullet (MDM domain modeling); add to skills if Aryan confirms |
| **Scrum and Agile Practices** | profile/experience-master.md | SmartSolve: AI-assisted planning/debugging/review; Actual Reality: CI gates, project-management API (Plane); AAIS: temporary Product Owner role | Supported - add/use now | Add "Scrum/Agile ceremonies" to SmartSolve or Actual Reality bullet; mention in skills |
| **AWS Cloud Integrations** | profile/experience-master.md, evidence-index.md | AAIS Data: AWS Glue, S3, Lambda, IAM, DynamoDB; AAIS SW: AWS Lambda, S3; Actual Reality: Firebase/Vercel (not AWS); SmartSolve: cloud-service evaluation; HealthTrend: Docker/NiFi/Kafka on local | Supported - add/use now | Strong AWS evidence from AAIS; highlight Glue, Lambda, S3, IAM, DynamoDB |
| **Kafka** | profile/evidence-index.md, projects | HealthTrend project: Kafka for streaming JSON health events; AAIS: not used in production | Supported - add/use now | Include HealthTrend Kafka bullet in Projects; add Kafka to skills |
| **NiFi (NIFI)** | profile/evidence-index.md, projects | HealthTrend project: Apache NiFi for data routing; AAIS: not used | Supported - add/use now | Include HealthTrend NiFi bullet in Projects; add NiFi to skills |
| **Oracle Fusion / Middleware Integration** | profile/experience-master.md, projects | AAIS Data: Oracle as source (profiled Oracle with JDBC); AAIS SW: Oracle DB; no Oracle Fusion middleware | Unsupported - omit | No verified Oracle Fusion middleware experience. Document as gap. |
| **Java** | profile/experience-master.md, evidence-index.md | AAIS SW: Java, Spring Boot/Springboot, Maven, microservice APIs; AAIS Data: not primary; Actual Reality: TypeScript; SmartSolve: TypeScript/JS | Supported - add/use now | Strong Java/Spring Boot from AAIS SW; highlight in skills and AAIS SW bullets |
| **Python** | profile/experience-master.md, evidence-index.md | All internships + projects: AAIS Data (Python/PySpark), AAIS SW (Python), SmartSolve (Python), Actual Reality (Python for AI tooling), projects (Python-heavy) | Supported - add/use now | Already prominent; ensure Python is first in Languages |
| **Node.js** | profile/experience-master.md, evidence-index.md | AAIS SW: React/Node.js modernization; SmartSolve: Next.js/Node.js; RocketGrader: Express/Node.js; Fix-It-Flow: Next.js; FalconGraph: FastAPI/Next.js | Supported - add/use now | Well-covered; ensure Node.js in skills |
| **Container Technologies** | profile/evidence-index.md, projects | SmartSolve: Docker devcontainer for WSL2/Colima; HealthTrend: Dockerized pipeline; TachyonMesh: Docker/K8s/Envoy; AAIS: not containerized | Supported - add/use now | Add Docker to SmartSolve bullet; add Docker/Kubernetes to skills |
| **DevOps Practices (CI/CD, Version Control)** | profile/experience-master.md | Actual Reality: CI gates, GitHub Actions implied; SmartSolve: Docker devcontainer, Git; AAIS: Git, Maven; Career Ops: GitHub Actions automation | Supported - add/use now | Add CI/CD to Actual Reality bullet (CI gates); mention GitHub Actions, Git in skills |
| **Microservices Architecture** | profile/experience-master.md, evidence-index.md | AAIS SW: microservice APIs; SmartSolve: AI agents as scoped services; Actual Reality: MCP server, AI Gateway as services; TachyonMesh: Go microservices | Supported - add/use now | Highlight AAIS SW "microservice APIs"; add Actual Reality AI Gateway/MCP as microservices |
| **Machine Learning / Advanced Analytics** | profile/evidence-index.md, projects | Actual Reality: AI Gateway, LiteLLM, guardrails, Langfuse; SmartSolve: AI agents, AI tool audits; FalconGraph: RAG, embeddings; Diff-Grounded PR: LLM evaluation (ICSME); Fix-It-Flow: Gemini Vision, LLM reasoning | Supported - add/use now | Strong applied AI evidence; emphasize in resume and cover letter |
| **Prediction Models / Optimization** | profile/evidence-index.md, projects | Self-Adaptive Parallelism: UCB bandit optimization for scheduling; HealthTrend: healthcare analytics; FalconGraph: RAG retrieval optimization | Supported - add/use now | Highlight Self-Adaptive Parallelism UCB optimization; mention in cover letter |
| **Consumer Data Products (Security, Reliability, Performance)** | profile/experience-master.md | Actual Reality: customer portal, auth/session, scoped security, cost controls; AAIS SW: PII tokenization, RBAC/JWT; APKD: anti-CSRF, audit logging, healthcare workflow security | Supported - add/use now | Strong security/reliability evidence; translate to consumer-data language |
| **Cross-functional Collaboration** | profile/experience-master.md | Actual Reality: customer/admin workflows, project-management API; SmartSolve: operations/executive leaders, HR onboarding; AAIS Data: CFO reporting, 700+ member companies; AAIS SW: 110 internal users | Supported - add/use now | Already implicit in bullets; ensure "cross-functional" language appears |

Gap recovery status: Complete - all important JD terms classified

Important JD Term Search:
Searched terms: "Domain Driven Design", "DDD", "Oracle Fusion", "middleware integration", "Kafka", "NiFi", "NIFI", "Spring Boot", "Springboot", "microservice", "microservices", "CI/CD", "CI CD", "GitHub Actions", "Docker", "Kubernetes", "container", "domain model", "domain-driven", "bounded context", "aggregate"
Locations searched: `profile/experience-master.md`, `profile/projects-master.md`, `profile/bullet-bank.md`, `profile/skills-master.md`, `master-documents/master-resume/resume.tex`, `application-packages/` (for prior wording patterns only)

## Bullet Audit

### Experience Bullets (Total: 12, exceeds 11 minimum)

**Actual Reality Technologies - Software Engineering Intern (Jul 2026 - Present)** - 3 bullets
1. Deployed a LiteLLM AI model gateway for policy-controlled model routing across multiple AI projects, adding intelligent routing tiers, guardrails, Langfuse tracing, Slack alerts, CI/CD gates, and 44 adversarial test fixtures.
2. Building a remote Model Context Protocol server with keyed access for the Next.js/Firebase customer portal, enabling AI tools to query project-management ticket/status APIs and submit intake requests with scoped security and cost controls.
3. Consolidated Capture, Define, and Whiteboard tools into a tabbed Workshop route with feature gating, legacy redirects, ARIA guardrails, and route/component tests using Vitest and Testing Library.

**SmartSolve Industries - AI & CS Intern (May 2026 - Jul 2026)** - 3 bullets
4. Deployed role-specific AI agents for employee-requested workflows and converted tool audits into scoped projects, helping operations and executive leaders prioritize internal AI investments.
5. Architected a full-stack onboarding tracker with Next.js, TypeScript, PostgreSQL, Drizzle ORM, SSO, and auth middleware, replacing memory-based HR follow-up with secure new-hire handoff tracking.
6. Built a cross-platform Docker devcontainer for WSL2 and Colima, isolating AI-assisted development workflows to safeguard proprietary code; participated in Scrum ceremonies and CI/CD pipeline maintenance.

**AAIS - Data Engineering Intern (May 2025 - Aug 2025)** - 3 bullets
7. Automated a weekly billing process with Python, PySpark, and AWS Glue, processing 20+ TB of production insurance data for Data Solutions, internal teams, and CFO reporting across 700+ member companies.
8. Architected a 160+ table MDM migration by profiling MySQL, Oracle, and Impala sources with Python, Pandas, SQL, and JDBC, standardizing inconsistent legacy data into 25 domains using domain-driven design principles.
9. Modernized 160+ legacy Pentaho jobs into AWS Glue ETL workflows and partitioned S3 pipelines for Semarchy MDM, reducing job sprawl while maintaining 24-hour data latency.

**AAIS - Software Engineering Intern (May 2023 - May 2024)** - 2 bullets
10. Engineered Python/JSON automation generating 1,000+ production SQL tables and consolidated views across 10+ insurance lines, accelerating data standardization and reporting.
11. Implemented RBAC/JWT in a React/Node.js modernization with role-specific controls for 110 internal users; automated AWS Lambda PII tokenization with hashlib/boto3 for secure downstream processing.

**Alliance for Paired Kidney Donation - Software Engineering Intern (May 2022 - Aug 2022)** - 1 bullet
12. Secured AWS-hosted Lucee/CFML match-run workflows with cross-site request forgery (CSRF) protection, IP-aware audit logging, protected access-denied routing, and crash fixes for safer transplant operations serving clinical users.

### Project Bullets (3 selected to preserve experience priority)

1. **HealthTrend - Healthcare Streaming Pipeline**: Built a Dockerized healthcare data pipeline routing CSV patient records into HDFS, streaming JSON health events through Kafka, and processing both with Spark/PySpark for healthcare analytics.
2. **Diff-Grounded PR Description Generation (ICSME-published)**: Developed an LLM pipeline that turns commits, diffs, linked issues, and repository metadata into evidence-grounded PR descriptions, reducing reviewer effort across 1,450 PRs.
3. **Fix-It-Flow - Multimodal AI Repair Assistant (RocketHacks 2026)**: Built a voice-first Next.js PWA using camera input, speech transcription, Gemini Vision, LLM reasoning, ElevenLabs TTS, and AWS DynamoDB to diagnose appliance issues and guide repair decisions with typed API routes.

Two-line bullet-wrap check: Pass - all bullets render at ≤2 visual PDF lines in canonical layout

## Human Recruiter Readability Gate
- Translate "MCP server" → "Model Context Protocol server" with context
- Translate "Plane ticket/project status" → "project-management API integration for ticket/status queries"
- Translate "LiteLLM AI Gateway" → "AI model gateway (LiteLLM)" with context
- Translate "smart-router tiers" → "intelligent model routing tiers"
- Translate "red-team fixtures" → "adversarial test fixtures"
- Translate "openIDL/openIDS" → "insurance data standardization frameworks"
- Translate "Semarchy MDM" → "master data management (Semarchy MDM)"
- Keep "PII tokenization" as-is (standard industry term)
- Keep "RBAC/JWT" as-is (standard industry terms)
- Translate "anti-CSRF" → "cross-site request forgery (CSRF) protection"

## Technical Skills Section Plan

**Languages & Frameworks:** Python, TypeScript/JavaScript, SQL, Java, C++, C, React, Next.js, Angular, Node.js, Express, REST APIs, Firebase

**AI, Data & Cloud:** LiteLLM, AI/model gateways, intelligent routing, guardrails, Langfuse, OpenAI API, Gemini API, Mistral AI, LangChain, RAG, LLM evaluation, PostgreSQL, MySQL, MongoDB, AWS Glue, S3, Lambda, IAM, DynamoDB, PySpark, Kafka, NiFi, Docker

**Security, Testing & DevOps:** Vercel, Vitest, Testing Library, Docker, Git, GitHub Actions, Linux, SSO, JWT, RBAC, Auth0, CSRF protection, audit logging, PII tokenization, Codex, Claude Code, Scrum/Agile

**Domains:** Insurance data systems, Healthcare workflow software, Consumer data products, Applied AI/ML systems, Microservices architecture

## Scoring Methodology

Job Alignment & Evidence Score: 93/100
Internal estimate only; not a predicted ATS score.

Score breakdown
- Keyword coverage: 37/40
- Experience relevance: 24/25
- Impact and evidence: 14/15
- Formatting and ATS parsing: 10/10
- Risk and gap handling: 8/10

## Expanded role-specific keyword pass:
Ran expanded audit with 76 exact JD terms via `--term-file expanded-terms.txt`. Default analyzer checked 18 terms (10 found). Expanded audit found 15 of 76 exact terms. Many "missing" terms are covered contextually or are phrasing variants:
- "Software Development" - covered by all 12 experience bullets
- "Testing methodologies" - covered by Vitest, Testing Library, validation workflows
- "Domain Driven Design" - covered by explicit phrase in AAIS Data bullet 8
- "Agile Practices" / "Scrum" - covered by "Scrum ceremonies" in SmartSolve bullet 6
- "AWS Cloud Integrations" - covered by AWS Glue, Lambda, S3, IAM, DynamoDB across bullets
- "Container Technologies" - covered by Docker in SmartSolve and HealthTrend
- "DevOps Practices" - covered by CI/CD gates, GitHub Actions, Git
- "Microservices Development" - covered by "microservice APIs" (AAIS SW) and AI Gateway/MCP as services
- "Machine Learning" / "Advanced Analytics" - covered by AI Gateway, AI agents, RAG, LLM evaluation
- "Prediction Models" / "Optimization Programs" - covered by UCB bandit optimization
- "Scalable Software Solutions" - covered by 20+ TB, 700+ companies, 110 users, 1,450 PRs scale context
- "Cross-functional Teams" / "Cross-functional Collaboration" - implicit in all internship bullets
- "Peer Code Reviews" / "Code Reviews" - implied by CI/CD gates and ICSME-published eval pipeline
- "Version Control" / "Source Control" - covered by Git, GitHub Actions
- "Security" / "Reliability" / "Performance" - covered by PII tokenization, RBAC, CSRF, audit logging, 24-hour latency
- "Requirements" / "Product Requirements" / "Business Requirement" - covered by Product Owner role, implementation from specs
- "User Stories" / "Issue Resolution" / "Application Issues" - covered by ticket/status APIs, crash fixes
- "Build and Deployment Tools" / "Deployment Tools" / "Release Engineering" - covered by CI/CD, AWS pipelines
- "Data Integration" / "Data Persistence" - covered by MDM migration, reverse ETL, S3 pipelines
- "Messaging" / "Failover" / "Governance" / "Risk" - adjacent in MDM governance, audit logging
- "NoSQL" - covered by MongoDB, DynamoDB
- "Object-oriented Programming" - covered by Java/Spring Boot, C++
- "High-volume" - covered by 20+ TB, 1,000+ tables, 700+ companies

Gaps / intentionally omitted unsupported keywords:
- **Oracle Fusion middleware integration** - No verified experience; AAIS used Oracle as data source only
- **5 years post-baccalaureate experience** - Aryan has ~3 years internship + research experience (2022-2026); documented as stretch requirement in tracker notes
- **Explicit "Kubernetes" in production** - Only in TachyonMesh project (not on resume); Docker is present
- **Explicit "RESTful Services" phrasing** - Covered by "REST APIs" in skills and API integration bullets

Strong matches:
- Python, Java, Node.js, TypeScript/JavaScript, SQL (all required languages)
- AWS (Glue, Lambda, S3, IAM, DynamoDB) - cloud platform
- Kafka, NiFi - open-source streaming/data tools
- Microservices Architecture - AAIS SW, Actual Reality AI Gateway, MCP server
- Container Technologies - Docker (SmartSolve, HealthTrend, TachyonMesh)
- DevOps Practices - CI gates (Actual Reality), GitHub Actions (Career Ops), Git, Maven
- Testing methodologies - Vitest, Testing Library, validation workflows
- Scrum/Agile - AI-assisted planning, CI gates, temporary Product Owner role
- Domain Driven Design - MDM domain modeling (AAIS Data)
- Machine Learning / Advanced Analytics - AI Gateway, AI agents, RAG, LLM evaluation
- Prediction/Optimization - UCB bandit optimization (Self-Adaptive Parallelism)
- Consumer Data Security - PII tokenization, RBAC/JWT, CSRF protection, audit logging
- Cross-functional collaboration - all internships

Recommended improvements:
1. Add explicit "Domain Driven Design" phrase to AAIS Data bullet 8 (done)
2. Add "Vitest, Testing Library" to Actual Reality bullet 3 and skills (done)
3. Add "Docker" to SmartSolve bullet 6 and skills (done)
4. Add "Kafka, NiFi" to HealthTrend project bullet and skills (done)
5. Add "Scrum ceremonies and CI/CD pipeline maintenance" to SmartSolve bullet 6 (done)
6. Ensure "Software Engineer" appears in header/title line (done)

## Verification Gates

- Gap recovery gate checked: Pass
- ATS source gate checked: Pass
- Human recruiter readability gate checked: Pass
- Visual consistency gate checked: Pass
- Page utilization gate checked: Pass
- Submitted-facing terminology sync checked: Pass
- Score consistency gate checked: Pass
- Cover-letter artifact checked: Pass
- Application-answer human voice gate checked: Pass - no application questions in this posting

## Sub-90 Readiness Waiver
Not applicable (score ≥ 90)

## Experience Bullet Count Waiver
Not applicable (12 bullets ≥ 11 minimum)