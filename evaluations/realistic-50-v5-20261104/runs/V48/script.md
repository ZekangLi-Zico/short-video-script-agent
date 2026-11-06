# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成《从门口到房间》修订：仅介绍添加字幕，删除片段裁剪和手动编辑介绍，保留“门口—招牌—室内”三个分镜。预计15秒，符合20秒上限。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 从门口到房间

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

镜头目的：在民宿门口介绍添加字幕功能。

画面：拍摄民宿门口，镜头缓慢靠近后停稳；产品介绍的旁白同步作为字幕显示在画面下方。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–4.0 秒**

旁白＋同步字幕：剪影练习版支持为视频添加字幕。

依据：P01/P01.F1

镜头末尾保持画面：4.0–5.0 秒（保留最后一拍屏幕文字）

预计镜头时长：5.0 秒

### 分镜 2

镜头目的：用招牌画面示范为入口指引添加字幕。

画面：镜头转向民宿招牌，拍清招牌全貌；旁白同步显示为字幕，文字避开招牌。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–3.5 秒**

旁白＋同步字幕：认准这块招牌，就是民宿入口。

镜头末尾保持画面：3.5–5.0 秒（保留最后一拍屏幕文字）

预计镜头时长：5.0 秒

### 分镜 3

镜头目的：进入室内，继续展示导览旁白与字幕同步出现。

画面：镜头从门口进入室内，缓慢扫过空桌椅后停稳；旁白同步作为字幕出现在画面下方。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–2.8 秒**

旁白＋同步字幕：进门后，桌椅就在眼前。

镜头末尾保持画面：2.8–5.0 秒（保留最后一拍屏幕文字）

预计镜头时长：5.0 秒

## 审稿备注（不进入视频，不计入时长）

供创作者核对修改与资料缺口，不是经过事实认证的产品介绍。

保留原标题、首镜文案及门口—招牌—室内三镜顺序；按要求删除手动编辑和片段裁剪介绍，替换为民宿导览字幕示例；各镜最低停留由8秒调整为5秒。

## 实际修订

位置按镜头索引比较；日志关联的是实际反馈，不证明模型因果推理。

- 修改：format_version, editor_notes, shot:1/visual, shot:1/hold_seconds, shot:1/purpose, shot:1/block:1, shot:2/visual, shot:2/hold_seconds, shot:2/purpose, shot:2/block:1, shot:3/visual, shot:3/hold_seconds, shot:3/purpose, shot:3/block:1；保留原镜头 0 个、原文案块 0 个。
- 修订前失败检查：duration

