"""Read-only verification of saved UI experiments; no model calls."""
import argparse,csv,hashlib,json,sys
from collections import Counter
from datetime import datetime,timezone,timedelta
from pathlib import Path

B=Path(__file__).resolve().parent
ROOT=B.parents[1]
sys.path.insert(0,str(ROOT))
from scripts.verify_evidence import verify_run
from src.listening import listening_copy

load=lambda p:json.loads(p.read_text(encoding='utf-8-sig'))
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
p=argparse.ArgumentParser();p.add_argument('--full',action='store_true');p.add_argument('--require-20',action='store_true');args=p.parse_args()
baseline=load(B/'baseline.json');cases={c['id']:c for c in load(B/'cases.json')}
errors=[];rows=[];attempts=[]
if sha(B/'cases.json')!=baseline['cases_sha256']:errors.append('frozen input file changed')
source_changed=[k for k,v in baseline['source_sha256'].items() if sha(ROOT/k)!=v]
for capture in sorted((B/'runs').glob('*/capture.json')):
 d=capture.parent;cap=load(capture);c=cases[cap['case']];r=c['request'];o=load(d/'output.json');m=load(d/'manifest.json');ui=load(d/'ui-input.json')
 e=verify_run(d)
 if o.get('metadata',{}).get('app_version')!='v7-natural-voice':e.append('wrong runtime version')
 if load(d/'listening.json')!=listening_copy(o.get('script')):e.append('listening mismatch')
 if (d/'voice.txt').read_text(encoding='utf8')!=('旧稿合并文案（未区分声画，不能直接视为旁白）\n\n' if listening_copy(o.get('script'))['kind']=='legacy_unspecified' else '')+listening_copy(o.get('script'))['text']+'\n':e.append('voice mismatch')
 if load(d/'input.json')!=r or load(d/'brief.json')!=c:e.append('input does not match frozen brief')
 expected={'topic':r['topic'],'audience':r['audience'],'platform':r['platform'],'target-seconds':str(r['target_seconds']),'duration-mode':r['duration_mode'],'expression-mode':r['expression_mode'],'style':r['style'],'product':r['product_id'],'provider':'codex','fault':'none'}
 if any(ui['fields'].get(k)!=v for k,v in expected.items()):e.append('UI fields mismatch')
 if json.loads(ui['fields']['initial-script'] or 'null')!=r.get('initial_script'):e.append('UI old draft mismatch')
 if datetime.fromisoformat(m['started_at']) < datetime.fromisoformat(ui['submitted_at'].replace('Z','+00:00'))-timedelta(seconds=2):e.append('result predates submission')
 if m['provider']!='codex' or m['evidence_kind']!='real_model':e.append('not a real-model entry')
 if m.get('fault_injection'):e.append('unexpected injected fault')
 if load(d/'run.json')['state']!='finished':e.append('final record not finished')
 trace=[json.loads(s) for s in (d/'trace.jsonl').read_text(encoding='utf-8').splitlines()]
 for t in trace:
  for k in ('model','review_model'):
   if k in t:
    diag=load(d/'diagnostics'/(t[k]['call_id']+'.json'))
    if not diag['response_received'] or diag['metadata']!=t[k]:e.append('diagnostic mismatch')
 diags=[load(q) for q in (d/'diagnostics').glob('*.json')]
 response_ids={x['call_id'] for x in diags if x.get('response_received')}
 trace_ids={t[k]['call_id'] for t in trace for k in ('model','review_model') if isinstance(t.get(k),dict) and t[k].get('call_id')}
 if response_ids!=trace_ids:e.append('response IDs differ from Trace')
 if len(response_ids)!=m['model_responses']:e.append('response count differs')
 for name in ('input.json','output.json','trace.jsonl','manifest.json','data_snapshot.json','script.md','checkpoint.json','run.json','voice.txt','listening.json'):
  if sha(d/name)!=sha(ROOT/'outputs/web'/cap['run_id']/name):e.append('backend copy mismatch: '+name)
 row={'case':c['id'],'name':c['name'],'folder':d.name,'run_id':cap['run_id'],'status':o['status'],'steps':m['steps'],'responses':m['model_responses'],'seconds':(o.get('duration') or {}).get('total_seconds'),'target':r['target_seconds'],'duration_mode':r['duration_mode'],'review_calls':sum(t['action']=='check_requirements' for t in trace),'write_calls':sum(t['action']=='write_script' for t in trace),'wall_seconds':round((datetime.fromisoformat(m['finished_at'])-datetime.fromisoformat(m['started_at'])).total_seconds(),1),'errors':e,'message':o['message']}
 (rows if m['model_responses']>0 else attempts).append(row)
 (d/'audit.json').write_text(json.dumps({'input_and_ui_match':not any('mismatch' in x for x in e),'errors':e,'provider':m['provider'],'responses':m['model_responses'],'files_sha256':{q.relative_to(d).as_posix():sha(q) for q in d.rglob('*') if q.is_file() and q.name not in {'audit.json','review.json'}}},ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
rows.sort(key=lambda r:r['case'])
if len(set(r['case'] for r in rows))!=len(rows):errors.append('duplicate counted case')
old_changed=[k for k,v in baseline['preserved_sha256'].items() if not (ROOT/k).is_file() or sha(ROOT/k)!=v] if args.full else []
if source_changed:errors.append('source changed')
if old_changed:errors.append('historical evidence changed')
errors.extend(f"{r['folder']}: {e}" for r in rows+attempts for e in r['errors'])
if args.require_20 and len(rows)!=20:errors.append('not all 20 real experiments archived')
summary={'verified_at':datetime.now(timezone.utc).isoformat(),'planned':20,'archived':len(rows),'actual_model_responses':sum(r['responses'] for r in rows),'statuses':dict(Counter(r['status'] for r in rows)),'zero_response_attempts':attempts,'source_files_checked':len(baseline['source_sha256']),'source_changed':source_changed,'old_files_checked':len(baseline['preserved_sha256']) if args.full else None,'old_files_changed':old_changed,'errors':errors,'runs':rows}
(B/'results.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
with (B/'results.csv').open('w',encoding='utf-8-sig',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['case','name','folder','run_id','status','steps','responses','seconds','target','duration_mode','review_calls','write_calls','wall_seconds','message'],extrasaction='ignore');w.writeheader();w.writerows(rows)
print(json.dumps({k:v for k,v in summary.items() if k not in {'runs','zero_response_attempts'}},ensure_ascii=False))
raise SystemExit(bool(errors))
