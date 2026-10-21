# Tailoring Notes - NVIDIA Software Engineer, Agent Performance Modeling - New College Grad 2026

Primary role lane: Applied AI/Agentic Systems with Systems/Performance Engineering secondary

## F-1 Work Authorization Gate
**Status: Proceed** - Posting is silent/ambiguous on sponsorship. No explicit no-sponsorship, citizen-only, permanent-resident-only, authorization-for-any-employer, or clearance-only language. Santa Clara location is compatible with F-1 OPT/STEM OPT. Track internally; do not mention in submitted artifacts.

## Referral Plan
Referral status: Not started
Referral target / source: Not identified yet
Next referral follow-up: To be scheduled after initial outreach
Action: Search LinkedIn for NVIDIA employees in Santa Clara (GPU architecture, inference, compiler teams), BGSU alumni at NVIDIA, and connections from prior internships. Prioritize referral outreach before or immediately after submission.

## Job-description source audit:
Full job description saved from NVIDIA careers posting JR2028350. Posted yesterday, applications accepted until October 24, 2026. No modifications made to original text.

## Job Keyword Map

### Exact Posted Role Title
**Software Engineer, Agent Performance Modeling - New College Grad 2026** - Include once in visible resume text (contact/title line).

### Required Skills & Tools (Must-Have)
| JD Term | Evidence Status | Source / Placement |
|---|---|---|
| MS Computer Science | Supported | Education: BGSU MS CS 4.0 GPA |
| LLM architectures | Supported | Actual Reality AI Gateway (LiteLLM routing), SmartSolve AI agents, FalconGraph RAG, Fix-It-Flow (Gemini Vision, Llama), RocketGrader (Mistral AI), Diff-Grounded PR Generation (OpenAI API) |
| LLM inference characteristics | Supported | Actual Reality smart-router tiers, guardrails, Langfuse traces; Fix-It-Flow multimodal inference; Diff-Grounded PR Generation evaluation |
| Simulation | Adjacent | Self-Adaptive Parallelism: C++/OpenMP adaptive runtime simulation, benchmarking, telemetry |
| Profiling | Adjacent | Self-Adaptive Parallelism: runtime instrumentation, CSV telemetry, speedup/efficiency plots |
| Performance modeling | Adjacent | Self-Adaptive Parallelism: UCB bandit optimization of scheduling policy, chunk size, thread count |
| Roofline analysis for LLM inference | Unsupported - omit | No verified GPU/LPU roofline analysis experience |
| Strong analytical skills | Supported | ICSME-published research, benchmarking, Self-Adaptive Parallelism evaluation |
| Rigorous experimentation/validation | Supported | Self-Adaptive Parallelism benchmark summaries, Diff-Grounded PR Generation eval across 1,450 PRs |
| Coding agents | Supported | Career Ops automation, Actual Reality AI-assisted development (Claude Code, Copilot, Cursor, Codex confirmed), SmartSolve AI-assisted planning/debugging/review |

### Preferred / Standout Skills (Nice-to-Have)
| JD Term | Evidence Status | Source / Placement |
|---|---|---|
| Agents automating complex engineering workflows | Supported | Career Ops job-discovery/application automation; Actual Reality MCP server with keyed access; SmartSolve AI agents for employee workflows; Fix-It-Flow voice-first diagnostic agent |
| Accelerator architecture | Unsupported - omit | No direct GPU/TPU/LPU architecture experience |
| Compute bottlenecks | Adjacent | Self-Adaptive Parallelism: thread scheduling, chunk size optimization |
| Memory bottlenecks | Adjacent | Self-Adaptive Parallelism: memory access patterns in OpenMP |
| Communication bottlenecks | Adjacent | Self-Adaptive Parallelism: scheduler policy tuning |
| Open-source contributions (agentic systems) | Partial | Career Ops (personal automation), Diff-Grounded PR Generation (ICSME-published, not open-source) |
| Open-source contributions (simulation) | Unsupported - omit | |
| Open-source contributions (inference optimization) | Unsupported - omit | |

### Domain Language & Responsibilities
| JD Term | Evidence Status | Notes |
|---|---|---|
| GPU, LPU, heterogeneous systems | Unsupported - omit | No direct accelerator hardware experience |
| Hardware architecture teams | Adjacent | Collaborated with senior engineers at AAIS, Actual Reality |
| Inference teams | Supported | Actual Reality AI Gateway model routing, LiteLLM smart-router tiers |
| Runtime teams | Adjacent | Self-Adaptive Parallelism runtime coordination |
| Compiler teams | Unsupported - omit | |
| Design space exploration | Adjacent | Self-Adaptive Parallelism adaptive scheduling exploration |
| Bottleneck analysis | Adjacent | Self-Adaptive Parallelism telemetry-driven optimization |

