# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成三镜脚本，预计14.6秒：按蒸笼、手写菜单、打包台顺序呈现今日备料，只介绍添加字幕，不出现顾客正脸。全部检查通过。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 早餐摊今日备料：给口播加上字幕

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

镜头目的：从蒸笼备料口播引出添加字幕的用途。

画面：蒸笼近景，摊主的手将包子摆进笼屉。画面下方随口播出现同句字幕；仅拍蒸笼和手部。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–3.3 秒**

旁白＋同步字幕：今天先备包子，摆好这一笼。

**第 2 拍 · 镜内 3.3–7.8 秒**

旁白：这段备料口播，用剪影练习版加上字幕。

依据：P01/P01.F1

预计镜头时长：7.8 秒

### 分镜 2

镜头目的：在手写菜单画面继续展示口播与字幕对应。

画面：切到手写菜单特写，摊主用手指点过“包子”“豆浆”两项；下方随口播显示同句字幕，不拍人脸。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–3.8 秒**

旁白＋同步字幕：今天备包子和豆浆，写在菜单上。

预计镜头时长：3.8 秒

### 分镜 3

镜头目的：用打包台备料收尾，完整展示一段带字幕的摊主日常。

画面：切到打包台俯拍，摊主把纸袋和杯子分别码齐，下方随口播显示同句字幕。画面只含台面、物品和手部，无顾客正脸。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–3.0 秒**

旁白＋同步字幕：纸袋、杯子摆好，准备开摊。

预计镜头时长：3.0 秒

预计总时长：14.6 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "dee06dfef914dc179d600a89e268fac6286e01eb62bee06944cfe65c65286887",
  "passed": true,
  "issues": [],
  "citations": [
    {
      "location": "shot:1/block:2",
      "source_id": "P01",
      "fact_id": "P01.F1",
      "quote": "剪影练习版支持为视频添加字幕。",
      "version": "2026-11-01",
      "text": "这段备料口播，用剪影练习版加上字幕。",
      "requires_semantic_review": true
    }
  ],
  "rules_version": "2026-11-03-v1",
  "requires_expression_review": true,
  "expression_slots": [
    {
      "location": "title",
      "text": "早餐摊今日备料：给口播加上字幕"
    },
    {
      "location": "shot:1/visual",
      "text": "蒸笼近景，摊主的手将包子摆进笼屉。画面下方随口播出现同句字幕；仅拍蒸笼和手部。"
    },
    {
      "location": "shot:1/block:1",
      "text": "今天先备包子，摆好这一笼。"
    },
    {
      "location": "shot:1/block:2",
      "text": "这段备料口播，用剪影练习版加上字幕。"
    },
    {
      "location": "shot:2/visual",
      "text": "切到手写菜单特写，摊主用手指点过“包子”“豆浆”两项；下方随口播显示同句字幕，不拍人脸。"
    },
    {
      "location": "shot:2/block:1",
      "text": "今天备包子和豆浆，写在菜单上。"
    },
    {
      "location": "shot:3/visual",
      "text": "切到打包台俯拍，摊主把纸袋和杯子分别码齐，下方随口播显示同句字幕。画面只含台面、物品和手部，无顾客正脸。"
    },
    {
      "location": "shot:3/block:1",
      "text": "纸袋、杯子摆好，准备开摊。"
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
  "script_hash": "dee06dfef914dc179d600a89e268fac6286e01eb62bee06944cfe65c65286887",
  "request_hash": "4299792130470435332510610b8526e5f391e330ac68588a7ba5d1498ead5ad2",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "做一条剪影练习版字幕功能介绍",
      "verdict": "met",
      "evidence": "第1镜口播明确介绍用剪影练习版添加字幕，三镜均展示字幕成片效果。"
    },
    {
      "field": "topic",
      "requirement": "背景是早餐摊主讲今日备料",
      "verdict": "met",
      "evidence": "三镜依次讲备包子、备包子和豆浆、整理纸袋杯子，配有摊主手部备料画面。"
    },
    {
      "field": "topic",
      "requirement": "只介绍添加字幕",
      "verdict": "met",
      "evidence": "公开文案与画面仅涉及添加字幕，未介绍手动编辑、裁剪或画面比例等其他功能。"
    },
    {
      "field": "topic",
      "requirement": "画面按蒸笼、手写菜单、打包台的顺序",
      "verdict": "met",
      "evidence": "第1镜蒸笼近景、第2镜手写菜单特写、第3镜打包台俯拍，顺序一致。"
    },
    {
      "field": "topic",
      "requirement": "不要出现顾客正脸",
      "verdict": "met",
      "evidence": "三镜分别限定蒸笼和手部、不拍人脸、台面物品和手部，无顾客正脸。"
    },
    {
      "field": "audience",
      "requirement": "小店新媒体兼职",
      "verdict": "met",
      "evidence": "用早餐摊口播和字幕成片展示单一功能，内容直观，适合小店兼职制作者理解。"
    },
    {
      "field": "platform",
      "requirement": "抖音",
      "verdict": "met",
      "evidence": "三段生活近景配短句字幕，预计14.6秒，适合短视频观看。"
    },
    {
      "field": "style",
      "requirement": "像同事分享经验",
      "verdict": "met",
      "evidence": "“这段备料口播，用剪影练习版加上字幕”采用日常分享语气，无夸张推销。"
    },
    {
      "field": "style",
      "requirement": "短句",
      "verdict": "met",
      "evidence": "各文案块均为简短单句，如“纸袋、杯子摆好，准备开摊。”"
    }
  ],
  "summary": "当前稿满足功能范围、早餐摊备料场景、画面顺序及不露顾客正脸等要求，产品声明有资料支持。预计14.6秒，符合25秒上限，节奏合理。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "早餐摊今日备料：给口播加上字幕",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "给口播视频添加字幕属于资料明确支持的功能。"
    },
    {
      "location": "shot:1/visual",
      "text": "蒸笼近景，摊主的手将包子摆进笼屉。画面下方随口播出现同句字幕；仅拍蒸笼和手部。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "展示添加字幕后的成片效果，未宣称自动识别或具体产品操作流程。"
    },
    {
      "location": "shot:1/block:1",
      "text": "今天先备包子，摆好这一笼。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于摊主备料场景台词，不含产品承诺。"
    },
    {
      "location": "shot:1/block:2",
      "text": "这段备料口播，用剪影练习版加上字幕。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "准确改写“剪影练习版支持为视频添加字幕”，未增加功能或效果。"
    },
    {
      "location": "shot:2/visual",
      "text": "切到手写菜单特写，摊主用手指点过“包子”“豆浆”两项；下方随口播显示同句字幕，不拍人脸。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "菜单与手部属于拍摄安排，字幕成片展示由添加字幕功能支持。"
    },
    {
      "location": "shot:2/block:1",
      "text": "今天备包子和豆浆，写在菜单上。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于今日备料的示意台词，不涉及产品能力。"
    },
    {
      "location": "shot:3/visual",
      "text": "切到打包台俯拍，摊主把纸袋和杯子分别码齐，下方随口播显示同句字幕。画面只含台面、物品和手部，无顾客正脸。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "整理物品属于场景动作，字幕展示未超出资料支持的添加字幕范围。"
    },
    {
      "location": "shot:3/block:1",
      "text": "纸袋、杯子摆好，准备开摊。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于备料收尾台词，不含可验证的产品声明。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "第1镜7.8秒承载两拍口播和摆包子动作，第2镜3.8秒展示菜单，第3镜3秒整理打包用品；同拍声画同步，停留有具体内容支撑，无空镜凑时长。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
