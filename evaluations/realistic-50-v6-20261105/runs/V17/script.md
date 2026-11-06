# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成3镜静音展位屏脚本，预计23.5秒。添加字幕与裁剪片段均有直观演示，关键信息全部上屏，无需旁白；时长、规则和需求检查均通过。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 剪影练习版：添加字幕与裁剪片段

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

镜头目的：明确产品名称及本次展示的两项功能。

画面：展位屏展示一段人物挥手的视频预览，画面上方固定产品名称，下方依次呈现两项功能文字。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–3.5 秒**

屏幕文字：剪影练习版

依据：P01/P01.F1

屏幕文字：为视频添加字幕

依据：P01/P01.F1

**第 2 拍 · 镜内 3.5–5.5 秒**

屏幕文字：裁剪视频片段

依据：P02/P02.F1

镜头末尾保持画面：5.5–6.0 秒（保留最后一拍屏幕文字）

预计镜头时长：6.0 秒

### 分镜 2

镜头目的：通过同一段画面的字幕出现过程，直观展示添加字幕。

画面：同一段人物挥手画面先无字幕播放，再展示添加字幕后的版本，底部出现示例字幕“欢迎来逛我们的展位”。功能说明固定在上方，示例字幕与说明分区显示。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–3.0 秒**

屏幕文字：为视频添加字幕

依据：P01/P01.F1

**第 2 拍 · 镜内 3.0–8.0 秒**

屏幕文字：欢迎来逛我们的展位

预计镜头时长：8.0 秒

### 分镜 3

镜头目的：展示裁剪前后片段的区别，让观众理解保留所需片段的用途。

画面：用素材示意条展示“空画面—人物挥手—空画面”，随后两端灰显，仅中间挥手段高亮；播放裁剪后的挥手片段。全程标注示意，不虚构产品按钮或操作路径。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–4.0 秒**

屏幕文字：裁剪视频片段

依据：P02/P02.F1

**第 2 拍 · 镜内 4.0–9.5 秒**

屏幕文字：演示：保留人物挥手这一段

预计镜头时长：9.5 秒

时长要求：22.5–25 秒（接近目标）。

