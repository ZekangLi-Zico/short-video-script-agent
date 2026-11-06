# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成3镜脚本，预计13.8秒。按蒸笼、手写菜单、打包台顺序展示早餐备料，仅介绍添加字幕，不出现顾客正脸；全部检查通过。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 早餐摊今日备料，给口播加上字幕

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

镜头目的：从蒸笼备料口播引出添加字幕功能。

画面：竖屏近拍摊主双手揭开蒸笼，露出包子。先呈现无字幕的备料画面，再以同一画面叠加对应字幕展示效果；只拍手和蒸笼。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–2.5 秒**

旁白＋同步字幕：今天先蒸两笼包子。

**第 2 拍 · 镜内 2.5–7.0 秒**

旁白：这段备料口播，用剪影练习版加上字幕。

依据：P01/P01.F1

预计镜头时长：7.0 秒

### 分镜 2

镜头目的：用手写菜单画面展示字幕与备料口播对应。

画面：镜头切到手写菜单，摊主在“豆浆”旁做记号；底部字幕随摊主口播出现，避开菜单文字。画面不出现其他人。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–3.8 秒**

旁白＋同步字幕：豆浆也备好了，今天就卖这几样。

预计镜头时长：3.8 秒

### 分镜 3

镜头目的：在打包台完成今日备料叙述，延续字幕展示。

画面：镜头切到打包台，摊主把纸袋和餐盒摆好，最后将一只纸袋立起；对应字幕随口播出现。构图仅保留台面和双手，不出现顾客正脸。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–3.0 秒**

旁白＋同步字幕：纸袋、餐盒摆好，准备开摊。

预计镜头时长：3.0 秒

预计总时长：13.8 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "1976182ff1810096027dcee29fc66cf0d5427172deb66876805ff1c6d2b7402e",
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
      "text": "早餐摊今日备料，给口播加上字幕"
    },
    {
      "location": "shot:1/visual",
      "text": "竖屏近拍摊主双手揭开蒸笼，露出包子。先呈现无字幕的备料画面，再以同一画面叠加对应字幕展示效果；只拍手和蒸笼。"
    },
    {
      "location": "shot:1/block:1",
      "text": "今天先蒸两笼包子。"
    },
    {
      "location": "shot:1/block:2",
      "text": "这段备料口播，用剪影练习版加上字幕。"
    },
    {
      "location": "shot:2/visual",
      "text": "镜头切到手写菜单，摊主在“豆浆”旁做记号；底部字幕随摊主口播出现，避开菜单文字。画面不出现其他人。"
    },
    {
      "location": "shot:2/block:1",
      "text": "豆浆也备好了，今天就卖这几样。"
    },
    {
      "location": "shot:3/visual",
      "text": "镜头切到打包台，摊主把纸袋和餐盒摆好，最后将一只纸袋立起；对应字幕随口播出现。构图仅保留台面和双手，不出现顾客正脸。"
    },
    {
      "location": "shot:3/block:1",
      "text": "纸袋、餐盒摆好，准备开摊。"
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
  "script_hash": "1976182ff1810096027dcee29fc66cf0d5427172deb66876805ff1c6d2b7402e",
  "request_hash": "4299792130470435332510610b8526e5f391e330ac68588a7ba5d1498ead5ad2",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "做一条剪影练习版字幕功能介绍",
      "verdict": "met",
      "evidence": "第1镜明确说“用剪影练习版加上字幕”，并安排添加字幕前后的画面对照。"
    },
    {
      "field": "topic",
      "requirement": "背景是早餐摊主讲今日备料",
      "verdict": "met",
      "evidence": "三镜分别讲蒸包子、备豆浆和摆放包装用品，画面均对应早餐摊备料。"
    },
    {
      "field": "topic",
      "requirement": "只介绍添加字幕",
      "verdict": "met",
      "evidence": "公开文案与功能示意仅涉及添加字幕，未介绍手动编辑、裁剪或比例选项；竖屏仅为拍摄安排。"
    },
    {
      "field": "topic",
      "requirement": "画面按蒸笼、手写菜单、打包台的顺序",
      "verdict": "met",
      "evidence": "第1至3镜依次呈现蒸笼、手写菜单和打包台。"
    },
    {
      "field": "topic",
      "requirement": "不要出现顾客正脸",
      "verdict": "met",
      "evidence": "第1镜只拍手和蒸笼，第2镜不出现其他人，第3镜仅保留台面和双手。"
    },
    {
      "field": "audience",
      "requirement": "小店新媒体兼职",
      "verdict": "met",
      "evidence": "用店铺备料口播演示加字幕，表达直接、拍摄任务简单，适合小店兼职创作者。"
    },
    {
      "field": "platform",
      "requirement": "抖音",
      "verdict": "met",
      "evidence": "采用竖屏近拍、同步字幕和三个简短生活镜头，符合短视频观看方式。"
    },
    {
      "field": "style",
      "requirement": "像同事分享经验",
      "verdict": "met",
      "evidence": "“这段备料口播，用剪影练习版加上字幕”以日常建议语气介绍用法。"
    },
    {
      "field": "style",
      "requirement": "短句",
      "verdict": "met",
      "evidence": "各文案块均为简短口语句，例如“纸袋、餐盒摆好，准备开摊”。"
    }
  ],
  "summary": "稿件落实了早餐摊备料场景、指定镜头顺序和仅介绍添加字幕的范围，公开功能表述有资料支持。预计13.8秒，符合25秒上限，节奏合理。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "早餐摊今日备料，给口播加上字幕",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "给口播视频添加字幕由P01.F1支持，早餐摊备料为场景设定。"
    },
    {
      "location": "shot:1/visual",
      "text": "竖屏近拍摊主双手揭开蒸笼，露出包子。先呈现无字幕的备料画面，再以同一画面叠加对应字幕展示效果；只拍手和蒸笼。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "叠加字幕的示意由添加字幕能力支持，其余为拍摄安排，未虚构产品界面或操作步骤。"
    },
    {
      "location": "shot:1/block:1",
      "text": "今天先蒸两笼包子。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "这是摊主备料情境台词，不包含产品承诺。"
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
      "evidence": "准确转述原标注事实“剪影练习版支持为视频添加字幕”，未增加其他能力。"
    },
    {
      "location": "shot:2/visual",
      "text": "镜头切到手写菜单，摊主在“豆浆”旁做记号；底部字幕随摊主口播出现，避开菜单文字。画面不出现其他人。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "字幕随口播展示属于添加字幕的成片示意，未宣称自动识别或自动避让文字。"
    },
    {
      "location": "shot:2/block:1",
      "text": "豆浆也备好了，今天就卖这几样。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "这是早餐摊备料和菜单情境台词，不涉及产品能力。"
    },
    {
      "location": "shot:3/visual",
      "text": "镜头切到打包台，摊主把纸袋和餐盒摆好，最后将一只纸袋立起；对应字幕随口播出现。构图仅保留台面和双手，不出现顾客正脸。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "口播对应字幕由添加字幕能力支持，摆放用品和限制构图均为拍摄安排。"
    },
    {
      "location": "shot:3/block:1",
      "text": "纸袋、餐盒摆好，准备开摊。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "这是备料收尾台词，没有可验证的产品效果声明。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "第1镜7秒承载揭笼、字幕前后对照及两段依次口播，第2镜3.8秒用于菜单标记，第3镜3秒用于摆放包装用品；同拍声画同步计时，各镜均有具体动作支撑，无明显空镜凑时长。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
