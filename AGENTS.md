# Career Ops Repo Instructions

This repository is used to maintain Aryan Miriyala's career source material, discover recent job opportunities, track applications, and generate targeted resumes and cover letters for specific job applications.

## Pipeline Separation Rule

This repo has two separate pipelines. Do not merge them unless Aryan explicitly asks to move from one pipeline into the other.

### Pipeline 1: Job Discovery

Trigger this pipeline when Aryan asks to find jobs, search job boards, discover recent postings, scan ATS feeds, update `job-search/jobs-inbox.csv`, generate Google search links, collect ATS URLs, or improve job crawling/discovery.

Job Discovery outputs belong under `job-search/` and should produce job leads, source reports, search links, direct ATS target updates, and CSV inbox updates. It does not generate tailored resumes or cover letters.

### Pipeline 2: Application Package Generation

Trigger this pipeline when Aryan provides a specific job description or says he is applying to a specific role/company.

Application Package Generation outputs belong under `application-packages/<Company>/<Role>/` and should produce the tailored resume, cover letter, tailoring notes, validation result, Job Alignment & Evidence Score, and tracker update. It does not search broadly for additional jobs unless Aryan separately asks for job discovery.

A discovered job becomes an application only after Aryan selects it or provides the specific job description/application link for that role.

## Application Package Operating Rule

For application package work, act from a senior technical recruiter and resume strategist perspective, not only a document-generation perspective. Optimize for truthful callback probability by making the strongest role-relevant evidence visible quickly, while keeping every claim grounded in `profile/`, `master-documents/`, project repositories, or the provided job description. Prior application packages and prior resumes are historical outputs, not source material; open them only when Aryan explicitly names a specific prior package to reuse, compare, or audit.

When Aryan provides a job description, treat it as a request to run the complete established application package pipeline for that role. Aryan should not need to separately ask for setup, next steps, resume generation, cover-letter generation, PDF compilation, ATS alignment, or tracker updates. Save the posting, research the company when useful, create or update the application package, draft tailoring notes, generate the tailored resume and cover letter, compile submission files in the employer's accepted format, run the parser validation and Job Alignment & Evidence Score, verify outputs, update the tracker, commit, and push.

Supplying a job description is approval to perform the full pipeline and generate tailored application artifacts. Do not stop at a proposal unless Aryan explicitly asks to review proposed changes first. If the job description has serious blockers, unsupported requirements, or unclear fit, proceed with truthful materials while flagging those risks in `tailoring-notes.md` and the final response.

If Aryan provides application questions, short-answer prompts, company/product interest, personal connection, desired emphasis, referral context, or a requested status override with the job description, preserve and use that context inside the package. Save drafted application answers in `application-questions.md` when they are part of the application, keep them grounded in Aryan's verified source material, and avoid submitting generic or over-polished AI-sounding answers.

For application questions and short-answer drafts, apply the human-application-answer standard before returning or saving the answer. The answer should sound like a thoughtful early-career engineer who can say the response out loud, not like a generated cover-letter excerpt. Use concrete context from Aryan's verified experience, projects, real company research, or explicit user-provided motivation. Avoid generic praise, over-polished symmetry, abstract filler, unsupported personal feelings, and AI-writing cliches such as "at the intersection of," "deeply passionate," "ever-evolving landscape," "seamlessly," "leverage," "robust," "transformative," or "perfect fit." Drafted answers must not use semicolons or em dashes. Avoid colons in answer prose unless the employer's form field or prompt format truly requires them. When an application package includes `application-questions.md` or `application-answers.md`, record `Application-answer human voice gate checked: Pass - <specific check summary>` in `tailoring-notes.md`.

When Aryan asks to create a resume and cover letter for a specific application, treat that application as `Applied` in `operations/application-tracker.md` unless Aryan explicitly requests another status. Do not leave a completed requested package at `Ready` by default. Do not read the full tracker into model context for a new application; use the known table schema plus a targeted append/upsert command or script. Read tracker contents only when checking for a duplicate, changing an existing row, or answering a tracker-specific question.

Every final application response must include the ready artifact paths, one-page PDF verification, application validator result, and the `Job Alignment & Evidence Score`. Describe this score as an internal alignment estimate, never as a prediction of an employer's ATS decision. Do not leave Aryan to ask separately whether the resume is aligned or whether the package passed validation.

Make incremental commits for small, coherent changes so the repository stays easy to review and push to GitHub. Do not bundle unrelated resume, cover-letter, application, tracker, and source-material updates into one large commit.

## Application Pipeline Execution Contract

For every job description, start from this file as the source of truth. Do not rely on memory from the current chat, prior application habits, or an abbreviated version of the workflow. Re-read the relevant `AGENTS.md` instructions and then execute the pipeline as a checklist.

If a profile guide, template, automation script, prior application, or reusable prompt conflicts with this file, this file takes precedence. Update the conflicting dependency before using it to finalize a new application package; do not silently fall back to the older rule. Do not inspect prior application packages just to look for conflicts or reusable wording unless Aryan explicitly names a specific package.

Do not mark an application package complete until all required outputs exist and have been verified:

- `application-packages/<Company>/<Role>/job-description.md`
- `application-packages/<Company>/<Role>/tailoring-notes.md`
- `application-packages/<Company>/<Role>/resume.tex`
- `application-packages/<Company>/<Role>/resume.pdf`
- `application-packages/<Company>/<Role>/cover-letter.md`
- `application-packages/<Company>/<Role>/cover-letter.pdf` or `cover-letter.docx`
- Updated `operations/application-tracker.md`
- Recorded Job Alignment & Evidence Score and alignment pass in `tailoring-notes.md`
- Passing `automation/validate_application_package.py` result
- Recorded verification gates in `tailoring-notes.md` with explicit `Pass` or allowed `Waived - <reason>` values; blank gate labels do not count
- Cleaned generated LaTeX artifacts
- Incremental commit and push

If context is resumed, compacted, or interrupted mid-application, re-open the application folder and this file before continuing. Continue from the repository state, not from assumptions about what was already done.

## Application Package Pipeline

Application packages should support broad but targeted early-career search lanes. Do not narrow the pipeline only to software engineering, data engineering, and AI roles. Valid primary lanes include software engineering/full stack, data engineering, applied AI/agentic systems, data analyst/business analyst, product analyst/operations analyst, cloud/platform/enterprise systems, security/IT/support-adjacent technical roles, healthcare/insurance/education workflow technology, and other adjacent early-career technical roles. Broaden the search, but still tailor each package to one primary lane so the resume and cover letter do not read as generic.

For every new job application:

