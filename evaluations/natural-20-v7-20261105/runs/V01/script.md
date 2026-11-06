# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成3镜脚本，预计16.8秒。按蒸笼、手写菜单、打包台顺序，仅介绍添加字幕，不出现顾客正脸；全部检查通过。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 早餐摊备料口播，用剪影练习版加字幕

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 连读旁白

今天店里备了包子和小米粥，我想拍条视频告诉大家。

这段备料口播，我用剪影练习版给视频添加字幕。

最后拍一下打包台，今天的备料就交代清楚了。

### 分镜 1

镜头目的：摊主介绍今日备料，引出拍摄需要

画面：蒸笼近景，摊主掀盖露出包子，只拍手和蒸笼。摊主画外口播，画面同步显示字幕。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–6.0 秒**

旁白＋同步字幕：今天店里备了包子和小米粥，我想拍条视频告诉大家。

预计镜头时长：6.0 秒

### 分镜 2

镜头目的：结合备料口播介绍添加字幕

画面：切到写着“包子、小米粥”的手写菜单，摊主的手依次指向两项。画面下方出现与口播一致的字幕，不展示未经确认的按钮。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–5.5 秒**

旁白＋同步字幕：这段备料口播，我用剪影练习版给视频添加字幕。

依据：P01/P01.F1

预计镜头时长：5.5 秒

### 分镜 3

镜头目的：以打包准备收束这次备料分享

画面：切到打包台，摊主将餐盒和打包袋摆齐，镜头稍停在整理好的台面。只拍手部与物品，不出现顾客正脸。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–5.3 秒**

旁白＋同步字幕：最后拍一下打包台，今天的备料就交代清楚了。

预计镜头时长：5.3 秒

