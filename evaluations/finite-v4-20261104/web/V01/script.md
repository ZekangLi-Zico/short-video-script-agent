# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：脚本已完成，保留现稿，无需删改。以早餐摊主讲今日备料为背景，仅介绍添加字幕，镜头按蒸笼、手写菜单、打包台排列，均要求不出现顾客正脸。估时约15秒，符合25秒上限；实际成片时长需在剪辑后确认。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 早餐摊备料口播，配上字幕

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

画面：蒸笼特写，摊主双手将包子摆入笼内。摊主自然口播本镜头文字，并将相同文字作为字幕叠加在画面下方。只拍蒸笼和手部，不出现顾客正脸。

旁白/字幕：今天备料，先把包子上笼。

来源：

预计镜头时长：4.0 秒

### 分镜 2

画面：切到手写菜单特写，摊主写下今日供应的包子。第一块文字为摊主口播及对应字幕；随后展示第二块产品事实卡，事实卡不作旁白。不展示软件界面，不出现顾客正脸。

旁白/字幕：菜单写好，今天就按这个备料。剪影练习版支持为视频添加字幕。

来源：P01/P01.F1

预计镜头时长：7.0 秒

### 分镜 3

画面：切到打包台，摊主双手摆齐打包盒和纸袋。摊主自然口播本镜头文字，并叠加相同字幕。镜头停在收拾好的台面，只拍手部和物品，不出现顾客正脸。

旁白/字幕：打包盒摆齐，准备开摊。

来源：

预计镜头时长：4.0 秒

