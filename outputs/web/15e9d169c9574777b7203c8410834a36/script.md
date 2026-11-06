# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成《从门口到房间》修改：仅介绍添加字幕，删除手动编辑和片段裁剪介绍，保留“门口—招牌—室内”三个分镜。预计18秒，全部检查通过。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 从门口到房间

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

镜头目的：介绍添加字幕，并用门口画面建立参观起点。

画面：拍摄民宿门口全景，镜头缓慢靠近入口，叠加添加字幕的介绍文字。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–4.0 秒**

旁白＋同步字幕：剪影练习版支持为视频添加字幕。

依据：P01/P01.F1

镜头末尾保持画面：4.0–6.0 秒（保留最后一拍屏幕文字）

预计镜头时长：6.0 秒

### 分镜 2

镜头目的：用招牌画面展示与场景对应的字幕示例。

画面：镜头对准民宿招牌，由稍宽画面缓慢靠近，叠加字幕“先认一下招牌”。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–2.0 秒**

旁白＋同步字幕：先认一下招牌

镜头末尾保持画面：2.0–6.0 秒（保留最后一拍屏幕文字）

预计镜头时长：6.0 秒

### 分镜 3

镜头目的：延续参观路线，展示室内画面的字幕示例。

画面：进入室内拍摄空桌椅，镜头缓慢横移展示桌椅布局，叠加字幕“再看看室内”。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–1.8 秒**

旁白＋同步字幕：再看看室内

镜头末尾保持画面：1.8–6.0 秒（保留最后一拍屏幕文字）

预计镜头时长：6.0 秒

## 审稿备注（不进入视频，不计入时长）

供创作者核对修改与资料缺口，不是经过事实认证的产品介绍。

保留原标题及首镜产品事实原文；删除手动编辑和片段裁剪介绍，改为两处场景字幕示例。三个分镜停留均由8秒缩短为6秒。

## 实际修订

位置按镜头索引比较；日志关联的是实际反馈，不证明模型因果推理。

- 修改：format_version, editor_notes, shot:1/visual, shot:1/hold_seconds, shot:1/purpose, shot:1/block:1, shot:2/visual, shot:2/hold_seconds, shot:2/purpose, shot:2/block:1, shot:3/visual, shot:3/hold_seconds, shot:3/purpose, shot:3/block:1；保留原镜头 0 个、原文案块 0 个。
- 修订前失败检查：duration, rules_check, requirements_check

预计总时长：18.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "7f6193804f8b4807ed0fb503a2ba0725d28f5eafe58984382aa357df03b6e976",
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
    }
  ],
  "rules_version": "2026-11-03-v1",
  "requires_expression_review": true,
  "expression_slots": [
    {
      "location": "title",
      "text": "从门口到房间"
    },
    {
      "location": "shot:1/visual",
      "text": "拍摄民宿门口全景，镜头缓慢靠近入口，叠加添加字幕的介绍文字。"
    },
    {
      "location": "shot:1/block:1",
      "text": "剪影练习版支持为视频添加字幕。"
    },
    {
      "location": "shot:2/visual",
      "text": "镜头对准民宿招牌，由稍宽画面缓慢靠近，叠加字幕“先认一下招牌”。"
    },
    {
      "location": "shot:2/block:1",
      "text": "先认一下招牌"
    },
    {
      "location": "shot:3/visual",
      "text": "进入室内拍摄空桌椅，镜头缓慢横移展示桌椅布局，叠加字幕“再看看室内”。"
    },
    {
      "location": "shot:3/block:1",
      "text": "再看看室内"
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
    },
    {
      "source_id": "P03",
      "fact_id": "P03.F1",
      "quote": "剪影练习版提供横屏和竖屏画面比例选项。",
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
  "script_hash": "7f6193804f8b4807ed0fb503a2ba0725d28f5eafe58984382aa357df03b6e976",
  "request_hash": "b2bceab66dc6d75c3a021c080ed8cf62efe059b4115ad4c66f61e86afcaeaa8c",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "只介绍添加字幕",
      "verdict": "met",
      "evidence": "第1镜仅介绍添加字幕，第2、3镜展示场景字幕，没有介绍其他产品功能。"
    },
    {
      "field": "topic",
      "requirement": "删除片段裁剪和手动编辑的介绍",
      "verdict": "met",
      "evidence": "当前所有公开文案及画面均无片段裁剪或手动编辑介绍，editor_notes的删除说明与实际一致。"
    },
    {
      "field": "topic",
      "requirement": "仍保留三个分镜",
      "verdict": "met",
      "evidence": "当前稿件共3个分镜。"
    },
    {
      "field": "topic",
      "requirement": "“门口—招牌—室内”的顺序",
      "verdict": "met",
      "evidence": "第1镜民宿门口、第2镜民宿招牌、第3镜室内空桌椅，顺序一致。"
    },
    {
      "field": "audience",
      "requirement": "民宿运营协作伙伴",
      "verdict": "met",
      "evidence": "三镜均采用民宿参观场景，并以对应字幕展示添加字幕的用途，适合民宿运营协作语境。"
    },
    {
      "field": "platform",
      "requirement": "小红书",
      "verdict": "met",
      "evidence": "18秒的民宿场景短视频配简短同步字幕，形式适合小红书观看。"
    },
    {
      "field": "style",
      "requirement": "简洁",
      "verdict": "met",
      "evidence": "每镜仅一个文案块，内容为一句功能介绍及两句简短场景字幕。"
    },
    {
      "field": "style",
      "requirement": "不营销",
      "verdict": "met",
      "evidence": "公开内容没有促销、夸张效果承诺或购买引导。"
    }
  ],
  "summary": "当前稿件满足需求：仅介绍添加字幕，已删除裁剪和手动编辑介绍，并保留三个分镜及指定顺序。公开声明有资料支持，预计18秒，场景动作能支撑停留。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "从门口到房间",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "标题描述参观路线，不包含产品能力承诺。"
    },
    {
      "location": "shot:1/visual",
      "text": "拍摄民宿门口全景，镜头缓慢靠近入口，叠加添加字幕的介绍文字。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "这是门口拍摄及文字叠加安排，没有新增产品操作或效果声明。"
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
      "evidence": "文案与P01.F1原文一致，仅声明支持添加字幕。"
    },
    {
      "location": "shot:2/visual",
      "text": "镜头对准民宿招牌，由稍宽画面缓慢靠近，叠加字幕“先认一下招牌”。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "描述招牌运镜及场景字幕示例，未虚构产品界面或自动流程。"
    },
    {
      "location": "shot:2/block:1",
      "text": "先认一下招牌",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "这是引导观察招牌的场景表达，不含产品承诺。"
    },
    {
      "location": "shot:3/visual",
      "text": "进入室内拍摄空桌椅，镜头缓慢横移展示桌椅布局，叠加字幕“再看看室内”。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "描述室内拍摄动作及字幕示例，不包含额外产品功能声明。"
    },
    {
      "location": "shot:3/block:1",
      "text": "再看看室内",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "这是参观路线的连接语，不含可验证产品承诺。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "每镜预计6秒：第1镜声画同步4秒并靠近入口，第2、3镜短句后分别留出4秒和4.2秒供观察招牌及横移展示桌椅，均有明确画面动作支撑。"
  },
  "expression_review_passed": true
}
```

## 执行路径

check_requirements → search_materials → write_script → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
