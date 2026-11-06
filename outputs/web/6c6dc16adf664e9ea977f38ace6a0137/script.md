# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成《字幕，让表达被看见》三镜脚本，预计16秒，符合28秒上限。展示领养日花絮添加字幕及手动修改文字，画面仅拍笼牌、牵引绳和志愿者手部，不含真实姓名或联系方式。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 字幕，让表达被看见

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

镜头目的：交代领养日记录场景，保持人物和联系信息不入镜。

画面：特写志愿者手部摆正仅写“领养日”的道具笼牌，再将牵引绳轻轻移到笼牌旁。背景虚化，不出现其他可辨识主体或文字。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–2.8 秒**

旁白＋同步字幕：从一段日常记录开始。

镜头末尾保持画面：2.8–3.0 秒（保留最后一拍屏幕文字）

预计镜头时长：3.0 秒

### 分镜 2

镜头目的：介绍添加字幕功能，让观众看到领养日花絮配上文字后的样子。

画面：近景拍志愿者双手整理牵引绳，笼牌留在画面边缘。动作开始时叠加示例字幕“整理牵引绳”，持续展示至绳圈收拢。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–5.0 秒**

旁白：剪影练习版支持为视频添加字幕。

依据：P01/P01.F1

屏幕文字：整理牵引绳

预计镜头时长：5.0 秒

### 分镜 3

镜头目的：说明字幕文字可以手动修改，并用同一花絮展示修改前后的具体文字。

画面：同一段手部收好牵引绳的近景先后播放两次：第一次展示修改前字幕，第二次硬切到手动修改后的字幕。用成片对照呈现，不展示软件界面或文字自动变化动画。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–4.0 秒**

旁白：字幕文字可以手动编辑。

依据：P01/P01.F2

屏幕文字：修改前：整理牵引绳

**第 2 拍 · 镜内 4.0–8.0 秒**

屏幕文字：手动修改后：收好牵引绳

预计镜头时长：8.0 秒