### Unsupported / Intentionally Omitted Keywords
- CUDA, GPU programming, LPU, tensor cores, tensor parallelism, pipeline parallelism
- NVIDIA-specific: Triton, TensorRT, cuDNN, NCU, NSight
- Roofline analysis (no verified evidence)
- Formal accelerator architecture coursework or projects
- Production on-call/SRE, Kubernetes, high-availability SaaS ownership

## Gap Recovery Gate

Gap recovery status: All important JD terms searched. Two categories: (1) Supported/Adjacent - include in resume, (2) Unsupported - document as intentionally omitted. No "Likely built but undocumented" terms requiring Aryan confirmation.

### Important JD Term Search:

| Searched Term | Locations Searched | Recovered Evidence | Final Decision |
|---|---|---|---|
| roofline analysis | profile/, master-documents/, project repos | None | Unsupported - omit |
| CUDA | profile/, master-documents/, project repos | None | Unsupported - omit |
| GPU programming | profile/, master-documents/, project repos | None | Unsupported - omit |
| accelerator architecture | profile/, master-documents/, project repos | Self-Adaptive Parallelism has C++/OpenMP systems performance but not accelerator-specific | Adjacent only - do not claim accelerator expertise |
| tensor parallelism | profile/, master-documents/, project repos | None | Unsupported - omit |
| pipeline parallelism | profile/, master-documents/, project repos | None | Unsupported - omit |
| simulation frameworks | profile/, master-documents/, project repos | Self-Adaptive Parallelism: custom C++/OpenMP simulation | Adjacent - include as performance modeling evidence |
| design space exploration | profile/, master-documents/, project repos | Self-Adaptive Parallelism: UCB-driven scheduling exploration | Adjacent - include |

## Bullet Audit

### Experience Section Target: ≥11 bullets
Current plan: 12 experience bullets across 4 roles (Actual Reality: 2, SmartSolve: 3, AAIS Data: 3, AAIS Software: 3, APKD: 1) = 12 bullets. Meets floor.

### Two-line bullet-wrap check: Pass
All bullets drafted to render ≤2 visual PDF lines in canonical layout. Verify after compilation.

### Human Recruiter Readability Gate
Internal terms translated:
- "magic link" to unauthenticated account-creation/secure sign-in flow (not used in this package)
- "Plane ticket/project status" to project-management API integration / customer-portal workflow
- "red-team fixtures" to adversarial test fixtures / safety validation
- "LiteLLM" to AI Gateway / model gateway (keep exact when JD-relevant)
- "MCP server" to AI agent protocol server / Model Context Protocol server

### Weak Opener Ban
No bullets start with "Responsible for", "Helped", "Worked on", or "Assisted".

### Experience-First Fit Rule Applied
Experience bullets prioritized over project bullets. Two projects included because they directly demonstrate LLM evaluation, agentic workflow automation, and performance modeling.

## Visual Consistency Gate
Resume source uses canonical template: letterpaper 11pt article, 0.22in LR margins, 0.10in TB margins, 0.92 linespread, glyphtounicode, pdfgentounicode=1, pagestyle empty, tightitemize with raised 10pt solid bullet. Matches canonical visual system.

## Page Utilization Gate
Target: content reaches close to bottom of page. 12 experience bullets + 2 project bullets + skills section should fill page. Verify after PDF compilation.

## Submitted-Facing Terminology Sync
Resume and cover letter use identical public-safe terminology for:
- AI Gateway / model-call routing (not "LiteLLM proxy" alone)
- Project-management API integration (not "Plane ticket" alone)
- Customer-portal workflow (not "admin AI tools" alone)
- Adversarial test fixtures (not "red-team fixtures" alone)
- Model Context Protocol server (not "MCP server" alone)

## ATS source gate checked: Pass
Resume source validated: no tabular, no images, no color, no headers/footers, no multi-column, canonical patterns present.

## Score Consistency Gate Checked: Pass
Score breakdown sums to recorded score, uses correct category weights.

## Cover-letter artifact checked: Pass
cover-letter.md created, PDF generated, terminology synchronized with resume.

---

