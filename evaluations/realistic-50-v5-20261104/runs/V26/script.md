# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成预计4秒的单镜脚本：展示“开讲”卡片，旁白仅说明“剪影练习版支持为视频添加字幕。”无寒暄，无第二个功能，全部检查通过。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 字幕，让表达被看见

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

镜头目的：直接说明剪影练习版支持为视频添加字幕。

画面：固定镜头正拍一张写着“开讲”的卡片，字迹清晰；卡片保持静止，旁白结束后切出。

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
  "script_hash": "d68df0d26e99c656a3d47a35893ec005d47a6018b2e4598e1d648774ea4cb3fd",
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
      "text": "字幕，让表达被看见"
    },
    {
      "location": "shot:1/visual",
      "text": "固定镜头正拍一张写着“开讲”的卡片，字迹清晰；卡片保持静止，旁白结束后切出。"
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
  "script_hash": "d68df0d26e99c656a3d47a35893ec005d47a6018b2e4598e1d648774ea4cb3fd",
  "request_hash": "0d282f89aa8e9846961d0637ec6061a9078d699019bca1b92d101b914577a3e9",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "六秒以内",
      "verdict": "met",
      "evidence": "duration_check估算总长4.0秒，passed=true，符合6秒上限。"
    },
    {
      "field": "topic",
      "requirement": "只介绍剪影练习版支持为视频添加字幕。",
      "verdict": "met",
      "evidence": "公开文案仅涉及添加字幕；未介绍手动编辑字幕、裁剪视频或画面比例选项。"
    },
    {
      "field": "topic",
      "requirement": "剪影练习版支持为视频添加字幕。",
      "verdict": "met",
      "evidence": "第1镜第2块旁白完整说出该句，与P01.F1原文一致。"
    },
    {
      "field": "topic",
      "requirement": "不要开场寒暄",
      "verdict": "met",
      "evidence": "第1镜直接展示“开讲”卡片并介绍添加字幕能力，没有问候或寒暄。"
    },
    {
      "field": "topic",
      "requirement": "不加第二个功能",
      "verdict": "met",
      "evidence": "全稿只有“为视频添加字幕”一个产品功能，标题和画面未引入其他功能。"
    },
    {
      "field": "topic",
      "requirement": "画面是一张写着“开讲”的卡片。",
      "verdict": "met",
      "evidence": "第1镜visual明确为“固定镜头正拍一张写着‘开讲’的卡片”，屏幕块文字为“开讲”。"
    },
    {
      "field": "audience",
      "requirement": "刚进入课程页的访客",
      "verdict": "met",
      "evidence": "“开讲”卡片贴合课程入口语境，旁白直接说明产品及基础能力，无需已有操作知识。"
    },
    {
      "field": "platform",
      "requirement": "抖音",
      "verdict": "met",
      "evidence": "单镜头、4秒估算时长及直接进入信息的表达，适合快速观看的短视频形式。"
    },
    {
      "field": "style",
      "requirement": "极简",
      "verdict": "met",
      "evidence": "仅一个固定镜头、一张静止卡片、两个屏幕字和一句旁白。"
    },
    {
      "field": "style",
      "requirement": "信息优先",
      "verdict": "met",
      "evidence": "旁白开头即说明“剪影练习版支持为视频添加字幕”，没有铺垫或额外行动号召。"
    }
  ],
  "summary": "当前稿满足全部明确要求：预计4秒，仅介绍添加字幕，画面为“开讲”卡片，无寒暄或额外功能；公开表达有据，节奏合理。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "字幕，让表达被看见",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于字幕主题的修辞表达，未承诺具体产品效果、传播数据或额外能力。"
    },
    {
      "location": "shot:1/visual",
      "text": "固定镜头正拍一张写着“开讲”的卡片，字迹清晰；卡片保持静止，旁白结束后切出。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅描述卡片、拍摄方式和切出安排，没有产品能力声明或虚构操作界面。"
    },
    {
      "location": "shot:1/block:1",
      "text": "开讲",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "课程开场卡片文字，不包含产品承诺。"
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
      "evidence": "与P01.F1原文逐字一致，仅声明为视频添加字幕，未增加自动化或其他能力。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "第1镜预计4.0秒：同一beat内旁白预计4.0秒，屏幕“开讲”阅读预计1.0秒、展示4秒，声画同步。4秒最低停留由完整旁白支撑，旁白结束后切出，无重复信息或额外空镜拖延。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
