"""Update current submission pointers from audited, individually reviewed results."""
import json
from datetime import datetime, timezone, timedelta
from pathlib import Path
B=Path(__file__).resolve().parent;ROOT=B.parents[1];D=ROOT/'docs'
load=lambda p:json.loads(p.read_text(encoding='utf8'))
s=load(B/'summary.json');a=load(B/'results.json')
assert a['archived']==50 and not a['errors'] and s['quality_assessments']=={'改进':21,'退步':4,'相当':13,'仍需补充':12}
manifests=[load(p) for p in (B/'runs').glob('*/manifest.json')]
start=min(datetime.fromisoformat(m['started_at']) for m in manifests)
end=max(datetime.fromisoformat(m['finished_at']) for m in manifests)
local=lambda t:t.astimezone(timezone(timedelta(hours=8))).strftime('%Y-%m-%d %H:%M:%S')
(B/'work-session.json').write_text(json.dumps({'model_campaign_started_at':start.isoformat(),'model_campaign_finished_at':end.isoformat(),
    'timezone':'Asia/Shanghai','local_window':[local(start),local(end)],'note':'AI网页执行与等待窗口，不等于候选人手写工时；不包括先前开发与后续文档打包。'},ensure_ascii=False,indent=2)+'\n',encoding='utf8')
