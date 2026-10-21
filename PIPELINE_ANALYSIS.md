# Career Ops Pipeline - Comprehensive Analysis & Improvement Plan

**Branch**: `pipeline-improvements` | **Date**: 2026-10-20

---

## Executive Summary

The repository has **two separate pipelines** that are well-architected but **not fully connected**:

| Pipeline | Status | Location | Key Strength |
|----------|--------|----------|--------------|
| **Job Discovery** | ✅ Production-ready | `job-search/` | Multi-layer ATS feeds, scoring, scan history, dedup |
| **Application Package Gen** | ✅ Near-production | `workspace_app/` | Evidence-grounded, BM25 retrieval, deterministic JD parser, validation gates |

**Critical Gap**: No automated bridge from `jobs-inbox.csv` → intake → generation run. User must manually copy JD and create intake.

---

## 1. Job Discovery Pipeline (`job-search/`) - Analysis

### Architecture (3 Layers)

```
┌─────────────────────────────────────────────────────────────────┐
│                    run-pipeline Command                         │
├──────────────┬──────────────────┬──────────────────────────────┤
│ direct-ats   │ broad-ats        │ public-search                │
│ (configured  │ (GH/Lev/Ashby/   │ (Arbeitnow, RemoteOK)        │
│  employer    │  Workday datasets)                            │
│  boards)     │                  │                              │
└──────────────┴──────────────────┴──────────────────────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │ jobs-inbox.csv   │  ← Minimal: company, position, posted_at, pulled_at, url
                    │ (shortlist only) │
                    └──────────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │ results/YYYY-MM-DD/│
                    │ pipeline/        │
                    │ ├─ jobs.csv      │
                    │ ├─ jobs-by-window.md
                    │ ├─ shortlist.md  │
                    │ ├─ review-candidates.md
                    │ └─ run-summary.md│
                    └──────────────────┘
```

### Strengths
- **Multi-source**: Direct ATS APIs (4 sources) + broad datasets (4 ATS) + public feeds (2)
- **Recency-aware**: 6h/12h/24h/48h windows, anchored to scan time not wall-clock
- **Deduplication**: `scan-history.tsv` tracks first_seen/last_seen by URL + identity_key
- **F-1/OPT filtering**: Sponsor watchlist, blocker detection, eligibility classification
- **Scoring**: Deterministic fit_score with role buckets, location policy, work auth signals
- **Config-driven**: Role buckets, filters, ATS targets, sponsor watchlist all in JSON configs

### Gaps & Issues

| Issue | Impact | Location |
|-------|--------|----------|
| **No auto-bridge to application pipeline** | Manual step: copy JD → create intake → start run | Missing glue code |
| **No scheduled/automated runs** | Must manually trigger `run-pipeline` | `scans.py` runs once per API call |
| **No job enrichment** | JDs not fetched automatically from URLs in inbox | `jobs-inbox.csv` has only URL, not full JD |
| **No company research** | No auto-fetch of company info, news, team, culture | Manual step for cover letter |
| **job-viewer.html** is static | No backend API integration for filtering/sorting | `job-viewer.html` loads CSV via fetch but no auth |
| **Broad ATS Workday support** | Workday API fragile, often blocked | `fetch_workday_company()` |
| **iCIMS/Workable/Oracle/SAP** | Marked as "adapter/backlog" - not implemented | `ats-sources.json` |
| **No resume→job matching** | Can't rank inbox by fit to *your* resume | One-way: job→score, not resume→job |

### Key Files
- `job-search/src/job_discovery.py` - 1800+ lines, main pipeline
- `job-search/config/` - role-buckets, filters, direct-ats-targets, h1b-sponsor-watchlist
- `job-search/results/YYYY-MM-DD/pipeline/` - dated outputs
- `workspace_app/scans.py` - API wrapper for run-pipeline (dry-run only!)

---

## 2. Application Package Generation (`workspace_app/`) - Analysis

### Architecture (7-Stage Pipeline)

