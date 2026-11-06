# 实际验收结果

模型入口：codex。Mock 不证明真实模型决策效果。

| 场景 | 状态 | 验收 | 步数 |
|---|---|---|---|
| [normal](normal/script.md) | blocked | 失败 | 1 |
| [missing_information](missing_information/script.md) | needs_input | 通过 | 0 |
| [no_material](no_material/script.md) | blocked | 通过 | 1 |
| [tool_failure](tool_failure/script.md) | blocked | 失败 | 1 |
| [recoverable_failure](recoverable_failure/script.md) | blocked | 失败 | 1 |
| [over_duration](over_duration/script.md) | blocked | 失败 | 1 |
| [rule_revision](rule_revision/script.md) | blocked | 失败 | 1 |
| [impossible_duration](impossible_duration/script.md) | blocked | 通过 | 1 |
