"""Assemble reviewed results; never infer quality ratings from task status."""
import csv, json, statistics
from collections import Counter
from datetime import datetime
from pathlib import Path

B = Path(__file__).resolve().parent
OLD = B.parent / 'realistic-50-v41-20261104'
load = lambda p: json.loads(p.read_text(encoding='utf-8-sig'))
audit = load(B/'results.json')
comparison = load(B/'comparison.json')
assert audit['archived'] == comparison['paired'] == 50 and not audit['errors']
assert audit['old_files_checked'] == 7788
reviews = [load(B/'runs'/r['case']/'review.json') for r in audit['runs']]
cases = {c['id']: c for c in load(B/'cases.json')}
paired = {r['case']: r for r in comparison['runs']}
rows = []
for r, review in zip(audit['runs'], reviews):
    old = load(OLD/'runs'/r['case']/'manifest.json')
    old_wall = (datetime.fromisoformat(old['finished_at'])-datetime.fromisoformat(old['started_at'])).total_seconds()
    rows.append(dict(case=r['case'], name=r['name'], old_status=paired[r['case']]['old_status'],
        new_status=r['status'], old_responses=paired[r['case']]['old_responses'], new_responses=r['responses'],
        old_seconds=paired[r['case']]['old_seconds'], new_seconds=r['seconds'],
        old_wall_seconds=round(old_wall,1), new_wall_seconds=r['wall_seconds'],
        assessment=review['assessment'], note=review['note'],
        hard_requirement_violation_observed=review['hard_requirement_violation_observed']))
with (B/'逐条复盘.csv').open('w',encoding='utf-8-sig',newline='') as f:
    writer=csv.DictWriter(f,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
diags=[load(p) for p in (B/'runs').glob('*/diagnostics/*.json')]
both_completed=[r for r in rows if r['old_status']==r['new_status']=='completed']
generic_titles=set(load(B.parents[1]/'data/brand_rules.json')['allowed_titles'])
def generic_count(base):
    return sum((load(base/'runs'/r['case']/'output.json').get('script') or {}).get('title') in generic_titles for r in rows)
stats={k:v for k,v in comparison.items() if k!='runs'}
stats.update(quality_assessments=dict(Counter(r['assessment'] for r in rows)),
    manual_stale_note_cases=[r['case'] for r in reviews if r.get('editorial_note_staleness',False)],
    observed_hard_requirement_violations=[r['case'] for r in reviews if r['hard_requirement_violation_observed']],
    old_median_wall_seconds=round(statistics.median(r['old_wall_seconds'] for r in rows),1),
    new_median_wall_seconds=round(statistics.median(r['new_wall_seconds'] for r in rows),1),
    diagnostics=len(diags),failed_response_diagnostics=sum(not x.get('response_received') for x in diags),
    both_completed_pairs=len(both_completed),
    both_completed_old_responses=sum(r['old_responses'] for r in both_completed),
    both_completed_new_responses=sum(r['new_responses'] for r in both_completed),
    both_completed_old_median_wall_seconds=round(statistics.median(r['old_wall_seconds'] for r in both_completed),1),
    both_completed_new_median_wall_seconds=round(statistics.median(r['new_wall_seconds'] for r in both_completed),1),
    old_generic_title_count=generic_count(OLD),new_generic_title_count=generic_count(B))
(B/'summary.json').write_text(json.dumps(stats,ensure_ascii=False,indent=2)+'\n',encoding='utf8')
lines=['# v5 · 50次真实模型网页实验','',
    '固定49种现实需求及1次预定重复，共50次。所有输入逐字沿用v4.1，未根据新版输出调整需求。四个网页实例通过表单提交真实Codex，未注入工具故障，未以Mock替代。', '',
    '每例目录保留 brief、网页输入、提交前后DOM、截图、input、output、script、Trace、检查点、运行清单、模型诊断、逐例评阅和完整性核验。', '',
    '[完整复盘](复盘报告.md) · [逐条评阅CSV](逐条复盘.csv) · [状态与耗时](results.csv) · [机器摘要](summary.json) · [冻结协议](protocol.json)', '',
    '|案例|实际需求|旧状态→新状态|质量评阅|证据|','|---|---|---|---|---|']
for r in rows:
    case=r['case'];lines.append(f"|{case}|{r['name']}|{r['old_status']} → {r['new_status']}|{r['assessment']}|[稿件](runs/{case}/script.md) · [Trace](runs/{case}/trace.jsonl) · [截图](runs/{case}/page.png) · [评阅](runs/{case}/review.json)|")
(B/'README.md').write_text('\n'.join(lines)+'\n',encoding='utf8')
report=['# v5真实网页50次配对复盘','',
    '评阅人为参与开发的AI助手，逐例阅读相同原始需求、两版成稿与实际Trace；不是独立盲评。输入预先冻结，质量结论没有提供给被测模型。', '',
    f"修改前：{stats['old_statuses']}，{stats['old_responses']}次模型响应。修改后：{stats['new_statuses']}，{stats['new_responses']}次响应。", '',
    f"逐例内容评阅：{stats['quality_assessments']}。单次任务耗时中位数：旧版{stats['old_median_wall_seconds']}秒，新版{stats['new_median_wall_seconds']}秒；包含所有状态，不作为模型速度因果结论。", '',
    '完成状态、内容质量和记录完整性分别统计。真正缺少产品事实的需求可以正确停在needs_input；模型超时记为本次失败，未以重跑覆盖。', '',
    f"源码{audit['source_files_checked']}项和历史{audit['old_files_checked']}项哈希未变；50组网页输入与保存输入一致，实际模型诊断与Trace响应对应，工具复算无错误。", '',
    '三项实现及关键收益详见 [提交效果报告](../../docs/15-v5-effective-scripts.md)。以下保留每例完整判断与代价。','']
for r in rows:
    case=r['case'];report += [f"## {case} {r['name']}：{r['assessment']}",'',
        f"{r['old_status']} → {r['new_status']}；响应 {r['old_responses']} → {r['new_responses']}；预计视频时长 {r['old_seconds']} → {r['new_seconds']} 秒。",'',
        r['note'],'',f"[原需求](runs/{case}/input.json) · [新稿](runs/{case}/script.md) · [Trace](runs/{case}/trace.jsonl) · [旧稿](../realistic-50-v41-20261104/runs/{case}/script.md)",'']
(B/'复盘报告.md').write_text('\n'.join(report),encoding='utf8')
print(json.dumps(stats,ensure_ascii=False))