1. Create `application-packages/<Company>/<Role>/`.
2. Save the full job posting as `job-description.md`. Do not replace the posting with a summary, keyword digest, or shortened role brief. It is acceptable to add a short metadata block above the posting, but the full employer-provided role text must remain available in the file because keyword extraction, gap recovery, scoring, and cover-letter targeting depend on the complete source. If the full posting cannot be recovered, document the source limitation in `tailoring-notes.md`.
3. Add or update the role in `operations/application-tracker.md` by targeted append/upsert without reading the full tracker into model context unless duplicate detection or an existing-row update is required.
4. Review `profile/evidence-index.md` first for relevant experience, projects, skills, reusable bullets, lane routing, project routing, and common unsupported claims. Open full profile master files only for exact wording, source verification, or gaps not covered by the index.
5. Apply `profile/ats-recruiter-resume-guide.md` and `profile/resume-targeting-guide.md` before proposing resume edits. Use these guides for rules and quality gates, not as a reason to reread unrelated source material.
6. Build a job keyword map before writing the resume: exact posted role title, required skills, exact tool/framework variants, repeated terms, responsibilities, domain language, must-have tools, nice-to-have tools, and unsupported terms to avoid. Do not use a fixed keyword threshold or the default analyzer's term count as the full keyword universe. Separate evidence-bearing ATS keywords from employer slogans, internal org names, broad soft-skill phrases, and repeated company boilerplate. Use the evidence-bearing terms to decide the Target Professional Title Clause, resume angle, bullet selection, projects, technical skills, and cover-letter proof points. Track lower-value or unsupported terms in `tailoring-notes.md` instead of stuffing them into submitted artifacts. Compare the map against the project routing cache in `profile/evidence-index.md` before selecting projects.
7. Run the **Gap Recovery Gate** before final bullet/project selection. For every important job requirement, preferred skill, tool, domain term, or responsibility that is not already planned for the resume, classify it as one of:
   - `Supported - add/use now`: verified in `profile/`, `master-documents/`, project repositories, or another inspected source, and should be added to the resume, cover letter, skills section, or tailoring notes if it improves fit.
   - `Likely built but undocumented - ask/update source`: Aryan may have built it, but the repo source material does not currently prove it. Do not put it in submitted artifacts until Aryan confirms it and the relevant `profile/` or project source material is updated.
   - `Unsupported - omit`: no verified evidence exists or the claim would be misleading; document it as intentionally omitted.
   Before classifying a term as unsupported, run an **Important JD Term Search** with targeted `rg` queries across `profile/`, `master-documents/`, and relevant project repositories for the exact tool, domain phrase, responsibility, and close employer wording. Record the searched terms, searched locations, recovered evidence, and final decisions in `tailoring-notes.md`. This gate exists so older projects, hackathons, coursework, private repos, local repositories, and partially documented builds are not accidentally ignored, while still keeping submitted claims interview-defensible.
8. Run the **F-1 Work Authorization Gate** before drafting final artifacts. Identify whether the role is compatible with F-1 CPT/OPT/STEM OPT timing, E-Verify/STEM OPT needs, location constraints, and future employer sponsorship. Treat sponsorship as an internal package risk, not submitted-application content: do not mention F-1, OPT, STEM OPT, visa status, future sponsorship, E-Verify, or Form I-983 in the resume or cover letter unless Aryan explicitly asks. If the posting is silent or ambiguous about sponsorship, proceed with the package and record follow-up questions internally. If the posting explicitly states no visa/work-visa sponsorship, requires independent permanent work authorization or authorization to work for any employer, restricts eligibility to U.S. citizens/permanent residents, requires clearance Aryan does not have, or otherwise directly conflicts with Aryan's F-1/OPT/STEM OPT path, flag it immediately and do not finalize the application package unless Aryan explicitly asks to proceed for archival, practice, or non-U.S. reasons.
9. Apply `profile/cover-letter-guide.md` before drafting any cover letter. Use known personal context from `profile/` and targeted user-provided context. Do not open prior application notes for cover-letter language unless Aryan explicitly names a specific prior package. Ask Aryan cover-letter personalization questions only when the letter would be materially weaker or risky without the answer:
   - What genuinely interests you about this company?
   - Do you have any personal connection to the company, product, industry, mission, or team?
   - Is there anything specific you want the hiring manager to feel after reading the letter?
10. Document the resume direction, Target Professional Title Clause, Gap Recovery Gate result, F-1 Work Authorization Gate result, referral plan, cover-letter angle, strongest matching experience/projects, important keyword targets, unsupported keywords to avoid, internal/private terms translated for recruiter readability, and any blocking eligibility questions in `tailoring-notes.md`.
11. Create a tailored `resume.tex` from `templates/canonical-resume.tex`, `master-documents/master-resume/resume.tex`, or another approved canonical resume template. Do not read previous application packages to discover the latest visual pattern during a normal new-package run.
12. Audit every experience and project bullet against the bullet rules before compiling. Rewrite any bullet that lacks a strong action verb, a specific contribution, truthful method or technology when relevant, scope/domain context, and impact/result. Every finalized bullet should normally render as no more than two visual PDF lines in the canonical layout; if a bullet exceeds two lines, shorten it, split it only when both resulting bullets add distinct value, or document a rare high-signal exception. Run the **Human Recruiter Readability Gate** at the same time: a reviewer who does not know Aryan's internal tickets, private repositories, company tooling, or project code names must still understand what system was built, how it worked, and why it mattered.
13. Generate `resume.pdf` locally from the tailored LaTeX source only when needed for submission.
14. Create `cover-letter.md` and, when submitting, generate a `cover-letter.pdf` or `cover-letter.docx`.
15. Run a resume-vs-job-description alignment pass after generating the resume. Use `python3 automation/analyze_application_keywords.py application-packages/<Company>/<Role>` when a resume artifact exists, then run an expanded role-specific keyword pass for important JD terms that the default helper may not know, using explicit `--term` values or a documented manual table. Include the default analyzer result, expanded keyword result, matched keywords, missing-but-truthful keyword opportunities, unsupported keywords intentionally omitted, concrete next-step recommendations, and the Job Alignment & Evidence Score. Treat analyzer output as exact-term coverage only; its denominator is not the total ATS keyword universe. Calculate the internal score separately and verify that the written score equals the point-by-point breakdown.
16. Add `tailoring-notes.md` explaining which experience, projects, and keywords were emphasized, plus the Gap Recovery Gate, F-1 Work Authorization Gate, bullet audit, Human Recruiter Readability Gate, ATS source gate, visual consistency gate, page utilization gate, submitted-facing terminology sync, alignment pass, score-consistency check, and Job Alignment & Evidence Score.
17. Run `python3 automation/validate_application_package.py application-packages/<Company>/<Role>` before marking the package ready. Fix failures instead of ignoring them. If a failure is intentional for a specific application, document the reason in `tailoring-notes.md` and the final response.
18. Update `operations/application-tracker.md` when the application is ready, applied, rejected, interviewing, or archived. Record referral status and next outreach/follow-up state for each application, even when no referral target has been found yet. For a new row, use `python3 automation/upsert_application_tracker.py ...` or another bounded append/upsert without printing or loading the whole tracker into model context.

