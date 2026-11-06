"""v6 contracts. Adapter stubs are not live-model evidence."""
import copy
import json
import os
import subprocess
import tempfile
import threading
import unittest
from pathlib import Path
from unittest.mock import patch
from src.agent import Agent, ModelError
from src.providers import CodexModel, payload
from src.mock import MockModel, action
from src.tools import ROOT, ToolBox, read_json
from src.recording import run_recorded
from scripts.verify_evidence import verify_run

REQUEST=read_json(ROOT/'examples/inputs/normal.json')

class EfficientMock(MockModel):
    def decide(self,state,rules):
        if state['script'] and not state.get('requirements_check'):
            return action('check_requirements','核对当前稿并取得实际检查反馈'), {'provider':'fixture'}
        return super().decide(state,rules)

class V6Tests(unittest.TestCase):
    def test_creative_payload_has_no_strict_title_or_copy_templates(self):
        state=dict(request={**REQUEST,'expression_mode':'creative'},script=None,retrieved={},duration=None,rules_check=None,history=[],max_steps=12)
        actual=json.loads(payload(state,ToolBox().rules))
        for key in ('allowed_titles','creative_copy','visuals','notes'):self.assertNotIn(key,actual['brand_rules'])
        self.assertIn('forbidden_phrases',actual['brand_rules'])
        state['request']['expression_mode']='strict'
        self.assertEqual(json.loads(payload(state,ToolBox().rules))['brand_rules'],ToolBox().rules)

    def test_history_does_not_repeat_scripts_but_keeps_failed_feedback(self):
        old={'title':'旧稿标记'*100,'shots':[]}
        state=dict(request=REQUEST,script=None,retrieved={},duration=None,rules_check=None,max_steps=12,
                   history=[dict(step=1,action='write_script',arguments={'script':old},decision_basis='修订理由',observation={'ok':True,'script_hash':'old'}),
                            dict(step=2,action='estimate_duration',arguments={'script':old},decision_basis='检查',observation={'ok':True,'passed':False,'total_seconds':38,'issues':['超过30秒']})])
        actual=payload(state,ToolBox().rules)
        self.assertNotIn('旧稿标记',actual);self.assertIn('超过30秒',actual);self.assertIn('修订理由',actual)
        self.assertEqual(state['history'][0]['arguments']['script'],old)

    def test_review_action_runs_and_records_missing_local_checks(self):
        with tempfile.TemporaryDirectory(dir=ROOT/'.runtime') as folder:
            r=run_recorded(folder,REQUEST,EfficientMock(),ToolBox())
            self.assertEqual(r['status'],'completed')
            self.assertEqual([e['action'] for e in r['trace']],['search_materials','write_script','check_requirements','finish'])
            self.assertEqual([e['action'] for e in r['trace'][2]['preflight_checks']],['estimate_duration','check_rules'])
            self.assertEqual(verify_run(folder),[])

    def test_local_failure_does_not_spend_review_call_or_claim_complete(self):
        class NoReview(EfficientMock):
            def review(self,*a,**kw):raise AssertionError('must wait for usable local checks')
        r=Agent(NoReview(),ToolBox(failures={'estimate_duration':-1}),max_steps=3).run(REQUEST)
        self.assertNotEqual(r['status'],'completed')
        self.assertEqual(r['requirements_check']['error'],'local_checks_failed')

    def test_codex_timeout_recovers_once_and_records_attempt(self):
        with patch.dict(os.environ,{'CODEX_BIN':'test-codex.exe'}):
            model=CodexModel()
            with patch.object(model,'_generate',side_effect=[ModelError('codex_timeout; call_id=first'),(action('finish','done',status='needs_input',message='need data'),{'call_id':'second'}),ModelError('codex_timeout; call_id=third'),ModelError('codex_timeout; call_id=fourth')]) as call:
                result,meta=model.decide(dict(request=REQUEST,script=None,retrieved={},duration=None,rules_check=None,history=[],max_steps=12),ToolBox().rules)
                self.assertEqual(meta['recovered_attempts'][0]['call_id'],'first')
                with self.assertRaisesRegex(ModelError,'fourth'):model.review(REQUEST,{},None,None)
                self.assertEqual(call.call_count,4)

    def test_no_recovery_after_cancel_or_non_timeout_error(self):
        with patch.dict(os.environ,{'CODEX_BIN':'test-codex.exe'}):
            for error,cancel in [('codex_timeout; call_id=a',True),('invalid_model_json',False)]:
                model=CodexModel();model.cancel_event=threading.Event()
                if cancel:model.cancel_event.set()
                with patch.object(model,'_generate',side_effect=ModelError(error)) as call:
                    with self.assertRaises(ModelError):model.review(REQUEST,{},None,None)
                    self.assertEqual(call.call_count,1)

    def test_codex_effort_is_per_call_and_visible_in_metadata(self):
        def reply(command,**kwargs):
            self.assertIn('model_reasoning_effort="medium"',command)
            Path(command[command.index('--output-last-message')+1]).write_text('{}',encoding='utf8')
            return subprocess.CompletedProcess(command,0,stdout='',stderr='')
        with patch.dict(os.environ,{'CODEX_BIN':'test-codex.exe','CODEX_REASONING_EFFORT':'medium'}),patch('src.providers.run_cli',side_effect=reply):
            _,meta=CodexModel()._generate('system','{}',{})
        self.assertEqual(meta['reasoning_effort'],'medium')

    def test_interrupted_review_checkpoint_replays_last_completed_state(self):
        from src.recording import recover_run
        class InterruptedReview(EfficientMock):
            def review(self,*a,**kw):raise RuntimeError('simulated interruption')
        with tempfile.TemporaryDirectory(dir=ROOT/'.runtime') as folder:
            r=run_recorded(folder,REQUEST,InterruptedReview(),ToolBox())
            self.assertEqual(r['status'],'blocked')
            self.assertEqual(verify_run(folder),[])

    def test_recovered_diagnostic_and_trace_metadata_match(self):
        calls=[]
        def reply(command,**kwargs):
            calls.append(command)
            if len(calls)==1:raise subprocess.TimeoutExpired('fixture',1)
            Path(command[command.index('--output-last-message')+1]).write_text('{}',encoding='utf8')
            return subprocess.CompletedProcess(command,0,stdout='',stderr='')
        with tempfile.TemporaryDirectory(dir=ROOT/'.runtime') as folder, patch.dict(os.environ,{'CODEX_BIN':'test-codex.exe'}),patch('src.providers.run_cli',side_effect=reply):
            m=CodexModel();m.diagnostics_dir=folder
            _,meta=m.review(REQUEST,{},None,None)
            diag=json.loads((Path(folder)/(meta['call_id']+'.json')).read_text(encoding='utf8'))
            self.assertEqual(diag['metadata'],meta)
            self.assertEqual(len(list(Path(folder).glob('*.json'))),2)

    def test_retrieval_change_refreshes_rule_check_for_existing_draft(self):
        from src.mock import example_script
        class RetrieveAfterCheck(EfficientMock):
            def decide(self,state,rules):
                names=['check_rules','search_materials','check_requirements','finish']
                name=names[len(state['history'])]
                return action(name,'fixture',query='字幕',status='completed' if name=='finish' else 'running',message='完成'),{'provider':'fixture'}
        request={**REQUEST,'initial_script':example_script()}
        with tempfile.TemporaryDirectory(dir=ROOT/'.runtime') as folder:
            r=run_recorded(folder,request,RetrieveAfterCheck(),ToolBox(),max_steps=4)
            self.assertEqual(r['status'],'completed')
            self.assertEqual(verify_run(folder),[])

    def test_cancel_at_review_phase_prevents_new_remote_call(self):
        cancelled=threading.Event()
        class NoReview(EfficientMock):
            def review(self,*a,**kw):raise AssertionError('new call after cancellation')
        def observe(event):
            if event['kind']=='reviewing':cancelled.set()
        result=Agent(NoReview(),ToolBox(),on_event=observe,cancel_event=cancelled).run(REQUEST)
        self.assertEqual(result['status'],'cancelled')
