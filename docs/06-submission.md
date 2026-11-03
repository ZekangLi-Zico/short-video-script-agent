# 提交清单与答题框模板

## 当前交付

本仓库包含第 4 题代码、可执行测试、输入与实际输出、运行 Trace、合成数据、说明文档和环境配置示例。GitHub 远程仓库尚未创建/上传，当前环境的 `gh` 未登录；不要把本地路径当作 GitHub URL。

## 答题框模板

```text
选择题目：第 4 题——短视频脚本 Agent
GitHub URL：填写实际上传后的仓库地址
最终 commit SHA：填写 git rev-parse HEAD 输出的完整值

运行与评审入口：README.md
代码：src/
可执行测试：tests/；运行 python -m scripts.run_tests
真实模型运行记录：examples/live/
离线 Mock 示例：examples/mock/（仅验证流程）
测试及验收结果：examples/test-results/、examples/live/evaluation.md
需求、方案、评估、AI 使用与复盘：docs/01–05

实现说明：Python 标准库 CLI；真实模型根据检索、估时和规则检查结果选择后续动作。
支持资料不足、工具失败、超时修订和无依据宣传纠错，设置执行步数上限。
公开文案采用带来源的事实块和批准连接语；时长为文本估算。

AI 辅助内容、个人贡献及已知限制：见 docs/04-ai-usage.md、docs/03-evaluation.md。
实际执行时间：见 examples/work-session.json；个人额外投入请按实际情况填写。
```

## 上传步骤

以下为待用户执行或另行授权的上传步骤，本项目准备过程没有向 GitHub 推送，也没有提交考试页面。

```bash
gh auth login
gh repo create short-video-script-agent --private --source=. --remote=origin --push
git rev-parse HEAD
```

如果已经建立远程仓库，使用该仓库自己的地址配置 origin，再 push；不要重复创建同名仓库。私有仓库必须给题目指定评审账号读取权限，截图未给出具体评审账号。

## 最终核对

- 将全部材料放在同一个 GitHub 仓库中，确认 README 能打开。
- 确保提交的 commit SHA 与 GitHub 已推送的版本完全相同。
- 确认没有 `.env`、密钥、登录文件或隐私资料。
- 候选人实际阅读并复验后，如实补充个人改动与验证记录，不将 AI 编码记作个人手写。
- 题目提交按钮点击后不能修改；仓库、SHA 与评审权限确认后再交卷。
- ZIP 可作为页面附件补充，不能替代题目要求的 GitHub URL 和 commit SHA。
