# 首次真实后端尝试：环境失败记录

该轮在受限执行沙盒中启动 Codex，无法写入 Codex 自身状态数据库/临时目录，七个需要模型的场景均在第一步出现 `model_error`，没有成功模型响应。缺信息场景由宿主前置校验返回。

当时的验收脚本只凭部分负例的 blocked 状态，会把 no_material 与 impossible_duration 错算为通过。本轮修复了该判断：模型错误不得替代业务负例证据，无素材还必须出现真实空检索结果。

原 `evaluation.json` 和所有失败产物保留原样。按新规则重新判断的结果见上级 `audit.json` 的 `startup_attempt_reassessment`：只有缺信息前置校验可通过，不能说此轮真实模型验收通过。

恢复正常本机执行权限后，完整验收另存 `../live-verified/`。没有改登录凭据或默认模型配置，也没有以 Mock 替代真实模型。
