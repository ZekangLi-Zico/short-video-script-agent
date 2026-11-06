# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成3镜头静音脚本，覆盖添加字幕、字幕文字编辑及裁剪片段，关键信息全部上屏，不依赖旁白。保留当前稿，无需删改。估时23秒，符合25秒目标的22.5—25秒范围；实际屏幕阅读节奏仍需成片确认。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 剪影练习版：添加字幕与裁剪片段

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

画面：全片静音，不设旁白。顶部显示标题；大字事实卡逐字显示本镜头全部block文字，并持续保留。旁边用展位日常素材演示从无字幕画面切换为带“今天逛展”字幕的画面，标注“演示示意”。不展示软件界面。

旁白/字幕：剪影练习版支持为视频添加字幕。

来源：P01/P01.F1

预计镜头时长：8.0 秒

### 分镜 2

画面：延续上一镜头的展位素材，大字事实卡逐字显示本镜头全部block文字，并持续保留。示例字幕先显示“今天逛展”，再变为“展位见闻”，留出阅读修改前后文字的时间；标注“文字修改示意”，不展示按钮或操作界面。

旁白/字幕：字幕文字可以手动编辑。

来源：P01/P01.F2

预计镜头时长：6.0 秒

### 分镜 3

画面：大字事实卡逐字显示本镜头全部block文字，并持续保留。用同一段展位素材展示裁剪示意：先播放包含开头、主体和结尾的原始片段，再播放仅保留中间主体的片段；分别显示“原始片段”“裁剪后示意”。不展示软件界面，结尾保留事实卡供路过观众阅读。

旁白/字幕：剪影练习版支持裁剪视频片段。

来源：P02/P02.F1

预计镜头时长：9.0 秒

时长要求：22.5–25 秒（接近目标）。

