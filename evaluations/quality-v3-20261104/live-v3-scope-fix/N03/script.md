# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成三镜头脚本，画面依次为巷口、门牌、门口，只介绍添加字幕，以核对门牌号的平实提醒收尾，未加入裁剪、导航、翻译或识别能力。本次修订仅将末镜最短停留从3秒增至6秒，其余内容保留。估算总时长13.8秒，符合20秒上限；三项检查均通过，无待补事项。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 给民宿入住指引加字幕

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

画面：实拍巷口，稳定展示周边环境；本镜头旁白同步显示为字幕。

旁白/字幕：拍民宿入住指引，先从巷口开始。

来源：

预计镜头时长：3.8 秒

### 分镜 2

画面：切到实际门牌的近景；本镜头产品事实作为旁白，同步显示为字幕，避开门牌文字。

旁白/字幕：剪影练习版支持为视频添加字幕。

来源：P01/P01.F1

预计镜头时长：4.0 秒

### 分镜 3

画面：切到民宿门口，稳定展示入口；本镜头旁白同步显示为字幕。

旁白/字幕：最后拍到门口。发之前，记得核对字幕里的门牌号。

来源：

预计镜头时长：6.0 秒

## 实际修订

位置按镜头索引比较；日志关联的是实际反馈，不证明模型因果推理。

- 修改：shot:3/hold_seconds；保留原镜头 2 个、原文案块 3 个。
- 修订前失败检查：requirements_check

