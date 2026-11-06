# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成三分镜脚本《字幕，让表达被看见》，用笔记本、字幕示意卡和讲义夹串联字幕添加与手动改字。每镜分别为8秒、8秒、7.5秒，预计总长23.5秒，全部检查通过。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 字幕，让表达被看见

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

镜头目的：展示课程片段添加字幕前后的变化，介绍添加字幕功能。

画面：教师坐在笔记本前观看自制课程片段。固定机位，片段由无字幕切换为后期叠加字幕的示意画面，停留供观众观察；不展示软件按钮或未经提供的界面。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–8.0 秒**

旁白＋同步字幕：剪影练习版支持为视频添加字幕。

依据：P01/P01.F1

预计镜头时长：8.0 秒

### 分镜 2

镜头目的：通过纸面改字动作，让教师理解字幕文字可以手动修改。

画面：俯拍笔记本旁的字幕示意卡。教师先指向卡片上一处写错的字，再用笔划掉并写上正确字；镜头停在修改后的卡片上。纸面动作仅作功能示意。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–8.0 秒**

旁白＋同步字幕：字幕文字可以手动编辑。

依据：P01/P01.F2

预计镜头时长：8.0 秒

### 分镜 3

镜头目的：把改字放回备课场景，展示对照讲义核对字幕的收尾动作。

画面：教师打开讲义夹，将修改后的字幕示意卡放在对应讲义旁，手指依次指向讲义原句和卡片改字处，核对后把卡片放回笔记本旁。保持俯拍，留出看清对应关系的时间。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–7.5 秒**

旁白＋同步字幕：把想说的话，放进画面里。

预计镜头时长：7.5 秒

时长要求：22.5–25 秒（接近目标）。

