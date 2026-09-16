import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from fastapi.testclient import TestClient
from workspace_app.api import create_app

from workspace_app.auth import SupabaseAuth
from workspace_app.core import JobIndex, board, discovery, load_jobs
from workspace_app.scans import Scans
from workspace_app.tests.test_workspace import csv_file


class DiscoveryWorkspaceTests(unittest.TestCase):
    def local_client(self, peer='127.0.0.1'):
        with patch.dict('os.environ', {'CAREER_OPS_LOCAL_ONLY': '1'}):
            return TestClient(create_app(self.root), client=(peer, 50000))

    def test_local_board_needs_no_account(self):
        with self.local_client() as client:
            self.assertEqual(client.get('/api/jobs').status_code, 200)
            session = client.get('/api/auth/session').json()
            self.assertTrue(session['local_only'])
            self.assertTrue(session['authenticated'])
            self.assertFalse(session['setup_required'])

    def test_passwordless_mode_rejects_non_loopback_peers(self):
        with self.local_client('192.0.2.10') as client:
            self.assertEqual(client.get('/api/jobs').status_code, 403)

    def test_passwordless_mode_rejects_cross_site_requests(self):
        with self.local_client() as client:
            self.assertEqual(client.get('/api/jobs', headers={'sec-fetch-site': 'cross-site'}).status_code, 403)
            self.assertEqual(client.post('/api/scans', json={'company_limit': 5}, headers={'origin': 'https://example.test'}).status_code, 403)

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.inbox = self.root / 'job-search/jobs-inbox.csv'
        self.row = {'company': 'Example', 'position': 'Engineer', 'url': 'https://example.test/jobs/1',
                    'posted_at': '2026-01-01T00:00:00Z', 'pulled_at': '2026-01-01T00:00:00Z'}

    def test_local_only_does_not_load_cloud_auth_settings(self):
        with patch.dict('os.environ', {'CAREER_OPS_LOCAL_ONLY': '1'}), patch('workspace_app.auth.credentials', side_effect=AssertionError):
            self.assertEqual(SupabaseAuth(self.root).config(), {'mode': 'local'})

    def test_index_reuses_unchanged_reports(self):
        csv_file(self.inbox, [self.row])
        index = JobIndex(self.root)
        with patch('workspace_app.core.load_jobs', wraps=load_jobs) as read:
            self.assertEqual(board(self.root, hours=0, index=index)['total'], 1)
            self.assertEqual(board(self.root, hours=0, q='absent', index=index)['total'], 0)
            self.assertEqual(read.call_count, 1)

    def test_unscreened_imports_are_not_shortlisted(self):
        csv_file(self.inbox, [self.row])
        self.assertEqual(board(self.root, hours=0, scope='shortlist')['total'], 0)
        result = board(self.root, hours=0, scope='unassessed')
        self.assertEqual(result['total'], 1)
        self.assertEqual(result['jobs'][0]['screening']['label'], 'Not assessed')

    def test_screening_explains_saved_review_and_blockers(self):
        csv_file(self.inbox, [{**self.row, 'status': 'review', 'flags': 'no_early_career_signal'}])
        result = board(self.root, hours=0)['jobs'][0]
        self.assertIn('No early-career wording', result['screening']['reason'])
        csv_file(self.inbox, [{**self.row, 'status': 'shortlist', 'flags': 'work_auth_blocker'}])
        self.assertEqual(board(self.root, hours=0)['jobs'][0]['screening']['label'], 'Eligibility flag')

    def test_rotating_company_batches_wrap_without_duplicate_entries(self):
        self.assertEqual(discovery.company_batch(list(range(5)), 3, 4), [4, 0, 1])
        self.assertEqual(discovery.company_batch(list(range(5)), 20, 4), [4, 0, 1, 2, 3])
        self.assertEqual(discovery.company_batch(list(range(5)), 0, 4), list(range(5)))
        self.assertEqual(discovery.company_batch([], 20, 4), [])

    def test_successful_scan_advances_batch_but_failure_retries_it(self):
        scans = Scans(self.root)
        scans.state = {'status': 'completed', 'company_limit': 20, 'company_offset': 0}
        with patch('workspace_app.scans.threading.Thread'):
            self.assertEqual(scans.start(100)['company_offset'], 20)
            scans.state['status'] = 'failed'
            self.assertEqual(scans.start(100)['company_offset'], 20)

    def test_index_refreshes_changed_added_and_deleted_reports(self):
        csv_file(self.inbox, [self.row])
        index = JobIndex(self.root)
        self.assertEqual(len(index.snapshot()[0]), 1)
        csv_file(self.inbox, [{**self.row, 'position': 'Data Engineer'}])
        self.assertEqual(index.snapshot()[0][0]['title'], 'Data Engineer')
        report = self.root / 'job-search/results/fixture/jobs.csv'
        csv_file(report, [{**self.row, 'url': 'https://example.test/jobs/2'}])
        self.assertEqual(len(index.snapshot()[0]), 2)
        report.unlink()
        self.assertEqual(len(index.snapshot()[0]), 1)

    def test_index_does_not_cache_time_window_results(self):
        csv_file(self.inbox, [self.row])
        index = JobIndex(self.root)
        self.assertEqual(board(self.root, hours=0, index=index)['total'], 1)
        self.assertEqual(board(self.root, hours=1, index=index)['total'], 0)

    def test_scan_progress_is_read_without_exposing_logs(self):
        scans = Scans(self.root)
        results = self.root / 'job-search/results/fixture'
        results.mkdir(parents=True)
        scans.state = {'status': 'running', 'results_dir': str(results.relative_to(self.root))}
        (results / 'progress.json').write_text(json.dumps({'stage': 'broad-ats'}))
        self.assertEqual(scans.snapshot()['stage'], 'broad-ats')
        (results / 'progress.json').write_text('{')
        self.assertNotIn('stage', scans.snapshot())

    def test_pipeline_records_coverage_and_preserves_cli_default(self):
        result_dir = self.root / 'results'
        args = discovery.build_parser().parse_args(['run-pipeline', '--dry-run', '--results-dir', str(result_dir)])
        direct = {'fetched_by_source': {'lever': 5}, 'fetch_error_count': 1, 'imported': [], 'review_candidates': []}
        public = {'fetched_by_source': {'arbeitnow': 7}, 'errors': ['synthetic failure'], 'imported': [], 'review_candidates': []}
        broad = {'source_stats': {'greenhouse': {'jobs_fetched': 11, 'company_errors': 2, 'companies_scanned': 3, 'companies_loaded': 10}}, 'imported': [], 'review_candidates': []}
        with patch.object(discovery, 'fetch_direct_ats_jobs', return_value=direct), \
                patch.object(discovery, 'run_broad_ats_scan', return_value=broad) as fetch_broad, \
                patch.object(discovery, 'fetch_public_jobs', return_value=public), \
                patch.object(discovery, 'write_run_outputs'), \
                patch.object(discovery, 'write_broad_ats_outputs'), \
                patch.object(discovery, 'generate_queries', return_value='Synthetic search links'):
            result = discovery.run_standard_pipeline(args)
        self.assertEqual(fetch_broad.call_args.args[0].company_limit, 0)
        self.assertEqual(result['fetched_jobs'], 23)
        self.assertEqual(result['source_errors'], 4)
        self.assertEqual(result['coverage'][1]['scanned'], 3)
        self.assertEqual(json.loads((result_dir / 'progress.json').read_text())['stage'], 'finished')
        self.assertEqual(json.loads((result_dir / 'run-state.json').read_text())['coverage'], result['coverage'])
