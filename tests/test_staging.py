import copy
import unittest

from src.schema import validate_script
from src.tools import ToolBox
from src.expression import expression_slots
from src.listening import listening_copy
from src.reporting import render_report
from src.revisions import revision_summary
from tests.test_effective_v5 import script as old_script, block


def staged_script():
    s = old_script(block('你好', channel='voice', source='', fact=''))
    s['format_version'] = 3
    s['shots'][0]['blocks'][0]['speaker'] = '阿晴'
    s['shots'][0]['staging'] = [dict(beat=1, action='阿晴将饭盒递出，陈峥伸手接住。',
                                  camera='双人中景。', sound='楼道脚步声。', min_seconds=3)]
    return s


class StagingTests(unittest.TestCase):
    def setUp(self): self.tools = ToolBox()

    def test_action_and_speech_overlap_instead_of_adding_description_length(self):
        s = staged_script()
        result = self.tools.call('estimate_duration', dict(script=s, target_seconds=3))
        self.assertTrue(result['ok'])
        self.assertEqual(result['total_seconds'], 3)
        self.assertEqual(result['shots'][0]['beats'][0]['action_seconds'], 3)

    def test_silent_action_has_its_own_time_and_never_enters_voice_export(self):
        s = staged_script()
        s['shots'][0]['staging'].append(dict(beat=2, action='陈峥望向门缝，阿晴收回手。',
                                           camera='', sound='', min_seconds=2))
        r = self.tools.call('estimate_duration', dict(script=s, target_seconds=5))
        self.assertTrue(r['ok'])
        self.assertEqual(r['total_seconds'], 5)
        self.assertEqual(r['shots'][0]['beats'][1]['start_seconds'], 3)
        self.assertEqual(listening_copy(s)['text'], '你好')
        s['shots'][0]['blocks'] = []
        self.assertEqual(self.tools.estimate_duration(s, 5)['total_seconds'], 5)
        self.assertEqual(listening_copy(s)['kind'], 'silent')
        rendered=render_report(dict(status='blocked',message='测试',metadata={'evidence_kind':'test'},
            script=s,duration=self.tools.estimate_duration(s,5),trace=[]))
        self.assertIn('按下方动作与屏幕文字制作',rendered)

    def test_staging_links_and_speakers_are_validated(self):
        validate_script(staged_script())
        for mutation in (
            lambda s:s['shots'][0]['staging'].clear(),
            lambda s:s['shots'][0]['staging'][0].update(beat=2),
            lambda s:s['shots'][0]['staging'][0].update(min_seconds=float('nan')),
            lambda s:s['shots'][0]['blocks'][0].update(speaker=''),
            lambda s:s['shots'][0]['blocks'][0].update(channel='screen'),
        ):
            s=staged_script(); mutation(s)
            with self.assertRaises(ValueError): validate_script(s)
        legacy=old_script(); validate_script(legacy)

    def test_row_projection_keeps_exact_actions_and_does_not_invent_legacy_staging(self):
        from src.staging import shot_rows
        s=staged_script(); timed=self.tools.estimate_duration(s,30)['shots'][0]
        rows=shot_rows(s['shots'][0],timed)
        self.assertEqual(rows[0]['action'],s['shots'][0]['staging'][0]['action'])
        self.assertEqual(rows[0]['blocks'][0]['speaker'],'阿晴')
        self.assertEqual((rows[0]['start_seconds'],rows[0]['end_seconds']),(0,3))
        self.assertIsNone(shot_rows(s['shots'][0],None)[0]['start_seconds'])
        legacy=old_script()
        self.assertEqual(shot_rows(legacy['shots'][0],None)[0]['action'],'')

    def test_actions_camera_and_sound_are_reviewed_and_revision_is_recorded(self):
        s=staged_script(); slots=expression_slots(s)
        stage=next(x for x in slots if x['location']=='shot:1/staging:1')
        self.assertIn('阿晴将饭盒递出',stage['text'])
        self.assertIn('双人中景',stage['text'])
        self.assertIn('楼道脚步声',stage['text'])
        changed=copy.deepcopy(s);changed['shots'][0]['staging'][0]['action']='陈峥退后一步。'
        self.assertIn('shot:1/staging',revision_summary(s,changed,[])['changed_fields'])

    def test_report_pairs_action_with_speaker_without_false_subtitle_note(self):
        s=staged_script();s['shots'][0]['hold_seconds']=5
        r=dict(status='completed',message='完成',metadata={'evidence_kind':'test'},script=s,
               duration=self.tools.estimate_duration(s,30),trace=[])
        report=render_report(r)
        self.assertIn('| 时间（镜内） | 动作与画面 | 对白与声音 |',report)
        self.assertIn('阿晴：你好',report)
        self.assertIn('阿晴将饭盒递出',report)
        self.assertNotIn('同拍声画同步',report)
        self.assertNotIn('保留最后一拍屏幕文字',report)
        self.assertNotIn('保留本段字幕',report)

    def test_creative_model_requests_staged_schema_but_strict_keeps_existing_format(self):
        from src.providers import StructuredModel
        class Capture(StructuredModel):
            def _generate(self,system,content,schema): return schema,{}
        base=dict(request={'expression_mode':'creative'},script=None,retrieved={},duration=None,
                  rules_check=None,requirements_check=None,history=[],max_steps=12)
        schema,_=Capture().decide(base,self.tools.rules)
        self.assertEqual(schema['properties']['script']['anyOf'][0]['properties']['format_version']['enum'],[3])
        base['request']['expression_mode']='strict'
        schema,_=Capture().decide(base,self.tools.rules)
        self.assertEqual(schema['properties']['script']['anyOf'][0]['properties']['format_version']['enum'],[2])

    def test_new_action_fields_cannot_bypass_existing_brand_checks(self):
        s=staged_script(); b=s['shots'][0]['blocks'][0]
        b.update(text='给视频加字幕',source_id='P01',fact_id='P01.F1')
        s['shots'][0]['staging'][0]['action']='展示自动识别所有讲话的按钮。'
        check=self.tools.call('check_rules',dict(script=s,retrieved_ids=['P01'],expression_mode='creative'))
        self.assertTrue(check['ok'])
        self.assertTrue(any(x['code']=='brand_rule_violation' for x in check['issues']))