预计总时长：15.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "10d2a4b79ab6967f06324469108d04b616ecd0964fac0928671380df72776bdc",
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
      "text": "拍摄民宿门口，镜头缓慢靠近后停稳；产品介绍的旁白同步作为字幕显示在画面下方。"
    },
    {
      "location": "shot:1/block:1",
      "text": "剪影练习版支持为视频添加字幕。"
    },
    {
      "location": "shot:2/visual",
      "text": "镜头转向民宿招牌，拍清招牌全貌；旁白同步显示为字幕，文字避开招牌。"
    },
    {
      "location": "shot:2/block:1",
      "text": "认准这块招牌，就是民宿入口。"
    },
    {
      "location": "shot:3/visual",
      "text": "镜头从门口进入室内，缓慢扫过空桌椅后停稳；旁白同步作为字幕出现在画面下方。"
    },
    {
      "location": "shot:3/block:1",
      "text": "进门后，桌椅就在眼前。"
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
  "script_hash": "10d2a4b79ab6967f06324469108d04b616ecd0964fac0928671380df72776bdc",
  "request_hash": "b2bceab66dc6d75c3a021c080ed8cf62efe059b4115ad4c66f61e86afcaeaa8c",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "只介绍添加字幕",
      "verdict": "met",
      "evidence": "第1镜介绍“剪影练习版支持为视频添加字幕”，第2、3镜展示民宿导览字幕示例。公开内容未介绍手动编辑、片段裁剪、画面比例等其他产品功能。"
    },
    {
      "field": "topic",
      "requirement": "删除片段裁剪",
      "verdict": "met",
      "evidence": "旧稿第3镜“剪影练习版支持裁剪视频片段。”已删除，替换为“进门后，桌椅就在眼前。”；其他镜头也未介绍裁剪。"
    },
    {
      "field": "topic",
      "requirement": "手动编辑的介绍",
      "verdict": "met",
      "evidence": "旧稿第2镜“字幕文字可以手动编辑。”已删除，替换为“认准这块招牌，就是民宿入口。”；其他镜头也未介绍手动编辑。"
    },
    {
      "field": "topic",
      "requirement": "保留三个分镜",
      "verdict": "met",
      "evidence": "当前稿件共3个分镜。"
    },
    {
      "field": "topic",
      "requirement": "“门口—招牌—室内”的顺序",
      "verdict": "met",
      "evidence": "第1镜拍摄民宿门口，第2镜转向民宿招牌，第3镜进入室内并扫过桌椅，顺序符合要求。"
    },
    {
      "field": "audience",
      "requirement": "民宿运营协作伙伴",
      "verdict": "met",
      "evidence": "三个镜头均围绕民宿导览展开，第2镜用字幕说明入口，第3镜说明室内桌椅，示例贴合民宿运营内容制作场景。"
    },
    {
      "field": "platform",
      "requirement": "小红书",
      "verdict": "met",
      "evidence": "预计15秒，以民宿实景搭配简短旁白和同步字幕，内容易于浏览；招牌镜头明确要求文字避开招牌，适合短视频呈现。"
    },
    {
      "field": "style",
      "requirement": "简洁",
      "verdict": "met",
      "evidence": "每镜仅一条短文案，分别承担功能介绍、入口指引和室内导览，没有冗长解释或重复介绍。"
    },
    {
      "field": "style",
      "requirement": "不营销",
      "verdict": "met",
      "evidence": "第1镜中性说明字幕功能，第2、3镜为场景导览；没有夸大效果、促销信息或购买引导。"
    }
  ],
  "summary": "已落实功能范围、删除要求和三镜顺序，受众、平台及风格适配合理。公开产品声明有资料支持；预计15秒，时长检查通过，节奏合理。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "从门口到房间",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "概括民宿导览路线，不包含可验证的产品能力或效果承诺。"
    },
    {
      "location": "shot:1/visual",
      "text": "拍摄民宿门口，镜头缓慢靠近后停稳；产品介绍的旁白同步作为字幕显示在画面下方。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "描述门口运镜、字幕位置及声画同步呈现的拍摄安排，没有宣称产品能自动识别语音或自动同步字幕。"
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
      "evidence": "与P01.F1原文“剪影练习版支持为视频添加字幕。”一致，未增加能力或效果声明。"
    },
    {
      "location": "shot:2/visual",
      "text": "镜头转向民宿招牌，拍清招牌全貌；旁白同步显示为字幕，文字避开招牌。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于招牌拍摄、字幕排版和声画同步安排，没有虚构产品界面、按钮或自动避让功能。"
    },
    {
      "location": "shot:2/block:1",
      "text": "认准这块招牌，就是民宿入口。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "配合民宿招牌画面的导览示例，不包含产品性能、用户背书或效果承诺。"
    },
    {
      "location": "shot:3/visual",
      "text": "镜头从门口进入室内，缓慢扫过空桌椅后停稳；旁白同步作为字幕出现在画面下方。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "描述进入室内、扫拍桌椅及字幕呈现的制作安排，没有新增产品能力声明或操作流程。"
    },
    {
      "location": "shot:3/block:1",
      "text": "进门后，桌椅就在眼前。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "与室内桌椅画面对应的场景描述，不涉及产品承诺。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "三镜预计各5秒，同beat的旁白与字幕并行，实际节拍估算依次为4.0、3.5、2.8秒。剩余1.0、1.5、2.2秒可用于门口靠近后停稳、辨认招牌及观察室内桌椅，均有明确画面任务支撑。总计15秒，宿主时长检查通过，没有重复事实或无任务空镜凑时长。"
  },
  "expression_review_passed": true
}
```

## 执行路径

estimate_duration → search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
