# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成3镜脚本，预计16秒，符合26秒上限。以空展厅、导览卡和休息区展示添加字幕及手动修改文字，未编造文物信息，结尾直接结束。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 展馆导览视频：添加字幕与修改文字

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

镜头目的：以空展厅视频展示添加字幕的用途。

画面：空展厅固定机位画面，切到同一视频的编辑画面，展示加入“这里是展厅”字幕后的效果；不突出未经资料确认的按钮。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–4.0 秒**

旁白＋同步字幕：剪影练习版支持为视频添加字幕。

依据：P01/P01.F1

**第 2 拍 · 镜内 4.0–6.0 秒**

屏幕文字：这里是展厅

预计镜头时长：6.0 秒

### 分镜 2

镜头目的：借导览卡画面演示手动修改字幕文字。

画面：志愿者手持只写“导览卡”的卡片；切入对应视频字幕编辑画面，将“这是卡片”手动改为“这是导览卡”，展示修改后的文字。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–3.0 秒**

旁白＋同步字幕：字幕文字可以手动编辑。

依据：P01/P01.F2

**第 2 拍 · 镜内 3.0–5.0 秒**

屏幕文字：这是卡片

**第 3 拍 · 镜内 5.0–7.0 秒**

屏幕文字：这是导览卡

预计镜头时长：7.0 秒

### 分镜 3

镜头目的：展示字幕在休息区镜头中的成片效果，然后直接结束。

画面：固定机位拍摄休息区座椅，画面配上“这里是休息区”字幕，停留供观看后直接切黑结束。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–3.0 秒**

屏幕文字：这里是休息区

预计镜头时长：3.0 秒

