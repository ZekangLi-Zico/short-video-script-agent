# v5 Effective Scripts Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [x]`) syntax for tracking.

**Goal:** 提高自然改写/翻译、声画时间安排和分镜内容质量，并用50次真实网页配对实验检验。

**Architecture:** 保持现有单Agent循环，版本化稿件结构兼容旧证据。明确来源验证和语义核对职责，新增声画节拍估时，网页呈现同步信息。

**Tech Stack:** Python标准库、原生JavaScript、已登录Codex、CUA网页操作。

**Spec:** docs/superpowers/specs/2026-11-04-v5-effective-scripts-design.md

## Global Constraints

- 旧版及所有历史测试文件保留；不覆盖旧证据。
- 最多12决策步；失败和缺资料如实返回，不能取消检查以提高完成率。
- 新格式voice/screen/both；beat=1–8；display_seconds=0–300。
- 真实实验只通过网页提交；沿用冻结50输入，不按结果调整输入。

## Review Focus

- 改写携带正确ID但增加功能/效果，必须由语义审核拒绝。
- 同步中英字幕与旁白不双计时，所有同屏文字仍有阅读预算。
- 新旧稿混用和保存重放不能破坏旧记录。
- purpose/备注不能替代观众实际看到的内容，修改时间结构使旧检查失效。
- 格式正确但空泛的镜头，生成指引要落实场景与信息用途，审核不能凭个人口味无限返工。

### Task 1: 格式、来源与声画估时
Files: src/schema.py, src/tools.py, src/timing.py, src/expression.py, tests/test_effective_v5.py
Interfaces: validate_script兼容旧稿；estimate_tracks(shot,rules)返回镜头与节拍估时；expression_slots枚举v2所有块；来源从素材提取原文。
- [x] 先写同步/串行、英文、改写引用及伪造ID测试并运行观察失败。
- [x] 实现格式、估时、引用及逐块语义门槛。
- [x] 运行新测试与原测试，修复契约冲突。

### Task 2: 成稿质量与展示
Files: src/providers.py, src/requirements.py, src/reporting.py, src/revisions.py, src/agent.py, web/app.js, scripts/verify_evidence.py, scripts/evaluate.py
Interfaces: 新稿schema、purpose、声画节拍检查结果；旧稿渲染/复算维持原路径。
- [x] 补充格式渲染、修订及证据重放测试，观察失败。
- [x] 更新生成/审核指引、来源与声画展示；不为实验题单独写规则。
- [x] 完整测试及独立代码审查，必要修复后再运行全套。

### Task 3: 真实网页实验与交付
Files: evaluations/realistic-50-v5-20261104/*, docs/15-v5-effective-scripts.md, README.md, docs/02–06
Interfaces: 已冻结cases.json；网页同样字段；每例独立不可覆盖文件夹。
- [x] 开发冒烟验证网页与真实模型新格式；冻结源码哈希。
- [x] 四路网页执行50次，逐个保存并审读，保留每个失败。
- [x] 验证结果复算、模型响应诊断、旧历史哈希；逐例对比真实成稿。
- [x] 更新提交文档、效果报告与新ZIP，核验内容哈希（最终校验记录见根目录提交包同名 `_校验.json`）。

## Execution notes

用户已明确要求按三项实施，直接原生执行，无额外选型确认。Git目录只读且现有工作区有大量历史修改，使用不可覆盖源码ZIP与哈希记录代替提交；不删除工作记录。最终按executing-plans要求安排一次独立代码审查。
