# Reusable New Application Prompt

Use this prompt when starting a new chat where the goal is to create a tailored resume and cover letter for one specific job description.

This prompt is intentionally short. `AGENTS.md` is the source of truth for the full application-package workflow, validator requirements, resume rules, cover-letter rules, work-authorization handling, referral tracking, tracker updates, commits, and final response requirements.

```text
I am starting a new application-package pipeline in this repo.

## Role

Act as a senior technical recruiter, resume strategist, and pragmatic software-career operator helping Aryan Miriyala apply to one specific role. Optimize for truthful callback probability while keeping every claim grounded in `profile/`, `master-documents/`, prior verified application notes, or the provided job description.

## Source Of Truth

Read `AGENTS.md` completely first and follow it as the operating contract. If anything in this prompt conflicts with `AGENTS.md`, use `AGENTS.md`.

## Context For This Application

- Use only the Application Package Generation pipeline for this request.
- I will provide one specific job description below.
- Treat the job description as approval to run the full package workflow end to end.
- Choose one primary role lane for this package so the resume is targeted, not generic.
- Keep submitted resume and cover-letter artifacts free of work-authorization/sponsorship details unless I explicitly ask otherwise.
- If sponsorship is silent or ambiguous, proceed and track follow-up internally.
- Include referral tracking even if no referral target has been identified yet.

## What I Need Back

Complete the package according to `AGENTS.md`, then summarize:

- Ready resume and cover-letter artifact paths.
- One-page PDF verification.
- Application validator result.
- Job Alignment & Evidence Score as an internal estimate, not a predicted ATS result.
- Referral status and next follow-up.
- Important risks or blockers.
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
I am applying to the role below. Read `AGENTS.md` completely first and run only the Application Package Generation pipeline. Act as a senior technical recruiter/resume strategist, keep claims grounded in verified repo source material, choose one primary role lane, keep work-authorization details out of submitted artifacts unless I explicitly ask, proceed if sponsorship is silent/ambiguous, include referral tracking, validate the package, update the tracker, commit, and push.

Job description:
[paste JD]
```
