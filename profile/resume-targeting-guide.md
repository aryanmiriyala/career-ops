# Resume Targeting Guide

Use this guide when tailoring a resume to a specific company and role. Apply the rules in `profile/ats-recruiter-resume-guide.md` throughout the process.

## Step 1: Parse the Job Description

Extract:

- Exact posted job title
- Required languages
- Required frameworks
- Cloud requirements
- Data requirements
- AI/ML requirements
- Security/auth requirements
- Domain context
- Repeated keywords
- Nice-to-have skills
- Recruiter-screen responsibilities
- ATS-critical exact terms

Save the posting in `application-packages/<Company>/<Role>/job-description.md`.

## Step 2: Select the Resume Angle

Choose one primary angle:

- Software engineering / full-stack engineering
- Data engineering
- Applied AI / agentic systems engineering
- Data analyst / business analyst
- Product analyst / operations analyst
- Cloud, platform, or enterprise systems engineering
- Security, IT, technical support, or support-adjacent engineering
- Healthcare, insurance, education, or enterprise workflow technology
- Other adjacent early-career technical roles

Choose one secondary angle if useful.

Broaden the role search without sending a generic resume. Each package should still choose one primary lane and tune the summary, experience order, project selection, skills categories, and cover-letter proof points to that lane. For analyst and adjacent roles, emphasize SQL, Python, data profiling, reporting-ready datasets, stakeholder workflows, documentation, operational context, and business impact before lower-level implementation detail.

## Step 2A: Work Authorization And Referral Intake

Before drafting submitted artifacts, classify the posting:

- `Proceed - posting silent/ambiguous`: the posting does not explicitly block F-1/OPT/STEM OPT or future sponsorship. Proceed and track follow-up internally.
- `Proceed - confirmed compatible`: the posting or company research supports CPT/OPT/STEM OPT, E-Verify, sponsorship, or international-student hiring.
- `Blocker - explicit incompatibility`: the posting explicitly says no visa/work-visa sponsorship, no current/future sponsorship, independent permanent work authorization, authorization to work for any employer, U.S. citizen/permanent resident only, incompatible clearance, or another direct conflict.

Do not mention F-1, OPT, STEM OPT, E-Verify, Form I-983, visa status, or sponsorship needs in the resume or cover letter unless Aryan explicitly asks. Keep those details in `tailoring-notes.md` and the new or updated tracker row. Do not read the full tracker solely to record these details for a new application.

Record referral status for every package:

- Referral target or source, if known.
- Connection path, such as alumni, employee, recruiter, professor, prior intern, founder, hiring manager, or mutual contact.
- Outreach status and next follow-up date.
- Whether a referral was requested, submitted, declined, or unavailable.

## Step 2B: Gap Recovery Gate

Before treating a job requirement as unsupported, check whether Aryan has already built something relevant that is missing from the current resume, skills list, project summaries, or reusable bullets.

Use the project routing cache in `profile/evidence-index.md` before opening the full project master. For any important JD term that is not already covered by the planned resume evidence, run targeted `rg` searches across `profile/`, `master-documents/`, and relevant project repositories before classifying the term as unsupported.

For each important missing requirement, preferred skill, tool, domain term, or responsibility:

- Mark `Supported - add/use now` when verified source material already proves it. Add it to the resume, cover letter, skills section, or tailoring notes when it improves role fit.
- Mark `Likely built but undocumented - ask/update source` when Aryan may have built it but current repo source material does not prove it. Do not use it in submitted artifacts until Aryan confirms it and the relevant `profile/` or project source material is updated.
- Mark `Unsupported - omit` when there is no verified evidence or the claim would be misleading.

Use this gate to recover older projects, hackathons, coursework, private repos, local repositories, and prior builds that might not be visible in the current one-page resume. Record the searched terms, searched locations, decision, and selected evidence in `tailoring-notes.md` so future packages know whether the gap was filled, needs source-material work, or should stay omitted.

## Step 3: Decide Whether to Use a Professional Summary

Use a summary when the job benefits from connecting multiple parts of Aryan's background in the first recruiter scan, especially for software roles that also value applied AI, healthcare, cloud/data engineering, full-stack systems, or cybersecurity.

Rules:

- Keep the summary to two sentences maximum and no more than two rendered PDF lines total. Prefer one tight sentence when the fit is obvious.
- Keep each sentence concise enough to scan quickly; do not write paragraph-style summaries.
- Make it role-specific and grounded in the job description's language.
- Include the exact posted job title once in visible summary text when truthful, using a non-misleading clause such as `<Exact Job Title>-aligned software engineer with...` or `Software engineer aligned with <Exact Job Title> responsibilities through...`.
- Lead with what Aryan brings: systems built, domains worked in, and technical strengths.
- Do not write an objective statement.
- Do not rewrite Aryan's actual past job titles, invent seniority, or repeat the posted title as a disconnected keyword.
- Do not turn the summary into a skills dump. Use only the 2-4 strongest job-description terms that are supported by bullets below.
- Do not use the summary to compensate for weak bullet alignment. The experience and project bullets still need to prove the fit.

## Step 4: Select Experience Bullets

Use `profile/evidence-index.md` first, then open `experience-master.md` and `bullet-bank.md` only for exact wording, source verification, or job-specific gaps not covered by the index.

Rules:

- Start from the `Platform-Ready Description` in `experience-master.md` when writing LinkedIn experience sections, cover-letter context, or expanded application material.
- Use the `Handshake Description` in `experience-master.md` for Handshake experience entries; keep it at or below 500 characters and do not paste the longer platform-ready version into Handshake.
- Use `Reusable Bullet Options` from `experience-master.md` when the application needs company/role-specific bullets.
- Use `bullet-bank.md` when the application needs job-family bullets across multiple roles.
- Treat Actual Reality Technologies as Aryan's current role. Use verified customer-portal evidence from `profile/experience-master.md` when it improves fit, especially Next.js/TypeScript, Firebase, Plane integration, auth/session work, dashboard status logic, Vitest tests, and customer/admin workflows. Keep private customer/client details out of submitted artifacts unless Aryan explicitly confirms they are public-safe.
- Prefer bullets matching the job's required stack.
- Build experience depth before project breadth. The Experience section should normally contain at least 11 strong, role-aligned bullets on early-career one-page application resumes; fewer requires an `Experience Bullet Count Waiver` in `tailoring-notes.md`.
- Put job keywords into bullets only when supported by real experience.
- Preserve internship roles by default. A weakly relevant internship may be compressed or omitted when it would displace substantially stronger evidence or force unreadable formatting; record the decision in `tailoring-notes.md`.
- Do not impose a fixed bullet maximum or require matching bullet counts across roles. Let the number of distinct, job-relevant accomplishments determine the count, subject to one-page readability.
- Audit each selected bullet against the formula: action verb + what changed + technology/method + scope/domain + impact/result.
- Rewrite, combine, or remove any bullet that does not provide a clear contribution, defensible context, and result; never retain a weak bullet for visual symmetry.
- When the resume is underfilled, add evidence by quality order: a stronger verified experience bullet, a deeper project bullet explaining purpose/method/result, a missing truthful must-have keyword in context, or a compact skills category. Do not add filler, duplicate claims, broad soft-skill labels, or unsupported technologies just to occupy space.
- Keep the most recent experience strong.
- Do not force unrelated skills into a bullet.
- Do not invent metrics.
- Keep bullets concise enough for one page.
- Preserve enough technical detail for a human reviewer to understand the work. If the section gets tight, adjust layout before removing the strongest truthful details.

## Step 5: Select Projects

Use `profile/evidence-index.md` first, especially its project routing cache, then open `projects-master.md` only for exact wording, source verification, or job-specific gaps not covered by the index.

Rules:

- Select projects by matching the JD's highest-priority technologies, domain terms, and proof style against the project routing cache before reading expanded project sections.
- Start from each project's `Platform-Ready Description` for LinkedIn, portfolios, cover letters, or expanded project sections.
- Use each project's `Handshake Description` for Handshake project entries; keep it at or below 500 characters and preserve the most important stack, problem, and outcome.
- Use `Tech Stack`, `Positioning Angles`, and `Reusable Bullet Options` to select only the project details that match the role.
- Projects support the resume angle after experience has been protected. Include fewer projects with stronger job-aligned bullets instead of cutting internship experience to fit more projects.
- For AI roles, prioritize Travel Health Advisor - BGSU Hackathon 2025 and RocketGrader.
- For full-stack roles, include both projects if space allows.
- For data-heavy roles, consider reducing project bullets to preserve room for AAIS data engineering.
- For security/platform roles, emphasize Auth0, RBAC, JWT, SSO, PII tokenization, and AWS.
- Avoid duplicate project entries. If two names refer to the same repository or product, consolidate them under one canonical project.
- Ground project claims in repository files and implementation details, not only README language.
- For software, data, AI, and analyst roles, prefer projects with proof of real execution quality: deployment or runnable setup, tests or validation checks, logging/observability when available, error handling, evaluation methodology, source-grounding, reproducible data flows, dashboards/reports, or clear business/user impact.

## Step 6: Tune Technical Skills

Use `profile/evidence-index.md` and `skills-master.md`. Open the full skills master only when the evidence index does not settle a required or preferred tool.

Rules:

- Include skills that appear in the job description and are supported by experience.
- Prefer exact job-description wording for tools and frameworks when truthful.
- Put the most relevant categories first.
- Keep the skills section compact.
- Avoid listing technologies that distract from the target role.
- List actual tools, languages, platforms, frameworks, libraries, and technical methods. Do not list broad work activities as skills unless they are expressed as concrete technical capabilities.

## Step 7: Verify Output

After approval and edits:

- Compile LaTeX.
- Confirm the resume PDF is exactly one page.
- Extract PDF text and inspect bullets.
- Run `python3 automation/analyze_application_keywords.py application-packages/<Company>/<Role>` after the resume artifact exists and use its exact-term report during the alignment pass.
- Confirm the exact posted job title appears once in visible summary/title text and is supported by evidence-bearing experience or project bullets.
- Confirm the Professional Summary is no more than two sentences, concise, and written in the job description's language without becoming a keyword list.
- Confirm the PDF text preserves section order and important keywords.
- Visually inspect the PDF for readability, spacing, cramped sections, canonical layout consistency, and bottom-page usage. A large unused bottom band fails this step when verified role-aligned evidence is still available.
- If the resume is too long, first tighten wording, remove repetition, and prioritize stronger evidence. Keep the canonical application-resume geometry and 11-point typography unchanged rather than creating application-specific spacing.
- Save tailoring notes.
