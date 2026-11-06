# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成3镜静音屏脚本，覆盖添加字幕、字幕文字编辑和裁剪片段，关键信息全部上屏，无需旁白。估时24秒，符合25秒目标的22.5—25秒区间。本次保留现稿，无需删改。演示画面为示意；估时不代表实际屏幕阅读时间，成片仍需确认文字可读性。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 添加字幕，裁剪片段

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

画面：静音，无旁白。上方持续显示本镜事实块，大字高对比。下方播放自摄的展位招手画面，叠加示例字幕“欢迎参观”，让观众同时看到画面与字幕；不展示产品界面。

旁白/字幕：剪影练习版支持为视频添加字幕。

来源：P01/P01.F1

预计镜头时长：8.0 秒

### 分镜 2

画面：上方持续显示本镜事实块。下方以两张文字卡依次展示修改前“欢迎参观”和修改后“欢迎来到展位”，随后并列供观众对照；标注“文字修改示意”。不模拟按钮或产品界面。

旁白/字幕：字幕文字可以手动编辑。

来源：P01/P01.F2

预计镜头时长：7.0 秒

### 分镜 3

画面：上方持续显示本镜事实块。下方先播放含走入画面、招手、离开画面的自摄片段，再播放仅保留招手部分的片段，分别标注“裁剪前”和“裁剪后”。标注“片段裁剪示意”，让观众观察保留内容的变化；不展示产品界面。

旁白/字幕：剪影练习版支持裁剪视频片段。

来源：P02/P02.F1

预计镜头时长：9.0 秒

## 审稿备注（不进入视频，不计入时长）

供创作者核对修改与资料缺口，不是经过事实认证的产品介绍。

全部关键信息以屏幕文字呈现，无需声音。事实块是持续展示的屏幕卡，不是旁白；示例文字与素材用于拍摄演示，不代表实际产品界面。三个镜头预设停留共24秒，分别用于阅读、文字对照和片段前后观看；最终以估时检查为准，工具对文字的串行估算不等于实际屏幕阅读时间。

时长要求：22.5–25 秒（接近目标）。

