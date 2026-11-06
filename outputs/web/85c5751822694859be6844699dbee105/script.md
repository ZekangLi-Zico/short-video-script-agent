# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成约4秒单镜脚本：画面为“开讲”卡片，旁白仅介绍剪影练习版支持为视频添加字幕。全部检查通过。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 剪影练习版：为视频添加字幕

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

镜头目的：直接告知访客剪影练习版支持为视频添加字幕。

画面：固定镜头拍摄一张写着“开讲”的卡片，卡片居中，保持静止至旁白结束。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–4.0 秒**

屏幕文字：开讲

旁白：剪影练习版支持为视频添加字幕。

依据：P01/P01.F1

预计镜头时长：4.0 秒

预计总时长：4.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "bd97de07b0b088e810dbc331cba051b8957db0b47a99529f496668094be00231",
  "passed": true,
  "issues": [],
  "citations": [
    {
      "location": "shot:1/block:2",
      "source_id": "P01",
      "fact_id": "P01.F1",
      "quote": "剪影练习版支持为视频添加字幕。",
      "version": "2026-11-01",
      "text": "剪影练习版支持为视频添加字幕。",
      "requires_semantic_review": true
    }
  ],
  "rules_version": "2026-11-03-v1",
  "requires_expression_review": true,
  "expression_slots": [
    {
      "location": "title",
      "text": "剪影练习版：为视频添加字幕"
    },
    {
      "location": "shot:1/visual",
      "text": "固定镜头拍摄一张写着“开讲”的卡片，卡片居中，保持静止至旁白结束。"
    },
    {
      "location": "shot:1/block:1",
      "text": "开讲"
    },
    {
      "location": "shot:1/block:2",
      "text": "剪影练习版支持为视频添加字幕。"
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
  "scope": "source_identity_and_brand_checks; every public claim requires semantic entailment review"
}
```

## 需求覆盖核对

以下为模型评估，可能漏判或误判，仍需人工确认。

```json
{
  "ok": true,
  "script_hash": "bd97de07b0b088e810dbc331cba051b8957db0b47a99529f496668094be00231",
  "request_hash": "0d282f89aa8e9846961d0637ec6061a9078d699019bca1b92d101b914577a3e9",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "六秒以内",
      "verdict": "met",
      "evidence": "宿主估算总时长为4.0秒，未超过6秒，passed为true。"
    },
    {
      "field": "topic",
      "requirement": "只介绍剪影练习版支持为视频添加字幕",
      "verdict": "met",
      "evidence": "标题和第1镜旁白均仅介绍添加字幕，未出现编辑字幕、裁剪或画面比例等其他功能。"
    },
    {
      "field": "topic",
      "requirement": "不要开场寒暄",
      "verdict": "met",
      "evidence": "第1镜直接朗读“剪影练习版支持为视频添加字幕。”，没有寒暄。"
    },
    {
      "field": "topic",
      "requirement": "不加第二个功能",
      "verdict": "met",
      "evidence": "全部公开文案只有添加字幕这一项产品功能。"
    },
    {
      "field": "topic",
      "requirement": "画面是一张写着“开讲”的卡片",
      "verdict": "met",
      "evidence": "第1镜画面明确为居中的“开讲”卡片，屏幕块也仅显示“开讲”。"
    },
    {
      "field": "audience",
      "requirement": "刚进入课程页的访客",
      "verdict": "met",
      "evidence": "“开讲”卡片配合一句直接的功能介绍，无需访客具备前置知识。"
    },
    {
      "field": "platform",
      "requirement": "抖音",
      "verdict": "met",
      "evidence": "单镜头、4秒短内容直接传递功能信息，适合短视频浏览。"
    },
    {
      "field": "style",
      "requirement": "极简，信息优先",
      "verdict": "met",
      "evidence": "仅用静止卡片和一句功能旁白，没有额外装饰文案或铺垫。"
    }
  ],
  "summary": "当前稿满足全部明确要求：约4秒，仅介绍添加字幕，画面为“开讲”卡片。公开产品声明均有资料支持，节奏合理。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "剪影练习版：为视频添加字幕",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "标题准确缩写添加字幕能力，未增加效果或自动化声明。"
    },
    {
      "location": "shot:1/visual",
      "text": "固定镜头拍摄一张写着“开讲”的卡片，卡片居中，保持静止至旁白结束。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅描述卡片构图和拍摄停留，不包含产品承诺。"
    },
    {
      "location": "shot:1/block:1",
      "text": "开讲",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于开场卡片文字，不包含可验证的产品声明。"
    },
    {
      "location": "shot:1/block:2",
      "text": "剪影练习版支持为视频添加字幕。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "与所标注事实原文一致，全部含义均获支持。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "第1镜同一节拍中旁白预计4秒、屏幕阅读1秒，并行计为4秒；卡片保持至旁白结束符合指定画面，没有额外空镜或重复凑时长。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
