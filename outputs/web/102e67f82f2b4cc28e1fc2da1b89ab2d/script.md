# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成《给课程录像添加字幕》三镜脚本，预计19.8秒。保留指定教室背景，仅介绍字幕添加，已删除手动编辑功能内容，全部检查通过。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 给课程录像添加字幕

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 连读旁白

整理这段课程录像时，我想给讲解配上字幕，方便学生对照着看。

在剪影练习版里，可以为视频添加字幕。

加好字幕后，我会再看一遍录像，听着讲解，对照画面上的文字。

### 分镜 1

镜头目的：交代课程录像配字幕的具体需要

画面：擦净的黑板前，桌上摊开课程讲义，后方是空座位。镜头从教室全景缓慢移向讲义。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–7.0 秒**

旁白：整理这段课程录像时，我想给讲解配上字幕，方便学生对照着看。

预计镜头时长：7.0 秒

### 分镜 2

镜头目的：展示为课程视频添加字幕的能力

画面：拍摄电脑上的课程视频预览，画面为擦净的黑板与空座位；从无字幕画面切换到带课程主题字幕的画面，不展示未经核实的按钮。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–4.5 秒**

旁白：在剪影练习版里，可以为视频添加字幕。

依据：P01/P01.F1

镜头末尾保持画面：4.5–6.0 秒（保留最后一拍屏幕文字）

预计镜头时长：6.0 秒

### 分镜 3

镜头目的：观看添加字幕后的课程片段，结束本次分享

画面：电脑旁放着课程讲义，播放已添加字幕的课程片段；镜头靠近预览画面，展示一句讲解及其对应字幕，最后停留在字幕上。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–6.8 秒**

旁白：加好字幕后，我会再看一遍录像，听着讲解，对照画面上的文字。

预计镜头时长：6.8 秒

## 审稿备注（不进入视频，不计入时长）

供创作者核对修改与资料缺口，不是经过事实认证的产品介绍。

已删除第3镜的手动编辑字幕功能介绍及修改前后演示，改为观看添加字幕后的课程片段；进一步精简第3镜旁白以缩短时长。

## 实际修订

位置按镜头索引比较；日志关联的是实际反馈，不证明模型因果推理。

- 修改：editor_notes, shot:3/visual, shot:3/purpose, shot:3/block:1；保留原镜头 2 个、原文案块 2 个。
- 修订前失败检查：requirements_check
- 修改：editor_notes, shot:3/block:1；保留原镜头 2 个、原文案块 2 个。
- 修订前失败检查：duration, requirements_check

时长要求：18.0–20 秒（接近目标）。

