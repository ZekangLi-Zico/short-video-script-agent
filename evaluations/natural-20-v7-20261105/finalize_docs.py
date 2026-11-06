"""Update current review entrances once all20 records are audited."""
import json,shutil
from pathlib import Path
B=Path(__file__).resolve().parent;ROOT=B.parents[1]
load=lambda p:json.loads(p.read_text(encoding='utf8'))
s=load(B/'summary.json');a=load(B/'results.json')
assert a['archived']==20 and not a['errors']
new=s['new_readiness'].get('可直接试配音',0);old=s['old_readiness'].get('可直接试配音',0)
metric=f'20次真实模型网页实验已逐次保存；其中19条有旁白，文本通读“可直接试配音”由{old}/19变为{new}/19，另1条静音稿单列。133项自动测试通过。'
scope='通读由参与开发的AI助手完成，非真人盲评或实际配音；运行状态与文案质量分开。全部原需求未改，47项测试版本文件和12006项历史文件哈希不变。'
rootreport=ROOT/'docs/17-v7-natural-voice.md'
rootreport.write_text('# v7 自然旁白与逻辑连贯性\n\n'+metric+'\n\n'+scope+'\n\n[完整前后对照报告](../evaluations/natural-20-v7-20261105/复盘报告.md) · [20组逐条索引](../evaluations/natural-20-v7-20261105/README.md) · [精选实际结果](../examples/v7-live/evaluation.md)\n\n改变生成顺序：先组织连续讲述，再分镜；现有审核读取真实旁白顺序，不增加模型阶段或防御门槛。网页增加连读旁白和TXT导出，显示真实后台版本。原有来源、时长、动态改稿和异常保存仍保留。\n\n具体改善、退步、仍需改写的句子、调用耗时、复算方法和证据都在完整报告中。旧v6文档、原版归档和全部测试记录保留。本轮20组聚焦表达，不声称全部旧故障场景又以新模型跑过。\n',encoding='utf8')
p=ROOT/'README.md';text=p.read_text(encoding='utf8');start=text.index('**当前v6');end=text.index('本地材料已整理')
intro='**当前v7：先写连贯旁白，再安排镜头。** 复用已有审核核对连续讲述，新增网页连读区与旁白下载；单Agent、12步上限和原有事实/时长检查不变。\n\n'
intro+='**评审入口：** [实际效果对照](docs/17-v7-natural-voice.md) · [精选证据](examples/v7-live/evaluation.md) · [完整20次记录](evaluations/natural-20-v7-20261105/README.md) · [五分钟路线](docs/13-reviewer-and-practice-guide.md) · [提交清单](docs/06-submission.md)\n\n'
intro+=metric+' '+scope+'\n\n需求、方案、评估、AI辅助与复盘见docs/01–05。历史[v6报告](docs/16-v6-titles-latency.md)和所有旧版测试保留。\n\n'
text=text[:start]+intro+text[end:]
text=text.replace('4. 运行完成后下载 Markdown、Trace 或 JSON；','4. 在“连读旁白”通读完整讲述，运行完成后可下载旁白TXT、Markdown、Trace或JSON；')
text=text.replace('| `script.md` |','| `voice.txt`、`listening.json` | 连续旁白与逐镜提取；旧稿声画未知时明确标注，静音稿为空 |\n| `script.md` |')
p.write_text(text,encoding='utf8')
updates={
'01-requirements.md':'当前v7在原题范围内提升文案自然度与逻辑连贯性；先连续讲述再分镜，不新增验收门槛或模型阶段。原有来源、预计时长、缺信息和失败处理保留。',
'02-solution.md':'v7先组织完整口头讲述，再拆分镜与引用。src/listening.py按镜头和beat顺序提取voice/both，排除screen、标题、画面与备注。现有需求审核接收同一投影，写稿、估时、事实、审核与修订循环不增加阶段。网页和保存产物共用提取逻辑；旧稿声画未知时标注合并文案。app_version来自后台并写入运行元数据。',
'03-evaluation.md':metric+' '+scope+' 本轮20组是原v6场景的固定子集，正常/静音/双语/旧稿均保留原输入；完整原题负向验收仍引用带版本标签的历史真实记录和当前自动回归。',
'04-ai-usage.md':'候选人指出旁白不像自然语言，要求关注文案与逻辑而非堆防御规则，并将本轮真实测试从50次改为20次。AI完成诊断、提示与连续旁白实现、独立上下文代码审查、133项回归、网页20次真实调用和逐条文本通读。候选人提出的质量反馈与方向决策是实际贡献；上述自动执行不冒充候选人亲测。',
'05-retrospective.md':'这轮纠正了把形式检查通过当成稿件可用的倾向。先写连贯讲述，再安排镜头，比不断增加拦截规则更贴近创作者需要。生成改善必须从实际句子和整篇转折验证，报告保留变差或仍生硬的例子。截图还暴露默认页面仍连旧进程，现用后台版本标记和启动核验避免混淆。'}
for name,paragraph in updates.items():
 p=ROOT/'docs'/name;t=p.read_text(encoding='utf8');first,rest=t.split('\n',1)
 if name=='01-requirements.md':rest=rest.replace('当前 v6 继承','历史v6继承',1)
 if name=='02-solution.md':rest=rest.replace('## v6 当前增量','## 历史v6增量',1)
 if name=='03-evaluation.md':rest=rest.replace('## 当前v6','## 历史v6',1)
 p.write_text(first+'\n\n## v7 本轮更新\n\n'+paragraph+' 见[v7实际报告](17-v7-natural-voice.md)。\n'+rest,encoding='utf8')