metrics='50次真实模型网页实验、292次有效模型响应：36 completed、12 needs_input、2 blocked（模型超时）。'
method=f'''沿用修改前v4.1的同一50条输入（49种现实情境＋1次预定重复），于北京时间 **{local(start)}—{local(end)}** 逐项通过网页提交真实Codex。输入在开发前冻结，不按预期结果修改，没有Mock或故障注入，也没有重跑覆盖失败。模型记录为CLI配置默认值，不据此虚报精确远端型号。

43项测试版本文件在整轮期间不变；7,788项历史文件哈希不变。50份网页字段与保存输入一致，294份调用诊断中292份收到有效模型响应、2份超时；有效响应与Trace逐一对应。最终工具复算无错误。见 [机器核验](../evaluations/realistic-50-v5-20261104/results.json)、[逐例评阅](../evaluations/realistic-50-v5-20261104/逐条复盘.csv) 和 [全部记录](../evaluations/realistic-50-v5-20261104/README.md)。'''
outcomes='''## 实际效果：什么需求现在做得更好

|案例|修改前v4.1|当前v5|实际收益|
|---|---|---|---|
|V22 中英双语展览|因没有英文事实原文而停止|中文旁白＋英文屏幕译文，三镜28秒完成|直接完成原先被逐字限制阻断的双语需求|
|V30 八秒三功能|长原文12.8秒，要求用户补短原文|三条有来源短句、三镜6.3秒完成|不丢功能，也不把依次卡片伪装为同步|
|V21 英语社团|12步、14响应，英文主要作场景叙事|4镜32秒，事实准确译为英文旁白；6步、7响应|功能与受众语言一致，减少本次返工|
|V20 横竖屏双交付|三镜14秒，末尾另放功能卡|两镜9.8秒，信息直接随大厅屏和手机呈现|更简洁，画面与功能说明结合|
|V45 旧稿压缩|45秒旧稿改到10秒，9响应|同一旧稿改到13秒，8响应；保留标题原文，补全动作和声画标记|有效修订同时保留可用内容，便于拍摄|
|V48 民宿客户返修|后两镜为“先看看招牌／再看看室内”|改成入口指引与室内导览，三镜15秒|减少空泛串场，保留镜头约束与仅讲字幕的范围|

上述均为实际保存结果，详见 [精选7组证据](../examples/v5-live/evaluation.md)。V45先观察45秒超限再改稿；V25先观察“只讲字幕却多讲手动编辑”的审核失败再删除；V46观察规则风险后移除无依据宣传。不同后续动作来自真实模型响应，未预制决策日志。

声画结构已实际用于纯静音V17/V31、英语V21、双语V22及旧稿迁移。V31每张卡的实际文字就是5字和8字，各停5秒；旧版把完整长句放在一个block，再靠visual说明拆卡。新稿累计有26处文案不同于来源原句，原句及ID仍保留供复核。

## 整体对照与代价

|观察|修改前v4.1|当前v5|
|---|---:|---:|
|同一输入的真实网页任务|50|50|
|完成脚本|36|36|
|需补资料|14|12|
|模型超时停止|0|2|
|有效模型响应|317|292|
|双方均完成的34例响应合计|262|250|
|全部任务耗时中位数|206.8秒|314.1秒|
|双方均完成的34例耗时中位数|223.8秒|353.1秒|

**整体完成数持平，完成范围发生了变化：V22/V30新增完成，V05/V28本次超时。** 292是收到响应的次数；包括失败调用的尝试为294，不等同付费金额。调用减少不代表运行更快，本轮等待实际更长。旧轮前段两路、后段四路；新轮四路，且运行时段、系统负载与远端模型状态不同，因此耗时是观察记录，不当作速度因果实验。

逐例综合评阅为 **21例改进、13例相当、4例退步、12例仍需补充**。这是参与开发的AI助手阅读原需求、新旧稿件和Trace后的判断，不是独立盲评，也不是生产准确率。未观察到最终完成稿违反明确硬要求或编造产品能力；这个样本观察不等于已证明不存在语义错误。

## 尚未解决的实际问题

1. **标题个性化退步。** 新版22份稿件复用四个示例标题之一，旧版仅2份；部分开头和结尾也偏泛。V32把具体错字示例写泛，教学信息弱于旧版。这是当前最明确的内容优化方向。
2. **自然模型超时仍存在。** V05/V28检索后写稿超时，未生成脚本，诊断和检查点均完整保存；没有重跑覆盖。本轮不能宣称稳定性提高。
3. **仍有可避免的返工。** V25首稿多讲手动编辑，审核后改正，响应7→12；V07/V46各有一次空文案块格式错误后恢复。结构化输出与范围遵循还不完全稳定。
4. **地道杭州话没有完成。** V24仍请求口语参考。资料库没有收费、导出、隐私或其他产品资料时，不能靠改写补出事实；新版已尽量只问完成任务所需的最少信息。
5. **时间仍为估计。** 已区分同步与串行、英文词和汉字，但没有用真实配音校准，也没有生成成片。该边界符合原题脚本任务，不能称为实测成片时长。

测试期间不再改应用，避免将不同版本混成一次50组结论。后续优先处理标题/结尾的场景针对性和调用耗时，再用相同输入检验；不靠放宽事实要求或去掉审核来提高数字。

## 对笔试评审的价值

原题明确看重有效修订与事实可追溯。现在评审既能看到有依据的改写、翻译、压缩实际解决了需求，也能逐步核对工具反馈怎样影响下一步；分镜用途、声画节拍和可见动作让结果更容易实际使用。50次完整记录、失败保留、旧版对照和118项自动测试提供可复核依据。没有为了展示框架而加入多Agent或生产部署。

这50组是自然创作需求，不覆盖所有受控故障设置。原题完整8类验收记录仍保留于历史 `examples/live/` 与 `examples/mock/`，标明原版本；本轮118项测试继续验证相应代码路径，不把旧故障实验改名为新实验。
'''
p=D/'15-v5-effective-scripts.md';text=p.read_text(encoding='utf8')
text=text.replace('真实网页50次实验正在按冻结协议执行，最终数据和逐例结果将在全部归档后填写。当前源代码保持冻结，不能把中途结果称为完整50次结论。',method+'\n\n'+outcomes)
p.write_text(text,encoding='utf8')

