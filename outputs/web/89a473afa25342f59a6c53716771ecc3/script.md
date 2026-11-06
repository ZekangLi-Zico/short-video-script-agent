# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成两镜大字卡脚本，预计10秒。每卡不超过8个汉字，无旁白，仅用实物剪刀和纸片呈现裁剪功能，并留足远距离阅读时间。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 裁剪视频片段

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

镜头目的：让观众认清产品名称，并建立剪纸的视觉意象。

画面：竖屏固定俯拍，白纸铺满背景。中央纸卡用超大黑字印出“剪影练习版”，实物剪刀静置在纸卡旁。文字保持完整、清晰、静止，不出现人物或软件界面。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–4.0 秒**

屏幕文字：剪影练习版

依据：P02/P02.F1

预计镜头时长：4.0 秒

### 分镜 2

镜头目的：明确产品支持裁剪视频片段，用剪去纸边的动作帮助理解裁剪。

画面：切到印有“支持裁剪视频片段”的宽纸卡，八字分两行居中放大。用定格拍摄让实物剪刀剪去纸卡外侧空白边，纸屑移到两旁；中央文字始终静止、无遮挡。动作结束后保持画面，背景仍仅为白纸。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–6.0 秒**

屏幕文字：支持裁剪
视频片段

依据：P02/P02.F1

预计镜头时长：6.0 秒

