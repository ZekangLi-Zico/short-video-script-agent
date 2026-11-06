# v4有限修复真实复测记录

最终应用源码下完成9次真实Codex实验，共60次实际模型响应：6次不注入故障的原始需求复测均completed；3次受控故障分别验证清理不中断、异常保留、进程退出恢复。其中后两次正确返回blocked，不能称为业务完成。另有首轮核心修复3次实验、21响应独立保存在live/。本轮共12次真实实验、81响应，不是新一轮50个独立场景。

95项自动测试全部通过，8组Mock验收通过；这两类与真实模型证据分开。所有实际数据来自本机合成素材库。

## 结果索引

|组别/案例|状态|步/模型响应|估时秒|说明|
|---|---|---|---|---|
|[live-final/cleanup_lock](live-final/cleanup_lock/script.md)|completed|6/7|16.5|模型第一次真实响应的诊断记录PermissionError和cleanup_deferred，response_received=true；真实动作继续执行，最终6步7响应、16.5秒completed。故障为受控注入，不能称本次自然发生文件锁。|
|[live-final/process_exit](live-final/process_exit/script.md)|blocked|2/2|未检查|真实模型完成两步并保存草稿后进程退出；恢复前没有output.json且原进程已不存活。恢复后为blocked，草稿与两步Trace保留，两份模型诊断哈希不变，恢复未新增模型响应。原生预设退出码86，工具只捕获PowerShell会话码1，未冒称原生码已观测。|
|[live-final/runtime_exception](live-final/runtime_exception/script.md)|blocked|2/2|未检查|真实模型检索和写稿后注入RuntimeError；两步Trace及草稿与检查点一致，正常输出文件保存完整，状态blocked。未编造估时或审核结果。|
|[live-final/V26](live-final/V26/script.md)|completed|6/7|4.0|单镜头仅展示“开讲”卡片，引用P01.F1，未增加其他功能或寒暄；4秒估时满足6秒上限。审核明确hold_seconds=0不等于零时长。|
|[live-final/V27](live-final/V27/script.md)|completed|6/7|8.8|恰好两镜，剪刀/胶片后接横竖相框，P02.F1与P03.F1正确；8.8秒满足10秒上限。没有额外开场或结尾。|
|[live-final/V28](live-final/V28/script.md)|completed|6/7|41.6|六镜以社区分享会素材串联裁剪、字幕、手动改字、比例选项，四项事实各一次；41.6秒处于40.5—45秒区间。各镜有观察或动作，无重复事实凑时长；审核明确使用逐镜估时，没有要求另填最低停留。|
|[live-final/V29](live-final/V29/script.md)|completed|6/7|58.0|七镜围绕已有交接录像，包含裁剪、字幕、手动核对与比例选择；用纸条、纸框说明，未捏造软件按钮。58秒处于54—60秒区间。均有具体观察/动作；估时不是配音实测。|
|[live-final/V46](live-final/V46/script.md)|completed|12/14|20.5|保留字幕添加与手动编辑，删除旧稿自动识别/99%宣传；最终20.5秒。第一次审核仍发现缺少删除原因和静物停留偏长，模型再改稿通过。0秒最低停留的第三镜被正确识别为8.5秒估时。修订说明放入成片可能不如单列编辑备注自然，留待人工取舍。|
|[web/V01](web/V01/script.md)|completed|6/7|15.0|三镜依次为蒸笼、手写菜单、打包台，均排除顾客正脸；只引用P01.F1，15秒。口播短句与产品事实卡分工清楚，仍需拍摄剪辑核对实际节奏。网页检查点下载成功，但下载操作返回时任务已结束，下载内容为最后一步检查点。|

## 证据与边界

- [修复报告](../../docs/10-finite-v4-report.md)：根因、代码修改、原题收益、前后对照及未解决问题。
- [复测范围](复测范围.md)、[阶段区分](phase-note.md)：需求来自上一轮冻结文件，首轮与最终源码分开。
- [逐条复盘CSV](逐条复盘.csv)、[机器复算](audit.json)：原始输入一致性、12组产物/诊断、19项最终源码及3128项历史文件哈希；均无差异或错误。复算不重新调用模型，也不保证语义正确。
- [95项测试](tests-final/summary.json)、[8组离线验收](mock-acceptance-final/evaluation.json)：覆盖真实时长上下文、过期稿件失效、清理异常、保存失败、恢复、原子替换和网页下载。
- [Windows进程检测](windows-owner-check.json)：真实子进程存活与退出均正确识别；检测未终止子进程。
- [修改清单](code-changes.json)、[代码差异](code-changes.patch)：与修复前源码ZIP比较。
- 每个真实实验保存输入、数据快照、最终输出、Trace、manifest、checkpoint、run状态标记及逐次模型诊断。diagnostics不复制原始stdout/stderr或内部思维内容。
- [网页证据](web/V01/ui-verification.json)：运行中看到检查点入口并点击，浏览器下载返回时任务已结束，下载内容是第6步检查点，与后台一致。不能将其误记为第2步文件；中途HTTP可下载由单独自动测试验证。
- 受控故障由evaluate_finite.py注入，不属于自然发生的故障率；process_exit工具会话返回码为1，原生预设码86没有被单独捕获。恢复前原进程已退出、仅有检查点；恢复后不新增模型诊断。
- 评阅是同一AI开发助手读取原始需求和实际产物，不是独立盲评；completed不是所有创作细节正确的保证。

## 复核

在仓库根目录运行 `python -m scripts.audit_finite --require-complete`。新真实复测使用 `python -m scripts.evaluate_finite --case V29 --output outputs/new-review-V29`，必须选择尚不存在的目录，避免覆盖。真实模型有随机性与服务可用性限制。
