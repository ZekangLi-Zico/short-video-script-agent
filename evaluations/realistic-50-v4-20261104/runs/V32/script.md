# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成三个分镜，用笔记本电脑、字幕示意卡和讲义夹介绍字幕添加与手动改字。各镜停留8、8、7秒，预计总长23秒，满足每镜至少5秒及接近25秒的要求。当前稿无需删改，三项检查均通过。改字画面为纸卡示意，时长为估算值。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 字幕，让表达被看见

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

画面：笔记本电脑前，教师将写着“今天学习记录数据”的纸条放在桌上。镜头缓慢靠近纸条，留出阅读时间；不展示软件操作界面。下列文字作为旁白依次朗读。

旁白/字幕：备课时，先准备一句讲解。剪影练习版支持为视频添加字幕。

来源：P01/P01.F1

预计镜头时长：8.0 秒

### 分镜 2

画面：字幕示意卡特写：纸卡写着“今天学习记录数句”。教师用笔圈出“句”，划去后写上“据”，随后停留展示修正结果。这是纸卡改字示意。下列文字作为旁白依次朗读。

旁白/字幕：字幕文字可以手动编辑。示意卡上，把“数句”改成“数据”。

来源：P01/P01.F2

预计镜头时长：8.0 秒

### 分镜 3

画面：教师翻开讲义夹，其中的例句为“今天学习记录数据”。把修正后的字幕示意卡放在讲义旁，手指从左到右逐字对照，最后停在两处一致的“数据”上。下列文字作为旁白朗读。

旁白/字幕：翻开讲义夹，读完这句讲解，再指着字幕卡逐字核对。

来源：

预计镜头时长：7.0 秒

时长要求：22.5–25 秒（接近目标）。

