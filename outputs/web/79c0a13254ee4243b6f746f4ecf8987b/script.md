# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成三个分镜，覆盖字幕添加和手动改字，包含笔记本、字幕示意卡、讲义夹场景。每镜分别停留7.5、8、8秒，估算总长23.5秒，符合接近25秒的目标。当前稿无需删改；实际成片时长需制作后确认。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 课程视频字幕入门：添加字幕与手动改字

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

画面：笔记本场景：教师坐在桌前，笔记本播放一小段课程画面。随后在画面下方叠加课程例句，并标注“字幕示意”。留出阅读时间，不展示软件按钮或操作界面。

旁白/字幕：先从一小段课程内容开始。剪影练习版支持为视频添加字幕。

来源：P01/P01.F1

预计镜头时长：7.5 秒

### 分镜 2

画面：字幕示意卡场景：桌面纸卡写着“今天学习分树”，旁边标注“改字示意”。教师指向“树”字，再换成写着“今天学习分数”的纸卡，前后并排展示，让观众看清改动。纸卡仅说明文字修改，不模拟软件操作。

旁白/字幕：字幕文字可以手动编辑。比如，把“分树”改成“分数”。

来源：P01/P01.F2

预计镜头时长：8.0 秒

### 分镜 3

画面：讲义夹场景：教师翻开讲义夹，用手指找到讲义中的“分数”，再与旁边改好的字幕示意卡逐字对照。镜头停在讲义关键词和对应字幕上，留出核对与阅读时间。

旁白/字幕：对照讲义，读一遍字幕，再核对课程里的关键词。

来源：

预计镜头时长：8.0 秒

时长要求：22.5–25 秒（接近目标）。

