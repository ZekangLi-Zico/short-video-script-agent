# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成三个分镜，覆盖字幕添加、手动改字，以及笔记本、字幕示意卡、讲义夹三个指定场景。每镜停留8秒、8秒、7.5秒，估算总长23.5秒，符合接近25秒的目标。保留当前稿，无需删改；改字画面为纸卡示意。三项检查均通过，实际成片时长仍需拍摄后核对。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 课程视频起步：添加字幕与手动改字

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

画面：笔记本电脑前，教师观看自己的课程片段。镜头缓慢靠近屏幕，配合旁白介绍字幕添加，不展示具体软件按钮或操作路径。

旁白/字幕：第一次剪课程视频，先从字幕开始。剪影练习版支持为视频添加字幕。

来源：P01/P01.F1

预计镜头时长：8.0 秒

### 分镜 2

画面：字幕示意卡特写：教师先指向卡片上的示例错字“学习目票”，再用笔把“票”改成“标”，留出时间观看修改前后的文字。此处为纸卡示意。

旁白/字幕：字幕文字可以手动编辑。先读一遍，再对照讲课内容检查错字。

来源：P01/P01.F2

预计镜头时长：8.0 秒

### 分镜 3

画面：教师打开讲义夹，将讲义放在字幕示意卡旁，用手指逐字对照课程关键词；核对后，再从头读一遍示意卡。

旁白/字幕：最后拿出讲义，逐字核对课程里的关键词，再完整读一遍。

来源：

预计镜头时长：7.5 秒

## 审稿备注（不进入视频，不计入时长）

供创作者核对修改与资料缺口，不是经过事实认证的产品介绍。

三个镜头分别使用笔记本、字幕示意卡、讲义夹，只介绍字幕添加和手动改字。所有blocks均为依次朗读的旁白；纸卡上的错字与改字属于拍摄示例，不另设产品事实卡。停留时间用于观看课程、观察改字及对照讲义，实际总时长待估时工具检查。

时长要求：22.5–25 秒（接近目标）。

