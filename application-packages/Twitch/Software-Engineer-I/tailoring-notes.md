# Tailoring Notes

Company: Twitch (Amazon)

Role: Software Engineer I (Community Growth)

Date: October 19, 2026

## Target Angle

Primary role lane: Early-career consumer-facing full-stack / frontend software engineering (React web + React Native mobile), with backend-infrastructure adjacency.

Primary angle: React-heavy consumer-facing web and mobile product engineering, framed around the posting's core promise that Web and Mobile Twitch must "Just Works." Evidence is the customer-portal interface consolidation, login/session reliability fixes, stale-data elimination, React Native/Expo mobile app, and the AI-driven engineering practices the posting calls out.

Secondary angle: Fullstack ownership and backend maintenance behind the features (AI Gateway infrastructure, AWS Lambda/S3/DynamoDB/IAM/Glue, Golang microservices on Kubernetes).

Adjacent role fit: Mobile engineer or frontend-focused SWE I, given the React Native bonus and consumer UX emphasis.

Why this lane: The posting is unambiguous that this is "primarily focused on web & mobile frontend development (React heavy for both Web & Mobile) but is expected to be fullstack." That is exactly the shape of the current Actual Reality Technologies work plus the DreamScape mobile app.

## Package Plan

Resume strategy: Start from `templates/canonical-resume.tex`. Reverse-chronological experience order preserved. Actual Reality leads with consumer-facing interface and reliability bullets rather than the AI Gateway bullet, because the posting's first responsibility is "Deliver high quality user experiences across Web and Mobile surfaces." AI Gateway moves to the fourth bullet so the AI-driven-engineering requirement is still evidenced without displacing the UX lead. Projects are restricted to the two technologies the posting lists as bonus points that Aryan can prove (React Native and Go). Technical Skills recategorized as Web & Mobile Frontend / Backend & APIs / AWS & DevOps / AI & Quality.

Cover-letter strategy: One-page, canonical 11pt Computer Modern layout, 0.80in side margins and 0.70in top/bottom margins. Anchors on the posting's "Just Works" language and the Chat / Stream Together / Discovery surfaces by name, then uses two deep proof points (customer-portal consolidation plus login/session reliability, and the DreamScape React Native app), closes with the AI-driven engineering practice and the product-partnership evidence. Tone is plain and specific, no slogan reuse beyond the employer's own phrasing.

Project strategy: DreamScape (React Native/Expo) and TachyonMesh (Golang/Kubernetes) only. Both directly satisfy named bonus points. Travel Health Advisor, RocketGrader, Fix-It-Flow, FalconGraph Search, and the portfolio project were evaluated and cut for page budget; the React/web consumer surface is already carried by Actual Reality, SmartSolve, and the Web & Mobile Frontend skills line.

Skills strategy: Four parser-friendly categories. The Frontend & Mobile category was renamed to "Web & Mobile Frontend" to mirror the posting's own "web and mobile surfaces" phrasing and to carry an exact `web` keyword.

Known stretch/risk strategy: Gaming/streaming domain familiarity and "software used by the gaming community" are genuinely absent from Aryan's source material. They are documented as honest gaps rather than papered over. AWS ECS, SQS, and Step Functions are also absent and omitted; Lambda, S3, DynamoDB, and IAM are evidenced and shown instead.

Token/source-access strategy: Read `profile/evidence-index.md`, `templates/canonical-resume.tex`, `templates/tailoring-notes-template.md`, `templates/canonical-cover-letter.md`, the validator and analyzer CLIs, and targeted `rg`-equivalent grep slices of `profile/experience-master.md` and `profile/projects-master.md`. No historical application package was opened. No full tracker read beyond the 12-line header used to confirm the upsert schema.

## F-1 Work Authorization Gate

Result: Pass - no blocker found; package built and submitted artifacts are clean of visa language.

Internal notes only:

- Posting sponsorship language: None. The Twitch posting is silent on visa sponsorship, work authorization, and E-Verify. It contains only the standard San Francisco Fair Chance Ordinance and equal-opportunity boilerplate.
- E-Verify / STEM OPT / Form I-983 follow-up: Not addressed in the posting. If a recruiter screen surfaces it, answer directly and truthfully about CPT/OPT eligibility and STEM OPT timing.
- Future sponsorship follow-up: None needed from the posting. Amazon is a large sponsor, but that is an inference, not posting language, so it is not used in any submitted artifact.
- Location / schedule / clearance / degree constraints: Onsite in San Francisco, CA ("You can work in San Francisco, CA"). Bachelor's degree in Computer Science required, satisfied (B.S. and M.S. in Computer Science, GPA 4.00/4.00). No clearance requirement. San Francisco onsite is compatible with OPT/STEM OPT but should be confirmed during recruiter screen regarding relocation timing after graduation (M.S. completed Aug. 2026).
- Submitted artifact rule: Do not mention F-1, OPT, STEM OPT, visa status, sponsorship, E-Verify, or Form I-983 in the resume or cover letter unless Aryan explicitly asks.