```
Intake (JD) ──▶ Requirements (JD Parser) ──▶ Evidence (BM25 Retrieval)
                                                            │
                                              Evidence Bank (YAML)
                                                            │
                                                           ▼
                              ┌─────────────────────────────────────────┐
                              │           Generation Engine             │
                              │  Resume → Cover Letter → Review → Repair│
                              │  Render (LaTeX→PDF) → Validate          │
                              └─────────────────────────────────────────┘
                                                            │
                                                           ▼
                                              Human Approval (Approval model)
                                                            │
                                                           ▼
                                              Package Published + Tracker Updated
```

### Strengths (Post Phase 1 Fixes)
- **Deterministic JD parsing** (no LLM for requirements extraction)
- **BM25 retrieval** (407 chunks, ~3k tokens vs 14k lexical)
- **Structured evidence bank** (38 bullets with IDs, ownership, metrics, line_count)
- **Allowlist/blocklist** skills for grounding
- **Page fitting module** (measures bullet lines via pdftotext -bbox)
- **Centralized contact** (profile/contact.yaml)
- **Model routing**: Writing (Z.ai) ≠ Review (OpenRouter Gemini) - different families
- **Comprehensive validator** (51 checks: ATS source, visual, page, bullets, skills, score consistency)
- **All 51 tests pass**

### Gaps & Issues

| Issue | Impact | Location |
|-------|--------|----------|
| **Evidence bank not wired into engine** | `retrieve()` still uses old `generation_sources.py` | `generation_engine.py:324` |
| **Page fitter not integrated** | Engine compiles → validates → repairs (LLM loop) not measured fitting | `page_fitter.py` unused |
| **No cover letter company research** | LLM writes generic without company intel | `LETTER_PROMPT` |
| **No application Q&A generation** | Many apps have short-answer questions | `application-questions.md` only manual |
| **Single intake per run** | Can't batch-process multiple jobs | API design |
| **No referral contact finder** | Tracker has referral fields but no lookup | `operations/application-tracker.md` |
| **No application submission** | Must manually upload PDFs to portals | Out of scope but critical |

### Key Files
- `workspace_app/generation_engine.py` - orchestrator
- `workspace_app/generation_sources.py` - BM25 retrieval (now default)
- `workspace_app/jd_parser.py` - deterministic JD parser
- `workspace_app/evidence_bank.py` - structured evidence (NOT YET USED)
- `workspace_app/page_fitter.py` - deterministic page fitting (NOT YET USED)
- `workspace_app/bm25_retrieval.py` - BM25 index
- `workspace_app/generation_models.py` - Pydantic schemas
- `workspace_app/generation_render.py` - LaTeX rendering with contact.yaml

---

## 3. Integration Gaps (The "Missing Middle")

### Current Manual Workflow
```
1. Run: python3 job-search/src/job_discovery.py run-pipeline
2. Open: jobs-inbox.csv or results/*/shortlist.md
3. Pick job, click URL, read full posting
4. Copy JD text
5. POST /api/intakes with {company, title, jd, mode}
6. GET /api/runs with {intake_id, provider, model, ...}
7. Wait for run to complete (status: needs_human_review)
8. Review artifacts, POST /api/runs/{id}/approve
9. Manually upload resume.pdf + cover-letter.pdf to employer portal
10. Update tracker with "Applied" status
```

### Missing Automation Layer

```
┌────────────────────────────────────────────────────────────────────┐
│                    MISSING: Orchestration Layer                    │
├────────────────────────────────────────────────────────────────────┤
│  jobs-inbox.csv ──▶ [Auto-fetch JD] ──▶ [Create Intake]           │
│       │                                        │                   │
│       ▼                                        ▼                   │
│  [Score against resume] ──▶ [Rank top-N] ──▶ [Batch generate]     │
│                                                                      │
│  [Company research] ──▶ [Enhance cover letter]                     │
│                                                                      │
│  [Form filler] ──▶ [Submit application] ──▶ [Update tracker]      │
└────────────────────────────────────────────────────────────────────┘
```

---

## 4. Priority Improvement Roadmap

### Phase 1: Connect Discovery → Application (HIGH IMPACT, ~1 week)

