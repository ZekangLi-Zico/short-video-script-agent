# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成20秒、3镜头的字幕添加脚本，保留擦净的黑板、课程讲义和空座位场景，仅介绍字幕添加，表达平实克制。时长、规则与需求检查均通过。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 课程画面里的字幕添加

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

镜头目的：用课后教室场景引出课程字幕展示。

画面：固定机位拍擦净的黑板，前景保留空座位。一只手将课程讲义放在桌面，镜头缓慢下移至讲义。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–4.0 秒**

旁白：黑板已经擦净，课程讲义留在桌上。

镜头末尾保持画面：4.0–6.0 秒（保留最后一拍屏幕文字）

预计镜头时长：6.0 秒

### 分镜 2

镜头目的：明确产品支持添加字幕，并展示字幕进入课程画面的变化。

画面：拍摄电脑屏幕中的教室视频，画面包含擦净的黑板和空座位。播放至讲义特写时，底部出现示例字幕“本节课程到这里结束”。不展示未经确认的按钮或操作路径。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–4.0 秒**

旁白＋同步字幕：剪影练习版支持为视频添加字幕。

依据：P01/P01.F1

**第 2 拍 · 镜内 4.0–7.0 秒**

屏幕文字：本节课程到这里结束

镜头末尾保持画面：7.0–8.0 秒（保留最后一拍屏幕文字）

预计镜头时长：8.0 秒

### 分镜 3

镜头目的：让观众观察字幕与课程画面同时呈现的最终样子。

画面：课程视频切回空座位与擦净的黑板，字幕仍位于画面底部；镜头缓慢拉远，桌上的课程讲义进入前景，停在完整教室构图。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–6.0 秒**

屏幕文字：本节课程到这里结束

预计镜头时长：6.0 秒

时长要求：18.0–20 秒（接近目标）。