If the job description includes an eligibility, location, sponsorship, clearance, degree, or schedule constraint, flag it during the intake response before spending effort on final artifacts. For Aryan's F-1 situation, explicit no-sponsorship, independent-work-authorization, authorization-for-any-employer, citizen-only, permanent-resident-only, or incompatible-clearance wording is a serious blocker, not a routine gap; archive or pause unless Aryan explicitly asks to continue. If the posting is silent or unclear on sponsorship, proceed and track the risk internally rather than self-disqualifying.

## Job Discovery Pipeline

For job-search and job-discovery requests, do not rely only on generic public boards. Use the layered job-search workflow in `job-search/`:

1. Run `python3 job-search/src/job_discovery.py run-pipeline` as the default command. It runs configured direct ATS targets, the broad ATS scan, supplemental public feeds, and search-link generation.
2. Review the dated `jobs-by-window.md`, `shortlist.md`, `review-candidates.md`, and `jobs.csv` files under `job-search/results/YYYY-MM-DD/pipeline/`.
3. Use generated search links to collect new ATS-hosted URLs, especially Greenhouse, Lever, Ashby, and SmartRecruiters links.
4. Run `discover-direct-ats-targets` on collected URLs to extract, verify, and save company board tokens in `job-search/config/direct-ats-targets.json`.
5. Use lower-level commands such as `run-direct-ats`, `run-broad-ats`, and `run-public-search` only for adapter debugging, source-specific checks, or intentionally scoped maintenance runs.
6. Keep iCIMS, Workable, Oracle, SAP SuccessFactors, ADP, BambooHR, Jobvite, and company-specific pages marked as adapter/backlog sources until reliable structured ingestion is implemented and verified.

The goal is breadth plus accuracy: search discovers new company boards, direct ATS APIs provide structured job data, and the CSV remains the manual-review source of truth.

Keep `job-search/jobs-inbox.csv` minimal. It should contain only `company`, `position`, `posted_at`, `pulled_at`, and `url`. Put scoring, source metadata, fit flags, notes, snippets, and other noisy/internal details in dated Markdown reports instead of the CSV.

Maintain scan history separately in `job-search/data/scan-history.tsv`. The history file may store URL, normalized company-role identity, first-seen time, last-seen time, source, status, score, flags, and location for dedupe and run-quality tracking. Do not add those fields to `jobs-inbox.csv`.

For F-1 job discovery, prioritize U.S. roles at companies with sponsor history in `job-search/config/h1b-sponsor-watchlist.json`, postings that mention OPT, STEM OPT, CPT, E-Verify, or visa sponsorship, and roles where the company has a realistic international-student hiring path. Postings with no-sponsorship, independent-work-authorization, U.S.-citizen-only, permanent-resident-only, clearance-only, or similar blocker language must not enter the strict shortlist inbox.

## Directory Conventions

- `master-documents/master-resume/`: canonical general resume source and PDF.
- `master-documents/master-cover-letter/`: reusable cover-letter template material.
- `profile/`: source-of-truth documents for experience, projects, skills, bullet banks, and cover-letter language. Start with `profile/evidence-index.md` for application generation; open larger master files only for exact wording, source verification, or uncovered gaps.
- `application-packages/<Company>/<Role>/`: one complete application package per role.
- `operations/application-tracker.md`: high-level status tracker for all active and historical applications.
- `job-search/`: recent-job discovery tooling for ATS search links, `jobs-inbox.csv` local job storage, scoring, and recency-bucket reports.
- `templates/`: reusable scaffolds for application folders, notes, and the reusable prompt for starting a new application pipeline.

Do not keep duplicate master resume copies. The canonical resume source is `master-documents/master-resume/resume.tex`.

Do not commit binary/generated artifacts unless Aryan explicitly asks. This includes PDFs, DOCX files, PNG previews, and LaTeX build artifacts.

## Token-Efficient Source Access

- Do not read all of `application-packages/` when creating a new application package. Existing packages are historical outputs, not default source material.
- Do not read the full `operations/application-tracker.md` for a new application row. Use targeted append/upsert behavior and the known schema; read the tracker only for duplicate checks, existing-row edits, status reports, or tracker-specific questions.
- Use `profile/evidence-index.md`, including its project routing cache, targeted `profile/` source sections, `master-documents/`, project repositories, the saved job description, and canonical templates as the default source set.
- Read the full `profile/experience-master.md` or `profile/projects-master.md` only when the evidence index lacks a needed requirement, exact source wording is needed, or a gap recovery search points to a specific section.
- Use targeted `rg` searches for exact job-description keywords, unsupported gaps, or specific company/domain context instead of broad historical-package scans. For every important JD term not already covered by the evidence index, record the targeted search before omitting the term.
- Open a prior application package only when Aryan explicitly names that package for reuse, comparison, or audit. Do not use prior resumes or prior cover letters as the normal way to discover evidence, wording, or visual patterns.

## Resume Rules