p=ROOT/'README.md';old=p.read_text(encoding='utf8');tail=old[old.index('## 网页人工测试'):]
head='''# 短视频脚本 Agent · 第4题

给定主题、受众、平台、目标时长和风格，生成有事实依据、可拍摄的分镜脚本；模型根据检索、估时及审核结果决定改稿、补查或结束。

**当前v5：自然改写与翻译、旁白/屏幕节拍、具体分镜。** 保留单Agent、Python标准库和12步上限，网页与CLI共用核心循环。

**评审入口：** [实际效果报告](docs/15-v5-effective-scripts.md) · [7组精选证据](examples/v5-live/evaluation.md) · [全部50次对照](evaluations/realistic-50-v5-20261104/README.md) · [五分钟路线](docs/13-reviewer-and-practice-guide.md) · [提交清单](docs/06-submission.md)

实测收益：双语需求V22由未完成变为28秒成稿；八秒三功能V30由12.8秒超限变为6.3秒完成；民宿返修V48把空泛串场改成入口和室内导览，同时保留用户指定镜头。来源原文与改写文案分别保留，声画同步关系直接显示在网页和Markdown中。

**118项自动测试全部通过。50次真实模型网页实验：292次有效响应，36完成、12需补资料、2次模型超时。** 修改前36完成、14需补资料；新增完成的两例被两次超时抵消，整体完成数持平。逐稿评阅为21例改善、13例相当、4例退步、12例仍需补资料；参与开发的AI助手评阅，非独立盲评。标题泛化与等待时间增加是当前实际问题，报告列出具体例子和成本。

输入预先冻结，与修改前逐字相同，未按预期结果反推；全部通过网页提交真实Codex，无故障注入、无Mock替代、不重跑覆盖失败。每次保存输入、实际输出、Trace、截图和诊断。43项版本文件与7,788项历史文件哈希未变，50份产物复算一致。旧源码、旧测试和旧项目包均保留。

|核对内容|入口|
|---|---|
|原题范围与验收|[需求](docs/01-requirements.md)|
|改写依据、声画估时、动态决策|[实现方案](docs/02-solution.md)|
|实际测试及版本边界|[评估](docs/03-evaluation.md)|
|AI辅助与候选人贡献|[AI使用](docs/04-ai-usage.md)、[复盘](docs/05-retrospective.md)|
|前一版本的原始50次实验|[v4.1历史报告](docs/14-v41-real50-comparison.md)|

本地提交包已整理；尚未推送最终GitHub提交或交卷。题目要求的仓库URL、最终commit SHA、读取权限及候选人实际投入记录，见提交清单。

'''
tail=tail.replace('在“脚本预览”看分镜、旁白、来源、估时与需求核对','在“脚本预览”看分镜、旁白/屏幕文字、节拍、来源、估时与需求核对')
p.write_text(head+tail,encoding='utf8')

p=D/'03-evaluation.md';old=p.read_text(encoding='utf8').replace('## 当前 v4.1 提交前优化版','## 历史 v4.1 提交前优化版',1)
section='''## 当前v5效果优化与50次真实网页对照

118项自动测试全部通过，记录见 `evaluations/realistic-50-v5-20261104/development-tests/final/`。50次真实网页实验、292次有效响应，36 completed、12 needs_input、2 blocked；两次blocked均为自然模型超时，未注入业务工具故障。新旧状态变化为V22/V30由未完成到完成，V05/V28由完成到超时，总完成数持平。

逐稿评阅21改善、13相当、4退步、12仍需补资料；全部50例和证据索引见 [本轮目录](../evaluations/realistic-50-v5-20261104/README.md)，实际收益和代价见 [效果报告](15-v5-effective-scripts.md)。34组双方完成案例的响应262→250，但耗时中位数223.8→353.1秒；不宣称更快。所有新旧稿均可查看，评阅不是独立盲评。

最终核验43项源码及7,788项历史文件不变；全部输入、网页产物、模型诊断及工具复算一致。50组v4.1历史记录在新代码下重放无差异。精选7组输入/输出/Trace置于 [examples/v5-live](../examples/v5-live/evaluation.md)，包含正常、双语、短表达、动态修订、资料不足及自然模型错误。历史8类原题验收仍保留原版本标签，本轮没有重新执行受控故障实验。

'''
p.write_text(old.replace('# 03 · 测试、实际结果与限制\n','# 03 · 测试、实际结果与限制\n\n'+section,1),encoding='utf8')

