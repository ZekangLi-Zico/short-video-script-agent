# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成4镜头脚本，保留客户确认标题“让每一句话都看得见”，涵盖字幕添加与手动编辑字幕文字，风格温和、简洁。估算15秒，符合25秒上限；规则检查与需求模型审核均通过，无需进一步删改。实际成片时长以制作结果为准。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 让每一句话都看得见

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

画面：自然光下，创作者面对镜头准备录制一段日常分享。画面展示活动标题“让每一句话都看得见”；本镜头文字块作为旁白。

旁白/字幕：把想说的话，放进画面里。

来源：

预计镜头时长：3.0 秒

### 分镜 2

画面：以日常录制画面为背景，展示添加字幕功能的产品事实卡。旁白逐字读出事实卡内容，不展示操作界面。

旁白/字幕：剪影练习版支持为视频添加字幕。

来源：P01/P01.F1

预计镜头时长：5.0 秒

### 分镜 3

画面：切至简洁浅色背景，展示手动编辑字幕文字的产品事实卡，轻柔强调“手动编辑”四字。旁白逐字读出事实卡内容。

旁白/字幕：字幕文字可以手动编辑。

来源：P01/P01.F2

预计镜头时长：4.0 秒

### 分镜 4

画面：创作者整理录制好的日常素材，画面缓缓定格。本镜头文字块作为结尾旁白，不展示软件界面。

旁白/字幕：先从一条短片开始。

来源：

预计镜头时长：3.0 秒

预计总时长：15.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "d27a04f39fbd0f3bcfcd1a0b7a593d1d04e1ef7786e5baac070f991d26d64cb2",
  "passed": true,
  "issues": [],
  "citations": [
    {
      "location": "shot:2/block:1",
      "source_id": "P01",
      "fact_id": "P01.F1",
      "quote": "剪影练习版支持为视频添加字幕。",
      "version": "2026-11-01"
    },
    {
      "location": "shot:3/block:1",
      "source_id": "P01",
      "fact_id": "P01.F2",
      "quote": "字幕文字可以手动编辑。",
      "version": "2026-11-01"
    }
  ],
  "rules_version": "2026-11-03-v1",
  "requires_expression_review": true,
  "expression_slots": [
    {
      "location": "title",
      "text": "让每一句话都看得见"
    },
    {
      "location": "shot:1/visual",
      "text": "自然光下，创作者面对镜头准备录制一段日常分享。画面展示活动标题“让每一句话都看得见”；本镜头文字块作为旁白。"
    },
    {
      "location": "shot:1/block:1",
      "text": "把想说的话，放进画面里。"
    },
    {
      "location": "shot:2/visual",
      "text": "以日常录制画面为背景，展示添加字幕功能的产品事实卡。旁白逐字读出事实卡内容，不展示操作界面。"
    },
    {
      "location": "shot:3/visual",
      "text": "切至简洁浅色背景，展示手动编辑字幕文字的产品事实卡，轻柔强调“手动编辑”四字。旁白逐字读出事实卡内容。"
    },
    {
      "location": "shot:4/visual",
      "text": "创作者整理录制好的日常素材，画面缓缓定格。本镜头文字块作为结尾旁白，不展示软件界面。"
    },
    {
      "location": "shot:4/block:1",
      "text": "先从一条短片开始。"
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
  "script_hash": "d27a04f39fbd0f3bcfcd1a0b7a593d1d04e1ef7786e5baac070f991d26d64cb2",
  "request_hash": "64ed8f11040d6330df52abfec5f77a1054855646cfc701f8dfb28ca89a6d98e5",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "介绍字幕添加",
      "verdict": "met",
      "evidence": "镜头2展示事实卡并口播“剪影练习版支持为视频添加字幕。”，覆盖字幕添加功能。"
    },
    {
      "field": "topic",
      "requirement": "手动编辑字幕文字",
      "verdict": "met",
      "evidence": "镜头3展示并口播“字幕文字可以手动编辑。”，画面强调“手动编辑”。"
    },
    {
      "field": "topic",
      "requirement": "标题必须是“让每一句话都看得见”",
      "verdict": "met",
      "evidence": "script.title为“让每一句话都看得见”，镜头1也安排展示同一活动标题。"
    },
    {
      "field": "audience",
      "requirement": "活动页新访客",
      "verdict": "met",
      "evidence": "镜头1呈现活动标题，镜头2、3用直白短句介绍两项基础功能，无需已有产品知识即可理解。"
    },
    {
      "field": "platform",
      "requirement": "抖音",
      "verdict": "met",
      "evidence": "四个镜头采用人物场景、简短事实卡和短句旁白，内容集中，适合短视频信息浏览。"
    },
    {
      "field": "style",
      "requirement": "温和",
      "verdict": "met",
      "evidence": "镜头1采用自然光，镜头3要求“轻柔强调”，结尾“先从一条短片开始。”语气平和。"
    },
    {
      "field": "style",
      "requirement": "简洁",
      "verdict": "met",
      "evidence": "每个镜头仅一条简短旁白；镜头2、3各介绍一项功能，没有冗长解释。"
    }
  ],
  "summary": "两项功能和客户确认的标题均已落实，受众、平台及风格适配。表达未见超出资料的产品承诺，各镜头停留安排合理。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "让每一句话都看得见",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "这是原始需求指定的活动标题，以修辞表达文字可见的主题，没有具体性能、准确率或自动化承诺。"
    },
    {
      "location": "shot:1/visual",
      "text": "自然光下，创作者面对镜头准备录制一段日常分享。画面展示活动标题“让每一句话都看得见”；本镜头文字块作为旁白。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "内容为录制场景、活动标题展示和旁白安排，没有声称真实用户背书或额外产品能力。"
    },
    {
      "location": "shot:1/block:1",
      "text": "把想说的话，放进画面里。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于引导创作的邀请式表达，没有给出可验证的产品性能或操作承诺。"
    },
    {
      "location": "shot:2/visual",
      "text": "以日常录制画面为背景，展示添加字幕功能的产品事实卡。旁白逐字读出事实卡内容，不展示操作界面。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "其中“添加字幕功能”由P01.F1“剪影练习版支持为视频添加字幕。”支持；其余内容为背景、事实卡和朗读安排，没有增加操作流程或效果声明。"
    },
    {
      "location": "shot:3/visual",
      "text": "切至简洁浅色背景，展示手动编辑字幕文字的产品事实卡，轻柔强调“手动编辑”四字。旁白逐字读出事实卡内容。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "其中“手动编辑字幕文字”由P01.F2“字幕文字可以手动编辑。”支持；背景、文字强调和旁白安排没有引入额外能力或虚构界面。"
    },
    {
      "location": "shot:4/visual",
      "text": "创作者整理录制好的日常素材，画面缓缓定格。本镜头文字块作为结尾旁白，不展示软件界面。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "描述人物整理素材及画面定格，未将整理行为宣称为产品功能，也没有产品效果承诺。"
    },
    {
      "location": "shot:4/block:1",
      "text": "先从一条短片开始。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于行动邀请，不含产品能力、价格或效果声明。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "镜头1停留3秒，承载活动标题、人物准备录制动作及短句“把想说的话，放进画面里。”；镜头2停留5秒，支持阅读和听完字幕添加事实卡；镜头3停留4秒，支持阅读编辑功能事实卡并观察“手动编辑”的强调；镜头4停留3秒，配合整理素材、缓缓定格及“先从一条短片开始。”。各镜头均有明确内容支撑，未见重复同一事实或明显空镜凑时长。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
