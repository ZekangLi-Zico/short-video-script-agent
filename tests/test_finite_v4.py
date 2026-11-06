"""Fault/contract regressions; these fixtures are not real-model evidence."""
import copy
import json
import os
import subprocess
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from src.agent import Agent
from src.mock import MockModel, action
from src.providers import CodexModel, StructuredModel
from src.tools import ROOT, ToolBox, read_json
from src.web import RunManager
from tests.test_web import wait_finished
from src.agent import ModelError
from src.requirements import bound_duration_check
from src.recording import run_recorded, recover_run, EvidenceSaveError
from src.reporting import atomic_json
from scripts.verify_evidence import verify_run


REQUEST = read_json(ROOT / 'examples/inputs/normal.json')


class DurationContextTests(unittest.TestCase):
    def test_stale_draft_target_or_mode_is_not_sent_as_trusted_timing(self):
        result = Agent(MockModel(),ToolBox()).run(REQUEST)
        self.assertEqual(bound_duration_check(result['duration'],REQUEST,result['script']),result['duration'])
        for change in ({'script_hash':'old'}, {'target_seconds':299}, {'duration_mode':'target'}, {'ok':False}):
            self.assertIsNone(bound_duration_check({**result['duration'],**change},REQUEST,result['script']))

    def test_valid_timing_does_not_override_unmet_content_review(self):
        class Unmet(MockModel):
            def review(self, request, script, rules_check=None, duration_check=None):
                report,meta=super().review(request,script,rules_check,duration_check)
                report['items'][0]['verdict']='unmet'
                report['items'][0]['evidence']='fixture: missing requested scene'
                return report,meta
        result=Agent(Unmet(),ToolBox()).run(REQUEST)
        self.assertTrue(result['duration']['passed'])
        self.assertNotEqual(result['status'],'completed')

    def test_agent_passes_actual_current_timing_to_reviewer(self):
        received = []
        class Reviewer(MockModel):
            def review(self, request, script, rules_check=None, duration_check=None):
                received.append(copy.deepcopy(duration_check))
                return super().review(request, script, rules_check)
        result = Agent(Reviewer(), ToolBox()).run(REQUEST)
        self.assertEqual(received, [result['duration']])
        self.assertGreater(received[0]['shots'][0]['estimated_seconds'], 0)
        self.assertEqual(result['script']['shots'][0]['hold_seconds'], 0)

    def test_adapter_sends_bound_timing_and_hold_semantics(self):
        calls = []
        class Recorder(StructuredModel):
            def _generate(self, system, content, schema):
                calls.append((system,json.loads(content))); return {},{}
        timing = {'script_hash':'test-hash','shots':[{'shot':1,'estimated_seconds':7.8}], 'passed':True}
        Recorder().review(REQUEST, {'title':'fixture','shots':[]}, {}, timing)
        self.assertEqual(calls[0][1]['duration_check'], timing)
        self.assertIn('0不代表镜头时长为0', calls[0][0])


