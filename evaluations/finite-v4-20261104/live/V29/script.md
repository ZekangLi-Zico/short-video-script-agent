# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成7镜教学脚本，覆盖工作交接录像的片段裁剪、字幕安排与校对、横竖比例选择。当前稿无需删改，未虚构按钮操作或安排无意义长停留。估算56.2秒，符合54—60秒目标，三项检查均通过；实际成片时长仍以录制剪辑结果为准。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 一分钟，整理一段工作交接录像

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

画面：实习生观看现有工作交接录像，依次切换观看、记录和对照录像的近景。纸上记录仅取自录像实际内容。本稿所有 blocks 均为旁白，不另设产品事实文字卡。

旁白/字幕：接手工作录像，先看完，记下任务、负责人和截止时间。

来源：

预计镜头时长：5.8 秒

### 分镜 2

画面：先展示录像中完整的任务说明，再切到纸面记录，用笔标出拟保留片段的起止位置；不展示软件按钮或操作界面。

旁白/字幕：剪影练习版支持裁剪视频片段。圈出任务说明，标出开头结尾，保留必要上下文。

来源：P02/P02.F1

预计镜头时长：8.5 秒

### 分镜 3

画面：用纸面分段示意区分开场等待、重复闲聊和任务说明。若录像确有任务变更，连续展示原因与新安排；若没有，则展示实习生检查上下文的动作，不编造录像内容。

旁白/字幕：去掉开场等待和重复闲聊；任务有变更，就把原因和新安排一起留下。

来源：

预计镜头时长：7.5 秒

### 分镜 4

画面：在现有录像画面上示意分句字幕，文字严格对应实际原声；随讲述更换字幕与对应画面，字幕避开人物展示的交接信息。

旁白/字幕：剪影练习版支持为视频添加字幕。跟着讲述分句，把负责人和时间写清楚，别挡住关键信息。

来源：P01/P01.F1

预计镜头时长：9.8 秒

### 分镜 5

画面：实习生听原声并对照字幕稿，镜头依次移向录像中实际出现的姓名、数字或日期；用纸面校对示意，不虚构产品编辑界面。

旁白/字幕：字幕文字可以手动编辑。对照原声核对姓名、数字和日期，别改掉原意。

来源：P01/P01.F2

预计镜头时长：7.5 秒

### 分镜 6

画面：以现有录像静帧制作横屏和竖屏构图示意，明确标为构图示意；依次观察人物、横向资料和边缘信息在框内的位置，不展示或暗示产品会自动调整构图。

旁白/字幕：剪影练习版提供横屏和竖屏画面比例选项。看录像构图：横向信息多，优先横屏；人物集中，再考虑竖屏。

来源：P03/P03.F1

预计镜头时长：10.8 秒

### 分镜 7

画面：连续播放整理后的录像片段，切换任务说明、对应字幕和关键资料的近景；实习生对照交接记录逐项检查，结束于完成复看的动作。

旁白/字幕：最后看一遍：任务听得懂，字幕对得上，交接信息都能看清。

来源：

预计镜头时长：6.3 秒

时长要求：54.0–60 秒（接近目标）。