- For Aryan's current early-career applications, the resume must be exactly one page unless the employer explicitly requests a CV or a longer format. It must also use the page efficiently: serious, readable, role-aligned content should extend into the bottom portion rather than leaving a large unused band.
- Use the repository's canonical application-resume visual system: US Letter, 11-point `article` class, Computer Modern typography, approximately 0.22-inch left/right margins and 0.10-inch top/bottom margins, approximately 0.92 line spread, centered name/contact block, small-caps ruled section headings, and raised 10-point solid round bullet markers. Keep a visible 2-point gap between each section heading and its divider rule. Do not create a new geometry, font size, heading treatment, or bullet system for an individual application.
- Maintain clear hierarchy while using the available page area efficiently. A finalized application resume should normally carry serious, readable content into the bottom portion of the page, consistent with the established application resumes. If a visible blank band remains, add stronger verified evidence or improve information density before finalizing.
- The 11-point font is a readability floor for the canonical application layout. Do not shrink text to add content. Narrow canonical page borders are permitted only because the layout remains single-column, text-only, and visually verified; do not reduce them further on a one-off basis.
- Use one consistent, ordinary solid bullet symbol throughout all application resumes. Do not mix solid bullets, hollow bullets, dashes, or decorative symbols.
- There is no fixed or hard maximum on the number of bullets for a role, project, or resume. Do not force every entry into an arbitrary two- or three-bullet pattern. Use as many bullets as are needed to present distinct, high-signal, role-aligned evidence while preserving the one-page and readability requirements.
- Bullet count is governed by evidence quality, not symmetry. Add a bullet only when it contributes a distinct accomplishment, system, decision, scope, or result; combine or remove bullets that repeat the same evidence. A role with five strong relevant bullets is preferable to a visually symmetrical role with three weaker bullets.
- **Experience Evidence Floor**: For early-career one-page application resumes, the experience section must normally contain at least 11 strong experience bullets before project bullets are allowed to consume meaningful space. This is a floor, not a target or cap. If fewer than 11 experience bullets are used, `tailoring-notes.md` must include an `Experience Bullet Count Waiver` explaining why no additional verified role-aligned internship, work, research, teaching, or operational evidence should be added. Do not preserve a broad project bullet while omitting a stronger verified experience bullet.
- **Experience-First Fit Rule**: When the page is tight, compress or remove lower-priority project detail before cutting truthful role-aligned experience evidence. Experience takes priority because it is dated, employer-backed evidence and usually carries more recruiter weight than standalone projects for early-career applications.
- **Current/Private Role Debloat Rule**: For current internships, private repositories, customer portals, or work that is still evolving, prefer a small number of high-level bullets that explain the product surface, Aryan's owned engineering contribution, technical method, user/customer context, and result. Do not list many small tickets, branch names, internal issue-tracker details, or tool-specific fixes unless they add a distinct, recruiter-readable accomplishment. Use older verified internships or projects to carry additional depth when they provide stronger public-safe evidence.
- **Visual Consistency Gate**: Before compiling a new application resume, compare its LaTeX preamble and layout macros against the canonical application-resume visual system in `templates/canonical-visual-system.md`, `templates/canonical-resume.tex`, `master-documents/master-resume/resume.tex`, or another approved canonical template. Reuse the same document class, geometry, font, header structure, section styling, bullet label, role/date hierarchy, and skills formatting. Tailoring should change evidence and ordering, not visual identity.
- **Canonical Visual Review Gate**: Render the new resume and inspect it against the canonical visual system, not against arbitrary historical application packages. Confirm that outer borders, name/contact placement, section rules, bullet size, role/date alignment, density, bottom-page usage, clipping, and overlap match the approved document family. Record this comparison in `tailoring-notes.md`.
- **Page Utilization Gate**: A one-page early-career resume is not complete merely because it has one page. The final resume should feel visually complete, with evidence-bearing content reaching close to the bottom of the page in the canonical application-resume family. If the final line of meaningful content leaves more than a small bottom gap, first add or restore verified role-aligned evidence, deepen a thin project bullet with purpose/method/result, add a truthful missing must-have keyword in context, or add a compact high-signal skills item. Do not mark this gate as passed solely because the validator allows the bottom whitespace; visually inspect the rendered PDF and close fillable whitespace whenever verified, role-matched substance can fit without crowding. Do not add filler, duplicate claims, broad soft-skill labels, unsupported technologies, or one-off spacing tricks to fill the page.
- **Canonical Source Gate**: Application resumes must use the canonical `letterpaper,11pt` article source structure, explicit `letterpaper` geometry, `glyphtounicode`, `\pdfgentounicode=1`, `\pagestyle{empty}`, `\linespread{0.92}`, and the canonical single-level `tightitemize` bullet list. If the canonical visual system changes, update this file, the guides, templates, and the validator before using the new pattern.
- If an established visual pattern uses an ATS-risky implementation such as `tabular`, reproduce the appearance with plain text and `\hfill`; consistency of appearance does not override the parser rules below.
- **No Hidden Text or Color Tricks**: Do not use white text, transparent text, colored keyword text, `xcolor`, `color`, `transparent`, or visual-only keyword placement. All resume text must be visible, truthful, and intended for a human reviewer.
- Use ATS-friendly, outcome-oriented bullets following the **STAR/CAR** and **Google XYZ** concepts: **Action Verb + What was built/changed + Method/Technology when relevant + Scope/Context + Impact/Result**.
- The bullet formula is an evidence gate, not a demand that every bullet contain a technology or numerical metric. Every experience and project bullet must clearly show the contribution, context, and result:
  - **Action Verb and Tense**: Begin with a strong active verb (e.g., *Architected, Engineer, Optimized, Migrated, Automate, Delivered*). Use present tense for ongoing responsibilities or results and past tense for completed work. Avoid passive phrases like "Responsible for," "Helped with," or "Worked on."
  - **Individual Contribution**: Make Aryan's own contribution clear. Team context is useful, but the bullet cannot hide behind group ownership. If using verbs like *Collaborated, Contributed, Supported, Partnered,* or *Assisted*, specify the concrete piece Aryan personally built, analyzed, fixed, led, designed, tested, automated, documented, or delivered.
  - **What**: Describe the specific system, feature, database, or pipeline that was built, automated, secured, or modernized.
  - **Method/Technology**: Explain how the work was completed. Name the exact language, framework, cloud service, architectural pattern, operating method, or collaboration approach when it adds truthful evidence. Do not force a technology into teaching, stakeholder, leadership, or operational bullets where it is not relevant.
  - **Scope/Context**: Show the scale, user base, size, or domain context (e.g., *20+ TB of insurance data, 700+ member companies, 110 internal users*).
  - **Impact/Result**: State the quantifiable business or technical outcome (e.g., *reducing cloud spend by 30%, decreasing latency, maintaining 24-hour data latency*). If a verified metric is unavailable, use a truthful qualitative result (e.g., *improving data reliability, strengthening form security, standardizing data flows, or reducing manual errors*).
  - **Metric Context**: When using a metric, include context when possible: baseline, before/after comparison, user count, data size, time window, operational constraint, or system scale. A smaller verified metric with context is stronger than a large number that cannot be explained.