| Task | Description | Files to Create/Modify |
|------|-------------|------------------------|
| **1.1 JD Fetcher** | Auto-fetch full JD from URLs in `jobs-inbox.csv` | `workspace_app/jd_fetcher.py` |
| **1.2 Resume→Job Matcher** | Score inbox jobs against your resume (TF-IDF/BM25) | `workspace_app/job_matcher.py` |
| **1.3 Batch Intake Creator** | CLI/API to create intakes from top-N ranked jobs | `workspace_app/batch_intake.py` |
| **1.4 Orchestration Script** | Single command: `python3 -m career_ops apply --top 10` | `automation/apply_pipeline.py` |
| **1.5 Company Research** | Auto-fetch company info (LinkedIn, news, Glassdoor) | `workspace_app/company_research.py` |

### Phase 2: Harden Application Generation (HIGH IMPACT, ~3 days)

| Task | Description | Files to Modify |
|------|-------------|-----------------|
| **2.1 Wire evidence_bank** | Use `evidence_bank.select_for_role()` in resume drafting | `generation_engine.py`, `generation_sources.py` |
| **2.2 Wire page_fitter** | Replace LLM repair loop with measured fitting | `generation_engine.py:380-424` |
| **2.3 Application Q&A Generator** | Parse form questions, draft answers from evidence | `workspace_app/qa_generator.py` |
| **2.4 Cover Letter Company Research** | Inject company intel into letter prompt | `generation_engine.py:341-348` |

### Phase 3: Application Submission (MEDIUM IMPACT, ~1 week)

| Task | Description | Approach |
|------|-------------|----------|
| **3.1 Portal Detector** | Identify ATS from apply URL (Greenhouse/Lever/Ashby/Workday) | `workspace_app/portal_detector.py` |
| **3.2 Form Filler** | Use Playwright/Selenium to auto-fill common fields | `workspace_app/form_filler.py` |
| **3.3 Submission Tracker** | Record submission confirmation, update tracker | Extend `upsert_application_tracker.py` |
| **3.4 Referral Finder** | LinkedIn search for connections at target company | `workspace_app/referral_finder.py` |

### Phase 4: Operational Excellence (ONGOING)

| Task | Description |
|------|-------------|
| **4.1 Scheduled Scans** | Cron/GitHub Action for daily `run-pipeline` |
| **4.2 Alerting** | Notify when high-fit jobs appear (email/Slack) |
| **4.3 Dashboard** | Web UI for inbox review, run status, tracker |
| **4.4 Analytics** | Track application funnel: discovered → applied → interview → offer |

---

## 5. Quick Wins (Can Do Today)

### 5.1 Create JD Fetcher + Batch Intake (2-3 hours)

```python
# automation/create_intakes_from_inbox.py
#!/usr/bin/env python3
"""Fetch JDs from jobs-inbox.csv and create intakes for top-N by fit_score."""

import csv
import json
import requests
from pathlib import Path
from job_search.src.job_discovery import ROOT, DEFAULT_INBOX

def fetch_jd(url: str) -> str:
    """Fetch full job description from URL."""
    # Try to detect ATS and use API, fallback to HTML scrape
    # ... implementation
    pass

def main():
    inbox = DEFAULT_INBOX
    jobs = []
    with inbox.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            jobs.append(row)
    
    # Sort by fit_score descending
    jobs.sort(key=lambda x: int(x.get("fit_score", 0)), reverse=True)
    
    # Take top 10
    for job in jobs[:10]:
        jd = fetch_jd(job["url"])
        # POST to /api/intakes or call IntakeStore.create()
        print(f"Created intake for {job['company']} - {job['position']}")
```

### 5.2 Wire Evidence Bank (1 hour)

In `generation_engine.py`, replace the evidence retrieval:

