# Active Discovery Sources

This is the implemented default pipeline, not the larger planned source catalog.

| Source | Access | Current default scope |
| --- | --- | --- |
| Greenhouse | boards-api.greenhouse.io | 100 rotating employer boards, plus Anthropic and Databricks |
| Lever | api.lever.co | 100 rotating employer boards |
| Ashby | api.ashbyhq.com | 100 rotating employer boards, plus OpenAI and Cursor |
| Workday | Employer-specific myworkdayjobs.com CXS endpoints | 100 rotating employer boards |
| Arbeitnow | www.arbeitnow.com/api/job-board-api | One supplemental feed request |
| RemoteOK | remoteok.com/api | One supplemental feed request |

SmartRecruiters has an adapter but no configured targets. Google search links are
generated, not automatically searched. LinkedIn, Indeed, Glassdoor, ZipRecruiter,
Handshake, Built In, Wellfound, Simplify, Hiring Cafe, iCIMS, Oracle, and other
entries in source-catalog.json are not active default ingestion sources.

Broad directories come from cached Feashliaa/job-board-aggregator GitHub datasets.
Directory size does not establish unique companies, healthy boards, or exhaustive
coverage. Broad batches can overlap direct targets.

Run `.venv/bin/python automation/export_discovery_sources.py` for individual board
URLs in the latest scan's source-inventory.csv. Selection is reconstructed from
current caches and the scan offset; it is not a historical request/success log.

## Visible Counts

Fetched counts precede role, seniority, score, location, recency, and duplicate
filtering. Standard scans use 48 hours, shortlist score 60 and review score 45.
Each layer saves at most 50 shortlist entries, plus 100 direct / 150 broad / 50
public review entries. The UI reads saved candidates, not every fetched posting.
Selecting a longer time window cannot recover older jobs discarded at ingestion.

The local board is U.S.-only. Explicit U.S. locations and recognized city/state
signals qualify; foreign, missing, and ambiguous remote locations are hidden.
Location matching is heuristic, not verified eligibility or geocoding. Stored
U.S. counts precede time/search/status filters. Each page holds up to 30 postings.
