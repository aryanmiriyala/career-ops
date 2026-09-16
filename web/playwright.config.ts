import { defineConfig } from '@playwright/test';
import { existsSync, mkdtempSync, mkdirSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join, resolve } from 'node:path';

const root = mkdtempSync(join(tmpdir(), 'career-ops-e2e-'));
const python = existsSync(resolve('../.venv/bin/python')) ? resolve('../.venv/bin/python') : 'python3';
mkdirSync(join(root, 'job-search/config'), { recursive: true });
mkdirSync(join(root, 'profile'));
mkdirSync(join(root, '.local-workspace'));
writeFileSync(join(root, '.local-workspace/scan.json'), JSON.stringify({ status: 'completed_with_warnings', company_limit: 20, fetched_jobs: 12, source_errors: 1, finished_at: new Date().toISOString(), coverage: [{ layer: 'broad-ats', source: 'Fixture Greenhouse', fetched: 12, errors: 1, scanned: 3, available: 50 }] }));
writeFileSync(join(root, 'job-search/config/filters.json'), JSON.stringify({ work_authorization_policy: { sponsorship_blocker_terms: ['no visa sponsorship'] } }));
writeFileSync(join(root, 'job-search/jobs-inbox.csv'), `company,position,posted_at,pulled_at,url,location\nExample Systems,Junior Data Engineer,${new Date().toISOString()},${new Date().toISOString()},https://example.test/jobs/1,United States\nExample Labs,Software Engineer Intern,2026-01-01T00:00:00Z,2026-01-01T00:00:00Z,https://example.test/jobs/2,United States\n`);
writeFileSync(join(root, 'profile/experience-master.md'), '# Experience\n## Example internship\n- Built Python and SQL data pipelines with automated validation for a synthetic classroom dataset of 500 records.\n');

export default defineConfig({
  testDir: './tests', fullyParallel: false, workers: 1, timeout: 30000,
  use: { baseURL: 'http://127.0.0.1:8876', trace: 'off', video: 'off' },
  projects: [{ name: 'desktop', use: { viewport: { width: 1440, height: 1000 } } }, { name: 'mobile', use: { viewport: { width: 390, height: 844 }, isMobile: true, hasTouch: true } }],
  webServer: { command: `${python} -m uvicorn workspace_app.api:app --host 127.0.0.1 --port 8876`, cwd: resolve('..'), env: { CAREER_OPS_ROOT: root, CAREER_OPS_LOCAL_ONLY: '1' }, url: 'http://127.0.0.1:8876/api/health', reuseExistingServer: false },
});
