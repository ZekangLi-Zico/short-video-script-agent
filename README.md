# 短视频脚本 Agent · 第4题

给定主题、受众、平台、目标时长和风格，生成有事实依据、可拍摄的分镜脚本；模型根据检索、估时及审核结果决定改稿、补查或结束。

**当前版本：v7.3.1-submission。** 保留v7.3的逐段动作、说话者、自然对白和网页预览；本次修复历史证据复算的版本兼容，新记录明确保存检索算法版本，验证报告默认另存，原始证据不覆盖。161项自动测试通过。

本轮四类网页真实模型验收符合要求：正常生成、超时后修订完成，无素材时请求资料，工具持续失败时明确停止。共18次模型响应、0次超时；当前4组及原始16组共20组证据复算通过。

**评审入口：** [当前四类真实网页验收](examples/current/evaluation.md) · [本轮修复与交付报告](evaluations/submission-v7.3.1-20261106/README.md) · [五分钟路线](docs/13-reviewer-and-practice-guide.md) · [提交清单](docs/06-submission.md)

**公开交付说明：** [发布说明与复现方法](PUBLICATION.md)。本仓库保留原Git历史、历次源码备份、测试输入/输出和Trace；公开日志中的个人电脑用户目录已脱敏，差异记录在`PUBLICATION-MANIFEST.json`。

原题产品案例使用虚构“剪影练习版”资料。另可选《城寨风云》前十二集编剧资料，包含32张资料卡、129条剧情与设定信息，用于片段和预告，见[资料说明](docs/18-story-materials.md)。创作模式新稿按“时间／动作与画面／对白与声音”展示并支持无对白动作，网页与下载一致；旧记录保留原格式。

历史结果单独保留：[v7自然旁白20次](docs/17-v7-natural-voice.md)、[v7.2调用故障修复](evaluations/call-fix-v7.2-20261106/README.md)、[v7.3动作与对白对照](evaluations/staging-v7.3-20261106/README.md)。这些不是本次v7.3.1的实验次数。需求、方案、评估、AI辅助与复盘见docs/01–05。

仓库为公开项目，当前提交版本以Git commit SHA为准，可运行`git rev-parse HEAD`获取。GitHub发布与笔试平台交卷是两个步骤；候选人实际投入时间仍须本人补充，具体见提交清单。旧报告保留当时的提交状态，最新交付入口以本页为准。

## 网页人工测试

Windows 双击根目录的 **`启动网页.cmd`**，或在 PowerShell 执行：

```powershell
.\run.ps1 -Mode web
```

浏览器打开 **http://127.0.0.1:8765/**。跨平台可用 `python -m src.web --open`；换端口用 `--port 8766`。

1. 填写主题、受众、平台、秒数和风格；选择“不超过目标秒数”或“接近目标（90%–100%）”。网页新任务默认场景创作，可切换严格引用；恢复旧历史会还原旧模式。
2. 选择“真实模型 · Codex”或“离线演练 · Mock”，点击“生成并检查”。
3. 在“脚本预览”按时间查看人物动作、镜头、说话者、台词与现场声，以及来源、估时和需求核对；在“执行过程”展开每步实际参数、返回结果和简短依据。需求核对是模型评估，仍需人工判断。
4. 在“连读旁白”通读完整讲述，运行完成后可下载旁白TXT、Markdown、Trace或JSON；最近运行可重新打开、修改输入后再试。

真实模型使用本机已登录 Codex 的额度。Mock 是固定桩，页面全程标注，不能证明模型决策。模型 API 只有在服务启动前配置环境变量才可选。

修改代码后需重启服务才能加载新版；已有服务占用端口时可改用新端口，不能把旧进程当作新版。

每次结果保存在 `outputs/web/<运行ID>/`。运行时即可下载检查点；刷新页面可重新接上当前服务的进行中任务。重启服务后恢复最近32条记录：已保存结果正常显示，已退出进程遗留的检查点恢复为未完成，不自动调用模型续跑，也不接管另一个存活进程的任务。“停止后续步骤”等待当前模型调用返回。网页只在本机监听，每个服务实例一次执行一个任务。

完整操作与逐项核对见 [网页人工测试指南](docs/07-web-manual-test.md)。选择“城寨风云”可写剧情片段与预告；选择“剪影练习版”继续原产品案例。漫剧资料来自已有改编文本，故事本身为虚构；本次只提供编剧文字资料，未接入视频、角色图片和配音。

## 运行环境与安装

- Python **3.11 或以上**。运行、测试均只使用标准库，`requirements.txt` 无第三方依赖。
- 在仓库根目录运行下列命令。不需要数据库、部署或视频生成服务；CLI 和网页共用核心代码。
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

自行安装可支持所选模型的 Codex CLI，并执行 `codex login`。程序依次寻找 `CODEX_BIN`、桌面环境提供的 `CODEX_APP_RUNTIME_CLI_PATH`、Windows 已安装 Codex 桌面应用的 CLI、PATH 中的 CLI。

```bash
python -m src.cli --provider codex --input examples/inputs/normal.json --output outputs/real
```

