# 短视频脚本 Agent · 第 4 题

给定主题、受众、平台、目标时长和风格，模型检索合成产品资料，编排有来源的分镜脚本，调用时长与规则检查，再根据实际观察修订或说明无法完成。

**评审入口：** [需求与验收映射](docs/01-requirements.md) · [方案与动态决策](docs/02-solution.md) · [实际验证](docs/03-evaluation.md) · [AI 使用说明](docs/04-ai-usage.md) · [复盘](docs/05-retrospective.md)

已保存的验证结果：**45 项自动测试通过，8/8 离线验收、8/8 真实后端场景符合预期**。其中缺信息场景由宿主校验，其余 7 类场景含真实模型响应。可直接阅读 [27 秒正常脚本](examples/live/normal/script.md)、[38 秒修订为 25 秒的执行记录](examples/live/over_duration/trace.jsonl) 和 [持续工具失败的停止记录](examples/live/tool_failure/trace.jsonl)。

## 运行环境与安装

- Python **3.11 或以上**。运行、测试均只使用标准库，`requirements.txt` 无第三方依赖。
- 在仓库根目录运行下列命令。不要求界面、数据库、部署或视频生成服务。
- 真实模型可选已登录的 Codex CLI，或者支持结构化 JSON 输出的模型 API。

```bash
python --version
python -m pip install -r requirements.txt
```

第二条为空依赖安装，可跳过。Windows 若 `python` 指向不可用的商店别名，可用已安装的 `py -3` 替换；本地也提供 `run.ps1`，自动寻找虚拟环境、Codex 附带 Python 或 PATH 中的 Python。

## 先离线验证

```bash
python -m src.cli --provider mock --input examples/inputs/normal.json --output outputs/demo
python -m scripts.run_tests
python -m scripts.evaluate --provider mock --output outputs/evaluation-mock
python -m scripts.verify_evidence
```

Windows 便捷入口：

```powershell
.\run.ps1 -Mode demo
.\run.ps1 -Mode test
.\run.ps1 -Mode evaluate
```

**Mock 是固定离线决策桩，只验证宿主流程、工具与异常处理，不证明真实模型的决策效果。** 不会在真模型失败时偷偷切换 Mock。每次运行必须显式指定 `--provider`，产物也标记证据类型。

## 真实模型入口 A：Codex CLI

自行安装可支持所选模型的 Codex CLI，并执行 `codex login`。程序优先使用 `CODEX_BIN`，其次 Codex 桌面环境提供的 `CODEX_APP_RUNTIME_CLI_PATH`，最后 PATH 中的 CLI。

```bash
python -m src.cli --provider codex --input examples/inputs/normal.json --output outputs/real
```

也可用 `.\run.ps1 -Mode live`。`CODEX_MODEL` 留空则使用 CLI 配置的模型；本仓库保存的真实记录使用的模型见各 Trace 的 `model.model` 字段。无需向项目复制登录凭证。

适配器把当前状态和工具结果作为输入，通过 `codex exec --ephemeral --sandbox read-only --output-schema` 获取一次结构化动作。业务工具由本项目执行。适配器不会保留 CLI 内部推理文本；如发现 CLI 调用额外 shell/MCP 等工具则拒绝该次结果。

## 真实模型入口 B：模型 API

`.env.example` 列出变量；**程序不会自动加载 `.env` 文件**。用终端环境变量设置，不能提交真实密钥。

```powershell
$env:MODEL_API_KEY = '<你的密钥>'
$env:MODEL_NAME = '<账号可用且支持结构化输出的模型名>'
$env:MODEL_BASE_URL = 'https://api.openai.com/v1'
$env:MODEL_API_STYLE = 'responses'
python -m src.cli --provider api --input examples/inputs/normal.json --output outputs/api
```

支持兼容接口时可将 `MODEL_API_STYLE` 设为 `chat`，调用 `/chat/completions`；默认调用 `/responses`。不同服务的模型与结构化输出支持并不相同。HTTP 401、超时和非法响应都返回明确失败，不提供虚构的成功结果。**API 适配器有契约测试，本次未用真实 API Key 联调。**

