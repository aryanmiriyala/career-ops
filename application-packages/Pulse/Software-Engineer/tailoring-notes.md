# Tailoring Notes - Pulse / Software Engineer

## Primary role lane:
Full-stack Software Engineering with Applied AI/Document Intelligence secondary

## F-1 Work Authorization Gate
**Classification: Proceed - confirmed compatible**
- Posting explicitly states: "Sponsorship available."
- No F-1/OPT/STEM OPT blocker language present.
- Role is on-site in San Francisco; relocation assistance offered.
- No E-Verify, Form I-983, or future sponsorship restrictions mentioned.
- Internal tracking: proceed with truthful materials.

## Referral Plan
- Referral status: Not started
- Referral target / source: Not identified yet
- Connection path: To be determined
- Next referral follow-up: To be determined
- Notes: Target Pulse employees on LinkedIn (SF-based, document intelligence, AI/ML). Prioritize alumni from BGSU or University of Toledo if any. No warm connection identified yet.

## Job Keyword Map

### Exact Posted Title
- Software Engineer

### Required Skills (from JD)
- Python or TypeScript + SQL
- 2+ years building production software (new grads considered)
- Clear communication and bias to ship

### Nice-to-Have Skills (from JD)
- FastAPI
- Postgres / PostgreSQL
- Redis
- React
- AWS

### Responsibilities (from JD)
- Build backend services in Python and secure APIs
- Ship front end features in React and TypeScript for console and tools
- Improve accuracy, latency, and reliability across the extraction pipeline
- Write tests, own deployments, and monitor production health
- Collaborate with design, ML, and customer-facing teams

### Domain-Specific Terms (Pulse Core Tech)
- Document understanding / extraction
- Layout understanding with specialized component detection models
- Low-latency OCR models for targeted extraction
- Advanced reading-order algorithms for complex structures
- Proprietary table structure recognition and parsing
- Fine-tuned vision-language models for charts, tables, and figures
- Multi-stage architecture
- Computer vision, NLP, data infrastructure intersection

### Company Context Keywords
- Small, fast-growing team
- San Francisco, 5 days in-office
- Fortune 100 enterprises, YC startups, public investment firms, growth-stage companies
- Tier 1 investors
- Relocation assistance for Bay Area moves

### Low-Value / Boilerplate Terms (tracked but not forced)
- Competitive base salary plus equity
- Performance-based bonus
- Daily meal stipend
- Medical, vision, and dental coverage

## Job-description source audit:
- Full employer posting saved verbatim in job-description.md
- No summarization or truncation performed
- Source: User-provided job description text

## Gap Recovery Gate
**Gap recovery status: Pass**

### Important JD Term Search:
Searched terms, searched locations, recovered evidence, and final decisions:

