import argparse,csv,hashlib,json,sys
from collections import Counter
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
from scripts.verify_evidence import verify_run
B=ROOT/'evaluations/realistic-50-v3-20261104'
load=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
p=argparse.ArgumentParser();p.add_argument('--full',action='store_true');args=p.parse_args()
baseline=load(B/'baseline.json');cases=load(B/'cases.json');rows=[]
assert sha(B/'cases.json')==baseline['cases_sha256']
changed=[k for k,v in baseline['source_sha256'].items() if sha(ROOT/k)!=v]
assert not changed,changed
for c in cases:
    d=B/'runs'/c['id']
    if not (d/'capture.json').exists():continue
    if (d/'infrastructure-error.json').exists():
        r=load(d/'infrastructure-error.json')
        rows.append(dict(case=c['id'],name=c['name'],run_id=r['run_id'],status=r['status'],seconds=r['seconds'],target=c['request']['target_seconds'],duration_mode=c['request']['duration_mode'],steps=r['steps'],responses=None,response_lower_bound=r['model_responses_lower_bound'],provider='codex',evidence_kind='partial_real_model_UI_evidence',wall_seconds=None,replay_passed=None,message=r['message']))
        continue
    o=load(d/'output.json');m=load(d/'manifest.json');capt=load(d/'capture.json')
    assert load(d/'input.json')==c['request'],c['id']
    errors=verify_run(d)
    audit={'input_matches_frozen':True,'replay_errors':errors,'provider':m['provider'],'actual_model_responses':m['model_responses'],'fault_injection':m.get('fault_injection'),
           'sha256':{n:sha(d/n) for n in ('input.json','output.json','trace.jsonl','manifest.json','data_snapshot.json','script.md','page.jpg')}}
    if (d/'audit.json').exists():assert load(d/'audit.json')==audit,c['id']
    else:(d/'audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    rows.append(dict(case=c['id'],name=c['name'],run_id=capt['run_id'],status=o['status'],seconds=(o.get('duration') or {}).get('total_seconds'),target=c['request']['target_seconds'],duration_mode=c['request']['duration_mode'],steps=m['steps'],responses=m['model_responses'],provider=m['provider'],evidence_kind=m['evidence_kind'],wall_seconds=round((datetime.fromisoformat(m['finished_at'])-datetime.fromisoformat(m['started_at'])).total_seconds(),1),replay_passed=not errors,message=o['message']))
old_changed=[]
if args.full:old_changed=[k for k,v in baseline['preserved_sha256'].items() if not (ROOT/k).is_file() or sha(ROOT/k)!=v]
summary={'updated_at':datetime.now(timezone.utc).isoformat(),'planned':50,'archived':len(rows),'actual_model_runs':sum((r['responses'] or r.get('response_lower_bound',0))>0 and r['provider']=='codex' for r in rows),'model_responses_exact_subset':sum(r['responses'] or 0 for r in rows),'model_responses_lower_bound':sum(r['responses'] or r.get('response_lower_bound',0) for r in rows),'partial_records':sum(r['responses'] is None for r in rows),'statuses':dict(Counter(r['status'] for r in rows)),'cases_unchanged':True,'app_data_unchanged':True,'source_files_checked':len(baseline['source_sha256']),'old_files_checked':len(baseline['preserved_sha256']) if args.full else None,'old_files_changed':old_changed,'complete_records_replayed':sum(r['replay_passed'] is not None for r in rows),'all_available_replays_passed':all(r['replay_passed'] for r in rows if r['replay_passed'] is not None),'runs':rows}
(B/'results.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with (B/'results.csv').open('w',encoding='utf-8-sig',newline='') as f:
    cols=['case','name','run_id','status','seconds','target','duration_mode','steps','responses','wall_seconds','message']
    w=csv.DictWriter(f,fieldnames=cols,extrasaction='ignore');w.writeheader();w.writerows(rows)
lines=['# v3 · 50次真实模型网页实验','','先冻结现实需求，再从网页提交；全部选择真实Codex，没有Mock，没有人工注入故障。初始四个相同版本本地实例交错运行，文件占用异常后降低并发；见protocol-amendment-01.md。耗时不是单用户性能基准。','',f"已归档 {len(rows)}/50；实际模型运行 {summary['actual_model_runs']}；可确认模型响应至少 {summary['model_responses_lower_bound']}；部分记录 {summary['partial_records']}。",'','程序completed不等于语义或业务合格。具体评阅与局限见复盘报告。旧版本和旧测试不覆盖。','','[冻结需求](测试清单.md) · [基线哈希](baseline.json) · [结果CSV](results.csv) · [机器摘要](results.json)','','|编号|场景|实际状态|估时/输入|步数|模型响应|原始证据|','|---|---|---|---|---|---|---|']
for r in rows:
    k=r['case'];links=f'[脚本](runs/{k}/script.md) · [Trace](runs/{k}/trace.jsonl) · [复算](runs/{k}/audit.json)' if r['responses'] is not None else f'[部分输出](runs/{k}/partial-output.json) · [页面步骤](runs/{k}/partial-trace-ui.json) · [运行故障](runs/{k}/infrastructure-error.json)'
    count=r['responses'] if r['responses'] is not None else '至少'+str(r.get('response_lower_bound',0))
    lines.append(f"|{k}|{r['name']}|{r['status']}|{r['seconds']} / {r['target']} ({r['duration_mode']})|{r['steps']}|{count}|{links} · [页面](runs/{k}/page.jpg)|")
(B/'README.md').write_text('\n'.join(lines)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in summary.items() if k!='runs'},ensure_ascii=False))
assert not old_changed,old_changed
assert summary['all_available_replays_passed']
