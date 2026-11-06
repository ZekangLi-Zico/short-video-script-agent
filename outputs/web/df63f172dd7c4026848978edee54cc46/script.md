# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成三镜分镜稿：先大厅屏、再手机，最后明确横屏与竖屏是两种可选画面比例。估算14秒，符合25秒上限，三项检查均通过。当前稿无需删改，未宣称自动同步裁剪或自动追踪人物，无待补事项。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 横屏与竖屏：两种可选画面比例

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

画面：大厅全景，镜头推向正在播放活动画面的横向大屏，展示实际观看场景。

旁白/字幕：先看大厅屏的播放场景。

来源：

预计镜头时长：4.0 秒

### 分镜 2

画面：切到手持竖向手机观看活动画面的近景。通过直接切镜呈现场景，不展示画面转换过程或产品操作界面。

旁白/字幕：再看手机上的观看场景。

来源：

预计镜头时长：4.0 秒

### 分镜 3

画面：简洁背景并列展示横向、竖向两个画框示意，分别标注“横屏”“竖屏”，上方显示“两种可选画面比例”。

旁白/字幕：剪影练习版提供横屏和竖屏画面比例选项。

来源：P03/P03.F1

预计镜头时长：6.0 秒

## 审稿备注（不进入视频，不计入时长）

供创作者核对修改与资料缺口，不是经过事实认证的产品介绍。

所有 blocks 均为旁白，可同步配字幕。末镜标签为同步屏幕信息，不另行朗读。大厅屏和手机为拍摄场景示意，不表现自动同步裁剪或自动追踪人物。内容仅涉及两种画面比例选项。

预计总时长：14.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "e8532c69f4ca91ff896afc59ef15149c9a664b47f153baed8cb4961a30bd69f1",
  "passed": true,
  "issues": [],
  "citations": [
    {
      "location": "shot:3/block:1",
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
      "text": "横屏与竖屏：两种可选画面比例"
    },
    {
      "location": "shot:1/visual",
      "text": "大厅全景，镜头推向正在播放活动画面的横向大屏，展示实际观看场景。"
    },
    {
      "location": "shot:1/block:1",
      "text": "先看大厅屏的播放场景。"
    },
    {
      "location": "shot:2/visual",
      "text": "切到手持竖向手机观看活动画面的近景。通过直接切镜呈现场景，不展示画面转换过程或产品操作界面。"
    },
    {
      "location": "shot:2/block:1",
      "text": "再看手机上的观看场景。"
    },
    {
      "location": "shot:3/visual",
      "text": "简洁背景并列展示横向、竖向两个画框示意，分别标注“横屏”“竖屏”，上方显示“两种可选画面比例”。"
    }
  ],
  "available_facts": [
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
  "script_hash": "e8532c69f4ca91ff896afc59ef15149c9a664b47f153baed8cb4961a30bd69f1",
  "request_hash": "8f83e2cbcbb2dd70c13429381120bdf2dd261a226dda5f319aca191d2a7b49e6",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "介绍横屏、竖屏画面比例选项",
      "verdict": "met",
      "evidence": "第3镜旁白明确介绍“提供横屏和竖屏画面比例选项”，画面并列展示两种画框，两项均有覆盖。"
    },
    {
      "field": "topic",
      "requirement": "说明这是两种可选画面比例",
      "verdict": "met",
      "evidence": "标题为“横屏与竖屏：两种可选画面比例”，第3镜屏幕文字也明确显示“两种可选画面比例”。"
    },
    {
      "field": "topic",
      "requirement": "场景先大厅屏再手机",
      "verdict": "met",
      "evidence": "第1镜展示大厅横向大屏播放活动画面，第2镜切到手持竖向手机观看活动画面，场景及顺序均符合要求。"
    },
    {
      "field": "topic",
      "requirement": "不要声称自动同步裁剪",
      "verdict": "met",
      "evidence": "全片未宣称自动同步裁剪；第2镜通过直接切镜呈现场景，明确不展示画面转换过程或产品操作界面。"
    },
    {
      "field": "topic",
      "requirement": "自动追踪人物",
      "verdict": "met",
      "evidence": "此项承接原文“不要声称……或……”的禁令。全片未宣称或演示自动追踪人物；第1镜的镜头推进仅为拍摄安排。"
    },
    {
      "field": "audience",
      "requirement": "活动视频外包剪辑师",
      "verdict": "met",
      "evidence": "第1、2镜均展示活动视频观看场景，第3镜介绍横竖屏比例选项，与活动视频剪辑师的内容交付场景相关。"
    },
    {
      "field": "platform",
      "requirement": "B站",
      "verdict": "met",
      "evidence": "稿件以明确标题、场景示例及画框对照完成简短功能介绍，适合B站视频呈现；无需在视频内直接说出平台名称。"
    },
    {
      "field": "style",
      "requirement": "客观",
      "verdict": "met",
      "evidence": "第3镜仅陈述资料支持的画面比例选项，第1、2镜说明观看场景，没有夸张效果或未经支持的能力承诺。"
    },
    {
      "field": "style",
      "requirement": "直截了当",
      "verdict": "met",
      "evidence": "标题直接点明两种比例，三镜旁白依次说明大厅屏、手机和比例选项，无无关铺垫或内部审稿说明。"
    }
  ],
  "summary": "全部明确需求均已落实：横竖屏两种可选比例表达清楚，场景先大厅屏再手机，未宣称自动同步裁剪或自动追踪人物。表达有据，节奏合理，宿主估算14秒，符合25秒上限。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "横屏与竖屏：两种可选画面比例",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P03",
          "fact_id": "P03.F1"
        }
      ],
      "evidence": "P03.F1明确提供横屏和竖屏画面比例选项，支持标题所述两种可选比例。"
    },
    {
      "location": "shot:1/visual",
      "text": "大厅全景，镜头推向正在播放活动画面的横向大屏，展示实际观看场景。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "这是大厅播放活动画面的场景及摄影安排，没有宣称产品投屏、自动转换或真实客户使用效果。"
    },
    {
      "location": "shot:1/block:1",
      "text": "先看大厅屏的播放场景。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅引导观众观看当前场景，不含产品能力或效果承诺。"
    },
    {
      "location": "shot:2/visual",
      "text": "切到手持竖向手机观看活动画面的近景。通过直接切镜呈现场景，不展示画面转换过程或产品操作界面。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅安排手机观看场景和剪辑方式，没有展示自动转换流程，也未虚构产品界面或操作步骤。"
    },
    {
      "location": "shot:2/block:1",
      "text": "再看手机上的观看场景。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅连接并介绍手机观看场景，不含可验证的产品承诺。"
    },
    {
      "location": "shot:3/visual",
      "text": "简洁背景并列展示横向、竖向两个画框示意，分别标注“横屏”“竖屏”，上方显示“两种可选画面比例”。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P03",
          "fact_id": "P03.F1"
        }
      ],
      "evidence": "两个画框和标签表达横屏、竖屏比例可选，均由P03.F1支持；画面明确为示意，没有声称具体产品界面或额外能力。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "duration_check中第1、2镜各4秒，分别配10个旁白单位，并安排大厅全景推进、手机近景供观察；第3镜6秒，配18个旁白单位及两种画框和标签对照，停留有明确内容支撑。三镜均满足各自hold_seconds最低停留要求，无明显重复凑时长；editor_notes不计入朗读。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
