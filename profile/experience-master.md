# Experience Master

This document is the source of truth for Aryan Miriyala's professional experience. Use it to build targeted resumes, cover letters, interview stories, and role-specific bullet banks.

## Standard Role Structure

Each role should preserve enough detail to support resumes, cover letters, LinkedIn, interview prep, and job-specific tailoring.

- Use the same section order for every role. Do not add role-specific alternate-description sections unless the same structure is added for every role.
- `Platform-Ready Description`: copyable paragraph for LinkedIn experience descriptions, cover-letter context, or an expanded project/experience section.
- `Handshake Description`: copyable role description for Handshake experience entries. Must be 500 characters or fewer.
- `Tech Stack`: one comma-separated line with a domain prefix, such as `Data engineering / Tech stack: Python, PySpark, AWS Glue.`
- `Business / Problem Context`: why the work mattered to the organization or users.
- `Problem / Company Impact Context`: specific problems solved, scale, or operational impact.
- `Work Performed`: factual inventory of work completed.
- `Positioning Angles`: ways to frame the role for different job families.
- `Reusable Bullet Options`: ATS-friendly bullets for resumes and tailored applications.

## Positioning Summary

Aryan's experience sits at the intersection of full-stack software engineering, cloud data engineering, AI-assisted development, security-aware application work, and legacy system modernization.

Core themes:

- Full-stack product engineering with Next.js, React, Angular, Node.js, PostgreSQL, MongoDB, Auth0, SSO, and role-based access control.
- Current software engineering internship experience at Actual Reality Technologies, positioned around augmented-intelligence, data-modeling, app-development, and manufacturing/process-improvement contexts. Exact repo-level claims require confirmation from Aryan or authenticated GitHub access before use in submitted artifacts.
- Cloud and data engineering with AWS Glue, S3, Lambda, PySpark, MySQL, Impala, Oracle, PostgreSQL, JDBC, and Semarchy MDM.
- AI-first engineering with Codex, Claude Code, LangChain, RAG, Mistral AI, HuggingFace, PyTorch, and TensorFlow.
- Security and compliance work involving SSO, JWT, RBAC, anti-CSRF tokens, PII tokenization, audit logging, and protected workflows.
- Legacy modernization involving ColdFusion/Lucee/CFML, HTML5 form updates, JavaScript fallbacks, CSS modernization, Bootstrap UI, and reusable modal/tab components.
- Cybersecurity education and research support through BGSU graduate research work, including CyberGuardian modules, ethical-hacking lab materials, NICE Framework/CAE-CD curriculum analysis, email security/forensics, cryptography, phishing demos, and workforce/curriculum gap analysis.

## Actual Reality Technologies

Title: Software Engineer
Dates: Jul. 2026 - Present
Location: Perrysburg, OH

### Resume Strategy & Presentation Rule

- **Resume Subheading (Mandatory for all application resumes):**
  ```latex
  \resumeSubheading
  {Software Engineer}{Jul. 2026 - Present}
  {Actual Reality Technologies}{Perrysburg, OH}
  ```
- **Strategic Intent:**
  - Aryan has been performing continuous software engineering work at Actual Reality since July 2026, delivering 1,476 commits on the customer portal, building the IRIS Playwright validation harness, deploying remote MCP tools, and integrating the LiteLLM AI Gateway.
  - Never include "promoted", "intern", or parenthetical date splits like `(Intern: Jul. 2026 -- Sep. 2026)` in the resume header or experience subheading.
  - Splitting the tenure or calling out the internal promotion in the resume header fractures Aryan's four-month tenure into a 1-month full-time line, breaks the strategic intent of the resume, introduces unnecessary administrative distraction, and risks confusion in automated ATS date parsers.
  - Showing `Software Engineer | Jul. 2026 - Present` presents an uninterrupted, truthful, and high-impact narrative.
  - The internal transition from intern to full-time in October 2026 is strictly conversational background for interviews to demonstrate speed of delivery and impact, not resume header content.
- **Internal Verification History:**
  - Transitioned from Software Engineering Intern (Jul. 2026 - Sep. 2026) to full-time Software Engineer in October 2026. Location: Perrysburg, OH. Continuous employment with no break in service.

### Platform-Ready Description

