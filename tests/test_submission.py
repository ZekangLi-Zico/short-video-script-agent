"""Submission regressions; fixtures here are not real-model evidence."""
import copy
import unittest

from scripts.evaluate import check_case
from src.agent import Agent
from src.mock import MockModel, action, example_script
from src.reporting import render_report
from src.requirements import bound_duration_check
from src.revisions import revision_summary
from src.schema import validate_script
from src.tools import ROOT, ToolBox, read_json

REQUEST = read_json(ROOT / 'examples/inputs/normal.json')
NOTE = '已删除自动识别和99%准确率承诺：客户未提供相关证据。此说明只供创作者审稿。'


class SubmissionTests(unittest.TestCase):
    def test_acceptance_rejects_missing_failed_or_stale_review_in_current_and_future_versions(self):
        valid = Agent(MockModel(), ToolBox()).run(REQUEST)
        self.assertEqual(check_case('normal', valid, {'completed'}), [])
        for policy in ('facts_duration_requirements_v4', 'facts_duration_requirements_v5'):
            for change in (None, {'passed': False}, {'ok': False}, {'script_hash': 'stale'}):
                with self.subTest(policy=policy, change=change):
                    bad = copy.deepcopy(valid)
                    bad['metadata']['completion_policy'] = policy
                    bad['requirements_check'] = None if change is None else {**bad['requirements_check'], **change}
                    self.assertTrue(check_case('normal', bad, {'completed'}))

    def test_legacy_scripts_and_bounded_editor_notes(self):
        old = example_script()
        validate_script(old)
        validate_script({**old, 'editor_notes': NOTE})
        for bad in (None, [], 5, 'x' * 2001):
            with self.assertRaises(ValueError):
                validate_script({**old, 'editor_notes': bad})

    def test_editor_notes_do_not_count_as_speech_or_publishable_claims(self):
        tools = ToolBox()
        old = example_script()
        new = {**copy.deepcopy(old), 'editor_notes': NOTE}
        before = tools.estimate_duration(old, 30)
        after = tools.estimate_duration(new, 30)
        self.assertEqual(before['total_seconds'], after['total_seconds'])
        self.assertNotEqual(before['script_hash'], after['script_hash'])
        self.assertTrue(tools.check_rules(new, ['P01'])['passed'])
        new['shots'][0]['blocks'][0]['text'] = '自动识别人声，准确率99%。'
        self.assertFalse(tools.check_rules(new, ['P01'])['passed'])

    def test_editor_notes_cannot_replace_a_public_source_fact(self):
        script = example_script()
        script['shots'] = script['shots'][:1]
        script['editor_notes'] = '剪影练习版支持为视频添加字幕。来源P01/F1。'
        self.assertFalse(ToolBox().check_rules(script, ['P01'])['passed'])

    def test_markdown_exports_notes_outside_shots_with_an_explicit_non_video_label(self):
        result = Agent(MockModel(), ToolBox()).run(REQUEST)
        result['script']['editor_notes'] = NOTE
        report = render_report(result)
        self.assertIn('## 审稿备注（不进入视频，不计入时长）', report)
        self.assertEqual(report.count(NOTE), 1)
        spoken = '\n'.join(s for s in report.splitlines() if s.startswith('旁白/字幕：'))
        self.assertNotIn(NOTE, spoken)

    def test_note_only_change_is_logged_and_invalidates_old_approval(self):
        old = example_script()
        new = {**copy.deepcopy(old), 'editor_notes': NOTE}
        self.assertEqual(revision_summary(old, new, [])['changed_fields'], ['editor_notes'])
        timing = ToolBox().call('estimate_duration', {'script': old, 'target_seconds': REQUEST['target_seconds']})
        self.assertIsNone(bound_duration_check(timing, REQUEST, new))
        sequence = [action('search_materials', '查事实', query='字幕'),
                    action('write_script', '写稿', script=old), action('estimate_duration', '估时'),
                    action('check_rules', '查规则'), action('check_requirements', '核对需求'),
                    action('write_script', '仅补审稿说明', script=new),
                    action('finish', '尝试复用旧审核', status='completed')]
        class Sequence(MockModel):
            def decide(self, state, rules):
                return sequence[len(state['history'])], {'provider': 'test_fixture'}
        result = Agent(Sequence(), ToolBox(), max_steps=7).run(REQUEST)
        self.assertEqual(result['trace'][-1]['observation']['error'], 'completion_gate_rejected')
        self.assertEqual(result['status'], 'step_limit')


if __name__ == '__main__':
    unittest.main()
