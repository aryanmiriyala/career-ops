import json
import tempfile
import time
import unittest
from pathlib import Path

from workspace_app.core import IntakeStore
from workspace_app.generation_engine import GenerationEngine, GenerationRuns
from workspace_app.generation_models import Approval, LetterDraft, PackageDraft, Requirements, ResumeDraft, Review, RunRequest
from workspace_app.generation_transport import allowed_route


class FakeTransport:
    def __init__(self):
        self.calls = []
        self.force_repair = False

    def complete(self, directory, run_id, stage, schema, system, payload, config, review=False):
        self.calls.append(stage)
        if schema is Requirements:
            return Requirements.model_validate({
                'lane': 'Data engineering', 'title': 'Data Engineer',
                'requirements': [{'id': 'R1', 'term': 'Python', 'quote': 'Python', 'priority': 'required'}],
                'eligibility': 'uncertain', 'eligibility_quotes': [],
                'eligibility_reason': 'The synthetic posting contains no work-authorization language.'})
        evidence_id = payload['evidence']['evidence'][0]['id']
        if schema is ResumeDraft:
            bullets = [{'text': f'Built Python data pipeline component {word} for reliable validation workflows.',
                        'evidence_ids': [evidence_id]} for word in
                       ['alpha', 'bravo', 'charlie', 'delta', 'echo', 'foxtrot', 'golf', 'hotel', 'india', 'juliet', 'kilo']]
            return ResumeDraft.model_validate({
                'target_title': 'Data Engineer', 'strategy': 'Lead with verified Python pipeline and validation evidence.',
                'summary': [], 'experience': [{'name': 'Example Company', 'title': 'Engineer', 'dates': '2024',
                    'location': 'Ohio', 'evidence_ids': [evidence_id], 'bullets': bullets}], 'projects': [],
                'skills': [{'text': 'Languages: Python', 'evidence_ids': [evidence_id]}],
                'gaps': [{'requirement_id': 'R1', 'decision': 'supported', 'evidence_ids': [evidence_id],
                          'rationale': 'The cited source explicitly documents Python pipeline work.'}]})
        if schema is LetterDraft:
            base = ('I am applying for the Data Engineer role at Example Company because the position emphasizes reliable '
                    'Python data workflows. My verified engineering work focused on building and validating pipeline components '
                    'that made downstream processing easier to inspect and maintain. ')
            return LetterDraft.model_validate({'paragraphs': [
                {'text': base + 'This connection makes the role a concrete match for my recent work.', 'evidence_ids': [evidence_id]},
                {'text': base + 'I translated implementation details into clear operational outcomes for collaborators.', 'evidence_ids': [evidence_id]},
                {'text': base + 'I would welcome a conversation about contributing this experience to the team.', 'evidence_ids': [evidence_id]}]})
        if schema is Review:
            experience_score = 10 if self.force_repair and stage == 'independent_review' else 25
            return Review.model_validate({'experience': {'earned': experience_score, 'rationale': 'The experience directly addresses the only extracted requirement.', 'evidence_ids': [evidence_id]},
                'impact': {'earned': 15, 'rationale': 'The draft presents concrete contribution and workflow outcomes.', 'evidence_ids': [evidence_id]},
                'risk': {'earned': 10, 'rationale': 'All claims use cited evidence and unsupported terms are omitted.', 'evidence_ids': [evidence_id]},
                'supported_requirement_ids': ['R1'], 'unsupported_claims': [], 'editorial_issues': [],
                'eligibility': 'uncertain', 'eligibility_reason': 'The posting contains no explicit work-authorization language.'})
        if schema is PackageDraft:
            return PackageDraft.model_validate({'resume': payload['resume'], 'cover_letter': payload['cover_letter']})
        raise AssertionError(schema)


class GenerationTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / 'profile').mkdir()
        (self.root / 'profile/evidence-index.md').write_text(
            '# Evidence\n## Example Company\nExample Company Engineer 2024 Ohio. Built Python data pipeline components '
            'for reliable validation workflows and maintainable downstream processing.\n')
        (self.root / 'job-search/config').mkdir(parents=True)
        (self.root / 'job-search/config/filters.json').write_text(json.dumps({'work_authorization_policy': {}}))
        self.jd = 'Example Company seeks a Data Engineer with Python for reliable data workflows. ' * 3
        self.intake = IntakeStore(self.root).create('Example Company', 'Data Engineer', self.jd, 'aggressive')
        self.transport = FakeTransport()
        self.runs = GenerationRuns(self.root, GenerationEngine(self.root, self.transport),
                                   validator=lambda directory: {'passed': True, 'exit_code': 0, 'output': 'PASS'},
                                   tracker=lambda state: {'passed': True, 'exit_code': 0, 'output': 'UPDATED'})

    def wait(self, identifier):
        for _ in range(100):
            state = self.runs.get(identifier)
            if state['status'] != 'running':
                return state
            time.sleep(.05)
        self.fail('generation did not finish')

    def test_aggressive_run_compiles_and_requires_human_release(self):
        state = self.wait(self.runs.start(RunRequest(intake_id=self.intake['id']))['id'])
        self.assertEqual(state['status'], 'needs_human_review', state.get('message'))
        self.assertEqual(state['alignment']['score'], 100)
        run_dir = self.runs.directory / state['id']
        self.assertTrue((run_dir / 'resume.pdf').is_file())
        self.assertTrue((run_dir / 'cover-letter.pdf').is_file())
        self.assertTrue((run_dir / 'eligibility.json').is_file())
        self.assertTrue((run_dir / 'gaps.json').is_file())
        self.assertTrue((run_dir / 'strategy.json').is_file())
        self.assertFalse((self.root / state['package'] / 'resume.pdf').exists())
        approved = self.runs.approve(state['id'], Approval(confirmed=True,
            factual_review='Reviewed every submitted claim against the cited synthetic source and found no unsupported claims.',
            visual_review='Reviewed both one-page PDFs and found no clipping, overlap, overflow, or inconsistent typography.',
            editorial_review='Reviewed the resume and letter for clear external-reader language, natural tone, and synchronized terms.'))
        self.assertEqual(approved['status'], 'ready')
        self.assertTrue((self.root / state['package'] / 'resume.pdf').is_file())

    def test_identical_rerun_uses_stage_cache(self):
        first = self.wait(self.runs.start(RunRequest(intake_id=self.intake['id']))['id'])
        self.assertEqual(first['status'], 'needs_human_review')
        calls = len(self.transport.calls)
        second = self.wait(self.runs.start(RunRequest(intake_id=self.intake['id']))['id'])
        self.assertEqual(second['status'], 'needs_human_review')
        self.assertEqual(len(self.transport.calls), calls)
        self.assertTrue(all(second['cache_hits'].values()))

    def test_refresh_drafts_reuses_requirements_only(self):
        first = self.wait(self.runs.start(RunRequest(intake_id=self.intake['id']))['id'])
        self.assertEqual(first['status'], 'needs_human_review')
        calls = len(self.transport.calls)
        second = self.wait(self.runs.start(RunRequest(intake_id=self.intake['id'], refresh_drafts=True))['id'])
        self.assertEqual(second['status'], 'needs_human_review')
        self.assertEqual(len(self.transport.calls), calls + 3)
        self.assertTrue(second['cache_hits']['requirements'])
        self.assertFalse(second['cache_hits']['resume'])
        self.assertFalse(second['cache_hits']['cover_letter'])
        self.assertFalse(second['cache_hits']['independent_review'])

    def test_paid_route_requires_explicit_approval(self):
        allowed_route('zai', 'glm-4.7-flash', False)
        with self.assertRaises(ValueError):
            allowed_route('openrouter', 'some/model', False)
        allowed_route('openrouter', 'some/model', True)

    def test_low_score_gets_one_targeted_repair_and_second_review(self):
        self.transport.force_repair = True
        state = self.wait(self.runs.start(RunRequest(intake_id=self.intake['id']))['id'])
        self.assertEqual(state['status'], 'needs_human_review')
        self.assertTrue(state['validation']['repair_attempted'])
        self.assertEqual(self.transport.calls.count('targeted_repair'), 1)
        self.assertEqual(self.transport.calls.count('repair_review'), 1)

    def test_sub90_release_requires_substantive_waiver(self):
        state = self.wait(self.runs.start(RunRequest(intake_id=self.intake['id']))['id'])
        path = self.runs.directory / state['id'] / 'run.json'
        state['alignment']['score'] = 89
        path.write_text(json.dumps(state))
        with self.assertRaises(ValueError):
            self.runs.approve(state['id'], Approval(confirmed=True, factual_review='factual review ' * 4,
                visual_review='visual review ' * 4, editorial_review='editorial review ' * 4))


if __name__ == '__main__':
    unittest.main()
