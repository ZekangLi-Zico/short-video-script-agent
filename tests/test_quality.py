"""Public-boundary checks for quality v3; fixtures are not real-model evidence."""
import copy
import unittest

from src.agent import Agent
from src.mock import MockModel, action, example_script
from src.requirements import review_observation
from src.schema import validate_request
from src.tools import ToolBox, ROOT, read_json


def brief(**changes):
    return {**read_json(ROOT / 'examples/inputs/normal.json'), 'expression_mode': 'creative', **changes}


def authored_script():
    s = example_script()
    s['title'] = '把今天的采访留下来'
    s['shots'][0]['visual'] = '校园采访现场，学生举起话筒，随后切到采访花絮。'
    s['shots'][0]['blocks'][0]['text'] = '采访结束了，让我们把这段回忆整理好。'
    return s


def surface_fixture(script):
    slots = [{'location': 'title', 'text': script['title']}]
    for i, shot in enumerate(script['shots'], 1):
        slots.append({'location': f'shot:{i}/visual', 'text': shot['visual']})
        for j, block in enumerate(shot['blocks'], 1):
            if not block['source_id'] and not block['fact_id']:
                slots.append({'location': f'shot:{i}/block:{j}', 'text': block['text']})
    return slots


def review_fixture(request, script):
    review, _ = MockModel().review({k:v for k,v in request.items() if k not in {'expression_mode','duration_mode'}}, script)
    review.update(expressions=[{**slot, 'verdict': 'plain_expression', 'references': [], 'evidence': 'offline review fixture'}
                               for slot in surface_fixture(script)],
                  pacing={'verdict': 'met', 'evidence': 'offline pacing fixture'})
    return review


class CreativeQualityTests(unittest.TestCase):
    def setUp(self):
        self.script, self.request, self.tools = authored_script(), brief(), ToolBox()

    def checked(self):
        return self.tools.call('check_rules', {'script': self.script, 'retrieved_ids': ['P01'], 'expression_mode': 'creative'})

    def test_free_scene_is_reviewable_but_strict_mode_still_rejects(self):
        creative = self.checked()
        self.assertTrue(creative['ok'])
        self.assertTrue(creative['passed'])
        self.assertTrue(creative['requires_expression_review'])
        self.assertEqual(creative['expression_slots'], surface_fixture(self.script))
        self.assertFalse(self.tools.check_rules(self.script, ['P01'])['passed'])

    def test_supported_fact_still_requires_exact_retrieved_quote(self):
        self.script['shots'][1]['blocks'][0]['text'] = '三秒完成所有字幕'
        checked = self.checked()
        self.assertTrue(checked['ok'])
        self.assertFalse(checked['passed'])
        self.assertIn('unsupported_claim', [i['code'] for i in checked['issues']])

    def test_complete_review_binds_every_exposed_surface(self):
        checked = self.checked()
        result = review_observation(review_fixture(self.request, self.script), self.request, self.script, checked)
        self.assertTrue(result['passed'])
        self.assertEqual(len(result['expressions']), len(surface_fixture(self.script)))

    def test_hidden_claim_or_uncertainty_cannot_pass(self):
        for verdict in ('unsupported_claim', 'uncertain'):
            for location in ('title', 'shot:1/visual', 'shot:1/block:1'):
                review = review_fixture(self.request, self.script)
                next(e for e in review['expressions'] if e['location']==location)['verdict'] = verdict
                result = review_observation(review, self.request, self.script, self.checked())
                self.assertFalse(result['passed'])

    def test_missing_duplicate_or_changed_surface_is_invalid(self):
        base = review_fixture(self.request, self.script)
        variants = [base['expressions'][:-1], base['expressions']+[base['expressions'][0]],
                    [{**e, 'text': '伪造审核原文'} if i==0 else e for i,e in enumerate(base['expressions'])]]
        for expressions in variants:
            with self.assertRaises(ValueError):
                review_observation({**base, 'expressions': expressions}, self.request, self.script, self.checked())

    def test_semantic_claim_needs_real_retrieved_reference(self):
        for refs in ([], [{'source_id':'OTHER01','fact_id':'OTHER01.F1'}], [{'source_id':'P01','fact_id':'missing'}]):
            review = review_fixture(self.request, self.script)
            review['expressions'][0].update(verdict='supported_claim', references=refs)
            with self.assertRaises(ValueError):
                review_observation(review, self.request, self.script, self.checked())
        review['expressions'][0]['references'] = [{'source_id':'P01','fact_id':'P01.F1'}]
        self.assertTrue(review_observation(review, self.request, self.script, self.checked())['passed'])

    def test_no_current_rules_evidence_cannot_pass_creative_review(self):
        with self.assertRaises(ValueError):
            review_observation(review_fixture(self.request,self.script), self.request,self.script,None)

    def test_invalid_mode_is_invalid_input(self):
        with self.assertRaises(ValueError): validate_request(brief(expression_mode='anything'))

    def test_review_failure_cannot_be_finished_as_completed(self):
        class BlindReviewer(MockModel):
            def review(self, request, script, rules_check=None, duration_check=None):
                # Deliberately only legacy report, as if adapter returned partial data.
                return MockModel().review({k:v for k,v in request.items() if k!='expression_mode'},script)
        result=Agent(BlindReviewer(), ToolBox()).run(self.request)
        self.assertNotEqual(result['status'],'completed')


