# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：《收摊以后》三镜脚本已完成，预计17.5秒。按折叠桌→旧书→收摊纸箱展开，介绍裁剪片段与添加字幕，结尾无关注点赞话术。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 收摊以后

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

镜头目的：用裁剪前后的收桌片段，展示如何留下需要的动作。

画面：竖屏固定机位拍摊主收起折叠桌。先展示动作前的一小段等待，再重播裁剪后的片段，直接从折起桌腿开始。不展示软件界面。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–3.5 秒**

屏幕文字：收摊以后

旁白：用剪影练习版裁剪视频片段。

依据：P02/P02.F1

**第 2 拍 · 镜内 3.5–6.5 秒**

旁白：留下收起桌子的这一刻。

镜头末尾保持画面：6.5–7.0 秒（保留最后一拍屏幕文字）

预计镜头时长：7.0 秒

### 分镜 2

镜头目的：为整理旧书的画面添加一句字幕，让收摊记录有具体表达。

画面：近景拍矮凳上的旧书。摊主合上最上面的一本，将书摞齐；画面下方出现“旧书收好，故事还在。”，字幕保持到双手整理完毕。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–6.0 秒**

旁白：还可以为视频添加字幕。

依据：P01/P01.F1

屏幕文字：旧书收好，故事还在。

预计镜头时长：6.0 秒

### 分镜 3

镜头目的：以装箱收摊的动作结束这段市集记录。

画面：俯拍收摊纸箱，摊主把旧书放进去，折好箱盖，双手抱起纸箱离开画面。保留纸箱摩擦与脚步声。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–3.0 秒**

旁白＋同步字幕：把今天收好，下周再摆。

镜头末尾保持画面：3.0–4.5 秒（保留最后一拍屏幕文字）

预计镜头时长：4.5 秒

