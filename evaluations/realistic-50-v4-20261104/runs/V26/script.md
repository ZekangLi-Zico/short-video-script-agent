# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：脚本已完成，无需删改：固定展示“开讲”卡片，旁白仅为“剪影练习版支持为视频添加字幕。”，无寒暄或第二功能。估算4秒，符合6秒上限，三项检查均通过。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 添加字幕

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

画面：固定展示一张写着“开讲”的卡片。事实块作为旁白直接朗读。

旁白/字幕：剪影练习版支持为视频添加字幕。

来源：P01/P01.F1

预计镜头时长：4.0 秒

预计总时长：4.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "dd876cdf7d14c81f55b17fbe23054ecb670ab4fb7b5accc587dd96c0b6bb0a3e",
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
      "text": "添加字幕"
    },
    {
      "location": "shot:1/visual",
      "text": "固定展示一张写着“开讲”的卡片。事实块作为旁白直接朗读。"
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
  "script_hash": "dd876cdf7d14c81f55b17fbe23054ecb670ab4fb7b5accc587dd96c0b6bb0a3e",
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
      "requirement": "剪影练习版支持为视频添加字幕。",
      "verdict": "met",
      "evidence": "第1镜旁白逐字包含该句，且已由rules_check核对P01.F1通过。"
    },
    {
      "field": "topic",
      "requirement": "只介绍剪影练习版支持为视频添加字幕。",
      "verdict": "met",
      "evidence": "标题“添加字幕”和第1镜旁白均只涉及添加字幕；画面为卡片，没有介绍手动编辑字幕、裁剪或画面比例等其他功能。"
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
      "evidence": "全稿仅有添加字幕这一项产品功能，未加入第二项功能。"
    },
    {
      "field": "topic",
      "requirement": "画面是一张写着“开讲”的卡片。",
      "verdict": "met",
      "evidence": "第1镜明确写明“固定展示一张写着‘开讲’的卡片”，事实块安排为旁白。"
    },
    {
      "field": "audience",
      "requirement": "刚进入课程页的访客",
      "verdict": "met",
      "evidence": "第1镜用一句直白旁白介绍产品基础功能，配合“开讲”卡片，无需访客具备操作知识。"
    },
    {
      "field": "platform",
      "requirement": "抖音",
      "verdict": "met",
      "evidence": "单镜头、两字卡片与一句旁白构成4.0秒短视频，信息集中，适合快速观看。"
    },
    {
      "field": "style",
      "requirement": "极简",
      "verdict": "met",
      "evidence": "全稿仅一个固定卡片镜头、一句旁白，标题为“添加字幕”。"
    },
    {
      "field": "style",
      "requirement": "信息优先",
      "verdict": "met",
      "evidence": "标题直接点明功能，旁白开头即给出产品名称与添加字幕能力，没有铺垫。"
    }
  ],
  "summary": "当前稿满足全部明确要求：仅介绍添加字幕，直接开讲，固定展示“开讲”卡片，预计4秒；表达有依据，节奏合理。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "添加字幕",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "标题指向添加字幕能力，P01.F1明确支持“剪影练习版支持为视频添加字幕。”，未增加效果或自动化承诺。"
    },
    {
      "location": "shot:1/visual",
      "text": "固定展示一张写着“开讲”的卡片。事实块作为旁白直接朗读。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "全文仅规定卡片画面与旁白呈现方式，不涉及产品能力、具体界面或操作步骤声明。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "第1镜预计4.0秒，承载14个语音单位的旁白与两字卡片“开讲”，朗读和观看任务与时长匹配。hold_seconds为0表示没有额外延长，未见重复事实或空镜凑时长。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
