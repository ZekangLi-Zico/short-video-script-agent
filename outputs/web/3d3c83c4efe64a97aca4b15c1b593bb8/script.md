# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成《从一段记录开始》：共3镜，预计23秒，以屏幕文字和画面示意介绍添加字幕、裁剪片段，全片静音，不依赖旁白。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 从一段记录开始

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

镜头目的：呈现待加工的日常视频，让后续两项功能有共同的展示对象。

画面：固定机位拍桌面：空桌开场，一只手将杯子放下，再退出画面。画面中央显示引导文字。全片静音。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–3.0 秒**

屏幕文字：从一段日常记录开始。

预计镜头时长：3.0 秒

### 分镜 2

镜头目的：让观众看到添加字幕后，文字如何出现在视频画面中。

画面：沿用放杯子的素材，上方大字展示产品事实。下方示例视频先播放无字幕画面，再叠加第二拍文字作为字幕，继续播放供观众阅读。仅作功能示意，不展示产品界面。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–4.0 秒**

屏幕文字：剪影练习版支持为视频添加字幕。

依据：P01/P01.F1

**第 2 拍 · 镜内 4.0–10.0 秒**

屏幕文字：把想说的话，放进画面里。

预计镜头时长：10.0 秒

### 分镜 3

镜头目的：展示裁剪片段的含义：保留放杯子的动作，去掉前后的空桌画面。

画面：产品事实大字保持显示。下方用三段连续画面示意“空桌、放杯、空桌”；前后空桌段逐渐变灰并移出，只留下中间动作，再播放保留片段。用素材条示意，不模拟按钮或操作界面。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–10.0 秒**

屏幕文字：剪影练习版支持裁剪视频片段。

依据：P02/P02.F1

预计镜头时长：10.0 秒

时长要求：22.5–25 秒（接近目标）。