预计总时长：10.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "de07b579edf8598cc7ac92d0276e5e3722aa34a066cb3b3c1bac18e38c3395ae",
  "passed": true,
  "issues": [],
  "citations": [
    {
      "location": "shot:1/block:1",
      "source_id": "P02",
      "fact_id": "P02.F1",
      "quote": "剪影练习版支持裁剪视频片段。",
      "version": "2026-11-01",
      "text": "剪影练习版",
      "requires_semantic_review": true
    },
    {
      "location": "shot:2/block:1",
      "source_id": "P02",
      "fact_id": "P02.F1",
      "quote": "剪影练习版支持裁剪视频片段。",
      "version": "2026-11-01",
      "text": "支持裁剪\n视频片段",
      "requires_semantic_review": true
    }
  ],
  "rules_version": "2026-11-03-v1",
  "requires_expression_review": true,
  "expression_slots": [
    {
      "location": "title",
      "text": "裁剪视频片段"
    },
    {
      "location": "shot:1/visual",
      "text": "竖屏固定俯拍，白纸铺满背景。中央纸卡用超大黑字印出“剪影练习版”，实物剪刀静置在纸卡旁。文字保持完整、清晰、静止，不出现人物或软件界面。"
    },
    {
      "location": "shot:1/block:1",
      "text": "剪影练习版"
    },
    {
      "location": "shot:2/visual",
      "text": "切到印有“支持裁剪视频片段”的宽纸卡，八字分两行居中放大。用定格拍摄让实物剪刀剪去纸卡外侧空白边，纸屑移到两旁；中央文字始终静止、无遮挡。动作结束后保持画面，背景仍仅为白纸。"
    },
    {
      "location": "shot:2/block:1",
      "text": "支持裁剪\n视频片段"
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
  "script_hash": "de07b579edf8598cc7ac92d0276e5e3722aa34a066cb3b3c1bac18e38c3395ae",
  "request_hash": "d5089772cb159a82a06b38fc2ccb255563f1443a217583fe30ed63215b43601c",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "介绍裁剪片段",
      "verdict": "met",
      "evidence": "第2镜屏幕文字为“支持裁剪\n视频片段”，明确介绍裁剪功能。"
    },
    {
      "field": "topic",
      "requirement": "只用大字屏幕卡片",
      "verdict": "met",
      "evidence": "两镜文案均为screen；第1镜使用“超大黑字”纸卡，第2镜将八字分两行居中放大，信息均通过大字卡传达。"
    },
    {
      "field": "topic",
      "requirement": "不使用旁白",
      "verdict": "met",
      "evidence": "所有文案块均为screen，无voice或both；两镜voice_seconds均为0。"
    },
    {
      "field": "topic",
      "requirement": "每张卡最多8个汉字",
      "verdict": "met",
      "evidence": "第1张“剪影练习版”为5个汉字；第2张“支持裁剪\\n视频片段”去除换行后为8个汉字。"
    },
    {
      "field": "topic",
      "requirement": "观众应能读清楚",
      "verdict": "met",
      "evidence": "第1镜黑字白底、文字静止，展示4秒；第2镜文字放大、静止且无遮挡，展示6秒。均超过宿主估算的对应阅读时间。"
    },
    {
      "field": "topic",
      "requirement": "画面只用实物剪刀和纸片意象",
      "verdict": "met",
      "evidence": "第1镜仅安排白纸、纸卡和实物剪刀；第2镜仅安排纸卡、剪刀、纸屑及白纸背景，未出现范围外画面元素。"
    },
    {
      "field": "audience",
      "requirement": "门店远距离观看者",
      "verdict": "met",
      "evidence": "两张卡仅5字和8字，采用超大字或分行放大，文字保持稳定并留出阅读时间，适合远距离观看。"
    },
    {
      "field": "platform",
      "requirement": "视频号",
      "verdict": "met",
      "evidence": "采用竖屏、两镜短视频形式，预计总长10秒；屏幕卡片可独立传达信息，平台适配合理。"
    },
    {
      "field": "style",
      "requirement": "短字卡",
      "verdict": "met",
      "evidence": "两张卡分别为“剪影练习版”和“支持裁剪\\n视频片段”，没有长句或额外说明。"
    },
    {
      "field": "style",
      "requirement": "清晰",
      "verdict": "met",
      "evidence": "第1镜明确黑字白底、固定俯拍；第2镜文字居中放大且始终无遮挡，功能表述直接。"
    }
  ],
  "summary": "需求均已落实：两张大字卡分别为5字和8字，无旁白，画面仅使用剪刀和纸片意象。公开功能表述有资料支持，预计10秒，符合20秒上限，阅读与动作停留合理。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "裁剪视频片段",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P02",
          "fact_id": "P02.F1"
        }
      ],
      "evidence": "P02.F1明确说明产品支持裁剪视频片段，标题未增加能力或效果。"
    },
    {
      "location": "shot:1/visual",
      "text": "竖屏固定俯拍，白纸铺满背景。中央纸卡用超大黑字印出“剪影练习版”，实物剪刀静置在纸卡旁。文字保持完整、清晰、静止，不出现人物或软件界面。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅安排构图、实物道具、产品名称纸卡和文字可见性，没有产品能力或效果承诺。"
    },
    {
      "location": "shot:1/block:1",
      "text": "剪影练习版",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P02",
          "fact_id": "P02.F1"
        }
      ],
      "evidence": "名称直接取自原块标注的P02.F1原文“剪影练习版支持裁剪视频片段。”，没有新增含义。"
    },
    {
      "location": "shot:2/visual",
      "text": "切到印有“支持裁剪视频片段”的宽纸卡，八字分两行居中放大。用定格拍摄让实物剪刀剪去纸卡外侧空白边，纸屑移到两旁；中央文字始终静止、无遮挡。动作结束后保持画面，背景仍仅为白纸。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P02",
          "fact_id": "P02.F1"
        }
      ],
      "evidence": "纸卡中的裁剪能力由P02.F1支持；剪纸为拍摄意象，未声称自动操作，也未虚构软件界面或操作步骤。"
    },
    {
      "location": "shot:2/block:1",
      "text": "支持裁剪\n视频片段",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P02",
          "fact_id": "P02.F1"
        }
      ],
      "evidence": "与原块标注的P02.F1含义一致，仅省略上一镜已展示的产品名称并加入换行。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "第1镜实际估算4秒，用于远距离辨认5字名称及剪刀纸卡意象；第2镜6秒，用于阅读8字功能卡、观察剪去空白边及动作后停留。两镜分别满足4秒和6秒最低停留，内容没有重复凑时长；宿主总长估算10秒并已通过20秒上限检查。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