| JD Term | Searched Locations | Evidence Found | Decision |
|---------|-------------------|----------------|----------|
| Python | profile/evidence-index.md, experience-master.md, projects-master.md | Actual Reality (Node.js but Python in AAIS, FalconGraph), AAIS (PySpark, AWS Glue), SmartSolve (Python), multiple projects | Supported - add/use now |
| TypeScript | profile/evidence-index.md, experience-master.md, projects-master.md | Actual Reality (Next.js 15), SmartSolve (Next.js), Aster Market, Fix-It-Flow, FalconGraph | Supported - add/use now |
| SQL | profile/evidence-index.md, experience-master.md | AAIS (MySQL, Oracle, PostgreSQL, Impala), SmartSolve (PostgreSQL), Aster Market (PostgreSQL/Neon) | Supported - add/use now |
| FastAPI | profile/evidence-index.md, projects-master.md | FalconGraph Search (FastAPI backend) | Supported - add/use now |
| PostgreSQL | profile/evidence-index.md, experience-master.md | AAIS, SmartSolve, Aster Market | Supported - add/use now |
| Redis | profile/evidence-index.md, experience-master.md | Actual Reality Technologies (MongoDB, Redis) | Supported - add/use now |
| React | profile/evidence-index.md, experience-master.md | Actual Reality, SmartSolve, multiple projects | Supported - add/use now |
| AWS | profile/evidence-index.md, experience-master.md | AAIS (Glue, S3, Lambda, IAM, DynamoDB), Fix-It-Flow (DynamoDB), HealthTrend | Supported - add/use now |
| Backend services / Secure APIs | profile/evidence-index.md, experience-master.md | Actual Reality (LiteLLM AI Gateway), AAIS (microservice APIs), FalconGraph (FastAPI) | Supported - add/use now |
| Front end features / React / TypeScript | profile/evidence-index.md, experience-master.md | Actual Reality (Next.js 15/React 19 customer portal), SmartSolve (Next.js) | Supported - add/use now |
| Extraction pipeline / accuracy / latency / reliability | profile/evidence-index.md, experience-master.md | Actual Reality (IRIS evaluation pipeline, 41+ test suites, latency tracking via Langfuse) | Supported - add/use now (adjacent: evaluation pipeline, not document extraction) |
| Tests / Deployments / Production monitoring | profile/evidence-index.md, experience-master.md | Actual Reality (Playwright, Vitest, Jest, CI/CD gates, Langfuse tracing, Slack alerts, 44 red-team fixtures) | Supported - add/use now |
| Document understanding / Document extraction / OCR / Layout understanding / Component detection / Reading-order algorithms / Table structure recognition / Table parsing / Vision-language models / VLM / Charts / Figures | profile/evidence-index.md, projects-master.md, master-documents/ | FalconGraph (PDF/DOCX/HTML crawling, document processing, RAG), Fix-It-Flow (Gemini Vision for camera input), Travel Health Advisor (health data) | Partially supported - adjacent evidence only. No direct OCR, VLM fine-tuning, table parsing, or layout understanding experience. Classified as Unsupported - omit for core claims, adjacent evidence noted in cover letter. |
| Computer vision / NLP | profile/evidence-index.md, projects-master.md | Fix-It-Flow (Gemini Vision), FalconGraph (document processing, embeddings), Diff-Grounded PR Generation (NLP/LLM) | Partially supported - adjacent evidence |
| Data infrastructure | profile/evidence-index.md, experience-master.md | AAIS (20+ TB, 700+ companies, MDM, ETL), HealthTrend (Kafka, NiFi, Spark) | Supported - add/use now |
| Multi-stage architecture | profile/evidence-index.md | Actual Reality (IRIS: LiteLLM gateway -> evaluation gate -> production) | Supported - add/use now (adjacent: AI pipeline architecture) |
| Startup experience | profile/evidence-index.md | Actual Reality Technologies (small team, early-stage), SmartSolve | Supported - add/use now |
| On-site / San Francisco / 5 days in-office | N/A | Location requirement only - no skill claim needed | Location constraint tracked in F-1 gate |

## Bullet Audit

### Experience Bullets (11 total - meets 11-bullet floor)

**Actual Reality Technologies (3 bullets)**
1. Integrated an internal LiteLLM AI gateway into IRIS (LibreChat fork with Node.js, React, MongoDB, Redis), enforcing multi-tier model routing, guardrails, and Langfuse tracing across production AI traffic.
   - Action verb: Integrated
   - What: AI gateway into IRIS platform
   - Method/Technology: LiteLLM, Node.js, React, MongoDB, Redis, multi-tier routing, guardrails, Langfuse
   - Scope: Production AI traffic
   - Impact: Enforced routing/tracing
   - Two-line check: Pass

2. Built an automated evaluation pipeline with Node.js and Playwright to validate multi-turn IRIS reasoning, tool execution, and citation accuracy across 41+ regression test suites.
   - Action verb: Built
   - What: Automated evaluation pipeline
   - Method/Technology: Node.js, Playwright
   - Scope: 41+ regression test suites
   - Impact: Validated reasoning, tool execution, citation accuracy
   - Two-line check: Pass

3. Architected a production customer portal using Next.js 15, React 19, and Firebase, implementing multi-tenant session isolation, automated Plane API ticket reconciliation, and real-time client retainer tracking.
   - Action verb: Architected
   - What: Production customer portal
   - Method/Technology: Next.js 15, React 19, Firebase
   - Scope: Multi-tenant, automated ticket reconciliation, retainer tracking
   - Impact: Production delivery
   - Two-line check: Pass

**SmartSolve Industries (3 bullets)**
4. Architected a full-stack onboarding system with Next.js, TypeScript, PostgreSQL, and Drizzle ORM, implementing SSO authentication and RBAC middleware to streamline cross-department handoffs.
   - Action verb: Architected
   - What: Full-stack onboarding system
   - Method/Technology: Next.js, TypeScript, PostgreSQL, Drizzle ORM, SSO, RBAC
   - Scope: Cross-department handoffs
   - Impact: Streamlined
   - Two-line check: Pass

5. Engineered domain-specific AI automation agents for enterprise workflows, benchmarking tooling viability and delivering production implementation roadmaps.
   - Action verb: Engineered
   - What: AI automation agents
   - Method/Technology: Benchmarking, tooling evaluation
   - Scope: Enterprise workflows
   - Impact: Production roadmaps adopted by leadership
   - Two-line check: Pass

6. Built containerized developer environments with Docker for WSL2 and macOS, standardizing local AI toolchains and isolating proprietary code during AI-assisted development.
   - Action verb: Built
   - What: Containerized developer environments
   - Method/Technology: Docker, WSL2, macOS
   - Scope: Team workstations
   - Impact: Standardized AI toolchains, isolated proprietary code
   - Two-line check: Pass

