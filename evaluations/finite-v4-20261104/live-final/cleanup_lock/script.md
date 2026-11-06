# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成三镜脚本，仅介绍添加字幕，以早餐摊主备料口播串联蒸笼、手写菜单、打包台，采用同事分享式短句，并明确避开顾客正脸。检查后无需删改。工具估算16.5秒，符合25秒上限；估算包含不朗读的事实卡文字，并非成片实测时长。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 早餐摊的备料口播，加上字幕

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

画面：蒸笼近景：只拍摊主双手将包子摆入蒸笼，不出现顾客正脸。摊主画外口播以下文字，同步叠加同文字幕，字幕不另行朗读。

旁白/字幕：今天备料，先把包子摆进蒸笼。

来源：

预计镜头时长：3.5 秒

### 分镜 2

画面：手写菜单特写：摊主写下今日供应的早餐，只拍手部与菜单，不出现顾客正脸。以下文字为摊主画外口播，同步叠加同文字幕。

旁白/字幕：再写好今日菜单。

来源：

预计镜头时长：3.0 秒

### 分镜 3

画面：打包台近景：摊主整理餐盒与纸袋，全程只拍手部和台面，不出现顾客正脸。第一块为摊主口播并同步显示字幕；第二块为同事分享式旁白；最后叠加第三块产品事实卡，事实卡不朗读。不展示软件按钮或操作界面。

旁白/字幕：餐盒、纸袋备齐，准备开摊。拍这种备料口播，试着加上字幕吧。剪影练习版支持为视频添加字幕。

来源：P01/P01.F1

预计镜头时长：10.0 秒