预计总时长：13.8 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "110c950ac10ded0109cd278e6167695bf52a1c316bfee83d488c5e9381a3131a",
  "passed": true,
  "issues": [],
  "citations": [
    {
      "location": "shot:2/block:1",
      "source_id": "P01",
      "fact_id": "P01.F1",
      "quote": "剪影练习版支持为视频添加字幕。",
      "version": "2026-11-01"
    }
  ],
  "rules_version": "2026-11-03-v1",
  "requires_expression_review": true,
  "expression_slots": [
    {
      "location": "title",
      "text": "给民宿入住指引加字幕"
    },
    {
      "location": "shot:1/visual",
      "text": "实拍巷口，稳定展示周边环境；本镜头旁白同步显示为字幕。"
    },
    {
      "location": "shot:1/block:1",
      "text": "拍民宿入住指引，先从巷口开始。"
    },
    {
      "location": "shot:2/visual",
      "text": "切到实际门牌的近景；本镜头产品事实作为旁白，同步显示为字幕，避开门牌文字。"
    },
    {
      "location": "shot:3/visual",
      "text": "切到民宿门口，稳定展示入口；本镜头旁白同步显示为字幕。"
    },
    {
      "location": "shot:3/block:1",
      "text": "最后拍到门口。发之前，记得核对字幕里的门牌号。"
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
  "script_hash": "110c950ac10ded0109cd278e6167695bf52a1c316bfee83d488c5e9381a3131a",
  "request_hash": "a427b60f9535bafce97f71bba52e3608a49f3595d0ba37cda883e76798d9a9f7",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "写一条介绍剪影练习版字幕功能的分享",
      "verdict": "met",
      "evidence": "标题为“给民宿入住指引加字幕”；镜头2旁白明确介绍“剪影练习版支持为视频添加字幕。”，且该句已获rules_check核对支持。"
    },
    {
      "field": "topic",
      "requirement": "画面依次是巷口、门牌、门口。",
      "verdict": "met",
      "evidence": "镜头1“实拍巷口”，镜头2“切到实际门牌的近景”，镜头3“切到民宿门口”，内容及顺序均符合要求。"
    },
    {
      "field": "topic",
      "requirement": "只讲添加字幕",
      "verdict": "met",
      "evidence": "全稿出现的产品功能仅为添加字幕；旁白同步显示是成片安排，核对门牌号是人工提醒，未介绍其他产品功能。"
    },
    {
      "field": "topic",
      "requirement": "不讲裁剪。",
      "verdict": "met",
      "evidence": "标题、三个镜头的画面描述及旁白均未介绍裁剪功能；“切到”描述镜头转换。"
    },
    {
      "field": "topic",
      "requirement": "不要虚构导航、翻译或识别能力。",
      "verdict": "met",
      "evidence": "导航方面：巷口、门牌、门口均为实拍场景，未声称产品能够导航或生成路线。"
    },
    {
      "field": "topic",
      "requirement": "不要虚构导航、翻译或识别能力。",
      "verdict": "met",
      "evidence": "翻译方面：全稿未出现翻译、多语言转换等能力声明。"
    },
    {
      "field": "topic",
      "requirement": "不要虚构导航、翻译或识别能力。",
      "verdict": "met",
      "evidence": "识别方面：“旁白同步显示为字幕”属于拍摄制作安排，未声明自动识别语音或门牌；结尾要求店主自行核对门牌号。"
    },
    {
      "field": "topic",
      "requirement": "最后用一句平实提醒收尾。",
      "verdict": "met",
      "evidence": "最后一句为“发之前，记得核对字幕里的门牌号。”，属于平实、具体的发布前提醒。"
    },
    {
      "field": "audience",
      "requirement": "自行拍摄入住指引的民宿店主",
      "verdict": "met",
      "evidence": "镜头1明确说“拍民宿入住指引”；三个实拍位置呈现入住指引场景，结尾的门牌号核对提醒适合自行拍摄的店主。"
    },
    {
      "field": "platform",
      "requirement": "抖音",
      "verdict": "met",
      "evidence": "采用三个直观实拍镜头、短句旁白和同步字幕，内容单一清楚，适合短视频观看。"
    },
    {
      "field": "style",
      "requirement": "简洁",
      "verdict": "met",
      "evidence": "三个镜头分别交代拍摄起点、字幕功能和收尾提醒，没有长篇解释或冗余功能介绍。"
    },
    {
      "field": "style",
      "requirement": "口语化",
      "verdict": "met",
      "evidence": "“先从巷口开始”“最后拍到门口”“发之前，记得核对”等表达自然口语化。"
    }
  ],
  "summary": "当前稿件满足原始需求：镜头顺序正确，只介绍添加字幕，民宿入住指引场景明确，结尾提醒平实；未发现额外能力声明或明显不合理的停留。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "给民宿入住指引加字幕",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "标题表达为入住指引视频添加字幕，属于P01.F1支持的视频添加字幕能力，没有延伸出导航、识别或其他效果承诺。"
    },
    {
      "location": "shot:1/visual",
      "text": "实拍巷口，稳定展示周边环境；本镜头旁白同步显示为字幕。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "整项描述实拍场景、稳定展示和成片字幕安排；“同步显示”未声称产品自动识别或自动生成字幕。"
    },
    {
      "location": "shot:1/block:1",
      "text": "拍民宿入住指引，先从巷口开始。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "说明拍摄用途与起始位置，不包含产品能力或效果承诺。"
    },
    {
      "location": "shot:2/visual",
      "text": "切到实际门牌的近景；本镜头产品事实作为旁白，同步显示为字幕，避开门牌文字。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "整项安排门牌近景、旁白呈现和字幕避让，没有虚构产品界面、按钮、自动避让或识别步骤。"
    },
    {
      "location": "shot:3/visual",
      "text": "切到民宿门口，稳定展示入口；本镜头旁白同步显示为字幕。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "描述入口实拍与旁白字幕的成片呈现，不包含额外产品能力声明。"
    },
    {
      "location": "shot:3/block:1",
      "text": "最后拍到门口。发之前，记得核对字幕里的门牌号。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "前句交代拍摄顺序，后句提醒发布者人工核对信息，未承诺产品能自动识别或校验门牌号。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "镜头1停留3秒，约13字旁白并展示巷口；镜头2停留3秒，约14字旁白并展示门牌近景，字幕明确避开门牌文字；镜头3停留6秒，约20字旁白并稳定展示入口。各镜头均有对应阅读和观察内容，没有重复同一事实或明显空镜凑时长。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → estimate_duration → check_rules → check_requirements → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