- **Two-Line Bullet Gate**: In the compiled PDF, each experience and project bullet should normally occupy no more than two visual lines. This keeps the resume scannable and prevents dense responsibility paragraphs. Verify with `pdftotext -layout` or visual inspection. If a bullet exceeds two lines, tighten wording while preserving action, context, method, and result; do not shrink the font or margins to compensate.
- Show broad skills through evidence instead of labels. Do not merely claim teamwork, communication, problem-solving, adaptability, ownership, leadership, or learning ability. Demonstrate them through the problem, stakeholders, constraints, decisions, personal contribution, and result.
- Project bullets must explain the project's purpose, user/problem or technical challenge, implementation method, and working result. Do not use projects as tech-stack dumps. A project bullet that only lists frameworks, languages, or APIs without explaining what the system does or why it matters must be rewritten.
- **Human Recruiter Readability Gate**: Submitted bullets must translate internal or obscure terms into plain product/system language. For example, describe a `magic link` as an unauthenticated account-creation or secure sign-in flow when that is the recruiter-relevant meaning, and describe private issue-tracker work as a project-management API integration or customer-portal workflow when the vendor name is not itself a JD keyword. Avoid ticket IDs, private route names, internal code names, and narrow implementation trivia unless the term is public, job-relevant, and explained by context.
- Every final bullet must be interview-defensible. Aryan should be able to explain the technical decisions, tradeoffs, tools used, personal contribution, result, and what he would improve if asked in an interview.
- AI-assisted bullets must be manually edited until they are specific, grounded, and defensible. Reject bullets that are grammatically polished but vague, inflated, buzzword-heavy, emotionally generic, or not traceable to `profile/`, `master-documents/`, project repositories, or the saved job description.
- **Strict Bullet Audit**: Before compilation, review every bullet individually. A bullet that lacks a clear action/contribution, defensible context, and result must be rewritten, combined with a related bullet, or removed. Do not preserve a weak bullet merely to keep bullet counts even across roles.
- **Weak Opener Ban**: No experience or project bullet may start with `Responsible for`, `Helped`, `Worked on`, or `Assisted`. If a collaborative contribution is important, start with the concrete action Aryan performed and name the artifact, system, method, and result.
- **Strong vs. Weak Bullets Example**:
  | Weak (Task-Oriented) | Strong (Impact & Technology-Oriented) |
  | :--- | :--- |
  | Worked on database validation and loaded data into S3 using AWS Lambda. | Automated database validation with AWS Lambda triggers that tokenized PII using hashlib/boto3 and ingested structured JSON into S3, securing data movement and maintaining 24-hour data latency. |
  | Helped build a Next.js onboarding tracker and added SSO authentication. | Architected a full-stack Next.js onboarding tracker with PostgreSQL, Drizzle ORM, SSO, and auth middleware to centralize HR workflows and protect sensitive employee data. |
- **Section-by-Section Guidance**:
  - **Professional Summary**: Optional, not mandatory, and omitted by default for early-career software resumes when the Experience and Technical Skills sections already make the fit clear. Use it only when a concise, job-specific summary materially improves the first recruiter scan. It must be no more than two sentences and, more importantly, must render as no more than two total PDF text lines in the final compiled resume. This is a hard visual gate checked after `pdftotext`; a three-line summary fails even if it is only one sentence. Use the job description's exact language for the role, core stack, domain, and priority responsibilities only when the terms are truthful and supported by evidence below. Omit the summary when it merely repeats the skills section, becomes a keyword list, uses generic buzzwords (e.g., "passionate," "fast learner"), or exists mainly to fill page space.
  - **Target Professional Title Clause**: When a specific job description is provided, extract the employer's exact posted role title and include that exact title once in visible resume text when Aryan can truthfully position toward it. Prefer a concise title token in the centered contact/title line when the Professional Summary is omitted, such as `Software Engineer`, `Software Engineer I`, or another truthful adjacent role label. Do not create a redundant standalone title line, do not add awkward `-aligned` phrasing, do not rewrite Aryan's actual past job titles to match the posting, do not claim a seniority level he has not held, and do not add the title as hidden text, repeated text, a keyword block, or a disconnected label. The surrounding resume evidence must prove the title alignment through role-aligned bullets and skills, not broad self-praise.
  - **Education**: Show degrees, GPA (e.g., GPA: 4.00/4.00), graduation dates, and university name. Ensure it is prominently displayed.
  - **Experience**: Keep experience entries in reverse chronological order by default. Do not reorder roles by relevance unless Aryan explicitly asks for a relevance-first resume for a specific application. Use tailoring inside each role instead: the first 1-2 bullets of relevant roles must align directly with the highest-priority responsibilities and keywords of the job description. Highlight systems thinking, architectural decisions, and working with constraints (e.g., scalability, reliability, security).
  - **Projects**: Use projects to support the primary resume angle and cover skill gaps not shown in the professional experience. Emphasize actual implementation details and files in the repository.
  - **Technical Skills**: Group into categorized lists (e.g., Languages, Frontend, Backend/API, Cloud/DevOps, Databases, AI/ML, Security). This is key for parser categorization. Do not list broad responsibilities (e.g., "troubleshooting") as skills.
- Do not invent metrics. Use exact numbers only when supported by the source material.
- Preserve the canonical LaTeX visual identity unless Aryan asks for a repository-wide redesign. Never redesign only one application package. Any approved visual-system change must update this file and the relevant guides before it is used for future packages.
- Keep bullets concise enough to fit the one-page layout (usually 1-2 lines on the PDF page).
- Experience generally takes precedence over Projects. Preserve internship roles by default because they are core early-career evidence, but this is a repository preference rather than an industry mandate. A weakly relevant internship may be compressed or omitted when retaining it would displace substantially stronger evidence or force unreadable formatting; document that decision in `tailoring-notes.md`.
- Do not leave a tailored resume genuinely sparse. If there is substantial usable space, add a high-signal verified experience bullet, relevant project, missing truthful must-have keyword in context, or stronger technical detail. Do not add filler, duplicate claims, broad soft-skill labels, unsupported technologies, or manipulate spacing solely to reach the bottom edge.
- During PDF review, inspect the entire page for balance, including the lower half and bottom. The page should look substantive and intentionally composed, match the canonical visual system, and avoid clipping, overlap, unreadable density, or a large unused bottom band.
- Avoid aggressive negative spacing in Experience and Projects. Do not use negative project `itemsep` or large negative bullet `vspace` values just to force more content onto the page.
- Prefer fewer, stronger projects with readable descriptions over many project one-liners stacked tightly, unless the additional projects can be included without hurting scanability. Projects should support the target role and remain scannable by a human reviewer.
- The resume must be readable by a human reviewer. Do not solve length problems by making the document feel cramped or shrinking text into unreadable sizes.
- When a resume is too long, first tighten wording, remove repetition, and prioritize the strongest role-aligned evidence. Keep the canonical 11-point font and standard geometry unchanged; solve fit through content decisions rather than one-off layout changes.

## Alignment And Evidence Scoring

Every finalized application resume should include an alignment pass against the saved `job-description.md`.

The `Job Alignment & Evidence Score` is a transparent internal rubric, not an employer ATS score, pass probability, or guarantee of an interview. Do not claim or imply that a universal employer ATS cutoff exists.

Application packages have an internal readiness gate of `90/100` or higher. Before finalizing a package below `90/100`, run another truthful alignment pass and improve the resume, cover letter, project selection, skills section, or keyword placement where the repo source material supports it. If the score still remains below `90/100` because of unsupported tools, eligibility constraints, location constraints, domain gaps, or other requirements Aryan cannot truthfully claim, the package may proceed only with an explicit `Sub-90 Readiness Waiver` section in `tailoring-notes.md` explaining why the score cannot be raised without inventing claims and whether Aryan still wants to apply. Do not use the waiver to avoid ordinary tailoring work.

