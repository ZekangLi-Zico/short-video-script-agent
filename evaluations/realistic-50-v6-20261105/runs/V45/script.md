# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已将旧稿从45秒压缩至预计16秒，保留标题“记录里的每句话”、原文及三镜顺序，仅保留添加字幕和手动改字两个功能。主要缩短镜头停留，全部检查已通过。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 记录里的每句话

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

镜头目的：用店主备料的日常引入口播记录。

画面：保留店主背影和备料台画面：店主把食材放到台面，整理好后开始介绍当天的准备。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–3.0 秒**

旁白＋同步字幕：一天的准备，从这里开始。

镜头末尾保持画面：3.0–4.0 秒（保留最后一拍屏幕文字）

预计镜头时长：4.0 秒

### 分镜 2

镜头目的：展示为店主口播视频添加字幕。

画面：延续备料画面，制作字幕示意卡：先显示没有字幕的画面，再出现与口播对应的字幕“一天的准备，从这里开始。”；角落标注“字幕示意”。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–4.0 秒**

旁白＋同步字幕：剪影练习版支持为视频添加字幕。

依据：P01/P01.F1

镜头末尾保持画面：4.0–6.0 秒（保留最后一拍屏幕文字）

预计镜头时长：6.0 秒

### 分镜 3

镜头目的：通过改正一个错字说明字幕文字可以手动编辑。

画面：保留纸上改字动作：纸上写着“一天的准各”，店主划掉“各”并写成“备”；随后切到标注“字幕示意”的文字卡，显示改正后的“一天的准备”。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–3.0 秒**

旁白＋同步字幕：字幕文字可以手动编辑。

依据：P01/P01.F2

镜头末尾保持画面：3.0–6.0 秒（保留最后一拍屏幕文字）

预计镜头时长：6.0 秒

## 审稿备注（不进入视频，不计入时长）

供创作者核对修改与资料缺口，不是经过事实认证的产品介绍。

保留原题、原文及三镜顺序，将原有三个15秒停留分别缩短为4秒、6秒、6秒；补充字幕示意与改字前后变化，未增加功能。

## 实际修订

位置按镜头索引比较；日志关联的是实际反馈，不证明模型因果推理。

- 修改：format_version, editor_notes, shot:1/visual, shot:1/hold_seconds, shot:1/purpose, shot:1/block:1, shot:2/visual, shot:2/hold_seconds, shot:2/purpose, shot:2/block:1, shot:3/visual, shot:3/hold_seconds, shot:3/purpose, shot:3/block:1；保留原镜头 0 个、原文案块 0 个。
- 修订前失败检查：duration

