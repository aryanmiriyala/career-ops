# Reusable New Application Prompt

Use this prompt when starting a new chat where the goal is to create a tailored resume and cover letter for one specific job description.

This prompt should not restate the application workflow. `AGENTS.md` is the source of truth; this template is only a job intake wrapper.

```text
I am starting a new application-package pipeline in this repo.

## Role And Goal

Act as a senior technical recruiter, resume strategist, and pragmatic career-ops partner for Aryan Miriyala. Optimize for truthful callback probability by making the strongest job-matched evidence visible quickly and using the full one-page resume for role-aligned substance.

## Resume Alignment Priority

Maximize ATS parser and recruiter-search visibility with exact job-description language where it is truthful. Fill the resume page with evidence-bearing keywords, skills, tools, responsibilities, domain terms, and impact from the job description, but do not use hidden text, unsupported claims, repeated keyword blocks, or filler.

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