**AAIS Data Engineering Intern (2 bullets)**
7. Engineered automated ETL pipelines using Python, PySpark, and AWS Glue, processing 20+ TB of production insurance data across 700+ member companies for executive billing reporting.
   - Action verb: Engineered
   - What: Automated ETL pipelines
   - Method/Technology: Python, PySpark, AWS Glue
   - Scope: 20+ TB, 700+ companies
   - Impact: Executive billing reporting
   - Two-line check: Pass

8. Led data profiling and schema migration across 160+ tables in MySQL, Oracle, and Impala using Python and SQL, standardizing legacy records into 25 unified master-data domains.
   - Action verb: Led
   - What: Data profiling and schema migration
   - Method/Technology: Python, SQL, MySQL, Oracle, Impala
   - Scope: 160+ tables, 25 domains
   - Impact: Standardized legacy records
   - Two-line check: Pass

**AAIS Software Engineering Intern (2 bullets)**
9. Automated schema generation with Python to produce 1,000+ production SQL tables and analytical views across 10+ insurance lines, accelerating industry openIDL data standardization.
   - Action verb: Automated
   - What: Schema generation
   - Method/Technology: Python
   - Scope: 1,000+ tables, 10+ insurance lines
   - Impact: Accelerated openIDL standardization
   - Two-line check: Pass

10. Implemented RBAC and JWT authentication in a React/Node.js web application, securing sensitive data access across 110 enterprise users.
    - Action verb: Implemented
    - What: RBAC and JWT authentication
    - Method/Technology: React, Node.js
    - Scope: 110 enterprise users
    - Impact: Secured sensitive data access
    - Two-line check: Pass

**APKD Software Engineering Intern (1 bullet)**
11. Hardened AWS-hosted clinical match-run systems by implementing CSRF protection, IP-based audit logging, and input validation, eliminating runtime exceptions for organ transplant coordination.
    - Action verb: Hardened
    - What: AWS-hosted clinical match-run systems
    - Method/Technology: CSRF protection, IP-based audit logging, input validation
    - Scope: Organ transplant coordination
    - Impact: Eliminated runtime exceptions
    - Two-line check: Pass

### Project Bullets (6 bullets)

**FalconGraph Search (2 bullets)**
- Built a source-grounded RAG search engine that crawled campus resources, processed PDF/DOCX/HTML documents, generated embeddings, retrieved with FAISS, and served cited answers via FastAPI and a Next.js interface.
- Implemented multithreaded C++/OpenMP web crawling, checkpointed document cleaning pipelines, and semantic ranking for source-grounded answer generation.

**Fix-It-Flow (2 bullets)**
- Built a voice-first Next.js PWA using camera input, Web Speech API, Gemini Vision, and ElevenLabs TTS to diagnose appliance issues and guide hands-free repair workflows backed by AWS DynamoDB.
- Designed typed API routes for inspection sessions, device identification, and repair-step generation with structured findings, confidence scores, and safety warnings.

**Diff-Grounded PR Generation (2 bullets)**
- Engineered an ICSME-published LLM pipeline synthesizing code diffs and repository metadata into evidence-grounded PR descriptions across 1,450 pull requests.
- Built automated LLM evaluation workflows comparing generated descriptions against raw code-change evidence for correctness, coverage, and clarity.

### Two-line bullet-wrap check: Pass
All bullets render at 2 visual lines or fewer in the compiled PDF.

## Scoring Methodology

### Job Alignment & Evidence Score: 83/100
Internal estimate only; not a predicted ATS score.

### Score breakdown
- Keyword coverage: 28/40
- Experience relevance: 22/25
- Impact and evidence: 14/15
- Formatting and ATS parsing: 10/10
- Risk and gap handling: 9/10

### Exact posted title matched in visible summary/title/header clause
Software Engineer -- appears in centered contact/title line as "Software Engineer"

### Strong matches
- Python, TypeScript, SQL (required core stack)
- FastAPI, PostgreSQL, Redis, React, AWS (all nice-to-have stack items)
- Next.js, Node.js, Firebase, Docker (full-stack production evidence)
- AI Gateway, LiteLLM, LLM evaluation, RAG, MCP, Guardrails, Langfuse (applied AI infrastructure)
- Playwright, Vitest, Jest, CI/CD gates, 44 red-team fixtures (testing/deployment/monitoring)
- Drizzle ORM, SSO, RBAC, JWT, Auth0, Anti-CSRF, Audit logging, PII tokenization (security/auth)
- PySpark, 20+ TB, 700+ companies, 160+ tables, 41+ test suites, 1,000+ SQL tables, 110 users (quantified scale)
- Startup experience (Actual Reality, SmartSolve)
- Document processing adjacency: FalconGraph (PDF/DOCX/HTML ingestion, FastAPI, FAISS, RAG), Fix-It-Flow (Gemini Vision)

