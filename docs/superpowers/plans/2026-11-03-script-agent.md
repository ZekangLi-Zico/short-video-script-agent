# Script Agent Implementation Plan

**Goal:** 完成第 4 题代码、可执行测试、运行证据与五份说明文档。

**Architecture:** Python 标准库 CLI；模型输出结构化动作，本地执行工具并将观察重新输入模型。检查结果与稿件哈希绑定，离线 Mock 单独标记。

**Tech Stack:** Python >= 3.11, unittest, urllib, optional Codex CLI.

**Spec:** ../specs/2026-11-03-script-agent-design.md

## Global Constraints
- 所有资料合成；无真实密钥、隐私资料。
- 运行不需要 UI、部署、多 Agent 或视频生成。
- 每次运行最多 12 个模型决策步骤（可通过 CLI 调整，硬上限 50）。
- 模型超时、工具失败、未完成必须有明确状态。

## Review Focus
- 修改脚本后复用过期检查：测试哈希与检查失效。
- 引用真实 ID 但编造文本：测试逐字事实核验。
- 工具失败却继续声称完成：测试完成门禁。
- 模型输出非法结构/未知动作：测试有界错误反馈。
- 目标时长为负数/布尔值/NaN：测试输入校验。

## Task 1 — 数据、工具、协议
- [x] data/materials.json, data/brand_rules.json, src/schema.py, src/tools.py。
- [x] 检索限制产品、来源原文匹配、时长边界和失败注入测试。

## Task 2 — 决策循环、模型接入、CLI
- [x] src/agent.py, src/providers.py, src/mock.py, src/cli.py。
- [x] 真模型 JSON 动作协议；API 与 Codex CLI；Mock 不冒充模型。
- [x] 完成门禁、改稿失效、最大步数、错误恢复与产物测试。

## Task 3 — 验收与交付
- [x] scripts/evaluate.py 跑验收场景并保存输入、输出、Trace、评估。
- [x] 运行真实模型并保留观察变化后的后续动作；不能运行则如实记录。
- [x] README、五份文档、提交模板、依赖与配置说明。
- [x] 完整测试、静态编译、材料清点与密钥检查。