预计总时长：23.5 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "14790eac25751e754704cd89597e6d4a133ecf747e6ca330348e6be3e976c0f1",
  "passed": true,
  "issues": [],
  "citations": [
    {
      "location": "shot:1/block:1",
      "source_id": "P01",
      "fact_id": "P01.F1",
      "quote": "剪影练习版支持为视频添加字幕。",
      "version": "2026-11-01",
      "text": "剪影练习版",
      "requires_semantic_review": true
    },
    {
      "location": "shot:1/block:2",
      "source_id": "P01",
      "fact_id": "P01.F1",
      "quote": "剪影练习版支持为视频添加字幕。",
      "version": "2026-11-01",
      "text": "为视频添加字幕",
      "requires_semantic_review": true
    },
    {
      "location": "shot:1/block:3",
      "source_id": "P02",
      "fact_id": "P02.F1",
      "quote": "剪影练习版支持裁剪视频片段。",
      "version": "2026-11-01",
      "text": "裁剪视频片段",
      "requires_semantic_review": true
    },
    {
      "location": "shot:2/block:1",
      "source_id": "P01",
      "fact_id": "P01.F1",
      "quote": "剪影练习版支持为视频添加字幕。",
      "version": "2026-11-01",
      "text": "为视频添加字幕",
      "requires_semantic_review": true
    },
    {
      "location": "shot:3/block:1",
      "source_id": "P02",
      "fact_id": "P02.F1",
      "quote": "剪影练习版支持裁剪视频片段。",
      "version": "2026-11-01",
      "text": "裁剪视频片段",
      "requires_semantic_review": true
    }
  ],
  "rules_version": "2026-11-03-v1",
  "requires_expression_review": true,
  "expression_slots": [
    {
      "location": "title",
      "text": "剪影练习版：添加字幕与裁剪片段"
    },
    {
      "location": "shot:1/visual",
      "text": "展位屏展示一段人物挥手的视频预览，画面上方固定产品名称，下方依次呈现两项功能文字。"
    },
    {
      "location": "shot:1/block:1",
      "text": "剪影练习版"
    },
    {
      "location": "shot:1/block:2",
      "text": "为视频添加字幕"
    },
    {
      "location": "shot:1/block:3",
      "text": "裁剪视频片段"
    },
    {
      "location": "shot:2/visual",
      "text": "同一段人物挥手画面先无字幕播放，再展示添加字幕后的版本，底部出现示例字幕“欢迎来逛我们的展位”。功能说明固定在上方，示例字幕与说明分区显示。"
    },
    {
      "location": "shot:2/block:1",
      "text": "为视频添加字幕"
    },
    {
      "location": "shot:2/block:2",
      "text": "欢迎来逛我们的展位"
    },
    {
      "location": "shot:3/visual",
      "text": "用素材示意条展示“空画面—人物挥手—空画面”，随后两端灰显，仅中间挥手段高亮；播放裁剪后的挥手片段。全程标注示意，不虚构产品按钮或操作路径。"
    },
    {
      "location": "shot:3/block:1",
      "text": "裁剪视频片段"
    },
    {
      "location": "shot:3/block:2",
      "text": "演示：保留人物挥手这一段"
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
  "script_hash": "14790eac25751e754704cd89597e6d4a133ecf747e6ca330348e6be3e976c0f1",
  "request_hash": "203dffcdfd4eed16b275a021c2db9cd98912b8eefbfae29e431c56613964e2c2",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "给展位静音屏写工具介绍",
      "verdict": "met",
      "evidence": "第1镜明确展位屏和产品名称，第2、3镜用字幕及裁剪示意介绍工具。"
    },
    {
      "field": "topic",
      "requirement": "添加字幕",
      "verdict": "met",
      "evidence": "第2镜显示“为视频添加字幕”，并展示添加示例字幕前后的画面。"
    },
    {
      "field": "topic",
      "requirement": "裁剪片段",
      "verdict": "met",
      "evidence": "第3镜显示“裁剪视频片段”，用两端灰显和中间片段播放展示裁剪结果。"
    },
    {
      "field": "topic",
      "requirement": "所有关键信息用屏幕文字表达",
      "verdict": "met",
      "evidence": "产品名称、两项功能及演示说明均通过screen文案呈现。"
    },
    {
      "field": "topic",
      "requirement": "不能依赖旁白",
      "verdict": "met",
      "evidence": "全部文案块均为screen，没有voice或both内容。"
    },
    {
      "field": "topic",
      "requirement": "分镜不超过四个",
      "verdict": "met",
      "evidence": "当前稿件共3个分镜。"
    },
    {
      "field": "audience",
      "requirement": "路过展位的普通观众",
      "verdict": "met",
      "evidence": "使用简短功能名称及人物挥手素材的前后对比，无需专业知识即可理解。"
    },
    {
      "field": "platform",
      "requirement": "视频号",
      "verdict": "met",
      "evidence": "3镜短视频以直观演示传递信息，未出现与视频号适配冲突的内容。"
    },
    {
      "field": "style",
      "requirement": "静音可读",
      "verdict": "met",
      "evidence": "全部信息通过屏幕文字展示，各拍预计展示时间均覆盖宿主估算的阅读时间。"
    },
    {
      "field": "style",
      "requirement": "简洁",
      "verdict": "met",
      "evidence": "仅用产品名称、两项功能短句和具体演示说明完成介绍，没有冗长解释。"
    }
  ],
  "summary": "当前稿件满足需求，两项功能均有屏幕文字与直观演示，静音观看也能理解。公开能力声明均有资料支持，预计23.5秒，节奏合理。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "剪影练习版：添加字幕与裁剪片段",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        },
        {
          "source_id": "P02",
          "fact_id": "P02.F1"
        }
      ],
      "evidence": "两条原文分别支持该产品添加字幕和裁剪视频片段。"
    },
    {
      "location": "shot:1/visual",
      "text": "展位屏展示一段人物挥手的视频预览，画面上方固定产品名称，下方依次呈现两项功能文字。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "这是展位视频的画面及文字排布安排，没有声称具体产品界面或额外能力。"
    },
    {
      "location": "shot:1/block:1",
      "text": "剪影练习版",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "名称与所标注原文中的产品名称一致。"
    },
    {
      "location": "shot:1/block:2",
      "text": "为视频添加字幕",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "原文明确支持为视频添加字幕，没有新增自动化或效果承诺。"
    },
    {
      "location": "shot:1/block:3",
      "text": "裁剪视频片段",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P02",
          "fact_id": "P02.F1"
        }
      ],
      "evidence": "原文明确支持裁剪视频片段。"
    },
    {
      "location": "shot:2/visual",
      "text": "同一段人物挥手画面先无字幕播放，再展示添加字幕后的版本，底部出现示例字幕“欢迎来逛我们的展位”。功能说明固定在上方，示例字幕与说明分区显示。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "前后画面只演示资料支持的添加字幕能力，分区属于视频编排且未虚构操作步骤。"
    },
    {
      "location": "shot:2/block:1",
      "text": "为视频添加字幕",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "与所标注原文的添加字幕能力一致。"
    },
    {
      "location": "shot:2/block:2",
      "text": "欢迎来逛我们的展位",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "这是示例字幕和邀请语，不含产品能力或效果承诺。"
    },
    {
      "location": "shot:3/visual",
      "text": "用素材示意条展示“空画面—人物挥手—空画面”，随后两端灰显，仅中间挥手段高亮；播放裁剪后的挥手片段。全程标注示意，不虚构产品按钮或操作路径。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P02",
          "fact_id": "P02.F1"
        }
      ],
      "evidence": "示意条及结果播放演示裁剪片段能力，未声称自动识别或具体产品UI。"
    },
    {
      "location": "shot:3/block:1",
      "text": "裁剪视频片段",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P02",
          "fact_id": "P02.F1"
        }
      ],
      "evidence": "与所标注原文的裁剪视频片段能力一致。"
    },
    {
      "location": "shot:3/block:2",
      "text": "演示：保留人物挥手这一段",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P02",
          "fact_id": "P02.F1"
        }
      ],
      "evidence": "保留指定素材片段是裁剪能力的具体演示，没有增加自动选段承诺。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "第1镜6秒支撑名称和功能分拍阅读；第2镜8秒用于字幕前后对比；第3镜9.5秒用于示意条变化和裁剪结果播放，各拍均有文字或观察任务，非空镜凑时长。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
