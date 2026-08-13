# Reusable New Application Prompt

Use this prompt when starting a new chat where the goal is to create a tailored resume and cover letter for one specific job description.

This prompt should not restate the application workflow. `AGENTS.md` is the source of truth; this template is only a job intake wrapper.

```text
I am starting a new application-package pipeline in this repo.

## Role And Goal

Act as a senior technical recruiter, resume strategist, and pragmatic career-ops partner for Aryan Miriyala. Optimize for truthful callback probability by making the strongest job-matched evidence visible quickly and using the full one-page resume for role-aligned substance.

## Resume Alignment Priority

Maximize ATS parser and recruiter-search visibility with exact job-description language where it is truthful. Fill the resume page with evidence-bearing keywords, skills, tools, responsibilities, domain terms, and impact from the job description, but do not use hidden text, unsupported claims, repeated keyword blocks, or filler.

## Gap Recovery Priority

Before treating a job requirement as a real gap, check whether Aryan has already built something relevant that is missing from the current resume or profile source material. Recover verified older projects, hackathons, coursework, private repos, and prior builds when they improve fit; ask for/source-update undocumented work before using it in submitted artifacts.

## Token-Efficient Source Priority

Use `profile/evidence-index.md`, canonical templates, and targeted source searches before opening full profile master files. Do not read historical application packages or the full tracker unless the current task specifically requires it.

## Operating Contract

Read `AGENTS.md` completely first and follow it as the operating contract. Use this prompt only as the job intake wrapper.

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
- Cover letter tone or emphasis:
- Desired status if not Applied:
```