p=D/'05-retrospective.md';old=p.read_text(encoding='utf8').replace('## v4.1 本轮复盘','## v4.1 历史复盘',1)
section='''## v5：让事实约束服务于成稿

这轮最有价值的变化是把“有依据”与“逐字照抄”分开：来源身份和原文可由代码核对，准确改写与翻译交给绑定同一稿件的语义审核。V22与V30因此从停止变为完成。声画分轨也让双语、静音卡和顺序文字有直接可执行的时间安排。

分镜不是给功能清单配背景。V48的入口指引、V45/V47/V49具体动作比原先名词镜头更好用；但V32的具体错字例子被写泛，22份稿复用示例标题，说明提示中的示例仍可能压过场景创作。后续应优先改善成稿的针对性，不继续堆叠审核层。

实际50次结果是36完成、12需补、2超时，与旧版完成数持平。内容评阅21改善、13相当、4退步、12需补；新能力确实完成了旧版受阻的任务，但没有证据说所有需求都更好或运行更稳定。完整对照见 [v5报告](15-v5-effective-scripts.md)。本人投入与独立复验仍需候选人如实补充。

'''
old=old.replace('## v4.1 历史复盘',section+'## v4.1 历史复盘',1)
old=old.replace('本项目将公开文案拆成引用事实与允许的连接语，事实必须逐字对应已检索原文；标题和画面指令也要遵守批准列表。这是一个有明确限制、但可以机械验证的取舍。','早期版本要求逐字引用和批准表达；v5改为保留来源原句、允许准确改写并做语义核对。来源存在性可以机械验证，句子是否真正受原文支持仍需语义判断。')
p.write_text(old,encoding='utf8')

p=D/'13-reviewer-and-practice-guide.md';old=p.read_text(encoding='utf8');begin=old.index('## 五分钟看什么');endsection=old.index('## 候选人建议亲自做的三件事')
route='''## 五分钟看什么

1. **一分钟看成稿收益。** 对照 `examples/v5-live/V22/script.md` 与旧版V22：中文旁白和英文字幕同步，28秒完成；再看V30如何用有依据的三条短句完成八秒需求。
2. **两分钟看动态修订。** `examples/v5-live/V45/trace.jsonl` 先估出旧稿45秒，模型再调整为13秒。核对原标题、原文和镜头顺序保留。V25展示审核发现多讲功能后，模型删除并重检。
3. **一分钟看真实失败。** V05写稿超时仍保存检查点和诊断；V34缺收费事实准确追问。业务工具受控故障的历史证据在 `evaluations/final-polish-20261104/runs/P07/` 和 `P08/`，有明确版本标签。
4. **一分钟看整体。** [效果报告](15-v5-effective-scripts.md)同时给出21例改善、4例退步及整体完成数持平；打开118项测试摘要与50份逐例对照，不只看精选成功稿。

网页入口运行 `python -m src.web --open`。当前全部记录见 `evaluations/realistic-50-v5-20261104/README.md`，精选7例已放在 `examples/v5-live/`。

'''
p.write_text(old[:begin]+route+old[endsection:],encoding='utf8')

