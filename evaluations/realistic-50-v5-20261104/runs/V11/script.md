# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成《字幕，让表达被看见》5镜脚本，预计36秒。用手写练习本和手机背面呈现字幕添加与手动改字，表达耐心简短，适合初学长者。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 字幕，让表达被看见

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

镜头目的：从一句日常用语开始，让学员准备字幕内容。

画面：俯拍手写练习本，手机背面朝上放在旁边。手在本上写下“今天去公园散步”，写完后用笔从左到右指读。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–3.5 秒**

旁白：先写一句话：今天去公园散步。

屏幕文字：今天去公园散步

镜头末尾保持画面：3.5–7.0 秒（保留最后一拍屏幕文字）

预计镜头时长：7.0 秒

### 分镜 2

镜头目的：介绍添加字幕的能力，用纸上示意展示文字进入画面。

画面：练习本翻到画有散步小画和横向方框的一页。手将写着“今天去公圆散步”的纸条放入方框下部，作为下一镜检查的例子。手机保持背面朝上，不展示软件界面。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–4.0 秒**

旁白＋同步字幕：剪影练习版支持为视频添加字幕。

依据：P01/P01.F1

**第 2 拍 · 镜内 4.0–7.3 秒**

旁白：这里用纸笔演示。

屏幕文字：纸上示意
今天去公圆散步

镜头末尾保持画面：7.3–8.0 秒（保留最后一拍屏幕文字）

预计镜头时长：8.0 秒

### 分镜 3

镜头目的：带学员逐字检查，发现例句中的错字。

画面：近拍练习本上的字幕纸条。笔尖依次指过文字，在“圆”字下停住，再轻轻圈出这个字；手机背面留在画面边缘。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–3.5 秒**

旁白：再读一遍。这里的“圆”字，写错了。

屏幕文字：今天去公圆散步

镜头末尾保持画面：3.5–7.0 秒（保留最后一拍屏幕文字）

预计镜头时长：7.0 秒

### 分镜 4

镜头目的：介绍手动编辑字幕的能力，并用纸笔示意改正一个字。

画面：保持纸上练习的近景。手划去纸条中的“圆”，在上方写上“园”，笔尖先指错字，再指改好的字，留出看清前后变化的时间。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–3.0 秒**

旁白＋同步字幕：字幕文字可以手动编辑。

依据：P01/P01.F2

**第 2 拍 · 镜内 3.0–6.0 秒**

旁白：把这个“圆”，改成公园的“园”。

屏幕文字：圆 → 园

镜头末尾保持画面：6.0–8.0 秒（保留最后一拍屏幕文字）

预计镜头时长：8.0 秒

### 分镜 5

镜头目的：复读修改后的句子，邀请学员开始自己的练习。

画面：镜头稍拉远，手指沿改好的句子再走一遍，然后移向练习本下一条空白横线，落笔准备写新句子。手机始终背面朝上。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–5.3 秒**

旁白：改好以后，再读一遍。接下来，您也写一句，练一练。

屏幕文字：今天去公园散步

镜头末尾保持画面：5.3–6.0 秒（保留最后一拍屏幕文字）

预计镜头时长：6.0 秒

时长要求：36.0–40 秒（接近目标）。