也可用 `.\run.ps1 -Mode live`。默认每进程 `CODEX_REASONING_EFFORT=medium`，可覆盖为low/medium/high/xhigh；不改全局Codex配置。`CODEX_MODEL` 留空则读取 CLI 配置的模型。v7.2 在使用内置服务且能解析模型时隔离个人 MCP 等无关配置，并显式保留模型和服务档位；自定义供应商或 profile 自动继承配置，也可设置 `CODEX_INHERIT_CONFIG=1`。真实记录的模型与配置模式见 Trace 和调用诊断。无需向项目复制登录凭证。

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
  "duration_mode": "target",
  "expression_mode": "creative",
  "style": "清楚、友好、克制",
  "product_id": "demo-editor"
}
```

`target_seconds` 为1–300秒。`duration_mode=max`表示上限；`target`表示90%–100%的预计时长区间。`expression_mode=creative`允许原创场景、标题、连接语，必须通过完整表面的独立语义审核；`strict`保留原批准列表。旧JSON缺省仍为strict/max。可传`initial_script`检查修订旧稿，结构见 [超时场景输入](examples/mock/over_duration/input.json)。

target模式由本地工具检查时长区间；模型审核检查是否重复事实或空镜拖时长。创作新稿为v3：每段取声音、屏幕阅读、展示停留、动作最低时长的较大值，再依次累加；无对白动作同样计时，说话者名字不计入朗读。v1/v2旧稿保持原算法。全部时长均为估算，不是实际配音或成片测量。

每次运行目录包含：

| 文件 | 内容 |
|---|---|
| `input.json` | 原始输入，包含旧稿时原样保留 |
| `output.json` | 状态、结构化可编辑脚本、估时、风险、来源 |
| `voice.txt`、`listening.json` | 连续旁白与逐镜提取；旧稿声画未知时明确标注，静音稿为空 |
| `script.md` | 人可读的分镜、旁白/字幕、镜头时长和引用 |
| `trace.jsonl` | 实际每一步的动作、参数、工具返回、简短依据与模型元数据 |
| `data_snapshot.json` | 本次使用的素材及品牌规则快照 |
| `manifest.json` | 应用与工具契约版本、运行时间、证据类型、数据哈希、步数上限、故障注入设置 |
| `checkpoint.json`、`run.json` | CLI/网页逐步落盘的最后检查点、运行标识和持有进程；检查点不是完成凭证 |
| `diagnostics/` | Codex每次调用的独立脱敏诊断，与Trace的call_id对应；不保存原始CLI输出或内部推理 |

`script.md` 便于人工编辑；需要程序复检时，将修改后的结构化稿件作为新输入的 `initial_script` 运行。程序不解析 Markdown 回写。

成功状态为 `completed`，CLI 退出码 0。`needs_input`、`blocked`、`step_limit`、`invalid_input` 的退出码为 2；这些状态可符合负向场景的预期，不能只看退出码判断验收。批量验收脚本在所有场景符合各自预期时返回 0。

## 验收与复现

首先复算当前提交件与历史示例，不调用远端模型：

```bash
python -m scripts.verify_evidence
python -m scripts.verify_evidence --group current
python -m scripts.verify_evidence --group historical
```

默认覆盖 `examples/current/`、`examples/mock/`、`examples/live/`，报告另存于 `outputs/evidence-audit/` 的时间戳文件。也可用 `--run <运行目录>` 多次指定，或 `--output <新报告路径>`。报告逐条列出应用版本、检索契约及选择依据；旧检索使用关键词算法，新检索保留ID优先。未知契约、被修改的结果或缺失文件会明确失败，不跳过后假装通过。此命令复算本地工具与证据一致性，不重新运行远端模型。

需要重新调用模型时：

```bash
python -m scripts.evaluate --provider codex --output outputs/evaluation-live
python -m scripts.evaluate --provider codex --output outputs/evaluation-live --case over_duration
python -m src.cli --provider mock --input examples/inputs/normal.json --fail-tool search_materials --fail-count -1 --output outputs/failure
```

共有正常、缺信息、无素材、持续工具失败、一次故障后恢复、超时修订、规则纠错、无法满足时长八个场景。按 `--case` 选部分运行时会合并该目录已有的验收索引，保留其他场景。

真实模型验收需要模型访问权限并消耗对应账号额度。模型输出具有随机性，新的运行可能采用不同路径或明确停止。

## 范围与取舍

- `data/materials.json`及品牌规则用于虚构产品“剪影练习版”，不代表小影或其他真实产品；`data/packs/city-drama/`来自已有漫剧改编文字，故事为虚构，来源与改编关系已注明。
- 新稿场景创作允许有来源的准确改写和翻译，原句与文案分别保存并做语义核对；严格模式与旧稿继续逐字引用。语义审核由模型判断，不能视为事实正确性的保证。
- 时长使用汉字/英文词/数字单位和镜头停留估算，不是 TTS 或成片实测。估算规则见 `docs/02-solution.md`。
- 默认最多 12 个动作步骤，可用 `--max-steps` 设置为 1–50；每次模型调用默认 180 秒，可用 `--timeout` 调整。需求核对动作会额外调用一次同后端模型，因而模型响应数可多于动作步数；Codex每次调用最多重试一次，整任务最多额外恢复两次超时、服务繁忙或流中断，每次尝试分别保存脱敏诊断。审核恢复失败就保存草稿并结束；默认最多12个决策步骤，每步至多决策与审核两次调用。
- 修改脚本会使旧检查失效。只有同一稿的来源/规则、时长、需求核对都通过，且核对绑定原请求，宿主才接受完成。需求核对使用同一后端的新上下文，不是独立模型认证，也不保证识别全部语义遗漏。
- 不生成图片、音频或视频，不接真实发布接口。

## 文件结构

```text
src/        模型决策循环、业务工具、真实模型接入、Mock、CLI、网页服务、报告
web/        本地网页表单、脚本预览与实际执行过程
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