预计总时长：16.5 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "0db21f4ed3231c773a2536b787c501a8a2413c417c20f430737b78d4300db65f",
  "passed": true,
  "issues": [],
  "citations": [
    {
      "location": "shot:3/block:3",
      "source_id": "P01",
      "fact_id": "P01.F1",
      "quote": "剪影练习版支持为视频添加字幕。",
      "version": "2026-11-01"
    }
  ],
  "rules_version": "2026-11-03-v1",
  "requires_expression_review": true,
  "expression_slots": [
    {
      "location": "title",
      "text": "早餐摊的备料口播，加上字幕"
    },
    {
      "location": "shot:1/visual",
      "text": "蒸笼近景：只拍摊主双手将包子摆入蒸笼，不出现顾客正脸。摊主画外口播以下文字，同步叠加同文字幕，字幕不另行朗读。"
    },
    {
      "location": "shot:1/block:1",
      "text": "今天备料，先把包子摆进蒸笼。"
    },
    {
      "location": "shot:2/visual",
      "text": "手写菜单特写：摊主写下今日供应的早餐，只拍手部与菜单，不出现顾客正脸。以下文字为摊主画外口播，同步叠加同文字幕。"
    },
    {
      "location": "shot:2/block:1",
      "text": "再写好今日菜单。"
    },
    {
      "location": "shot:3/visual",
      "text": "打包台近景：摊主整理餐盒与纸袋，全程只拍手部和台面，不出现顾客正脸。第一块为摊主口播并同步显示字幕；第二块为同事分享式旁白；最后叠加第三块产品事实卡，事实卡不朗读。不展示软件按钮或操作界面。"
    },
    {
      "location": "shot:3/block:1",
      "text": "餐盒、纸袋备齐，准备开摊。"
    },
    {
      "location": "shot:3/block:2",
      "text": "拍这种备料口播，试着加上字幕吧。"
    }
  ],
  "available_facts": [
    {
      "source_id": "P01",
      "fact_id": "P01.F1",
      "quote": "剪影练习版支持为视频添加字幕。",
      "version": "2026-11-01"
    },
    {
      "source_id": "P01",
      "fact_id": "P01.F2",
      "quote": "字幕文字可以手动编辑。",
      "version": "2026-11-01"
    },
    {
      "source_id": "P02",
      "fact_id": "P02.F1",
      "quote": "剪影练习版支持裁剪视频片段。",
      "version": "2026-11-01"
    },
    {
      "source_id": "P03",
      "fact_id": "P03.F1",
      "quote": "剪影练习版提供横屏和竖屏画面比例选项。",
      "version": "2026-11-01"
    }
  ],
  "scope": "exact_quote_and_brand_checks_only; expression semantics require independent model review"
}
```

## 需求覆盖核对

以下为模型评估，可能漏判或误判，仍需人工确认。

```json
{
  "ok": true,
  "script_hash": "0db21f4ed3231c773a2536b787c501a8a2413c417c20f430737b78d4300db65f",
  "request_hash": "4299792130470435332510610b8526e5f391e330ac68588a7ba5d1498ead5ad2",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "做一条剪影练习版字幕功能介绍",
      "verdict": "met",
      "evidence": "镜头3第3块明确介绍“剪影练习版支持为视频添加字幕。”，前两镜展示口播配字幕的使用方式。"
    },
    {
      "field": "topic",
      "requirement": "背景是早餐摊主讲今日备料",
      "verdict": "met",
      "evidence": "镜头1安排摊主画外口播“今天备料，先把包子摆进蒸笼。”；后续展示写今日菜单、整理餐盒与纸袋，具体体现早餐摊备料场景。"
    },
    {
      "field": "topic",
      "requirement": "只介绍添加字幕",
      "verdict": "met",
      "evidence": "产品内容仅包含口播叠加字幕、建议加字幕和支持添加字幕的事实卡；未介绍手动编辑字幕、裁剪视频或画面比例等其他功能。写菜单、整理餐盒属于场景动作。"
    },
    {
      "field": "topic",
      "requirement": "画面按蒸笼、手写菜单、打包台的顺序",
      "verdict": "met",
      "evidence": "镜头1为“蒸笼近景”，镜头2为“手写菜单特写”，镜头3为“打包台近景”，顺序一致。"
    },
    {
      "field": "topic",
      "requirement": "不要出现顾客正脸",
      "verdict": "met",
      "evidence": "三个镜头均明确“不出现顾客正脸”，取景分别限定为摊主双手、手部与菜单、手部和台面。"
    },
    {
      "field": "audience",
      "requirement": "小店新媒体兼职",
      "verdict": "met",
      "evidence": "用小店备料口播演示字幕用途，镜头简单、文案通俗，并以“拍这种备料口播，试着加上字幕吧。”给出易理解的建议。"
    },
    {
      "field": "platform",
      "requirement": "抖音",
      "verdict": "met",
      "evidence": "采用三个连续场景特写、简短口播和同步字幕，适合短视频浏览；宿主估算总长16.5秒，符合本次25秒上限。"
    },
    {
      "field": "style",
      "requirement": "像同事分享经验",
      "verdict": "met",
      "evidence": "镜头3以“拍这种备料口播，试着加上字幕吧。”进行自然建议，语气接近日常同事交流。"
    },
    {
      "field": "style",
      "requirement": "短句",
      "verdict": "met",
      "evidence": "口播使用“再写好今日菜单。”“餐盒、纸袋备齐，准备开摊。”等短句，产品事实卡也为单句。"
    }
  ],
  "summary": "全部明确需求已落实：早餐摊备料场景具体，镜头顺序正确，避开顾客正脸，功能介绍仅限添加字幕。表达没有额外产品承诺，预计节奏合理。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "早餐摊的备料口播，加上字幕",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "标题交代场景和添加字幕的行动主题，没有提出性能、效果或自动化承诺。"
    },
    {
      "location": "shot:1/visual",
      "text": "蒸笼近景：只拍摊主双手将包子摆入蒸笼，不出现顾客正脸。摊主画外口播以下文字，同步叠加同文字幕，字幕不另行朗读。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "描述取景、摆包子动作及口播字幕的剪辑安排；“同步叠加同文字幕”未声称产品自动识别或自动同步。"
    },
    {
      "location": "shot:1/block:1",
      "text": "今天备料，先把包子摆进蒸笼。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于摊主备料的情境台词，不涉及产品能力或效果。"
    },
    {
      "location": "shot:2/visual",
      "text": "手写菜单特写：摊主写下今日供应的早餐，只拍手部与菜单，不出现顾客正脸。以下文字为摊主画外口播，同步叠加同文字幕。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于菜单书写、取景及字幕呈现安排，没有虚构软件界面、按钮或自动工作流程。"
    },
    {
      "location": "shot:2/block:1",
      "text": "再写好今日菜单。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "描述备料场景中的下一步动作，不含产品声明。"
    },
    {
      "location": "shot:3/visual",
      "text": "打包台近景：摊主整理餐盒与纸袋，全程只拍手部和台面，不出现顾客正脸。第一块为摊主口播并同步显示字幕；第二块为同事分享式旁白；最后叠加第三块产品事实卡，事实卡不朗读。不展示软件按钮或操作界面。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "全文安排场景动作、配音分工和事实卡展示方式，未额外宣称产品能力，也未构造具体操作界面。"
    },
    {
      "location": "shot:3/block:1",
      "text": "餐盒、纸袋备齐，准备开摊。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于早餐摊准备工作的情境台词，不含产品承诺。"
    },
    {
      "location": "shot:3/block:2",
      "text": "拍这种备料口播，试着加上字幕吧。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于添加字幕的行动建议，没有承诺传播效果、效率提升或自动化能力。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "镜头1预计3.5秒，支撑摆包子动作及一句口播；镜头2预计3秒，支撑菜单特写、写字动作和短句口播；镜头3预计10秒，包含整理包装用品、两段简短口播及最后不朗读的事实卡，停留有具体内容支撑。各镜均满足3秒最低展示时间，未见重复事实或空镜凑时长。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
