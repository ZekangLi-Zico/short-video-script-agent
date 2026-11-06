# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成三分镜脚本：以笔记本、字幕示意卡和讲义夹展示添加字幕、手动改字及核对步骤。每镜8秒，预计共24秒，全部检查通过。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 课程视频字幕：添加字幕，再手动改字

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

镜头目的：在笔记本上展示课程视频添加字幕前后的变化。

画面：教师坐在笔记本前，屏幕播放课程片段；同一画面由无字幕切换为带字幕，停留观察字幕与授课画面的关系。不展示未经资料确认的按钮或菜单。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–4.0 秒**

旁白＋同步字幕：剪影练习版支持为视频添加字幕。

依据：P01/P01.F1

镜头末尾保持画面：4.0–8.0 秒（保留最后一拍屏幕文字）

预计镜头时长：8.0 秒

### 分镜 2

镜头目的：用字幕示意卡讲清字幕文字能够手动修改。

画面：桌面摆放标有“字幕示意”的卡片，教师把“学习目漂”卡替换为“学习目标”卡，手指点出改动的字，停留对照。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–3.0 秒**

旁白＋同步字幕：字幕文字可以手动编辑。

依据：P01/P01.F2

**第 2 拍 · 镜内 3.0–5.8 秒**

旁白＋同步字幕：例如，把“目漂”改成“目标”。

镜头末尾保持画面：5.8–8.0 秒（保留最后一拍屏幕文字）

预计镜头时长：8.0 秒

### 分镜 3

镜头目的：引导教师用讲义核对课程字幕，形成明确的练习步骤。

画面：教师打开讲义夹，指向讲义上的“学习目标”，再把改好的字幕示意卡放在旁边；镜头同时保留讲义和卡片，让观众核对文字。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–5.0 秒**

旁白＋同步字幕：打开讲义夹，对照课程用词，检查字幕里的字。

镜头末尾保持画面：5.0–8.0 秒（保留最后一拍屏幕文字）

预计镜头时长：8.0 秒

时长要求：22.5–25 秒（接近目标）。

预计总时长：24.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "82d95b52c21faf9c3b81861f8af1e91377f4025ba626a0d2f4103ac6f6d140f9",
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
      "text": "课程视频字幕：添加字幕，再手动改字"
    },
    {
      "location": "shot:1/visual",
      "text": "教师坐在笔记本前，屏幕播放课程片段；同一画面由无字幕切换为带字幕，停留观察字幕与授课画面的关系。不展示未经资料确认的按钮或菜单。"
    },
    {
      "location": "shot:1/block:1",
      "text": "剪影练习版支持为视频添加字幕。"
    },
    {
      "location": "shot:2/visual",
      "text": "桌面摆放标有“字幕示意”的卡片，教师把“学习目漂”卡替换为“学习目标”卡，手指点出改动的字，停留对照。"
    },
    {
      "location": "shot:2/block:1",
      "text": "字幕文字可以手动编辑。"
    },
    {
      "location": "shot:2/block:2",
      "text": "例如，把“目漂”改成“目标”。"
    },
    {
      "location": "shot:3/visual",
      "text": "教师打开讲义夹，指向讲义上的“学习目标”，再把改好的字幕示意卡放在旁边；镜头同时保留讲义和卡片，让观众核对文字。"
    },
    {
      "location": "shot:3/block:1",
      "text": "打开讲义夹，对照课程用词，检查字幕里的字。"
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
  "script_hash": "82d95b52c21faf9c3b81861f8af1e91377f4025ba626a0d2f4103ac6f6d140f9",
  "request_hash": "5a8a440420139279ec1553d5df17e98f299a81d8749d3f199cabda7f4dd353a5",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "用三个分镜介绍字幕添加和手动改字",
      "verdict": "met",
      "evidence": "稿件共三个分镜，第1镜介绍添加字幕，第2镜介绍手动改字并示范纠错。"
    },
    {
      "field": "topic",
      "requirement": "每个镜头至少停留5秒",
      "verdict": "met",
      "evidence": "三个镜头的hold_seconds和预计时长均为8秒。"
    },
    {
      "field": "topic",
      "requirement": "场景为笔记本、字幕示意卡、讲义夹",
      "verdict": "met",
      "evidence": "第1镜展示笔记本，第2镜替换字幕示意卡，第3镜打开讲义夹核对文字。"
    },
    {
      "field": "topic",
      "requirement": "目标接近25秒",
      "verdict": "met",
      "evidence": "当前时长估算为24秒，处于22.5至25秒目标区间，passed为true。"
    },
    {
      "field": "audience",
      "requirement": "初次编辑课程视频的教师",
      "verdict": "met",
      "evidence": "教师、课程片段和讲义核对场景贴合受众，添加字幕与改字的说明直接易懂。"
    },
    {
      "field": "platform",
      "requirement": "B站",
      "verdict": "met",
      "evidence": "三镜课程字幕教学以同步声画和具体纠错示例呈现，适合B站短视频观看。"
    },
    {
      "field": "style",
      "requirement": "慢节奏",
      "verdict": "met",
      "evidence": "每镜8秒，并安排观察字幕、对照错字和核对讲义的停留。"
    },
    {
      "field": "style",
      "requirement": "明确",
      "verdict": "met",
      "evidence": "第1镜讲添加字幕，第2镜用“目漂”改为“目标”说明编辑，第3镜给出核对行动。"
    }
  ],
  "summary": "稿件满足三分镜、两项功能、指定场景和慢节奏要求，预计24秒，接近25秒目标。公开表达有资料支持或属于合理示意，未发现新增产品承诺。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "课程视频字幕：添加字幕，再手动改字",
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
      "evidence": "标题涉及的添加字幕和手动改字均由两条资料支持。"
    },
    {
      "location": "shot:1/visual",
      "text": "教师坐在笔记本前，屏幕播放课程片段；同一画面由无字幕切换为带字幕，停留观察字幕与授课画面的关系。不展示未经资料确认的按钮或菜单。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "无字幕到带字幕的示意对应添加字幕能力，未虚构操作界面或自动化流程。"
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
      "evidence": "与标注资料原文一致。"
    },
    {
      "location": "shot:2/visual",
      "text": "桌面摆放标有“字幕示意”的卡片，教师把“学习目漂”卡替换为“学习目标”卡，手指点出改动的字，停留对照。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "明确以卡片示意手动修改字幕文字，属于资料支持的能力范围。"
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
      "evidence": "与标注资料原文一致。"
    },
    {
      "location": "shot:2/block:2",
      "text": "例如，把“目漂”改成“目标”。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "这是手动编辑字幕文字的具体示例，没有宣称自动纠错。"
    },
    {
      "location": "shot:3/visual",
      "text": "教师打开讲义夹，指向讲义上的“学习目标”，再把改好的字幕示意卡放在旁边；镜头同时保留讲义和卡片，让观众核对文字。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于实物摆放和人工核对的拍摄安排，没有新增产品能力声明。"
    },
    {
      "location": "shot:3/block:1",
      "text": "打开讲义夹，对照课程用词，检查字幕里的字。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "这是人工核对的行动指引，不承诺产品自动检查。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "三镜均为8秒：第1镜声画4秒后观察字幕，第2镜两拍共5.8秒后对照改字，第3镜声画5秒并安排打开讲义、指认和摆卡；停留有具体动作与观察内容支撑。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
