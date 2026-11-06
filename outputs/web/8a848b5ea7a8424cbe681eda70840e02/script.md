# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成早餐备料场景的三镜头脚本，仅介绍添加字幕，按蒸笼→手写菜单→打包台展开，明确避开顾客正脸，采用同事分享式短句。当前稿无需删改。估算16.3秒，符合25秒上限；实际时长以成片为准。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 早餐备料口播，加个字幕

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

画面：蒸笼近景，摊主的手将包子摆入蒸屉。摊主画外音讲今日备料，旁白原文作为添加字幕的成片示例叠加。只拍蒸笼与手部，不出现顾客正脸。

旁白/字幕：今天的包子，先上蒸笼。

来源：

预计镜头时长：5.0 秒

### 分镜 2

画面：镜头转到手写菜单，摊主的手指过早餐品名。以同事分享经验的语气读出产品事实，同时显示同文事实卡；事实卡与摊主口播字幕采用不同样式，不展示操作界面。画面仅包含菜单和手部，不出现顾客正脸。

旁白/字幕：剪影练习版支持为视频添加字幕。

来源：P01/P01.F1

预计镜头时长：5.0 秒

### 分镜 3

画面：镜头转到打包台，摊主双手将打包袋摆齐。先播放摊主备料旁白，并叠加对应的示例字幕；随后由介绍者说出结尾建议。仅拍台面与手部，不出现顾客正脸。

旁白/字幕：打包袋也备好了，准备开摊。拍备料口播，试着加上字幕吧。

来源：

预计镜头时长：6.3 秒

