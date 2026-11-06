"""Update submission pointers only after all 50 records are audited and read."""
import json
from datetime import datetime,timezone,timedelta
from pathlib import Path
B=Path(__file__).resolve().parent;ROOT=B.parents[1];D=ROOT/'docs'
load=lambda p:json.loads(p.read_text(encoding='utf8'))
s=load(B/'summary.json');a=load(B/'results.json');ops=load(B/'operational-metrics.json')
assert a['archived']==50 and not a['errors']
assert sum(s['quality_assessments'].values())==50
assert load(B/'development-tests/final/summary.json')['passed']
metrics=f"50次真实模型网页实验：{s['new_statuses']}，{s['new_responses']}次有效响应，{ops['new']['attempts']}次调用尝试。"
median=f"全部任务耗时中位数由{s['old_median_wall_seconds']}秒降至{s['new_median_wall_seconds']}秒"
title=f"复用四个示例标题的稿件由{s['old_generic_title_count']}份变为{s['new_generic_title_count']}份"
quality='、'.join(f'{k}{v}例' for k,v in s['quality_assessments'].items())
manifests=[load(p) for p in (B/'runs').glob('V[0-9][0-9]/manifest.json')]
start=min(datetime.fromisoformat(m['started_at']) for m in manifests);end=max(datetime.fromisoformat(m['finished_at']) for m in manifests)
local=lambda t:t.astimezone(timezone(timedelta(hours=8))).strftime('%Y-%m-%d %H:%M:%S')
(B/'work-session.json').write_text(json.dumps({'model_campaign_started_at':start.isoformat(),'model_campaign_finished_at':end.isoformat(),'timezone':'Asia/Shanghai','local_window':[local(start),local(end)],'note':'AI网页执行及等待窗口，不等于候选人亲自投入时间。'},ensure_ascii=False,indent=2)+'\n',encoding='utf8')
section=f'''## 真实50次结果与前后对照

北京时间 **{local(start)}—{local(end)}**，同一组49种业务需求及1次预定重复，四网页逐项提交。沿用v5原输入，不根据本轮输出或预期结论修改需求；所有尝试保存。开发小样另外存放，不计入正式50次。

|指标|修改前v5|当前v6|
|---|---:|---:|
|已完成脚本|{s['old_statuses'].get('completed',0)}|{s['new_statuses'].get('completed',0)}|
|需补资料|{s['old_statuses'].get('needs_input',0)}|{s['new_statuses'].get('needs_input',0)}|
|未完成/其他|{50-s['old_statuses'].get('completed',0)-s['old_statuses'].get('needs_input',0)}|{50-s['new_statuses'].get('completed',0)-s['new_statuses'].get('needs_input',0)}|
|有效模型响应|{s['old_responses']}|{s['new_responses']}|
|调用尝试（含失败）|{ops['old']['attempts']}|{ops['new']['attempts']}|
|未收到有效响应的尝试|{ops['old']['failed_attempts']}|{ops['new']['failed_attempts']}|
|任务耗时中位数|{s['old_median_wall_seconds']}秒|{s['new_median_wall_seconds']}秒|
|任务耗时P90|{ops['old']['tasks']['p90']}秒|{ops['new']['tasks']['p90']}秒|
|示例标题复用数|{s['old_generic_title_count']}|{s['new_generic_title_count']}|
|结构无效动作数|{ops['old']['invalid_actions']}|{ops['new']['invalid_actions']}|

双方均完成的{s['both_completed_pairs']}组，响应合计{s['both_completed_old_responses']}→{s['both_completed_new_responses']}，耗时中位数{s['both_completed_old_median_wall_seconds']}→{s['both_completed_new_median_wall_seconds']}秒。不同运行时间与服务负载仍会影响耗时，表中是实测配对观察，不是独立控制的速度因果实验。输入/输出token不是费用。

逐稿评阅：**{quality}**。由开发助手逐例阅读原需求、两版脚本与Trace，非独立人类盲评。内容、状态与速度分开判断，不把completed直接当作优质脚本。

本轮观察到{ops['new']['recovered_calls']}次成功响应带有超时恢复记录；恢复逻辑另有离线故障契约测试。若本轮未触发，不能把完成率改善归因为恢复救回任务。

44项冻结版本文件不变；9944项旧历史文件哈希不变；50份网页输入与保存输入一致，实际响应与诊断对应，工具复算无错误。详见 [完整逐例复盘](../evaluations/realistic-50-v6-20261105/复盘报告.md)、[全部输入/输出/Trace](../evaluations/realistic-50-v6-20261105/README.md)、[调用耗时指标](../evaluations/realistic-50-v6-20261105/operational-metrics.json)。

## 具体成稿变化

'''
for case in ('V01','V05','V14','V22','V28','V45'):
    review=load(B/'runs'/case/'review.json');o=load(B/'runs'/case/'output.json')
    section+=f"- **{case}，{review['assessment']}：** {review['note']} [实际脚本](../evaluations/realistic-50-v6-20261105/runs/{case}/script.md)\n"
