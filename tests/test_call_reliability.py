"""Call-boundary regressions: stubs verify recovery, real web runs are separate evidence."""
import copy
import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

from src.agent import Agent, ModelError
from src.mock import MockModel, action
from src.providers import CodexModel, payload, run_cli
from src.tools import ROOT, ToolBox, read_json

REQUEST = read_json(ROOT/'examples/inputs/normal.json')


def state():
    return dict(request=REQUEST,script=None,retrieved={},duration=None,rules_check=None,
                requirements_check=None,history=[],max_steps=12)


class CallReliabilityTests(unittest.TestCase):
    def test_timeout_preserves_output_drained_after_termination(self):
        process = Mock(pid=123456789)
        process.communicate.side_effect = [subprocess.TimeoutExpired('fixture',1),('partial events','connection lost')]
        with patch('subprocess.Popen',return_value=process),patch('subprocess.run'),patch('os.killpg',create=True):
            with self.assertRaises(subprocess.TimeoutExpired) as caught:
                run_cli(['fixture'],input='',timeout=1,cwd='.')
        self.assertEqual(caught.exception.stdout,'partial events')
        self.assertEqual(caught.exception.stderr,'connection lost')

    def test_failure_diagnostics_keep_phase_and_safe_signals_not_body(self):
        secret='private-text-not-for-log'
        events='\n'.join(json.dumps(e) for e in [
            {'type':'thread.started','thread_id':'fixture-thread'}, {'type':'turn.started'},
            {'type':'item.completed','item':{'type':'reasoning','text':secret}},
            {'type':'error','message':'stream disconnected: '+secret}])
        with tempfile.TemporaryDirectory(dir=ROOT/'.runtime') as folder,patch.dict(os.environ,{'CODEX_BIN':'test-codex.exe'}):
            model=CodexModel();model.diagnostics_dir=Path(folder)
            with patch('src.providers.run_cli',side_effect=subprocess.TimeoutExpired('fixture',1,output=events,stderr='Bearer '+secret)):
                with self.assertRaises(ModelError):model.review(REQUEST,{},None,None)
            records=[read_json(p) for p in Path(folder).glob('*.json')]
            self.assertEqual(len(records),2)
            for record in records:
                self.assertEqual(record['phase'],'review')
                self.assertEqual(record['runtime']['last_event'],'error')
                self.assertIn('stream_disconnected',record['runtime']['signals'])
                self.assertEqual(record['metadata']['thread_id'],'fixture-thread')
                self.assertGreaterEqual(record['elapsed_seconds'],0)
                self.assertNotIn(secret,json.dumps(record))

    def test_decision_and_later_review_each_can_recover_with_run_budget(self):
        reply=(action('finish','fixture',status='needs_input',message='缺资料'),{'call_id':'ok'})
        with patch.dict(os.environ,{'CODEX_BIN':'test-codex.exe'}):
            model=CodexModel()
            with patch.object(model,'_generate',side_effect=[ModelError('codex_timeout; call_id=d'),reply,
                    ModelError('codex_timeout; call_id=r'),({}, {'call_id':'review-ok'}),
                    ModelError('codex_timeout; call_id=budget')]) as generate:
                model.decide(state(),ToolBox().rules)
                _,meta=model.review(REQUEST,{},None,None)
                self.assertEqual(meta['recovered_attempts'][0]['call_id'],'r')
                with self.assertRaisesRegex(ModelError,'budget'):model.decide(state(),ToolBox().rules)
                self.assertEqual(generate.call_count,5)

    def test_exhausted_review_stops_without_spending_another_decision(self):
        class FailedReviewer(MockModel):
            def decide(self,s,r):
                if s.get('requirements_check'):raise AssertionError('decision after unavailable review')
                if s['script']:return action('check_requirements','核对当前稿'),{'provider':'fixture'}
                return super().decide(s,r)
            def review(self,*args,**kwargs):raise ModelError('codex_timeout; call_id=review')
        result=Agent(FailedReviewer(),ToolBox()).run(REQUEST)
        self.assertEqual(result['status'],'blocked')
        self.assertIsNotNone(result['script'])
        self.assertEqual(result['trace'][-1]['action'],'check_requirements')
        self.assertIn('审核',result['message'])
        self.assertFalse(result['requirements_check']['ok'])

    def test_decision_compacts_duplicate_checks_but_keeps_failed_feedback(self):
        s=state()
        s['rules_check']={'ok':True,'passed':True,'script_hash':'x','available_facts':[{'quote':'repeated-fact'*50}],
                          'citations':[{'quote':'repeated-fact'*50}],'expression_slots':[{'text':'repeated-script'*50}]}
        s['requirements_check']={'ok':True,'passed':False,'script_hash':'x','request_hash':'r','summary':'需修订',
            'items':[{'verdict':'met','requirement':'already satisfied'},{'verdict':'unmet','requirement':'必须交代原因'}],
            'expressions':[{'verdict':'plain_expression','text':'checked text'},
                           {'verdict':'unsupported_claim','text':'无依据承诺','evidence':'资料未说明'}]}
        before=copy.deepcopy(s)
        actual=json.loads(payload(s,ToolBox().rules))
        self.assertNotIn('available_facts',actual['rules_check'])
        self.assertNotIn('repeated-script',json.dumps(actual))
        self.assertEqual(actual['requirements_check']['unmet_items'][0]['requirement'],'必须交代原因')
        self.assertEqual(actual['requirements_check']['failed_expressions'][0]['text'],'无依据承诺')
        self.assertEqual(s,before)

    def test_default_openai_configuration_is_scoped_and_model_preserved(self):
        with tempfile.TemporaryDirectory(dir=ROOT/'.runtime') as folder:
            Path(folder,'config.toml').write_text('model="fixture-model"\nservice_tier="fast"\n[mcp_servers.unrelated]\ncommand="unused-secret-marker"\n',encoding='utf-8')
            def reply(command,**kwargs):
                self.assertIn('--ignore-user-config',command)
                self.assertEqual(command[command.index('--model')+1],'fixture-model')
                self.assertIn('service_tier="fast"',command)
                self.assertIn('read-only',command)
                self.assertNotIn('unused-secret-marker',str(command))
                Path(command[command.index('--output-last-message')+1]).write_text('{}',encoding='utf-8')
                return subprocess.CompletedProcess(command,0,'','')
            with patch.dict(os.environ,{'CODEX_BIN':'test-codex.exe','CODEX_HOME':folder},clear=True),patch('src.providers.run_cli',side_effect=reply):
                _,meta=CodexModel()._generate('system','{}',{})
                self.assertEqual(meta['configuration_mode'],'isolated')

    def test_custom_provider_configuration_is_not_silently_dropped(self):
        with tempfile.TemporaryDirectory(dir=ROOT/'.runtime') as folder:
            Path(folder,'config.toml').write_text('model="fixture-model"\nmodel_provider="custom"\n',encoding='utf-8')
            def reply(command,**kwargs):
                self.assertNotIn('--ignore-user-config',command)
                Path(command[command.index('--output-last-message')+1]).write_text('{}',encoding='utf-8')
                return subprocess.CompletedProcess(command,0,'','')
            with patch.dict(os.environ,{'CODEX_BIN':'test-codex.exe','CODEX_HOME':folder},clear=True),patch('src.providers.run_cli',side_effect=reply):
                _,meta=CodexModel()._generate('system','{}',{})
                self.assertEqual(meta['configuration_mode'],'inherited_custom_provider')


if __name__=='__main__':unittest.main()
