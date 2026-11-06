# Story Materials Implementation Plan

> For agentic workers: use superpowers:executing-plans to implement task by task.

**Goal:** 把已有《城寨风云》前十二集整理成可直接选择、阅读和用于短片创作的资料包。

**Architecture:** 原 ToolBox 默认资料不变；新增 catalog 按 product_id 选择独立资料及规则。writer/reviewer 根据宿主的 narrative 类型适配故事事实，保留现有循环。

**Tech Stack:** Python 标准库、原生 JavaScript、本地网页。

**Spec:** ../specs/2026-11-06-story-materials-design.md

## Constraints

- 保留 v7 与所有历史记录，外部漫剧文件只读。
- 新资料基于现有改编文本并保留来源，修订覆盖旧稿仅限对应内容。
- 不增加模型调用阶段，不扩大成视频制作系统。

## Tasks

- [x] 1. data/packs/city-drama：生成完整资料、来源快照、清晰的版本说明及 5 组创作需求。核对人物别名、分集顺序和第 8 集送饭修订。
- [x] 2. src/catalog.py、tools.py、providers.py、requirements.py、cli.py、web.py：接通独立资料与剧情语义，测试搜索和快照、CLI/web 一致性。
- [x] 3. web/index.html、app.js、style.css：可选项目、分类阅读、载入需求；旧历史恢复仍显示对应资料。
- [x] 4. 运行全部自动测试；网页真实模型验证，保留实际失败/修订；写交付说明与限制、校验历史未变。

执行结果：32张卡、129条信息、9份来源、5组需求；140项自动测试通过。2条真实网页运行均生成并通过内容检查，但收尾连续超时，最终blocked，未计作完整成功。12140个历史文件哈希不变；详见 evaluations/story-pack-20261106/README.md。未改原工程、未推送或交卷。

## Review Focus

- 后续修订是否真的覆盖旧稿，不向模型同时提供相反事实。
- 漫剧选择是否实际改变运行数据，而非仅更换页面标签。
- 原产品与无素材测试是否仍保持原行为。
- 人物对白能否自然创作，模型不会强行插入产品功能。
- 页面与记录是否准确区分改编文本、创作表达和未接入的成片资产。