预计总时长：24.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "255c73ec22d056c5b864dac13963360d21c16196b0b7f1b6d2fee0f81c5b3718",
  "passed": true,
  "issues": [],
  "citations": [
    {
      "location": "shot:1/block:1",
      "source_id": "P01",
      "fact_id": "P01.F1",
      "quote": "剪影练习版支持为视频添加字幕。",
      "version": "2026-11-01"
    },
    {
      "location": "shot:2/block:1",
      "source_id": "P01",
      "fact_id": "P01.F2",
      "quote": "字幕文字可以手动编辑。",
      "version": "2026-11-01"
    },
    {
      "location": "shot:3/block:1",
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
      "text": "添加字幕，裁剪片段"
    },
    {
      "location": "shot:1/visual",
      "text": "静音，无旁白。上方持续显示本镜事实块，大字高对比。下方播放自摄的展位招手画面，叠加示例字幕“欢迎参观”，让观众同时看到画面与字幕；不展示产品界面。"
    },
    {
      "location": "shot:2/visual",
      "text": "上方持续显示本镜事实块。下方以两张文字卡依次展示修改前“欢迎参观”和修改后“欢迎来到展位”，随后并列供观众对照；标注“文字修改示意”。不模拟按钮或产品界面。"
    },
    {
      "location": "shot:3/visual",
      "text": "上方持续显示本镜事实块。下方先播放含走入画面、招手、离开画面的自摄片段，再播放仅保留招手部分的片段，分别标注“裁剪前”和“裁剪后”。标注“片段裁剪示意”，让观众观察保留内容的变化；不展示产品界面。"
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
  "scope": "exact_quote_and_brand_checks_only; expression semantics require independent model review"
}
```

## 需求覆盖核对

以下为模型评估，可能漏判或误判，仍需人工确认。

```json
{
  "ok": true,
  "script_hash": "255c73ec22d056c5b864dac13963360d21c16196b0b7f1b6d2fee0f81c5b3718",
  "request_hash": "203dffcdfd4eed16b275a021c2db9cd98912b8eefbfae29e431c56613964e2c2",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "给展位静音屏写工具介绍",
      "verdict": "met",
      "evidence": "第1镜明确“静音，无旁白”，采用“大字高对比”的屏幕事实块，并配合展位招手画面；三个镜头均围绕工具功能展开。"
    },
    {
      "field": "topic",
      "requirement": "添加字幕",
      "verdict": "met",
      "evidence": "第1镜屏幕文字为“剪影练习版支持为视频添加字幕。”，画面叠加示例字幕“欢迎参观”。"
    },
    {
      "field": "topic",
      "requirement": "裁剪片段",
      "verdict": "met",
      "evidence": "第3镜屏幕文字为“剪影练习版支持裁剪视频片段。”，并展示完整片段与仅保留招手部分的前后对比。"
    },
    {
      "field": "topic",
      "requirement": "所有关键信息用屏幕文字表达",
      "verdict": "met",
      "evidence": "三个镜头均明确持续显示事实块，覆盖添加字幕、手动编辑字幕和裁剪片段；对比画面另有“文字修改示意”“裁剪前”“裁剪后”等屏幕标注。"
    },
    {
      "field": "topic",
      "requirement": "不能依赖旁白",
      "verdict": "met",
      "evidence": "第1镜明确“静音，无旁白”；各镜通过持续展示的屏幕文字和示意画面传达信息，无需声音补充。"
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
      "evidence": "第1镜采用大字高对比文字，第2、3镜用文字修改和片段裁剪的直观对比解释功能，无需专业知识即可理解。"
    },
    {
      "field": "platform",
      "requirement": "视频号",
      "verdict": "met",
      "evidence": "标题“添加字幕，裁剪片段”直接说明内容，三个短镜头以屏幕文字和演示传达信息，适合视频号短视频观看。"
    },
    {
      "field": "style",
      "requirement": "静音可读",
      "verdict": "met",
      "evidence": "各镜事实块持续显示，第1镜明确大字高对比；示例字幕及前后对比均有可读文字，不依赖听觉。"
    },
    {
      "field": "style",
      "requirement": "简洁",
      "verdict": "met",
      "evidence": "每镜仅有一句功能事实，分别配合字幕叠加、文字修改和片段裁剪示意，没有冗长旁白或无关内容。"
    }
  ],
  "summary": "当前稿件满足明确需求：3个分镜覆盖添加字幕与裁剪片段，关键信息均以屏幕文字呈现，适合静音观看。表达有资料支持，各镜停留均有阅读或观察任务，节奏合理。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "添加字幕，裁剪片段",
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
      "evidence": "标题涉及的添加字幕与裁剪视频片段两项能力，分别由P01.F1和P02.F1直接支持。"
    },
    {
      "location": "shot:1/visual",
      "text": "静音，无旁白。上方持续显示本镜事实块，大字高对比。下方播放自摄的展位招手画面，叠加示例字幕“欢迎参观”，让观众同时看到画面与字幕；不展示产品界面。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "叠加示例字幕展示的是P01.F1支持的添加字幕能力；静音、高对比文字和展位画面属于拍摄安排，未宣称自动生成字幕或虚构产品界面。"
    },
    {
      "location": "shot:2/visual",
      "text": "上方持续显示本镜事实块。下方以两张文字卡依次展示修改前“欢迎参观”和修改后“欢迎来到展位”，随后并列供观众对照；标注“文字修改示意”。不模拟按钮或产品界面。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "文字修改前后的对照由“字幕文字可以手动编辑”支持；明确标注示意，未添加自动改写能力、按钮名称或操作步骤。"
    },
    {
      "location": "shot:3/visual",
      "text": "上方持续显示本镜事实块。下方先播放含走入画面、招手、离开画面的自摄片段，再播放仅保留招手部分的片段，分别标注“裁剪前”和“裁剪后”。标注“片段裁剪示意”，让观众观察保留内容的变化；不展示产品界面。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P02",
          "fact_id": "P02.F1"
        }
      ],
      "evidence": "保留原片段中招手部分的示意属于P02.F1支持的片段裁剪能力，未声称自动识别动作或自动选择保留内容。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "duration_check给出的三镜预计时长为8秒、7秒、9秒，分别满足对应最低停留时间。第1镜用于阅读一句事实并观察字幕叠加；第2镜用于依次阅读两张文字卡并对照；第3镜用于观看裁剪前后片段。各镜都有明确阅读或观察内容，没有重复同一事实或空镜凑时长。总长24秒，宿主目标区间检查已通过。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