### Gaps / intentionally omitted unsupported keywords
- **Document intelligence core**: OCR, low-latency OCR, layout understanding, component detection, reading-order algorithms, proprietary table structure recognition, table parsing, fine-tuned vision-language models for charts/tables/figures -- no direct experience; adjacent RAG/document ingestion only (FalconGraph)
- **Computer vision / NLP specialization**: No production CV/NLP model training or fine-tuning; Gemini Vision usage in Fix-It-Flow is API consumption only
- **Postgres** (exact variant): Resume uses "PostgreSQL"; JD says "Postgres" -- covered by adjacent evidence
- **Secure APIs** (exact phrase): Resume uses "APIs" and "guardrails"; covered by adjacent evidence
- **Front end features** (exact phrase): Resume uses "customer portal" and "onboarding system"; covered by adjacent evidence
- **Extraction pipeline / accuracy / latency / reliability** (exact phrases): Resume uses "evaluation pipeline" and "accuracy" in AI context; adjacent evidence only
- **Deployments / Production health / Production monitoring** (exact phrases): Resume uses "CI/CD gates", "Langfuse tracing", "Slack alerts"; adjacent evidence
- **Tests** (exact term): Resume uses "regression test suites", "smoke test", "CI/CD gates"; adjacent evidence
- **Bias to ship / Clear communication**: Soft skills -- not claimed as technical keywords
- **On-site / San Francisco / 5 days in-office**: Location requirement -- tracked in F-1 gate, not a resume skill
- **Multi-stage architecture** (exact phrase): Resume describes pipeline architecture but not this exact phrase
- **Data infrastructure** (exact phrase): Resume covers data engineering at scale but not this exact phrase

### Recommended improvements
1. If Aryan has any document processing / OCR / table extraction experience (coursework, hackathon, private repo), add to profile and resume.
2. Consider adding "Postgres" as a variant alongside "PostgreSQL" in skills section for exact-term matching.
3. Add "Deployments" and "Production monitoring" to skills or bullets for exact-term coverage.
4. Strengthen document intelligence adjacency in cover letter (already done via FalconGraph reference).
5. If targeting similar document intelligence roles long-term, build a focused project demonstrating PDF/table extraction or layout analysis.

### Expanded role-specific keyword pass:
Ran expanded keyword audit with 67 terms from the full job description (see expanded-terms.txt). Found 34 terms in resume, 33 missing. Missing terms are primarily document-intelligence-specific (OCR, VLM, table parsing, layout understanding) and exact-phrase variants. Adjacent evidence documented for partially supported terms. Full results recorded in analyzer output.

## Sub-90 Readiness Waiver
This package scores 83/100, below the 90/100 internal readiness gate. The primary gap is the specialized document intelligence domain that constitutes Pulse's core differentiation: OCR, layout understanding, component detection, reading-order algorithms, table structure recognition/parsing, and fine-tuned vision-language models for charts/tables/figures. Aryan has strong adjacent evidence (FalconGraph RAG document ingestion, FastAPI document processing pipeline, Fix-It-Flow Gemini Vision API consumption, AI Gateway evaluation infrastructure) but no direct experience with the specific document understanding stack Pulse has built.

The waiver is justified because:
1. The posting considers new grads and values "eager to learn and adapt quickly" -- the role is open to adjacent skill transfer.
2. Sponsorship is available, removing a common blocker for international candidates.
3. All required core skills (Python/TypeScript/SQL) and nice-to-have stack items (FastAPI, PostgreSQL, Redis, React, AWS) are truthfully covered with production evidence.
4. The full-stack + AI infrastructure experience (LiteLLM gateway, evaluation pipelines, customer portal, 20+ TB data pipelines) demonstrates the engineering caliber Pulse seeks.
5. No unsupported claims were added to inflate the score; the gap is documented transparently.

Aryan intends to proceed with this application given the sponsorship availability, strong stack alignment, and the role's openness to learning. The cover letter explicitly references the adjacent document processing experience (FalconGraph) to bridge the gap.

## Verification Gates

- Gap recovery gate checked: Pass
- ATS source gate checked: Pass
- Human recruiter readability gate checked: Pass
- Visual consistency gate checked: Pass
- Page utilization gate checked: Pass
- Submitted-facing terminology sync checked: Pass
- Score consistency gate checked: Pass
- Cover-letter artifact checked: Pass

## Application-answer human voice gate checked: Pass
No application questions provided with this job description.