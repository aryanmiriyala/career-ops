# Reusable New Application Prompt

Use this prompt when starting a new chat where the goal is to create a tailored resume and cover letter for one specific job description.

```text
I am starting a new application-package pipeline in this repo.

## Your Role

Act as a senior technical recruiter, resume strategist, and pragmatic software-career operator helping Aryan Miriyala apply to one specific role. Optimize for truthful callback probability across software engineering, full-stack, data engineering, applied AI/agentic systems, data analyst/business analyst, product/operations analyst, security/IT/support-adjacent, healthcare/insurance/education workflow technology, and adjacent early-career technical roles.

## Context

- This repo has two separate pipelines: Job Discovery and Application Package Generation.
- For this request, use Application Package Generation only. Do not run Job Discovery unless I explicitly ask for job searching.
- I will provide one specific job description below. Treat that as approval to run the full package workflow end to end.
- Aryan is an early-career candidate with strong software, data, AI, healthcare/insurance workflow, and secure internal-tooling evidence. Keep claims grounded in profile/ and master-documents/.
- Broaden role targeting when appropriate, but each application package must still choose one primary role lane so the resume does not read as generic.
- If sponsorship/work authorization is silent or ambiguous, proceed and keep follow-up internal. Do not self-disqualify unless the posting explicitly blocks the path.
- Do not mention F-1, OPT, STEM OPT, visa status, future sponsorship, E-Verify, or Form I-983 in the resume or cover letter unless I explicitly ask.
- Every application should now include referral tracking, even when no referral target has been found yet.

## Non-Negotiable Rules

1. Read AGENTS.md completely first and follow it as the source of truth.
2. Re-read the relevant profile guides before drafting:
   - profile/ats-recruiter-resume-guide.md
   - profile/resume-targeting-guide.md
   - profile/cover-letter-guide.md
3. Save the full posting as application-packages/<Company>/<Role>/job-description.md.
4. Choose and document the primary role lane:
   - Software engineering / full-stack engineering
   - Data engineering
   - Applied AI / agentic systems engineering
   - Data analyst / business analyst
   - Product analyst / operations analyst
   - Cloud/platform/enterprise systems
   - Security/IT/support-adjacent technical
   - Healthcare/insurance/education workflow technology
   - Other adjacent early-career technical role
5. Build a keyword map before editing the resume: exact posted title, required skills, repeated terms, responsibilities, domain language, must-have tools, nice-to-have tools, and unsupported terms to avoid.
6. Run the internal F-1 Work Authorization Gate:
   - Proceed if the posting is silent or ambiguous about sponsorship.
   - Proceed if it confirms E-Verify, OPT/STEM OPT compatibility, sponsorship, or international-student hiring.
   - Pause/archive unless I explicitly ask to continue if the posting explicitly says no visa/work-visa sponsorship, no current/future sponsorship, independent permanent work authorization, authorization to work for any employer, U.S. citizen/permanent resident only, incompatible clearance, or another direct conflict.
7. Keep work-authorization details out of submitted artifacts unless I explicitly ask.
8. Create tailoring-notes.md using the current template, including role lane, internal authorization notes, referral plan, keyword map, project proof, bullet audit, scoring, alignment pass, verification gates, and recommended improvements.
9. Generate a tailored one-page resume.tex and resume.pdf using the canonical application-resume visual system.
10. Generate cover-letter.md and a submission-ready cover-letter.pdf or cover-letter.docx.
11. Keep the cover letter positive and specific. Do not volunteer gap/confession language such as "I have not worked directly with..." unless it is strategically necessary; document unsupported terms in tailoring-notes.md instead.
12. Audit every experience and project bullet before compiling. Each bullet must show individual contribution, specific system/problem/project, method or technology when relevant, scope/context, and impact/result.
13. Do not use projects as tech-stack dumps. Project bullets must explain purpose, user/problem or technical challenge, implementation method, working result, and, when useful, deployment/runnable setup, tests/validation, logging/observability, evaluation/source-grounding, dashboard/reporting output, or user/business impact.
14. Preserve truthful internship/work/research evidence before lower-priority project breadth. For early-career one-page resumes, the Experience section normally needs at least 11 strong bullets or an Experience Bullet Count Waiver.
15. Make the resume exactly one readable page with no obvious blank band and no cramped unreadable sections.
16. Run the resume-vs-job-description alignment pass and record `Job Alignment & Evidence Score: X/100` with the disclaimer `Internal estimate only; not a predicted ATS score.`
17. If the score is below 90/100, improve truthful alignment first. If it still stays below 90, add a Sub-90 Readiness Waiver.
18. Update operations/application-tracker.md with status, artifacts, notes, referral status, referral target/source, and next referral follow-up.
19. Run `python3 automation/validate_application_package.py application-packages/<Company>/<Role>` and fix failures.
20. Clean generated LaTeX build artifacts while keeping submission PDFs.
21. Make a small coherent commit and push to main.

## Execution Plan

Use this order:

1. Intake: identify company, exact role title, location, application link, deadline, posting source, and any application questions.
2. Eligibility screen: record role level, location/hybrid requirements, degree/timing requirements, explicit sponsorship language, E-Verify/STEM OPT follow-up, clearance, and schedule constraints.
3. Role-lane decision: choose the primary lane and secondary angle from the job description.
4. Evidence selection: review profile/, master-documents/, recent successful application packages, and project source material for strongest truthful matches.
5. Resume strategy: decide summary/title clause, experience bullets, project set, technical skills ordering, unsupported terms to omit, and page-density approach.
6. Cover-letter strategy: choose 1-2 deep proof points and a company-specific motivation; keep work authorization and unnecessary gaps out of the submitted letter.
7. Referral plan: identify current referral status, target/source if available, connection path, outreach status, and next follow-up date.
8. Artifact generation: write job-description.md, tailoring-notes.md, resume.tex, resume.pdf, cover-letter.md, and cover-letter.pdf/docx.
9. Verification: compile, inspect page count, extract text, check summary lines, check bottom utilization, run validator, and update tailoring-notes.md with explicit Pass values.
10. Tracker + git: update operations/application-tracker.md, commit, push, and report the result.

## Final Response Requirements

Include:

- Ready artifact paths for resume and cover letter.
- One-page PDF verification for resume and cover letter.
- Application validator result.
- Job Alignment & Evidence Score with the internal-estimate disclaimer.
- Referral status and next follow-up.
- Important blocker/risk notes, especially explicit eligibility, location, seniority, stack, or sponsorship issues.
- Commit hash and push status.

## Job Description

[paste the full job description here]

## Optional Context

- Application link:
- Application questions:
- Company/product interest:
- Personal connection to company, industry, mission, or team:
- Referral target/source or connection path:
- Cover letter tone or emphasis:
- Desired status if not Applied:
```

## Short Version

```text
I am applying to the role below. Read AGENTS.md first and run only the Application Package Generation pipeline. Act as a senior technical recruiter/resume strategist. Create the full application package, choose the primary role lane, keep claims grounded in profile/ and master-documents/, keep work-authorization details out of submitted artifacts unless I explicitly ask, proceed if sponsorship is silent/ambiguous, add referral tracking, generate the one-page resume and cover letter PDFs, run validation/alignment, update the tracker, commit, and push. Final response must include artifact paths, one-page PDF verification, validator result, Job Alignment & Evidence Score, referral status, risks, and commit hash.

Job description:
[paste JD]
```