Full-time Software Engineer (promoted from Software Engineering Intern in October 2026) at Actual Reality Technologies, building AI systems infrastructure and production web applications. Current work centers on the IRIS project, an advanced glass-research and materials science AI expert system developed for the Northwest Ohio Innovation Consortium (NOIC) on ActualChat. IRIS serves glass scientists, materials engineers, and industrial researchers across furnace dynamics, glass chemistry, defect analysis, ASTM/ISO testing standards, and patent landscape queries using dual-source RAG (LlamaIndex/LlamaCloud knowledge base and live web search). Engineering contributions for IRIS include architecting an automated validation gate runner that drives the live chat API via headless Chrome (Playwright) to systematically test multi-turn conversations, verify tool calling, parse streaming SSE replies, and validate citation accuracy against 41+ test cases reconstructed from an extensive 79-finding University of Toledo bug-hunt backlog with rigorous thermodynamic and physics equations (NIST-JANAF enthalpies, steam heat content, Stokes' law calculations). Also connected the IRIS sandbox environment to the company's LiteLLM AI Gateway on staging using pinned Gemini model endpoints to evaluate model routing, safety guardrails, and latency. Concurrently revamped, hardened, and wrapped up the company's customer portal (`my.actualreality.ai`) end-to-end as its primary engineer across 1,476 commits, delivering two-way Plane API ticket and intake reconciliation, client retainer tracking, remote Model Context Protocol (MCP) server tools for AI agents, multi-tenant session isolation, per-user notification read states, interactive Gantt timelines, Firestore index and query reliability, and exhaustive smoke test suites.

### Handshake Description

Full-time Software Engineer (promoted from Intern) at Actual Reality Technologies, building the validation gate runner and AI Gateway evaluation pipeline for the IRIS glass-research AI chatbot, and revamping the production Next.js/Firebase customer portal end-to-end across 1,476 commits with Plane two-way synchronization, retainer hours tracking, and remote MCP tools.

### Tech Stack

Software engineering / Full-Stack, AI Systems & Testing / Tech stack: LibreChat, ActualChat (enterprise LibreChat fork), Node.js, Express, React, MongoDB, Redis, WebSocket, TypeScript, Next.js 15, React 19, Firebase, Firebase Auth, Firebase Admin, Firestore rules/indexes, Playwright, Headless Chrome, Jest, Vitest, Testing Library, ESLint, Tailwind CSS, Plane API, Model Context Protocol (MCP), remote MCP servers, LiteLLM, AI Gateway, Railway, Gemini API (`gemini-3.1-pro-preview`, `gemini-3.5-flash`), smart-router tiers, guardrails, Langfuse tracing, Slack block alerts, CI/deploy gates, Server-Sent Events (SSE), streaming chat APIs, YAML test suites, thermodynamic calculations (NIST-JANAF), Stokes' law calculations, multi-turn dialogue evaluation, authentication/session cookies, session isolation, role provisioning, Gantt/timeline UI, dotenvx, feature flags, smoke testing.

### Business / Problem Context

Actual Reality Technologies builds augmented intelligence, AI systems, predictive analytics, and enterprise platforms for manufacturing, material science, and operational clients. Aryan's work spans two major initiatives: the IRIS glass-research AI platform for the Northwest Ohio Innovation Consortium (NOIC), and the core Actual Reality customer portal (`my.actualreality.ai`).

#### The IRIS Project: Glass-Research AI Expert System for NOIC

The Northwest Ohio Innovation Consortium (NOIC) is a regional innovation alliance uniting glass manufacturers, industrial research institutes, and universities (including the University of Toledo and Bowling Green State University) to accelerate advanced manufacturing, decarbonization, and material science innovation. Actual Reality was commissioned to build IRIS, a specialized AI assistant designed to act as an authoritative technical research expert for glass scientists, plant engineers, and materials researchers.

Key architectural and domain pillars of IRIS include:
- **Domain Scope:** High-accuracy answers across glass chemistry (silicates, borosilicates, soda-lime), melting and refining dynamics, batch formulation, furnace thermal profiles, refractory wear, emissions, quality defects (stones, cords, seeds, blisters), ASTM/ISO standard testing methods (e.g., ASTM C169, C1279, C1499, E1300), and patent landscape exploration.
- **Dual-Retrieval RAG Engine:** Built on ActualChat (an enterprise conversational AI platform running on Railway with MongoDB and Redis). Combines an internal LlamaCloud / LlamaIndex vector database (indexing thousands of glass patents, technical papers, conference symposia, and proprietary industry reports) with live web search for recent literature.
- **Strict Provenance & Citations:** Every assertion requires explicit citation anchors (`\ue202turn{MESSAGE_ID}file{INDEX}`) mapped to verified source passages, alongside calibrated confidence ratings (High, Moderate, Low).

#### The Problem: The University of Toledo Bug-Hunt & Phase 1 Backlog

Following initial Phase 1 delivery, engineering students at the University of Toledo executed an intensive bug hunt on June 8, 2026, surfacing a backlog of 79 documented findings. These issues threatened user trust in safety-critical manufacturing contexts:
1. **Calculation Errors & Hallucinations:** Fabricated batch chemistry numbers, wrong units, and arithmetic errors in thermodynamic formulas caused by LLMs calculating in-weights rather than executing code tools.
2. **Retrieval & Context Clashes:** Uploaded user files were clobbered when LlamaIndex vector searches triggered, and follow-up queries lost conversation context.
3. **Scope & Overconfidence:** The system answered out-of-domain general questions instead of declining per the glass-only scope, or stated speculative assertions with unwarranted certainty.
4. **Code & Platform Bugs:** File-search timeouts, hanging worker threads, and unescaped LaTeX/math rendering (`$`) in ActualChat.

#### The Strategy: Dual-Track Phase 1 Wrap-up & AI Gateway Integration

To deliver validated fixes to NOIC by late October 2026 while de-risking a proposed Phase 2 AI Gateway contract, Actual Reality structured two parallel tracks:
- **Track 1 (Direct ActualChat Fixes):** Directly resolving core code bugs (file search context preservation, relevance threshold filtering), configuring agents to mandate code execution for calculations, and tuning prompt boundary instructions.
- **Track 2 (AI Gateway Discovery & Integration):** Connecting the IRIS sandbox (`iris-sandbox.up.railway.app`) to Actual Reality's LiteLLM AI Gateway on staging (`litellm-staging-b883.up.railway.app`) under dedicated tenant credentials, evaluating pinned Gemini models (`gemini-3.1-pro-preview`), inspecting guardrails (prompt injection, Presidio PII filtering), and tracking request latencies and Langfuse traces.
- **The Validation Gate Contract:** Neither direct code fixes nor gateway routing could be promoted to production without passing an empirical validation gate: a finding was only marked resolved if it reproduced on the "before" setup and passed at least 4 out of 5 consecutive runs on the "after" setup, evaluated via structured LLM-as-a-judge scoring with data science oversight. This automated gate runner was designed and built by Aryan.

### Problem / Company Impact Context

- Promoted to full-time Software Engineer in October 2026 following successful internship delivery across AI Gateway and customer portal initiatives; immediately took ownership of the IRIS project evaluation and gateway promotion track.
- Enabled NOIC (Northwest Ohio Innovation Consortium) consortium partners, researchers, and glass manufacturers to trust IRIS for mission-critical industrial queries, turning an experimental prototype burdened by 79 bug-hunt issues into an enterprise-ready research platform backed by empirical validation evidence.
- Generated the empirical data de-risking NOIC's Phase 2 AI Gateway Statement of Work (SOW), comparing direct-Gemini baselines against LiteLLM gateway-routed models on staging to demonstrate measurable gains in response accuracy, citation survival, and guardrail protection.
- Architected and built the IRIS validation gate runner (IRIS-61 / PR #85), an automated Node.js CLI driving headless Chrome (Playwright) to validate the real chat API against sandbox endpoints with host allowlisting, SSE parsing, citation extraction, tool-call tracking, timeout/abort handling, and opt-in concurrency.
- Connected the IRIS sandbox environment to the AI Gateway staging infrastructure (IRIS-59 / PR #83) with dedicated tenant configuration in `actualchat.yaml`, binding the gateway agent to pinned Gemini models (`gemini-3.1-pro-preview`).
- Systematically designed and rebuilt a 41-case test set from 79 bug-hunt findings (IRIS-52, IRIS-53, IRIS-54, IRIS-55, IRIS-60), mathematically verifying complex glass chemistry and physical calculations using NIST-JANAF reaction enthalpies, steam enthalpy changes (500°C -> 1450°C), batch reaction energetics, and Stokes' law bubble rising velocities.
- Completely revamped and wrapped up the customer portal (`my.actualreality.ai`) end-to-end across 1,476 authored commits, turning a fragile prototype into a hardened production platform.
- Engineered two-way support ticket and intake reconciliation between the customer portal and Plane (PORTAL-177, PORTAL-160, PORTAL-161, PORTAL-162, PORTAL-194), delivering Plane decisions, decline explanations, standing-decline cursors with retry logic, and 10-minute periodic sync.
- Built client retainer management and hours tracking (PORTAL-197, PORTAL-200), allowing administrators to configure monthly retainers in Company Settings and automatically aggregating worked hours across all linked projects.
- Developed remote Model Context Protocol (MCP) server tools (PORTAL-182) that allow customer and admin AI tools to query team member profiles, team rosters, and Plane project/ticket statuses with keyed access and cost controls.
- Hardened multi-tenant session isolation (PORTAL-198, PORTAL-201) to prevent older staff sessions from overriding client identities, enabled staff to run internal clients without customer logins, and removed magic links in favor of secure password authentication (PORTAL-118).
- Fixed notification state leaks (PORTAL-199) by decoupling read states so one user marking a notification read does not clear it for the entire client organization.
- Stabilized the Firestore data layer by fixing `useCollection` query constraint keying (PORTAL-122), exporting composite indexes to version control (PORTAL-123), and adding bounded backoff re-subscription for failed client reads (PORTAL-121, PORTAL-141).
- Added an interactive Gantt / Timeline layout to project boards (PORTAL-175) and consolidated fragmented workflow tools into a unified tabbed Workshop route (PORTAL-72).
- Authored an exhaustive smoke test inventory covering all customer and admin surfaces (PORTAL-145, PORTAL-151, PORTAL-202).
- Deployed a pinned LiteLLM AI Gateway on Railway for intelligent model routing, smart-router tiers, guardrail policies, Langfuse tracing, Slack alerts, CI/deploy gates, and 44 red-team fixtures.

### Work Performed

- Promoted to Software Engineer (Full-Time) in October 2026.
- Primary engineer and author of 1,476 commits in `Actual-Reality/customer-portal`, driving the application from early development through complete end-to-end wrap-up and production deployment.
- Author of PR #85 (IRIS-61: Build validation gate runner) in `Actual-Reality/ActualChat`, building the headless Chrome testing harness in `config/iris-gate/` with Jest test suites, SSE event stream decoding, and answer/citation/tool-call extraction.
- Author of PR #83 (IRIS-59: Connect the IRIS sandbox to gateway staging) in `Actual-Reality/ActualChat`, implementing tenant configuration specs, Gemini model binding, and test coverage.
- Authored PR #91 (IRIS-53) and PR #92 (IRIS-54) in `Actual-Reality/ActualChat`, constructing exact and rebuilt YAML test cases for student bug-hunt findings with pass/fail evaluation criteria.
- Authored tickets IRIS-55 and IRIS-60, conducting technical investigations into glass batch calculation formulas, reaction enthalpies, and multi-turn challenge conversation recovery.
- Completed customer portal tickets PORTAL-72 through PORTAL-202 spanning Plane two-way triage sync, retainer hours tracking, remote MCP tools, notification read-state isolation, session cookie domain logic, Firestore index and query constraint fixes, and exhaustive smoke test suites.

### Positioning Angles

- Full-time Software Engineer promotion
- AI Systems & LLM evaluation infrastructure
- Validation gate runner & headless browser automation
- End-to-end customer portal architecture and delivery
- Model Context Protocol (MCP) server development
- Full-stack TypeScript, Next.js 15, and React 19 engineering
- Two-way API synchronization and cursor-based reconciliation
- Multi-tenant authentication, session isolation, and RBAC
- Enterprise client retainer management and hours tracking
- Firestore data modeling, query optimization, and security rules
- Observable AI Gateway routing and safety policy
- Test automation (Jest, Vitest, Playwright, Testing Library)
- Domain modeling in material science and glass research

### Reusable Bullet Options

- Engineered features for IRIS, an enterprise glass-research AI platform built on a LibreChat fork (Node.js, React, MongoDB), integrating an internal LiteLLM gateway with multi-tier routing and Langfuse tracing.
- Built an automated evaluation pipeline with Node.js and Playwright to validate multi-turn IRIS reasoning, tool execution, and citation accuracy across 41+ regression test suites.
- Built evaluation infrastructure and gateway integration for IRIS, an advanced glass-research AI expert system developed for the Northwest Ohio Innovation Consortium (NOIC), enabling glass scientists and manufacturers to query complex melting chemistry, ASTM standards, and patents with verified citations.
- Led evaluation infrastructure and gateway integration for the IRIS glass-research AI chatbot on ActualChat (LibreChat fork), configuring pinned Gemini models, tenant specs, and automated configuration tests.
- Built an automated validation gate runner with Node.js, Playwright, and headless Chrome, executing multi-turn evaluations against live chat APIs and extracting answers, tool calls, and citations across 41+ bug-hunt test cases.
- Connected the IRIS AI chatbot sandbox to an internal LiteLLM AI Gateway on staging, configuring pinned Gemini models, tenant specs, and automated configuration tests.
- Reconstructed 41+ bug-hunt test cases into structured YAML suites, verifying complex chemical and thermodynamic calculations using NIST-JANAF reaction enthalpies, steam heat content, and Stokes' law bubble rising velocities.
- Architected the production customer portal with Next.js 15, React 19, and Firebase, delivering multi-tenant session isolation, client retainer tracking, and automated support ticket reconciliation.
- Built two-way Plane API synchronization for support tickets and intake, delivering triage decisions, mandatory decline explanations, and standing-decline cursors with retry logic.
- Implemented client retainer tracking in Company Settings, aggregating worked hours across all linked projects to provide transparent retainer utilization for clients and administrators.
- Developed remote Model Context Protocol (MCP) tools with keyed authentication, allowing AI agents to securely query team member profiles, team rosters, and Plane project/ticket statuses under cost and rate controls.
- Hardened multi-tenant session isolation and role provisioning, preventing older staff sessions from overriding client logins and eliminating magic links for secure password authentication.
- Deployed a LiteLLM AI model gateway for policy-controlled model routing across multiple AI projects, adding intelligent routing tiers, guardrails, Langfuse tracing, Slack alerts, CI/CD gates, and 44 adversarial test fixtures.
- Consolidated Capture, Define, and Whiteboard tools into a tabbed Workshop route with feature gating, legacy redirects, ARIA guardrails, and route/component tests using Vitest and Testing Library.

### Source And Verification Notes

- Confirmed by Aryan: promoted to full-time Software Engineer at Actual Reality Technologies in October 2026; prior role was Software Engineering Intern (July 2026 - September 2026). Location: Perrysburg, OH.
- Repositories inspected in `/Users/aryanmiriyala/Desktop/Actual-Reality`: `ActualChat` (branches `iris-sandbox`, `IRIS-53...`, `IRIS-54...`, `IRIS-55...`, `IRIS-60...`), `customer-portal` (1,476 commits by Aryan Miriyala), `iris-gate`, and `iris-gateway`.
- Key ActualChat PRs authored by Aryan: PR #85 (IRIS-61: Build validation gate runner), PR #83 (IRIS-59: Connect the IRIS sandbox to gateway staging), PR #91 (IRIS-53), PR #92 (IRIS-54).
- Key Customer Portal PRs/commits authored by Aryan: PORTAL-72 through PORTAL-202, including PORTAL-177 (Plane triage sync), PORTAL-182 (MCP tools), PORTAL-197 / PORTAL-200 (retainer hours tracking), PORTAL-198 / PORTAL-201 (session isolation & internal clients), PORTAL-199 (notification read state), PORTAL-121 / 122 / 123 / 141 (Firestore reliability), PORTAL-145 / 151 (smoke test inventory).
- IRIS project intent and planning documents inspected: `IRIS Phase 1 Plan (draft, 2026-10-06).md`, `IRIS Phase 1 Wrap-up × AI Gateway_ Intent.pdf`, `IRIS-52 notes.md`, `IRIS-53-pr-body.md`, `IRIS-54-pr-body.md`, `IRIS-55-notes.md`, `IRIS-60-notes.md`.
- AI Gateway field guide inspected: `profile/source-materials/actual-reality/ai-gateway-field-guide.docx` (pinned LiteLLM proxy on Railway, smart-router tiers, guardrails, Langfuse tracing, 44 red-team fixtures).

## SmartSolve Industries

Role: Artificial Intelligence Engineer Intern  
Location: Bowling Green, OH  
Dates: May 2026 - Jul. 2026

### Platform-Ready Description

Worked on AI-enabled internal software at SmartSolve, combining full-stack engineering, secure workflow design, AI adoption planning, and AI-assisted development for quality-management and operations tooling. Work followed a phased AI integration roadmap covering environment onboarding, AI tool audits, department workflow improvements, role-specific AI coaching, internal knowledge-base documentation, LLM/API and cloud-service evaluation, prototype planning, stakeholder-facing technical updates, and handoff planning. Specific engineering work included planning a QMS dependency register to model relationships between quality documents, building a Next.js onboarding tracker with PostgreSQL, Drizzle ORM, SSO, and authentication middleware for HR/new-hire workflows, and creating Docker devcontainers for WSL2 and Colima to make development environments reproducible while keeping AI-assisted tooling isolated around proprietary code.

### Handshake Description

Built AI-enabled internal tools for quality-management and operations workflows, including QMS document relationship planning, a secure Next.js/PostgreSQL onboarding tracker with SSO/auth middleware, and Docker devcontainers for reproducible, isolated AI-assisted development.

### Tech Stack

AI / Full-stack / Tech stack: Next.js, TypeScript / JavaScript, PostgreSQL, Drizzle ORM, SSO, authentication middleware, Docker, WSL2, Colima, Codex, Claude Code, LLM APIs, OpenAI, Anthropic Claude, cloud-service evaluation, API integration planning, webhook automation planning, internal knowledge-base documentation.

### Business / Problem Context

SmartSolve work centered on internal software, AI adoption, AI-assisted workflows, and operational tooling. Resume bullets should emphasize the onboarding tracker, secure access patterns, AI integration roadmap work, and AI-first development practices when they match the target role.

### Problem / Company Impact Context

- Supported early-stage AI and internal software planning where architecture, security, and developer workflow decisions were still being shaped.
- Worked under a phased AI integration roadmap for department-level AI usage, employee AI capstone planning, internal tool prototyping, technical documentation, stakeholder updates, and handoff planning.
- Supported AI tool usage audits by identifying gaps, redundancies, integration opportunities, and department-level workflow improvement candidates.
- Worked on QMS dependency-register planning to help connect related quality-management documents and make document relationships easier to understand.
- Built onboarding workflow software to centralize HR/new-hire process tracking and protect sensitive employee data.
- Improved reproducibility and onboarding for developers by creating Docker-based development environments across WSL2 and Colima.
- Used AI-assisted coding tools while keeping development workflows isolated around proprietary source code and company data.

### Work Performed

- Worked in an early planning/build phase across AI-oriented internal projects.
- Worked from a phased AI integration roadmap covering foundation/quick wins, role-specific AI training, prototype iteration, technical presentation, documentation, and handoff planning.
- Supported structured review of AI tool usage and department workflow opportunities, with emphasis on identifying problems, proposed AI solutions, expected outcomes, and measurable success criteria.
- Worked on a QMS dependency register intended to link multiple QMS documents and model what properly connected QMS documentation should look like.
- Architected a full-stack onboarding tracker for HR/new-hire workflows.
- Used Next.js for the application layer.
- Used PostgreSQL with Drizzle ORM for structured persistence.
- Implemented SSO and authentication middleware to protect sensitive employee and onboarding data.
- Built a cross-platform Docker devcontainer for WSL2 and Colima.
- Isolated AI-assisted development tooling to help protect proprietary data.
- Evaluated possible LLM/API, cloud-service, API-integration, webhook-automation, internal knowledge-base, and lightweight proprietary-tool directions for internal workflow automation.
- Used agentic CLI tools, including Codex and Claude Code, as daily development assistants for planning, implementation, review, and iteration.

### Positioning Angles

- AI-first software engineering
- AI adoption and internal workflow modernization
- LLM/API and cloud-service integration planning
- Secure internal tooling
- Full-stack product development
- Developer experience and environment isolation
- HR workflow automation

### Reusable Bullet Options

- Architected a full-stack Next.js onboarding tracker with PostgreSQL, Drizzle ORM, SSO, and auth middleware, replacing memory-based HR follow-up with secure new-hire handoff tracking.
- Deployed role-specific AI agents for employee workflows and converted tool audits into scoped projects, helping operations and executive leaders prioritize internal AI investments.
- Evaluated LLM/API and cloud-service integration paths for internal workflow automation, shaping lightweight proprietary tool concepts, API integrations, webhook automations, internal documentation, and applied business-problem training material.
- Built a cross-platform Docker devcontainer for WSL2 and Colima, isolating AI-assisted development workflows to safeguard proprietary source code and company data; participated in Scrum ceremonies and CI/CD pipeline maintenance.
- Applied AI-first engineering workflows with Codex and Claude Code to accelerate feature development, implementation planning, and code review.
- Modeled early architecture for AI-enabled internal systems, including a QMS dependency register designed to make quality-document relationships traceable.

### Source And Verification Notes

- User-provided SmartSolve offer/JD document visually inspected on August 7, 2026. The document lists official role title `AI & Computer Science Intern` (standardized across resume, profile, and application materials as `Artificial Intelligence Engineer Intern`), direct report to the CEO, Bowling Green, OH with remote flexibility as role requires, part-time 20-39 hours/week, and an internship description built around a four-phase AI integration roadmap.
- The SmartSolve document lists official internship dates as May 4, 2026 to August 7, 2026. Aryan separately stated the internship ended in July 2026, so public-facing master resume/CV materials currently keep the visible end date as `Jul. 2026` unless Aryan asks to use the offer-letter end date.
- Roadmap language should be used carefully: the document supports the planned scope and responsibilities, but completed-outcome claims should require Aryan confirmation or additional source evidence.

## Bowling Green State University

Role: Graduate Research Assistant I  
Location: Bowling Green, OH  
Dates: Aug. 2024 - May 2026

### Platform-Ready Description

Supported BGSU cybersecurity education and research by developing hands-on labs, technical training materials, and curriculum mappings across ethical hacking, OSINT, Nmap/NSE, Metasploit, OpenVAS/Greenbone, Wireshark, Burp Suite, OWASP ZAP, email forensics, cryptography, secure key management, NICE Framework/CAE-CD alignment, and CyberGuardian-based learning. Led 10 undergraduate students in organizing a middle-school CyberCamp, translating security concepts into accessible activities such as phishing demos, password-security exercises, cryptography labs, and cyber escape-room material.

### Handshake Description

Developed cybersecurity labs, training materials, and curriculum mappings across ethical hacking, OSINT, Wireshark, Burp Suite, OWASP ZAP, email forensics, cryptography, secure key management, NICE/CAE-CD, and CyberGuardian. Led 10 undergraduates in organizing a middle-school CyberCamp.

### Tech Stack

Cybersecurity education / Tech stack: NICE Framework, CAE-CD curriculum mapping, CyberGuardian, Kali Linux, ethical hacking, OSINT, reconnaissance, service enumeration, Nmap / Nmap Scripting Engine, Metasploit / msfconsole / msfvenom, OpenVAS / Greenbone, Wireshark / tcpdump, arpspoof / dsniff, Burp Suite, OWASP ZAP / OWASP Top 10, Shodan, theHarvester, Metagoofil, Wappalyzer, Netcat / Ncat, Masscan, Snort, John the Ripper, Hydra, Mimikatz, RainbowCrack, Cain, WCE, Immunity Debugger, Mona, Vulnserver, DVWA, Metasploitable2, PentesterLab, cryptography, public key infrastructure, secure key management, Azure Key Vault lab material, Shamir's Secret Sharing, PGP / GnuPG, SPF / DKIM / DMARC, email header analysis, password security, phishing awareness, email forensics, web application security, XSS / SQL injection lab concepts, packet capture analysis, exploit-development lab concepts, curriculum analysis, technical writing, presentation development.

### Business / Problem Context

Graduate research assistant work centered on cybersecurity education, cyber workforce/curriculum research, cyber range and training materials, instructional content development, and technical lab design. This work is not currently a default fit for the one-page technical resume, but it is useful for LinkedIn continuity, cover letters, and roles involving cybersecurity, secure software, education technology, developer advocacy, technical training, research, or curriculum engineering.

### Problem / Company Impact Context

- Built cybersecurity education material that translated advanced security topics into usable student-facing labs, presentations, workshops, and outreach activities.
- Supported cyber workforce/curriculum mapping through NICE Framework and CAE-CD material, helping connect cybersecurity roles, knowledge areas, and instructional requirements.
- Helped organize a middle-school CyberCamp by leading 10 undergraduate students and using CyberGuardian modules, cryptography activities, phishing demos, password-security exercises, and cyber escape-room materials.
- Covered the ethical-hacking lifecycle from reconnaissance through payload delivery in controlled instructional environments.
- Local work reviewed from `/Users/aryanmiriyala/Desktop/Work-RA` included Fall 2024, Spring 2025, Fall 2025, and Spring 2026 materials across CyberGuardian, cryptography, phishing/email security, escape rooms, password games, NICE/CAE-CD, ethical hacking, email forensics, secure key management, and tools/frameworks inventories.

### Work Performed

- Developed and refined cybersecurity education materials across cryptography, phishing awareness, password security, email authentication, email security, email forensics, anonymous communication, and ethical-hacking topics.
- Led a team of 10 undergraduate students to organize a CyberCamp for middle school students.
- Built or supported hands-on lab materials involving OSINT, port scanning, service enumeration, vulnerability scanning, packet analysis, credential attacks, web application security, exploit development, payload generation, and traffic interception in authorized training environments.
- Researched and organized cybersecurity tools and frameworks used in ethical-hacking instruction, including Kali Linux, Nmap/NSE, Metasploit, msfconsole, msfvenom, OpenVAS/Greenbone, Wireshark, tcpdump, arpspoof/dsniff, Burp Suite, OWASP ZAP, Shodan, John the Ripper, Hydra, Mimikatz, Immunity Debugger, Mona, DVWA, Metasploitable2, Vulnserver, and PentesterLab.
- Worked with NICE Framework and CAE-CD curriculum materials to support cybersecurity workforce, role, knowledge-unit, and curriculum analysis.
- Built or refined email security and forensics material covering phishing analysis, email headers, SPF/DKIM/DMARC, PGP/GnuPG, packet captures, and secure email communication.
- Supported cryptography and secure key-management content involving symmetric/asymmetric encryption, hashing, PKI, key storage, key recovery, key distribution, HSM concepts, Azure Key Vault lab material, and Shamir's Secret Sharing.
- Helped create presentation decks, lab guides, workshop material, student-facing activities, and instructor-facing notes for cybersecurity learning modules.
- Supported cybersecurity outreach/education assets such as escape-room activities, board-game concepts, password exercises, and phishing/security demos.

### Positioning Angles

- Cybersecurity education and research support
- Team leadership and student mentorship
- Middle-school CyberCamp organization
- Applied security labs and instructional design using real security tools and controlled training targets
- Cyber workforce/curriculum mapping
- Ethical-hacking workflow coverage from reconnaissance through payload delivery
- Email security, forensics, cryptography, and secure key-management education
- Technical communication
- Research assistantship with practical teaching/outreach artifacts

### Reusable Bullet Options

- Developed cybersecurity education materials and hands-on lab content across cryptography, secure key management, phishing, password security, email authentication, email forensics, ethical hacking, OSINT, vulnerability scanning, packet analysis, exploit-development concepts, and web application security.
- Led a team of 10 undergraduate students to organize a middle-school CyberCamp using CyberGuardian modules, cryptography activities, phishing demos, password-security exercises, and cyber escape-room materials.
- Organized NICE Framework and CAE-CD curriculum analysis across cybersecurity roles, knowledge areas, tools, and instructional requirements, translating them into student- and instructor-facing materials.
- Created and refined presentations, lab guides, workshop activities, and outreach exercises, including CyberGuardian modules, cyber escape-room activities, password games, email-security labs, cryptography modules, and ethical-hacking tool inventories.

## Bowling Green State University

Role: Teaching Assistant  
Location: Bowling Green, OH  
Dates: Aug. 2021 - May 2023

### Platform-Ready Description

Supported College Algebra instruction at the BGSU Math Emporium by helping students debug quantitative reasoning errors, work through algebra problems, and understand course concepts in a high-volume learning-support environment. The role strengthened technical communication, structured problem explanation, and student-facing support skills by translating abstract math concepts into step-by-step guidance.

### Handshake Description

Supported College Algebra instruction at the BGSU Math Emporium by helping students work through algebra problems, debug quantitative reasoning errors, and understand course concepts in a high-volume learning-support environment.

### Tech Stack

Teaching / Tech stack: College Algebra, quantitative reasoning, student support, teaching assistance, concept explanation, high-volume learning support.

### Business / Problem Context

Supported College Algebra at the Math Emporium.

### Problem / Company Impact Context

- Helped students work through algebra concepts in a high-volume learning-support environment.
- Strengthened student understanding by breaking down difficult quantitative concepts into clearer steps.
- Built communication, patience, and mentoring skills that transfer to technical collaboration and user support.

### Work Performed

- Helped students understand algebra concepts and complete course work.
- Answered questions in a high-volume learning-support environment.
- Worked directly with students to clarify difficult concepts.

### Positioning Angles

- Teaching and mentorship
- Communication
- Explaining technical or quantitative concepts
- Student-facing support

### Reusable Bullet Options

- Supported College Algebra students at the Math Emporium by answering questions, explaining difficult concepts, and helping students work through course material.

## Bowling Green State University

Role: Learning Assistant  
Location: Bowling Green, OH  
Dates: Aug. 2022 - Dec. 2022

### Platform-Ready Description

Led CS 2010: Programming Fundamentals labs by helping students understand core programming concepts, debug assignments, reason through lab exercises, and apply foundational problem-solving patterns. The role blended technical instruction with hands-on debugging support for early computer science learners building confidence with code.

### Handshake Description

Led CS 2010: Programming Fundamentals labs by helping students understand core programming concepts, debug assignments, reason through lab exercises, and apply foundational problem-solving patterns.

### Tech Stack

Computer science instruction / Tech stack: programming fundamentals, lab instruction, debugging support, introductory computer science, student mentorship, technical communication.

### Business / Problem Context

Supported CS 2010: Programming Fundamentals.

### Problem / Company Impact Context

- Helped early computer science students understand foundational programming concepts and lab assignments.
- Supported debugging and conceptual problem solving for students learning to code.
- Built experience explaining technical ideas clearly to beginners, a useful foundation for technical collaboration, documentation, and mentoring.

### Work Performed

- Led programming labs.
- Answered student questions and helped students debug conceptual and coding misunderstandings.
- Supported students learning foundational programming concepts.
- Helped students work through assignments, lab tasks, and core problem-solving patterns.

### Positioning Angles

- Technical teaching
- Developer communication
- Debugging support
- Mentoring early programmers

### Reusable Bullet Options

- Led labs and supported students in CS 2010: Programming Fundamentals, helping students understand foundational programming concepts, debug assignments, and build confidence with code.
- Answered student questions during labs and support sessions, translating technical concepts into practical explanations for early computer science learners.

## Bowling Green State University

Role: Student Worker, Registration and Records  
Location: Bowling Green, OH  
Dates: May 2021 - Apr. 2023

### Platform-Ready Description

Supported BGSU Registration and Records operations by handling student records, file workflows, administrative processes, and customer-service requests in a university office environment. The role required accurate record handling, confidentiality, responsive communication, and reliable execution of student-facing operational workflows.

### Handshake Description

Supported BGSU Registration and Records operations through student-record handling, file workflows, administrative support, confidential information handling, and customer-service requests in a university office environment.

### Tech Stack

Operations / Tech stack: student records, administrative workflows, file handling, customer service, university operations, confidential record handling.

### Business / Problem Context

Registration and Records work supported day-to-day university administrative operations involving student records, office workflows, file handling, and student-facing service.

### Problem / Company Impact Context

- Supported administrative workflows where accuracy, confidentiality, responsiveness, and attention to detail mattered.
- Helped maintain smooth student-facing office operations through file handling, record support, and customer-service workflows.
- Built operational reliability and communication skills through direct university office support.

### Work Performed

- Supported Registration and Records operations.
- Handled student records and administrative workflows.
- Provided customer-service support in a university office setting.

### Positioning Angles

- Operational reliability
- Detail-oriented administrative work
- Confidential record handling
- Customer-facing communication

### Reusable Bullet Options

- Supported Registration and Records operations through student-record handling, administrative support, and customer-service workflows.

## American Association of Insurance Services

Role: Data Engineering Intern  
Location: Lisle, IL  
Dates: May 2025 - Aug. 2025

### Platform-Ready Description

Built production AWS data engineering workflows for AAIS insurance data platforms, replacing manually executed SQL billing processes and legacy Pentaho ETL jobs with PySpark, AWS Glue Workflows, partitioned S3 pipelines, custom IAM access controls, reverse ETL, validation workflows, and Semarchy MDM migration architecture. The work processed 20+ TB of golden-table insurance data from MySQL, Oracle, Impala, PostgreSQL, and related enterprise sources, calculated recurring charges for 700+ member companies, and supported the profiling, mapping, and standardization of 160+ source tables into 25 MDM domains. The role combined end-to-end data engineering responsibilities: understanding source-system structure, designing the migration flow, building production Glue jobs, validating outputs, and helping make insurance data more reliable, governed, and self-service-ready.

### Handshake Description

Built production AWS data workflows for insurance platforms using Python, PySpark, SQL, AWS Glue, S3, IAM, and Semarchy MDM. Automated manual billing over 20+ TB of data for 700+ member companies and supported profiling, mapping, validation, and standardization across enterprise sources.

### Tech Stack

Data engineering / Tech stack: Python, Pandas, SQL, PySpark, AWS Glue, AWS Glue Workflows, AWS S3, AWS IAM, MySQL, Impala, Oracle, PostgreSQL, JDBC, Semarchy MDM / Semarchy xDM, Pentaho, golden tables, insurance data platforms, billing workflows, master data management, reverse ETL, data validation.

### Business / Problem Context

AAIS is a P&C insurance advisory and statistical-agent organization that supports member carriers, regulator-facing statistical reporting, insurance data standards, and data/technology products. This internship focused on production data engineering for billing automation, master data management, cloud ETL, access-controlled data movement, and standardization of insurance datasets used across internal and member-facing workflows.

### Problem / Company Impact Context

- Replaced a fully manual SQL billing workflow with a production PySpark and AWS Glue Workflow, removing manual execution from recurring charge calculations.
- Processed 20+ TB of production golden-table data from sources including MySQL, Impala, Oracle, PostgreSQL, and related enterprise systems.
- Supported billing calculations for 700+ member companies.
- Contributed to MDM migration work intended to reduce legacy Pentaho job sprawl, standardize data domains, and move toward more maintainable cloud-native ETL patterns.
- Built custom IAM roles so users and workflows had appropriate AWS data access instead of broad or mismatched permissions.
- Helped move insurance data workflows toward more standardized, validated, and self-service-ready data availability.

### Work Performed

- Automated a fully manual SQL billing process with a production PySpark script and AWS Glue Workflow.
- Developed PySpark processing over production golden tables from multiple enterprise sources, including MySQL, Impala, Oracle, PostgreSQL, and related systems.
- Orchestrated recurring AWS Glue Workflows.
- Processed 20+ TB of production insurance data.
- Calculated charges for 700+ member companies.
- Profiled 160+ MySQL/Oracle/Impala tables using Python, Pandas, SQL, and JDBC.
- Mapped data similarities across systems.
- Designed architecture and data flow for migration into 25 MDM domains.
- Defined a unified taxonomy of 25 MDM domains.
- Replaced 160+ Pentaho jobs with AWS Glue-based ETL.
- Loaded partitioned data into S3 for Semarchy MDM.
- Delivered reverse-ETL/data validation workflows.
- Supported a self-service application with automated data availability.
- Maintained 24-hour data latency across new MDM domains.
- Built custom AWS IAM roles for controlled data access.

### Positioning Angles

- Data engineering at scale
- AWS ETL orchestration
- Legacy job replacement
- MDM migration
- Billing automation
- Data validation and reverse ETL
- Large data processing

### Reusable Bullet Options

- Automated a weekly DBeaver SQL billing process with Python, PySpark, and AWS Glue, processing 20+ TB of production insurance data for Data Solutions, internal teams, and CFO reporting.
- Architected a 160+ table MDM migration by profiling MySQL/Oracle/Impala sources through JDBC with Python, Pandas, and SQL, standardizing inconsistent legacy insurance data into 25 domains using domain-driven design principles.
- Modernized 160+ legacy Pentaho jobs into AWS Glue ETL workflows and partitioned S3 pipelines for Semarchy MDM, improving maintainability for governed MDM ingestion.
- Delivered reverse-ETL and data-validation workflows with custom AWS IAM roles, giving users controlled self-service access to validated insurance data while maintaining 24-hour latency.

## American Association of Insurance Services

Role: Software Engineering Intern  
Location: Lisle, IL  
Dates: May 2023 - May 2024

### Platform-Ready Description

Built production insurance data-standardization and application modernization workflows at AAIS, including openIDL/openIDS-aligned data-model generation, Python/JSON-driven SQL schema creation, React/Node.js access-control modernization, and AWS Lambda automation for PII-tokenized data movement into S3. The work generated 1,000+ production SQL tables across MySQL, Oracle, PostgreSQL, and 10+ insurance lines, used Pandas, multiprocessing, fuzzy matching, and hashing for large CSV processing, and introduced RBAC/JWT patterns to replace broad employee-wide access with role-specific controls for about 110 users. The role connected backend automation, data modeling, full-stack access control, and AWS event-driven processing to help standardize insurance data structures and support more controlled internal data access.

### Handshake Description

Built insurance data-standardization and modernization workflows using Python, JSON, SQL, MySQL, Oracle/PostgreSQL, React, Node.js, JWT/RBAC, AWS Lambda, and S3. Generated 1,000+ production SQL tables, processed large CSV datasets, and helped replace broad internal access with role-specific controls.

### Tech Stack

Software engineering / Data standardization / Tech stack: Python, JSON, Pandas, multiprocessing, SQL, MySQL, Oracle, PostgreSQL, Java, Spring Boot / Springboot, Maven, OpenShift / Open Shift, microservice APIs, React, Node.js, JWT, RBAC, AWS Lambda, AWS S3, boto3, hashlib, insurance taxonomies, openIDL / openIDS context, large CSV processing, fuzzy matching, PII tokenization.

### Business / Problem Context

This role combined software engineering, insurance data modeling, full-stack modernization, access control, and AWS automation. The strongest resume story is helping standardize insurance data and modernize internal access patterns: generating production SQL structures from insurance taxonomies, reducing open internal data access through RBAC/JWT proposals, and automating database validation and PII-safe data movement.

### Problem / Company Impact Context

- Supported a larger insurance data-standardization effort connected to openIDL/openIDS-style goals: common insurance data models, reduced duplication, and easier sharing/reporting across industry workflows.
- Generated 1,000+ production SQL tables from Python/JSON-driven taxonomy parsing instead of hand-building schema structures.
- Helped move internal application access away from broad employee-wide visibility toward role-specific access control for about 110 employees.
- Temporarily served as Product Owner for an AAIS internal application, translating business requirements into implementation tasks and coordinating delivery priorities.
- Automated database validation triggered by new rows in MySQL, Oracle, and PostgreSQL tables, tokenizing PII and moving structured output into S3 for downstream standardization flows.

### Work Performed

- Engineered foundational data-modeling work for openIDL/openIDS-aligned insurance standardization.
- Parsed insurance taxonomies with Python and JSON-based generation logic.
- Generated and implemented 1,000+ production SQL tables.
- Supported MySQL, Oracle, and PostgreSQL databases.
- Worked across 10+ insurance lines.
- Built Python data-processing workflows using Pandas and multiprocessing.
- Cleaned and processed large CSV datasets.
- Implemented fuzzy de-duplication and data hashing.
- Contributed to React/Node.js modernization work.
- Temporarily served as Product Owner for an AAIS internal application and translated business requirements into implementation tasks.
- Implemented RBAC and JWT authentication proposal/workflows to replace broad employee-wide data access.
- Built secure, role-specific internal landing page functionality for about 110 internal users.
- Automated database validation triggered by new MySQL, Oracle, and PostgreSQL rows with AWS Lambda.
- Used hashlib and boto3 to tokenize PII and ingest structured JSON into S3 for downstream standardization workflows.

### Positioning Angles

- Full-stack modernization
- Temporary Product Owner ownership for an internal application
- Data modeling and SQL generation
- Secure access control
- PII handling
- AWS automation
- Insurance data platforms

### Reusable Bullet Options

- Engineered Python/JSON automation that generated 1,000+ production SQL tables and consolidated views across 10+ insurance lines, accelerating openIDL/openIDS-aligned data standardization and reporting.
- Automated CSV cleaning and deduplication with Python, Pandas, multiprocessing, fuzzy matching, and hashing, improving source quality for insurance standardization pipelines.
- Implemented RBAC and JWT patterns in a full-stack React/Node.js modernization, replacing broad employee-wide visibility with role-specific controls for about 110 users.
- Temporarily served as Product Owner for an AAIS internal application, translating business requirements into implementation tasks while coordinating delivery priorities.
- Automated AWS Lambda validation that tokenized PII with hashlib/boto3 and delivered structured JSON to S3, supporting safer downstream insurance data processing for SDMA workflows.

### Source And Verification Notes

- Confirmed by Aryan on August 23, 2026: AAIS experience included Spring Boot/Springboot, Maven, OpenShift/Open Shift, microservice APIs, and temporary Product Owner responsibility for an AAIS internal application. Use Product Owner wording specifically in the AAIS internal-application context and avoid implying a permanent Product Owner title.

## Alliance for Paired Kidney Donation

Role: Software Engineering Intern  
Location: Toledo, OH  
Dates: May 2022 - Aug. 2022

### Platform-Ready Description

Improved an AWS-hosted Lucee/CFML healthcare workflow platform for kidney-paired donation operations by strengthening form security, auditability, data-entry reliability, and internal clinical workflow usability. Work included global anti-CSRF form protection, IP-aware audit logging, protected access-denied/404 routing, HTML5 date/time picker modernization, JavaScript fallbacks, themed CSS, cfform/cfinput compatibility updates, reusable modal/tab UI patterns, clinical logistics defaults, Matchgrid import ordering, MFI file-location fixes, and duplicate-antigen MFI crash handling. The role focused on modernizing a legacy healthcare workflow application while preserving graceful degradation and improving reliability for internal transplant operations.

### Handshake Description

Improved an AWS-hosted Lucee/ColdFusion healthcare workflow platform by adding anti-CSRF protection, audit logging, access-denied/404 flows, HTML5 date/time picker updates, JavaScript/CSS fixes, logistics defaults, import ordering, and reliability fixes for internal clinical operations.

### Tech Stack

Healthcare software / Tech stack: Lucee, CFML / ColdFusion, AWS, HTML5, JavaScript, CSS, Bootstrap, cfform / cfinput migration considerations, anti-CSRF tokens, audit logging, access control workflows, HTML5 date/time pickers, JavaScript fallbacks, clinical logistics workflows, data import reliability, icons and tooltips, modal/tab UI patterns, MFI recipient workflows, Matchgrid import workflows.

### Business / Problem Context

Alliance for Paired Kidney Donation works in kidney-paired donation, where internal software supports sensitive donor/recipient workflows, transplant logistics, matching operations, audit trails, and administrative coordination. The relevant platform context is a healthcare/clinical workflow system where reliability, secure data entry, access control, and operational usability matter because small workflow failures can disrupt transplant-support processes.

### Problem / Company Impact Context

- Strengthened security and auditability by applying anti-CSRF protections globally across forms and adding user IP addresses to audit-trail logging.
- Improved protected workflow handling by sending unauthorized users to an access-denied page instead of ending sessions and by adding a clearer 404 page for nonexistent templates.
- Modernized legacy Lucee/CFML form workflows with HTML5-compliant date/time inputs, themed picker styling, JavaScript fallbacks, and cfform script updates to reduce entry friction and support graceful degradation.
- Improved internal transplant/logistics operations by adding center-level preferred blood-tube defaults and surfacing those values on logistics-sheet workflows.
- Improved import/data reliability by fixing Matchgrid ordering, MFI upload file paths, and RecipientMFIEdit crashes caused by duplicate MFI values for the same antigen.

### Work Performed

- Worked on an AWS-hosted Lucee/CFML/ColdFusion healthcare workflow platform.
- Added anti-CSRF tokens to all forms globally.
- Added user IP address capture to audit-trail logging.
- Added access-denied behavior so unauthorized access routed to a protected page instead of ending user sessions.
- Added cleaner 404 page behavior for nonexistent templates.
- Changed time, date, and date-time fields to HTML5 pickers.
- Ensured date picker inputs used standard HTML input tags instead of cfinput.
- Added JavaScript form script source to cfform in PopInForm_Offer.
- Added themed CSS so date pickers matched the rest of the application.
- Reviewed ColdFusion code for HTML5 compatibility.
- Preserved manual input and graceful degradation for date/time fields.
- Replaced text in MatchRunView tables with appropriate icons and mouseovers/tooltips.
- Tabified registrations, offers, and combinations.
- Migrated modals into separate files.
- Ensured Matchgrid import files were listed by upload date, latest first.
- Fixed MFIUpload_Recipient_Processing.cfm file location.
- Fixed RecipientMFIEdit crashes when a recipient had multiple MFI values in one dataset for the same antigen.
- Added preferred blood-tube defaults for centers.
- Added logistics sheet display/population for preferred blood tubes.

### Positioning Angles

- Healthcare software engineering
- Security and compliance-aware engineering
- Legacy platform modernization
- Frontend usability improvements
- Clinical workflow support
- Data quality and operational reliability

### Reusable Bullet Options

- Secured AWS-hosted Lucee/CFML match-run workflows with anti-CSRF, IP-aware audit logging, protected routing, crash fixes, and blood-tube defaults for safer transplant operations.
- Modernized legacy ColdFusion forms with HTML5 date/time pickers, themed CSS, JavaScript fallbacks, and cfform script updates to improve standards compliance, data entry, and graceful degradation.
- Improved internal transplant logistics by adding center-level blood-tube defaults, logistics-sheet population, Matchgrid upload ordering, MFI file-location fixes, and duplicate-antigen MFI crash handling.
- Refactored MatchRun, registration, offer, and combination interfaces into reusable modal/tab components with icons and tooltips to improve usability and maintainability for internal operations.

## Education

Bowling Green State University  
Master of Science in Computer Science  
GPA: 4.00/4.00  
Dates: Aug. 2024 - Aug. 2026

Bowling Green State University  
Bachelor of Science in Computer Science  
GPA: 4.00/4.00  
Dates: Jan. 2021 - Apr. 2024
