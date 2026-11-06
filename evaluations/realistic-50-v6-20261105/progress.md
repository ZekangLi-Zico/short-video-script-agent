# Ledger — docs/superpowers/plans/2026-11-05-v6-latency-and-titles.md

保留完成：657文件源码归档，9944历史文件哈希。诊断基线：22模板标题、2次写稿超时、任务中位314.1秒。

Ruling: 在用户指定现有目录执行，使用不可覆盖归档而非git worktree；.git只读，既有修改不动，不执行技能里的提交/清理步骤。
Pre-flight: 自动预检查与回放器共享Trace契约；完整原始检查保留preflight_checks。重试与审计共享call_id契约，失败不计作模型响应但单独保存。

Task 1/2: implementation complete; first 125 tests passed. Added 11 focused v6 tests, each bug regression observed RED then GREEN (green-review-fixes.txt).
Final review: /root/review_v6 independent fresh-context review. Important: retrieval-set cache stale; cancelled review still starts a call. Both fixed RED→GREEN. Checkpoint interruption reproduced and fixed RED→GREEN. Full final suite follows.
Final: minor (deferred): cancel during a decision call that subsequently times out reports blocked, not cancelled; no further retry, preserved timeout diagnostics. Existing behavior, no new work or data loss. Document rather than broaden this round.
Ruling: retain full base Codex runtime instructions and configured model; only per-process effort=medium and compact application payload. Avoid broad global configuration changes. Longer inherited runtime input remains a potential cost.
Campaign running: first 27 cases archived via UI; 26 completed / 1 needs_input. V01-V27 read individually (out-of-order completions retained). Source frozen during campaign. Formal source final 129 tests passed before submission; all prior records remain unchanged.
Complete: 50 UI-submitted real-model experiments, 231 responses, 38 completed / 12 needs_input / 0 failed calls. Every case individually read and reviewed: 26 improved, 12 equivalent, 12 still need facts (AI developer assessment, not blind human review). Full audit: 44 frozen files and 9944 preserved historical files unchanged; all inputs, model metadata and tool replays match. Documentation and seven curated examples updated; local ZIP verification follows.
