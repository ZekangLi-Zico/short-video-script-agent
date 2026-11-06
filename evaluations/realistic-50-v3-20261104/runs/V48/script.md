# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已保留原标题及“门口—招牌—室内”三个分镜，仅介绍添加字幕；手动编辑和片段裁剪介绍已替换为对应场景的字幕示例。镜头停留由各8秒调整为4、3、3秒，估算总时长10秒，符合20秒上限，全部检查通过。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 从门口到房间

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

画面：民宿门口

旁白/字幕：剪影练习版支持为视频添加字幕。

来源：P01/P01.F1

预计镜头时长：4.0 秒

### 分镜 2

画面：民宿招牌

旁白/字幕：字幕示例：民宿招牌。

来源：

预计镜头时长：3.0 秒

### 分镜 3

画面：室内空桌椅

旁白/字幕：字幕示例：室内一角。

来源：

预计镜头时长：3.0 秒

## 实际修订

位置按镜头索引比较；日志关联的是实际反馈，不证明模型因果推理。

- 修改：shot:1/hold_seconds, shot:2/hold_seconds, shot:2/block:1, shot:3/hold_seconds, shot:3/block:1；保留原镜头 0 个、原文案块 1 个。
- 修订前失败检查：duration, rules_check

预计总时长：10.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "5c481c9861854575cb7a5b6d7ba1b0e7142ade2f8d8a3b95d1964f505303826f",
  "passed": true,
  "issues": [],
  "citations": [
    {
      "location": "shot:1/block:1",
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
      "text": "从门口到房间"
    },
    {
      "location": "shot:1/visual",
      "text": "民宿门口"
    },
    {
      "location": "shot:2/visual",
      "text": "民宿招牌"
    },
    {
      "location": "shot:2/block:1",
      "text": "字幕示例：民宿招牌。"
    },
    {
      "location": "shot:3/visual",
      "text": "室内空桌椅"
    },
    {
      "location": "shot:3/block:1",
      "text": "字幕示例：室内一角。"
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
  "script_hash": "5c481c9861854575cb7a5b6d7ba1b0e7142ade2f8d8a3b95d1964f505303826f",
  "request_hash": "b2bceab66dc6d75c3a021c080ed8cf62efe059b4115ad4c66f61e86afcaeaa8c",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "只介绍添加字幕",
      "verdict": "met",
      "evidence": "第1镜头介绍“支持为视频添加字幕”；第2、3镜头仅提供字幕内容示例。未介绍裁剪、手动编辑或画面比例等其他功能。"
    },
    {
      "field": "topic",
      "requirement": "删除片段裁剪和手动编辑的介绍",
      "verdict": "met",
      "evidence": "针对片段裁剪：旧稿第3镜头的“剪影练习版支持裁剪视频片段。”已删除，当前改为“字幕示例：室内一角。”，其他位置也未介绍裁剪。"
    },
    {
      "field": "topic",
      "requirement": "删除片段裁剪和手动编辑的介绍",
      "verdict": "met",
      "evidence": "针对手动编辑：旧稿第2镜头的“字幕文字可以手动编辑。”已删除，当前改为“字幕示例：民宿招牌。”，其他位置也未介绍手动编辑。"
    },
    {
      "field": "topic",
      "requirement": "仍保留三个分镜",
      "verdict": "met",
      "evidence": "当前稿恰有三个分镜，分别呈现民宿门口、民宿招牌和室内空桌椅。"
    },
    {
      "field": "topic",
      "requirement": "“门口—招牌—室内”的顺序",
      "verdict": "met",
      "evidence": "第1镜头“民宿门口”→第2镜头“民宿招牌”→第3镜头“室内空桌椅”，顺序一致。"
    },
    {
      "field": "audience",
      "requirement": "民宿运营协作伙伴",
      "verdict": "met",
      "evidence": "三个镜头均使用民宿场景，字幕示例直接对应招牌及室内空间，适合协作伙伴理解民宿视频的字幕应用。"
    },
    {
      "field": "platform",
      "requirement": "小红书",
      "verdict": "met",
      "evidence": "标题“从门口到房间”明确，三个生活场景配合简短字幕，适合小红书短视频呈现。"
    },
    {
      "field": "style",
      "requirement": "简洁",
      "verdict": "met",
      "evidence": "每个镜头仅一条短文案，依次说明添加字幕能力、展示招牌字幕、展示室内字幕，没有冗长解释。"
    },
    {
      "field": "style",
      "requirement": "不营销",
      "verdict": "met",
      "evidence": "全文采用功能说明和场景示例，没有夸张效果、优惠宣传、购买引导或营销式结尾。"
    }
  ],
  "summary": "当前稿符合要求：仅介绍添加字幕，已删除裁剪和手动编辑介绍，保留三个分镜及指定顺序。受众、平台、风格和镜头节奏均适配。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "从门口到房间",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "标题描述空间游览路线，不包含产品能力或效果承诺。"
    },
    {
      "location": "shot:1/visual",
      "text": "民宿门口",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅指定民宿门口这一拍摄场景，不涉及产品声明。"
    },
    {
      "location": "shot:2/visual",
      "text": "民宿招牌",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅指定招牌画面，没有产品操作、界面或效果声明。"
    },
    {
      "location": "shot:2/block:1",
      "text": "字幕示例：民宿招牌。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅提供对应招牌画面的示例字幕内容，未声称自动识别、自动生成或手动编辑等能力。"
    },
    {
      "location": "shot:3/visual",
      "text": "室内空桌椅",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅描述室内拍摄对象，不包含产品承诺。"
    },
    {
      "location": "shot:3/block:1",
      "text": "字幕示例：室内一角。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅提供室内画面的示例字幕内容，没有额外能力、操作流程或效果声明。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "第1镜头4秒承载“剪影练习版支持为视频添加字幕。”及门口画面，长度合理；第2镜头3秒用于阅读“字幕示例：民宿招牌。”并观察招牌；第3镜头3秒用于阅读“字幕示例：室内一角。”并观察桌椅。各镜头均有具体阅读或观察内容，没有明显重复事实或空镜凑时长。"
  },
  "expression_review_passed": true
}
```

## 执行路径

estimate_duration → check_rules → search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
