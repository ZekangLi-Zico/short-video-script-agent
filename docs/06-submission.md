# 当前提交清单 · v7.3.1

当前工作区为 **v7.3.1-submission**。当前代码、文档、161项自动测试和四类网页真实模型证据分别从[README](../README.md)、[验收索引](../examples/current/evaluation.md)、[本轮报告](../evaluations/submission-v7.3.1-20261106/README.md)进入。历次版本和测试仍保留，根目录旧ZIP是历史快照。

公开目标仓库为 https://github.com/ZekangLi-Zico/short-video-script-agent 。当前提交以实际Git commit SHA为准，可运行`git rev-parse HEAD`获取。公开交付范围及日志脱敏见[发布说明](../PUBLICATION.md)。GitHub发布不等于笔试平台交卷。

## 评审可复现入口

```bash
python -m scripts.run_tests
python -m scripts.verify_evidence --group current
python -m scripts.verify_evidence --group historical
python -m src.web --open
```

前三项不调用模型。网页选择真实Codex需评审本机登录，或按README配置自己的模型API；提供Mock离线入口并明确其局限。无需向仓库提交或向别人发送凭证。

## 答题框模板

```text
选择题目：第4题——短视频脚本Agent
GitHub URL：https://github.com/ZekangLi-Zico/short-video-script-agent
最终commit SHA：填写本次推送核实的完整SHA（git rev-parse HEAD）

当前版本：v7.3.1-submission
本人实际投入：约4小时（根据聊天与人工测试记录事后估算，不含AI后台编码、自动测试和模型等待）
个人投入与贡献：docs/20-personal-contribution.md
运行与安装：README.md
当前四类真实模型验收：examples/current/evaluation.md
修复、实际结果与遗留事项：evaluations/submission-v7.3.1-20261106/README.md
需求、方案、评估、AI辅助、复盘：docs/01–05
本轮161项自动测试：evaluations/submission-v7.3.1-20261106/automated/

模型根据实际素材、估时和检查结果选择补查、改稿或结束；保留执行记录和来源。
页面按时间展示动作、说话者与对白，支持脚本下载。无资料或工具持续失败会说明未完成。
受控工具故障、离线Mock与真实模型响应分别标注。时长为脚本估算，未生成实际视频。
AI辅助与本人贡献如实披露；本人实际投入及复验情况见docs/04-ai-usage.md和docs/13-reviewer-and-practice-guide.md。
```

## 已确认的投入与交卷信息

候选人已确认个人实际投入约4小时，依据2026年11月3日至6日的聊天与人工测试记录事后估算。投入包括需求分析、人工试用、内容审阅、问题反馈、迭代决策和提交核对；不含AI后台编码、自动化测试、批量模型实验和模型调用等待。具体分工见[个人投入与贡献说明](20-personal-contribution.md)。后续如亲自追加复验，可另填[复验记录表](13-reviewer-and-practice-guide.md)，不把未做事项记成已完成。

仓库选择公开，无需单独邀请评审账号。提交署名使用已登录GitHub账号ZekangLi-Zico及GitHub的noreply邮箱。无需提供密码、API Key或登录令牌。

## 最后执行步骤

1. 个人投入与贡献说明已由本人确认，本次随提交文档同步。
2. 代码、文档、data、examples、历史证据与archives统一在本仓库；排除.runtime、登录文件、.env、缓存及根目录重复旧ZIP。原文件仍保留本地。
3. 核对将提交的文件和大小、密钥扫描及链接；在干净检出中执行上述离线命令。
4. 推送并核对远程文件后，在笔试平台填写题号、实际URL与完整SHA。

历次报告保留发生时的提交状态，当前发布状态以仓库及实际commit为准。笔试平台交卷由候选人完成。