预计总时长：23.5 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "b77eb1aaee72488aedf214fdd0a6ebfe99d56ab886bfdbf056fbdcceb600493b",
  "passed": true,
  "issues": [],
  "citations": [
    {
      "location": "shot:1/block:1",
      "source_id": "P01",
      "fact_id": "P01.F1",
      "quote": "剪影练习版支持为视频添加字幕。",
      "version": "2026-11-01",
      "text": "剪影练习版支持为视频添加字幕。",
      "requires_semantic_review": true
    },
    {
      "location": "shot:2/block:1",
      "source_id": "P01",
      "fact_id": "P01.F2",
      "quote": "字幕文字可以手动编辑。",
      "version": "2026-11-01",
      "text": "字幕文字可以手动编辑。",
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
      "text": "教师坐在笔记本前观看自制课程片段。固定机位，片段由无字幕切换为后期叠加字幕的示意画面，停留供观众观察；不展示软件按钮或未经提供的界面。"
    },
    {
      "location": "shot:1/block:1",
      "text": "剪影练习版支持为视频添加字幕。"
    },
    {
      "location": "shot:2/visual",
      "text": "俯拍笔记本旁的字幕示意卡。教师先指向卡片上一处写错的字，再用笔划掉并写上正确字；镜头停在修改后的卡片上。纸面动作仅作功能示意。"
    },
    {
      "location": "shot:2/block:1",
      "text": "字幕文字可以手动编辑。"
    },
    {
      "location": "shot:3/visual",
      "text": "教师打开讲义夹，将修改后的字幕示意卡放在对应讲义旁，手指依次指向讲义原句和卡片改字处，核对后把卡片放回笔记本旁。保持俯拍，留出看清对应关系的时间。"
    },
    {
      "location": "shot:3/block:1",
      "text": "把想说的话，放进画面里。"
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
  "script_hash": "b77eb1aaee72488aedf214fdd0a6ebfe99d56ab886bfdbf056fbdcceb600493b",
  "request_hash": "5a8a440420139279ec1553d5df17e98f299a81d8749d3f199cabda7f4dd353a5",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "用三个分镜",
      "verdict": "met",
      "evidence": "稿件包含三个分镜，依次展示添加字幕、手动改字和对照讲义核对字幕。"
    },
    {
      "field": "topic",
      "requirement": "字幕添加",
      "verdict": "met",
      "evidence": "第1镜声画同步呈现“剪影练习版支持为视频添加字幕。”，画面展示课程片段从无字幕切换为叠加字幕的示意。"
    },
    {
      "field": "topic",
      "requirement": "手动改字",
      "verdict": "met",
      "evidence": "第2镜声画同步呈现“字幕文字可以手动编辑。”，并用字幕示意卡上的划错、改字动作辅助理解。"
    },
    {
      "field": "topic",
      "requirement": "每个镜头至少停留5秒",
      "verdict": "met",
      "evidence": "三个镜头的hold_seconds分别为8、8、7.5秒；duration_check对应预计时长也分别为8、8、7.5秒，均不少于5秒。"
    },
    {
      "field": "topic",
      "requirement": "笔记本",
      "verdict": "met",
      "evidence": "第1镜明确安排“教师坐在笔记本前观看自制课程片段”；第2、3镜也包含笔记本旁的布景与动作。"
    },
    {
      "field": "topic",
      "requirement": "字幕示意卡",
      "verdict": "met",
      "evidence": "第2镜俯拍字幕示意卡并展示手动改字；第3镜将修改后的字幕示意卡与讲义对照。"
    },
    {
      "field": "topic",
      "requirement": "讲义夹",
      "verdict": "met",
      "evidence": "第3镜明确安排“教师打开讲义夹”，随后对照讲义原句与卡片改字处。"
    },
    {
      "field": "topic",
      "requirement": "目标接近25秒",
      "verdict": "met",
      "evidence": "当前duration_check预计总长23.5秒，处于宿主给定的22.5至25秒目标区间，passed为true。"
    },
    {
      "field": "audience",
      "requirement": "初次编辑课程视频的教师",
      "verdict": "met",
      "evidence": "第1镜使用教师观看自制课程片段的场景，第2镜用纸面改字解释手动编辑，第3镜对照讲义核对字幕；表述简短，无需预先掌握编辑术语。"
    },
    {
      "field": "platform",
      "requirement": "B站",
      "verdict": "met",
      "evidence": "三个分镜组成约23.5秒的功能介绍短片，采用简短中文旁白与同步屏幕文字，适合B站短视频观看。"
    },
    {
      "field": "style",
      "requirement": "慢节奏",
      "verdict": "met",
      "evidence": "各镜停留7.5至8秒，使用固定机位或俯拍，并明确安排观察字幕变化、观看改字和对照讲义的时间。"
    },
    {
      "field": "style",
      "requirement": "明确",
      "verdict": "met",
      "evidence": "第1、2镜分别直述添加字幕和手动编辑文字两项能力，配套示意动作对应清楚；第3镜通过讲义与改字处的对照完成收尾。"
    }
  ],
  "summary": "各项需求均已落实。三个镜头覆盖字幕添加、手动改字及指定场景，预计23.5秒，每镜均超过5秒；公开表达有资料支持或属于场景与创意表达，节奏合理。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "字幕，让表达被看见",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于围绕字幕的修辞性标题，没有具体产品性能、自动化或效果承诺。"
    },
    {
      "location": "shot:1/visual",
      "text": "教师坐在笔记本前观看自制课程片段。固定机位，片段由无字幕切换为后期叠加字幕的示意画面，停留供观众观察；不展示软件按钮或未经提供的界面。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "画面示意的产品能力仅为给视频添加字幕，由P01.F1支持；教师、课程片段和固定机位属于拍摄安排，未新增自动生成字幕或具体软件操作声明。"
    },
    {
      "location": "shot:1/block:1",
      "text": "剪影练习版支持为视频添加字幕。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "文案与P01.F1原文完全一致，引用与原块标注一致，没有扩展功能或效果。"
    },
    {
      "location": "shot:2/visual",
      "text": "俯拍笔记本旁的字幕示意卡。教师先指向卡片上一处写错的字，再用笔划掉并写上正确字；镜头停在修改后的卡片上。纸面动作仅作功能示意。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "纸面改字仅示意字幕文字可手动编辑，由P01.F2支持；未将纸笔动作描述为软件操作，也未宣称自动纠错。"
    },
    {
      "location": "shot:2/block:1",
      "text": "字幕文字可以手动编辑。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "文案与P01.F2原文完全一致，引用与原块标注一致，没有增加自动化能力。"
    },
    {
      "location": "shot:3/visual",
      "text": "教师打开讲义夹，将修改后的字幕示意卡放在对应讲义旁，手指依次指向讲义原句和卡片改字处，核对后把卡片放回笔记本旁。保持俯拍，留出看清对应关系的时间。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "描述教师人工对照纸面材料的动作和拍摄安排，未声称产品能够读取讲义、自动核对或自动改字。"
    },
    {
      "location": "shot:3/block:1",
      "text": "把想说的话，放进画面里。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于表达主题的行动邀请，没有具体产品能力、量化效果或自动化承诺。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "按duration_check的实际节拍估算，第1镜8秒、旁白4秒，余下时间用于观察字幕前后变化；第2镜8秒、旁白3秒，配合指错字、划掉、写正确字和观察结果；第3镜7.5秒、旁白3秒，配合打开讲义夹、摆卡、指向对照及归位。各镜均有具体观察或动作支撑停留，未见重复事实或空镜凑时长。各块均为both且同beat同步，声画时间无需相加。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