预计总时长：56.2 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "8c2c6e3b54e11b4a3a6b4ed930790e78c4cfbeda37ad2d5dbd22d46e99d179e8",
  "passed": true,
  "issues": [],
  "citations": [
    {
      "location": "shot:2/block:1",
      "source_id": "P02",
      "fact_id": "P02.F1",
      "quote": "剪影练习版支持裁剪视频片段。",
      "version": "2026-11-01"
    },
    {
      "location": "shot:4/block:1",
      "source_id": "P01",
      "fact_id": "P01.F1",
      "quote": "剪影练习版支持为视频添加字幕。",
      "version": "2026-11-01"
    },
    {
      "location": "shot:5/block:1",
      "source_id": "P01",
      "fact_id": "P01.F2",
      "quote": "字幕文字可以手动编辑。",
      "version": "2026-11-01"
    },
    {
      "location": "shot:6/block:1",
      "source_id": "P03",
      "fact_id": "P03.F1",
      "quote": "剪影练习版提供横屏和竖屏画面比例选项。",
      "version": "2026-11-01"
    }
  ],
  "rules_version": "2026-11-03-v1",
  "requires_expression_review": true,
  "expression_slots": [
    {
      "location": "title",
      "text": "一分钟，整理一段工作交接录像"
    },
    {
      "location": "shot:1/visual",
      "text": "实习生观看现有工作交接录像，依次切换观看、记录和对照录像的近景。纸上记录仅取自录像实际内容。本稿所有 blocks 均为旁白，不另设产品事实文字卡。"
    },
    {
      "location": "shot:1/block:1",
      "text": "接手工作录像，先看完，记下任务、负责人和截止时间。"
    },
    {
      "location": "shot:2/visual",
      "text": "先展示录像中完整的任务说明，再切到纸面记录，用笔标出拟保留片段的起止位置；不展示软件按钮或操作界面。"
    },
    {
      "location": "shot:2/block:2",
      "text": "圈出任务说明，标出开头结尾，保留必要上下文。"
    },
    {
      "location": "shot:3/visual",
      "text": "用纸面分段示意区分开场等待、重复闲聊和任务说明。若录像确有任务变更，连续展示原因与新安排；若没有，则展示实习生检查上下文的动作，不编造录像内容。"
    },
    {
      "location": "shot:3/block:1",
      "text": "去掉开场等待和重复闲聊；任务有变更，就把原因和新安排一起留下。"
    },
    {
      "location": "shot:4/visual",
      "text": "在现有录像画面上示意分句字幕，文字严格对应实际原声；随讲述更换字幕与对应画面，字幕避开人物展示的交接信息。"
    },
    {
      "location": "shot:4/block:2",
      "text": "跟着讲述分句，把负责人和时间写清楚，别挡住关键信息。"
    },
    {
      "location": "shot:5/visual",
      "text": "实习生听原声并对照字幕稿，镜头依次移向录像中实际出现的姓名、数字或日期；用纸面校对示意，不虚构产品编辑界面。"
    },
    {
      "location": "shot:5/block:2",
      "text": "对照原声核对姓名、数字和日期，别改掉原意。"
    },
    {
      "location": "shot:6/visual",
      "text": "以现有录像静帧制作横屏和竖屏构图示意，明确标为构图示意；依次观察人物、横向资料和边缘信息在框内的位置，不展示或暗示产品会自动调整构图。"
    },
    {
      "location": "shot:6/block:2",
      "text": "看录像构图：横向信息多，优先横屏；人物集中，再考虑竖屏。"
    },
    {
      "location": "shot:7/visual",
      "text": "连续播放整理后的录像片段，切换任务说明、对应字幕和关键资料的近景；实习生对照交接记录逐项检查，结束于完成复看的动作。"
    },
    {
      "location": "shot:7/block:1",
      "text": "最后看一遍：任务听得懂，字幕对得上，交接信息都能看清。"
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
  "scope": "exact_quote_and_brand_checks_only; expression semantics require independent model review"
}
```

## 需求覆盖核对

以下为模型评估，可能漏判或误判，仍需人工确认。

```json
{
  "ok": true,
  "script_hash": "8c2c6e3b54e11b4a3a6b4ed930790e78c4cfbeda37ad2d5dbd22d46e99d179e8",
  "request_hash": "e649bd32b380ab985c81ac5b1dd8cb23cf20267ebcbd534e6731c545f0d4c7e9",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "用一分钟左右",
      "verdict": "met",
      "evidence": "duration_check估算总长56.2秒，位于54—60秒目标区间，passed=true。"
    },
    {
      "field": "topic",
      "requirement": "围绕现有录像",
      "verdict": "met",
      "evidence": "第1镜从观看现有录像开始；第4镜字幕对应实际原声；第6镜使用现有录像静帧比较构图。"
    },
    {
      "field": "topic",
      "requirement": "字幕",
      "verdict": "met",
      "evidence": "第4镜讲分句、写清负责人和时间、避开关键信息；第5镜讲对照原声校对姓名、数字和日期。"
    },
    {
      "field": "topic",
      "requirement": "片段裁剪",
      "verdict": "met",
      "evidence": "第2镜标出保留片段的起止位置；第3镜提出去掉等待和重复闲聊，并保留任务变更的原因与新安排。"
    },
    {
      "field": "topic",
      "requirement": "比例选择",
      "verdict": "met",
      "evidence": "第6镜比较横屏与竖屏，并说明“横向信息多，优先横屏；人物集中，再考虑竖屏”。"
    },
    {
      "field": "topic",
      "requirement": "背景是工作交接",
      "verdict": "met",
      "evidence": "标题明确为“工作交接录像”；第1镜记录任务、负责人和截止时间，第7镜对照交接记录复查，业务场景具体。"
    },
    {
      "field": "topic",
      "requirement": "不要虚构按钮操作",
      "verdict": "met",
      "evidence": "第2镜明确不展示软件按钮或操作界面；第5镜使用纸面校对，第6镜标明构图示意。全稿未出现虚构按钮名称或产品操作步骤。"
    },
    {
      "field": "topic",
      "requirement": "不要同一画面无意义长停留",
      "verdict": "met",
      "evidence": "各镜头均安排切换、标记、校对或构图观察；最长的第6镜为10.8秒，有横竖构图比较及人物、资料、边缘信息的观察任务。"
    },
    {
      "field": "audience",
      "requirement": "工作室新来的运营实习生",
      "verdict": "met",
      "evidence": "以实习生接手录像为起点，使用“先看完”“标出开头结尾”“对照原声”等具体指引，适合新手理解和执行。"
    },
    {
      "field": "platform",
      "requirement": "B站",
      "verdict": "met",
      "evidence": "标题点明教程主题，分镜包含示意、对照和复查，形成完整的短教学内容，适合B站观看场景。"
    },
    {
      "field": "style",
      "requirement": "教学式",
      "verdict": "met",
      "evidence": "第2—6镜结合能力介绍与安排方法，说明如何保留上下文、校对字幕及选择比例，具有明确教学内容。"
    },
    {
      "field": "style",
      "requirement": "循序渐进",
      "verdict": "met",
      "evidence": "依次安排观看记录、确定裁剪、保留上下文、添加与校对字幕、选择比例、最终复查，步骤衔接清楚。"
    }
  ],
  "summary": "当前脚本已覆盖全部明确需求，预计56.2秒。工作交接场景具体，教学步骤清楚，未发现虚构操作、无依据的产品承诺或无意义长停留。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "一分钟，整理一段工作交接录像",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "结合一分钟教程语境，是内容标题，未宣称产品自动处理或保证一分钟完成实际工作。"
    },
    {
      "location": "shot:1/visual",
      "text": "实习生观看现有工作交接录像，依次切换观看、记录和对照录像的近景。纸上记录仅取自录像实际内容。本稿所有 blocks 均为旁白，不另设产品事实文字卡。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "描述观看、纸面记录、镜头切换及旁白安排，没有产品能力或效果承诺。"
    },
    {
      "location": "shot:1/block:1",
      "text": "接手工作录像，先看完，记下任务、负责人和截止时间。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "要求观看者人工梳理交接信息，没有宣称产品自动识别或提取信息。"
    },
    {
      "location": "shot:2/visual",
      "text": "先展示录像中完整的任务说明，再切到纸面记录，用笔标出拟保留片段的起止位置；不展示软件按钮或操作界面。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于纸面规划与拍摄安排，未虚构产品界面或具体操作步骤。"
    },
    {
      "location": "shot:2/block:2",
      "text": "圈出任务说明，标出开头结尾，保留必要上下文。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "是人工选择剪辑内容的建议，没有额外产品能力声明。"
    },
    {
      "location": "shot:3/visual",
      "text": "用纸面分段示意区分开场等待、重复闲聊和任务说明。若录像确有任务变更，连续展示原因与新安排；若没有，则展示实习生检查上下文的动作，不编造录像内容。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "用纸面演示内容取舍，并按录像实际内容安排画面，没有自动识别、自动剪辑或真实案例背书。"
    },
    {
      "location": "shot:3/block:1",
      "text": "去掉开场等待和重复闲聊；任务有变更，就把原因和新安排一起留下。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "提出人工剪辑的取舍原则，未声称软件会自动判断或处理这些内容。"
    },
    {
      "location": "shot:4/visual",
      "text": "在现有录像画面上示意分句字幕，文字严格对应实际原声；随讲述更换字幕与对应画面，字幕避开人物展示的交接信息。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "展示为视频添加字幕，由P01.F1支持；分句、原声对应和避挡是示意画面的制作要求，未宣称自动转写、自动同步或自动避挡。"
    },
    {
      "location": "shot:4/block:2",
      "text": "跟着讲述分句，把负责人和时间写清楚，别挡住关键信息。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "是字幕内容与呈现方式的人工安排建议，没有承诺产品自动分句、识别负责人或调整位置。"
    },
    {
      "location": "shot:5/visual",
      "text": "实习生听原声并对照字幕稿，镜头依次移向录像中实际出现的姓名、数字或日期；用纸面校对示意，不虚构产品编辑界面。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "描述人工听音校对和镜头安排，没有宣称自动纠错，也未设定产品界面。"
    },
    {
      "location": "shot:5/block:2",
      "text": "对照原声核对姓名、数字和日期，别改掉原意。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于人工校对要求，没有产品准确率或自动校正承诺。"
    },
    {
      "location": "shot:6/visual",
      "text": "以现有录像静帧制作横屏和竖屏构图示意，明确标为构图示意；依次观察人物、横向资料和边缘信息在框内的位置，不展示或暗示产品会自动调整构图。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P03",
          "fact_id": "P03.F1"
        }
      ],
      "evidence": "横屏、竖屏两种比例由P03.F1支持；画面明确为构图示意，未增加自动构图、智能追踪或特定界面操作声明。"
    },
    {
      "location": "shot:6/block:2",
      "text": "看录像构图：横向信息多，优先横屏；人物集中，再考虑竖屏。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "根据内容提出人工选择比例的建议，没有宣称产品自动推荐比例或保证传播效果。"
    },
    {
      "location": "shot:7/visual",
      "text": "连续播放整理后的录像片段，切换任务说明、对应字幕和关键资料的近景；实习生对照交接记录逐项检查，结束于完成复看的动作。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "安排成片复看与人工检查，没有新增产品功能、自动验收流程或效果保证。"
    },
    {
      "location": "shot:7/block:1",
      "text": "最后看一遍：任务听得懂，字幕对得上，交接信息都能看清。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "“最后看一遍”引出人工复查标准，未把清晰、准确等目标表述为产品保证的结果。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "第1镜5.8秒配21个旁白单位，切换观看、记录和对照；第2镜8.5秒配32个单位，展示任务说明并标记起止；第3镜7.5秒配28个单位，分段示意与检查上下文；第4镜9.8秒配37个单位，随讲述更换字幕和画面；第5镜7.5秒配28个单位，听原声并校对具体信息；第6镜10.8秒配41个单位，比较横竖构图并观察框内内容；第7镜6.3秒配23个单位，复看并逐项检查。各镜均有相应观察或动作内容，无明显重复凑时长；hold_seconds均为0仅表示没有额外最低停留要求。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
