"""Compile saved, individually read cases; no generated test results."""
import json,statistics
from collections import Counter
from pathlib import Path
B=Path(__file__).resolve().parent;ROOT=B.parents[1]
load=lambda p:json.loads(p.read_text(encoding='utf8'))
audit=load(B/'results.json');ops=load(B/'operational-metrics.json')
assert audit['archived']==20 and not audit['errors']
cases={c['id']:c for c in load(B/'cases.json')}
reviews=[load(B/'runs'/c/'review.json') for c in cases]
counts=lambda key:dict(Counter(r[key] for r in reviews))
summary={'cases':20,'old_readiness':dict(Counter(r['old']['readiness'] for r in reviews)),
         'new_readiness':counts('readiness'),'comparisons':counts('comparison'),
         'spoken_denominator':19,'statuses':audit['statuses'],'responses':audit['actual_model_responses'],
         'old_latency':ops['old']['tasks'],'new_latency':ops['new']['tasks'],
         'method':'开发助手实际文本通读，不是独立人类盲评，不是配音或成片测量。静音稿单列。'}
(B/'summary.json').write_text(json.dumps(summary,ensure_ascii=False,indent=2),encoding='utf8')
lines=['# v7 自然旁白与20次真实网页复测','',
'这轮把生成顺序改为先讲清楚一件事，再分配镜头和引用；已有审核同时看到连续旁白。没有增加模型阶段、拒绝门槛或针对某个句子的替换规则。','',
'## 实际结果','',
f"20组原需求逐字复测：{audit['statuses']}；{audit['actual_model_responses']}次有效模型响应。全部通过网页选择真实Codex并点击生成，每次输入、结果、Trace、诊断和页面截图均单独保存。没有替换失败的重跑。",'',
'|文本通读结论|旧v6|新v7|','|---|---:|---:|']
for label in ['可直接试配音','需局部改写','需整体重写','静音稿不适用','未成稿']:
 lines.append(f"|{label}|{summary['old_readiness'].get(label,0)}|{summary['new_readiness'].get(label,0)}|")
lines += ['',f"逐条对照：{summary['comparisons']}。静音需求V17不进入19条旁白的配音就绪分母。以上判断由参与开发的AI助手逐条阅读实际文本，并非真人盲评或TTS试听。‘可直接试配音’表示文本通读未发现必须改写的明显问题，不代表已经录制。",'',
f"同一20组的任务耗时中位数：{ops['old']['tasks']['median']}秒 → {ops['new']['tasks']['median']}秒；P90：{ops['old']['tasks']['p90']}秒 → {ops['new']['tasks']['p90']}秒。有效响应{ops['old']['responses']} → {ops['new']['responses']}次；失败调用尝试{ops['old']['failed_attempts']} → {ops['new']['failed_attempts']}次。双方均四个网页并行，运行时间窗口不同，不能把服务波动全部归因于提示修改。",'',
'## 做了什么','',
'1. 先组织完整口头讲述，再拆分镜。功能事实可以放进有具体用途的自然句子，引用仍指向原素材；镜头顺序不再强行决定旁白中的时间或因果关系。',
'2. 复用现有需求审核，加入只含voice/both的连续文本。画面说明、镜头目的和屏幕翻译不会混进旁白；审核仍核对原需求和事实，不因单纯措辞偏好要求改稿。',
'3. 网页增加连读旁白与TXT下载，方便直接通读。旧稿声画不明时明确标成合并文案，静音稿没有伪造旁白。',
'4. 页面显示实际后台版本，每次运行记录app_version，防止新页面连着旧写稿进程。用户截图对应旧v3记录，原样保存在reported-example-v3；它不混入v6配对统计。','',
'## 方法和保留证据','',
'20组从已冻结v6真实工作brief中按场景覆盖选取，未改需求，也未把期待文案/执行路径传给Agent。选定并保存protocol.json、cases.json后才实施修改；旧版通读评价在新版运行前保存于baseline-readthrough.json。正式测试过程中应用源码保持冻结。',
'开发回归133项全部通过，记录在development-tests/review-fixed。它们验证提取、接口、保存和原有流程，不证明文案自然。另一AI上下文完成代码审查，旧稿下载误标已用失败回归修复。',
f"保存的50组v6记录重放通过；当前20组证据复算通过。{audit['source_files_checked']}项源码/测试/数据文件未改变，{audit['old_files_checked']}项历史文件哈希未改变。v6原版归档在archives/v6-before-v7-20261105。",'',
'## 每条结果与前后对照','',
'每条先列通读评价，完整稿件包含可核对的旁白、画面和引用；每个runs目录还含原始input.json、output.json、trace.jsonl、voice.txt和page.png。','']
for r in reviews:
 c=r['case'];lines += [f"### {c} {cases[c]['name']}",
 f"旧：{r['old']['readiness']}。{r['old']['note']}",
 f"新：{r['readiness']}；{r['comparison']}。{r['note']}",
 f"剩余：{r['remaining'] or '本条文本通读未发现必须改写的明显问题。'}",
 f"[旧完整稿](../realistic-50-v6-20261105/runs/{c}/script.md) · [新完整稿](runs/{c}/script.md) · [新连读文案](runs/{c}/voice.txt) · [过程](runs/{c}/trace.jsonl)", '']
lines += ['## 对原题的作用','',
'原题要求可编辑、满足时长且有事实依据的脚本。自然表达的提升让这些约束落实到可读的成稿，而不是只有检查通过。来源ID、分镜估时、工具结果与实际修订仍可追溯；连续旁白和版本标记使评审与本人复验更容易。没有为了框架名称、复杂Runtime或多Agent增加工作量。',
'代码、README、依赖、环境变量示例、五份文档及历史正常/缺信息/无素材/工具故障/超时修订证据仍保留。本轮20组是表达对照，不冒充重新覆盖所有故障验收。GitHub URL、最终commit SHA、访问权限和候选人真实投入/本人复验仍需按实际情况填写。','',
'## 仍存在的问题','',
'本轮通读留下的具体句子和修改建议逐条列在上面，不以“检查通过”替代内容质量判断。单一合成产品资料、同一模型后端的评估、静态语速估时和服务延迟仍是边界；没有新增真实配音测量、视频生成、数据库或自动发布。',
'本轮执行过程、代码审查及文本评价由AI辅助完成；候选人提出问题、确定优化方向并进行自己的网页试用，不把自动完成的20次记为候选人亲测。','']
(B/'复盘报告.md').write_text('\n'.join(lines),encoding='utf8')
index=['# v7 20次真实网页实验索引','', '[前后复盘](复盘报告.md) · [机器核验](results.json) · [评测协议](protocol.json) · [汇总](summary.json)','',
'|ID|现实需求|运行状态|文本通读|对比|','|---|---|---|---|---|']
for r in reviews:
 c=r['case'];row=next(x for x in audit['runs'] if x['case']==c)
 index.append(f"|[{c}](runs/{c}/script.md)|{cases[c]['name']}|{row['status']}|{r['readiness']}|{r['comparison']}|")
(B/'README.md').write_text('\n'.join(index)+'\n',encoding='utf8')
print(json.dumps(summary,ensure_ascii=False))
