# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成《把读书会的话留下》三分镜稿，覆盖签到桌、书页、分享者背影，介绍添加字幕和手动编辑字幕文字。估算21.8秒，符合24秒目标的90%—100%范围。无需进一步删改；实际成片时长仍以录制剪辑为准。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 把读书会的话留下

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

画面：签到桌近景：志愿者摆好书本，来宾签到后落座；镜头跟随手部动作，缓慢移向桌上的书。

旁白/字幕：签到桌旁，摆好书本，等大家落座。把读书会的话，留在这段记录里。

来源：

预计镜头时长：7.0 秒

### 分镜 2

画面：书页特写：手指停在准备分享的一行，翻页后停住。产品事实以文字卡呈现，旁白同步读出，不展示软件界面。

旁白/字幕：翻到想分享的那一页。剪影练习版支持为视频添加字幕。

来源：P01/P01.F1

预计镜头时长：6.3 秒

### 分镜 3

画面：分享者背影中景：保留自然讲述动作，将本镜旁白作为字幕叠加；镜头缓慢靠近，最后停在背影与书页同框的画面。

旁白/字幕：字幕文字可以手动编辑。镜头停在分享者背后，听完一句，再核对记录里的文字。

来源：P01/P01.F2

预计镜头时长：8.5 秒

## 审稿备注（不进入视频，不计入时长）

供创作者核对修改与资料缺口，不是经过事实认证的产品介绍。

仅介绍添加字幕和手动编辑字幕文字。事实卡均同步口播，不另计为并行阅读内容；场景与连接语为原创拍摄设计。时长待工具估算，尚未完成规则和需求检查。

时长要求：21.6–24 秒（接近目标）。