预计总时长：16.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "37cce1d7c447bc34b959d847242f5acd48b918cf187c3e183c92cf295ba9472d",
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
      "text": "字幕，让表达被看见"
    },
    {
      "location": "shot:1/visual",
      "text": "特写志愿者手部摆正仅写“领养日”的道具笼牌，再将牵引绳轻轻移到笼牌旁。背景虚化，不出现其他可辨识主体或文字。"
    },
    {
      "location": "shot:1/block:1",
      "text": "从一段日常记录开始。"
    },
    {
      "location": "shot:2/visual",
      "text": "近景拍志愿者双手整理牵引绳，笼牌留在画面边缘。动作开始时叠加示例字幕“整理牵引绳”，持续展示至绳圈收拢。"
    },
    {
      "location": "shot:2/block:1",
      "text": "剪影练习版支持为视频添加字幕。"
    },
    {
      "location": "shot:2/block:2",
      "text": "整理牵引绳"
    },
    {
      "location": "shot:3/visual",
      "text": "同一段手部收好牵引绳的近景先后播放两次：第一次展示修改前字幕，第二次硬切到手动修改后的字幕。用成片对照呈现，不展示软件界面或文字自动变化动画。"
    },
    {
      "location": "shot:3/block:1",
      "text": "字幕文字可以手动编辑。"
    },
    {
      "location": "shot:3/block:2",
      "text": "修改前：整理牵引绳"
    },
    {
      "location": "shot:3/block:3",
      "text": "手动修改后：收好牵引绳"
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
  "script_hash": "37cce1d7c447bc34b959d847242f5acd48b918cf187c3e183c92cf295ba9472d",
  "request_hash": "5c0b0575b38040eae7c360d4797877a9d0ce4b18e4b26ee4c709496cad63c2dd",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "做一条工具介绍",
      "verdict": "met",
      "evidence": "第2镜点名“剪影练习版”并介绍添加字幕，第3镜介绍字幕文字手动编辑，构成工具功能介绍。"
    },
    {
      "field": "topic",
      "requirement": "领养日花絮",
      "verdict": "met",
      "evidence": "第1镜道具笼牌明确写“领养日”，第2、3镜展示志愿者手部整理牵引绳，具体体现领养日记录场景。"
    },
    {
      "field": "topic",
      "requirement": "添加字幕",
      "verdict": "met",
      "evidence": "第2镜旁白“剪影练习版支持为视频添加字幕。”，同时在牵引绳画面显示示例字幕“整理牵引绳”；P01.F1支持该能力。"
    },
    {
      "field": "topic",
      "requirement": "手动修改文字",
      "verdict": "met",
      "evidence": "第3镜旁白“字幕文字可以手动编辑。”，依次展示“修改前：整理牵引绳”和“手动修改后：收好牵引绳”；P01.F2支持该能力。"
    },
    {
      "field": "topic",
      "requirement": "画面只拍笼牌、牵引绳和志愿者手部",
      "verdict": "met",
      "evidence": "第1镜仅拍手部、道具笼牌和牵引绳，并明确背景无其他可辨识主体；第2、3镜延续这些对象，第3镜明确不展示软件界面。"
    },
    {
      "field": "topic",
      "requirement": "不使用真实姓名和联系方式",
      "verdict": "met",
      "evidence": "笼牌仅写“领养日”，其他公开文字为功能介绍及动作示例；全部镜头与文案均未出现真实姓名或联系方式。"
    },
    {
      "field": "audience",
      "requirement": "动物救助志愿者",
      "verdict": "met",
      "evidence": "用领养日、笼牌及志愿者整理牵引绳的记录示范字幕功能，贴合动物救助志愿者的活动记录需求，说明通俗。"
    },
    {
      "field": "platform",
      "requirement": "视频号",
      "verdict": "met",
      "evidence": "三镜短篇采用中文旁白、简短屏幕文字和直观前后对照，适合视频号观看；宿主估算总长16秒。"
    },
    {
      "field": "style",
      "requirement": "温暖",
      "verdict": "met",
      "evidence": "第1镜“轻轻移到笼牌旁”的动作及标题“字幕，让表达被看见”，营造温和、关照表达的氛围。"
    },
    {
      "field": "style",
      "requirement": "不煽情",
      "verdict": "met",
      "evidence": "公开文案围绕日常记录和两项字幕功能，没有悲情叙述、夸张情绪或情感施压。"
    }
  ],
  "summary": "需求均已落实：领养日场景明确，两项字幕功能有资料支持，拍摄范围和隐私限制符合要求。预计16秒，符合28秒上限，节奏合理。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "字幕，让表达被看见",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于主题性表达，没有承诺传播量、识别准确率或其他可验证产品效果。"
    },
    {
      "location": "shot:1/visual",
      "text": "特写志愿者手部摆正仅写“领养日”的道具笼牌，再将牵引绳轻轻移到笼牌旁。背景虚化，不出现其他可辨识主体或文字。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于道具、动作及构图安排，未声称背景虚化由产品实现，也未引入产品能力承诺。"
    },
    {
      "location": "shot:1/block:1",
      "text": "从一段日常记录开始。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于场景引入语，不含产品能力或效果声明。"
    },
    {
      "location": "shot:2/visual",
      "text": "近景拍志愿者双手整理牵引绳，笼牌留在画面边缘。动作开始时叠加示例字幕“整理牵引绳”，持续展示至绳圈收拢。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "示例画面展示为视频添加字幕，受P01.F1支持；字幕出现时机是成片编排，没有宣称自动识别动作或自动生成字幕。"
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
      "evidence": "与P01.F1原文一致，未新增能力或效果承诺，引用与原块一致。"
    },
    {
      "location": "shot:2/block:2",
      "text": "整理牵引绳",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "是画面动作的示例字幕，不含产品能力声明。"
    },
    {
      "location": "shot:3/visual",
      "text": "同一段手部收好牵引绳的近景先后播放两次：第一次展示修改前字幕，第二次硬切到手动修改后的字幕。用成片对照呈现，不展示软件界面或文字自动变化动画。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        },
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "成片对照展示添加字幕和手动修改字幕文字，分别由P01.F1、P01.F2支持；未虚构按钮、软件布局或自动修改流程。"
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
      "evidence": "与P01.F2原文一致，引用与原块一致。"
    },
    {
      "location": "shot:3/block:2",
      "text": "修改前：整理牵引绳",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "标示示例字幕的修改前状态，文字内容为画面动作描述，没有额外产品承诺。"
    },
    {
      "location": "shot:3/block:3",
      "text": "手动修改后：收好牵引绳",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "展示手动编辑后的字幕文字，属于P01.F2支持的能力示例，没有宣称自动改写。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "第1镜3秒，声画同拍估算2.8秒，配合摆正笼牌及移动牵引绳；第2镜5秒，旁白约4秒，字幕持续5秒并伴随收拢绳圈动作；第3镜8秒，两个beat各4秒，分别展示修改前后文字，首拍旁白约3秒，次拍用于阅读和对照。重复片段服务于具体文字比较，未见空镜凑时长；并行声画无需相加，总长16秒且宿主判定通过。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
