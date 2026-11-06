# v4.1 当前版本定向网页证据

8次网页提交，7组含真实Codex响应，共54次响应；P05为零调用输入校验。5 completed、2 needs_input、1 blocked。全部逐次保存，未用Mock或新结果覆盖失败。受控工具故障为P07/P08；其余没有注入业务故障。

| 场景 | 结果 | 步数 / 响应 | 估时 | 逐次证据 |
|---|---|---|---|---|
| P01 旧稿能力核对 | completed | 12 / 14 | 12 | [评阅](runs/P01/review.md) · [脚本](runs/P01/script.md) · [Trace](runs/P01/trace.jsonl) |
| P02 早餐摊口播 | completed | 6 / 7 | 13 | [评阅](runs/P02/review.md) · [脚本](runs/P02/script.md) · [Trace](runs/P02/trace.jsonl) |
| P03 字幕旧稿压缩 | completed | 8 / 9 | 12 | [评阅](runs/P03/review.md) · [脚本](runs/P03/script.md) · [Trace](runs/P03/trace.jsonl) |
| P04 旧稿能力核对（预定重复） | completed | 8 / 9 | 16 | [评阅](runs/P04/review.md) · [脚本](runs/P04/script.md) · [Trace](runs/P04/trace.jsonl) |
| P05 missing_information | needs_input | 0 / 0 | — | [评阅](runs/P05/review.md) · [脚本](runs/P05/script.md) · [Trace](runs/P05/trace.jsonl) |
| P06 no_material | needs_input | 3 / 3 | — | [评阅](runs/P06/review.md) · [脚本](runs/P06/script.md) · [Trace](runs/P06/trace.jsonl) |
| P07 tool_failure | blocked | 4 / 4 | — | [评阅](runs/P07/review.md) · [脚本](runs/P07/script.md) · [Trace](runs/P07/trace.jsonl) |
| P08 recoverable_failure | completed | 7 / 8 | 12.8 | [评阅](runs/P08/review.md) · [脚本](runs/P08/script.md) · [Trace](runs/P08/trace.jsonl) |

## 复核入口

- `cases.json`、`cases.sha256`、`protocol.md`：运行前冻结的需求与方法。
- `tested-source.json`：41项应用、数据、脚本及测试的版本哈希。
- `tests/summary.json`、`tests/unittest.txt`：101项自动测试通过。
- `mock-acceptance/evaluation.json`：8/8离线流程验收。
- `audit.json`：8组新记录、54次诊断/Trace响应一致，旧v4的50组内部复算通过，5438项历史文件未变。
- `runs/Pxx/`：原始brief、网页字段、提交前后DOM、截图、完整后台复制、每次模型诊断和实际评阅。
- `ui-harness-reference.js`：CUA网页提交/归档辅助函数的留档；并非独立可执行浏览器程序。P08点击超时后的显式填写见其ui-input说明。
- `final-web.png`：P01公开脚本与独立审稿备注的最终网页。
- [改进、对照与剩余问题](../../docs/12-final-polish-report.md)。

本次审核由同一AI开发助手完成，不是独立人工盲评。audit.py只核对证据一致性，不认证语义质量。该审计需要完整开发工作区含旧根ZIP；精简项目包应核对自己的DELIVERY.json，不宣称具有所有旧ZIP。

运行本轮只读审计：`python evaluations/final-polish-20261104/audit.py`（会写本目录audit.json；不会调用模型或修改历史记录）。
