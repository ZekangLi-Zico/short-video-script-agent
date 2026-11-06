"""Print actual paired briefs/scripts/failed checks for human reading; no grading."""
import json,sys
from pathlib import Path
B=Path(__file__).resolve().parent
OLD=B.parent/'realistic-50-v41-20261104'
load=lambda p:json.loads(p.read_text(encoding='utf8'))
cases={c['id']:c for c in load(B/'cases.json')}
for case in sys.argv[1:]:
    print('\n###',case, cases[case]['name'])
    print('需求',json.dumps(cases[case]['request'],ensure_ascii=False))
    for label,base in [('旧v4.1',OLD),('新v5',B)]:
        d=base/'runs'/case
        if not (d/'output.json').exists():
            print(label,'未完成归档');continue
        o=load(d/'output.json');m=load(d/'manifest.json')
        print(label,o['status'],'秒',(o.get('duration') or {}).get('total_seconds'),'步',m['steps'],'响应',m['model_responses'])
        s=o.get('script')
        if s:
            print('标题',s['title'])
            for i,shot in enumerate(s['shots'],1):
                print(i,shot['visual'])
                if shot.get('purpose'):print('用途',shot['purpose'])
                print(' / '.join(f"[{b.get('channel','旧声画合并')}拍{b.get('beat',1)} {b['source_id']}/{b['fact_id']}] {b['text']}" for b in shot['blocks']))
            print('备注',s.get('editor_notes',''))
        print('说明',o['message'])
        trace=[json.loads(x) for x in (d/'trace.jsonl').read_text(encoding='utf8').splitlines()]
        print('路径',' → '.join(t['action'] for t in trace))
        for t in trace:
            obs=t['observation']
            if obs.get('ok') is False or obs.get('passed') is False:
                print('失败观察',t['step'],t['action'],obs.get('error'),obs.get('message',''),obs.get('issues',''))
                if t['action']=='estimate_duration':print('估时',obs.get('total_seconds'),obs.get('issue'))
                if t['action']=='check_requirements':
                    print('需求未满足',[x for x in obs.get('items',[]) if x['verdict']!='met'])
                    print('表达未满足',[x for x in obs.get('expressions',[]) if x['verdict'] not in ['plain_expression','supported_claim']])
                    print('节奏',obs.get('pacing'))
