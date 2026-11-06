"""Behavioral contracts for usable wording and explicit audiovisual beats."""
import copy
import unittest
from src.tools import ToolBox
from src.schema import validate_script
from src.expression import expression_slots, validate_expression_review


def block(text='给视频加字幕', channel='both', beat=1, source='P01', fact='P01.F1', display=0):
    return dict(text=text, source_id=source, fact_id=fact, channel=channel, beat=beat, display_seconds=display)


def script(*blocks):
    return dict(format_version=2, title='今天的记录', editor_notes='', shots=[
        dict(purpose='让观众看到字幕如何承载这段画面中的话', visual='字幕叠加在拍摄画面上', hold_seconds=0, blocks=list(blocks or [block()]))])


class EffectiveV5Tests(unittest.TestCase):
    def setUp(self): self.tools=ToolBox()

    def test_versioned_script_accepted_and_legacy_unchanged(self):
        self.assertTrue(self.tools.call('estimate_duration',dict(script=script(),target_seconds=30))['ok'])
        from src.mock import example_script
        validate_script(example_script())

    def test_paraphrase_is_reviewable_with_actual_source_quote(self):
        result=self.tools.call('check_rules',dict(script=script(),retrieved_ids=['P01'],expression_mode='creative'))
        self.assertTrue(result['ok']); self.assertTrue(result['passed'])
        self.assertEqual(result['citations'][0]['quote'],'剪影练习版支持为视频添加字幕。')
        self.assertEqual(result['citations'][0]['text'],'给视频加字幕')
        self.assertTrue(result['citations'][0]['requires_semantic_review'])
        self.assertEqual(len(result['expression_slots']),3)

    def test_same_text_voice_and_screen_are_simultaneous(self):
        s=script(block('今天一起记录生活',channel='voice'),block('今天一起记录生活',channel='screen'))
        result=self.tools.call('estimate_duration',dict(script=s,target_seconds=3))
        self.assertTrue(result['ok']); self.assertEqual(result['total_seconds'],2.5)
        self.assertTrue(result['passed'])

    def test_screen_cards_in_distinct_beats_are_sequential(self):
        s=script(block('今天一起记录生活',channel='screen'),block('今天一起记录生活',channel='screen',beat=2))
        result=self.tools.call('estimate_duration',dict(script=s,target_seconds=4))
        self.assertTrue(result['ok']); self.assertEqual(result['total_seconds'],5.0)
        self.assertFalse(result['passed'])
        self.assertEqual(result['shots'][0]['beats'][1]['start_seconds'],2.5)

    def test_all_simultaneous_screen_text_needs_reading_time(self):
        s=script(block('今天一起记录生活',channel='screen'),block('明天接着继续拍摄',channel='screen'))
        r=self.tools.call('estimate_duration',dict(script=s,target_seconds=4))
        self.assertTrue(r['ok']); self.assertEqual(r['total_seconds'],4.5)

    def test_english_speech_rate_not_four_words_per_second(self):
        s=script(block('Add captions to your video and tell your own story',channel='voice'))
        r=self.tools.call('estimate_duration',dict(script=s,target_seconds=4))
        self.assertTrue(r['ok']); self.assertEqual(r['total_seconds'],4.5)
        self.assertFalse(r['passed'])

    def test_screen_hold_is_not_spoken_and_notes_not_timed(self):
        s=script(block('字幕',channel='screen',display=6)); s['editor_notes']='只展示文字，不需要旁白。'*30
        r=self.tools.call('estimate_duration',dict(script=s,target_seconds=6))
        self.assertTrue(r['ok']); self.assertEqual(r['total_seconds'],6)
        self.assertEqual(r['shots'][0]['beats'][0]['voice_seconds'],0)

    def test_wrong_source_and_strict_rewrite_are_rejected(self):
        self.assertFalse(self.tools.call('check_rules',dict(script=script(block(source='OTHER01')),retrieved_ids=['P01'],expression_mode='creative')).get('passed',False))
        self.assertFalse(self.tools.call('check_rules',dict(script=script(),retrieved_ids=['P01'],expression_mode='strict')).get('passed',False))

    def test_bound_rewrite_cannot_be_approved_as_plain_expression(self):
        s=script(); checked=self.tools.call('check_rules',dict(script=s,retrieved_ids=['P01'],expression_mode='creative'))
        self.assertTrue(checked['ok'])
        r={'expressions':[dict(**slot,verdict='plain_expression',references=[],evidence='test') for slot in expression_slots(s)],
           'pacing':dict(verdict='met',evidence='test')}
        with self.assertRaises(ValueError): validate_expression_review(r,{'expression_mode':'creative'},s,checked)
        r['expressions'][-1].update(verdict='supported_claim',references=[dict(source_id='P01',fact_id='P01.F1')])
        self.assertTrue(validate_expression_review(r,{'expression_mode':'creative'},s,checked))
        r['expressions'][-1]['references']=[dict(source_id='P01',fact_id='P01.F2')]
        with self.assertRaises(ValueError): validate_expression_review(r,{'expression_mode':'creative'},s,checked)

    def test_semantic_rejection_of_added_capability_blocks_completion(self):
        s=script(block('自动识别每句话')); checked=self.tools.call('check_rules',dict(script=s,retrieved_ids=['P01'],expression_mode='creative'))
        self.assertTrue(checked['ok']); self.assertFalse(checked['passed'])

    def test_malformed_channel_beat_and_partial_fields_rejected(self):
        for field,value in [('channel','silent'),('beat',True),('beat',0),('display_seconds',float('nan'))]:
            s=script();s['shots'][0]['blocks'][0][field]=value
            with self.assertRaises(ValueError): validate_script(s)
        s=script();del s['shots'][0]['blocks'][0]['channel']
        with self.assertRaises(ValueError): validate_script(s)

    def test_rendered_script_distinguishes_channels_and_purpose(self):
        from src.reporting import render_report
        s=script(block('给视频加字幕',channel='voice'),block('Add captions to video',channel='screen'))
        report=render_report(dict(status='completed',message='完成',metadata={'evidence_kind':'test'},script=s,
            duration=self.tools.estimate_duration(s,30),trace=[]))
        self.assertIn('旁白：给视频加字幕',report)
        self.assertIn('屏幕文字：Add captions to video',report)
        self.assertIn('同一时段的配音和屏幕文字同时播放',report)
        self.assertIn('镜头目的：',report)

    def test_purpose_edit_is_recorded_as_actual_revision(self):
        from src.revisions import revision_summary
        s=script(); changed=copy.deepcopy(s);changed['shots'][0]['purpose']='用字幕保留采访中的原话'
        self.assertIn('shot:1/purpose',revision_summary(s,changed,[])['changed_fields'])

    def test_tail_hold_is_visible_to_editor(self):
        from src.reporting import render_report
        s=script(block('字幕',channel='screen'));s['shots'][0]['hold_seconds']=12
        report=render_report(dict(status='completed',message='完成',metadata={'evidence_kind':'test'},script=s,
            duration=self.tools.estimate_duration(s,30),trace=[]))
        self.assertIn('镜头末尾保持画面：1.0–12.0 秒',report)

    def test_semantic_rejection_is_not_structural_error(self):
        s=script(block('一键完成所有字幕')); checked=self.tools.call('check_rules',dict(script=s,retrieved_ids=['P01'],expression_mode='creative'))
        self.assertTrue(checked['passed'])
        r={'expressions':[dict(**slot,verdict='plain_expression',references=[],evidence='test') for slot in expression_slots(s)],'pacing':dict(verdict='met',evidence='test')}
        r['expressions'][-1].update(verdict='unsupported_claim',references=[],evidence='素材没有一键自动能力')
        self.assertFalse(validate_expression_review(r,{'expression_mode':'creative'},s,checked))

    def test_editorial_purpose_does_not_trigger_public_brand_rule(self):
        s=script();s['shots'][0]['purpose']='删除原稿中的自动识别说法，只保留添加字幕'
        self.assertTrue(self.tools.check_rules(s,['P01'],'creative')['passed'])
        s['shots'][0]['visual']='屏幕写出自动识别所有讲话'
        self.assertFalse(self.tools.check_rules(s,['P01'],'creative')['passed'])

    def test_saved_v2_run_replays_with_same_checks(self):
        import tempfile
        from pathlib import Path
        from src.agent import Agent
        from src.mock import MockModel,action
        from src.reporting import save_run
        from scripts.verify_evidence import verify_run
        s=script();req=dict(topic='添加字幕',audience='创作者',platform='抖音',style='简洁',target_seconds=30,product_id='demo-editor',expression_mode='creative')
        req['product_id']=self.tools.materials[0]['product_id']
        class Model(MockModel):
            def decide(self,state,rules):
                steps=[action('search_materials','查原文',query='字幕'),action('write_script','按场景压缩事实',script=s),action('estimate_duration','测声画'),action('check_rules','核对来源'),action('check_requirements','检查表达'),action('finish','完成',status='completed')]
                return steps[len(state['history'])],{'provider':'mock'}
            def review(self,request,script,rules_check=None,duration_check=None):
                r,m=super().review(request,script,rules_check,duration_check)
                r['expressions'][-1].update(verdict='supported_claim',references=[dict(source_id='P01',fact_id='P01.F1')])
                return r,m
        result=Agent(Model(),self.tools).run(req)
        self.assertEqual(result['status'],'completed')
        from src.tools import ROOT
        with tempfile.TemporaryDirectory(dir=ROOT / '.runtime') as tmp:
            save_run(tmp,req,result,self.tools)
            self.assertEqual(verify_run(Path(tmp)),[])


if __name__=='__main__': unittest.main()