(D/'06-submission.md').write_text('''# 提交清单与答题框模板

当前 **v5效果优化版** 的代码、118项自动测试、50次真实网页记录、逐例对比和报告已在本地整理。三项优化是有依据的改写/翻译、声画节拍、可拍分镜。主报告为 [15-v5-effective-scripts.md](15-v5-effective-scripts.md)，精选证据为 [examples/v5-live](../examples/v5-live/evaluation.md)。

最新快照：`小影科技笔试_第4题_v5_效果优化与50次复测提交包.zip`。包内DELIVERY.json记录各文件哈希；旧源码归档、全部测试及失败记录保留。根目录已有旧ZIP保留在本地，不重复嵌套进新包；历史7,788项哈希核验针对开发工作区，新包自身按DELIVERY.json核验。

**尚未推送最终Git commit或交卷。** 本地无GitHub远程，旧基线SHA不能标作最终版本。需要真实仓库URL、推送后的完整SHA、私有仓库的评审读取权限；候选人实际投入时间与本人复验也须据实填写。

## 答题框模板

```text
选择题目：第4题——短视频脚本Agent
GitHub URL：填写实际仓库地址
最终commit SHA：填写已推送的完整SHA

运行和评审入口：README.md
当前效果及前后对照：docs/15-v5-effective-scripts.md
五分钟证据路线：docs/13-reviewer-and-practice-guide.md
需求、方案、评估、AI辅助与复盘：docs/01–05
精选输入、实际输出、Trace：examples/v5-live/
50次网页真实实验及逐例评阅：evaluations/realistic-50-v5-20261104/
118项自动测试：evaluations/realistic-50-v5-20261104/development-tests/final/

运行：python -m src.web --open
自动测试：python -m scripts.run_tests
离线入口：python -m src.cli --provider mock --input examples/inputs/normal.json --output outputs/demo
真实模型：网页选择Codex，或按README配置模型API。

新稿支持有来源的自然改写和翻译，明确旁白、屏幕文字和播放节拍。
实测双语需求由未完成变为28秒成稿，八秒三功能由超限变为6.3秒成稿。
50次真实实验共292次有效响应：36完成、12需补资料、2次模型超时；全部记录保留。
模型依据实际检索和检查结果调整下一步，宿主绑定同一稿件验证检查结果并限制12步。
AI辅助及个人贡献见docs/04-ai-usage.md；个人投入与复验记录据实填写。
```

## 最后提交步骤

1. 按五分钟路线亲自运行并理解至少一条实际修订链，填写本人时间与复验记录。
2. 在同一个GitHub仓库放入代码、文档、examples、evaluations及源码archives，勿加入凭证、.env、.runtime或私人资料。所有实验网页输出已复制到对应runs目录，便于集中审阅。
3. 创建最终commit、推送，打开远程README与Trace核对内容和读取权限，再复制完整SHA到答题框。

以下是待执行命令，本轮没有代为推送或交卷：

```bash
git add README.md PRODUCT.md DESIGN.md src web tests scripts data docs evaluations examples requirements.txt .env.example .gitignore run.ps1 启动网页.cmd
git add -f archives
git commit -m "Improve grounded expression, audiovisual timing and storyboard evidence"
git remote add origin <实际仓库URL>
git push -u origin HEAD
git rev-parse HEAD
```

已配置origin时不要重复添加。ZIP可以作为附件，不能替代题目指定的GitHub URL与SHA。新环境的网页历史由outputs读取，若使用精简仓库，先运行一次才会有历史；完整提交包保留outputs。
''',encoding='utf8')

p=D/'04-ai-usage.md';p.write_text(p.read_text(encoding='utf8')+f'\n最终网页实验由AI助手执行：{metrics}逐例评阅21改善、13相当、4退步、12仍需补资料，由同一开发助手审读，不是候选人亲自测试或独立盲评。实际运行窗口见 `evaluations/realistic-50-v5-20261104/work-session.json`。\n',encoding='utf8')
p=D/'superpowers/plans/2026-11-04-v5-effective-scripts.md';text=p.read_text(encoding='utf8');text=text.replace('- [ ]','- [x]');text=text.replace('- [x] 更新提交文档、效果报告与新ZIP，核验内容哈希。','- [ ] 更新提交文档、效果报告与新ZIP，核验内容哈希。');p.write_text(text,encoding='utf8')
print(json.dumps({'window':[local(start),local(end)],'updated':'README and docs01–06,13,15; all previous reports retained'},ensure_ascii=False))
