"""Collect actual webpage runs; keep each original and copy current evidence once."""
import hashlib
import json
import shutil
import sys
from datetime import datetime
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
sys.path.insert(0,str(ROOT))
from scripts.verify_evidence import verify_run

HERE=Path(__file__).resolve().parent

def read(path):return json.loads(path.read_text(encoding='utf-8'))

def sha(path):
    with path.open('rb') as f:return hashlib.file_digest(f,'sha256').hexdigest()

def collect():
    cases={c['id']:c for c in read(HERE/'cases.json')}
    rows=[]
    for item in read(HERE/'web-runs.json'):
        case=cases[item['case_id']];folder=ROOT/'outputs/web'/item['run_id']
        result=read(folder/'output.json');manifest=read(folder/'manifest.json')
        request=read(folder/'input.json');meta=result['metadata']
        trace=[json.loads(line) for line in (folder/'trace.jsonl').read_text(encoding='utf-8').splitlines() if line.strip()]
        observations=[]
        for t in trace:
            observations += [{'step':t['step'],'action':t['action'],'observation':t['observation']}]
            observations += [{'step':t['step'],**p} for p in t.get('preflight_checks',[])]
        estimates=[{'step':t['step'],'seconds':t['observation']['total_seconds'],'passed':t['observation']['passed']}
                   for t in observations if t['action']=='estimate_duration' and t['observation'].get('ok')]
        reasons=[];kind=case['id']
        if request!=case['request']:reasons.append('实际输入与冻结需求不一致')
        if manifest['fault_injection']!=case['failures']:reasons.append('实际故障设置不一致')
        if meta.get('app_version')!='v7.3.1-submission' or meta.get('evidence_kind')!='real_model' or meta.get('model_responses',0)<1:
            reasons.append('不是本轮真实模型记录')
        if any(t['action']=='model_error' for t in trace):reasons.append('模型错误不能代替业务负例')
        if kind in {'product_normal','over_duration'}:
            if result['status']!='completed':reasons.append('未完成成稿')
            if not all((result.get(k) or {}).get('passed') for k in ('duration','rules_check','requirements_check')):
                reasons.append('成稿检查未全部通过')
        if kind=='over_duration':
            failed=[x['step'] for x in estimates if not x['passed']]
            if not failed or not any(t['action']=='write_script' and t['step']>failed[0] for t in trace):
                reasons.append('缺少观察超时后实际修订的路径')
        if kind=='no_material':
            if result['status'] not in {'needs_input','blocked'}:reasons.append('无素材未明确请求补充或停止')
            if not any(t['action']=='search_materials' and t['observation'].get('ok') and t['observation'].get('count')==0 for t in trace):
                reasons.append('缺少实际空检索')
        if kind=='tool_failure':
            if result['status'] not in {'blocked','step_limit'}:reasons.append('工具持续失败未明确停止')
            if not any(t['observation'].get('error')=='injected_tool_failure' for t in trace):reasons.append('故障未实际触发')
        errors=verify_run(folder)
        dest=ROOT/'examples/current'/kind
        if not dest.exists():shutil.copytree(folder,dest)
        different=[p.relative_to(folder).as_posix() for p in folder.rglob('*') if p.is_file()
                   and (not (dest/p.relative_to(folder)).is_file() or sha(p)!=sha(dest/p.relative_to(folder)))]
        if different:reasons.append('精选复制与原运行不一致：'+','.join(different))
        diagnostics=[read(p) for p in (folder/'diagnostics').glob('*.json')]
        rows.append({'case':kind,'web_run_id':item['run_id'],'status':result['status'],
                     'elapsed_seconds':round((datetime.fromisoformat(meta['finished_at'])-datetime.fromisoformat(meta['started_at'])).total_seconds(),2),
                     'model_responses':meta['model_responses'],'attempts':len(diagnostics),
                     'timeouts':sum(d.get('error_code')=='codex_timeout' for d in diagnostics),
                     'estimated_video_seconds':(result.get('duration') or {}).get('total_seconds'),
                     'duration_observations':estimates,'steps':len(trace),'actions':[t['action'] for t in trace],
                     'failures_injected':manifest['fault_injection'],'input_matches_frozen':request==case['request'],
                     'checks':{k:(result.get(k) or {}).get('passed') for k in ('duration','rules_check','requirements_check')},
                     'evidence_errors':errors,'acceptance_errors':reasons,'passed':not(errors or reasons),
                     'message':result['message'],'evidence_path':dest.relative_to(ROOT).as_posix()})
    report={'cases_recorded':len(rows),'all_four_recorded':len(rows)==4,'passed':len(rows)==4 and all(r['passed'] for r in rows),'runs':rows}
    (HERE/'live-results.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False,indent=2))

if __name__=='__main__':collect()