预计总时长：19.8 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "400f8bf154c57f9b701abc2b5894a969a747819961ded4441893b8fe70af12b9",
  "passed": true,
  "issues": [],
  "citations": [
    {
      "location": "shot:2/block:1",
      "source_id": "P01",
      "fact_id": "P01.F1",
      "quote": "剪影练习版支持为视频添加字幕。",
      "version": "2026-11-01",
      "text": "在剪影练习版里，可以为视频添加字幕。",
      "requires_semantic_review": true
    }
  ],
  "rules_version": "2026-11-03-v1",
  "requires_expression_review": true,
  "expression_slots": [
    {
      "location": "title",
      "text": "给课程录像添加字幕"
    },
    {
      "location": "shot:1/visual",
      "text": "擦净的黑板前，桌上摊开课程讲义，后方是空座位。镜头从教室全景缓慢移向讲义。"
    },
    {
      "location": "shot:1/block:1",
      "text": "整理这段课程录像时，我想给讲解配上字幕，方便学生对照着看。"
    },
    {
      "location": "shot:2/visual",
      "text": "拍摄电脑上的课程视频预览，画面为擦净的黑板与空座位；从无字幕画面切换到带课程主题字幕的画面，不展示未经核实的按钮。"
    },
    {
      "location": "shot:2/block:1",
      "text": "在剪影练习版里，可以为视频添加字幕。"
    },
    {
      "location": "shot:3/visual",
      "text": "电脑旁放着课程讲义，播放已添加字幕的课程片段；镜头靠近预览画面，展示一句讲解及其对应字幕，最后停留在字幕上。"
    },
    {
      "location": "shot:3/block:1",
      "text": "加好字幕后，我会再看一遍录像，听着讲解，对照画面上的文字。"
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
  "script_hash": "400f8bf154c57f9b701abc2b5894a969a747819961ded4441893b8fe70af12b9",
  "request_hash": "fe513b9257dbed69caead2482b20e7d77c4402d6ab34c67d59e7319e8c7156e7",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "介绍字幕添加",
      "verdict": "met",
      "evidence": "第2镜明确介绍“可以为视频添加字幕”，并展示添加前后的画面。"
    },
    {
      "field": "topic",
      "requirement": "背景是擦净的黑板、课程讲义、空座位。",
      "verdict": "met",
      "evidence": "第1镜画面同时包含擦净的黑板、摊开的课程讲义及后方空座位。"
    },
    {
      "field": "topic",
      "requirement": "不要问句",
      "verdict": "met",
      "evidence": "标题及三镜旁白均为陈述句，没有问句。"
    },
    {
      "field": "topic",
      "requirement": "感叹号",
      "verdict": "met",
      "evidence": "标题、旁白及画面说明均未使用感叹号。"
    },
    {
      "field": "topic",
      "requirement": "下载引导",
      "verdict": "met",
      "evidence": "全部公开文案均无下载引导，第3镜以观看课程片段结束。"
    },
    {
      "field": "topic",
      "requirement": "“轻松搞定”式保证",
      "verdict": "met",
      "evidence": "旁白仅说明添加字幕及观看核对，没有省力、速度或效果保证。"
    },
    {
      "field": "topic",
      "requirement": "只讲这个功能。",
      "verdict": "met",
      "evidence": "全部镜头仅围绕添加字幕展开，未介绍手动编辑字幕或裁剪视频；第3镜是人工观看核对。"
    },
    {
      "field": "audience",
      "requirement": "线上课程剪辑助教",
      "verdict": "met",
      "evidence": "连续旁白依次交代课程录像配字幕的需要、添加能力和观看核对，贴合助教整理课程录像的工作。"
    },
    {
      "field": "platform",
      "requirement": "B站",
      "verdict": "met",
      "evidence": "约20秒的课程剪辑功能演示具有明确主题和具体画面，适合B站短视频呈现。"
    },
    {
      "field": "style",
      "requirement": "平实，克制",
      "verdict": "met",
      "evidence": "“整理这段课程录像时”到“加好字幕后”的叙述连贯，语气客观，无夸张承诺或煽动性结尾。"
    }
  ],
  "summary": "当前稿落实了字幕添加的单一功能范围、指定背景和各项禁用要求，表达连贯且适合课程剪辑助教。产品声明有资料支持，预计19.8秒，镜头节奏合理。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "给课程录像添加字幕",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "课程录像属于视频，标题仅涉及资料支持的添加字幕能力。"
    },
    {
      "location": "shot:1/visual",
      "text": "擦净的黑板前，桌上摊开课程讲义，后方是空座位。镜头从教室全景缓慢移向讲义。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅为教室背景和镜头运动安排，不包含产品承诺。"
    },
    {
      "location": "shot:1/block:1",
      "text": "整理这段课程录像时，我想给讲解配上字幕，方便学生对照着看。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "表达配字幕的个人意图与使用场景，没有承诺学习效果或额外产品能力。"
    },
    {
      "location": "shot:2/visual",
      "text": "拍摄电脑上的课程视频预览，画面为擦净的黑板与空座位；从无字幕画面切换到带课程主题字幕的画面，不展示未经核实的按钮。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "示意画面只展示视频添加字幕的结果，未虚构按钮、布局或自动流程。"
    },
    {
      "location": "shot:2/block:1",
      "text": "在剪影练习版里，可以为视频添加字幕。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "准确改写原文“剪影练习版支持为视频添加字幕”，保留了原块引用。"
    },
    {
      "location": "shot:3/visual",
      "text": "电脑旁放着课程讲义，播放已添加字幕的课程片段；镜头靠近预览画面，展示一句讲解及其对应字幕，最后停留在字幕上。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "展示添加字幕后的课程视频，不暗示自动识别、自动同步或编辑功能。"
    },
    {
      "location": "shot:3/block:1",
      "text": "加好字幕后，我会再看一遍录像，听着讲解，对照画面上的文字。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "描述创作者人工观看和核对的安排，不声明产品具备核对能力。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "三镜预计7.0、6.0、6.8秒，分别由课程背景移动镜头、字幕前后切换、讲解与字幕核对支撑；第2镜旁白后的1.5秒可供观察字幕，其余镜头与旁白时长匹配。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → check_requirements → write_script → check_requirements → write_script → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