A package is ready when the score is at least `90/100`, or when a documented sub-90 waiver is present, mandatory qualifications are truthfully addressed or clearly flagged, important job language is supported by evidence, the parser and visual checks pass, and no unsupported claims were added. Use the numerical score to identify improvement opportunities, not to manufacture a target result.

## ATS Parser And Recruiter Screen Rules

Treat ATS alignment as structured parsing plus human review, not as magic. A strong package must be optimized for both the parser and the recruiter.

- **Single-Column Layout**: Always use a clean, single-column layout. Multi-column formats cause parsers to scramble text, leading to misinterpretation of experience.
- **No Complex Elements**: Do not use tables, LaTeX `tabular`/`tabular*` constructs, images, icons, text boxes, graphics, personal logos, or decorative formatting in application resumes. Do not place contact information in a PDF header or footer. These elements can hide, split, or reorder text for parsers. The PDF must be text-extractable in reading order with `pdftotext`.
- **Text-Based File Contract**: Generate text-based PDFs from LaTeX by default and use DOCX only when the employer requests it or a specific portal fails PDF parsing. Never submit image-based, scanned, screenshot, design-tool-flattened, or rasterized resumes. Keep `resume.pdf` under a conservative 2.5 MB parser target, while keeping all final submission artifacts under 5 MB unless the employer explicitly allows more.
- **Exact Keyword Mirroring**: Use exact job-description language for critical terms when truthful. If the job description says `REST-based API development` or `AWS Glue`, use those exact phrases rather than synonyms.
- **Exact Posted Title Match**: Treat the employer's exact posted role title as a high-priority keyword because recruiter filtering can search full resume text for job titles, skills, locations, and other keywords. The exact posted title should appear once in a truthful visible summary/title/header clause and should also be reflected through nearby evidence-bearing bullets. If the posted title includes unsupported seniority, specialization, clearance, or licensure language, include only a non-misleading adjacent title and document the unsupported part in `tailoring-notes.md`.
- **Context-Bound Keywords**: Put each high-priority keyword in evidence-bearing context (e.g., a role bullet or project line must show what was built, secured, or improved using that technology) instead of just dumping a list of tools.
- **Standard Heading Titles**: Use standard titles for sections that are included: `Professional Summary`, `Education`, `Experience`, `Projects`, and `Technical Skills`. `Professional Summary` remains optional. Creative section names can confuse parser categorization.
- **Relevance Placement**: Preserve reverse chronological experience order unless Aryan explicitly requests a different ordering. Make the role fit visible through the professional summary, technical skills, project selection, and the first 1-2 bullets inside relevant roles rather than moving older roles above newer roles.
- **Mirror Qualification Hierarchy**: Mirror required qualifications first, then preferred qualifications. Required degree, location/eligibility constraints, core language requirements, and must-have tools should be visibly covered before nice-to-have tools.
- **Avoid Keyword Stuffing**: Do not repeat keywords without a defensible context. Hidden text and repetitive keyword blocks are prohibited because they damage readability, credibility, and parser quality.
- **Keyword Quality Filter**: Prioritize exact titles, required tools, required languages, frameworks, databases, cloud/devops tools, responsibilities, and domain terms. Do not force company slogans, legal boilerplate, equal-opportunity language, vague soft skills, or internal organization names into the resume unless they naturally describe Aryan's evidence.
- **Expanded Keyword Audit**: The default keyword analyzer is a deterministic helper, not a complete ATS model. For each application, create an expanded role-specific keyword list from the full JD, including exact variants and punctuation/casing used by the employer (for example `Springboot` vs. `Spring Boot`, `Open Shift` vs. `OpenShift`, or `Jenkins pipeline`). Record the expanded match result in `tailoring-notes.md` and explain which missing terms are harmless variants, truthful additions to make, or unsupported claims to omit.
- **Adjacent Evidence**: Include adjacent truthful technologies only as supporting evidence, not as substitutes.
- **After Compiling Verification**: Extract resume text with `pdftotext` and scan it as an ATS would: confirm exact role title, required languages, cloud/platform terms, and top responsibilities appear in readable order. When `pdftotext -bbox` is available, use it or the package validator to detect whether meaningful text stops too far above the bottom of the page.

Use this scoring model only as the internal `Job Alignment & Evidence Score`, not as a guarantee or prediction of an employer's ATS result. The score must be reproducible from a written breakdown; do not record only a naked number.

- **Keyword coverage**: 40 points for truthful coverage of important job-title, skill, tool, platform, methodology, and domain keywords.
- **Experience relevance**: 25 points for how strongly the selected experience/projects match the role's responsibilities and business context.
- **Impact and evidence**: 15 points for quantified scope, concrete outcomes, and action + technology + impact bullets.
- **Formatting and ATS parsing**: 10 points for one-page PDF, readable layout, extractable text, standard headings, and no graphics/tables that break parsing.
- **Risk and gap handling**: 10 points for avoiding unsupported claims, identifying important missing skills, and flagging eligibility/location constraints.

Record the score in `tailoring-notes.md` with:

- `## Scoring Methodology`
- `Job Alignment & Evidence Score: X/100`
- `Internal estimate only; not a predicted ATS score.`
- `Score breakdown` with exact point allocations for keyword coverage, experience relevance, impact/evidence, formatting/ATS parsing, and risk/gap handling
- `Exact posted title matched in visible summary/title/header clause`, or `Waived - <reason>` when Aryan requests a cleaner adjacent title or the exact posted title would overclaim unsupported specialization/seniority
- `Strong matches`
- `Gaps / intentionally omitted unsupported keywords`
- `Recommended improvements`
- `Sub-90 Readiness Waiver` when the score is below `90/100`

Do not inflate the score by adding unsupported keywords. A lower truthful score is better than a higher score built on claims Aryan cannot defend. The written `Score breakdown` must sum exactly to the recorded score and to 100 possible points; if a later edit changes coverage, recompute the score before finalizing. If an external or open-source scorer is used, record the tool name, version or commit, configuration, extracted resume text input, job-description input, and score output. Do not call an external scorer an employer ATS result.

## Cover Letter Rules