预计总时长：20.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "7eb4dd043bec36749336e81ccaaf4ceb4ef82ab5a8c36494f9031b89fe6524b5",
  "passed": true,
  "issues": [],
  "citations": [
    {
      "location": "shot:2/block:1",
      "source_id": "P01",
      "fact_id": "P01.F1",
      "quote": "剪影练习版支持为视频添加字幕。",
      "version": "2026-11-01",
      "text": "剪影练习版支持为视频添加字幕。",
      "requires_semantic_review": true
    }
  ],
  "rules_version": "2026-11-03-v1",
  "requires_expression_review": true,
  "expression_slots": [
    {
      "location": "title",
      "text": "课程画面里的字幕添加"
    },
    {
      "location": "shot:1/visual",
      "text": "固定机位拍擦净的黑板，前景保留空座位。一只手将课程讲义放在桌面，镜头缓慢下移至讲义。"
    },
    {
      "location": "shot:1/block:1",
      "text": "黑板已经擦净，课程讲义留在桌上。"
    },
    {
      "location": "shot:2/visual",
      "text": "拍摄电脑屏幕中的教室视频，画面包含擦净的黑板和空座位。播放至讲义特写时，底部出现示例字幕“本节课程到这里结束”。不展示未经确认的按钮或操作路径。"
    },
    {
      "location": "shot:2/block:1",
      "text": "剪影练习版支持为视频添加字幕。"
    },
    {
      "location": "shot:2/block:2",
      "text": "本节课程到这里结束"
    },
    {
      "location": "shot:3/visual",
      "text": "课程视频切回空座位与擦净的黑板，字幕仍位于画面底部；镜头缓慢拉远，桌上的课程讲义进入前景，停在完整教室构图。"
    },
    {
      "location": "shot:3/block:1",
      "text": "本节课程到这里结束"
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
  "script_hash": "7eb4dd043bec36749336e81ccaaf4ceb4ef82ab5a8c36494f9031b89fe6524b5",
  "request_hash": "fe513b9257dbed69caead2482b20e7d77c4402d6ab34c67d59e7319e8c7156e7",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "介绍字幕添加",
      "verdict": "met",
      "evidence": "第2镜明确说明支持添加字幕，并展示课程视频中的示例字幕。"
    },
    {
      "field": "topic",
      "requirement": "背景是擦净的黑板、课程讲义、空座位。",
      "verdict": "met",
      "evidence": "第1镜同时安排擦净的黑板、空座位和放到桌面的课程讲义，第3镜再次呈现完整构图。"
    },
    {
      "field": "topic",
      "requirement": "不要问句",
      "verdict": "met",
      "evidence": "标题及全部公开文案均为陈述句，没有问句。"
    },
    {
      "field": "topic",
      "requirement": "感叹号",
      "verdict": "met",
      "evidence": "标题及所有文案块均未使用感叹号。"
    },
    {
      "field": "topic",
      "requirement": "下载引导",
      "verdict": "met",
      "evidence": "三镜均无下载、安装或获取产品的引导。"
    },
    {
      "field": "topic",
      "requirement": "“轻松搞定”式保证",
      "verdict": "met",
      "evidence": "第2镜仅陈述字幕添加能力，未承诺操作轻松、效率或效果。"
    },
    {
      "field": "topic",
      "requirement": "只讲这个功能。",
      "verdict": "met",
      "evidence": "稿件仅介绍字幕添加，未引入手动编辑字幕、裁剪视频或其他功能。"
    },
    {
      "field": "audience",
      "requirement": "线上课程剪辑助教",
      "verdict": "met",
      "evidence": "第2镜以课程视频和课程结束字幕示例呈现字幕添加，贴合课程剪辑工作。"
    },
    {
      "field": "platform",
      "requirement": "B站",
      "verdict": "met",
      "evidence": "课程场景、简短口播与字幕演示适合作为B站短视频内容。"
    },
    {
      "field": "style",
      "requirement": "平实，克制",
      "verdict": "met",
      "evidence": "文案使用客观陈述，画面采用缓慢移动与固定构图，没有夸张营销措辞。"
    }
  ],
  "summary": "当前稿落实了字幕添加、指定背景和各项禁用要求，未扩展其他功能。公开能力表述有资料支持，20秒估算通过，画面动作与字幕观察安排能够支撑停留。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "课程画面里的字幕添加",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "标题中的字幕添加能力由P01.F1支持，课程画面仅限定示例场景。"
    },
    {
      "location": "shot:1/visual",
      "text": "固定机位拍擦净的黑板，前景保留空座位。一只手将课程讲义放在桌面，镜头缓慢下移至讲义。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅描述教室布景、手部动作及摄影安排，不含产品承诺。"
    },
    {
      "location": "shot:1/block:1",
      "text": "黑板已经擦净，课程讲义留在桌上。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅描述镜头中的黑板和讲义。"
    },
    {
      "location": "shot:2/visual",
      "text": "拍摄电脑屏幕中的教室视频，画面包含擦净的黑板和空座位。播放至讲义特写时，底部出现示例字幕“本节课程到这里结束”。不展示未经确认的按钮或操作路径。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "示例画面展示资料支持的字幕添加结果，未虚构产品按钮、自动流程或操作步骤。"
    },
    {
      "location": "shot:2/block:1",
      "text": "剪影练习版支持为视频添加字幕。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "与所标注P01.F1原文一致，无新增效果或能力。"
    },
    {
      "location": "shot:2/block:2",
      "text": "本节课程到这里结束",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "作为课程视频的示例字幕，不构成产品能力或效果声明。"
    },
    {
      "location": "shot:3/visual",
      "text": "课程视频切回空座位与擦净的黑板，字幕仍位于画面底部；镜头缓慢拉远，桌上的课程讲义进入前景，停在完整教室构图。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "持续展示已添加字幕的示例结果，其余内容为场景和摄影安排。"
    },
    {
      "location": "shot:3/block:1",
      "text": "本节课程到这里结束",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "延续课程结束示例字幕，不含产品承诺。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "第1镜6秒含4秒口播及放讲义、下移镜头；第2镜8秒含4秒同步声画和3秒示例字幕展示；第3镜6秒虽延续同句字幕，但有拉远、讲义进入前景及完整构图观察，具备明确画面任务。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
