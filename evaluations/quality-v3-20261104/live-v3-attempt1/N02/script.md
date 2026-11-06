# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成三镜头交接脚本：开场介绍社区旧物交换，中段分别介绍裁剪片段和手动编辑字幕，结尾回到交换现场，无节省时间承诺。当前稿无需删改，三项检查均通过；估算23.5秒，符合22.5至25秒要求，实际时长以成片为准。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 剪影练习版：社区旧物交换拍摄交接

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

画面：社区旧物交换活动全景，桌上摆着旧书和生活用品，老志愿者将拍摄设备交给新志愿者。以下文案为旁白。

旁白/字幕：新来的志愿者，欢迎接棒！今天记录社区旧物交换，先拍大家摆好物品。

来源：

预计镜头时长：7.5 秒

### 分镜 2

画面：以拍到的旧物和名称纸签为底图，依次叠加裁剪片段、手动编辑字幕的功能事实卡，卡片逐字使用对应事实块，不展示软件界面。全部文案按块顺序口播，事实卡与对应旁白同步显示。

旁白/字幕：剪影练习版支持裁剪视频片段。片段裁好后，核对字幕中的物品名称。字幕文字可以手动编辑。

来源：P02/P02.F1, P01/P01.F2

预计镜头时长：10.0 秒

### 分镜 3

画面：回到交换现场，镜头跟随双方递交旧物的双手，随后抬起拍到点头致谢的表情。以下文案为旁白。

旁白/字幕：最后回到交换现场，拍下双方交接物品，再记一声谢谢。

来源：

预计镜头时长：6.0 秒

时长要求：22.5–25 秒（接近目标）。