预计总时长：36.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "7b7e1cfb6f8773842d20a44b9bb795ed291e8ec7ede50dc109ffe62eb2d161b5",
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
      "location": "shot:4/block:1",
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
      "text": "俯拍手写练习本，手机背面朝上放在旁边。手在本上写下“今天去公园散步”，写完后用笔从左到右指读。"
    },
    {
      "location": "shot:1/block:1",
      "text": "先写一句话：今天去公园散步。"
    },
    {
      "location": "shot:1/block:2",
      "text": "今天去公园散步"
    },
    {
      "location": "shot:2/visual",
      "text": "练习本翻到画有散步小画和横向方框的一页。手将写着“今天去公圆散步”的纸条放入方框下部，作为下一镜检查的例子。手机保持背面朝上，不展示软件界面。"
    },
    {
      "location": "shot:2/block:1",
      "text": "剪影练习版支持为视频添加字幕。"
    },
    {
      "location": "shot:2/block:2",
      "text": "这里用纸笔演示。"
    },
    {
      "location": "shot:2/block:3",
      "text": "纸上示意\n今天去公圆散步"
    },
    {
      "location": "shot:3/visual",
      "text": "近拍练习本上的字幕纸条。笔尖依次指过文字，在“圆”字下停住，再轻轻圈出这个字；手机背面留在画面边缘。"
    },
    {
      "location": "shot:3/block:1",
      "text": "再读一遍。这里的“圆”字，写错了。"
    },
    {
      "location": "shot:3/block:2",
      "text": "今天去公圆散步"
    },
    {
      "location": "shot:4/visual",
      "text": "保持纸上练习的近景。手划去纸条中的“圆”，在上方写上“园”，笔尖先指错字，再指改好的字，留出看清前后变化的时间。"
    },
    {
      "location": "shot:4/block:1",
      "text": "字幕文字可以手动编辑。"
    },
    {
      "location": "shot:4/block:2",
      "text": "把这个“圆”，改成公园的“园”。"
    },
    {
      "location": "shot:4/block:3",
      "text": "圆 → 园"
    },
    {
      "location": "shot:5/visual",
      "text": "镜头稍拉远，手指沿改好的句子再走一遍，然后移向练习本下一条空白横线，落笔准备写新句子。手机始终背面朝上。"
    },
    {
      "location": "shot:5/block:1",
      "text": "改好以后，再读一遍。接下来，您也写一句，练一练。"
    },
    {
      "location": "shot:5/block:2",
      "text": "今天去公园散步"
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
  "script_hash": "7b7e1cfb6f8773842d20a44b9bb795ed291e8ec7ede50dc109ffe62eb2d161b5",
  "request_hash": "5d5f844deb8a130965b069c67d1de997138a045e7ec49210ef6cb066698c7050",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "介绍字幕添加",
      "verdict": "met",
      "evidence": "第2镜公开文案为“剪影练习版支持为视频添加字幕。”，配合将文字纸条放入纸上画面的示意。"
    },
    {
      "field": "topic",
      "requirement": "手动改字",
      "verdict": "met",
      "evidence": "第4镜说明“字幕文字可以手动编辑。”，并用纸笔演示将“圆”改为“园”。"
    },
    {
      "field": "topic",
      "requirement": "给第一次剪视频的长者看",
      "verdict": "met",
      "evidence": "第1至5镜围绕同一句生活用语，依次安排写句子、添加文字示意、检查、改字和复读；第5镜以“您也写一句，练一练”邀请参与，无需已有剪辑经验。"
    },
    {
      "field": "topic",
      "requirement": "手写练习本",
      "verdict": "met",
      "evidence": "第1镜在练习本上手写句子，第2至5镜持续使用练习本、纸条和笔进行演示。"
    },
    {
      "field": "topic",
      "requirement": "手机背面",
      "verdict": "met",
      "evidence": "第1、2、3、5镜明确安排手机背面入画，第4镜延续纸上练习近景；全稿未安排展示手机正面或软件界面。"
    },
    {
      "field": "topic",
      "requirement": "不假设能一键自动完成",
      "verdict": "met",
      "evidence": "第3、4镜安排逐字检查及手动改字；公开文案仅声明添加字幕和手动编辑能力，没有一键完成或自动化承诺。"
    },
    {
      "field": "topic",
      "requirement": "避免年轻人网络用语",
      "verdict": "met",
      "evidence": "全稿使用“今天去公园散步”“再读一遍”“练一练”等日常表达，未出现网络流行语。"
    },
    {
      "field": "audience",
      "requirement": "社区手机课堂学员",
      "verdict": "met",
      "evidence": "纸笔演示、逐字指读和第5镜的练习邀请适合课堂跟学；没有要求学员理解专业软件界面。"
    },
    {
      "field": "platform",
      "requirement": "视频号",
      "verdict": "met",
      "evidence": "稿件采用5镜短视频形式，配有中文旁白、简短屏幕文字和可观察的演示动作；预计36秒，适合视频号观看。"
    },
    {
      "field": "style",
      "requirement": "耐心",
      "verdict": "met",
      "evidence": "第1镜指读，第3镜停笔圈错字，第4镜留出前后对照时间，第5镜复读后邀请练习，推进温和且有观察空间。"
    },
    {
      "field": "style",
      "requirement": "短句",
      "verdict": "met",
      "evidence": "旁白以“这里用纸笔演示。”“再读一遍。”“改好以后，再读一遍。”等短句推进，没有复杂长句。"
    },
    {
      "field": "style",
      "requirement": "无术语",
      "verdict": "met",
      "evidence": "全稿以写句子、找错字和改字的日常说法解释功能；第4镜“手动编辑”后紧接“把这个‘圆’，改成公园的‘园’”，未引入需专业背景理解的术语。"
    }
  ],
  "summary": "原始要求均已落实，两处产品能力表述有原文支持，纸笔演示未虚构软件操作。预计36秒，符合宿主确认的目标区间；各镜停留有具体动作和观察内容支撑。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "字幕，让表达被看见",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于主题性表达，没有承诺具体产品性能、传播效果或自动化能力。"
    },
    {
      "location": "shot:1/visual",
      "text": "俯拍手写练习本，手机背面朝上放在旁边。手在本上写下“今天去公园散步”，写完后用笔从左到右指读。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅安排纸笔书写、手机摆放和指读动作，没有产品能力声明。"
    },
    {
      "location": "shot:1/block:1",
      "text": "先写一句话：今天去公园散步。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于练习引导及例句，不含产品承诺。"
    },
    {
      "location": "shot:1/block:2",
      "text": "今天去公园散步",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于练习例句，不涉及产品事实。"
    },
    {
      "location": "shot:2/visual",
      "text": "练习本翻到画有散步小画和横向方框的一页。手将写着“今天去公圆散步”的纸条放入方框下部，作为下一镜检查的例子。手机保持背面朝上，不展示软件界面。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "明确是练习本和纸条的拍摄示意，没有将方框冒充实际软件界面，也未虚构按钮、自动流程或产品操作步骤。"
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
      "evidence": "与P01.F1原文完全一致，仅声明为视频添加字幕，没有增加自动识别或一键完成能力。"
    },
    {
      "location": "shot:2/block:2",
      "text": "这里用纸笔演示。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "说明当前教学呈现方式，与练习本和纸条画面一致，不是产品能力声明。"
    },
    {
      "location": "shot:2/block:3",
      "text": "纸上示意\n今天去公圆散步",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "包含示意标识和供检查的错字例句，不含产品承诺。"
    },
    {
      "location": "shot:3/visual",
      "text": "近拍练习本上的字幕纸条。笔尖依次指过文字，在“圆”字下停住，再轻轻圈出这个字；手机背面留在画面边缘。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于人工指读和圈字的拍摄动作，没有声称软件能自动发现错误。"
    },
    {
      "location": "shot:3/block:1",
      "text": "再读一遍。这里的“圆”字，写错了。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "针对纸上例句进行读写教学，没有提出产品纠错能力声明。"
    },
    {
      "location": "shot:3/block:2",
      "text": "今天去公圆散步",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于刻意保留错字的练习文本，供下一镜修改，不涉及产品事实。"
    },
    {
      "location": "shot:4/visual",
      "text": "保持纸上练习的近景。手划去纸条中的“圆”，在上方写上“园”，笔尖先指错字，再指改好的字，留出看清前后变化的时间。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "明确展示纸笔改字和前后对照，没有将纸面动作描述为软件中的实际操作步骤。"
    },
    {
      "location": "shot:4/block:1",
      "text": "字幕文字可以手动编辑。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "与P01.F2原文完全一致，没有增加自动纠错、批量修改或其他编辑能力。"
    },
    {
      "location": "shot:4/block:2",
      "text": "把这个“圆”，改成公园的“园”。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "结合纸笔画面，这是具体改字练习指令，没有虚构软件按钮或自动工作流。"
    },
    {
      "location": "shot:4/block:3",
      "text": "圆 → 园",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "展示练习中的错字和正字对照，不构成额外产品能力声明。"
    },
    {
      "location": "shot:5/visual",
      "text": "镜头稍拉远，手指沿改好的句子再走一遍，然后移向练习本下一条空白横线，落笔准备写新句子。手机始终背面朝上。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于复读、转向下一次练习及取景安排，没有产品承诺。"
    },
    {
      "location": "shot:5/block:1",
      "text": "改好以后，再读一遍。接下来，您也写一句，练一练。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于检查建议和练习邀请，没有声称用户必然获得某种效果。"
    },
    {
      "location": "shot:5/block:2",
      "text": "今天去公园散步",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "展示修改后的练习例句，不涉及产品事实。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "按duration_check，各镜预计为7、8、7、8、6秒。第1镜书写并指读，支撑旁白后3.5秒停留；第2镜两个节拍共7.3秒，配合翻页和放纸条；第3镜逐字指读、停笔和圈字，支撑3.5秒观察时间；第4镜两个节拍共6秒，另有2秒用于看清改字对照；第5镜旁白约5.3秒，配合复读和落笔准备。重复例句分别承担检查、修改和复核任务，没有空镜凑时长；同拍声画无需重复累加。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