预计总时长：17.5 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "6c28170ac377db1d5741590fd922e7bbe59a922b7ebcdb917edd5f4be881a565",
  "passed": true,
  "issues": [],
  "citations": [
    {
      "location": "shot:1/block:2",
      "source_id": "P02",
      "fact_id": "P02.F1",
      "quote": "剪影练习版支持裁剪视频片段。",
      "version": "2026-11-01",
      "text": "用剪影练习版裁剪视频片段。",
      "requires_semantic_review": true
    },
    {
      "location": "shot:2/block:1",
      "source_id": "P01",
      "fact_id": "P01.F1",
      "quote": "剪影练习版支持为视频添加字幕。",
      "version": "2026-11-01",
      "text": "还可以为视频添加字幕。",
      "requires_semantic_review": true
    }
  ],
  "rules_version": "2026-11-03-v1",
  "requires_expression_review": true,
  "expression_slots": [
    {
      "location": "title",
      "text": "收摊以后"
    },
    {
      "location": "shot:1/visual",
      "text": "竖屏固定机位拍摊主收起折叠桌。先展示动作前的一小段等待，再重播裁剪后的片段，直接从折起桌腿开始。不展示软件界面。"
    },
    {
      "location": "shot:1/block:1",
      "text": "收摊以后"
    },
    {
      "location": "shot:1/block:2",
      "text": "用剪影练习版裁剪视频片段。"
    },
    {
      "location": "shot:1/block:3",
      "text": "留下收起桌子的这一刻。"
    },
    {
      "location": "shot:2/visual",
      "text": "近景拍矮凳上的旧书。摊主合上最上面的一本，将书摞齐；画面下方出现“旧书收好，故事还在。”，字幕保持到双手整理完毕。"
    },
    {
      "location": "shot:2/block:1",
      "text": "还可以为视频添加字幕。"
    },
    {
      "location": "shot:2/block:2",
      "text": "旧书收好，故事还在。"
    },
    {
      "location": "shot:3/visual",
      "text": "俯拍收摊纸箱，摊主把旧书放进去，折好箱盖，双手抱起纸箱离开画面。保留纸箱摩擦与脚步声。"
    },
    {
      "location": "shot:3/block:1",
      "text": "把今天收好，下周再摆。"
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
  "script_hash": "6c28170ac377db1d5741590fd922e7bbe59a922b7ebcdb917edd5f4be881a565",
  "request_hash": "bceb0659a6ebdae1e0dc6ecf8ecaa4c0a9a8ee07337ab0c24112bb4db60db25d",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "介绍裁剪片段",
      "verdict": "met",
      "evidence": "第1镜旁白“用剪影练习版裁剪视频片段。”，画面对比裁剪前的等待与裁剪后直接折起桌腿的片段。"
    },
    {
      "field": "topic",
      "requirement": "添加字幕",
      "verdict": "met",
      "evidence": "第2镜旁白“还可以为视频添加字幕。”，同时显示示例字幕“旧书收好，故事还在。”。"
    },
    {
      "field": "topic",
      "requirement": "画面顺序为折叠桌、旧书、收摊纸箱。",
      "verdict": "met",
      "evidence": "第1镜收起折叠桌，第2镜整理旧书，第3镜将旧书装入收摊纸箱，顺序一致。"
    },
    {
      "field": "topic",
      "requirement": "标题用“收摊以后”",
      "verdict": "met",
      "evidence": "script.title为“收摊以后”，第1镜屏幕标题也为“收摊以后”。"
    },
    {
      "field": "topic",
      "requirement": "结尾不说关注点赞。",
      "verdict": "met",
      "evidence": "第3镜以“把今天收好，下周再摆。”结束，没有关注或点赞邀请。"
    },
    {
      "field": "audience",
      "requirement": "周末市集摊主",
      "verdict": "met",
      "evidence": "三镜围绕摊主收桌、整理旧书和装箱离场展开，“下周再摆”呼应每周出摊的生活场景。"
    },
    {
      "field": "platform",
      "requirement": "抖音",
      "verdict": "met",
      "evidence": "第1镜明确竖屏拍摄，全片以三个简短镜头呈现功能与收摊故事，配有屏幕文字；宿主预计总长17.5秒，适合短视频观看。"
    },
    {
      "field": "style",
      "requirement": "朴素",
      "verdict": "met",
      "evidence": "采用固定机位、旧书近景与纸箱俯拍，保留纸箱摩擦和脚步声，文案简洁，没有夸张宣传。"
    },
    {
      "field": "style",
      "requirement": "轻叙事",
      "verdict": "met",
      "evidence": "由收桌、收书推进到装箱离场，以“把今天收好，下周再摆。”自然收束，构成简短的收摊故事。"
    }
  ],
  "summary": "各项需求均已落实，产品表述有资料支持，节奏合理。宿主预计总长17.5秒，已通过22秒上限检查。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "收摊以后",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "叙事标题，不含产品能力或效果承诺。"
    },
    {
      "location": "shot:1/visual",
      "text": "竖屏固定机位拍摊主收起折叠桌。先展示动作前的一小段等待，再重播裁剪后的片段，直接从折起桌腿开始。不展示软件界面。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P02",
          "fact_id": "P02.F1"
        }
      ],
      "evidence": "裁掉等待、保留收桌动作的对比示意由“剪影练习版支持裁剪视频片段。”支持；其余为拍摄安排，没有新增自动化能力或虚构软件界面。"
    },
    {
      "location": "shot:1/block:1",
      "text": "收摊以后",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "屏幕标题，仅交代故事情境。"
    },
    {
      "location": "shot:1/block:2",
      "text": "用剪影练习版裁剪视频片段。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P02",
          "fact_id": "P02.F1"
        }
      ],
      "evidence": "与原文“剪影练习版支持裁剪视频片段。”含义一致，未增加功能或效果；引用与原块标注一致。"
    },
    {
      "location": "shot:1/block:3",
      "text": "留下收起桌子的这一刻。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "围绕收桌动作的叙事表达，没有额外产品性能或自动化承诺。"
    },
    {
      "location": "shot:2/visual",
      "text": "近景拍矮凳上的旧书。摊主合上最上面的一本，将书摞齐；画面下方出现“旧书收好，故事还在。”，字幕保持到双手整理完毕。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "视频画面添加字幕的示意由“剪影练习版支持为视频添加字幕。”支持；文字位置和停留为成片编排，没有声称自动生成或自动匹配动作。"
    },
    {
      "location": "shot:2/block:1",
      "text": "还可以为视频添加字幕。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "准确承接原文“剪影练习版支持为视频添加字幕。”，仅省去重复产品名；引用与原块标注一致。"
    },
    {
      "location": "shot:2/block:2",
      "text": "旧书收好，故事还在。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "配合整理旧书的情绪文案，不含产品承诺。"
    },
    {
      "location": "shot:3/visual",
      "text": "俯拍收摊纸箱，摊主把旧书放进去，折好箱盖，双手抱起纸箱离开画面。保留纸箱摩擦与脚步声。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "描述装箱、离场与现场声音的拍摄安排，没有声称产品具备音频处理等功能。"
    },
    {
      "location": "shot:3/block:1",
      "text": "把今天收好，下周再摆。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "收摊故事的结束语，不含可验证的产品能力或效果声明。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "第1镜预计7秒，两拍旁白依次占3.5秒和3秒，标题与首拍同步，裁剪前后对比支撑画面停留。第2镜预计6秒，3秒旁白与6秒字幕同步，合书、摞齐动作支撑余下观察时间。第3镜预计4.5秒，同文声画占3秒，随后1.5秒可延续抱箱离场与现场声音。各镜有明确动作或阅读内容，没有重复事实或无内容空镜凑时长。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