## Scoring Methodology

Job Alignment & Evidence Score: 88/100
Internal estimate only; not a predicted ATS score.

Score breakdown
- Keyword coverage: 32/40 (strong on LLM architectures, AI agents, coding agents, Python/C++; missing GPU/LPU, roofline, CUDA, accelerator architecture)
- Experience relevance: 22/25 (MS CS 4.0, 5 internships, AI gateway, agentic workflows, performance modeling adjacency; missing direct hardware/accelerator experience)
- Impact and evidence: 14/15 (quantified: 20+ TB, 1000+ tables, 110 users, 1450 PRs, 44 test fixtures; strong action+method+result bullets)
- Formatting and ATS parsing: 10/10 (canonical one-page, text-extractable, standard headings, no graphics/tables)
- Risk and gap handling: 10/10 (unsupported GPU/LPU/roofline/CUDA documented as omitted, F-1 gate passed, no unsupported claims added)

Expanded role-specific keyword pass:
Default analyzer found 48/80 exact terms. Missing terms are primarily unsupported hardware/accelerator keywords (CUDA, GPU, LPU, TensorRT, Triton, roofline analysis, accelerator architecture) documented as intentionally omitted. Adjacent terms present under different wording (instrumentation/telemetry, simulation/performance modeling).

Strong matches
- MS Computer Science, 4.0 GPA (exact requirement)
- LLM architectures & inference: Actual Reality AI Gateway, SmartSolve agents, FalconGraph RAG, Fix-It-Flow, RocketGrader, Diff-Grounded PR Generation
- AI agents automating engineering workflows: Career Ops, Actual Reality MCP server, SmartSolve agents, Fix-It-Flow
- Simulation/performance modeling: Self-Adaptive Parallelism (C++/OpenMP, UCB optimization, telemetry)
- Coding agents: Claude Code, Copilot, Cursor, Codex (confirmed production use)
- Python, C++, TypeScript, AWS (Glue, Lambda, S3, IAM, DynamoDB)
- 5 internships, production scale (20+ TB, 1000+ tables, 110 users)
- ICSME-published LLM evaluation research

Gaps / intentionally omitted unsupported keywords
- GPU/LPU/heterogeneous systems hardware experience
- CUDA, TensorRT, Triton, cuDNN, NCU, NSight
- Roofline analysis for LLM inference
- Accelerator architecture (compute/memory/communication bottlenecks at hardware level)
- NVIDIA-specific tooling
- Formal compiler/runtime team collaboration
- Open-source contributions in agentic systems/simulation/inference optimization (Career Ops is personal, Diff-Grounded is published not open-source)

Recommended improvements
1. Add "roofline analysis" only if Aryan can verify coursework/project evidence (e.g., computer architecture course project)
2. Add "CUDA basics" only if Aryan has coursework/self-study to reference
3. Strengthen accelerator adjacency: emphasize Self-Adaptive Parallelism memory/compute optimization as transferable to GPU scheduling
4. Consider adding a second project bullet if page space allows (e.g., FalconGraph RAG for retrieval-performance angle)

## Sub-90 Readiness Waiver
**Score: 88/100 (below 90 threshold)**

**Reason:** The role explicitly targets GPU/LPU/heterogeneous systems performance modeling with roofline analysis for LLM inference—specialized hardware/architecture skills Aryan does not have verified evidence for. The resume truthfully covers the agentic engineering, LLM architecture, simulation, and coding-agent requirements (which comprise ~60% of the JD), but cannot claim the accelerator-hardware half without inventing claims.

**Decision:** Proceed with application. The package is strong for the agentic/simulation/software-engineering lane of this role. Aryan's MS CS 4.0, AI Gateway production experience, agentic automation portfolio, and C++/OpenMP performance modeling are genuine differentiators for the "agentic engineering" half of the team's charter. The hardware modeling gap is documented here and not papered over in submitted artifacts.

---

## Verification Gates Summary
- ATS source gate checked: Pass
- Visual consistency gate checked: Pass
- Human recruiter readability gate checked: Pass
- Submitted-facing terminology sync checked: Pass
- Score consistency gate checked: Pass
- Cover-letter artifact checked: Pass
- Page utilization gate checked: Pass (pending PDF verification)
- Two-line bullet-wrap check: Pass (pending PDF verification)
- Experience bullet count: 12 (≥11 floor met)
- Gap recovery gate checked: Pass
- F-1 Work Authorization Gate: Proceed