# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：脚本已完成：保留原标题及“门口—招牌—室内”三个分镜，只介绍添加字幕；手动编辑和片段裁剪介绍已替换为场景字幕。镜头停留调整为4、3、3秒，估时10秒，符合20秒上限。三项检查均通过，实际字幕阅读节奏需在剪辑时核对。

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

旁白/字幕：先看看招牌。

来源：

预计镜头时长：3.0 秒

### 分镜 3

画面：室内空桌椅

旁白/字幕：再看看室内。

来源：

预计镜头时长：3.0 秒

## 审稿备注（不进入视频，不计入时长）

供创作者核对修改与资料缺口，不是经过事实认证的产品介绍。

保留原标题、三个分镜画面及门口—招牌—室内顺序，保留首镜添加字幕事实。按用户限定范围删除手动编辑和片段裁剪介绍，后两镜替换为场景字幕示例。首镜事实作旁白，后两镜文字仅作为屏幕字幕。各镜最短停留由8秒调整为4、3、3秒。估时工具仍会串行计算所有文字，屏幕字幕的实际阅读时间需在剪辑时核对。

## 实际修订

位置按镜头索引比较；日志关联的是实际反馈，不证明模型因果推理。

- 修改：editor_notes, shot:1/hold_seconds, shot:2/hold_seconds, shot:2/block:1, shot:3/hold_seconds, shot:3/block:1；保留原镜头 0 个、原文案块 1 个。
- 修订前失败检查：duration, rules_check

预计总时长：10.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "ab35c841c1a6bd7cc156d9a20d2fef7fe06fb82977de50c356d993ecb79e9af8",
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
      "text": "先看看招牌。"
    },
    {
      "location": "shot:3/visual",
      "text": "室内空桌椅"
    },
    {
      "location": "shot:3/block:1",
      "text": "再看看室内。"
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
  "script_hash": "ab35c841c1a6bd7cc156d9a20d2fef7fe06fb82977de50c356d993ecb79e9af8",
  "request_hash": "b2bceab66dc6d75c3a021c080ed8cf62efe059b4115ad4c66f61e86afcaeaa8c",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "添加字幕",
      "verdict": "met",
      "evidence": "第1镜明确介绍“剪影练习版支持为视频添加字幕。”；第2、3镜的短句按editor_notes安排为屏幕字幕示例。"
    },
    {
      "field": "topic",
      "requirement": "只介绍添加字幕",
      "verdict": "met",
      "evidence": "全稿介绍的产品功能只有第1镜的添加字幕；后两镜“先看看招牌。”“再看看室内。”为场景文字，没有介绍其他产品功能。"
    },
    {
      "field": "topic",
      "requirement": "删除片段裁剪和手动编辑的介绍。",
      "verdict": "met",
      "evidence": "片段裁剪已删除：旧稿第3镜“剪影练习版支持裁剪视频片段。”已替换为“再看看室内。”，当前观众可见内容中没有裁剪介绍。"
    },
    {
      "field": "topic",
      "requirement": "删除片段裁剪和手动编辑的介绍。",
      "verdict": "met",
      "evidence": "手动编辑已删除：旧稿第2镜“字幕文字可以手动编辑。”已替换为“先看看招牌。”，当前观众可见内容中没有手动编辑介绍。"
    },
    {
      "field": "topic",
      "requirement": "仍保留三个分镜",
      "verdict": "met",
      "evidence": "当前稿件共3个分镜，分别为“民宿门口”“民宿招牌”“室内空桌椅”。"
    },
    {
      "field": "topic",
      "requirement": "“门口—招牌—室内”的顺序",
      "verdict": "met",
      "evidence": "第1镜“民宿门口”、第2镜“民宿招牌”、第3镜“室内空桌椅”，顺序一致。"
    },
    {
      "field": "audience",
      "requirement": "民宿运营协作伙伴",
      "verdict": "met",
      "evidence": "三个画面围绕民宿门口、招牌和室内，结合简明的添加字幕介绍，符合民宿运营协作中的视频素材场景。"
    },
    {
      "field": "platform",
      "requirement": "小红书",
      "verdict": "met",
      "evidence": "稿件用三个生活场景镜头介绍单一功能，后两镜配简短屏幕文字，适合小红书短视频表达。"
    },
    {
      "field": "style",
      "requirement": "简洁",
      "verdict": "met",
      "evidence": "每镜仅一句文字；第2、3镜分别为“先看看招牌。”“再看看室内。”，没有冗长解释。"
    },
    {
      "field": "style",
      "requirement": "不营销",
      "verdict": "met",
      "evidence": "第1镜客观陈述添加字幕能力，后两镜描述场景；标题及正文没有夸大效果、促销或购买引导。"
    }
  ],
  "summary": "已满足需求：仅介绍添加字幕，删除裁剪和手动编辑介绍，保留三个分镜及指定顺序。受众、平台和风格适配，表达与节奏检查通过。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "从门口到房间",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "标题描述空间游览顺序，不包含产品能力或效果承诺。"
    },
    {
      "location": "shot:1/visual",
      "text": "民宿门口",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅指定民宿门口拍摄场景，没有产品功能、操作步骤或真实客户背书声明。"
    },
    {
      "location": "shot:2/visual",
      "text": "民宿招牌",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅指定招牌画面，没有可验证的产品承诺。"
    },
    {
      "location": "shot:2/block:1",
      "text": "先看看招牌。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "引导观众观察当前场景的字幕文字，不声明产品能力。"
    },
    {
      "location": "shot:3/visual",
      "text": "室内空桌椅",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "描述室内拍摄对象，没有虚构产品界面、自动流程或效果。"
    },
    {
      "location": "shot:3/block:1",
      "text": "再看看室内。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "连接至室内画面的场景字幕，不包含产品性能或效果声明。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "duration_check给出三镜预计时长4、3、3秒，与最低停留时间一致。第1镜4秒承载一句添加字幕旁白；第2、3镜各3秒供阅读“先看看招牌。”“再看看室内。”并观察对应画面，停留有具体内容支撑，没有重复功能介绍或明显空镜凑时长。editor_notes不计入朗读；宿主估算总长10秒，已通过20秒上限检查。"
  },
  "expression_review_passed": true
}
```

## 执行路径

estimate_duration → check_rules → search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
