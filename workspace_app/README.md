# Local Career Ops Workspace

React + TypeScript + Vite frontend, Tailwind CSS with Radix-backed UI primitives, and FastAPI backend. The local application supports recent-job discovery, saved job-description intake, evidence-grounded resume and cover-letter generation, independent review, deterministic alignment scoring, one-page PDF compilation, human approval, package validation, and tracker updates.

## Run

From the repository root, install Python dependencies in a virtual environment:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-workspace.txt
```

Build the frontend with Bun 1.3.13 (pinned in `web/.bun-version` and `packageManager`):

```sh
cd web
bun install --frozen-lockfile
bun run build
```

Then, from the repository root:

```sh
python3 automation/run_workspace.py
```

Open the URL printed by the launcher (normally http://127.0.0.1:8765). It selects another port if busy and opens directly to the job board, even if Supabase settings exist in `.env`. No login or account setup is required. This explicit local-only mode rejects non-loopback clients and cross-site browser requests; do not expose it through a public proxy or tunnel. Any trusted program running on your computer can access it. No cloud account or model key is required to browse or refresh jobs. Live discovery still requires internet access; saved jobs work offline. Direct Uvicorn startup without `CAREER_OPS_LOCAL_ONLY=1` retains the previous authenticated behavior.

For frontend development, run `bun run dev` from `web/` while the backend runs on port 8765. Vite proxies `/api` to the backend. Bun runs the TypeScript checker and Vite, manages frontend dependencies, and owns the single `web/bun.lock` lockfile. Use `bun add` for dependency changes; do not regenerate an npm lockfile. No Vercel account is involved.

## Supabase Auth

Supabase is optional and deferred for the local-only workflow. To explicitly use it instead of local login, start Uvicorn directly without `CAREER_OPS_LOCAL_ONLY=1`, add these settings to the root `.env`, then reload the page:

```dotenv
SUPABASE_URL=https://YOUR_PROJECT.supabase.co
SUPABASE_PUBLISHABLE_KEY=
SUPABASE_ALLOWED_EMAIL=
```

The legacy `SUPABASE_ANON_KEY` is supported instead of a publishable key. Never put a service-role or secret key in the publishable/anon variable. The public configuration endpoint exposes only the project URL and a validated publishable/anon key, as required by the browser SDK. It never returns provider credentials.

In Supabase, enable email/password sign-in, disable public signups for this private workspace, and create/confirm the allowed owner user through the dashboard. Use that user's email as `SUPABASE_ALLOWED_EMAIL`. The UI supports password sign-in and sign-out; signup, OAuth, invitation acceptance, and self-service password recovery are not implemented yet. Manage/reset the initial owner through the Supabase dashboard. Set the project's site URL to the chosen app origin before adding email redirect workflows.

The browser uses `@supabase/supabase-js` for session persistence and refresh. The backend verifies the access token through the configured project's `/auth/v1/user` endpoint and requires a confirmed email matching the owner allowlist. Successful checks are cached for up to 30 seconds. Invalid or incomplete Supabase configuration fails closed and disables local login. Local cookies cannot bypass Supabase mode. Supabase manages identity data; it is not used for career documents or application state.

Tests mock Supabase responses. Live project sign-in must be verified after settings are supplied. Supabase access tokens can remain valid until their expiry even after refresh-token revocation; this is not an immediate global session revocation implementation.

## Jobs

The board reads `job-search/jobs-inbox.csv` and dated `jobs.csv` reports. It does not read historical application package contents. Posted-date filters exclude undated and future-dated records. Relative posting dates are anchored to the recorded scan observation, not the current page load. Discovery date and publication date are separate controls.

An in-memory index caches parsed reports and invalidates when reports are added, edited, or removed. Time-window filtering is evaluated on every request, so cached jobs do not retain stale freshness labels. The index is disposable; source CSVs stay authoritative.

The UI reports the current scan layer and shows completed source coverage: fetched posting counts before filtering, failures, and attempted versus available boards for broad ATS sources. Zero returned matches does not imply zero source failures. The default 100-board batch is per broad source, not complete coverage. Successful refreshes advance the batch offset; failed/cancelled scans retry their batch. Batches wrap independently around each source directory. Directory entries are not guaranteed to be unique companies or working boards. Use All boards for the uncapped scan, subject to the scan timeout. Discovery is deterministic and makes no LLM calls. It does not generate application packages.

Discovery filter labels are automatic screening metadata, not human review or application statuses. Rule match means the saved scan tagged a posting as shortlisted; Check fit means retained for review; Eligibility flag means a configured work-authorization blocker was detected. Legacy inbox rows without a screening decision are Not assessed and are excluded from Rule matches. Open a job for the screening explanation and saved source flags. These filters are not a personalized resume alignment evaluation. The Review evidence action only starts evidence intake, not document generation.

Refresh starts the existing `run-pipeline --dry-run` command in a background subprocess. The default UI scope caps the broad scan at 100 boards per ATS source, with 20 and 250 also selectable. Configured direct targets and supplemental public feeds are still included. The original CLI default remains unlimited and offset zero. Each UI scan has a unique directory under `job-search/results/YYYY-MM-DD/workspace-<id>/`.

Only one scan runs at a time in the local process. Cancellation terminates the child; a 20-minute timeout bounds it. Restarted in-progress scans are marked interrupted. Source failures are counted in `run-state.json` and shown as warnings when the subprocess finishes. Partial reports may appear during a run. Refresh is manual in this increment; scheduled refresh and posting-liveness verification remain pending. Returned matches are not proof that a role is still accepting applications.

Dry-run scans leave the manually maintained inbox and discovery history unchanged. The board deduplicates URLs and preserves the earliest observation available across saved reports. This is a browsing index, not a replacement application tracker.

## Application Generation

Selecting a job prefills an intake form. Paste the complete employer posting before saving. Inputs and deterministic evidence candidates are stored under `.local-workspace/intakes/<fingerprint>/`. Repeating identical intake input reopens the same snapshot with zero model calls. Intake snapshots intentionally retain their original evidence/source hashes; automatic invalidation or refresh after profile edits is not implemented yet.

Candidates come only from canonical profile and master-document sources, never historical application packages. Retrieval is requirement-aware and bounded. Each generated claim cites stable evidence IDs; deterministic checks reject unknown evidence IDs, unsupported numbers, mismatched entry metadata, and duplicate submitted claims. The independent review and required human factual check cover semantic overstatement that deterministic checks cannot prove.

Faithful keeps close to original verified wording. Balanced curates evidence and blends supported JD language naturally. Aggressive maximizes exact JD terminology, evidence selection, and ordering while retaining the same evidence boundary. Aggressive never permits synthetic tools, projects, titles, metrics, scope, ownership, or outcomes.

Runs persist under `.local-workspace/generation-runs/`. Stage cache keys include prompt version, model route, full structured input, source hashes, and mode. Matching runs reuse cached model output; the UI can explicitly regenerate writing stages while retaining cached requirements. There are no silent provider fallbacks and only one bounded repair attempt.

The Job Alignment & Evidence Score is a 100-point internal estimate: exact requirement coverage 40, experience relevance 25, impact and evidence 15, formatting and parsing 10, and risk/gap handling 10. It is not an employer ATS prediction. Scores below 90 require a substantive release waiver. Final release also requires factual, visual, and editorial review, one-page resume and cover-letter checks, the repository package validator, and any experience-bullet waiver required by repository policy.

Approved artifacts are copied to `application-packages/<Company>/<Role>/` and the bounded tracker helper records the package as `Ready`. Generation never marks an application as submitted. The package includes the full JD, PDFs and source files, tailoring notes, alignment and validation results, requirement/eligibility/gap/strategy records, evidence selection, and editorial review.

## Providers

`/api/providers` exposes presence booleans and variable names only. Existing `ZAI_KEY`, `OPENCODE_API_KEY`, `OPEN_ROUTER_KEY`, and `LANGFUSE_BASE_URL` aliases are supported. `.env` is never served by the app.

Connection buttons request account/model metadata. Metadata reachability does not establish authentication, generation permissions, or free quota for every provider. The Z.ai button sends a synthetic `glm-4.7-flash` request capped at 32 output tokens with thinking disabled. The default generation route permits only that model without the explicit paid/quota checkbox. Other configured routes require explicit approval and never become silent fallbacks.

Each request reserves against a local run token budget and writes actual provider usage, served model, latency, and billing uncertainty to a local ledger. Langfuse tracing is metadata-only: run IDs, stages, model names, latency, and token usage may be sent, but job descriptions, profile excerpts, prompts, resumes, and cover letters are not uploaded as trace content.

## Test

From the repository root:

```sh
.venv/bin/python -m unittest discover -s workspace_app/tests -v
```

From `web/`, after building:

```sh
bunx playwright install chromium
bun run test:e2e
```

Browser tests start a separate API on port 8876 against synthetic data in a temporary directory. They do not use the real owner account, API keys, profile data, or an existing browser session. They cover passwordless local entry, date/search filters, job selection, application controls, master documents, and provider settings on desktop and mobile. Backend tests exercise the staged generation workflow with synthetic sources and a fake model transport, including real LaTeX compilation. Screen recordings and traces are disabled.

## Deployment Boundary

This single-process server is a local development build. The recommended production target is React on AWS Amplify Hosting, a Python API on AWS, S3 for artifacts, DynamoDB for job state, and Fargate/Step Functions for generation tasks, with Supabase Auth. AWS deployments must replace the in-process subprocess manager and filesystem store, add persistent distributed admission control, enforce HTTPS, and configure the real frontend origin. Do not deploy local-owner mode publicly.

Before cloud deployment, replace the in-process generation thread and local filesystem with durable task and artifact services. Build a representative human-rated evaluation set before changing model routing or claiming that a cheaper model preserves writing quality.
