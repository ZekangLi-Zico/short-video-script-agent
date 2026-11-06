"""Select deterministic replay semantics from recorded versions, never observations.

keyword_v1 is the search implementation in commit
e624c5a872f26fb0689fcc6a3e246da35edccbb7, src/tools.py. The ID-first
branch arrived with v7.1; v7 and earlier unversioned records used keywords.
Only search semantics changed; existing script formats select their timing rules.
"""
import copy
import re

from src.tools import ToolBox

LEGACY_VERSIONS = {None, 'v7-natural-voice'}
ID_FIRST_VERSIONS = {'v7.1-story-materials','v7.2-call-reliability',
                     'v7.3-staged-storyboard','v7.3.1-submission'}


def search_contract(manifest):
    version=manifest.get('app_version')
    declared=manifest.get('tool_contracts',{}).get('search_materials')
    inferred='keyword_v1' if version in LEGACY_VERSIONS else 'id_first_v2' if version in ID_FIRST_VERSIONS else None
    if declared is not None:
        if declared not in {'keyword_v1','id_first_v2'}:
            raise ValueError(f'未知检索复算版本：{declared}')
        if version is not None and inferred and declared!=inferred:
            raise ValueError('记录的检索版本与应用版本冲突')
        return declared,'manifest'
    if inferred:
        return inferred,'legacy_unversioned' if version is None else 'app_version'
    raise ValueError(f'应用版本缺少已知检索复算契约：{version}')


class LegacySearchTools(ToolBox):
    search_contract='keyword_v1'

    def search_materials(self,query,product_id):
        if not isinstance(query,str) or not 1<=len(query.strip())<=200:
            raise ValueError('query 必须为 1–200 字符')
        q=query.strip().casefold()
        terms=re.findall(r'[a-z0-9]+|[\u3400-\u9fff]+',q)
        ranked=[]
        for item in self.materials:
            if item['product_id']!=product_id: continue
            haystack=' '.join([item['title'],*item['keywords'],*(f['text'] for f in item['facts'])]).casefold()
            score=sum(2 for word in item['keywords'] if word.casefold() in q)
            score+=sum(1 for term in terms if term in haystack)
            if score: ranked.append((score,item))
        ranked.sort(key=lambda entry:(-entry[0],entry[1]['id']))
        return {'query':query,'product_id':product_id,'materials':[copy.deepcopy(item) for _,item in ranked[:5]],
                'count':len(ranked[:5])}


def replay_tools(snapshot,manifest):
    contract,_=search_contract(manifest)
    cls=LegacySearchTools if contract=='keyword_v1' else ToolBox
    return cls(snapshot['materials'],snapshot['rules'],manifest.get('fault_injection',{}))