class DurationQualityTests(unittest.TestCase):
    def test_target_interval_and_legacy_cap(self):
        tools = ToolBox()
        s = example_script()
        self.assertTrue(tools.estimate_duration(s,30)['passed'])
        self.assertFalse(tools.estimate_duration(s,30,duration_mode='target')['passed'])
        for seconds, expected in ((27,True),(30,True),(26.9,False),(30.1,False)):
            s['shots'][0]['hold_seconds']=seconds-10
            s['shots'][1]['hold_seconds']=10
            result=tools.estimate_duration(s,30,duration_mode='target')
            self.assertEqual(result['passed'],expected)
            self.assertEqual(result['min_seconds'],27)

    def test_bad_mode_and_fake_padding_review(self):
        with self.assertRaises(ValueError): validate_request(brief(duration_mode='magic'))
        req=brief(duration_mode='target')
        s=authored_script()
        checked=ToolBox().call('check_rules',dict(script=s,retrieved_ids=['P01'],expression_mode='creative'))
        r=review_fixture(req,s)
        r['pacing']={'verdict':'unmet','evidence':'镜头无内容却停留30秒'}
        self.assertFalse(review_observation(r,req,s,checked)['passed'])

    def test_agent_binds_duration_mode_and_review_adapter(self):
        from src.providers import StructuredModel
        from src.requirements import CREATIVE_REVIEW_SCHEMA
        calls=[]
        class Recorder(StructuredModel):
            def _generate(self, system, content, schema):
                calls.append((system,content,schema)); return {},{}
        Recorder().review(brief(),authored_script(),{})
        self.assertEqual(calls[0][2],CREATIVE_REVIEW_SCHEMA)
        result=Agent(MockModel(),ToolBox()).run(brief(duration_mode='target'))
        duration_calls=[t for t in result['trace'] if t['action']=='estimate_duration']
        self.assertTrue(duration_calls)
        self.assertTrue(all(t['arguments'].get('duration_mode')=='target' for t in duration_calls))


class RevisionQualityTests(unittest.TestCase):
    def test_malformed_pacing_verdict_is_recorded_not_an_uncaught_crash(self):
        for bad in ([], {}, None, True):
            class Malformed(MockModel):
                def review(self, request, script, rules_check=None, duration_check=None):
                    report, meta = super().review(request,script,rules_check)
                    report['pacing']['verdict']=bad
                    return report, meta
            result=Agent(Malformed(),ToolBox()).run(brief())
            self.assertNotEqual(result['status'],'completed')
            self.assertTrue(any(t['observation'].get('error')=='requirements_review_failed' for t in result['trace']))

    def test_agent_reports_actual_local_revision_and_stale_checks_are_cleared(self):
        old=example_script(long=True)
        new=copy.deepcopy(old); new['shots'][0]['hold_seconds']=0; new['shots'][1]['hold_seconds']=0
        sequence=[action('search_materials','查素材',query='字幕'),action('estimate_duration','测旧稿'),
                  action('check_rules','查旧稿'),action('write_script','按超时反馈缩短停留',script=new),
                  action('estimate_duration','复测'),action('check_rules','复查'),
                  action('check_requirements','核对'),action('finish','完成',status='completed')]
        snapshots=[]
        class Sequence(MockModel):
            def decide(self,state,rules):
                snapshots.append(copy.deepcopy(state)); return sequence[len(state['history'])],{'provider':'mock'}
        result=Agent(Sequence(),ToolBox()).run(brief(initial_script=old))
        self.assertEqual(result['status'],'completed')
        revision=next(t['observation']['revision'] for t in result['trace'] if t['action']=='write_script')
        self.assertEqual(revision['changed_fields'],['shot:1/hold_seconds','shot:2/hold_seconds'])
        self.assertEqual(revision['unchanged_blocks'],2)
        self.assertEqual(revision['feedback'][0]['check'],'duration')
        self.assertIsNone(snapshots[4]['rules_check'])
        self.assertIsNone(snapshots[4]['requirements_check'])
        self.assertIsNone(snapshots[4]['duration'])

    def test_trace_replays_creative_mode_with_complete_review(self):
        import tempfile
        from pathlib import Path
        from src.reporting import save_run
        from scripts.verify_evidence import verify_run
        req=brief(duration_mode='max')
        tools=ToolBox(); result=Agent(MockModel(),tools).run(req)
        self.assertEqual(result['status'],'completed')
        with tempfile.TemporaryDirectory(dir=ROOT / '.runtime') as temp:
            save_run(Path(temp),req,result,tools)
            self.assertEqual(verify_run(temp),[])


if __name__ == '__main__': unittest.main()
