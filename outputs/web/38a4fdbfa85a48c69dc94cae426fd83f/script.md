# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成安静、说明式的三镜脚本，覆盖添加字幕、手动编辑字幕文字，以及空展厅、导览卡和休息区三个背景。未编造文物年代或展品故事，结尾直接切黑。当前稿无需修改，估算12秒，符合26秒上限，无待补事项。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 展馆记录：添加与编辑字幕

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

画面：空展厅固定远景，展示安静的空间。以下文字作为轻声旁白，不出现文物年代或展品故事。

旁白/字幕：志愿者的展馆记录，从空展厅开始。

来源：

预计镜头时长：4.0 秒

### 分镜 2

画面：导览卡近景，卡面仅写“导览卡”。画面下方叠加“导览卡”作为添加字幕的示意，不展示软件界面。以下产品事实作为轻声旁白。

旁白/字幕：剪影练习版支持为视频添加字幕。

来源：P01/P01.F1

预计镜头时长：4.0 秒

### 分镜 3

画面：休息区固定中景，画面下方以字幕排版示意将“休区”改为“休息区”，不展示按钮或操作步骤。以下产品事实作为轻声旁白；旁白与修改示意结束后直接切黑，无号召语、无尾卡。

旁白/字幕：字幕文字可以手动编辑。

来源：P01/P01.F2

预计镜头时长：4.0 秒

预计总时长：12.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "7a1a0e0bb05bd87c107ddc830cffb796a14f92c81c3043c5d648602f66e44753",
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
      "text": "展馆记录：添加与编辑字幕"
    },
    {
      "location": "shot:1/visual",
      "text": "空展厅固定远景，展示安静的空间。以下文字作为轻声旁白，不出现文物年代或展品故事。"
    },
    {
      "location": "shot:1/block:1",
      "text": "志愿者的展馆记录，从空展厅开始。"
    },
    {
      "location": "shot:2/visual",
      "text": "导览卡近景，卡面仅写“导览卡”。画面下方叠加“导览卡”作为添加字幕的示意，不展示软件界面。以下产品事实作为轻声旁白。"
    },
    {
      "location": "shot:3/visual",
      "text": "休息区固定中景，画面下方以字幕排版示意将“休区”改为“休息区”，不展示按钮或操作步骤。以下产品事实作为轻声旁白；旁白与修改示意结束后直接切黑，无号召语、无尾卡。"
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
  "script_hash": "7a1a0e0bb05bd87c107ddc830cffb796a14f92c81c3043c5d648602f66e44753",
  "request_hash": "7939e15fdb046b0dd28287a964cd0fc6469e821c86b3f1bc72d2ae0c7d16d93a",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "介绍添加字幕",
      "verdict": "met",
      "evidence": "第2镜旁白“剪影练习版支持为视频添加字幕。”，画面叠加“导览卡”作为添加字幕示意。"
    },
    {
      "field": "topic",
      "requirement": "手动编辑字幕文字",
      "verdict": "met",
      "evidence": "第3镜旁白“字幕文字可以手动编辑。”，并示意将“休区”改为“休息区”。"
    },
    {
      "field": "topic",
      "requirement": "空展厅",
      "verdict": "met",
      "evidence": "第1镜明确安排“空展厅固定远景”。"
    },
    {
      "field": "topic",
      "requirement": "导览卡",
      "verdict": "met",
      "evidence": "第2镜明确安排“导览卡近景”，卡面仅写“导览卡”。"
    },
    {
      "field": "topic",
      "requirement": "休息区",
      "verdict": "met",
      "evidence": "第3镜明确安排“休息区固定中景”。"
    },
    {
      "field": "topic",
      "requirement": "不要编造文物年代或展品故事",
      "verdict": "met",
      "evidence": "全部镜头和旁白均未提供文物年代或展品故事；导览卡仅展示名称。"
    },
    {
      "field": "topic",
      "requirement": "结尾直接结束",
      "verdict": "met",
      "evidence": "第3镜明确要求“旁白与修改示意结束后直接切黑，无号召语、无尾卡”。"
    },
    {
      "field": "audience",
      "requirement": "展馆志愿者",
      "verdict": "met",
      "evidence": "第1镜以“志愿者的展馆记录”引入，后续使用导览卡和休息区文字演示字幕功能，贴合展馆记录场景。"
    },
    {
      "field": "platform",
      "requirement": "视频号",
      "verdict": "met",
      "evidence": "三镜以简短中文旁白配合直观字幕示意，内容完整、易理解，适合视频号短视频呈现。"
    },
    {
      "field": "style",
      "requirement": "安静",
      "verdict": "met",
      "evidence": "第1、3镜使用固定景别，三镜均安排轻声旁白，第1镜明确展示安静空间。"
    },
    {
      "field": "style",
      "requirement": "说明式",
      "verdict": "met",
      "evidence": "第2、3镜直接说明添加字幕和手动编辑文字两项功能，并配合对应示意，无夸张宣传。"
    }
  ],
  "summary": "明确需求均已落实：两项字幕功能、三个展馆背景及直接结束的结尾均有体现。表达有资料支持，逐镜节奏合理。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "展馆记录：添加与编辑字幕",
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
      "evidence": "标题中的添加字幕和编辑字幕分别由P01.F1、P01.F2支持，未承诺自动编辑或其他能力。"
    },
    {
      "location": "shot:1/visual",
      "text": "空展厅固定远景，展示安静的空间。以下文字作为轻声旁白，不出现文物年代或展品故事。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅规定展厅背景、景别、旁白方式和内容边界，不含产品能力或效果承诺。"
    },
    {
      "location": "shot:1/block:1",
      "text": "志愿者的展馆记录，从空展厅开始。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于场景引入，未声称真实客户背书或产品效果。"
    },
    {
      "location": "shot:2/visual",
      "text": "导览卡近景，卡面仅写“导览卡”。画面下方叠加“导览卡”作为添加字幕的示意，不展示软件界面。以下产品事实作为轻声旁白。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "字幕叠加示意对应P01.F1支持的添加字幕能力；画面下方是成片字幕安排，未虚构产品界面、按钮或操作流程。"
    },
    {
      "location": "shot:3/visual",
      "text": "休息区固定中景，画面下方以字幕排版示意将“休区”改为“休息区”，不展示按钮或操作步骤。以下产品事实作为轻声旁白；旁白与修改示意结束后直接切黑，无号召语、无尾卡。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "修改字幕文字的示意由P01.F2支持，配套旁白明确为手动编辑，未暗示自动纠错；其余内容为拍摄和收尾安排。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "duration_check中三镜预计均为4秒：第1镜配14单位旁白和展厅观察，第2镜配14单位旁白及导览卡字幕示意，第3镜配10单位旁白及“休区”改为“休息区”的简短演示。各镜均有明确内容支撑，第3镜满足4秒最低停留，无重复事实或空镜凑时长。总计12秒，宿主已判定符合26秒上限。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
