# v6实际网页证据精选

全部来自正式50次网页实验，复制实际产物，没有重新生成。完整结果见 [50次索引](../../evaluations/realistic-50-v6-20261105/README.md)。

|案例|核对重点|实际状态|证据|
|---|---|---|---|
|V01|早餐摊标题与场景|completed|[输入](V01/input.json) · [脚本](V01/script.md) · [Trace](V01/trace.jsonl) · [评阅](V01/review.json)|
|V05|上轮超时的修理铺需求|completed|[输入](V05/input.json) · [脚本](V05/script.md) · [Trace](V05/trace.jsonl) · [评阅](V05/review.json)|
|V22|中英双语需求|completed|[输入](V22/input.json) · [脚本](V22/script.md) · [Trace](V22/trace.jsonl) · [评阅](V22/review.json)|
|V28|45秒功能介绍|completed|[输入](V28/input.json) · [脚本](V28/script.md) · [Trace](V28/trace.jsonl) · [评阅](V28/review.json)|
|V45|旧稿压缩|completed|[输入](V45/input.json) · [脚本](V45/script.md) · [Trace](V45/trace.jsonl) · [评阅](V45/review.json)|
|V34|收费资料缺口|needs_input|[输入](V34/input.json) · [脚本](V34/script.md) · [Trace](V34/trace.jsonl) · [评阅](V34/review.json)|
|V46|旧稿无依据宣传|completed|[输入](V46/input.json) · [脚本](V46/script.md) · [Trace](V46/trace.jsonl) · [评阅](V46/review.json)|

历史故障实验仍在examples/live、examples/mock及旧评估目录，版本标签不变；正式50次不注入故障，不能当作本版重新执行了所有受控故障场景。129项离线自动测试仅证明代码契约，不计作真实模型实验。