- Keep cover letters specific to the company and role.
- Use verified personal context already in `profile/` and targeted user-provided context. Do not open prior application notes for normal cover-letter drafting unless Aryan explicitly names a specific prior package. Ask Aryan about personal connection, motivation, or desired impression only when the letter would be materially weaker or risky without the answer.
- Reuse verified facts from `profile/`.
- Avoid generic filler, flattery, and unsupported claims (e.g., "perfect fit," "passionate about coding").
- Do not mention F-1, OPT, STEM OPT, visa status, future sponsorship, E-Verify, Form I-983, or work-authorization risk in the submitted cover letter unless Aryan explicitly asks.
- Do not volunteer gap/confession language such as `I have not worked directly with...` unless the gap is an obvious central requirement and a concise adjacent-evidence reframing is stronger than silence. Keep unsupported-keyword and missing-requirement analysis in `tailoring-notes.md`.
- Keep submitted-facing terminology synchronized with the resume. If internal wording is translated or de-jargoned in the resume, update the cover letter to use the same recruiter-readable product/system language.
- Emphasize the strongest match between the job description and Aryan's experience.
- Map the cover letter to the job description using **one or two deep technical proof points** showing how Aryan solved a similar problem, rather than rehashing the resume in paragraph format.
- Prefer confident, direct, warm language over exaggerated language.
- Use the cover letter to add context, motivation, judgment, and personal fit.
- Keep the cover letter to one page using the canonical cover-letter layout: 11-point Computer Modern text, approximately 0.80-inch left/right margins and 0.70-inch top/bottom margins, the same name/contact hierarchy used across application letters, and no decorative graphics.
- Use a concise opening, one or two evidence paragraphs, and a short closing; three or four short paragraphs are normally appropriate. Do not impose a two-paragraph limit when it harms clarity.
- For job submission, produce a PDF or DOCX cover-letter artifact, not only a Markdown draft.
- Follow the employer's requested file type and naming instructions. Use PDF by default only when the application accepts it; use DOCX when specifically requested.
- Keep `resume.pdf` under a conservative 2.5 MB parser target and keep final resume/cover-letter submission artifacts under 5 MB unless the employer explicitly allows a larger file. This keeps artifacts compatible with common ATS upload and parsing constraints.
- Match the resume's typography and professional visual identity without adding graphics or decorative elements.
- **Cover-Letter Consistency Gate**: Reuse the canonical cover-letter preamble, header, date/addressee order, paragraph spacing, salutation, and signature treatment from `master-documents/master-cover-letter/` or an approved canonical template. Do not read prior cover-letter packages solely for visual comparison. Company-specific content may change; the visual system should not.
- Use a warm, professional, human tone.
- Mention company-specific research and personal connection when truthful.
- Treat AI-assisted writing as a drafting and revision aid only. Manually edit every letter for specific details, natural voice, factual accuracy, and employer relevance; never submit generic generated prose.

Good cover letters should:

- Explain why this company and role are specifically interesting.
- Connect Aryan's strongest matching experience to the employer's needs.
- Add a personal or human detail when available.
- Show evidence through short examples rather than broad self-praise.
- Stay concise, specific, and easy to read.

Cover-letter guidance incorporated from a 2026 web check:
- Yale Office of Career Strategy: tailor each letter to a specific job, connect skills to employer needs, use job-description keywords truthfully, write in confident active language, keep it to one page, and use a clear opening/body/closing structure.
- Purdue OWL: use the cover letter to explain experience in a story-like format, go deeper on relevant skills, relate those skills to job requirements, show individualized tailoring, and demonstrate written communication quality.

## Resume And Cover-Letter Standards Maintenance

Treat these rules as evidence-based operating standards, not timeless folklore. Employer instructions for a specific application override repository defaults for file type, page length, requested sections, and naming conventions.

When changing the governing resume or cover-letter rules:

1. Prefer current primary or institutionally accountable sources: employer/ATS documentation, NACE or SHRM research, LinkedIn Talent Solutions labor-market research, and established university career centers.
2. Do not use anonymous resume blogs, affiliate sites, keyword-stuffing advice, or unsupported claims about universal ATS behavior as policy evidence.
3. Separate parser compatibility, recruiter readability, job alignment, and personal repository preferences; do not present one category as proof of another.
4. Record the research date and material rule changes in the relevant guide or commit message.
5. Recheck the standards at least annually or when major ATS/employer guidance changes.

The July 2026 standards audit used guidance from Greenhouse, NACE, SHRM, LinkedIn Talent Solutions, MIT CAPD, Harvard Career Services, Yale Office of Career Strategy, UC Berkeley Career Engagement, the University of Michigan Career Center, and Purdue OWL.

The July 16, 2026 bullet-quality audit used Harvard Career Services, Yale Office of Career Strategy, and NACE guidance to strengthen the experience/project bullet rules around individual contribution, evidence-backed skills, project purpose and result, metric context, interview defensibility, and manual cleanup of AI-assisted bullet drafts.

The July 20, 2026 enforcement audit used Greenhouse Support, Lever Developer documentation, Workday Developer documentation, UC Berkeley Career Engagement, Harvard Mignone Center for Career Success, MIT CAPD, University of Michigan Career Center, and NACE guidance to tighten ATS-safe source checks, bottom-page utilization checks, bullet-audit documentation, and the distinction between recruiter-readable white space and an underfilled one-page resume.

The July 20, 2026 supplemental evidence audit added Lever Help Center, Workday Resume REST API documentation, Oracle Taleo attachment documentation, SAP SuccessFactors Recruiting documentation, iCIMS developer documentation, University of Pennsylvania Career Services, MIT CAPD cover-letter guidance, UC Berkeley cover-letter guidance, and NACE Job Outlook 2026 guidance. The resulting hard rules require parseable text PDFs or employer-requested DOCX files, no image-based resumes, canonical source validation, no blank verification gates, no placeholder text, no weak bullet openers, and a conservative 5 MB final artifact size unless employer instructions override it.

The July 22, 2026 title-keyword audit used Greenhouse Talent Filtering, Greenhouse resume parsing documentation, MIT CAPD resume guidance, Yale Office of Career Strategy guidance, University of Michigan Career Center guidance, and Harvard Mignone Center resume guidance to add the Target Professional Title Clause and two-sentence Professional Summary rules. Those rules were superseded by the Aug. 20, 2026 audit for early-career application resumes: the employer's exact posted role title should still appear once in truthful visible resume text, but a concise contact/title-line placement is preferred when the Professional Summary is omitted. The title must stay free of fake past titles, hidden text, keyword stuffing, generic buzzwords, and unsupported seniority/title inflation.

The July 23, 2026 F-1 work-authorization audit used USCIS practical training guidance, DHS Study in the States STEM OPT/Form I-983 guidance, university employer guides for hiring international students, and sponsor-history database guidance to add the F-1 Work Authorization Gate. The gate prioritizes OPT/STEM OPT/E-Verify/sponsorship-compatible roles and prevents no-sponsorship or independent-work-authorization blocker postings from entering the strict shortlist.

