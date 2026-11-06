# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成裁剪片段介绍脚本：完整事实分成5字和8字两张大字卡，各展示5秒，预计共10秒，符合20秒上限；无旁白，画面仅用实物剪刀和纸片。成片仍需按门店实际观看距离确认字号与可读性。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 裁剪片段

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

画面：固定俯拍实物剪刀和白色纸片，全程仅使用这两种实物意象。纸片区域以大号黑字依次展示两张屏幕卡：前5秒只显示“剪影练习版”；后5秒只显示“支持裁剪视频片段。”，后卡分两行，每行4个汉字。两卡直接切换，文字保持静止、居中、清晰，剪刀放在文字区域之外。不显示其他文字，不使用旁白。

旁白/字幕：剪影练习版支持裁剪视频片段。

来源：P02/P02.F1

预计镜头时长：10.0 秒

## 审稿备注（不进入视频，不计入时长）

供创作者核对修改与资料缺口，不是经过事实认证的产品介绍。

事实块保留完整原文，制作时按画面说明分两张屏幕卡连续呈现，不作为旁白朗读。每卡各停留5秒，总计划展示时间10秒。标题仅为脚本名称，不额外上屏。文字估时不代表屏幕卡阅读速度的精确测量；成片需按门店实际观看距离确认字号和可读性。

预计总时长：10.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "159bf65a13d424e0cbdbd241339d0c20ecf55b61cebe29181c4b19ff44534dff",
  "passed": true,
  "issues": [],
  "citations": [
    {
      "location": "shot:1/block:1",
      "source_id": "P02",
      "fact_id": "P02.F1",
      "quote": "剪影练习版支持裁剪视频片段。",
      "version": "2026-11-01"
    }
  ],
  "rules_version": "2026-11-03-v1",
  "requires_expression_review": true,
  "expression_slots": [
    {
      "location": "title",
      "text": "裁剪片段"
    },
    {
      "location": "shot:1/visual",
      "text": "固定俯拍实物剪刀和白色纸片，全程仅使用这两种实物意象。纸片区域以大号黑字依次展示两张屏幕卡：前5秒只显示“剪影练习版”；后5秒只显示“支持裁剪视频片段。”，后卡分两行，每行4个汉字。两卡直接切换，文字保持静止、居中、清晰，剪刀放在文字区域之外。不显示其他文字，不使用旁白。"
    }
  ],
  "available_facts": [
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
  "script_hash": "159bf65a13d424e0cbdbd241339d0c20ecf55b61cebe29181c4b19ff44534dff",
  "request_hash": "d5089772cb159a82a06b38fc2ccb255563f1443a217583fe30ed63215b43601c",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "介绍裁剪片段",
      "verdict": "met",
      "evidence": "第1镜第二张卡显示“支持裁剪视频片段。”，明确介绍所要求的功能。"
    },
    {
      "field": "topic",
      "requirement": "只用大字屏幕卡片",
      "verdict": "met",
      "evidence": "第1镜明确以“大号黑字依次展示两张屏幕卡”，信息均通过字卡呈现；editor_notes说明标题不额外上屏。"
    },
    {
      "field": "topic",
      "requirement": "不使用旁白",
      "verdict": "met",
      "evidence": "第1镜明确“不使用旁白”；editor_notes进一步说明事实块“不作为旁白朗读”。"
    },
    {
      "field": "topic",
      "requirement": "每张卡最多8个汉字",
      "verdict": "met",
      "evidence": "第1镜第一张卡“剪影练习版”为5个汉字，第二张卡“支持裁剪视频片段。”为8个汉字。完整事实块按画面说明拆卡，并非同卡显示。"
    },
    {
      "field": "topic",
      "requirement": "观众应能读清楚",
      "verdict": "met",
      "evidence": "第1镜安排白色纸片上的大号黑字，静止、居中，每卡停留5秒；第二卡每行4个汉字，剪刀置于文字区域之外，具备合理的阅读安排。"
    },
    {
      "field": "topic",
      "requirement": "画面只用实物剪刀和纸片意象",
      "verdict": "met",
      "evidence": "第1镜明确“全程仅使用这两种实物意象”，未安排人物、产品界面或其他实物意象。"
    },
    {
      "field": "audience",
      "requirement": "门店远距离观看者",
      "verdict": "met",
      "evidence": "第1镜采用少字、大号黑字、白色底面、静止展示和每卡5秒停留，信息无需听取旁白，适配远距离观看需求。"
    },
    {
      "field": "platform",
      "requirement": "视频号",
      "verdict": "met",
      "evidence": "两张卡直接切换，信息简短且可无声理解；宿主估算总长10秒，适合视频号短视频呈现。"
    },
    {
      "field": "style",
      "requirement": "短字卡",
      "verdict": "met",
      "evidence": "第1镜仅安排两张字卡，分别为5个和8个汉字，无额外上屏文字。"
    },
    {
      "field": "style",
      "requirement": "清晰",
      "verdict": "met",
      "evidence": "第1镜明确文字“大号”“静止、居中、清晰”，并将剪刀放在文字区域之外，避免遮挡。"
    }
  ],
  "summary": "需求均已落实。两张大字卡分别为5字和8字，各展示5秒，无旁白，画面意象符合限制；功能表达有资料支持，节奏安排合理。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "裁剪片段",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P02",
          "fact_id": "P02.F1"
        }
      ],
      "evidence": "标题所指的裁剪功能由“剪影练习版支持裁剪视频片段。”支持，未增加效果或自动化承诺。"
    },
    {
      "location": "shot:1/visual",
      "text": "固定俯拍实物剪刀和白色纸片，全程仅使用这两种实物意象。纸片区域以大号黑字依次展示两张屏幕卡：前5秒只显示“剪影练习版”；后5秒只显示“支持裁剪视频片段。”，后卡分两行，每行4个汉字。两卡直接切换，文字保持静止、居中、清晰，剪刀放在文字区域之外。不显示其他文字，不使用旁白。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P02",
          "fact_id": "P02.F1"
        }
      ],
      "evidence": "两卡连续表达的产品声明与P02.F1原文一致。其余内容均为实物拍摄、文字排版和停留安排，未虚构产品按钮、界面、操作流程或额外能力。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "duration_check给出第1镜预计10秒，与hold_seconds=10及两卡各5秒的安排一致。两卡分别展示产品名和裁剪功能，文字为5字和8字；考虑远距离阅读，停留有明确用途，无重复事实或空镜凑时长。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
