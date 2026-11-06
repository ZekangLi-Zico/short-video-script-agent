"""Listening extraction/integration contracts, not a fluency score."""
import copy
import json
import unittest
import tempfile
from pathlib import Path
from src.recording import run_recorded
from src.mock import MockModel
from src.tools import ROOT,ToolBox,read_json
from src.web import RunManager
from src.providers import StructuredModel
from src.version import APP_VERSION


class Capture(StructuredModel):
    def _generate(self, system, content, schema):
        self.sent = json.loads(content)
        return {}, {}


class NaturalVoiceTests(unittest.TestCase):
    def test_review_gets_actual_audible_order_without_screen_notes_or_title(self):
        script = {'format_version':2,'title':'标题不念','editor_notes':'审稿备注不念','shots':[
            {'visual':'画面不念','purpose':'说明不念','blocks':[
                {'beat':2,'channel':'voice','text':'接着检查名称。'},
                {'beat':1,'channel':'screen','text':'SILENT TRANSLATION'},
                {'beat':1,'channel':'both','text':'先把视频看一遍。'},
                {'beat':2,'channel':'voice','text':'确认没有写错。'}]},
            {'blocks':[{'beat':1,'channel':'voice','text':'这就可以交稿了。'}]}]}
        before = copy.deepcopy(script)
        model = Capture()
        model.review({'expression_mode':'creative'},script)
        self.assertIn('listening_copy',model.sent)
        self.assertEqual(model.sent['listening_copy'],{
            'kind':'voice','text':'先把视频看一遍。接着检查名称。确认没有写错。\n\n这就可以交稿了。',
            'shots':[{'shot':1,'text':'先把视频看一遍。接着检查名称。确认没有写错。'},
                     {'shot':2,'text':'这就可以交稿了。'}]})
        self.assertEqual(script,before)

    def test_saved_run_exposes_exact_listening_artifact_and_current_version(self):
        with tempfile.TemporaryDirectory(dir=ROOT/'.runtime') as folder:
            result=run_recorded(folder,read_json(ROOT/'examples/inputs/normal.json'),MockModel(),ToolBox())
            target=Path(folder)
            self.assertTrue((target/'listening.json').is_file())
            copy=json.loads((target/'listening.json').read_text(encoding='utf8'))
            self.assertEqual(copy['kind'],'legacy_unspecified')
            self.assertEqual((target/'voice.txt').read_text(encoding='utf8'),
                             '旧稿合并文案（未区分声画，不能直接视为旁白）\n\n'+copy['text']+'\n')
            self.assertEqual(result['metadata']['app_version'],APP_VERSION)
            manager=RunManager(target/'empty')
            self.assertEqual(manager.config()['app_version'],result['metadata']['app_version'])

    def test_listening_retains_english_spacing_and_excludes_silent_shots(self):
        from src.listening import listening_copy
        script={'format_version':2,'shots':[
            {'blocks':[{'beat':1,'channel':'screen','text':'不朗读'}]},
            {'blocks':[{'beat':1,'channel':'voice','text':'Watch the clip.'},{'beat':2,'channel':'both','text':'Then check the caption.'}]}]}
        self.assertEqual(listening_copy(script),{'kind':'voice','text':'Watch the clip. Then check the caption.','shots':[{'shot':2,'text':'Watch the clip. Then check the caption.'}]})

    def test_silent_and_empty_drafts_do_not_invent_voice(self):
        from src.listening import listening_copy
        self.assertEqual(listening_copy({'format_version':2,'shots':[{'blocks':[{'beat':1,'channel':'screen','text':'只显示'}]}]}),{'kind':'silent','text':'','shots':[]})
        self.assertEqual(listening_copy(None),{'kind':'empty','text':'','shots':[]})


if __name__=='__main__':unittest.main()