section+='\n这些变化对应原题的实际成稿、有效修订和事实可追溯。通过减少无用决策和提示干扰改善结果，未增加审核层或生产功能。\n'
p=D/'16-v6-titles-latency.md';text=p.read_text(encoding='utf8');begin=text.index('## 真实实验');endpos=text.index('## 当前边界')
p.write_text(text[:begin]+section+'\n'+text[endpos:],encoding='utf8')

p=ROOT/'README.md';old=p.read_text(encoding='utf8');tail=old[old.index('## 网页人工测试'):]
tail=tail.replace('也可用 `.\\run.ps1 -Mode live`。','也可用 `.\\run.ps1 -Mode live`。默认每进程 `CODEX_REASONING_EFFORT=medium`，可覆盖为low/medium/high/xhigh；不改全局Codex配置。')
tail=tail.replace('总调用次数仍受步骤上限约束。','Codex每任务最多额外恢复一次超时，每次尝试分别保存诊断；决策最多12步、每步至多决策与审核两次调用。')
tail=tail.replace('每次结果保存在','修改代码后需重启服务才能加载新版；已有服务占用端口时可改用新端口，不能把旧进程当作新版。\n\n每次结果保存在',1)
head=f'''# 短视频脚本 Agent · 第4题

给定主题、受众、平台、目标时长和风格，生成有事实依据、可拍摄的分镜脚本；模型根据检索、估时及审核结果决定改稿、补查或结束。

**当前v6：标题贴合场景，减少检查往返，限制一次超时恢复。** 保留v5的自然改写/翻译与声画节拍，单Agent、Python标准库和12步上限。

**评审入口：** [实际效果对照](docs/16-v6-titles-latency.md) · [精选证据](examples/v6-live/evaluation.md) · [完整50次记录](evaluations/realistic-50-v6-20261105/README.md) · [五分钟路线](docs/13-reviewer-and-practice-guide.md) · [提交清单](docs/06-submission.md)

**129项自动测试通过。** {metrics} {median}；{title}。具体标题、脚本与失败均可逐条查看。

逐稿评阅：{quality}，由参与开发的AI助手阅读实际新旧产物，非独立盲评。输入预先冻结，网页提交真实Codex，每次保存结果；未用Mock替代、未重跑覆盖失败。44项测试版本文件和9944项历史文件哈希不变。

需求、方案、评估、AI辅助与复盘见 [docs/01](docs/01-requirements.md)、[02](docs/02-solution.md)、[03](docs/03-evaluation.md)、[04](docs/04-ai-usage.md)、[05](docs/05-retrospective.md)。历史[v5报告](docs/15-v5-effective-scripts.md)和所有旧版测试保留。

本地材料已整理，尚未推送最终GitHub提交或交卷。题目要求的仓库URL、最终commit SHA、读取权限及候选人实际投入记录见提交清单。

'''
p.write_text(head+tail,encoding='utf8')

p=D/'03-evaluation.md';old=p.read_text(encoding='utf8').replace('## 当前v5效果优化与50次真实网页对照','## 历史v5效果优化与50次真实网页对照')
section=f'''## 当前v6：标题与调用效率

129项自动测试全部通过，见 `evaluations/realistic-50-v6-20261105/development-tests/final/`。{metrics} {median}；{title}。逐稿评阅为{quality}，非独立盲评。

完整证据、比较方法及剩余问题见 [v6报告](16-v6-titles-latency.md) 与 [50次索引](../evaluations/realistic-50-v6-20261105/README.md)。44项源码和9944项历史哈希不变，50组结果可复算。继承的v5全部50组记录也已重放。实际工具/模型受控故障历史保留原标签，本轮50次未注入故障；不要把旧故障实验重命名为新版本实验。

'''
p.write_text(old.replace('\n\n','\n\n'+section,1),encoding='utf8')
p=D/'05-retrospective.md';old=p.read_text(encoding='utf8');at=old.index('## v5')
section=f'''## v6：减少干扰与无用等待

v5把可写性放开后，仍向creative提供strict的四个标题和连接语示例，造成大量套用。本轮从提示输入移除这些干扰，并保留全部当前需求与事实。实际{title}。

等待也不只是网络问题：每个本地检查之前都在等待模型选择动作。现在一次模型审核动作补齐本地检查，仍由模型读取真实结果选择修订。配合medium推理配置和历史压缩，{median}。完整状态变化、退步及例子见 [实际报告](16-v6-titles-latency.md)，不把单次观察当作永久保证。

独立审查发现缓存需同时绑定检索集合，以及取消不能只在步骤开头检查；两者均用失败测试复现后修复。129项测试通过。无需为了这道题加入多Agent编排、复杂队列或数据库。

'''
p.write_text(old[:at]+section+old[at:],encoding='utf8')

