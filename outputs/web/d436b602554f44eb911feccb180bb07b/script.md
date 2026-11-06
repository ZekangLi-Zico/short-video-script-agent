# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已保留原标题及“门口—招牌—室内”三个分镜，仅介绍添加字幕。手动编辑和片段裁剪介绍已替换为简短场景引导，镜头停留调整为4、3、3秒。总时长估算10秒，符合20秒上限；三项检查均通过。

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

旁白/字幕：抬头看看招牌。

来源：

预计镜头时长：3.0 秒

### 分镜 3

画面：室内空桌椅

旁白/字幕：走进室内，看看桌椅。

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
  "script_hash": "04812a05b9f3d319824848497f059e254ac1a1108a4748f97544e950effaf5eb",
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
      "text": "抬头看看招牌。"
    },
    {
      "location": "shot:3/visual",
      "text": "室内空桌椅"
    },
    {
      "location": "shot:3/block:1",
      "text": "走进室内，看看桌椅。"
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
  "script_hash": "04812a05b9f3d319824848497f059e254ac1a1108a4748f97544e950effaf5eb",
  "request_hash": "b2bceab66dc6d75c3a021c080ed8cf62efe059b4115ad4c66f61e86afcaeaa8c",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "只介绍添加字幕",
      "verdict": "met",
      "evidence": "第1镜介绍“剪影练习版支持为视频添加字幕。”；第2、3镜仅引导观看民宿场景，全文未介绍其他产品功能。"
    },
    {
      "field": "topic",
      "requirement": "删除片段裁剪和手动编辑的介绍",
      "verdict": "met",
      "evidence": "片段裁剪删除项：旧稿第3镜“剪影练习版支持裁剪视频片段。”已删除，当前稿件未再介绍裁剪功能。"
    },
    {
      "field": "topic",
      "requirement": "删除片段裁剪和手动编辑的介绍",
      "verdict": "met",
      "evidence": "手动编辑删除项：旧稿第2镜“字幕文字可以手动编辑。”已删除，当前稿件未再介绍手动编辑功能。"
    },
    {
      "field": "topic",
      "requirement": "仍保留三个分镜",
      "verdict": "met",
      "evidence": "当前稿件共3个分镜，分别展示民宿门口、民宿招牌和室内空桌椅。"
    },
    {
      "field": "topic",
      "requirement": "“门口—招牌—室内”的顺序",
      "verdict": "met",
      "evidence": "第1镜“民宿门口”→第2镜“民宿招牌”→第3镜“室内空桌椅”，顺序一致。"
    },
    {
      "field": "audience",
      "requirement": "民宿运营协作伙伴",
      "verdict": "met",
      "evidence": "三个分镜均围绕民宿场景，第1镜用直接、易懂的语言说明添加字幕能力，适合向民宿运营协作伙伴传达。"
    },
    {
      "field": "platform",
      "requirement": "小红书",
      "verdict": "met",
      "evidence": "采用3个连续场景和简短旁白，宿主估算总长10秒，内容形式适合小红书短视频。"
    },
    {
      "field": "style",
      "requirement": "简洁",
      "verdict": "met",
      "evidence": "每镜仅一句文案，包括“抬头看看招牌。”“走进室内，看看桌椅。”，没有冗长解释。"
    },
    {
      "field": "style",
      "requirement": "不营销",
      "verdict": "met",
      "evidence": "第1镜仅陈述添加字幕能力，其余文案为场景引导；标题和正文均无夸张效果、促销或购买引导。"
    }
  ],
  "summary": "当前稿件满足要求：仅介绍添加字幕，已删除裁剪和手动编辑介绍，保留三个分镜及指定顺序。表达简洁、不营销，节奏合理。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "从门口到房间",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "标题描述空间行进路线，不包含产品能力或效果承诺。"
    },
    {
      "location": "shot:1/visual",
      "text": "民宿门口",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "第1镜为民宿外景拍摄安排，不包含产品声明。"
    },
    {
      "location": "shot:2/visual",
      "text": "民宿招牌",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "第2镜指定观察对象，不包含产品功能、界面或操作步骤。"
    },
    {
      "location": "shot:2/block:1",
      "text": "抬头看看招牌。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅引导观看招牌，不包含可验证的产品承诺。"
    },
    {
      "location": "shot:3/visual",
      "text": "室内空桌椅",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "第3镜描述室内陈设，不包含产品声明或真实客户背书。"
    },
    {
      "location": "shot:3/block:1",
      "text": "走进室内，看看桌椅。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅安排进入室内和观察桌椅的动作，不包含产品能力或效果承诺。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "宿主预计第1镜4秒，承载14个口播单位的字幕功能介绍；第2、3镜各3秒，分别承载6、8个口播单位，并安排观察招牌、进入室内看桌椅。各镜满足最低停留时间，画面任务明确，没有重复事实或明显过长的空镜停留。"
  },
  "expression_review_passed": true
}
```

## 执行路径

estimate_duration → check_rules → search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
