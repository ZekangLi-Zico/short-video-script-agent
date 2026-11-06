# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：脚本已完成：保留原标题、两镜结构及原有台词，补齐声画与动作编排，取消过长停留。预计7.3秒，符合30秒上限，全部检查通过。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 字幕，让表达被看见

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 连读旁白

想让画面里的表达更清楚？

剪影练习版支持为视频添加字幕。

### 分镜 1

场景：人物面对镜头，背景简洁，直接向第一次制作口播视频的创作者提问。

镜头目的：提出让口播表达更清楚的需要

| 时间（镜内） | 动作与画面 | 对白与声音 |
|---|---|---|
| 0–3.3 秒 | 人物看向镜头，自然说出问题，句末稍作停顿。<br>镜头：固定中近景 | 旁白：想让画面里的表达更清楚？（同步字幕） |

来源：动作安排见表达审核

预计镜头时长：3.3 秒

### 分镜 2

场景：切换为简洁的字幕功能文字卡片，不展示产品操作界面。

镜头目的：介绍为视频添加字幕的能力

| 时间（镜内） | 动作与画面 | 对白与声音 |
|---|---|---|
| 0–4.0 秒 | 文字卡片完整出现，旁白介绍字幕功能，卡片保持至朗读结束。<br>镜头：固定全屏文字卡 | 旁白：剪影练习版支持为视频添加字幕。（同步字幕） |

来源：P01/P01.F1

预计镜头时长：4.0 秒

## 审稿备注（不进入视频，不计入时长）

供创作者核对修改与资料缺口，不是经过事实认证的产品介绍。

保留原标题、两镜结构和全部原有台词；取消两镜各19秒的最低停留，改为按文案朗读与阅读时间播放，并迁移为format_version=3。

## 实际修订

位置按镜头索引比较；日志关联的是实际反馈，不证明模型因果推理。

- 修改：format_version, editor_notes, shot:1/visual, shot:1/hold_seconds, shot:1/purpose, shot:1/staging, shot:1/block:1, shot:2/visual, shot:2/hold_seconds, shot:2/purpose, shot:2/staging, shot:2/block:1；保留原镜头 0 个、原文案块 0 个。
- 修订前失败检查：duration

预计总时长：7.3 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "c4edcd4e6e8679d4d4e2143b0e9b409fb7e1ace4b0adec8e585ccb97cd76d88d",
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
      "text": "字幕，让表达被看见"
    },
    {
      "location": "shot:1/visual",
      "text": "人物面对镜头，背景简洁，直接向第一次制作口播视频的创作者提问。"
    },
    {
      "location": "shot:1/staging:1",
      "text": "动作：人物看向镜头，自然说出问题，句末稍作停顿。\n镜头：固定中近景"
    },
    {
      "location": "shot:1/block:1",
      "text": "想让画面里的表达更清楚？"
    },
    {
      "location": "shot:2/visual",
      "text": "切换为简洁的字幕功能文字卡片，不展示产品操作界面。"
    },
    {
      "location": "shot:2/staging:1",
      "text": "动作：文字卡片完整出现，旁白介绍字幕功能，卡片保持至朗读结束。\n镜头：固定全屏文字卡"
    },
    {
      "location": "shot:2/block:1",
      "text": "剪影练习版支持为视频添加字幕。"
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
  "script_hash": "c4edcd4e6e8679d4d4e2143b0e9b409fb7e1ace4b0adec8e585ccb97cd76d88d",
  "request_hash": "fa28107203980ab0cf69de95fe59a073c2dd4f2a0ff4d759eb9409e8ac82dc0f",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "介绍字幕功能",
      "verdict": "met",
      "evidence": "第2镜明确介绍“剪影练习版支持为视频添加字幕”，符合主题且有原文支持。"
    },
    {
      "field": "audience",
      "requirement": "第一次制作口播短视频的创作者",
      "verdict": "met",
      "evidence": "两镜从表达需求接到添加字幕的能力，语言直白、没有专业术语，初次创作者可一次理解。"
    },
    {
      "field": "platform",
      "requirement": "抖音",
      "verdict": "met",
      "evidence": "采用面对镜头提问接全屏功能卡片的两镜结构，7.3秒内传达一个明确功能，适合短视频观看。"
    },
    {
      "field": "style",
      "requirement": "清楚、友好、克制",
      "verdict": "met",
      "evidence": "“想让画面里的表达更清楚？”自然衔接字幕功能介绍，语气温和且没有夸大效果。"
    }
  ],
  "summary": "稿件满足字幕功能介绍及受众、平台、风格要求，公开功能声明有资料支持。预计7.3秒，符合30秒上限，声画节奏合理。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "字幕，让表达被看见",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "标题是对字幕呈现文字的修辞表达，没有额外产品能力或效果承诺。"
    },
    {
      "location": "shot:1/visual",
      "text": "人物面对镜头，背景简洁，直接向第一次制作口播视频的创作者提问。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于人物、背景和提问对象的拍摄安排。"
    },
    {
      "location": "shot:1/staging:1",
      "text": "动作：人物看向镜头，自然说出问题，句末稍作停顿。\n镜头：固定中近景",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅安排表演、停顿和机位，不含产品声明。"
    },
    {
      "location": "shot:1/block:1",
      "text": "想让画面里的表达更清楚？",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "以问题引出观众需求，没有承诺产品必然产生某种效果。"
    },
    {
      "location": "shot:2/visual",
      "text": "切换为简洁的字幕功能文字卡片，不展示产品操作界面。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于文字卡片的呈现安排，未虚构产品界面或操作步骤。"
    },
    {
      "location": "shot:2/staging:1",
      "text": "动作：文字卡片完整出现，旁白介绍字幕功能，卡片保持至朗读结束。\n镜头：固定全屏文字卡",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅规定文字卡展示和旁白同步方式，没有新增功能声明。"
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
      "evidence": "与P01.F1原文完全一致，未扩展为自动生成等其他能力。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "第1镜3.3秒承载短句提问及自然停顿，第2镜4秒同步朗读和展示功能文字卡；总计7.3秒，无额外空镜或重复凑时。"
  },
  "expression_review_passed": true
}
```

## 执行路径

estimate_duration → search_materials → write_script → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
