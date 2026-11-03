# 01 · 需求与成功标准

## 用户与目标

服务需要快速起草短视频脚本的创作者。输入主题、受众、平台、目标时长和风格，结合产品资料与品牌规则输出有事实依据、满足预计时长上限的可编辑脚本。资料不足时明确指出缺口；不编造卖点或伪称完成。

## 输入与材料

- 六项必填：`topic`、`audience`、`platform`、`target_seconds`、`style`、`product_id`。
- 可选 `initial_script`，支持检查和修订已有稿件。该扩展用来复现超时与无依据宣传场景。
- `data/materials.json`：合成资料，带产品 ID、素材 ID、事实 ID、版本日期与事实原文。
- `data/brand_rules.json`：允许的连接语/标题/画面指令、禁用表达、语速估算参数。

## 范围

实现 CLI、三个本地工具、单 Agent 动态决策循环、真实模型适配器与离线 Mock、测试和运行记录。按用户追加需求提供本地网页，便于填写输入、查看实际执行过程与下载结果；网页不改变题目验收标准。不包含线上部署、多 Agent、视频生成或发布。

## 验收映射

| 题目要求 | 实现 | 运行证据/测试 |
|---|---|---|
| 正常生成 | 检索→生成→检查→结束，顺序由模型选择 | `normal`；`test_valid_completion_and_saved_artifacts` |
| 缺关键信息 | 输入校验返回 needs_input，列出缺失字段 | `missing_information` |
| 无素材 | 模型观察空检索后补查或请求补充 | `no_material` |
| 工具失败 | 错误返回模型；模型选择重试或停止 | `tool_failure`、`recoverable_failure` |
| 超时修订或明确失败 | 绑定原时长上限，修改后复检 | `over_duration`、`impossible_duration` |
| 规则不通过后调整 | 展示风险位置，模型替换无依据文案，再检查 | `rule_revision` |
| 标题、分镜、旁白/字幕、总时长 | `output.json` 与 `script.md` | 正常输出及超时修订输出 |
| 来源 ID、风险、任务状态 | 事实块、citations、issues、status | 规则检查及来源测试 |
| 至少两条动态路径 | 真模型实际观察不同工具结果后调整 | `examples/live/` 的 Trace |
| 至少三组输入、输出、运行记录 | 八种场景分目录保存 | `examples/mock/` 与 `examples/live/` |
| 执行上限 | 12 步默认上限，超限 step_limit | 提前完成/未知动作/上限测试 |

## 成功标准与边界

`completed` 必须满足当前脚本结构合法，至少有一条来源事实，所有公开文案通过规则检查，预计总时长不超过上限，检查哈希与当前稿一致。来源、产品、目标上限都由宿主绑定，模型不能改检查参数绕过约束。

场景验收的成功不等于业务任务均应 completed。例如无素材预期为 needs_input/blocked，工具持续失败预期为 blocked/step_limit，不能把失败场景强行包装成成功。

时长是上限而非必须接近目标；只支持文本估算。输入缺失由确定性前置校验处理，不将该路径宣传为模型自主追问的证据。