p=D/'06-submission.md'
p.write_text(f'''# 提交清单与答题框模板

当前 **v6标题与效率优化版** 已包含代码、129项自动测试、50次真实网页记录和前后对照。主报告：[16-v6-titles-latency.md](16-v6-titles-latency.md)；精选证据：[examples/v6-live](../examples/v6-live/evaluation.md)。

最新快照：`小影科技笔试_第4题_v6_标题与效率优化50次复测提交包.zip`。包内DELIVERY.json记录文件哈希，旧源码及全部实验记录保留；旧根目录ZIP保留本地，不重复嵌套。9944项历史哈希针对工作区，新包按自己的DELIVERY.json核验。

**尚未推送最终Git commit或交卷。** 本地没有GitHub远程；旧SHA不是最终提交。需填写实际仓库URL、推送后的完整SHA、私有仓库评审读取权限，以及候选人真实投入与本人复验。

```text
选择题目：第4题——短视频脚本Agent
GitHub URL：填写真实仓库地址
最终commit SHA：填写已推送的完整SHA

运行入口：README.md
实际改进及前后对照：docs/16-v6-titles-latency.md
需求、设计、评估、AI使用、复盘：docs/01–05
精选输入、实际输出和Trace：examples/v6-live/
全部50次网页实验：evaluations/realistic-50-v6-20261105/
129项测试：evaluations/realistic-50-v6-20261105/development-tests/final/

启动网页：python -m src.web --open
自动测试：python -m scripts.run_tests
离线入口：python -m src.cli --provider mock --input examples/inputs/normal.json --output outputs/demo
真实模型：网页选择Codex，或按README配置模型API。

{metrics}
{median}；{title}。
模型依据实际工具结果决定改稿、补查或停止，保留来源、声画时长和完整执行记录。
AI辅助、个人贡献和实际投入时间据实填写，见docs/04-ai-usage.md。
```

## 最后提交

1. 亲自运行并理解一条有效修订链，填写本人时间与复验记录。
2. 同一GitHub仓库放入代码、文档、examples、evaluations及archives，不加入凭证、.env、.runtime或隐私资料。
3. 创建最终commit并推送，核对远程README、Trace及权限，再填写URL和完整SHA。ZIP不能代替题目要求的GitHub交付。

```bash
git add README.md PRODUCT.md DESIGN.md src web tests scripts data docs evaluations examples requirements.txt .env.example .gitignore run.ps1 启动网页.cmd
git add -f archives
git commit -m "Improve scenario titles and reduce model waiting with preserved evidence"
git remote add origin <实际仓库URL>
git push -u origin HEAD
git rev-parse HEAD
```

以上命令尚未执行；已配置origin时不重复添加。新环境网页历史从outputs读取；完整提交包保留outputs。
''',encoding='utf8')

p=D/'13-reviewer-and-practice-guide.md';old=p.read_text(encoding='utf8');startpos=old.index('## 五分钟看什么');stop=old.index('## 候选人建议')
intro=f'''## 五分钟看什么

1. **看标题和正文。** `examples/v6-live/V01/` 与v5同例对照，观察标题如何对应早餐摊和字幕用途；指定标题案例从完整50次目录查阅。
2. **看真正改稿。** `examples/v6-live/V05/trace.jsonl` 的预检查返回时长问题，随后模型修订并重检；预检查与模型动作明确区分。
3. **看边界。** V34资料不足不会编造收费；v5 V05超时仍保留原记录。自动超时恢复是执行机制，不当作模型智能决策证据。
4. **看完整数据。** [v6报告](16-v6-titles-latency.md)给出所有50次结果、耗时、标题变化及逐稿评阅。129项离线测试与真实模型结果分开。

网页运行 `python -m src.web --open`；已运行旧服务时用新端口。全部记录见 [50次索引](../evaluations/realistic-50-v6-20261105/README.md)，精选7例见 [examples/v6-live](../examples/v6-live/evaluation.md)。

'''
p.write_text(old[:startpos]+intro+old[stop:],encoding='utf8')
print(metrics,median,title)