预计总时长：16.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "7dbd3ed98dd5d6f07544da8fa8350cc54d5b5107394688df0bd36386eb70fe96",
  "passed": true,
  "issues": [],
  "citations": [
    {
      "location": "shot:1/block:1",
      "source_id": "P01",
      "fact_id": "P01.F1",
      "quote": "剪影练习版支持为视频添加字幕。",
      "version": "2026-11-01",
      "text": "剪影练习版支持为视频添加字幕。",
      "requires_semantic_review": true
    },
    {
      "location": "shot:2/block:1",
      "source_id": "P01",
      "fact_id": "P01.F2",
      "quote": "字幕文字可以手动编辑。",
      "version": "2026-11-01",
      "text": "字幕文字可以手动编辑。",
      "requires_semantic_review": true
    }
  ],
  "rules_version": "2026-11-03-v1",
  "requires_expression_review": true,
  "expression_slots": [
    {
      "location": "title",
      "text": "展馆导览视频：添加字幕与修改文字"
    },
    {
      "location": "shot:1/visual",
      "text": "空展厅固定机位画面，切到同一视频的编辑画面，展示加入“这里是展厅”字幕后的效果；不突出未经资料确认的按钮。"
    },
    {
      "location": "shot:1/block:1",
      "text": "剪影练习版支持为视频添加字幕。"
    },
    {
      "location": "shot:1/block:2",
      "text": "这里是展厅"
    },
    {
      "location": "shot:2/visual",
      "text": "志愿者手持只写“导览卡”的卡片；切入对应视频字幕编辑画面，将“这是卡片”手动改为“这是导览卡”，展示修改后的文字。"
    },
    {
      "location": "shot:2/block:1",
      "text": "字幕文字可以手动编辑。"
    },
    {
      "location": "shot:2/block:2",
      "text": "这是卡片"
    },
    {
      "location": "shot:2/block:3",
      "text": "这是导览卡"
    },
    {
      "location": "shot:3/visual",
      "text": "固定机位拍摄休息区座椅，画面配上“这里是休息区”字幕，停留供观看后直接切黑结束。"
    },
    {
      "location": "shot:3/block:1",
      "text": "这里是休息区"
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
  "scope": "source_identity_and_brand_checks; every public claim requires semantic entailment review"
}
```

## 需求覆盖核对

以下为模型评估，可能漏判或误判，仍需人工确认。

```json
{
  "ok": true,
  "script_hash": "7dbd3ed98dd5d6f07544da8fa8350cc54d5b5107394688df0bd36386eb70fe96",
  "request_hash": "7939e15fdb046b0dd28287a964cd0fc6469e821c86b3f1bc72d2ae0c7d16d93a",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "添加字幕",
      "verdict": "met",
      "evidence": "第1镜说明支持添加字幕，并展示“这里是展厅”的字幕效果。"
    },
    {
      "field": "topic",
      "requirement": "手动编辑字幕文字",
      "verdict": "met",
      "evidence": "第2镜将“这是卡片”手动改为“这是导览卡”。"
    },
    {
      "field": "topic",
      "requirement": "空展厅",
      "verdict": "met",
      "evidence": "第1镜明确采用空展厅固定机位画面。"
    },
    {
      "field": "topic",
      "requirement": "导览卡",
      "verdict": "met",
      "evidence": "第2镜展示志愿者手持写有“导览卡”的卡片。"
    },
    {
      "field": "topic",
      "requirement": "休息区",
      "verdict": "met",
      "evidence": "第3镜拍摄休息区座椅并显示对应字幕。"
    },
    {
      "field": "topic",
      "requirement": "不要编造文物年代或展品故事",
      "verdict": "met",
      "evidence": "全部镜头仅介绍场景和字幕功能，没有文物年代或展品故事。"
    },
    {
      "field": "topic",
      "requirement": "结尾直接结束",
      "verdict": "met",
      "evidence": "第3镜展示休息区字幕后直接切黑，没有额外结束语或行动邀请。"
    },
    {
      "field": "audience",
      "requirement": "展馆志愿者",
      "verdict": "met",
      "evidence": "第2镜由志愿者展示导览卡，字幕示例适用于展馆场景。"
    },
    {
      "field": "platform",
      "requirement": "视频号",
      "verdict": "met",
      "evidence": "三镜头用简短中文声画说明功能，16秒的内容适合短视频观看。"
    },
    {
      "field": "style",
      "requirement": "安静",
      "verdict": "met",
      "evidence": "固定机位与字幕观察停留形成平静表达，没有喧闹或夸张安排。"
    },
    {
      "field": "style",
      "requirement": "说明式",
      "verdict": "met",
      "evidence": "前两镜分别说明添加字幕和手动编辑文字，并配具体示例。"
    }
  ],
  "summary": "当前稿覆盖全部明确要求，功能表述有资料支持，三个展馆背景均已落实，结尾直接结束。预计16秒，符合26秒上限，镜头节奏合理。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "展馆导览视频：添加字幕与修改文字",
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
      "evidence": "标题中的添加字幕和修改文字均由两条功能原文支持。"
    },
    {
      "location": "shot:1/visual",
      "text": "空展厅固定机位画面，切到同一视频的编辑画面，展示加入“这里是展厅”字幕后的效果；不突出未经资料确认的按钮。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "仅示意资料支持的添加字幕效果，没有指定按钮名称或具体界面布局。"
    },
    {
      "location": "shot:1/block:1",
      "text": "剪影练习版支持为视频添加字幕。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "文案与所引功能原文一致。"
    },
    {
      "location": "shot:1/block:2",
      "text": "这里是展厅",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "这是配合空展厅画面的场景字幕，不含产品承诺。"
    },
    {
      "location": "shot:2/visual",
      "text": "志愿者手持只写“导览卡”的卡片；切入对应视频字幕编辑画面，将“这是卡片”手动改为“这是导览卡”，展示修改后的文字。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "文字替换是手动编辑字幕的具体示意，没有新增自动化能力或界面操作步骤。"
    },
    {
      "location": "shot:2/block:1",
      "text": "字幕文字可以手动编辑。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "文案与所引手动编辑功能原文一致。"
    },
    {
      "location": "shot:2/block:2",
      "text": "这是卡片",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "这是修改前的场景示例字幕，不含产品能力声明。"
    },
    {
      "location": "shot:2/block:3",
      "text": "这是导览卡",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "这是修改后的场景示例字幕，不含产品能力声明。"
    },
    {
      "location": "shot:3/visual",
      "text": "固定机位拍摄休息区座椅，画面配上“这里是休息区”字幕，停留供观看后直接切黑结束。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "字幕成片效果由添加字幕功能支持，固定机位和切黑属于拍摄安排。"
    },
    {
      "location": "shot:3/block:1",
      "text": "这里是休息区",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "这是休息区画面的场景说明，不含产品承诺。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "第1镜6秒用于功能说明及字幕观察，第2镜7秒依次展示说明和修改前后文字，第3镜3秒观看休息区成片；各拍有明确阅读或观察内容，无空镜凑时长。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