预计总时长：21.8 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "5d6447a2709e391d5c8d81fba372fe1e2633dface46ac5d34864ff65df2f5fed",
  "passed": true,
  "issues": [],
  "citations": [
    {
      "location": "shot:2/block:2",
      "source_id": "P01",
      "fact_id": "P01.F1",
      "quote": "剪影练习版支持为视频添加字幕。",
      "version": "2026-11-01"
    },
    {
      "location": "shot:3/block:1",
      "source_id": "P01",
      "fact_id": "P01.F2",
      "quote": "字幕文字可以手动编辑。",
      "version": "2026-11-01"
    }
  ],
  "rules_version": "2026-11-03-v1",
  "requires_expression_review": true,
  "expression_slots": [
    {
      "location": "title",
      "text": "把读书会的话留下"
    },
    {
      "location": "shot:1/visual",
      "text": "签到桌近景：志愿者摆好书本，来宾签到后落座；镜头跟随手部动作，缓慢移向桌上的书。"
    },
    {
      "location": "shot:1/block:1",
      "text": "签到桌旁，摆好书本，等大家落座。把读书会的话，留在这段记录里。"
    },
    {
      "location": "shot:2/visual",
      "text": "书页特写：手指停在准备分享的一行，翻页后停住。产品事实以文字卡呈现，旁白同步读出，不展示软件界面。"
    },
    {
      "location": "shot:2/block:1",
      "text": "翻到想分享的那一页。"
    },
    {
      "location": "shot:3/visual",
      "text": "分享者背影中景：保留自然讲述动作，将本镜旁白作为字幕叠加；镜头缓慢靠近，最后停在背影与书页同框的画面。"
    },
    {
      "location": "shot:3/block:2",
      "text": "镜头停在分享者背后，听完一句，再核对记录里的文字。"
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
  "scope": "exact_quote_and_brand_checks_only; expression semantics require independent model review"
}
```

## 需求覆盖核对

以下为模型评估，可能漏判或误判，仍需人工确认。

```json
{
  "ok": true,
  "script_hash": "5d6447a2709e391d5c8d81fba372fe1e2633dface46ac5d34864ff65df2f5fed",
  "request_hash": "19501a3419a2e7a54b42e8fa42d7c37ee31f2ee574c4a5de11438014ffcdbf26",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "介绍字幕添加",
      "verdict": "met",
      "evidence": "第2镜旁白明确介绍：“剪影练习版支持为视频添加字幕。”已由P01.F1核对支持。"
    },
    {
      "field": "topic",
      "requirement": "手动编辑字幕文字",
      "verdict": "met",
      "evidence": "第3镜旁白明确说明：“字幕文字可以手动编辑。”已由P01.F2核对支持。"
    },
    {
      "field": "topic",
      "requirement": "签到桌",
      "verdict": "met",
      "evidence": "第1镜为“签到桌近景”，安排志愿者摆书、来宾签到落座。"
    },
    {
      "field": "topic",
      "requirement": "书页",
      "verdict": "met",
      "evidence": "第2镜为“书页特写”，包含指向分享内容、翻页和停留；第3镜结尾也有书页同框。"
    },
    {
      "field": "topic",
      "requirement": "分享者背影",
      "verdict": "met",
      "evidence": "第3镜明确为“分享者背影中景”，结尾停在背影与书页同框的画面。"
    },
    {
      "field": "topic",
      "requirement": "恰好三个分镜",
      "verdict": "met",
      "evidence": "当前稿件共3个分镜，分别围绕签到桌、书页、分享者背影展开。"
    },
    {
      "field": "topic",
      "requirement": "标题用“把读书会的话留下”",
      "verdict": "met",
      "evidence": "当前标题为“把读书会的话留下”，与指定文字一致。"
    },
    {
      "field": "audience",
      "requirement": "图书馆活动志愿者",
      "verdict": "met",
      "evidence": "第1镜呈现志愿者布置签到桌，第2、3镜连接读书分享与活动文字记录，内容适合活动志愿者使用。"
    },
    {
      "field": "platform",
      "requirement": "视频号",
      "verdict": "met",
      "evidence": "采用三个简短分镜，以读书会实景、简明旁白和字幕呈现信息，适合视频号短视频观看。"
    },
    {
      "field": "style",
      "requirement": "温和",
      "verdict": "met",
      "evidence": "第1镜“等大家落座”、第3镜“听完一句”等措辞平和，配合缓慢移镜与自然讲述动作。"
    },
    {
      "field": "style",
      "requirement": "清楚",
      "verdict": "met",
      "evidence": "第2、3镜分别用直接短句介绍添加字幕和手动编辑字幕文字，两项功能表达明确。"
    }
  ],
  "summary": "已落实两项字幕功能、三个指定画面、分镜数量和标题要求，受众、平台及风格适配。表达有依据，节奏合理；估算总长21.8秒，已通过目标时长检查。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "把读书会的话留下",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "以读书会记录为主题的标题，不含具体产品能力或效果承诺。"
    },
    {
      "location": "shot:1/visual",
      "text": "签到桌近景：志愿者摆好书本，来宾签到后落座；镜头跟随手部动作，缓慢移向桌上的书。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于签到场景、人物动作和运镜安排，不含产品声明。"
    },
    {
      "location": "shot:1/block:1",
      "text": "签到桌旁，摆好书本，等大家落座。把读书会的话，留在这段记录里。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "描述活动准备与记录意愿，未承诺自动记录等产品能力。"
    },
    {
      "location": "shot:2/visual",
      "text": "书页特写：手指停在准备分享的一行，翻页后停住。产品事实以文字卡呈现，旁白同步读出，不展示软件界面。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "规定书页动作和事实文案的呈现方式，本段未新增产品能力、按钮或操作流程。"
    },
    {
      "location": "shot:2/block:1",
      "text": "翻到想分享的那一页。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于翻书动作的场景连接语，不含产品声明。"
    },
    {
      "location": "shot:3/visual",
      "text": "分享者背影中景：保留自然讲述动作，将本镜旁白作为字幕叠加；镜头缓慢靠近，最后停在背影与书页同框的画面。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "“将本镜旁白作为字幕叠加”展示添加字幕的能力，由P01.F1支持；其余为人物动作、运镜与构图安排。"
    },
    {
      "location": "shot:3/block:2",
      "text": "镜头停在分享者背后，听完一句，再核对记录里的文字。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "描述拍摄位置和人工核对文字的行动，不声称产品自动核对或纠错。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "第1镜预计7.0秒，26个口播单位配合摆书、签到落座和移镜；第2镜预计6.3秒，23个口播单位配合指向书页、翻页及同步事实卡；第3镜预计8.5秒，32个口播单位配合自然讲述、字幕观察和缓慢靠近。各镜均有具体内容支撑，未见重复事实或空镜凑时长；hold_seconds均为0不影响已估算的朗读与播放时间。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
