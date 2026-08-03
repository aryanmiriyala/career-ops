# Reusable New Application Prompt

Use this prompt when starting a new chat where the goal is to create a tailored resume and cover letter for one specific job description.

This prompt should not restate the application workflow. `AGENTS.md` is the source of truth; this template is only a job intake wrapper.

```text
I am starting a new application-package pipeline in this repo.

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