预计总时长：16.8 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "96f8a90cef8315160654658307413db9152a858ed00943d95de9795df371b884",
  "passed": true,
  "issues": [],
  "citations": [
    {
      "location": "shot:2/block:1",
      "source_id": "P01",
      "fact_id": "P01.F1",
      "quote": "剪影练习版支持为视频添加字幕。",
      "version": "2026-11-01",
      "text": "这段备料口播，我用剪影练习版给视频添加字幕。",
      "requires_semantic_review": true
    }
  ],
  "rules_version": "2026-11-03-v1",
  "requires_expression_review": true,
  "expression_slots": [
    {
      "location": "title",
      "text": "早餐摊备料口播，用剪影练习版加字幕"
    },
    {
      "location": "shot:1/visual",
      "text": "蒸笼近景，摊主掀盖露出包子，只拍手和蒸笼。摊主画外口播，画面同步显示字幕。"
    },
    {
      "location": "shot:1/block:1",
      "text": "今天店里备了包子和小米粥，我想拍条视频告诉大家。"
    },
    {
      "location": "shot:2/visual",
      "text": "切到写着“包子、小米粥”的手写菜单，摊主的手依次指向两项。画面下方出现与口播一致的字幕，不展示未经确认的按钮。"
    },
    {
      "location": "shot:2/block:1",
      "text": "这段备料口播，我用剪影练习版给视频添加字幕。"
    },
    {
      "location": "shot:3/visual",
      "text": "切到打包台，摊主将餐盒和打包袋摆齐，镜头稍停在整理好的台面。只拍手部与物品，不出现顾客正脸。"
    },
    {
      "location": "shot:3/block:1",
      "text": "最后拍一下打包台，今天的备料就交代清楚了。"
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
  "script_hash": "96f8a90cef8315160654658307413db9152a858ed00943d95de9795df371b884",
  "request_hash": "4299792130470435332510610b8526e5f391e330ac68588a7ba5d1498ead5ad2",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "做一条剪影练习版字幕功能介绍",
      "verdict": "met",
      "evidence": "标题及第2镜明确介绍用剪影练习版为视频添加字幕，并展示字幕效果。"
    },
    {
      "field": "topic",
      "requirement": "背景是早餐摊主讲今日备料",
      "verdict": "met",
      "evidence": "第1镜摊主说“今天店里备了包子和小米粥”，配合蒸笼、菜单和打包准备体现早餐摊备料。"
    },
    {
      "field": "topic",
      "requirement": "只介绍添加字幕",
      "verdict": "met",
      "evidence": "全稿仅介绍添加字幕，未出现手动编辑字幕、裁剪视频或调整画面比例等其他功能。"
    },
    {
      "field": "topic",
      "requirement": "画面按蒸笼、手写菜单、打包台的顺序",
      "verdict": "met",
      "evidence": "第1至3镜分别为蒸笼近景、手写菜单、打包台，顺序一致。"
    },
    {
      "field": "topic",
      "requirement": "不要出现顾客正脸",
      "verdict": "met",
      "evidence": "三镜均安排物品和摊主手部画面，第3镜另明确“不出现顾客正脸”。"
    },
    {
      "field": "audience",
      "requirement": "小店新媒体兼职",
      "verdict": "met",
      "evidence": "通过拍摄备料口播并添加字幕的具体小店任务介绍功能，没有专业术语或难以理解的操作描述。"
    },
    {
      "field": "platform",
      "requirement": "抖音",
      "verdict": "met",
      "evidence": "三个具体场景配简短口播与同步字幕，预计16.8秒，适合短视频观看。"
    },
    {
      "field": "style",
      "requirement": "像同事分享经验",
      "verdict": "met",
      "evidence": "连续口播以“我想拍条视频”接“我用剪影练习版”再到打包台收束，口吻日常且指代清楚。"
    },
    {
      "field": "style",
      "requirement": "短句",
      "verdict": "met",
      "evidence": "每镜仅一句简短口播，如“这段备料口播，我用剪影练习版给视频添加字幕”，无复杂长句。"
    }
  ],
  "summary": "当前稿满足功能范围、早餐摊备料场景、画面顺序和不露脸要求，公开产品声明有资料支持。预计16.8秒，符合25秒上限，节奏合理。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "早餐摊备料口播，用剪影练习版加字幕",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "标题的产品能力仅为添加字幕，与P01.F1一致。"
    },
    {
      "location": "shot:1/visual",
      "text": "蒸笼近景，摊主掀盖露出包子，只拍手和蒸笼。摊主画外口播，画面同步显示字幕。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "描述拍摄对象及声画同步安排，未声称产品自动识别或生成字幕。"
    },
    {
      "location": "shot:1/block:1",
      "text": "今天店里备了包子和小米粥，我想拍条视频告诉大家。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于摊主备料场景台词，不含产品能力或真实客户背书。"
    },
    {
      "location": "shot:2/visual",
      "text": "切到写着“包子、小米粥”的手写菜单，摊主的手依次指向两项。画面下方出现与口播一致的字幕，不展示未经确认的按钮。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "安排菜单特写和字幕展示，没有虚构产品界面、按钮或自动工作流程。"
    },
    {
      "location": "shot:2/block:1",
      "text": "这段备料口播，我用剪影练习版给视频添加字幕。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "原文明确支持为视频添加字幕，此处结合备料场景改写，未增加能力或效果。"
    },
    {
      "location": "shot:3/visual",
      "text": "切到打包台，摊主将餐盒和打包袋摆齐，镜头稍停在整理好的台面。只拍手部与物品，不出现顾客正脸。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅描述整理打包用品及取景安排，不含产品承诺。"
    },
    {
      "location": "shot:3/block:1",
      "text": "最后拍一下打包台，今天的备料就交代清楚了。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "承接前两镜的备料信息并收束场景，没有将表达效果归因于产品能力。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "三镜预计6.0、5.5、5.3秒，分别由掀蒸笼、指菜单、摆齐餐盒与打包袋支撑，同拍口播和字幕同步，未见重复事实或空镜凑时长。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