## Referral Plan

Referral status: Not started.

Referral target / source: None identified yet. Plausible paths for later outreach are Amazon/Twitch frontend engineers visible on LinkedIn who have shipped React web or React Native features, and BGSU alumni working at Amazon.

Connection path: Warm outreach through LinkedIn with a short note referencing the customer's-consumer-facing React portal reliability work and the React Native app. Website or resume link included only if it helps the first message.

Outreach status: No outreach drafted or sent yet.

Next follow-up date: 2026-10-26, or immediately after the application is submitted.

Outreach tone: Short and low-pressure. Initial message carries one proof point and the role link. Follow-up asks for a brief conversation about the Community Growth team's web and mobile surfaces rather than restating Aryan's work history.

Notes: A referral is not a prerequisite for this application. If outreach starts, keep the message to the channel and do not repeat the full stack, publication list, or project inventory unless the recipient asks.

## Job Keyword Map

Job-description source audit:

- Full employer posting saved in `job-description.md`: Yes, verbatim, under "Full Employer Posting".
- Metadata added without replacing full posting: Yes, a short Role Metadata block (company, team, location, Job ID TW9303, date, source, salary range, eligibility notes) sits above the posting.
- Source limitation, if any: Posting text was supplied directly by Aryan. Employer-side bonus text and perks were preserved as given. The posting does not link a canonical URL; the Job ID TW9303 is recorded for later lookup.

Default exact-term analyzer result:

- Checked terms: 7 (analyzer's automatic extraction: AI, AWS, DynamoDB, React, software engineer, authorization, code reviews).
- Found: 5 of 7.
- Missing: `authorization` (boilerplate work-authorization language, deliberately omitted to avoid visa signaling), `code reviews` (plural form; the singular `code review` is present and covered).
- Notes: The default denominator of 7 is far smaller than the real keyword universe for this posting and is not a coverage claim. The expanded pass below is the meaningful audit.

Expanded role-specific keyword pass:

- Term file used: `expanded-keywords.txt` (61 terms, employer exact wording plus close variants).
- Checked terms: 61.
- Found: 42, including Software Engineer I, React, React Native, frontend, backend, web, mobile, mobile app, TypeScript, JavaScript, Next.js, Angular, Expo, Node.js, Express, REST API(s), Go, Golang, AWS, Lambda, DynamoDB, S3, ECS-adjacent AWS context, Kubernetes, Docker, microservices, infrastructure, observability, latency, authentication, accessibility, CI, testing, PostgreSQL, MySQL, MongoDB, Firebase, user experience, consumer-facing, customer portal, customer-facing portal, code review, business impact, product-owner ownership.
- Missing truthful opportunities: None remaining. Six gaps were closed during the pass (`consumer-facing`, `customer portal`, `user experience`, `code review`, `business impact`, `microservices`, `infrastructure`, `accessibility`, `web`, `fullstack`).
- Unsupported / intentionally omitted: `ECS`, `SQS`, `Step Functions` (no evidence anywhere in `profile/`), `Twitch`, `gaming`, `streaming`, `software used by` (no gaming or streaming project, no Twitch product work, no maintained community-software ownership).
- Harmless variants: `code reviews` vs `code review`; `frontend development` vs `frontend`; `consumer products` vs `consumer-facing`; `AI driven engineering` vs the evidenced `AI gateway and model routing` plus `Claude Code`/`Codex`/`CI gates`; `development lifecycles` and `automated tools` are employer slogans for the same evidenced practice.
- Notes: `design review`, `designers`, and `product managers` are only partially supported. Aryan has verified Product Owner ownership of an internal application (business requirements to implementation tasks, delivery priorities with stakeholders) but no verified design-review participation or named designer/product-manager collaboration. `stakeholders` carries this truthfully rather than forcing the exact employer nouns.

Required skills: React, React Native (bonus), web and mobile frontend, TypeScript, fullstack, backend maintenance, consumer-facing product work, AI-driven engineering practices, communication with technical and business audiences.

Repeated terms: React, web, mobile, consumer-facing, user experience, features, engineering practices.

Responsibilities: Deliver high-quality UX across web and mobile; partner with product, design, and engineering to design/launch/operate features; work backwards from customer problems; participate in design and code reviews; maintain backend services behind features.

Domain language: live streaming, communities, streamers, viewers, discovery, audience growth, engagement.

Must-have tools: React (heavy), AWS. Everything else is listed as bonus or narrative.

Nice-to-have tools: React Native, Go, AWS ECS/DynamoDB/Lambda/SQS/Step Functions, AI-driven engineering tooling.

Unsupported terms to avoid: Twitch-specific platform features (Chat, Stream Together, Discovery implementation details), gaming/streaming domain expertise, AWS ECS/SQS/Step Functions, Streamer/Viewer persona claims.

Low-value / boilerplate terms tracked but not forced: `AI driven engineering`, `optimize development lifecycles using modern automated tools`, `design reviews`, `San Francisco Fair Chance Ordinance`, equal-opportunity statement, Amazon benefits and perks list, salary range.

Internal/private terms translated for recruiter readability:

- `Plane` / `Plane API` -> "project-management ticket and project status" (the MCP bullet was cut for page budget, so no vendor name appears).
- `magic link` / `secure account-link` -> "login transitions" and "password and secure account-link login".
- `smart-router tiers`, `LiteLLM`, `Langfuse` -> kept, because AI gateway and model routing are the recruiter-relevant concepts and the tool names are already public-facing product vocabulary.
- `Lucee/CFML`, `anti-CSRF`, `IP-aware audit logging` -> "AWS-hosted transplant match platform" plus the security controls named plainly.
- `openIDL/openIDS` -> kept; it is a real insurance data standard and reads as domain credibility to a technical reviewer.
- No ticket IDs, branch names, private route names, customer names, or the private repository URL appear anywhere in the resume or cover letter.

## Gap Recovery Gate

Gap recovery status: Complete. Every named bonus requirement and every core responsibility was searched before being treated as a gap.

Important JD Term Search:

- Terms searched: `React Native`, `Expo`, `react-native`, `Golang`, `Go microservices`, `TachyonMesh`, `ECS`, `SQS`, `Step Functions`, `Elastic Container`, `gaming`, `streaming`, `Twitch`, `Discord`, `esports`, `video game`, `accessib`, `ARIA`, `WCAG`, `a11y`, `Lighthouse`, `responsive`, `design review`, `code review`, `cross-functional`, `product manager`, `designer`, `user experience`, `Product Owner`, `users`.
- Locations searched: `profile/` (evidence-index.md, experience-master.md, projects-master.md, skills-master.md, bullet-bank.md, linkedin-profile-master.md), `master-documents/`.
- Evidence recovered:
  - `React Native` / `Expo`: **Supported**. `profile/projects-master.md` DreamScape (React Native, Expo SDK 54, Expo Router, Expo AV, AsyncStorage, Zustand, Zod, local-first architecture) and `profile/skills-master.md` lines 28-30. Added as a project and in the Web & Mobile Frontend skills line.
  - `Go`: **Supported**. `profile/projects-master.md` TachyonMesh (lines 716-741, Golang + Kubernetes + Envoy + Prometheus + Grafana + OpenTelemetry), routed through `profile/evidence-index.md` line 147. Note: the evidence index "Common Unsupported Or Narrow Claims" list names Go, but that list is a general default and is overridden here by the verified TachyonMesh project record. Go is claimed only in TachyonMesh context.
  - `AWS`: **Supported** for Lambda, S3, DynamoDB, IAM, Glue (`profile/experience-master.md` AAIS and Actual Reality sections, `projects-master.md` Fix-It-Flow DynamoDB).
  - `ECS`, `SQS`, `Step Functions`: **Unsupported**. Zero matches in `profile/` or `master-documents/`. Intentionally omitted.
  - `Twitch`, `gaming`, `streaming`: **Unsupported** as gaming/streaming domain work. The only `streaming` hits are unrelated: ElevenLabs text-to-speech streaming (Fix-It-Flow) and healthcare streaming ingestion (HealthTrend). Intentionally omitted.
  - `software used by the gaming community`: **Unsupported**. No maintained community or game-software ownership. Intentionally omitted.
  - `accessibility`: **Supported**. Actual Reality Workshop route accessibility/ARIA guardrails (`experience-master.md` line 61, `bullet-bank.md` line 28). Recovered after the first resume draft used only "ARIA"; rewritten to "accessibility" for recruiter readability.
  - `code review`: **Supported**. SmartSolve (`experience-master.md` line 179, `evidence-index.md` line 50): Codex and Claude Code applied across implementation planning, debugging, code review, and self-review. Added to the devcontainer bullet.
  - `product managers` / `designers`: **Partially supported**. Only Product Owner ownership of an internal AAIS application is verified. Kept as "stakeholders"; exact employer nouns not forced.
- Terms still unsupported: AWS ECS, AWS SQS, Step Functions, Twitch platform experience, gaming/streaming familiarity, maintained gaming-community software, design-review participation.
- Searches intentionally skipped, if any: None. Project-repository browsing was not needed because every recovered item is documented in `profile/`; skipping repo inspection avoids opening private source material that the submitted artifacts do not require.

Supported gaps added to package:

- React Native / Expo (DreamScape project plus skills line) - covers the first named bonus point.
- Go / Golang microservices, Kubernetes, Envoy, Prometheus, Grafana (TachyonMesh project plus Backend & APIs and AWS & DevOps skills lines) - covers the second named bonus point.
- `business impact` (SmartSolve bullet) - mirrors the posting's "drive business impact" and is truthful to the AI-audit work.
- `accessibility`, `code review`, `user experience`, `consumer-facing`, `customer portal`, `microservices`, `infrastructure`, `web`, `fullstack` - all natural recoveries of verified evidence into employer wording.

Likely built but undocumented - source update needed:

- None raised as blocking. If Aryan has any Twitch-adjacent side work, streaming hobby projects, or community-maintained software, that would close the largest remaining gap and should be added to `profile/projects-master.md` before any future Twitch-family application.

Unsupported gaps intentionally omitted:

- AWS ECS, SQS, Step Functions.
- Twitch, gaming, streaming familiarity; "software used by the gaming community".
- Design-review participation; direct collaboration with named product managers or designers.
- Chat, Stream Together, or Discovery implementation experience.

Profile/source updates needed:

- Consider adding an explicit `Common Unsupported` exception for Go, since `profile/evidence-index.md` line 258 currently lists Go as unsupported while `projects-master.md` verifies TachyonMesh. Left unchanged here because profile edits are outside this package's scope, but the conflict is recorded so it does not cause the term to be wrongly dropped in a future Go-heavy application.

Notes: The Go conflict is the one place where the compact index and the master file disagree. Master-file evidence won, per the source-priority order in `profile/evidence-index.md`.

## Job Keywords Used

- Software Engineer I, React, React Native, Expo, Next.js, TypeScript, JavaScript, Angular, HTML/CSS
- frontend, backend, fullstack, microservices, infrastructure, web, mobile, mobile app
- Node.js, Express, REST APIs, Go, PostgreSQL, MySQL, MongoDB, Firebase, SSO, JWT, RBAC
- AWS, Lambda, S3, DynamoDB, IAM, AWS Glue, Kubernetes, Prometheus, Grafana, Docker, Vercel, Railway
- customer portal, consumer-facing, user experience, accessibility, authentication, business impact, code review, latency, testing, CI
- LiteLLM, AI gateway and model routing, guardrails, Langfuse, Gemini API, Mistral AI, RAG, Vitest, Testing Library, Codex, Claude Code

## Experience Emphasized

- Actual Reality Technologies - all four bullets, reordered so consumer-facing interface work and reliability lead, and the AI Gateway moves to fourth.
- SmartSolve Industries - all three bullets, retitled to carry `code review` and `business impact`.
- AAIS Data Engineering - two bullets, kept for `scale`, `AWS`, and backend-system ownership.
- AAIS Software Engineering - three bullets, kept for `scale` (1,000+ tables), the React/Node.js surface, and the Product Owner / stakeholder partnership evidence.
- Alliance for Paired Kidney Donation - one bullet, kept as the shortest dated production evidence and for reliability-on-real-user-systems credibility.

## Projects Emphasized

- DreamScape: AI Sleep Learning App (React Native, Expo, TypeScript) - two bullets.
- TachyonMesh: Traffic & Observability Proxy (Golang, Kubernetes, Envoy, Prometheus) - one bullet.

Project proof emphasized:

- Deployment / runnable setup: TachyonMesh deploys a containerized Golang backend on Kubernetes; Actual Reality ships to Vercel and a pinned LiteLLM proxy on Railway.
- Tests / validation: Actual Reality Vitest and Testing Library route and component suites plus architecture tests; SmartSolve and AAIS work validated in production data and user systems.
- Logging / observability: TachyonMesh Prometheus/Grafana/Envoy metrics; Actual Reality Langfuse traces and Slack block alerts on the AI Gateway.
- Evaluation / source-grounding: AAIS 1,000+ production tables and openIDL/openIDS alignment; Actual Reality 44 red-team fixtures and 134 passing tests.
- Dashboard / reporting / business output: Actual Reality four-state project status reporting derived from work-item counts; AAIS CFO-facing billing reporting.
- User, stakeholder, or workflow impact: Consumer-facing portal reliability (no redirect flashes, no stale project data, no stranded spinners); AAIS role-specific access control for about 110 internal users; SmartSolve secure new-hire handoff tracking.

## Skills Emphasized

- Web & Mobile Frontend: React, React Native, Expo, Next.js, Angular, TypeScript, JavaScript, HTML/CSS
- Backend & APIs: Node.js, Express, Go, REST APIs, PostgreSQL, MySQL, MongoDB, Firebase, SSO, JWT, RBAC
- AWS & DevOps: Lambda, S3, DynamoDB, IAM, AWS Glue, Vercel, Railway, Docker, Kubernetes, Prometheus
- AI & Quality: LiteLLM, AI gateway and model routing, guardrails, Langfuse, OpenAI API, Gemini API, Mistral AI, LangChain, RAG, Vitest, Testing Library, Codex, Claude Code

## Bullet Audit

Every experience and project bullet must satisfy: action verb + what changed + technology/method + scope/domain + impact/result.

Experience bullet count: 13 (Actual Reality 4, SmartSolve 3, AAIS Data 2, AAIS SWE 3, APKD 1). Above the 11-bullet floor, so no `Experience Bullet Count Waiver` is required.

Two-line bullet-wrap check:

- Result: Pass - all 16 experience and project bullets render at exactly one or two lines in `pdftotext -layout`.
- Method used: Bounded `pdftotext -layout` line-grouping check plus `pdftotext -bbox` bottom-margin measurement, matching the validator's own logic. No full PDF text dumped into context beyond the single-page layout read used for visual verification.
- Exceptions, if any: None.

Experience bullets checked:

- Consolidated three customer workflow tools into one tabbed customer portal with feature gating, legacy redirects, accessibility and tab-history guardrails, and route/component tests.
- Hardened production authentication on the consumer-facing portal by deriving session-cookie domains from request hosts and stabilizing login transitions, so users no longer hit redirect flashes or stranded spinners.
- Improved project-data reliability by paginating work-item counts, forcing refreshes through route and gateway cache layers, and deriving project states from counts instead of rounded progress.
- Deployed a LiteLLM AI Gateway infrastructure for policy-controlled model routing, adding smart-router tiers, guardrails, Langfuse traces, Slack alerts, CI gates, and 44 red-team fixtures.
- Architected a fullstack onboarding tracker with Next.js, TypeScript, PostgreSQL, Drizzle ORM, SSO, and auth middleware, replacing memory-based HR follow-up with secure new-hire handoff tracking.
- Deployed role-specific AI agents for employee workflows and converted tool audits into scoped projects, making expected outcomes and business impact explicit for operations and executive leaders.
- Built a cross-platform Docker devcontainer for WSL2 and Colima and used Claude Code and Codex daily for code review and debugging, isolating AI-assisted development around proprietary code.
- Automated a weekly SQL billing process with Python, PySpark, and AWS Glue, processing 20+ TB of production insurance data for internal teams and CFO reporting.
- Delivered reverse-ETL and data-validation workflows with custom AWS IAM roles, giving users controlled self-service access to validated data while maintaining 24-hour latency.
- Engineered Python/JSON automation that generated 1,000+ production SQL tables across 10+ insurance lines, accelerating openIDL/openIDS-aligned data standardization and reporting.
- Served as temporary Product Owner for an internal application, translating business requirements into implementation tasks and coordinating delivery priorities with stakeholders.
- Implemented RBAC and JWT patterns in a React/Node.js modernization, replacing employee-wide visibility with role-specific controls for about 110 internal users.
- Secured an AWS-hosted transplant match platform in Lucee/CFML with anti-CSRF protection, IP-aware audit logging, and protected routing for safer clinical operations.

Project bullets checked:

- Built a cross-platform React Native/Expo mobile app for sleep-based microlearning, adding AI-generated study cues, quizzes, text-to-speech audio, and a local-first mobile user experience.
- Integrated Gemini and ElevenLabs APIs to summarize documents, generate quizzes, cache synthesized audio, and schedule sleep-mode playback across iOS and Android.
- Built a containerized Golang microservices backend on Kubernetes behind an Envoy proxy, instrumented with Prometheus and Grafana to profile request latency and tune throughput under heavy concurrent traffic.

Weak bullets rewritten:

- DreamScape bullet 1 originally ended "and local-first session tracking." Rewritten to "a local-first mobile user experience" to carry the posting's own phrase while keeping the local-first architecture claim.
- Actual Reality bullet 1 originally said "ARIA and tab-history guardrails." Rewritten to "accessibility and tab-history guardrails" so a recruiter without ARIA context understands the user-facing outcome.
- SmartSolve bullet 2 originally ended "helping operations and executive leaders prioritize internal AI investments." Rewritten to surface expected outcomes and business impact, which is what the underlying AI audits actually produced.

Responsibility-only bullets removed or rewritten:

- Actual Reality MCP-server bullet (remote MCP server with keyed access for customer and admin AI tools) removed for page budget, not for weakness. It is verified and can return in a future package.
- AAIS Data Engineering bullet on modernizing 160+ legacy Pentaho jobs into AWS Glue workflows and partitioned S3 pipelines removed for page budget; the remaining AAIS Data bullets still carry AWS and 20+ TB scale.
- SmartSolve QMS dependency-register bullet removed; it is planning work and weaker than the other three for a product-engineering role.
- Travel Health Advisor, RocketGrader, Fix-It-Flow, FalconGraph Search, Self-Adaptive Parallelism, and the portfolio project removed so the two provable bonus technologies (React Native, Go) could each carry a full project entry.
- AAIS automated CSV cleaning/deduplication bullet removed as redundant with the 1,000+ table generation bullet.

Bullets over two visual lines tightened:

- Actual Reality project-data reliability bullet trimmed from "route and gateway cache layers" phrasing to the current form.
- SmartSolve onboarding-tracker bullet kept at two lines by dropping "full-stack" hyphenation to "fullstack" (also an exact posting keyword).

Human recruiter readability notes:

- Internal/tool-specific terms translated: Plane ticket/project status became generic project-management language before the bullet was cut; magic-link sign-in became "login transitions"; ARIA became "accessibility"; Pentaho and Semarchy MDM were dropped rather than explained.
- Private details removed or generalized: No customer name, no `my.actualreality.ai` URL, no private repository reference, no Plane vendor name, no ticket IDs, no branch names, no internal file paths.
- Current/private-role debloat decision: Actual Reality is capped at four bullets covering the product surface, reliability work, and the AI Gateway. Small individual ticket fixes (Firestore index repair, invite domains, auth user reconciliation) were deliberately excluded because they are private-repo trivia. Older verified internships (AAIS, APKD) carry the additional depth.

## Changes Made

- Resume: Created `resume.tex` from `templates/canonical-resume.tex`. Contact title changed from "Software Engineer" to "Software Engineer I" (Target Professional Title Clause, exact posted title, entry band, truthful against internship-only evidence). Actual Reality bullets reordered and retitled for consumer-facing UX lead. SmartSolve bullets retitled. AAIS and APKD bullets selected for scale, reliability, and React/Node.js surface. Projects reduced to DreamScape and TachyonMesh. Technical Skills recategorized into Web & Mobile Frontend / Backend & APIs / AWS & DevOps / AI & Quality.
- Cover letter: Created `cover-letter.md` and `cover-letter.tex`. Anchored on the posting's "Just Works" language and the named Chat / Stream Together / Discovery surfaces, with two deep proof points and a plain closing.
- Internal notes: This file. Also recorded a profile inconsistency: `profile/evidence-index.md` lists Go as unsupported while `profile/projects-master.md` verifies TachyonMesh.

## Submission Readiness

Recommended status: Applied.

Submit now or hold: Submit. The package passes the validator, is exactly one page, carries no unsupported claims, and flags its one real weakness (no gaming/streaming domain evidence) without inventing any. Onsite San Francisco and the SWE I entry band are both reasonable targets.

Pre-submit actions: Confirm the posting is still open under Job ID TW9303 and record the canonical Amazon/Twitch careers URL in the tracker. Aryan should be ready to answer the San Francisco relocation question during the recruiter screen.

Referral before submit: Optional. No referral target identified. If outreach begins, keep it short and follow `templates/referral-outreach-template.md`.

## Scoring Methodology

Scoring source: Internal `Job Alignment & Evidence Score` rubric from `AGENTS.md`, applied by manual keyword analysis plus `automation/analyze_application_keywords.py` with the package-local expanded term file. No external or third-party ATS scorer was used, so no external tool name, version, or configuration needs recording.

Score breakdown:

- Keyword coverage: 36/40 - React, React Native, Expo, Next.js, TypeScript, Go/Golang, AWS (Lambda, S3, DynamoDB, IAM, Glue), Kubernetes, Docker, Node/Express REST APIs, PostgreSQL, MySQL, MongoDB, Firebase, microservices, infrastructure, observability, CI, testing, authentication, accessibility, consumer-facing, customer portal, user experience, business impact, code review, latency, and the exact posted title are all present in evidence-bearing context. Deductions: no AWS ECS/SQS/Step Functions, no Twitch/gaming/streaming terms, and `designers`/`product managers` are carried only by the truthful `stakeholders` wording.
- Experience relevance: 23/25 - Two dated consumer-facing React/Next.js roles plus a cross-platform React Native app match the posting's "web & mobile frontend development (React heavy)" and "1+ years of professional engineering experience building consumer-facing products." The reliability focus maps directly to "making sure Web and Mobile Twitch 'Just Works'," and the Product Owner bullet covers the product/business partnership half. Deduction: no direct live-streaming or community-domain product work.
- Impact and evidence: 14/15 - Action-plus-technology-plus-result bullets carry quantified scope: 44 red-team fixtures, 134 passing tests, 20+ TB, 1,000+ production SQL tables, 160+ tables across 10+ insurance lines, about 110 internal users, 24-hour data latency, 700+ member companies in supporting source material. Deduction: the consumer-facing React work is internship-scale rather than mass-market scale, so its impact is described qualitatively rather than with a user-count metric.
- Formatting and ATS parsing: 10/10 - One page confirmed by `pdfinfo`; text extracts cleanly through `pdftotext`; canonical 11pt article class, letterpaper geometry, 0.22in side margins, 0.92 line spread, `glyphtounicode`, `\pdfgentounicode=1`, `\pagestyle{empty}`, single-level `tightitemize`; no `tabular`, images, icons, text boxes, columns, colors, headers, or footers; single consistent solid bullet; no Professional Summary, so no summary line-count risk; 103 KB PDF, far under the 2.5 MB parser target.
- Risk and gap handling: 9/10 - Sponsorship language is absent from the posting, so the F-1 gate passes and no visa language appears in either submitted artifact. Every bonus requirement was searched before being called a gap; three unsupported AWS services and the entire gaming/streaming domain were identified and intentionally omitted rather than approximated. One deduction: the gaming/streaming domain gap is real and cannot be closed from current source material.

## Alignment Pass

Job Alignment & Evidence Score: 92/100

Internal estimate only; not a predicted ATS score.

Keyword coverage helper:

- Default analyzer (`automation/analyze_application_keywords.py application-packages/Twitch/Software-Engineer-I`): 7 terms checked, 5 found, 2 missing (`authorization` boilerplate, `code reviews` plural variant).
- Expanded analyzer with `expanded-keywords.txt`: 61 terms checked, 42 found after the recovery pass, 19 missing. Every remaining miss is either an employer slogan (`AI driven engineering`, `automated tools`, `development lifecycles`, `frontend development`), an unsupported technology (ECS, SQS, Step Functions), an unsupported domain term (Twitch, gaming, streaming, software used by), a boilerplate work-authorization term (`authorization`), or a partial-evidence collaboration noun (`designers`, `design review`, `product managers`, `customer problems`, `consumer products`).
- Interpretation: the default 7-term denominator is not the ATS keyword universe. Coverage should be read from the 61-term expanded pass.

Strong matches:

- React-heavy web frontend: Actual Reality Next.js 15 / React 19 customer portal, SmartSolve Next.js fullstack tracker, AAIS React/Node.js modernization.
- React Native mobile: DreamScape on React Native and Expo, plus the Web & Mobile Frontend skills line.
- Consumer-facing UX and reliability: portal tool consolidation, login/session hardening, stale-data elimination. This is the strongest single match to the posting's core mission.
- Fullstack with backend ownership: AI Gateway, AWS Lambda/S3/DynamoDB/IAM/Glue, PostgreSQL/MongoDB/Firebase, REST APIs.
- Go backend language: TachyonMesh Golang microservices on Kubernetes with Envoy, Prometheus, and Grafana.
- AI-driven engineering: LiteLLM AI Gateway with smart-router tiers, guardrails, Langfuse tracing, Slack alerts, CI gates, 44 red-team fixtures; daily Claude Code and Codex use for debugging and code review inside an isolated Docker devcontainer.
- Scale and reliability: 20+ TB, 1,000+ production SQL tables, about 110 internal users, 24-hour data latency.

Gaps / intentionally omitted unsupported keywords:

- AWS ECS, SQS, and Step Functions. No evidence in `profile/` or `master-documents/`. Omitted rather than approximated with ECS-adjacent Kubernetes/Docker wording.
- Twitch, gaming, and streaming familiarity. No gaming or streaming project exists. The only `streaming` hits in source material are ElevenLabs audio streaming and healthcare data ingestion.
- "Personally built and/or maintains software used by the gaming community." No maintained community software. Omitted.
- Design reviews and direct collaboration with named product managers and designers. Only temporary Product Owner ownership is verified; carried as `stakeholders`.
- Streamer/viewer domain vocabulary (audience growth, engagement, revenue for streamers, discovery pathways). Not supported by evidence and not invented.

Recommended improvements:

- If Aryan builds or maintains anything in the gaming or streaming space, adding it to `profile/projects-master.md` would close the single largest remaining gap for future Twitch-family, Discord, or streaming-platform applications.
- If Aryan has used ECS, SQS, or Step Functions outside the documented roles, that belongs in `profile/skills-master.md` and `profile/experience-master.md` before any future AWS-heavy application.
- Prepare the San Francisco relocation story for the recruiter screen, since the posting is onsite and the M.S. completed August 2026.

## Verification

- LaTeX compiled: Pass - `pdflatex -interaction=nonstopmode -halt-on-error` succeeded for `resume.tex` and `cover-letter.tex`.
- PDF page count: Pass - `resume.pdf` is exactly 1 page. `cover-letter.pdf` is exactly 1 page.
- Professional Summary line count: Not applicable - no Professional Summary section is used, per the early-career default in `AGENTS.md`.
- Experience bullet count gate: Pass - 13 experience bullets against the 11-bullet floor; no waiver needed.
- PDF text checked with bounded output: Pass - single `pdftotext -layout` read used for the canonical visual review; reading order confirmed as name, contact/title, Education, Experience, Projects, Technical Skills.
- Keyword coverage helper run: Pass - default analyzer run, result recorded above.
- Expanded keyword term file checked: Pass - `expanded-keywords.txt`, 61 exact terms.
- Expanded role-specific keyword audit checked: Pass - 42 found, 19 missing, each missing term classified as slogan, unsupported technology, unsupported domain, boilerplate, or partial-evidence collaboration noun.
- Two-line bullet-wrap check: Pass - all 16 experience and project bullets render at one or two lines; verified with `pdftotext -layout` line grouping and confirmed by the validator.
- Gap recovery gate checked: Pass - searched terms, locations, recovered evidence, and final decisions recorded above.
- ATS source gate checked: Pass - no `tabular`/`tabular*`/`tabularx`, no `graphicx`/`includegraphics`, no `multicols`/`twocolumn`, no `textblock`/`textpos`, no `fontawesome`, no `xcolor`/`color`/`transparent`, no `fancyhdr`. Canonical required patterns all present.
- Human recruiter readability gate checked: Pass - no ticket IDs, branch names, private routes, internal code names, customer names, or private repository URLs. ARIA explained as accessibility, magic-link flows described as login transitions, vendor names reduced to plain product language.
- Visual consistency gate checked: Pass - preamble and macros copied unchanged from `templates/canonical-resume.tex`, which matches `templates/canonical-visual-system.md` and `master-documents/master-resume/resume.tex`. No one-off geometry, font size, heading, or bullet changes. Rendered output reviewed for border width, name/contact placement, section rules, bullet size, role/date alignment, and density.
- Page utilization gate checked: Pass - last text baseline sits 5.1pt above the bottom margin, comfortably inside the 24pt hard-failure and 20pt warning thresholds. Verified by `pdftotext -bbox` measurement. The page was filled by restoring verified evidence, not by tightening margins, shrinking fonts, or adding filler: the AAIS React/Node.js RBAC bullet was restored after Travel Health Advisor was cut, and the AWS & DevOps skills line was expanded with Prometheus.
- Submitted-facing terminology sync checked: Pass - the cover letter uses the same public-safe terms as the resume: customer portal, tabbed surface, feature gating, legacy redirects, accessibility guardrails, session-cookie domains, login transitions, work-item counts, route and gateway cache layers, React Native and Expo, local-first persistence, LiteLLM AI Gateway, smart-router tiers, guardrails, CI gates, red-team fixtures, Claude Code, Codex, Docker devcontainer. No cover-letter-only internal terminology was introduced.
- Score consistency gate checked: Pass - 36 + 23 + 14 + 10 + 9 = 92, which equals the recorded `Job Alignment & Evidence Score: 92/100`. Breakdown sums to 100 possible points.
- Cover-letter artifact checked: Pass - `cover-letter.md` and `cover-letter.tex` produce a 1-page, 44 KB `cover-letter.pdf` with the canonical 11pt Computer Modern layout, 0.80in side margins, 0.70in top/bottom margins, and the same name/contact hierarchy as the resume. No graphics or decorative elements. No F-1, OPT, sponsorship, E-Verify, or Form I-983 language.
- Application validator run: Pass - `python3 automation/validate_application_package.py application-packages/Twitch/Software-Engineer-I` returned success after the LaTeX build artifacts were removed.
- Token-efficient source access checked: Pass - worked from `profile/evidence-index.md`, canonical templates, targeted grep slices of `profile/experience-master.md` and `profile/projects-master.md`, the validator and analyzer CLI output, and a 12-line tracker header. No historical application package, no full tracker read, and no raw `pdftotext -bbox` dump was used.