预计总时长：23.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "fcce4c45da2d208182930c505dd4c5f30a92009f0e2dc1e8c775be81636411cb",
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
      "source_id": "P02",
      "fact_id": "P02.F1",
      "quote": "剪影练习版支持裁剪视频片段。",
      "version": "2026-11-01",
      "text": "剪影练习版支持裁剪视频片段。",
      "requires_semantic_review": true
    }
  ],
  "rules_version": "2026-11-03-v1",
  "requires_expression_review": true,
  "expression_slots": [
    {
      "location": "title",
      "text": "从一段记录开始"
    },
    {
      "location": "shot:1/visual",
      "text": "固定机位拍桌面：空桌开场，一只手将杯子放下，再退出画面。画面中央显示引导文字。全片静音。"
    },
    {
      "location": "shot:1/block:1",
      "text": "从一段日常记录开始。"
    },
    {
      "location": "shot:2/visual",
      "text": "沿用放杯子的素材，上方大字展示产品事实。下方示例视频先播放无字幕画面，再叠加第二拍文字作为字幕，继续播放供观众阅读。仅作功能示意，不展示产品界面。"
    },
    {
      "location": "shot:2/block:1",
      "text": "剪影练习版支持为视频添加字幕。"
    },
    {
      "location": "shot:2/block:2",
      "text": "把想说的话，放进画面里。"
    },
    {
      "location": "shot:3/visual",
      "text": "产品事实大字保持显示。下方用三段连续画面示意“空桌、放杯、空桌”；前后空桌段逐渐变灰并移出，只留下中间动作，再播放保留片段。用素材条示意，不模拟按钮或操作界面。"
    },
    {
      "location": "shot:3/block:1",
      "text": "剪影练习版支持裁剪视频片段。"
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
  "script_hash": "fcce4c45da2d208182930c505dd4c5f30a92009f0e2dc1e8c775be81636411cb",
  "request_hash": "203dffcdfd4eed16b275a021c2db9cd98912b8eefbfae29e431c56613964e2c2",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "给展位静音屏写工具介绍",
      "verdict": "met",
      "evidence": "第1镜明确“全片静音”，第2、3镜通过屏幕文字及功能示意介绍工具，符合展位静音展示场景。"
    },
    {
      "field": "topic",
      "requirement": "添加字幕",
      "verdict": "met",
      "evidence": "第2镜屏幕显示“剪影练习版支持为视频添加字幕。”，并安排无字幕画面到叠加字幕的示意。"
    },
    {
      "field": "topic",
      "requirement": "裁剪片段",
      "verdict": "met",
      "evidence": "第3镜屏幕显示“剪影练习版支持裁剪视频片段。”，画面演示去掉前后空桌片段、保留放杯动作。"
    },
    {
      "field": "topic",
      "requirement": "所有关键信息用屏幕文字表达",
      "verdict": "met",
      "evidence": "产品名称及添加字幕、裁剪片段两项能力均写在screen文案块中，无仅靠声音传达的关键信息。"
    },
    {
      "field": "topic",
      "requirement": "不能依赖旁白",
      "verdict": "met",
      "evidence": "全部文案块的channel均为screen，没有voice或both；画面明确要求全片静音。"
    },
    {
      "field": "topic",
      "requirement": "分镜不超过四个",
      "verdict": "met",
      "evidence": "当前稿共3个分镜。"
    },
    {
      "field": "audience",
      "requirement": "路过展位的普通观众",
      "verdict": "met",
      "evidence": "使用放杯子的日常素材，通过加字幕、去掉空桌片段直观解释功能；文案无专业术语，便于普通观众理解。"
    },
    {
      "field": "platform",
      "requirement": "视频号",
      "verdict": "met",
      "evidence": "稿件为3镜短视频，功能文字与演示结合，估算总长23秒，适合作为视频号工具介绍内容。"
    },
    {
      "field": "style",
      "requirement": "静音可读",
      "verdict": "met",
      "evidence": "所有信息均以屏幕文字呈现；各拍展示时间为3、4、6、10秒，均达到duration_check对应的文字阅读估算。"
    },
    {
      "field": "style",
      "requirement": "简洁",
      "verdict": "met",
      "evidence": "全稿3镜、4个短文案块，围绕同一素材展示两项功能，没有冗长解释或无关信息。"
    }
  ],
  "summary": "需求均已落实：两项功能完整，静音可读，共3镜。产品声明均有资料支持；总长估算23秒通过目标区间检查，各镜停留有阅读或演示内容支撑。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "从一段记录开始",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于引入场景的标题，不含产品能力或效果承诺。"
    },
    {
      "location": "shot:1/visual",
      "text": "固定机位拍桌面：空桌开场，一只手将杯子放下，再退出画面。画面中央显示引导文字。全片静音。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅描述拍摄动作、文字位置和静音安排，不含产品事实声明。"
    },
    {
      "location": "shot:1/block:1",
      "text": "从一段日常记录开始。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于场景引导语，不承诺产品性能或能力。"
    },
    {
      "location": "shot:2/visual",
      "text": "沿用放杯子的素材，上方大字展示产品事实。下方示例视频先播放无字幕画面，再叠加第二拍文字作为字幕，继续播放供观众阅读。仅作功能示意，不展示产品界面。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "示意视频添加字幕的效果，由“剪影练习版支持为视频添加字幕。”支持；未虚构产品界面、按钮或自动操作流程。"
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
      "evidence": "与P01.F1原文一致，引用保留了原块标注的source_id和fact_id。"
    },
    {
      "location": "shot:2/block:2",
      "text": "把想说的话，放进画面里。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "结合本镜字幕示意，该句表达将文字作为字幕加入视频，属于添加字幕能力的通俗表述，未新增自动识别等能力。"
    },
    {
      "location": "shot:3/visual",
      "text": "产品事实大字保持显示。下方用三段连续画面示意“空桌、放杯、空桌”；前后空桌段逐渐变灰并移出，只留下中间动作，再播放保留片段。用素材条示意，不模拟按钮或操作界面。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P02",
          "fact_id": "P02.F1"
        }
      ],
      "evidence": "移除前后片段、保留中间片段是裁剪能力的示意，由P02.F1支持；变灰移出属于示意动画，没有宣称产品会自动识别或裁剪。"
    },
    {
      "location": "shot:3/block:1",
      "text": "剪影练习版支持裁剪视频片段。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P02",
          "fact_id": "P02.F1"
        }
      ],
      "evidence": "与P02.F1原文一致，引用保留了原块标注的source_id和fact_id。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "第1镜预计3秒，短引导文字阅读估算2.75秒，可与放杯动作同步。第2镜预计10秒，第一拍4秒展示功能事实，第二拍6秒展示字幕叠加并供阅读。第3镜预计10秒，除阅读功能文字外，还安排三段素材展示、移除前后片段及保留片段回放，停留有具体动作支撑。各镜符合最低停留要求，没有明显重复事实或空镜凑时长；宿主估算总长23秒，已通过22.5至25秒目标区间。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
