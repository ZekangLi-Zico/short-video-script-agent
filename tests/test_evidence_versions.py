"""Versioned replay must reproduce history without accepting altered observations."""
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts.verify_evidence import verify_run
from src.agent import Agent
from src.mock import MockModel
from src.reporting import save_run
from src.tools import ROOT, ToolBox, read_json


class EvidenceVersionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.scratch=ROOT/'.runtime/tests'
        cls.scratch.mkdir(parents=True,exist_ok=True)

    def test_original_over_duration_replays_without_editing_the_record(self):
        self.assertEqual(verify_run(ROOT/'examples/live/over_duration'), [])

    def test_legacy_replay_still_rejects_changed_search_results(self):
        with tempfile.TemporaryDirectory(dir=self.scratch) as folder:
            dst=Path(folder)/'old'
            shutil.copytree(ROOT/'examples/live/over_duration',dst)
            entries=[json.loads(s) for s in (dst/'trace.jsonl').read_text(encoding='utf-8').splitlines()]
            entries[2]['observation']['materials']=entries[2]['observation']['materials'][:1]
            entries[2]['observation']['count']=1
            (dst/'trace.jsonl').write_text(''.join(json.dumps(e,ensure_ascii=False)+'\n' for e in entries),encoding='utf-8')
            self.assertTrue(verify_run(dst))

    def test_contract_selection_is_explicit_not_chosen_by_saved_success(self):
        from scripts.replay_compat import search_contract, replay_tools
        self.assertEqual(search_contract({}), ('keyword_v1','legacy_unversioned'))
        self.assertEqual(search_contract({'app_version':'v7-natural-voice'}),('keyword_v1','app_version'))
        self.assertEqual(search_contract({'app_version':'v7.3-staged-storyboard'}),('id_first_v2','app_version'))
        snapshot=read_json(ROOT/'examples/live/over_duration/data_snapshot.json')
        old=replay_tools(snapshot,{}).search_materials('demo-editor 剪影练习版 字幕功能 P01','demo-editor')
        new=replay_tools(snapshot,{'app_version':'v7.3-staged-storyboard'}).search_materials('demo-editor 剪影练习版 字幕功能 P01','demo-editor')
        self.assertEqual([m['id'] for m in old['materials']],['P01','P02','P03'])
        self.assertEqual([m['id'] for m in new['materials']],['P01'])
        for manifest in ({'app_version':'unknown-build'}, {'tool_contracts':{'search_materials':'unknown'}},
                         {'app_version':'v7.3-staged-storyboard','tool_contracts':{'search_materials':'keyword_v1'}}):
            with self.assertRaises(ValueError): search_contract(manifest)

    def test_new_record_pins_search_contract_and_replays(self):
        with tempfile.TemporaryDirectory(dir=self.scratch) as folder:
            tools=ToolBox(); req=read_json(ROOT/'examples/inputs/normal.json')
            result=Agent(MockModel(),tools).run(req)
            save_run(folder,req,result,tools)
            self.assertEqual(read_json(Path(folder)/'manifest.json')['tool_contracts']['search_materials'],'id_first_v2')
            self.assertEqual(verify_run(folder),[])

    def test_cli_writes_new_report_and_preserves_original_audit(self):
        from scripts.verify_evidence import main
        before=(ROOT/'examples/evidence-audit.json').read_bytes()
        with tempfile.TemporaryDirectory(dir=self.scratch) as folder:
            target=Path(folder)/'report.json'
            with patch('builtins.print'):
                code=main(['--run',str(ROOT/'examples/live/over_duration'),'--output',str(target)])
            report=read_json(target)
            self.assertEqual(code,0)
            self.assertEqual(report['runs'][0]['search_contract'],'keyword_v1')
            self.assertEqual((ROOT/'examples/evidence-audit.json').read_bytes(),before)

    def test_cli_reports_missing_record_as_failure(self):
        from scripts.verify_evidence import main
        with tempfile.TemporaryDirectory(dir=self.scratch) as folder:
            target=Path(folder)/'report.json'
            with patch('builtins.print'):
                code=main(['--run',str(Path(folder)/'missing'),'--output',str(target)])
            self.assertEqual(code,1)
            self.assertFalse(read_json(target)['passed'])


if __name__=='__main__': unittest.main()