预计总时长：23.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "4cec2fb0511534273230593468f0546b56e59ac5542124618244babda9643acd",
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
      "text": "剪影练习版：添加字幕与裁剪片段"
    },
    {
      "location": "shot:1/visual",
      "text": "全片静音，不设旁白。顶部显示标题；大字事实卡逐字显示本镜头全部block文字，并持续保留。旁边用展位日常素材演示从无字幕画面切换为带“今天逛展”字幕的画面，标注“演示示意”。不展示软件界面。"
    },
    {
      "location": "shot:2/visual",
      "text": "延续上一镜头的展位素材，大字事实卡逐字显示本镜头全部block文字，并持续保留。示例字幕先显示“今天逛展”，再变为“展位见闻”，留出阅读修改前后文字的时间；标注“文字修改示意”，不展示按钮或操作界面。"
    },
    {
      "location": "shot:3/visual",
      "text": "大字事实卡逐字显示本镜头全部block文字，并持续保留。用同一段展位素材展示裁剪示意：先播放包含开头、主体和结尾的原始片段，再播放仅保留中间主体的片段；分别显示“原始片段”“裁剪后示意”。不展示软件界面，结尾保留事实卡供路过观众阅读。"
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
  "script_hash": "4cec2fb0511534273230593468f0546b56e59ac5542124618244babda9643acd",
  "request_hash": "203dffcdfd4eed16b275a021c2db9cd98912b8eefbfae29e431c56613964e2c2",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "给展位静音屏写工具介绍",
      "verdict": "met",
      "evidence": "镜头1明确“全片静音，不设旁白”，三镜头均以展位素材配大字事实卡介绍工具功能。"
    },
    {
      "field": "topic",
      "requirement": "添加字幕",
      "verdict": "met",
      "evidence": "镜头1上屏“剪影练习版支持为视频添加字幕。”，并展示无字幕画面切换为带“今天逛展”字幕的画面。"
    },
    {
      "field": "topic",
      "requirement": "裁剪片段",
      "verdict": "met",
      "evidence": "镜头3上屏“剪影练习版支持裁剪视频片段。”，并展示原始片段与仅保留中间主体的裁剪示意。"
    },
    {
      "field": "topic",
      "requirement": "所有关键信息用屏幕文字表达",
      "verdict": "met",
      "evidence": "三个镜头均要求“大字事实卡逐字显示本镜头全部block文字，并持续保留”；镜头1另显示标题，功能信息均明确上屏。"
    },
    {
      "field": "topic",
      "requirement": "不能依赖旁白",
      "verdict": "met",
      "evidence": "镜头1规定“全片静音，不设旁白”，字幕添加、手动编辑与片段裁剪均通过事实卡和画面示意表达。"
    },
    {
      "field": "topic",
      "requirement": "分镜不超过四个",
      "verdict": "met",
      "evidence": "当前稿件共3个镜头。"
    },
    {
      "field": "audience",
      "requirement": "路过展位的普通观众",
      "verdict": "met",
      "evidence": "三镜头使用大字、简短功能说明和直观前后对比，无需专业背景；镜头3明确“结尾保留事实卡供路过观众阅读”。"
    },
    {
      "field": "platform",
      "requirement": "视频号",
      "verdict": "met",
      "evidence": "三镜头构成简短完整的工具介绍，以屏幕文字配功能示意，可直接静音理解；宿主估算总长23秒，适合短视频观看。"
    },
    {
      "field": "style",
      "requirement": "静音可读",
      "verdict": "met",
      "evidence": "全片不设旁白，所有事实卡均以大字显示并保留，三镜头分别安排8秒、6秒、9秒展示。"
    },
    {
      "field": "style",
      "requirement": "简洁",
      "verdict": "met",
      "evidence": "每镜仅一条简短功能事实，配对应示意；共3镜头，没有冗长铺垫或重复口号。"
    }
  ],
  "summary": "各项需求均已落实：三镜头静音介绍字幕添加与片段裁剪，关键信息全部上屏，表达有资料支持，展示节奏合理。宿主时长检查通过。",
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
      "evidence": "标题中的添加字幕和裁剪片段分别由P01.F1与P02.F1直接支持，没有附加效果承诺。"
    },
    {
      "location": "shot:1/visual",
      "text": "全片静音，不设旁白。顶部显示标题；大字事实卡逐字显示本镜头全部block文字，并持续保留。旁边用展位日常素材演示从无字幕画面切换为带“今天逛展”字幕的画面，标注“演示示意”。不展示软件界面。",
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
      "evidence": "添加字幕的事实卡和画面示意由P01.F1支持；顶部标题同时包含裁剪片段，由P02.F1支持。其余为静音、排版及拍摄安排，未虚构产品界面或操作步骤。"
    },
    {
      "location": "shot:2/visual",
      "text": "延续上一镜头的展位素材，大字事实卡逐字显示本镜头全部block文字，并持续保留。示例字幕先显示“今天逛展”，再变为“展位见闻”，留出阅读修改前后文字的时间；标注“文字修改示意”，不展示按钮或操作界面。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "字幕文字前后变化对应P01.F2“字幕文字可以手动编辑。”，并明确标为修改示意，没有宣称自动改写或虚构按钮。"
    },
    {
      "location": "shot:3/visual",
      "text": "大字事实卡逐字显示本镜头全部block文字，并持续保留。用同一段展位素材展示裁剪示意：先播放包含开头、主体和结尾的原始片段，再播放仅保留中间主体的片段；分别显示“原始片段”“裁剪后示意”。不展示软件界面，结尾保留事实卡供路过观众阅读。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P02",
          "fact_id": "P02.F1"
        }
      ],
      "evidence": "去掉片段开头和结尾、保留中间主体的示意属于P02.F1支持的片段裁剪，没有声称自动识别主体或其他未证实能力。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "宿主预计镜头1为8秒，承载标题、简短事实卡及字幕添加前后对比；镜头2为6秒，承载手动编辑说明与两组字幕对比；镜头3为9秒，承载裁剪说明、原始片段及裁剪后片段。均达到各自最低展示时间，停留有明确阅读和观察任务，没有重复事实或空镜凑时长。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
