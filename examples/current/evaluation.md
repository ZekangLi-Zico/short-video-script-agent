# 当前提交证据 · v7.3.1-submission

本目录保存四类**通过网页、使用真实Codex模型**执行的验收记录。输入在运行前冻结，没有按生成结果改写。两条正常业务完成；两条负向场景分别请求资料、报告工具失败，四类均符合验收要求。共18次模型响应、18次调用尝试、0次超时。

| 场景 | 实际输入与结果 | 状态 | 运行耗时 | 过程 |
|---|---|---|---:|---|
| 产品正常稿 | [输入](product_normal/input.json) · [脚本](product_normal/script.md) · [JSON](product_normal/output.json) | completed；3镜，24.8秒 | 120.91秒 | [Trace](product_normal/trace.jsonl)：检索→写稿→审核→完成 |
| 超时旧稿修订 | [输入含旧稿](over_duration/input.json) · [修订稿](over_duration/script.md) · [JSON](over_duration/output.json) | completed；38秒→7.3秒 | 75.44秒 | [Trace](over_duration/trace.jsonl)：先发现超时，再补查、改稿、复检 |
| 无素材 | [输入](no_material/input.json) · [实际返回](no_material/output.json) | needs_input；未生成脚本 | 29.41秒 | [Trace](no_material/trace.jsonl)：两次实际空检索，第二次缩短查询，随后要求补资料 |
| 工具持续失败 | [输入](tool_failure/input.json) · [实际返回](tool_failure/output.json) | blocked；未生成脚本 | 37.53秒 | [Trace](tool_failure/trace.jsonl)：三次检索故障，改变查询后仍失败，明确停止 |

工具失败由网页“素材检索持续失败”设置受控注入，不是自然故障；模型响应是真实调用，未使用Mock。无素材使用资料库里没有资料的项目，两次检索工具都正常返回0条，不能和模型调用失败混为一谈。

超时案例的需求是“不超过30秒”，并非接近30秒；模型保留原两句文案和两镜顺序，去掉两镜各19秒的长停留，转换为带动作与说话者的v3格式。最终7.3秒是脚本估算，不是实际配音长度。修订统计按完整结构块比较，格式转换后可能显示0个块原样保留；上述两句文字事实上未变，可对照输入与输出。

每组保留原始输入、输出、Trace、资料快照、运行清单、检查点及模型诊断，与原网页运行目录逐文件相同。网页输入快照和页面截图在[本轮报告目录](../../evaluations/submission-v7.3.1-20261106/README.md)，[机器统计](../../evaluations/submission-v7.3.1-20261106/live-results.json)可查看全部核验项。

```bash
python -m scripts.verify_evidence --group current
```

此命令只复算本地工具、检查绑定及Trace一致性；不调用远端模型。缺必填字段、步数上限、规则误用等另外由[161项自动测试](../../evaluations/submission-v7.3.1-20261106/automated/summary.json)覆盖，历史真实验收见[examples/live](../live/evaluation.md)。历史原始结果不改写为本轮版本。