预计总时长：15.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "320e759fe97904d08d0895c54e07098853404b7dcc1320749e006252d16ac907",
  "passed": true,
  "issues": [],
  "citations": [
    {
      "location": "shot:2/block:2",
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
      "text": "早餐摊备料口播，配上字幕"
    },
    {
      "location": "shot:1/visual",
      "text": "蒸笼特写，摊主双手将包子摆入笼内。摊主自然口播本镜头文字，并将相同文字作为字幕叠加在画面下方。只拍蒸笼和手部，不出现顾客正脸。"
    },
    {
      "location": "shot:1/block:1",
      "text": "今天备料，先把包子上笼。"
    },
    {
      "location": "shot:2/visual",
      "text": "切到手写菜单特写，摊主写下今日供应的包子。第一块文字为摊主口播及对应字幕；随后展示第二块产品事实卡，事实卡不作旁白。不展示软件界面，不出现顾客正脸。"
    },
    {
      "location": "shot:2/block:1",
      "text": "菜单写好，今天就按这个备料。"
    },
    {
      "location": "shot:3/visual",
      "text": "切到打包台，摊主双手摆齐打包盒和纸袋。摊主自然口播本镜头文字，并叠加相同字幕。镜头停在收拾好的台面，只拍手部和物品，不出现顾客正脸。"
    },
    {
      "location": "shot:3/block:1",
      "text": "打包盒摆齐，准备开摊。"
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
  "script_hash": "320e759fe97904d08d0895c54e07098853404b7dcc1320749e006252d16ac907",
  "request_hash": "4299792130470435332510610b8526e5f391e330ac68588a7ba5d1498ead5ad2",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "做一条剪影练习版字幕功能介绍",
      "verdict": "met",
      "evidence": "镜头2事实卡明确写出“剪影练习版支持为视频添加字幕。”，三个镜头均安排字幕展示。"
    },
    {
      "field": "topic",
      "requirement": "背景是早餐摊主讲今日备料",
      "verdict": "met",
      "evidence": "摊主口播“今天备料，先把包子上笼。”“菜单写好，今天就按这个备料。”，画面包含摆包子、写菜单和整理打包用品。"
    },
    {
      "field": "topic",
      "requirement": "只介绍添加字幕",
      "verdict": "met",
      "evidence": "产品功能仅涉及添加字幕及其成片示意；未介绍手动编辑字幕、裁剪视频或画面比例选项，也未声称自动生成字幕。"
    },
    {
      "field": "topic",
      "requirement": "画面按蒸笼、手写菜单、打包台的顺序",
      "verdict": "met",
      "evidence": "镜头1为“蒸笼特写”，镜头2为“手写菜单特写”，镜头3为“打包台”，顺序一致。"
    },
    {
      "field": "topic",
      "requirement": "不要出现顾客正脸",
      "verdict": "met",
      "evidence": "三个镜头均明确“不出现顾客正脸”；镜头1、3进一步限定只拍手部和物品，镜头2限定菜单特写。"
    },
    {
      "field": "audience",
      "requirement": "小店新媒体兼职",
      "verdict": "met",
      "evidence": "使用早餐摊备料这一小店拍摄场景，以口播对应字幕示例和一句功能说明呈现，无需理解专业术语。"
    },
    {
      "field": "platform",
      "requirement": "抖音",
      "verdict": "met",
      "evidence": "三个生活场景特写配短口播和字幕，内容集中；宿主估算总长15秒，适合短视频观看。"
    },
    {
      "field": "style",
      "requirement": "像同事分享经验",
      "verdict": "met",
      "evidence": "“菜单写好，今天就按这个备料。”“打包盒摆齐，准备开摊。”以自然工作口吻分享具体做法，语气平实。"
    },
    {
      "field": "style",
      "requirement": "短句",
      "verdict": "met",
      "evidence": "口播均为简短句子，如“今天备料，先把包子上笼。”；产品事实卡也仅用一句话介绍功能。"
    }
  ],
  "summary": "稿件覆盖全部明确要求：早餐摊备料场景、指定画面顺序和顾客正脸限制均已落实，功能范围仅为添加字幕。表达有资料支持，预计15秒，节奏合理。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "早餐摊备料口播，配上字幕",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "标题中的“配上字幕”对应为视频添加字幕，P01.F1支持该能力；早餐摊备料是拍摄场景。"
    },
    {
      "location": "shot:1/visual",
      "text": "蒸笼特写，摊主双手将包子摆入笼内。摊主自然口播本镜头文字，并将相同文字作为字幕叠加在画面下方。只拍蒸笼和手部，不出现顾客正脸。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "“将相同文字作为字幕叠加”示意添加字幕，获P01.F1支持；字幕置于画面下方属于成片构图安排，未虚构软件界面或自动识别能力。"
    },
    {
      "location": "shot:1/block:1",
      "text": "今天备料，先把包子上笼。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "摊主描述备料动作，不含产品能力或效果承诺。"
    },
    {
      "location": "shot:2/visual",
      "text": "切到手写菜单特写，摊主写下今日供应的包子。第一块文字为摊主口播及对应字幕；随后展示第二块产品事实卡，事实卡不作旁白。不展示软件界面，不出现顾客正脸。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "口播对应字幕及所展示的“支持为视频添加字幕”事实卡均由P01.F1支持；菜单、切镜和事实卡不作旁白属于拍摄安排。"
    },
    {
      "location": "shot:2/block:1",
      "text": "菜单写好，今天就按这个备料。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "描述摊主按菜单备料的场景，不含产品声明。"
    },
    {
      "location": "shot:3/visual",
      "text": "切到打包台，摊主双手摆齐打包盒和纸袋。摊主自然口播本镜头文字，并叠加相同字幕。镜头停在收拾好的台面，只拍手部和物品，不出现顾客正脸。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "“叠加相同字幕”仅展示添加字幕能力，由P01.F1支持；整理物品及停留台面属于场景与拍摄安排。"
    },
    {
      "location": "shot:3/block:1",
      "text": "打包盒摆齐，准备开摊。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "描述整理打包用品和准备营业，不含产品能力或效果承诺。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "宿主估算三个镜头分别为4秒、7秒、4秒，均满足最低停留4秒、6秒、4秒。镜头1用短口播配摆包子动作；镜头2安排写菜单、口播字幕和随后阅读一句事实卡，7秒有具体内容支撑；镜头3用短口播配整理用品及完成后的台面展示。字幕在不同备料动作中持续示例，不属于重复事实或空镜凑时长。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