class EvidenceDurabilityTests(unittest.TestCase):
    def test_active_owner_is_not_recovered_by_another_manager(self):
        with tempfile.TemporaryDirectory(dir=ROOT/'.runtime') as folder:
            class PauseProcess(BaseException):pass
            def pause(event):
                if event['kind']=='thinking':raise PauseProcess()
            with self.assertRaises(PauseProcess):
                run_recorded(folder,REQUEST,MockModel(),ToolBox(),on_event=pause)
            self.assertIsNone(recover_run(folder))
            self.assertFalse((Path(folder)/'output.json').exists())

    def test_cleanup_lock_does_not_replace_model_timeout(self):
        with patch.dict(os.environ, {'CODEX_BIN':'test-codex.exe'}), \
             patch('src.providers.run_cli',side_effect=subprocess.TimeoutExpired('test',1)), \
             patch('tempfile.TemporaryDirectory.cleanup',side_effect=PermissionError(32,'fixture lock')):
            with self.assertRaisesRegex(ModelError,'codex_timeout'):
                CodexModel()._generate('test','{}',{})

    def test_failed_final_save_leaves_recoverable_checkpoint_without_new_calls(self):
        with tempfile.TemporaryDirectory(dir=ROOT/'.runtime') as folder:
            with patch('src.recording.save_run',side_effect=OSError('fixture disk write failure')):
                with self.assertRaises(EvidenceSaveError):
                    run_recorded(folder,REQUEST,MockModel(),ToolBox())
            self.assertFalse((Path(folder)/'output.json').exists())
            self.assertTrue((Path(folder)/'checkpoint.json').is_file())
            self.assertTrue(recover_run(folder))
            output=json.loads((Path(folder)/'output.json').read_text(encoding='utf-8'))
            self.assertEqual(output['status'],'blocked')
            self.assertTrue(output['script'])
            self.assertEqual(verify_run(folder),[])
            self.assertFalse(recover_run(folder))

    def test_checkpoint_is_durable_before_next_model_call_and_restart_never_completes_it(self):
        class SimulatedProcessStop(BaseException): pass
        with tempfile.TemporaryDirectory(dir=ROOT/'.runtime') as folder:
            class Stops(MockModel):
                def decide(model_self,state,rules):
                    if len(state['history'])==2:
                        saved=json.loads((Path(folder)/'checkpoint.json').read_text(encoding='utf-8'))
                        self.assertEqual(len(saved['result']['trace']),2)
                        self.assertEqual(saved['result']['script'],state['script'])
                        raise SimulatedProcessStop()
                    return super().decide(state,rules)
            with self.assertRaises(SimulatedProcessStop):
                run_recorded(folder,REQUEST,Stops(),ToolBox())
            with patch('src.recording.owner_running',return_value=False):
                self.assertTrue(recover_run(folder))
            output=json.loads((Path(folder)/'output.json').read_text(encoding='utf-8'))
            self.assertEqual(output['status'],'blocked')
            self.assertEqual(output['metadata']['steps'],2)
            self.assertEqual(verify_run(folder),[])

    def test_atomic_replace_failure_keeps_previous_valid_checkpoint(self):
        with tempfile.TemporaryDirectory(dir=ROOT/'.runtime') as folder:
            target=Path(folder)/'checkpoint.json'
            atomic_json(target,{'step':2})
            with patch('src.reporting.os.replace',side_effect=PermissionError('fixture target lock')):
                with self.assertRaises(PermissionError): atomic_json(target,{'step':3})
            self.assertEqual(json.loads(target.read_text(encoding='utf-8')),{'step':2})

    def test_checkpoint_from_another_run_cannot_be_restored(self):
        with tempfile.TemporaryDirectory(dir=ROOT/'.runtime') as folder:
            run_recorded(folder,REQUEST,MockModel(),ToolBox())
            record=json.loads((Path(folder)/'run.json').read_text(encoding='utf-8'))
            atomic_json(Path(folder)/'run.json',{**record,'state':'recording','run_id':'different'})
            with self.assertRaisesRegex(ValueError,'不匹配'):recover_run(folder)

    def test_diagnostics_are_per_call_and_do_not_copy_raw_provider_output(self):
        with tempfile.TemporaryDirectory(dir=ROOT/'.runtime') as folder:
            def failed(command,**kwargs):
                return subprocess.CompletedProcess(command,1,stdout='Selected model is at capacity. secret-fixture',stderr='private body')
            with patch.dict(os.environ,{'CODEX_BIN':'test-codex.exe'}),patch('src.providers.run_cli',side_effect=failed):
                model=CodexModel();model.diagnostics_dir=Path(folder)
                for _ in range(2):
                    with self.assertRaises(ModelError):model._generate('test','{}',{})
            files=list(Path(folder).glob('decision-*.json'))
            self.assertEqual(len(files),2)
            for file in files:
                text=file.read_text(encoding='utf-8')
                self.assertNotIn('secret-fixture',text)
                self.assertNotIn('private body',text)
                self.assertEqual(json.loads(text)['provider_error_code'],'model_at_capacity')

    def test_valid_codex_response_survives_cleanup_lock(self):
        expected = action('search_materials','fixture',query='字幕')
        def reply(command, **kwargs):
            Path(command[command.index('--output-last-message')+1]).write_text(json.dumps(expected),encoding='utf-8')
            return subprocess.CompletedProcess(command,0,stdout='{"type":"turn.completed","usage":{}}\n',stderr='')
        with patch.dict(os.environ, {'CODEX_BIN':'test-codex.exe'}), patch('src.providers.run_cli',side_effect=reply), \
             patch('tempfile.TemporaryDirectory.cleanup',side_effect=PermissionError(32,'fixture lock')):
            actual, meta = CodexModel()._generate('test','{}',{})
        self.assertEqual(actual, expected)
        self.assertIn('cleanup_deferred', meta['warnings'])

    def test_unexpected_exception_preserves_last_completed_steps_and_draft(self):
        class CrashesAfterDraft(MockModel):
            def decide(self, state, rules):
                if len(state['history']) == 2:
                    raise RuntimeError('private diagnostic must not reach user')
                return super().decide(state,rules)
        with tempfile.TemporaryDirectory(dir=ROOT/'.runtime') as folder:
            manager = RunManager(folder,lambda provider,timeout:CrashesAfterDraft())
            run_id = manager.start({'provider':'mock','request':REQUEST})
            job = wait_finished(manager,run_id)
            self.assertTrue(job['saved'])
            self.assertEqual(job['result']['status'],'blocked')
            self.assertEqual(len(job['trace']),2)
            self.assertIsNotNone(job['script'])
            checkpoint = json.loads((Path(folder)/run_id/'checkpoint.json').read_text(encoding='utf-8'))
            self.assertEqual(len(checkpoint['result']['trace']),2)
            self.assertNotIn('private diagnostic',json.dumps(job))
            restored = RunManager(folder,lambda *_:self.fail('must not invoke a model on restore')).get(run_id)
            self.assertEqual(restored['result']['status'],'blocked')
            self.assertEqual(restored['script'],job['script'])


if __name__ == '__main__': unittest.main()
