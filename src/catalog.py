"""Small, local materials catalog shared by web and CLI; old defaults stay stable."""
from .tools import ROOT, ToolBox, read_json

STORY_FILE = ROOT / 'data/packs/city-drama/materials.json'


def toolbox_for(request, failures=None):
    if request.get('product_id') == 'city-drama':
        pack = read_json(STORY_FILE)
        return ToolBox(materials=pack['materials'], rules=pack['rules'], failures=failures,
                       synthetic_data=pack['synthetic'])
    return ToolBox(failures=failures)


def story_presets():
    return read_json(ROOT / 'data/packs/city-drama/briefs.json')


def material_catalog():
    story = read_json(STORY_FILE)
    return [
        {k: story[k] for k in ('id','name','description','material_kind','materials','provenance_note')},
        {'id':'demo-editor','name':'剪影练习版 · 原产品示例', 'material_kind':'product',
         'description':'原笔试的虚构产品样例，保留字幕、手动编辑、裁剪和画面比例四项事实。',
         'provenance_note':'合成产品资料，用于原题验收；不代表真实产品。',
         'materials':[m for m in ToolBox().materials if m['product_id']=='demo-editor']},
        {'id':'product-without-materials','name':'无素材项目 · 资料不足测试', 'material_kind':'product',
         'description':'没有可用资料，用于核查补查与请求补充。','provenance_note':'','materials':[]},
    ]