预计总时长：16.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "c7ec9a57217beb3c910b8aee29acc6a8804d02e52a0c6fccc80b2ff981b57c76",
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
    },
    {
      "location": "shot:3/block:1",
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
      "text": "记录里的每句话"
    },
    {
      "location": "shot:1/visual",
      "text": "保留店主背影和备料台画面：店主把食材放到台面，整理好后开始介绍当天的准备。"
    },
    {
      "location": "shot:1/block:1",
      "text": "一天的准备，从这里开始。"
    },
    {
      "location": "shot:2/visual",
      "text": "延续备料画面，制作字幕示意卡：先显示没有字幕的画面，再出现与口播对应的字幕“一天的准备，从这里开始。”；角落标注“字幕示意”。"
    },
    {
      "location": "shot:2/block:1",
      "text": "剪影练习版支持为视频添加字幕。"
    },
    {
      "location": "shot:3/visual",
      "text": "保留纸上改字动作：纸上写着“一天的准各”，店主划掉“各”并写成“备”；随后切到标注“字幕示意”的文字卡，显示改正后的“一天的准备”。"
    },
    {
      "location": "shot:3/block:1",
      "text": "字幕文字可以手动编辑。"
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
  "script_hash": "c7ec9a57217beb3c910b8aee29acc6a8804d02e52a0c6fccc80b2ff981b57c76",
  "request_hash": "e65b14b1e8059398f2345dd2e1671d2b818db82a54d1ef482bc3f6497e0b06dd",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "把所附旧稿压缩到25秒以内",
      "verdict": "met",
      "evidence": "当前稿保留旧稿三镜内容，duration_check估算总长16秒，已通过25秒上限检查。"
    },
    {
      "field": "topic",
      "requirement": "保留添加字幕和手动改字两个功能",
      "verdict": "met",
      "evidence": "第2镜介绍“为视频添加字幕”，第3镜介绍“字幕文字可以手动编辑”并展示改字。"
    },
    {
      "field": "topic",
      "requirement": "标题保持“记录里的每句话”",
      "verdict": "met",
      "evidence": "当前标题为“记录里的每句话”，与指定标题一致。"
    },
    {
      "field": "topic",
      "requirement": "优先改冗长停留",
      "verdict": "met",
      "evidence": "三镜原有15秒最低停留分别缩短为4秒、6秒、6秒，原文保留。"
    },
    {
      "field": "topic",
      "requirement": "不要额外添功能",
      "verdict": "met",
      "evidence": "公开文案及示意画面仅涉及添加字幕和手动改字，未加入裁剪或其他功能。"
    },
    {
      "field": "audience",
      "requirement": "第一次拍口播的店主",
      "verdict": "met",
      "evidence": "店主备料并介绍当天准备的场景，配合字幕和改字示意，便于口播新手理解。"
    },
    {
      "field": "platform",
      "requirement": "抖音",
      "verdict": "met",
      "evidence": "16秒三镜结构、简短同步字幕及明确动作演示适合短视频观看。"
    },
    {
      "field": "style",
      "requirement": "自然",
      "verdict": "met",
      "evidence": "以“一天的准备，从这里开始。”配合备料动作引入，语言平实。"
    },
    {
      "field": "style",
      "requirement": "紧凑",
      "verdict": "met",
      "evidence": "三镜依次完成场景引入、添加字幕、手动改字，停留均有具体动作或前后对照支撑。"
    }
  ],
  "summary": "当前稿满足原始需求：保留指定标题与两个功能，优先缩短停留，预计16秒。公开表达有资料支持，镜头节奏合理。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "记录里的每句话",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "主题性标题，不包含具体产品能力或效果承诺。"
    },
    {
      "location": "shot:1/visual",
      "text": "保留店主背影和备料台画面：店主把食材放到台面，整理好后开始介绍当天的准备。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "店主备料与口播的拍摄安排，不含产品声明。"
    },
    {
      "location": "shot:1/block:1",
      "text": "一天的准备，从这里开始。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "日常场景引入语，不含可验证的产品承诺。"
    },
    {
      "location": "shot:2/visual",
      "text": "延续备料画面，制作字幕示意卡：先显示没有字幕的画面，再出现与口播对应的字幕“一天的准备，从这里开始。”；角落标注“字幕示意”。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "画面仅示意为视频添加字幕，未声称自动识别或展示虚构产品操作。"
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
      "evidence": "文案与P01.F1原文一致。"
    },
    {
      "location": "shot:3/visual",
      "text": "保留纸上改字动作：纸上写着“一天的准各”，店主划掉“各”并写成“备”；随后切到标注“字幕示意”的文字卡，显示改正后的“一天的准备”。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "纸上手动改字与字幕示意卡呈现手动编辑能力，未增加自动纠错承诺。"
    },
    {
      "location": "shot:3/block:1",
      "text": "字幕文字可以手动编辑。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "文案与P01.F2原文一致。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "第1镜4秒支撑备料与3秒声画文案；第2镜6秒支撑4秒文案及字幕出现对照；第3镜6秒支撑3秒文案、划改错字及结果展示，无明显空镜凑时长。"
  },
  "expression_review_passed": true
}
```

## 执行路径

estimate_duration → search_materials → write_script → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
