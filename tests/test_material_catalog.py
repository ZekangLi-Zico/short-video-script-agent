import hashlib
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from src.tools import ROOT, ToolBox, read_json
from src.providers import StructuredModel
from src.web import RunManager


class MaterialCatalogTests(unittest.TestCase):
    def test_story_project_selects_real_dossier_and_keeps_demo_isolated(self):
        from src.catalog import toolbox_for
        story = toolbox_for({'product_id':'city-drama'})
        demo = toolbox_for({'product_id':'demo-editor'})
        self.assertEqual(story.rules['material_kind'], 'narrative')
        self.assertFalse(story.synthetic_data)
        self.assertEqual(demo.data_hash, ToolBox().data_hash)
        self.assertEqual(story.search_materials('字幕','demo-editor')['count'], 0)
        self.assertEqual(demo.search_materials('陈峥','city-drama')['count'], 0)
        self.assertEqual(toolbox_for({'product_id':'unknown'}).search_materials('字幕','unknown')['count'],0)

    def test_episode_ids_get_precise_cards_among_shared_character_names(self):
        from src.catalog import toolbox_for
        tools = toolbox_for({'product_id':'city-drama'})
        results = tools.search_materials('CZ-E08 CZ-C-QING CZ-S-HOME','city-drama')['materials']
        self.assertEqual({m['id'] for m in results}, {'CZ-E08','CZ-C-QING','CZ-S-HOME'})
        episode = next(m for m in results if m['id']=='CZ-E08')
        text = ' '.join(f['text'] for f in episode['facts'])
        self.assertIn('电路坏了很久',text)
        self.assertNotIn('电路没坏',text)

    def test_all_material_evidence_points_into_unchanged_local_sources(self):
        pack = read_json(ROOT/'data/packs/city-drama/materials.json')
        self.assertEqual(len([m for m in pack['materials'] if m['category']=='分集剧情']),12)
        for source in pack['sources'].values():
            data=(ROOT/'data/packs/city-drama'/source['file']).read_bytes()
            self.assertEqual(hashlib.sha256(data).hexdigest(),source['sha256'])
        for card in pack['materials']:
            self.assertTrue(card['evidence'])
            for r in card['evidence']:
                self.assertLessEqual(1,r['start_line'])
                self.assertLessEqual(r['start_line'],r['end_line'])
                self.assertLessEqual(r['end_line'],pack['sources'][r['source']]['line_count'])

    def test_web_config_exposes_complete_catalog_and_story_briefs(self):
        with tempfile.TemporaryDirectory(dir=ROOT/'.runtime') as d:
            config=RunManager(d).config()
        story=next(p for p in config['material_packs'] if p['id']=='city-drama')
        self.assertEqual(len(story['materials']),32)
        self.assertTrue(any(p['request']['product_id']=='city-drama' for p in config['presets']))
        self.assertEqual(len(config['materials']),3)  # old API field kept

    def test_reviewer_uses_host_material_kind_not_user_label(self):
        model=StructuredModel()
        request={'expression_mode':'creative','material_kind':'narrative'}
        with patch.object(model,'_with_recovery',return_value=({},{})) as call:
            model.review(request,{}, {'material_kind':'narrative'},None)
            self.assertIn('剧情资料',call.call_args.args[0])
            self.assertIn('角色对白',call.call_args.args[0])
            model.review(request,{}, {},None)
            self.assertNotIn('剧情资料',call.call_args.args[0])

    def test_web_worker_and_cli_share_selection(self):
        from src.catalog import story_presets
        from src.cli import main
        preset=story_presets()[0]
        seen=[]
        def record(output,request,model,tools,**kw):
            seen.append(tools.data_hash)
            return {'status':'blocked','message':'test','metadata':{'evidence_kind':'test'},'trace':[],
                    'script':None,'duration':None,'rules_check':None,'requirements_check':None}
        with tempfile.TemporaryDirectory(dir=ROOT/'.runtime') as tmp:
            path=Path(tmp)/'input.json'
            path.write_text(json.dumps(preset['request']),encoding='utf-8')
            with patch('src.cli.run_recorded',side_effect=record):
                main(['--provider','mock','--input',str(path),'--output',str(Path(tmp)/'cli')])
            manager=RunManager(Path(tmp)/'web')
            manager.jobs['test']={'provider':'mock','request':preset['request'],'cancel_event':None}
            with patch('src.web.run_recorded',side_effect=record):
                manager._work('test',{})
            self.assertEqual(len(seen),2)
            self.assertEqual(seen[0],seen[1])
            self.assertNotEqual(seen[0],ToolBox().data_hash)

    def test_custom_material_file_carries_its_own_rules(self):
        from src.cli import main
        seen=[]
        def record(output,request,model,tools,**kw):
            seen.append(tools.rules.get('material_kind'))
            return {'status':'blocked','message':'test','metadata':{'evidence_kind':'test'}}
        with patch('src.cli.run_recorded',side_effect=record):
            main(['--provider','mock','--input',str(ROOT/'examples/inputs/normal.json'),
                  '--materials',str(ROOT/'data/packs/city-drama/materials.json')])
        self.assertEqual(seen,['narrative'])


if __name__=='__main__':
    unittest.main()