预计总时长：23.5 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "653afd14557033c78010af243f9cbce683b9e3d2325c00224f104ac8dc42cfc4",
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
      "text": "课程视频起步：添加字幕与手动改字"
    },
    {
      "location": "shot:1/visual",
      "text": "笔记本电脑前，教师观看自己的课程片段。镜头缓慢靠近屏幕，配合旁白介绍字幕添加，不展示具体软件按钮或操作路径。"
    },
    {
      "location": "shot:1/block:1",
      "text": "第一次剪课程视频，先从字幕开始。"
    },
    {
      "location": "shot:2/visual",
      "text": "字幕示意卡特写：教师先指向卡片上的示例错字“学习目票”，再用笔把“票”改成“标”，留出时间观看修改前后的文字。此处为纸卡示意。"
    },
    {
      "location": "shot:2/block:2",
      "text": "先读一遍，再对照讲课内容检查错字。"
    },
    {
      "location": "shot:3/visual",
      "text": "教师打开讲义夹，将讲义放在字幕示意卡旁，用手指逐字对照课程关键词；核对后，再从头读一遍示意卡。"
    },
    {
      "location": "shot:3/block:1",
      "text": "最后拿出讲义，逐字核对课程里的关键词，再完整读一遍。"
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
  "script_hash": "653afd14557033c78010af243f9cbce683b9e3d2325c00224f104ac8dc42cfc4",
  "request_hash": "5a8a440420139279ec1553d5df17e98f299a81d8749d3f199cabda7f4dd353a5",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "用三个分镜",
      "verdict": "met",
      "evidence": "当前稿件共3个分镜，分别呈现观看课程、纸卡改字和讲义核对。"
    },
    {
      "field": "topic",
      "requirement": "字幕添加",
      "verdict": "met",
      "evidence": "第1镜旁白明确介绍：“剪影练习版支持为视频添加字幕。”rules_check已核对P01.F1。"
    },
    {
      "field": "topic",
      "requirement": "手动改字",
      "verdict": "met",
      "evidence": "第2镜旁白说明“字幕文字可以手动编辑”，并用纸卡将“学习目票”改为“学习目标”作示意；该能力由P01.F2支持。"
    },
    {
      "field": "topic",
      "requirement": "每个镜头至少停留5秒",
      "verdict": "met",
      "evidence": "第1至3镜hold_seconds分别为8、8、7.5秒；duration_check中的预计时长也分别为8、8、7.5秒，均不少于5秒。"
    },
    {
      "field": "topic",
      "requirement": "笔记本",
      "verdict": "met",
      "evidence": "第1镜画面明确为“笔记本电脑前，教师观看自己的课程片段”。"
    },
    {
      "field": "topic",
      "requirement": "字幕示意卡",
      "verdict": "met",
      "evidence": "第2镜使用“字幕示意卡特写”，展示指出错字及用笔改字的动作。"
    },
    {
      "field": "topic",
      "requirement": "讲义夹",
      "verdict": "met",
      "evidence": "第3镜明确安排“教师打开讲义夹”，取出讲义与字幕示意卡对照。"
    },
    {
      "field": "topic",
      "requirement": "目标接近25秒",
      "verdict": "met",
      "evidence": "duration_check估算总长23.5秒，位于22.5至25秒的目标区间内，passed=true。"
    },
    {
      "field": "audience",
      "requirement": "初次编辑课程视频的教师",
      "verdict": "met",
      "evidence": "第1镜以“第一次剪课程视频，先从字幕开始”引入，画面主体为教师；后续结合讲课内容和讲义核对，内容基础且贴合课程制作场景。"
    },
    {
      "field": "platform",
      "requirement": "B站",
      "verdict": "met",
      "evidence": "三个分镜组成简短的课程视频编辑入门介绍，包含旁白、改字示例和核对动作，适合作为B站知识类短视频内容。"
    },
    {
      "field": "style",
      "requirement": "慢节奏",
      "verdict": "met",
      "evidence": "各镜预计停留7.5至8秒；第1镜慢推，第2镜观察改字前后，第3镜逐字核对，均有明确的观看或动作安排。"
    },
    {
      "field": "style",
      "requirement": "明确",
      "verdict": "met",
      "evidence": "前两镜分别直接说明字幕添加和手动编辑；改字画面明确标为纸卡示意，第3镜具体说明核对课程关键词。"
    }
  ],
  "summary": "全部明确要求均已落实。三个分镜覆盖两项功能及指定场景，每镜至少5秒，预计总长23.5秒且时长检查通过；表达有依据，节奏合理。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "课程视频起步：添加字幕与手动改字",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        },
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "标题中的“添加字幕”由P01.F1支持，“手动改字”由P01.F2支持；未增加自动化或效果承诺。"
    },
    {
      "location": "shot:1/visual",
      "text": "笔记本电脑前，教师观看自己的课程片段。镜头缓慢靠近屏幕，配合旁白介绍字幕添加，不展示具体软件按钮或操作路径。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "内容为教师观看课程、镜头慢推及旁白配合的拍摄安排，没有新增产品能力、按钮名称或操作流程声明。"
    },
    {
      "location": "shot:1/block:1",
      "text": "第一次剪课程视频，先从字幕开始。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "面向初学者的开场建议，不承诺产品性能或使用效果。"
    },
    {
      "location": "shot:2/visual",
      "text": "字幕示意卡特写：教师先指向卡片上的示例错字“学习目票”，再用笔把“票”改成“标”，留出时间观看修改前后的文字。此处为纸卡示意。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "明确限定为纸卡上的示例改字，是拍摄动作安排，没有声称软件具备自动纠错、手写输入等能力。"
    },
    {
      "location": "shot:2/block:2",
      "text": "先读一遍，再对照讲课内容检查错字。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "要求使用者自行阅读和核对，属于行动建议，没有产品自动检查或准确率承诺。"
    },
    {
      "location": "shot:3/visual",
      "text": "教师打开讲义夹，将讲义放在字幕示意卡旁，用手指逐字对照课程关键词；核对后，再从头读一遍示意卡。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "教师操作讲义夹和纸卡的生活场景安排，不涉及产品界面、自动工作流或未证实功能。"
    },
    {
      "location": "shot:3/block:1",
      "text": "最后拿出讲义，逐字核对课程里的关键词，再完整读一遍。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "人工核对课程关键词的行动建议，没有宣称产品提供额外能力或保证校对结果。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "第1镜预计8秒、28个旁白单位，配合观看课程及慢推镜头；第2镜预计8秒、25个旁白单位，支撑指出错字、改字及前后观察；第3镜预计7.5秒、23个旁白单位，配合打开讲义夹、对照关键词及复读短卡。每镜均有具体内容支撑停留，纸卡改字与讲义核对承担不同任务，无明显空镜或重复事实凑时长。editor_notes未计入朗读。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