预计总时长：23.5 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "77aba424eabfee9a67188d90f5ba88a3169bc6cdcb37490af88a45cc38b22d3d",
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
      "location": "shot:2/block:3",
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
      "text": "剪影练习版：社区旧物交换拍摄交接"
    },
    {
      "location": "shot:1/visual",
      "text": "社区旧物交换活动全景，桌上摆着旧书和生活用品，老志愿者将拍摄设备交给新志愿者。以下文案为旁白。"
    },
    {
      "location": "shot:1/block:1",
      "text": "新来的志愿者，欢迎接棒！今天记录社区旧物交换，先拍大家摆好物品。"
    },
    {
      "location": "shot:2/visual",
      "text": "以拍到的旧物和名称纸签为底图，依次叠加裁剪片段、手动编辑字幕的功能事实卡，卡片逐字使用对应事实块，不展示软件界面。全部文案按块顺序口播，事实卡与对应旁白同步显示。"
    },
    {
      "location": "shot:2/block:2",
      "text": "片段裁好后，核对字幕中的物品名称。"
    },
    {
      "location": "shot:3/visual",
      "text": "回到交换现场，镜头跟随双方递交旧物的双手，随后抬起拍到点头致谢的表情。以下文案为旁白。"
    },
    {
      "location": "shot:3/block:1",
      "text": "最后回到交换现场，拍下双方交接物品，再记一声谢谢。"
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
  "script_hash": "77aba424eabfee9a67188d90f5ba88a3169bc6cdcb37490af88a45cc38b22d3d",
  "request_hash": "95af10ecf5b018c6c856f0f439ea4640c4d98b42f842a745079c7565df8e8ad0",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "做一条剪影练习版的交接说明",
      "verdict": "met",
      "evidence": "标题为“剪影练习版：社区旧物交换拍摄交接”；镜头1交接拍摄设备，后续说明拍摄内容和工具功能。"
    },
    {
      "field": "topic",
      "requirement": "使用社区旧物交换活动的拍摄场景",
      "verdict": "met",
      "evidence": "镜头1展示社区旧物交换全景、旧书和生活用品；镜头3展示双方递交旧物。"
    },
    {
      "field": "topic",
      "requirement": "裁剪视频片段",
      "verdict": "met",
      "evidence": "镜头2第1块明确介绍“剪影练习版支持裁剪视频片段。”，并同步显示功能卡。"
    },
    {
      "field": "topic",
      "requirement": "手动编辑字幕文字",
      "verdict": "met",
      "evidence": "镜头2第3块明确介绍“字幕文字可以手动编辑。”，并同步显示功能卡。"
    },
    {
      "field": "topic",
      "requirement": "用三个镜头",
      "verdict": "met",
      "evidence": "当前稿件恰有三个镜头。"
    },
    {
      "field": "topic",
      "requirement": "开场交代活动",
      "verdict": "met",
      "evidence": "镜头1旁白“今天记录社区旧物交换”，画面同步展示活动全景。"
    },
    {
      "field": "topic",
      "requirement": "中段说工具",
      "verdict": "met",
      "evidence": "镜头2介绍剪影练习版的片段裁剪和字幕文字手动编辑功能。"
    },
    {
      "field": "topic",
      "requirement": "结尾回到交换现场",
      "verdict": "met",
      "evidence": "镜头3画面明确“回到交换现场”，拍摄交接旧物和点头致谢。"
    },
    {
      "field": "topic",
      "requirement": "不许承诺节省多少时间",
      "verdict": "met",
      "evidence": "标题、全部画面说明及旁白均未出现节省时间的数字或效果承诺。"
    },
    {
      "field": "audience",
      "requirement": "刚加入的社区志愿者",
      "verdict": "met",
      "evidence": "镜头1用“新来的志愿者，欢迎接棒！”引入；拍物品、核对名称、记录交接等说明具体易懂。"
    },
    {
      "field": "platform",
      "requirement": "视频号",
      "verdict": "met",
      "evidence": "采用三个镜头的社区活动短视频形式，现场画面结合简短旁白与功能卡，适合信息流观看。"
    },
    {
      "field": "style",
      "requirement": "亲切直白",
      "verdict": "met",
      "evidence": "“欢迎接棒”“先拍大家摆好物品”“再记一声谢谢”等用语亲切，拍摄指示直接。"
    },
    {
      "field": "style",
      "requirement": "避免广告腔",
      "verdict": "met",
      "evidence": "工具段仅陈述两项功能；全文没有夸张卖点、购买引导或宣传口号。"
    }
  ],
  "summary": "全部明确需求均已覆盖，三镜头顺序、社区交换场景和两项功能介绍符合要求；无节省时间承诺，表达审核通过，停留安排合理。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "剪影练习版：社区旧物交换拍摄交接",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "标题标明工具名称、活动场景和交接主题，没有产品能力或效果承诺。"
    },
    {
      "location": "shot:1/visual",
      "text": "社区旧物交换活动全景，桌上摆着旧书和生活用品，老志愿者将拍摄设备交给新志愿者。以下文案为旁白。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "内容为社区活动及设备交接的拍摄安排，没有产品声明或真实客户背书。"
    },
    {
      "location": "shot:1/block:1",
      "text": "新来的志愿者，欢迎接棒！今天记录社区旧物交换，先拍大家摆好物品。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "内容为欢迎语、活动介绍及拍摄指示，不含产品能力或效果承诺。"
    },
    {
      "location": "shot:2/visual",
      "text": "以拍到的旧物和名称纸签为底图，依次叠加裁剪片段、手动编辑字幕的功能事实卡，卡片逐字使用对应事实块，不展示软件界面。全部文案按块顺序口播，事实卡与对应旁白同步显示。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P02",
          "fact_id": "P02.F1"
        },
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "裁剪片段和手动编辑字幕分别由P02.F1、P01.F2支持；卡片叠加、顺序口播和同步显示属于成片制作安排，未虚构产品界面或自动工作流。"
    },
    {
      "location": "shot:2/block:2",
      "text": "片段裁好后，核对字幕中的物品名称。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "这是衔接剪辑与人工核对名称的行动指示，没有新增产品能力、具体界面步骤或效果承诺。"
    },
    {
      "location": "shot:3/visual",
      "text": "回到交换现场，镜头跟随双方递交旧物的双手，随后抬起拍到点头致谢的表情。以下文案为旁白。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "描述现场人物动作、运镜和旁白安排，不含产品声明。"
    },
    {
      "location": "shot:3/block:1",
      "text": "最后回到交换现场，拍下双方交接物品，再记一声谢谢。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "内容为现场拍摄及收声指示，没有产品性能或自动化承诺。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "三个镜头的hold_seconds均为0，没有额外停留凑时长。镜头1旁白对应活动全景和设备交接；镜头2逐块口播、同步展示两张功能卡，并以核对名称衔接；镜头3旁白对应递交旧物、抬镜和致谢。各镜头均有明确观察或动作内容，没有重复事实或空镜拖延。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
