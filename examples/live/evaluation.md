# 实际验收结果

模型入口：codex。Mock 不证明真实模型决策效果。

| 场景 | 状态 | 验收 | 步数 |
|---|---|---|---|
| [normal](normal/script.md) | completed | 通过 | 5 |
| [missing_information](missing_information/script.md) | needs_input | 通过 | 0 |
| [no_material](no_material/script.md) | needs_input | 通过 | 3 |
| [tool_failure](tool_failure/script.md) | blocked | 通过 | 4 |
| [recoverable_failure](recoverable_failure/script.md) | completed | 通过 | 6 |
| [over_duration](over_duration/script.md) | completed | 通过 | 7 |
| [rule_revision](rule_revision/script.md) | completed | 通过 | 7 |
| [impossible_duration](impossible_duration/script.md) | needs_input | 通过 | 1 |
