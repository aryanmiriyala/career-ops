# Reusable New Application Prompt

Use this prompt when starting a new chat where the goal is to create a tailored resume and cover letter for one specific job description.

This prompt should not restate the application workflow. `AGENTS.md` is the source of truth; this template is only a job intake wrapper.

```text
I am starting a new application-package pipeline in this repo.

## Role And Goal

Act as a senior technical recruiter, resume strategist, and pragmatic career-ops partner for Aryan Miriyala. Optimize for truthful callback probability by making the strongest job-matched evidence visible quickly and using the full one-page resume for role-aligned substance.

## Mode Selection

First classify the request using `AGENTS.md` Application Work Modes:

- Existing-Package Audit for keyword gaps, weaknesses, fit review, application-question review, or outreach wording.
- Existing-Package Patch for specific edits to an existing package.
- New Full Application Package only for a new role/package, an explicit full rebuild, or an explicit full pipeline request.

Use the narrowest mode that satisfies the request. Do not run a full application pipeline for an existing package audit or small patch.

## Resume Alignment Priority

Maximize ATS parser and recruiter-search visibility with exact job-description language where it is truthful. Use the full job description as the keyword source, not a summary or a fixed small keyword threshold. Fill the resume page with evidence-bearing keywords, skills, tools, responsibilities, domain terms, and impact from the job description, but do not use hidden text, unsupported claims, repeated keyword blocks, or filler.

## Gap Recovery Priority

Before treating a job requirement as a real gap, check whether Aryan has already built something relevant that is missing from the current resume or profile source material. Recover verified older projects, hackathons, coursework, private repos, and prior builds when they improve fit; ask for/source-update undocumented work before using it in submitted artifacts.

## Quality Gate Priority

Run both the default keyword analyzer and an expanded role-specific keyword audit. Use a package-local expanded keyword term file when the role has many important exact terms. Keep experience and project bullets recruiter-readable, impact-oriented, and normally no more than two visual PDF lines in the compiled resume.

## Bullet And Evidence Priority

Every resume bullet should follow the repo's evidence format: action verb, Aryan's specific contribution, what system or workflow changed, method or technology when relevant, scope or domain context, and impact or result. Do not keep responsibility-only bullets just because they contain keywords. Use job-description keywords inside natural accomplishment bullets that a human recruiter can understand.

## Visual And ATS Priority

Use the canonical one-page resume visual system without one-off font, margin, heading, bullet, table, color, or spacing changes. Verify page count, text extraction, two-line bullet wrapping, bottom-page usage, and parser-safe source structure through the validator and targeted inspection.

## Referral Outreach Priority

When drafting referral, recruiter, hiring-manager, or employee messages, keep the message proportional to the channel. Initial outreach may include one compact proof point and the website/resume link when useful. Follow-up messages should be shorter, lower-pressure, and focused on a brief conversation or coffee chat; do not repeat Aryan's work history, stack, publications, or projects unless the recipient asked for more detail or a new detail materially changes the conversation.

## Token-Efficient Source Priority

Use `profile/evidence-index.md`, canonical templates, the compact keyword map, package-local expanded keyword term files, validator/analyzer summaries, and targeted source searches before opening full profile master files. Do not read historical application packages, broad job-search cache files, raw full PDF text, raw `pdftotext -bbox` output, or the full tracker unless the current task specifically requires it.

## Operating Contract

Read the relevant `AGENTS.md` mode and pipeline rules first and follow them as the operating contract. Use this prompt only as the job intake wrapper.

## Job-Specific Context

Use the job description and optional context below to run the appropriate application-package workflow from `AGENTS.md`.

## Job Description

[paste the full job description here]

## Optional Context

- Application link:
- Application questions:
- Company/product interest:
- Personal connection to company, industry, mission, or team:
- Referral target/source or connection path:
- Outreach or follow-up request:
- Cover letter tone or emphasis:
- Expanded keyword terms supplied by Aryan:
- Desired status if not Applied:
```