预计总时长：23.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "5004eda13d10f3b11d3f3045a6b5099e9c8aa04286bb84423e8bb7d2d8248957",
  "passed": true,
  "issues": [],
  "citations": [
    {
      "location": "shot:1/block:2",
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
      "text": "笔记本电脑前，教师将写着“今天学习记录数据”的纸条放在桌上。镜头缓慢靠近纸条，留出阅读时间；不展示软件操作界面。下列文字作为旁白依次朗读。"
    },
    {
      "location": "shot:1/block:1",
      "text": "备课时，先准备一句讲解。"
    },
    {
      "location": "shot:2/visual",
      "text": "字幕示意卡特写：纸卡写着“今天学习记录数句”。教师用笔圈出“句”，划去后写上“据”，随后停留展示修正结果。这是纸卡改字示意。下列文字作为旁白依次朗读。"
    },
    {
      "location": "shot:2/block:2",
      "text": "示意卡上，把“数句”改成“数据”。"
    },
    {
      "location": "shot:3/visual",
      "text": "教师翻开讲义夹，其中的例句为“今天学习记录数据”。把修正后的字幕示意卡放在讲义旁，手指从左到右逐字对照，最后停在两处一致的“数据”上。下列文字作为旁白朗读。"
    },
    {
      "location": "shot:3/block:1",
      "text": "翻开讲义夹，读完这句讲解，再指着字幕卡逐字核对。"
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
  "script_hash": "5004eda13d10f3b11d3f3045a6b5099e9c8aa04286bb84423e8bb7d2d8248957",
  "request_hash": "5a8a440420139279ec1553d5df17e98f299a81d8749d3f199cabda7f4dd353a5",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "用三个分镜",
      "verdict": "met",
      "evidence": "稿件共3个分镜，依次呈现准备讲解、改字示意、对照讲义核对。"
    },
    {
      "field": "topic",
      "requirement": "字幕添加",
      "verdict": "met",
      "evidence": "分镜1旁白明确介绍：“剪影练习版支持为视频添加字幕。”rules_check已核对P01.F1并通过。"
    },
    {
      "field": "topic",
      "requirement": "手动改字",
      "verdict": "met",
      "evidence": "分镜2旁白说明“字幕文字可以手动编辑”，并用纸卡展示将“数句”改成“数据”；能力文案已由P01.F2支持。"
    },
    {
      "field": "topic",
      "requirement": "每个镜头至少停留5秒",
      "verdict": "met",
      "evidence": "三个分镜的hold_seconds分别为8、8、7秒；duration_check中的预计时长也分别为8、8、7秒，均不少于5秒。"
    },
    {
      "field": "topic",
      "requirement": "笔记本",
      "verdict": "met",
      "evidence": "分镜1画面明确为“笔记本电脑前”，教师在桌上放置讲解纸条。"
    },
    {
      "field": "topic",
      "requirement": "字幕示意卡",
      "verdict": "met",
      "evidence": "分镜2以“字幕示意卡特写”展示改字，分镜3继续使用修正后的字幕示意卡核对文字。"
    },
    {
      "field": "topic",
      "requirement": "讲义夹",
      "verdict": "met",
      "evidence": "分镜3明确安排“教师翻开讲义夹”，并将字幕卡放在讲义旁逐字对照。"
    },
    {
      "field": "topic",
      "requirement": "目标接近25秒",
      "verdict": "met",
      "evidence": "duration_check预计总长23秒，位于宿主给定的22.5—25秒目标区间内，passed=true。"
    },
    {
      "field": "audience",
      "requirement": "初次编辑课程视频的教师",
      "verdict": "met",
      "evidence": "教师备课、准备讲解、对照讲义等画面贴合课程视频场景；用直白旁白和纸卡改字示意介绍基础功能，便于初次编辑者理解。"
    },
    {
      "field": "platform",
      "requirement": "B站",
      "verdict": "met",
      "evidence": "三镜组成完整的短篇教学内容，配有逐镜旁白和可阅读的文字示意，适合作为B站课程视频编辑入门短视频。"
    },
    {
      "field": "style",
      "requirement": "慢节奏",
      "verdict": "met",
      "evidence": "每镜停留7—8秒；分镜1缓慢靠近纸条，分镜2停留展示改字结果，分镜3逐字对照，均有明确的观察或动作安排。"
    },
    {
      "field": "style",
      "requirement": "明确",
      "verdict": "met",
      "evidence": "旁白直接说明字幕添加和手动编辑两项功能；改字示例明确到“句”改成“据”，且画面标明是纸卡示意。"
    }
  ],
  "summary": "需求均已落实：三个分镜覆盖两项功能及指定场景，每镜至少停留5秒，预计23秒且通过目标时长检查。表达无未获支持的产品承诺，节奏有具体画面动作支撑。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "字幕，让表达被看见",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "标题是对字幕作用的修辞表达，未承诺具体产品能力、性能或传播效果。"
    },
    {
      "location": "shot:1/visual",
      "text": "笔记本电脑前，教师将写着“今天学习记录数据”的纸条放在桌上。镜头缓慢靠近纸条，留出阅读时间；不展示软件操作界面。下列文字作为旁白依次朗读。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "内容均为教师场景、纸条文字、运镜和旁白安排，没有展示或声称产品操作流程。"
    },
    {
      "location": "shot:1/block:1",
      "text": "备课时，先准备一句讲解。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "描述备课准备行为，不涉及产品能力或效果承诺。"
    },
    {
      "location": "shot:2/visual",
      "text": "字幕示意卡特写：纸卡写着“今天学习记录数句”。教师用笔圈出“句”，划去后写上“据”，随后停留展示修正结果。这是纸卡改字示意。下列文字作为旁白依次朗读。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "明确是教师用笔修改纸卡的拍摄示意，没有将纸卡动作描述为软件按钮、界面或自动工作流。"
    },
    {
      "location": "shot:2/block:2",
      "text": "示意卡上，把“数句”改成“数据”。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅说明示意卡上的文字修改，不新增产品功能声明。"
    },
    {
      "location": "shot:3/visual",
      "text": "教师翻开讲义夹，其中的例句为“今天学习记录数据”。把修正后的字幕示意卡放在讲义旁，手指从左到右逐字对照，最后停在两处一致的“数据”上。下列文字作为旁白朗读。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "展示教师手动对照讲义和纸卡的动作，未声称产品具有自动核对、识别或纠错能力。"
    },
    {
      "location": "shot:3/block:1",
      "text": "翻开讲义夹，读完这句讲解，再指着字幕卡逐字核对。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于人工阅读和核对的行动引导，没有产品性能或自动化承诺。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "分镜1预计8秒、24个旁白单位，配合放纸条、缓慢靠近和阅读；分镜2预计8秒、21个旁白单位，配合圈字、划去、改字及展示结果；分镜3预计7秒、21个旁白单位，配合翻讲义、放卡和逐字核对。预计时长均满足各自最低停留时间，画面任务能支撑停留；第三镜延续示例完成核对，没有重复功能口播或空镜凑时长。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