## 输入与输出

```json
{
  "topic": "介绍字幕功能",
  "audience": "第一次制作口播短视频的创作者",
  "platform": "抖音",
  "target_seconds": 30,
  "style": "清楚、友好、克制",
  "product_id": "demo-editor"
}
```

`target_seconds` 在本项目中解释为 **时长上限**，不强制填满；1–300 秒。可以额外传入 `initial_script` 作为待检查修订的旧稿，结构见 [超时场景输入](examples/mock/over_duration/input.json)。

在不违反上限的前提下，提示模型尽量安排接近目标的节奏（建议 80%–100%，不是硬性下限）。旧版较短脚本保留于 `examples/iterations/before_pacing/`，用于说明这个质量改进。

每次运行目录包含：

| 文件 | 内容 |
|---|---|
| `input.json` | 原始输入，包含旧稿时原样保留 |
| `output.json` | 状态、结构化可编辑脚本、估时、风险、来源 |
| `script.md` | 人可读的分镜、旁白/字幕、镜头时长和引用 |
| `trace.jsonl` | 实际每一步的动作、参数、工具返回、简短依据与模型元数据 |
| `data_snapshot.json` | 本次使用的素材及品牌规则快照 |
| `manifest.json` | 运行时间、证据类型、数据哈希、步数上限、故障注入设置 |

`script.md` 便于人工编辑；需要程序复检时，将修改后的结构化稿件作为新输入的 `initial_script` 运行。程序不解析 Markdown 回写。

成功状态为 `completed`，CLI 退出码 0。`needs_input`、`blocked`、`step_limit`、`invalid_input` 的退出码为 2；这些状态可符合负向场景的预期，不能只看退出码判断验收。批量验收脚本在所有场景符合各自预期时返回 0。

## 验收与复现

```bash
python -m scripts.evaluate --provider codex --output outputs/evaluation-live
python -m scripts.evaluate --provider codex --output outputs/evaluation-live --case over_duration
python -m src.cli --provider mock --input examples/inputs/normal.json --fail-tool search_materials --fail-count -1 --output outputs/failure
```

共有正常、缺信息、无素材、持续工具失败、一次故障后恢复、超时修订、规则纠错、无法满足时长八个场景。按 `--case` 选部分运行时会合并该目录已有的验收索引，保留其他场景。

真实模型验收需要模型访问权限并消耗对应账号额度。模型输出具有随机性，新的运行可能采用不同路径或明确停止。

## 范围与取舍

- `data/` 全部是合成资料，虚构产品“剪影练习版”的功能不代表小影或其他真实产品。
- 为机械验证事实，公开文案使用逐字引用的事实块及品牌批准的连接语，标题和镜头指令也有允许表。模型选择、组合、排序与修订；这不是无限制创意写作，也不是通用语义事实验证器。
- 时长使用汉字/英文词/数字单位和镜头停留估算，不是 TTS 或成片实测。估算规则见 `docs/02-solution.md`。
- 默认最多 12 步，可用 `--max-steps` 设置为 1–50；每次模型调用默认 180 秒，可用 `--timeout` 调整。
- 修改脚本会使旧检查失效。只有同一稿的来源/规则检查和时长检查均通过，宿主才接受完成。
- 不生成图片、音频或视频，不接真实发布接口。

## 文件结构

```text
src/        模型决策循环、业务工具、真实模型接入、Mock、CLI、报告
tests/      单元、集成、适配器契约与反例测试
scripts/    批量验收及测试证据生成
examples/   输入、实际输出、执行记录、测试与验收结果
data/       合成素材与品牌规则
docs/       需求、方案、评估、AI 使用说明、复盘、提交清单
```

提交前按 [提交清单](docs/06-submission.md) 填写题号、GitHub URL 与最终 commit SHA。

## 接口参考

- [Codex 非交互运行](https://developers.openai.com/codex/noninteractive/)
- [结构化模型输出](https://developers.openai.com/api/docs/guides/structured-outputs)

本项目使用模型生成 JSON 动作再由宿主分派，不依赖某个 Agent 框架；API 适配器使用上述结构化输出协议。