```python
# OLD (line ~324)
evidence = retrieve(self.root, req)

# NEW
from .evidence_bank import load_evidence_bank, EvidenceBank
bank = load_evidence_bank(self.root)
# Convert requirements to required/preferred tech lists
required = [r.term for r in req.requirements if r.priority == "required"]
preferred = [r.term for r in req.requirements if r.priority == "preferred"]
lane = req.lane.lower().replace("/", "-").replace(" ", "-")
exp_bullets, proj_bullets = bank.select_for_role(required, preferred, lane)
# Build evidence dict compatible with existing format
evidence = build_evidence_from_bank(exp_bullets, proj_bullets)
```

### 5.3 Wire Page Fitter (1 hour)

In `generation_engine.py`, replace the repair loop (lines 381-424):

```python
# OLD: LLM-based repair loop
# NEW: Deterministic fitting
from .page_fitter import fit_resume_to_page

fitted = fit_resume_to_page(run_dir, resume)
resume = fitted.resume
# If page_count > 1 or bottom_gap > threshold, trigger targeted LLM shorten
if fitted.page_count > 1 or fitted.bottom_gap_points > 24:
    # Only then ask LLM to shorten specific overlong bullets
    ...
```

---

## 6. Architecture Decision Records Needed

| Decision | Options | Recommendation |
|----------|---------|----------------|
| **Job→Application bridge** | CLI script vs API endpoint vs background worker | CLI script first (simpler), API later |
| **Company research source** | LinkedIn API (paid), SerpAPI, manual curation | SerpAPI + manual fallback |
| **Form filling** | Playwright (Python), Selenium, browser extension | Playwright - headless, reliable |
| **Scheduling** | GitHub Actions, cron, APScheduler | GitHub Actions (free, integrated) |
| **State persistence** | SQLite, JSON files, Redis | JSON files (current pattern) |

---

## 7. Risk Assessment

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| ATS API changes break fetchers | Medium | High | Version pinning, fallback to HTML scrape |
| Form filling detected as bot | Medium | High | Human-in-the-loop, random delays, residential proxies |
| Token cost spikes | Low | Medium | Budget enforcement, local models for draft |
| Evidence bank gaps | Medium | Medium | Gap recovery gate, human review required |
| F-1/OPT eligibility wrong | Low | Critical | Conservative blocker detection, never auto-apply |

---

## 8. Next Steps

### Immediate (This Week)
1. ✅ **DONE**: Fix 3 critical bugs, add providers, evidence bank, BM25, JD parser, page fitter, contact.yaml
2. **TODO**: Create `automation/apply_pipeline.py` - the bridge script
3. **TODO**: Wire `evidence_bank` and `page_fitter` into `generation_engine`
4. **TODO**: Test end-to-end: inbox → intake → run → approve → tracker

### Short-term (Next 2 Weeks)
1. Add scheduled GitHub Action for daily job discovery
2. Implement company research for cover letters
3. Add application Q&A generator
4. Build referral contact finder (LinkedIn search)

### Medium-term (Next Month)
1. Form filler for Greenhouse/Lever/Ashby portals
2. Web dashboard for reviewing inbox and runs
3. Analytics: application funnel tracking

---

## Appendix: Key Commands Reference

```bash
# Job Discovery
python3 job-search/src/job_discovery.py run-pipeline --company-limit 100
python3 job-search/src/job_discovery.py generate-queries --windows 0-6h,0-24h
python3 job-search/src/job_discovery.py discover-direct-ats-targets --path urls.txt

# Application Package (via API)
curl -X POST http://localhost:8000/api/intakes -d '{"company":"X","title":"Y","jd":"..."}'
curl -X POST http://localhost:8000/api/runs -d '{"intake_id":"...","provider":"zai","model":"glm-4.7-flash"}'
curl -X POST http://localhost:8000/api/runs/{id}/approve -d '{"confirmed":true,"factual_review":"...","visual_review":"...","editorial_review":"..."}'

# Validation
python3 automation/validate_application_package.py application-packages/Company/Role
python3 automation/analyze_application_keywords.py application-packages/Company/Role
python3 automation/validate_resume_pdf.py master-documents/master-resume/resume.pdf

# Tracker
python3 automation/upsert_application_tracker.py --status Applied --company X --role Y --resume-path ... --cover-letter-path ...
```