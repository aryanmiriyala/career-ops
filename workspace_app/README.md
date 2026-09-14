# Local Career Ops Workspace

React + TypeScript + Vite frontend, FastAPI backend. This is the first application increment: login, recent job board, background discovery, provider diagnostics, and saved JD/evidence intake. It does not generate or approve submitted-facing resumes or cover letters yet.

## Run

From the repository root, install Python dependencies in a virtual environment:

```sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements-workspace.txt
```

Build the frontend:

```sh
cd web
npm ci
npm run build
```

Then, from the repository root:

```sh
.venv/bin/python -m uvicorn workspace_app.api:app --host 127.0.0.1 --port 8765
```

Open http://127.0.0.1:8765. Without Supabase settings, create the single local owner account on first visit. Passwords require 12 characters and are stored as salted scrypt hashes. Sessions use HttpOnly, SameSite=Strict cookies. The local HTTP cookie is intentionally not Secure; this mode must remain bound to loopback and is not a cloud authentication solution.

For frontend development, run `npm run dev` from `web/` while the backend runs on port 8765. Vite proxies `/api` to the backend. No Vercel account is involved.

## Supabase Auth

To use Supabase instead of local login, add these settings to the root `.env`, then reload the page:

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

Refresh starts the existing `run-pipeline --dry-run` command in a background subprocess. The default UI scope caps the broad scan at 20 boards per ATS source; choose all boards for the full broad scan. Configured direct targets and supplemental public feeds are still included. The original CLI default remains unlimited. Each UI scan has a unique directory under `job-search/results/YYYY-MM-DD/workspace-<id>/`.

Only one scan runs at a time in the local process. Cancellation terminates the child; a 20-minute timeout bounds it. Restarted in-progress scans are marked interrupted. Source failures are counted in `run-state.json` and shown as warnings when the subprocess finishes. Partial reports may appear during a run. Refresh is manual in this increment; scheduled refresh and posting-liveness verification remain pending. Returned matches are not proof that a role is still accepting applications.

Dry-run scans leave the manually maintained inbox and discovery history unchanged. The board deduplicates URLs and preserves the earliest observation available across saved reports. This is a browsing index, not a replacement application tracker.

## Intake and Evidence

Selecting a job prefills an intake form. Paste the complete employer posting before saving. Inputs and deterministic evidence candidates are stored under `.local-workspace/intakes/<fingerprint>/`. Repeating identical intake input reopens the same snapshot with zero model calls. Intake snapshots intentionally retain their original evidence/source hashes; automatic invalidation or refresh after profile edits is not implemented yet.

Candidates come only from the named profile source files. The initial retriever uses lexical ranking and a maximum of 18 excerpts / 18,000 evidence characters. Estimated tokens use characters divided by four, not provider token accounting. Missing terms need manual source/gap recovery. Source-linked excerpts are not an independent guarantee that a future generated claim is truthful.

Faithful, Balanced, and Aggressive are saved mode selections for the future writer. All preserve verified facts. Selecting a mode does not currently rewrite content. Explicit configured work-authorization phrases block the intake; ambiguity is not automatically resolved. No final application folder, tracker entry, score, or PDF is fabricated by this preliminary workflow.

## Providers

`/api/providers` exposes presence booleans and variable names only. Existing `ZAI_KEY`, `OPENCODE_API_KEY`, `OPEN_ROUTER_KEY`, and `LANGFUSE_BASE_URL` aliases are supported. `.env` is never served by the app.

Connection buttons request account/model metadata. Metadata reachability does not establish authentication, generation permissions, or free quota for every provider. The Z.ai button sends a synthetic `glm-4.7-flash` request capped at 32 output tokens with thinking disabled. There are no retries or paid fallbacks. It sends no profile content and returns only sanitized status, latency, and numeric usage. Verify the model's current free pricing before future use; provider promotions can change. Langfuse credential presence is displayed, but tracing is not integrated yet.

## Test

From the repository root:

```sh
.venv/bin/python -m unittest discover -s workspace_app/tests -v
```

From `web/`, after building:

```sh
npx playwright install chromium
npm run test:e2e
```

Browser tests start a separate API on port 8876 against synthetic data in a temporary directory. They do not use the real owner account, API keys, profile data, or an existing browser session. They cover desktop and mobile login, date/search filters, job selection, evidence intake, provider settings, and sign-out. Screen recordings and traces are disabled. Screenshots capture only synthetic test pages.

## Deployment Boundary

This single-process server is a local development build. The recommended production target is React on AWS Amplify Hosting, a Python API on AWS, S3 for artifacts, DynamoDB for job state, and Fargate/Step Functions for generation tasks, with Supabase Auth. AWS deployments must replace the in-process subprocess manager and filesystem store, add persistent distributed admission control, enforce HTTPS, and configure the real frontend origin. Do not deploy local-owner mode publicly.

The next increment is a source-grounded draft engine, persisted stage cache, independent quality evaluation, and deterministic canonical PDF rendering. It should be benchmarked before enabling a submission-ready workflow.
