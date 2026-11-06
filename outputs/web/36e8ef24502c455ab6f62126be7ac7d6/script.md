# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成三镜头脚本，先大厅屏再手机，明确介绍横屏、竖屏两种可选画面比例。预计11秒，符合25秒上限；三项检查均通过。当前稿无需删改，未声称自动同步裁剪或自动追踪人物。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 横屏、竖屏：两种可选画面比例

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

画面：活动大厅实拍：横向大屏播放预先准备的活动画面。旁白字幕叠加在屏幕外，不展示软件界面。

旁白/字幕：活动视频，先看大厅屏。

来源：

预计镜头时长：3.0 秒

### 分镜 2

画面：硬切到手持手机的近景：手机竖向展示预先准备的活动画面，镜头保持稳定。

旁白/字幕：再看手机上的画面。

来源：

预计镜头时长：3.0 秒

### 分镜 3

画面：简洁背景上并列展示横向、竖向两个静态画框示意。事实块文字作为字幕显示，同时由旁白朗读。

旁白/字幕：剪影练习版提供横屏和竖屏画面比例选项。

来源：P03/P03.F1

预计镜头时长：5.0 秒

预计总时长：11.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "844f3c89cc152da14e3421d4c769ecc96893dfad9661b33ff88845913385223a",
  "passed": true,
  "issues": [],
  "citations": [
    {
      "location": "shot:3/block:1",
      "source_id": "P03",
      "fact_id": "P03.F1",
      "quote": "剪影练习版提供横屏和竖屏画面比例选项。",
      "version": "2026-11-01"
    }
  ],
  "rules_version": "2026-11-03-v1",
  "requires_expression_review": true,
  "expression_slots": [
    {
      "location": "title",
      "text": "横屏、竖屏：两种可选画面比例"
    },
    {
      "location": "shot:1/visual",
      "text": "活动大厅实拍：横向大屏播放预先准备的活动画面。旁白字幕叠加在屏幕外，不展示软件界面。"
    },
    {
      "location": "shot:1/block:1",
      "text": "活动视频，先看大厅屏。"
    },
    {
      "location": "shot:2/visual",
      "text": "硬切到手持手机的近景：手机竖向展示预先准备的活动画面，镜头保持稳定。"
    },
    {
      "location": "shot:2/block:1",
      "text": "再看手机上的画面。"
    },
    {
      "location": "shot:3/visual",
      "text": "简洁背景上并列展示横向、竖向两个静态画框示意。事实块文字作为字幕显示，同时由旁白朗读。"
    }
  ],
  "available_facts": [
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
  "script_hash": "844f3c89cc152da14e3421d4c769ecc96893dfad9661b33ff88845913385223a",
  "request_hash": "8f83e2cbcbb2dd70c13429381120bdf2dd261a226dda5f319aca191d2a7b49e6",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "介绍横屏、竖屏画面比例选项",
      "verdict": "met",
      "evidence": "镜头3旁白明确说明“剪影练习版提供横屏和竖屏画面比例选项”，画面并列展示两种画框。"
    },
    {
      "field": "topic",
      "requirement": "说明这是两种可选画面比例",
      "verdict": "met",
      "evidence": "标题“横屏、竖屏：两种可选画面比例”明确表达数量及可选关系。"
    },
    {
      "field": "topic",
      "requirement": "场景先大厅屏再手机",
      "verdict": "met",
      "evidence": "镜头1为活动大厅横向大屏，镜头2硬切到竖向展示活动画面的手机，顺序符合要求。"
    },
    {
      "field": "topic",
      "requirement": "不要声称自动同步裁剪或自动追踪人物。",
      "verdict": "met",
      "evidence": "针对自动同步裁剪：全部标题、画面及旁白均未声称该能力；大厅屏和手机展示的均明确为“预先准备的活动画面”。"
    },
    {
      "field": "topic",
      "requirement": "不要声称自动同步裁剪或自动追踪人物。",
      "verdict": "met",
      "evidence": "针对自动追踪人物：全部文案和画面安排均未出现人物追踪声明或演示；镜头2的“镜头保持稳定”属于拍摄安排。"
    },
    {
      "field": "audience",
      "requirement": "活动视频外包剪辑师",
      "verdict": "met",
      "evidence": "镜头1、2使用活动视频在大厅屏与手机上的展示场景，与活动视频剪辑师需要理解的画面比例选择相关。"
    },
    {
      "field": "platform",
      "requirement": "B站",
      "verdict": "met",
      "evidence": "采用明确标题、三镜头演示以及字幕配旁白的简短功能介绍形式，适合B站视频观看。"
    },
    {
      "field": "style",
      "requirement": "客观",
      "verdict": "met",
      "evidence": "镜头3仅陈述资料支持的比例选项，没有夸张效果、优越性或自动化承诺。"
    },
    {
      "field": "style",
      "requirement": "直截了当",
      "verdict": "met",
      "evidence": "标题直接点明两种比例；旁白依次为“先看大厅屏”“再看手机上的画面”和功能说明，没有无关铺垫。"
    }
  ],
  "summary": "当前稿件已落实两种比例介绍、大厅屏到手机的场景顺序，以及受众、平台和风格要求。未引入自动同步裁剪或人物追踪承诺，表达审核通过。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "横屏、竖屏：两种可选画面比例",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P03",
          "fact_id": "P03.F1"
        }
      ],
      "evidence": "P03.F1明确提供横屏和竖屏画面比例选项，支持标题中的两种可选比例表述。"
    },
    {
      "location": "shot:1/visual",
      "text": "活动大厅实拍：横向大屏播放预先准备的活动画面。旁白字幕叠加在屏幕外，不展示软件界面。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于大厅场景及字幕位置的拍摄安排；播放预先准备的画面，没有宣称软件投屏、自动适配或裁剪能力。"
    },
    {
      "location": "shot:1/block:1",
      "text": "活动视频，先看大厅屏。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "用于引入活动视频的大厅展示场景，不含产品能力或效果承诺。"
    },
    {
      "location": "shot:2/visual",
      "text": "硬切到手持手机的近景：手机竖向展示预先准备的活动画面，镜头保持稳定。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于手机展示及摄影安排；“预先准备”未暗示自动转换，“镜头保持稳定”未宣称产品防抖或追踪能力。"
    },
    {
      "location": "shot:2/block:1",
      "text": "再看手机上的画面。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于场景切换连接语，不含产品承诺。"
    },
    {
      "location": "shot:3/visual",
      "text": "简洁背景上并列展示横向、竖向两个静态画框示意。事实块文字作为字幕显示，同时由旁白朗读。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P03",
          "fact_id": "P03.F1"
        }
      ],
      "evidence": "两种画框及同步呈现的事实块均对应P03.F1支持的横屏、竖屏比例选项；未虚构软件按钮、界面布局或操作流程。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "镜头1、2的hold_seconds均为3，分别有大厅大屏、手机画面可供观察，并配有简短旁白。镜头3通过并列画框、字幕和朗读完成核心说明，hold_seconds为0，没有额外静态停留；未见重复事实或空镜凑时长。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
