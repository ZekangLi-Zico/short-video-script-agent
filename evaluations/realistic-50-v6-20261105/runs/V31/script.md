# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成3镜头脚本，预计16秒。全程无旁白，三张大字卡均不超过8个汉字，仅用实物剪刀与纸片呈现裁剪概念；全部检查通过。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 用剪刀纸片看懂片段裁剪

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

镜头目的：明确介绍视频片段裁剪功能。

画面：纯色桌面上摆一条长纸片与一把实物剪刀；画面上方居中显示高对比大字，纸片和剪刀保持静止，让观众读清文字。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–5.0 秒**

屏幕文字：支持裁剪视频片段

依据：P02/P02.F1

预计镜头时长：5.0 秒

### 分镜 2

镜头目的：以剪纸动作表现裁剪片段的概念。

画面：近景只呈现实物剪刀与长纸片。剪刀先剪下纸片左端，再剪下右端；大字卡固定在画面上方，剪切动作在下方完成。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–6.0 秒**

屏幕文字：像剪一段纸

预计镜头时长：6.0 秒

### 分镜 3

镜头目的：展示裁剪后的纸段，让观众理解留下片段的结果。

画面：剪刀合拢放在一侧，裁下的两端移至画面边缘，中间纸段独立居中；上方显示大字卡，保持构图供观众观察。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–5.0 秒**

屏幕文字：留下这一段

预计镜头时长：5.0 秒

预计总时长：16.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "f098092234edf6e96ea96b62b606485ad8c89bc15f2ef17045f7b225ae40c006",
  "passed": true,
  "issues": [],
  "citations": [
    {
      "location": "shot:1/block:1",
      "source_id": "P02",
      "fact_id": "P02.F1",
      "quote": "剪影练习版支持裁剪视频片段。",
      "version": "2026-11-01",
      "text": "支持裁剪视频片段",
      "requires_semantic_review": true
    }
  ],
  "rules_version": "2026-11-03-v1",
  "requires_expression_review": true,
  "expression_slots": [
    {
      "location": "title",
      "text": "用剪刀纸片看懂片段裁剪"
    },
    {
      "location": "shot:1/visual",
      "text": "纯色桌面上摆一条长纸片与一把实物剪刀；画面上方居中显示高对比大字，纸片和剪刀保持静止，让观众读清文字。"
    },
    {
      "location": "shot:1/block:1",
      "text": "支持裁剪视频片段"
    },
    {
      "location": "shot:2/visual",
      "text": "近景只呈现实物剪刀与长纸片。剪刀先剪下纸片左端，再剪下右端；大字卡固定在画面上方，剪切动作在下方完成。"
    },
    {
      "location": "shot:2/block:1",
      "text": "像剪一段纸"
    },
    {
      "location": "shot:3/visual",
      "text": "剪刀合拢放在一侧，裁下的两端移至画面边缘，中间纸段独立居中；上方显示大字卡，保持构图供观众观察。"
    },
    {
      "location": "shot:3/block:1",
      "text": "留下这一段"
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
  "script_hash": "f098092234edf6e96ea96b62b606485ad8c89bc15f2ef17045f7b225ae40c006",
  "request_hash": "d5089772cb159a82a06b38fc2ccb255563f1443a217583fe30ed63215b43601c",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "介绍裁剪片段",
      "verdict": "met",
      "evidence": "第1镜明确显示“支持裁剪视频片段”，第2—3镜用剪纸及保留中段呈现裁剪概念。"
    },
    {
      "field": "topic",
      "requirement": "只用大字屏幕卡片",
      "verdict": "met",
      "evidence": "全部文案块均为screen，各镜画面明确安排大字卡。"
    },
    {
      "field": "topic",
      "requirement": "不使用旁白",
      "verdict": "met",
      "evidence": "三个文案块均无voice或both，时长检查各镜voice_seconds均为0。"
    },
    {
      "field": "topic",
      "requirement": "每张卡最多8个汉字",
      "verdict": "met",
      "evidence": "三张实际屏幕卡依次为“支持裁剪视频片段”8字、“像剪一段纸”5字、“留下这一段”5字。"
    },
    {
      "field": "topic",
      "requirement": "观众应能读清楚",
      "verdict": "met",
      "evidence": "大字卡分别展示5、6、5秒，第1镜明确高对比，后两镜固定文字位置供阅读。"
    },
    {
      "field": "topic",
      "requirement": "画面只用实物剪刀和纸片意象",
      "verdict": "met",
      "evidence": "三镜均围绕实物剪刀、长纸片及裁后纸段展开，未加入产品界面或其他意象。"
    },
    {
      "field": "audience",
      "requirement": "门店远距离观看者",
      "verdict": "met",
      "evidence": "高对比大字、固定卡片位置及每卡至少5秒停留适合远距离阅读，无需听取旁白。"
    },
    {
      "field": "platform",
      "requirement": "视频号",
      "verdict": "met",
      "evidence": "16秒三镜以简短中文卡片及直观动作传递单一功能，适合短视频观看。"
    },
    {
      "field": "style",
      "requirement": "短字卡，清晰",
      "verdict": "met",
      "evidence": "每卡5—8字，画面按长纸片、剪两端、保留中段的顺序清晰展开。"
    }
  ],
  "summary": "当前稿满足需求，三张屏幕卡均不超过8个汉字，无旁白，且仅使用剪刀与纸片意象。功能声明有资料支持，预计16秒，阅读与动作停留合理。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "用剪刀纸片看懂片段裁剪",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "标题说明视频的讲解方式，没有新增产品能力或性能承诺。"
    },
    {
      "location": "shot:1/visual",
      "text": "纯色桌面上摆一条长纸片与一把实物剪刀；画面上方居中显示高对比大字，纸片和剪刀保持静止，让观众读清文字。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅描述实物摆放、字卡样式及阅读安排，没有产品操作或效果声明。"
    },
    {
      "location": "shot:1/block:1",
      "text": "支持裁剪视频片段",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P02",
          "fact_id": "P02.F1"
        }
      ],
      "evidence": "原文“剪影练习版支持裁剪视频片段。”直接支持此省略产品名的表述。"
    },
    {
      "location": "shot:2/visual",
      "text": "近景只呈现实物剪刀与长纸片。剪刀先剪下纸片左端，再剪下右端；大字卡固定在画面上方，剪切动作在下方完成。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "实物剪纸动作属于概念示意，未声称产品具有对应按钮或操作流程。"
    },
    {
      "location": "shot:2/block:1",
      "text": "像剪一段纸",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "结合实物剪纸画面属于比喻，没有新增可验证的产品承诺。"
    },
    {
      "location": "shot:3/visual",
      "text": "剪刀合拢放在一侧，裁下的两端移至画面边缘，中间纸段独立居中；上方显示大字卡，保持构图供观众观察。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅安排纸段与剪刀的位置及观察停留，没有虚构产品界面或自动化能力。"
    },
    {
      "location": "shot:3/block:1",
      "text": "留下这一段",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "文字指向画面中保留的纸段，属于示意说明，没有额外功能声明。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "实际估算三镜为5、6、5秒：首镜供远距离读取8字卡，第二镜完成两次剪切，第三镜供观察保留纸段；均有明确阅读或动作内容支撑，总长16秒通过20秒上限检查。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