预计总时长：23.5 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "fbecd3f37f41bcf8cb16abadfc09c8cf7b575c9727c96c58ad783ecefd668b79",
  "passed": true,
  "issues": [],
  "citations": [
    {
      "location": "shot:1/block:2",
      "source_id": "P01",
      "fact_id": "P01.F1",
      "quote": "剪影练习版支持为视频添加字幕。",
      "version": "2026-11-01"
    },
    {
      "location": "shot:2/block:1",
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
      "text": "课程视频字幕入门：添加字幕与手动改字"
    },
    {
      "location": "shot:1/visual",
      "text": "笔记本场景：教师坐在桌前，笔记本播放一小段课程画面。随后在画面下方叠加课程例句，并标注“字幕示意”。留出阅读时间，不展示软件按钮或操作界面。"
    },
    {
      "location": "shot:1/block:1",
      "text": "先从一小段课程内容开始。"
    },
    {
      "location": "shot:2/visual",
      "text": "字幕示意卡场景：桌面纸卡写着“今天学习分树”，旁边标注“改字示意”。教师指向“树”字，再换成写着“今天学习分数”的纸卡，前后并排展示，让观众看清改动。纸卡仅说明文字修改，不模拟软件操作。"
    },
    {
      "location": "shot:2/block:2",
      "text": "比如，把“分树”改成“分数”。"
    },
    {
      "location": "shot:3/visual",
      "text": "讲义夹场景：教师翻开讲义夹，用手指找到讲义中的“分数”，再与旁边改好的字幕示意卡逐字对照。镜头停在讲义关键词和对应字幕上，留出核对与阅读时间。"
    },
    {
      "location": "shot:3/block:1",
      "text": "对照讲义，读一遍字幕，再核对课程里的关键词。"
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
  "script_hash": "fbecd3f37f41bcf8cb16abadfc09c8cf7b575c9727c96c58ad783ecefd668b79",
  "request_hash": "5a8a440420139279ec1553d5df17e98f299a81d8749d3f199cabda7f4dd353a5",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "用三个分镜",
      "verdict": "met",
      "evidence": "当前稿件共3个分镜，依次呈现字幕添加、手动改字和对照讲义核对。"
    },
    {
      "field": "topic",
      "requirement": "字幕添加",
      "verdict": "met",
      "evidence": "分镜1旁白明确介绍“剪影练习版支持为视频添加字幕”，画面叠加课程例句并标注“字幕示意”。"
    },
    {
      "field": "topic",
      "requirement": "手动改字",
      "verdict": "met",
      "evidence": "分镜2旁白说明“字幕文字可以手动编辑”，配合将“分树”改为“分数”的纸卡示例。"
    },
    {
      "field": "topic",
      "requirement": "每个镜头至少停留5秒",
      "verdict": "met",
      "evidence": "三个分镜的hold_seconds分别为7.5、8、8，均不少于5秒。"
    },
    {
      "field": "topic",
      "requirement": "笔记本",
      "verdict": "met",
      "evidence": "分镜1明确安排“教师坐在桌前，笔记本播放一小段课程画面”。"
    },
    {
      "field": "topic",
      "requirement": "字幕示意卡",
      "verdict": "met",
      "evidence": "分镜2以字幕示意卡展示修改前后的例句，并安排两张纸卡并排观察。"
    },
    {
      "field": "topic",
      "requirement": "讲义夹",
      "verdict": "met",
      "evidence": "分镜3明确安排教师翻开讲义夹，找到“分数”并与字幕示意卡逐字对照。"
    },
    {
      "field": "topic",
      "requirement": "目标接近25秒",
      "verdict": "met",
      "evidence": "稿件标注的镜头停留合计23.5秒，接近25秒目标；此处依据脚本安排判断覆盖，不代表成片实测时长。"
    },
    {
      "field": "audience",
      "requirement": "初次编辑课程视频的教师",
      "verdict": "met",
      "evidence": "标题定位“课程视频字幕入门”，画面采用教师、课程例句和讲义核对，内容从添加字幕与基础改字开始，适合初次编辑者。"
    },
    {
      "field": "platform",
      "requirement": "B站",
      "verdict": "met",
      "evidence": "稿件采用主题明确的入门标题、连续分镜和口播示例，知识讲解形式适合B站短视频。"
    },
    {
      "field": "style",
      "requirement": "慢节奏",
      "verdict": "met",
      "evidence": "每镜停留7.5至8秒，分别安排例句阅读、修改前后对比和讲义核对，均留有观察时间。"
    },
    {
      "field": "style",
      "requirement": "明确",
      "verdict": "met",
      "evidence": "分镜1直接说明添加字幕，分镜2直接说明手动编辑并展示“分树→分数”，分镜3给出具体核对动作，表述清楚。"
    }
  ],
  "summary": "全部需求均已覆盖。涉及产品能力的表达有资料支持，三个镜头的阅读、改字对比和讲义核对能合理支撑慢节奏停留。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "课程视频字幕入门：添加字幕与手动改字",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        },
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "标题涉及添加字幕和手动改字，分别由P01.F1的添加字幕能力、P01.F2的手动编辑字幕文字能力支持。"
    },
    {
      "location": "shot:1/visual",
      "text": "笔记本场景：教师坐在桌前，笔记本播放一小段课程画面。随后在画面下方叠加课程例句，并标注“字幕示意”。留出阅读时间，不展示软件按钮或操作界面。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "叠加课程例句示意为视频添加字幕，由P01.F1支持；教师和笔记本属于拍摄场景，未虚构软件按钮、界面或操作流程。"
    },
    {
      "location": "shot:1/block:1",
      "text": "先从一小段课程内容开始。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "这是选择课程片段的引导语，不含产品能力或效果承诺。"
    },
    {
      "location": "shot:2/visual",
      "text": "字幕示意卡场景：桌面纸卡写着“今天学习分树”，旁边标注“改字示意”。教师指向“树”字，再换成写着“今天学习分数”的纸卡，前后并排展示，让观众看清改动。纸卡仅说明文字修改，不模拟软件操作。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "纸卡前后对比示意手动修改字幕文字，由P01.F2支持；没有声称自动纠错，也未模拟具体软件操作。"
    },
    {
      "location": "shot:2/block:2",
      "text": "比如，把“分树”改成“分数”。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "承接手动编辑字幕的旁白，给出文字替换示例，未超出P01.F2支持的能力范围。"
    },
    {
      "location": "shot:3/visual",
      "text": "讲义夹场景：教师翻开讲义夹，用手指找到讲义中的“分数”，再与旁边改好的字幕示意卡逐字对照。镜头停在讲义关键词和对应字幕上，留出核对与阅读时间。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "全部动作由教师对纸质讲义和示意卡完成，是人工核对与拍摄安排，没有承诺产品自动核对等能力。"
    },
    {
      "location": "shot:3/block:1",
      "text": "对照讲义，读一遍字幕，再核对课程里的关键词。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "这是面向教师的人工检查建议，不含产品性能、自动化或效果保证。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "分镜1停留7.5秒，两句简短旁白配课程画面和例句阅读；分镜2停留8秒，旁白配指字、换卡及前后对比；分镜3停留8秒，一句旁白配翻讲义、定位关键词和逐字核对。每镜均有明确观察或动作任务，未见重复同一事实或空镜凑时长。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
