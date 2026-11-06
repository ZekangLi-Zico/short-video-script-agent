"""Regression tests for issues observed in the frozen 50-run campaign."""
import copy
import unittest

from src.agent import Agent, ModelError
from src.mock import MockModel, action, example_script
from src.reporting import render_report
from src.tools import ROOT, ToolBox, read_json
from scripts.evaluate import check_case


class RepairTests(unittest.TestCase):
    def test_review_receives_actual_fact_evidence_for_current_script(self):
        received = []

        class FactAwareReviewer(MockModel):
            def review(self, request, script, rules_check=None, duration_check=None):
                received.append(copy.deepcopy(rules_check))
                return super().review(request, script)

        result = Agent(FactAwareReviewer(), ToolBox()).run(read_json(ROOT/'examples/inputs/normal.json'))
        self.assertEqual(received, [result['rules_check']])
        self.assertTrue(received[0]['passed'])
        self.assertEqual(received[0]['citations'][0]['quote'], '剪影练习版支持为视频添加字幕。')
        self.assertEqual(result['trace'][-2]['arguments']['rules_check'], received[0])

    def test_model_start_failure_is_not_evidence_of_business_negative_case(self):
        class Unavailable(MockModel):
            evidence_kind = 'real_model'

            def decide(self, state, rules):
                raise ModelError('test_startup_failure')

        request = read_json(ROOT/'examples/inputs/normal.json')
        for case, changed in [('no_material', {'product_id': 'absent'}), ('impossible_duration', {'target_seconds': 1})]:
            result = Agent(Unavailable(), ToolBox()).run({**request, **changed})
            self.assertTrue(check_case(case, result, {'blocked', 'needs_input'}))

    def test_unmet_requirement_is_feedback_not_success_and_reported(self):
        class RejectingReviewer(MockModel):
            def review(self, request, script, rules_check=None, duration_check=None):
                report, meta = super().review(request, script)
                report['items'][0].update(verdict='unmet', evidence='当前稿只有通用画面，缺少校园采访背景。')
                return report, meta

        request = read_json(ROOT/'examples/inputs/normal.json')
        request['topic'] = '以校园采访为背景介绍字幕功能'
        result = Agent(RejectingReviewer(), ToolBox()).run(request)
        self.assertEqual(result['status'], 'needs_input')
        self.assertFalse(result['requirements_check']['passed'])
        self.assertEqual(result['trace'][-2]['action'], 'check_requirements')
        self.assertIn('缺少校园采访背景', render_report(result))

    def test_uncertain_or_invalid_review_cannot_be_accepted(self):
        for mode in ('uncertain', 'missing_field', 'invented_quote', 'transport'):
            class BadReviewer(MockModel):
                def review(self, request, script, rules_check=None, duration_check=None):
                    if mode == 'transport':
                        raise ModelError('test_review_timeout')
                    report, meta = super().review(request, script)
                    if mode == 'uncertain':
                        report['items'][0]['verdict'] = 'uncertain'
                    elif mode == 'missing_field':
                        report['items'][-1] = copy.deepcopy(report['items'][0])
                    else:
                        report['items'][0]['requirement'] = '这是用户没有提过的要求'
                    return report, meta

            with self.subTest(mode=mode):
                result = Agent(BadReviewer(), ToolBox()).run(read_json(ROOT/'examples/inputs/normal.json'))
                self.assertNotEqual(result['status'], 'completed')
                self.assertFalse(result['requirements_check'].get('passed', False))

    def test_revision_invalidates_requirement_review_even_after_other_rechecks(self):
        class StaleReviewModel(MockModel):
            def __init__(self):
                self.revised = False

            def decide(self, state, rules):
                if state.get('requirements_check') and not self.revised:
                    self.revised = True
                    script = copy.deepcopy(state['script'])
                    script['shots'][0]['hold_seconds'] = 5
                    return action('write_script', '修改已审核的稿件', script=script), {'provider': self.name}
                if self.revised and state['duration'] and state['rules_check']:
                    return action('finish', '试图复用旧需求检查', status='completed'), {'provider': self.name}
                return super().decide(state, rules)

        result = Agent(StaleReviewModel(), ToolBox(), max_steps=9).run(read_json(ROOT/'examples/inputs/normal.json'))
        self.assertEqual(result['status'], 'step_limit')
        self.assertIsNone(result['requirements_check'])
        self.assertEqual(result['trace'][-1]['observation']['error'], 'completion_gate_rejected')

    def test_two_checks_alone_cannot_claim_all_requirements_completed(self):
        class UnreviewedModel:
            name, evidence_kind = 'test_sequence', 'test_stub'

            def __init__(self):
                self.actions = iter([
                    action('search_materials', '检索', query='字幕'),
                    action('write_script', '生成', script=example_script()),
                    action('estimate_duration', '估时'),
                    action('check_rules', '核对事实'),
                    action('finish', '直接宣称完成', status='completed'),
                ])

            def decide(self, state, rules):
                return next(self.actions), {'provider': self.name}

        result = Agent(UnreviewedModel(), ToolBox(), max_steps=5).run(read_json(ROOT/'examples/inputs/normal.json'))
        self.assertEqual(result['status'], 'step_limit')
        self.assertEqual(result['trace'][-1]['observation']['error'], 'completion_gate_rejected')

    def test_completed_script_preserves_model_explanation_in_delivery(self):
        explanation = "已删除没有统计依据的效果数字，仅保留有来源的字幕功能。"

        class ExplainingModel(MockModel):
            def decide(self, state, rules):
                response, meta = super().decide(state, rules)
                if response['action'] == 'finish' and response['status'] == 'completed':
                    response['message'] = explanation
                return response, meta

        result = Agent(ExplainingModel(), ToolBox()).run(read_json(ROOT/'examples/inputs/normal.json'))
        self.assertEqual(result['status'], 'completed')
        self.assertIn(explanation, result['message'])
        self.assertIn(explanation, render_report(result))
        self.assertIn('未生成或发布视频', result['message'])
