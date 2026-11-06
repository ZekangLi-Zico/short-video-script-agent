# v5真实网页证据精选

以下全部来自冻结版本的50次真实网页实验，复制原始记录，没有重新生成或修饰结果。完整50组及旧版对照在 `evaluations/realistic-50-v5-20261104/`。

|例子|核对重点|实际结果|证据|
|---|---|---|---|
|V22|双语事实表达与声画同步|completed|[输入](V22/input.json) · [输出](V22/script.md) · [Trace](V22/trace.jsonl) · [评阅](V22/review.json)|
|V30|八秒三功能短表达|completed|[输入](V30/input.json) · [输出](V30/script.md) · [Trace](V30/trace.jsonl) · [评阅](V30/review.json)|
|V45|旧稿45秒到13秒的有效修订|completed|[输入](V45/input.json) · [输出](V45/script.md) · [Trace](V45/trace.jsonl) · [评阅](V45/review.json)|
|V25|超出单功能范围后实际修订|completed|[输入](V25/input.json) · [输出](V25/script.md) · [Trace](V25/trace.jsonl) · [评阅](V25/review.json)|
|V46|删除无依据宣传并保留叙事|completed|[输入](V46/input.json) · [输出](V46/script.md) · [Trace](V46/trace.jsonl) · [评阅](V46/review.json)|
|V34|收费资料不足的明确缺口|needs_input|[输入](V34/input.json) · [输出](V34/script.md) · [Trace](V34/trace.jsonl) · [评阅](V34/review.json)|
|V05|真实模型超时与已保存失败记录|blocked|[输入](V05/input.json) · [输出](V05/script.md) · [Trace](V05/trace.jsonl) · [评阅](V05/review.json)|

正常、资料不足、模型故障及多种动态修订均可直接查看。原题完整的8类验收（含缺必填字段、空素材、受控业务工具故障）仍在 `examples/live/`、`examples/mock/` 和历史定向实验中，均保留原版本标签；本次自然场景50组未注入故障，不将历史故障实验冒充v5新跑结果。

自动测试的新结果见 `evaluations/realistic-50-v5-20261104/development-tests/final/`，118项全部通过；离线测试不计入50次真实实验。
