# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：脚本已完成，无需修改。画面仅展示“开讲”卡片，旁白为“剪影练习版支持为视频添加字幕。”无开场寒暄或第二个功能。预计4秒，符合6秒上限；时长为估算值，三项检查均已通过。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 添加字幕

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

画面：画面仅展示一张写着“开讲”的静态卡片；事实块作为旁白朗读。

旁白/字幕：剪影练习版支持为视频添加字幕。

来源：P01/P01.F1

预计镜头时长：4.0 秒

预计总时长：4.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "e9d40d95258673cac79a64458bad6b4976d6dd7da0f28076ac4726c79b0cf47f",
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
      "text": "画面仅展示一张写着“开讲”的静态卡片；事实块作为旁白朗读。"
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
  "script_hash": "e9d40d95258673cac79a64458bad6b4976d6dd7da0f28076ac4726c79b0cf47f",
  "request_hash": "0d282f89aa8e9846961d0637ec6061a9078d699019bca1b92d101b914577a3e9",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "六秒以内",
      "verdict": "met",
      "evidence": "duration_check给出总长4.0秒，passed=true，符合6秒上限。"
    },
    {
      "field": "topic",
      "requirement": "只介绍剪影练习版支持为视频添加字幕。",
      "verdict": "met",
      "evidence": "标题为“添加字幕”，第1镜旁白仅介绍添加字幕；画面没有出现其他产品功能。"
    },
    {
      "field": "topic",
      "requirement": "剪影练习版支持为视频添加字幕。",
      "verdict": "met",
      "evidence": "第1镜第1块原文为“剪影练习版支持为视频添加字幕。”，与要求一致，且已获P01.F1支持。"
    },
    {
      "field": "topic",
      "requirement": "不要开场寒暄",
      "verdict": "met",
      "evidence": "第1镜直接朗读功能介绍，没有问候或寒暄。"
    },
    {
      "field": "topic",
      "requirement": "不加第二个功能",
      "verdict": "met",
      "evidence": "全稿只有添加字幕这一项功能，没有介绍资料中的手动编辑字幕或其他功能。"
    },
    {
      "field": "topic",
      "requirement": "画面是一张写着“开讲”的卡片。",
      "verdict": "met",
      "evidence": "第1镜明确写明“画面仅展示一张写着‘开讲’的静态卡片”，功能文字作为旁白朗读。"
    },
    {
      "field": "audience",
      "requirement": "刚进入课程页的访客",
      "verdict": "met",
      "evidence": "“开讲”卡片呼应课程入口，旁白直接介绍基础功能，不需要访客具备操作知识。"
    },
    {
      "field": "platform",
      "requirement": "抖音",
      "verdict": "met",
      "evidence": "全稿单镜头、预计4秒，卡片文字仅“开讲”，旁白简短直接，适合短视频快速观看。"
    },
    {
      "field": "style",
      "requirement": "极简",
      "verdict": "met",
      "evidence": "只有一张静态卡片和一句旁白，没有额外场景或装饰性文案。"
    },
    {
      "field": "style",
      "requirement": "信息优先",
      "verdict": "met",
      "evidence": "标题“添加字幕”直接点明主题，旁白从第一句即说明产品支持的功能。"
    }
  ],
  "summary": "全部要求已落实：仅介绍添加字幕，画面为“开讲”卡片，预计4秒。表达有资料支持，节奏合理。",
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
      "evidence": "P01.F1明确支持为视频添加字幕；标题没有增加自动化或效果承诺。"
    },
    {
      "location": "shot:1/visual",
      "text": "画面仅展示一张写着“开讲”的静态卡片；事实块作为旁白朗读。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "整句仅规定卡片画面和旁白安排，不包含产品能力、具体界面或操作步骤声明。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "第1镜预计4.0秒，承载14个旁白单位和“开讲”两字卡片，阅读与聆听负担合理。hold_seconds=0表示没有额外延长，旁白仍有预计播放时间；没有重复事实或明显凑时长。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