The July 24, 2026 scoring and layout enforcement audit used open-source/current scoring references including SkillVector, Resume Radar, Resume Matcher, OpenCATS, and `@pranavraut033/ats-checker`. The rule update added hard validator checks for Professional Summary visual line count, an experience-bullet floor, and point-by-point score methodology documentation. The current repo score remains an internal readiness score; future adoption of an open-source scorer should prefer deterministic, explainable tools with pinned versions, local inputs, recorded configuration, and no claims that the output predicts an employer ATS decision.

The Aug. 20, 2026 Disney Software Engineer I pipeline audit tightened the practical application of those standards: Professional Summary is now omitted by default unless it adds clear scan value, exact posted titles should use concise visible title/header text instead of awkward `-aligned` wording, current/private-role evidence must be debloated into product/system/outcome bullets, obscure internal terms must be translated for human recruiter readability, submitted resume and cover-letter terminology must stay synchronized, and the written Job Alignment & Evidence Score must match its point-by-point breakdown.

The Aug. 21, 2026 ATS standards audit rechecked current Greenhouse, Workday, Oracle Taleo, iCIMS, MIT CAPD, UC Berkeley, University of Michigan, Yale, and Harvard guidance. The resulting pipeline changes strengthened text-based PDF/DOCX handling, added a conservative 2.5 MB resume parser-size check, blocked hidden/color/transparent-text keyword tricks, removed validator requirements that forced specific employer names into every resume, and refreshed templates/source material so future packages inherit the recruiter-readable header/title and internal-term translation rules.

## Job Search & Discovery Strategies (Getting Ahead of the Line)

To maximize callback rates, Aryan needs to apply to roles extremely quickly—ideally within 24 to 48 hours of posting. The Job Discovery pipeline helps achieve this using a layered approach:

1. **Standard Pipeline Command**: Use `python3 job-search/src/job_discovery.py run-pipeline` as the default job-discovery command. It should run the configured discovery layers, group outputs by posted-time windows, and update `jobs-inbox.csv` only with strict shortlist matches.
2. **Persistent Scan History**: Let the standard pipeline update `job-search/data/scan-history.tsv` so repeated runs preserve first-seen and last-seen timestamps, identify previously seen postings, and avoid treating every pull as newly discovered.
3. **Direct ATS Feeds**: Keep `job-search/config/direct-ats-targets.json` updated with company tokens. The standard pipeline pulls structured postings directly from Greenhouse, Lever, Ashby, and SmartRecruiters targets.
4. **Recent Google Search Queries**:
   - Run `generate-queries` to output search links for target roles and domains.
   - Use Google Search operators for 6-hour, 12-hour, 24-hour, and 48-hour windows (`qdr:h6`, `qdr:h12`, `qdr:d`, and `qdr:d2`) to find freshly indexed postings on company portals before they are listed on major job boards.
5. **Domain Verification**: When paste-url discovery yields new Greenhouse/Lever/Ashby/SmartRecruiters URLs, run `discover-direct-ats-targets` to verify them and update the config file automatically.
6. **Location Scope**: Default job discovery should prioritize U.S.-based and U.S.-remote roles. India-based roles should appear in review reports by default. Other non-U.S./non-India roles should be excluded from the standard pipeline unless Aryan explicitly asks for broader international review.
7. **Inbox Maintenance**: Regularly check `job-search/jobs-inbox.csv`. Keep it minimal (only company, position, posted_at, pulled_at, and url). Move approved roles into the Application Package Generation pipeline.

## Verification

After approved resume changes:

1. Compile the LaTeX file with `pdflatex -interaction=nonstopmode -halt-on-error resume.tex`.
2. Confirm the PDF page count with `pdfinfo resume.pdf`. It must be exactly 1 page.
3. Confirm `resume.pdf` is text-based, extractable, and under the conservative 2.5 MB parser target.
4. Confirm the resume uses the canonical 11-point application layout and standard geometry, bullet symbols are consistent, and the source contains no `tabular`, `tabular*`, images, icons, text boxes, color/transparent text, or hidden keyword tricks.
5. Extract text with `pdftotext resume.pdf -` and confirm contact details, headings, dates, roles, and bullets appear in the intended reading order.
6. If `pdftotext -bbox resume.pdf -` is available, confirm the bottom unused area is only a small finishing margin, not merely below the validator's hard failure threshold. If verified role-aligned evidence can fit cleanly, close the gap before marking page utilization as passed. A substantially underfilled page fails unless `tailoring-notes.md` explains that no additional verified role-aligned evidence should be added.
7. Render the resume and inspect it against the canonical application-resume visual system for border consistency, name/contact placement, section styling, bullet appearance, role/date hierarchy, density, bottom-page usage, clipping, and overlap. A visibly inconsistent, sparse, or fillably underused bottom area fails this check even when the automated validator passes.
8. Run `python3 automation/analyze_application_keywords.py application-packages/<Company>/<Role>` and use the exact-term report to identify missing truthful keyword opportunities and unsupported keywords that should stay omitted. Then run or document an expanded role-specific keyword audit using important JD terms not covered by the default helper. Do not record a small default denominator such as `20/20` as if it means the resume covers every important term in the posting.
9. Run the resume-vs-job-description alignment pass and record the Job Alignment & Evidence Score, score methodology, point-by-point breakdown, and its internal-estimate disclaimer in `tailoring-notes.md`.
10. Confirm mandatory qualifications and the highest-priority truthful keywords appear in evidence-bearing context; record unsupported requirements as gaps rather than adding them.
11. Confirm the employer's exact posted role title appears once in visible resume text through a truthful Target Professional Title Clause, and that the title is supported by nearby experience or project evidence rather than repeated as a disconnected keyword.
12. Confirm the Professional Summary, when used, renders as no more than two PDF text lines. Rewrite or omit it if it renders as three lines or repeats skills already visible below.
13. Confirm bullets are recruiter-readable without internal ticket/tool context and that private-source details have been translated into public-safe product/system language.
14. Confirm the Experience section normally contains at least 11 strong bullets; if it does not, add verified role-aligned evidence or document an `Experience Bullet Count Waiver`.
15. Confirm `tailoring-notes.md` records `Pass` for `ATS source gate checked`, `Visual consistency gate checked`, `Human recruiter readability gate checked`, `Submitted-facing terminology sync checked`, `Score consistency gate checked`, `Cover-letter artifact checked`, and `Pass` or `Waived - <reason>` for `Page utilization gate checked`.
16. Run `python3 automation/validate_application_package.py application-packages/<Company>/<Role>` and address any failures.
17. Report changed files, verification results, validator result, and the Job Alignment & Evidence Score with the disclaimer that it is not a predicted ATS result.
18. Remove generated LaTeX build artifacts. Keep submission PDFs only when Aryan asks for final application artifacts or when the application package needs a ready-to-submit PDF.