预计总时长：16.3 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "08901d795f7b572a7f32506ff1ba0a670086e34c2cfbb84d713c793a039c9a4b",
  "passed": true,
  "issues": [],
  "citations": [
    {
      "location": "shot:2/block:1",
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
      "text": "早餐备料口播，加个字幕"
    },
    {
      "location": "shot:1/visual",
      "text": "蒸笼近景，摊主的手将包子摆入蒸屉。摊主画外音讲今日备料，旁白原文作为添加字幕的成片示例叠加。只拍蒸笼与手部，不出现顾客正脸。"
    },
    {
      "location": "shot:1/block:1",
      "text": "今天的包子，先上蒸笼。"
    },
    {
      "location": "shot:2/visual",
      "text": "镜头转到手写菜单，摊主的手指过早餐品名。以同事分享经验的语气读出产品事实，同时显示同文事实卡；事实卡与摊主口播字幕采用不同样式，不展示操作界面。画面仅包含菜单和手部，不出现顾客正脸。"
    },
    {
      "location": "shot:3/visual",
      "text": "镜头转到打包台，摊主双手将打包袋摆齐。先播放摊主备料旁白，并叠加对应的示例字幕；随后由介绍者说出结尾建议。仅拍台面与手部，不出现顾客正脸。"
    },
    {
      "location": "shot:3/block:1",
      "text": "打包袋也备好了，准备开摊。"
    },
    {
      "location": "shot:3/block:2",
      "text": "拍备料口播，试着加上字幕吧。"
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
  "script_hash": "08901d795f7b572a7f32506ff1ba0a670086e34c2cfbb84d713c793a039c9a4b",
  "request_hash": "4299792130470435332510610b8526e5f391e330ac68588a7ba5d1498ead5ad2",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "做一条剪影练习版字幕功能介绍",
      "verdict": "met",
      "evidence": "第2镜头明确介绍“剪影练习版支持为视频添加字幕。”，第1、3镜头展示字幕成片示例。"
    },
    {
      "field": "topic",
      "requirement": "背景是早餐摊主讲今日备料",
      "verdict": "met",
      "evidence": "第1镜头安排摊主讲今日备料，旁白为“今天的包子，先上蒸笼。”；第3镜头补充“打包袋也备好了，准备开摊。”"
    },
    {
      "field": "topic",
      "requirement": "只介绍添加字幕",
      "verdict": "met",
      "evidence": "第2镜头仅介绍添加字幕，第1、3镜头仅展示字幕示例；全文未介绍手动编辑字幕、裁剪视频或画面比例等其他功能。事实卡与字幕采用不同样式属于拍摄排版安排，未宣称产品提供样式功能。"
    },
    {
      "field": "topic",
      "requirement": "画面按蒸笼、手写菜单、打包台的顺序",
      "verdict": "met",
      "evidence": "第1镜头为“蒸笼近景”，第2镜头“转到手写菜单”，第3镜头“转到打包台”，顺序一致。"
    },
    {
      "field": "topic",
      "requirement": "不要出现顾客正脸",
      "verdict": "met",
      "evidence": "三个镜头均明确“不出现顾客正脸”，取景分别限定为蒸笼与手部、菜单和手部、台面与手部。"
    },
    {
      "field": "audience",
      "requirement": "小店新媒体兼职",
      "verdict": "met",
      "evidence": "以早餐摊备料口播为实例，用“拍备料口播，试着加上字幕吧。”给出易理解的拍摄建议，适合小店兼职内容制作场景。"
    },
    {
      "field": "platform",
      "requirement": "抖音",
      "verdict": "met",
      "evidence": "三个镜头围绕同一早餐摊场景展开，配合短旁白和字幕示例，内容集中，适合短视频观看。"
    },
    {
      "field": "style",
      "requirement": "像同事分享经验",
      "verdict": "met",
      "evidence": "第2镜头明确采用“同事分享经验的语气”，结尾“试着加上字幕吧”也是日常建议口吻。"
    },
    {
      "field": "style",
      "requirement": "短句",
      "verdict": "met",
      "evidence": "各段均为简短单句，如“今天的包子，先上蒸笼。”和“打包袋也备好了，准备开摊。”，无长篇解释。"
    }
  ],
  "summary": "稿件满足全部明确需求：以早餐摊主讲今日备料为背景，只介绍添加字幕，画面顺序正确，并明确避开顾客正脸。表达有资料支持，镜头停留安排合理。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "早餐备料口播，加个字幕",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "标题点明使用场景并提出添加字幕的建议，没有承诺额外能力或效果。"
    },
    {
      "location": "shot:1/visual",
      "text": "蒸笼近景，摊主的手将包子摆入蒸屉。摊主画外音讲今日备料，旁白原文作为添加字幕的成片示例叠加。只拍蒸笼与手部，不出现顾客正脸。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "“添加字幕的成片示例叠加”展示的能力由P01.F1支持；未声称自动识别旁白。蒸笼、手部与画外音属于拍摄安排。"
    },
    {
      "location": "shot:1/block:1",
      "text": "今天的包子，先上蒸笼。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于早餐备料场景旁白，不涉及产品能力或效果承诺。"
    },
    {
      "location": "shot:2/visual",
      "text": "镜头转到手写菜单，摊主的手指过早餐品名。以同事分享经验的语气读出产品事实，同时显示同文事实卡；事实卡与摊主口播字幕采用不同样式，不展示操作界面。画面仅包含菜单和手部，不出现顾客正脸。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "规定取景、语气和事实卡排版，本项未新增产品声明。“不同样式”是成片视觉安排，没有宣称产品具备样式设置能力；配套口播事实已由rules_check单独核对。"
    },
    {
      "location": "shot:3/visual",
      "text": "镜头转到打包台，摊主双手将打包袋摆齐。先播放摊主备料旁白，并叠加对应的示例字幕；随后由介绍者说出结尾建议。仅拍台面与手部，不出现顾客正脸。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "“叠加对应的示例字幕”仅展示P01.F1支持的添加字幕能力；没有虚构操作界面、按钮或自动工作流，其余内容为拍摄安排。"
    },
    {
      "location": "shot:3/block:1",
      "text": "打包袋也备好了，准备开摊。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于摊主备料场景旁白，不涉及产品声明。"
    },
    {
      "location": "shot:3/block:2",
      "text": "拍备料口播，试着加上字幕吧。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于行动建议，没有承诺字幕带来的流量、效率或其他效果。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "第1镜头5秒，包含摆包子动作、短旁白和字幕阅读；第2镜头5秒，包含指菜单动作及一句功能事实的听读；第3镜头6秒，包含摆齐打包袋、两句短旁白与示例字幕。各镜头均有明确动作或阅读内容支撑，字幕示例结合不同备料内容展开，没有明显空镜或重复事实凑时长。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