p=ROOT/'docs/07-web-manual-test.md';t=p.read_text(encoding='utf8').replace('当前v6：','继承的声画功能：',1).replace('当前这轮正式测试使用8832–8835端口','v7本轮正式测试使用8842–8845端口')
first,rest=t.split('\n',1);p.write_text(first+'\n\n当前v7：页面顶部应显示“文案优化版v7”；每条运行显示实际app_version。脚本预览新增“连读旁白”，先整段通读再检查分镜，支持下载TXT。双语屏幕翻译不混入旁白，静音稿说明没有旁白，旧稿标成声画未知的合并文案。检查通过不等于文案一定自然。\n'+rest,encoding='utf8')
p=ROOT/'docs/13-reviewer-and-practice-guide.md';t=p.read_text(encoding='utf8');i=t.index('## 五分钟看什么');j=t.index('## 候选人建议亲自做的三件事')
t=t[:i]+'''## 五分钟看什么

1. 打开[v7对照报告](17-v7-natural-voice.md)，先读实际旁白和具体问题，不只看通过率。
2. 在[20组索引](../evaluations/natural-20-v7-20261105/README.md)选择一条改善和一条仍需改写的案例，看旧稿、新稿和Trace。
3. 运行网页，确认顶部v7版本，使用“连读旁白”和TXT导出逐句试读，再核对来源与分镜时长。
4. 查看[精选证据](../examples/v7-live/evaluation.md)中的真实修订链；故障、无素材与缺信息的历史验收保留版本标签。133项自动测试与实际模型结果分开。

'''+t[j:];p.write_text(t,encoding='utf8')
p=ROOT/'docs/06-submission.md';t=p.read_text(encoding='utf8')
t=t.replace('v6标题与效率优化版','v7自然旁白与连贯性优化版').replace('129项','133项').replace('50次真实网页记录','20次真实网页记录').replace('16-v6-titles-latency.md','17-v7-natural-voice.md').replace('examples/v6-live','examples/v7-live').replace('v6_标题与效率优化50次','v7_自然旁白与20次').replace('9944项','12006项').replace('全部50次网页实验','本轮20次网页实验').replace('realistic-50-v6-20261105','natural-20-v7-20261105').replace('development-tests/final/','development-tests/review-fixed/')
t=t.replace('50次真实模型网页实验：38次完成、12次需补资料、0次模型失败，231次有效响应，231次调用尝试。\n全部任务耗时中位数由314.1秒降至126.1秒；复用四个示例标题的稿件由22份变为0份。',metric+'\n'+scope)
t=t.replace('Improve scenario titles and reduce model waiting with preserved evidence','Improve coherent spoken copy with twenty preserved real-model comparisons')
p.write_text(t,encoding='utf8')
target=ROOT/'examples/v7-live';target.mkdir(exist_ok=False)
chosen=['V02','V03','V05','V06','V17','V22','V47']
for c in chosen:shutil.copytree(B/'runs'/c,target/c)
rows=['# v7 精选实际证据','', '完整20组见[索引](../../evaluations/natural-20-v7-20261105/README.md)，逐条评价见[报告](../../evaluations/natural-20-v7-20261105/复盘报告.md)。包含改善、仍需修改、静音、双语和旧稿。','']
for c in chosen:
 r=load(B/'runs'/c/'review.json');rows.append(f"- [{c}完整脚本]({c}/script.md)：{r['readiness']}，{r['comparison']}。{r['note']}")
(target/'evaluation.md').write_text('\n'.join(rows)+'\n',encoding='utf8')
print('Current documentation and7 representative unchanged evidence copies updated')
