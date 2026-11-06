# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：脚本已完成，无需再修改。固定两镜：会议室空椅子介绍添加字幕，会议资料封面介绍横竖屏比例选项；不含会议发言内容或员工姓名。预计9秒，符合20秒上限。横竖取景框仅作构图示意。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 添加字幕与横竖屏比例

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

画面：会议室空椅子固定镜头，不出现人物、姓名标识或会议发言内容。本镜产品介绍旁白同步显示为字幕，不展示软件界面。

旁白/字幕：剪影练习版支持为视频添加字幕。

来源：P01/P01.F1

预计镜头时长：4.0 秒

### 分镜 2

画面：会议资料封面固定特写，封面仅写“会议资料”，不出现员工姓名或发言内容。在封面画面上叠加横向、竖向取景框作构图示意，主体始终为该封面，不展示软件界面。

旁白/字幕：剪影练习版提供横屏和竖屏画面比例选项。

来源：P03/P03.F1

预计镜头时长：5.0 秒

## 审稿备注（不进入视频，不计入时长）

供创作者核对修改与资料缺口，不是经过事实认证的产品介绍。

固定两个分镜，两条事实块均为产品介绍旁白。取景框仅作构图示意，不代表软件界面或操作流程。

预计总时长：9.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "c7bd9186bd5171a2255fbf11898c6e6e002de698815045b22b5f71bdd265159f",
  "passed": true,
  "issues": [],
  "citations": [
    {
      "location": "shot:1/block:1",
      "source_id": "P01",
      "fact_id": "P01.F1",
      "quote": "剪影练习版支持为视频添加字幕。",
      "version": "2026-11-01"
    },
    {
      "location": "shot:2/block:1",
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
      "text": "添加字幕与横竖屏比例"
    },
    {
      "location": "shot:1/visual",
      "text": "会议室空椅子固定镜头，不出现人物、姓名标识或会议发言内容。本镜产品介绍旁白同步显示为字幕，不展示软件界面。"
    },
    {
      "location": "shot:2/visual",
      "text": "会议资料封面固定特写，封面仅写“会议资料”，不出现员工姓名或发言内容。在封面画面上叠加横向、竖向取景框作构图示意，主体始终为该封面，不展示软件界面。"
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
  "script_hash": "c7bd9186bd5171a2255fbf11898c6e6e002de698815045b22b5f71bdd265159f",
  "request_hash": "ba2bdefd5f318c1b41a9d753aafc5e14453b6a56431a14aaa98befe8c588f8ca",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "介绍添加字幕",
      "verdict": "met",
      "evidence": "第1镜旁白为“剪影练习版支持为视频添加字幕。”，画面安排该旁白同步显示为字幕。"
    },
    {
      "field": "topic",
      "requirement": "横竖屏比例选项",
      "verdict": "met",
      "evidence": "第2镜旁白明确介绍“横屏和竖屏画面比例选项”，并叠加横向、竖向取景框作构图示意。"
    },
    {
      "field": "topic",
      "requirement": "固定两个分镜",
      "verdict": "met",
      "evidence": "稿件恰有两个分镜；字幕及取景框均安排在对应镜头内，没有另增镜头。"
    },
    {
      "field": "topic",
      "requirement": "第一镜会议室空椅子",
      "verdict": "met",
      "evidence": "第1镜画面明确为“会议室空椅子固定镜头”。"
    },
    {
      "field": "topic",
      "requirement": "第二镜会议资料封面",
      "verdict": "met",
      "evidence": "第2镜为“会议资料封面固定特写”，且明确“主体始终为该封面”。"
    },
    {
      "field": "topic",
      "requirement": "不出现发言内容和员工姓名。",
      "verdict": "met",
      "evidence": "发言内容限制已落实：两镜均明确排除会议发言内容；旁白仅介绍产品功能，没有会议发言。"
    },
    {
      "field": "topic",
      "requirement": "不出现发言内容和员工姓名。",
      "verdict": "met",
      "evidence": "员工姓名限制已落实：第1镜排除姓名标识，第2镜封面仅写“会议资料”；标题及旁白均未出现员工姓名。"
    },
    {
      "field": "audience",
      "requirement": "公司行政视频编辑",
      "verdict": "met",
      "evidence": "会议室和会议资料封面对应行政工作场景，字幕与画面比例介绍简明，适合行政视频编辑理解。"
    },
    {
      "field": "platform",
      "requirement": "视频号",
      "verdict": "met",
      "evidence": "两镜分别介绍一项功能，配合字幕和构图示意，信息集中，适合视频号短视频呈现。"
    },
    {
      "field": "style",
      "requirement": "简洁",
      "verdict": "met",
      "evidence": "每镜仅一句产品介绍，标题直接点明两项功能，没有冗余开场或结尾。"
    },
    {
      "field": "style",
      "requirement": "专业",
      "verdict": "met",
      "evidence": "使用会议场景与客观功能表述；取景框明确为构图示意，没有虚构软件界面或操作流程。"
    }
  ],
  "summary": "全部明确要求均已落实：两项功能介绍完整，两个分镜的数量、顺序和场景正确，未出现会议发言内容或员工姓名。表达审核通过，镜头节奏合理。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "添加字幕与横竖屏比例",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        },
        {
          "source_id": "P03",
          "fact_id": "P03.F1"
        }
      ],
      "evidence": "标题涉及添加字幕、横竖屏比例两项功能，分别由P01.F1和P03.F1支持，未附加自动化或效果承诺。"
    },
    {
      "location": "shot:1/visual",
      "text": "会议室空椅子固定镜头，不出现人物、姓名标识或会议发言内容。本镜产品介绍旁白同步显示为字幕，不展示软件界面。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "描述拍摄场景、内容排除和成片字幕安排；“旁白同步显示为字幕”没有宣称产品能够自动识别或自动同步字幕。"
    },
    {
      "location": "shot:2/visual",
      "text": "会议资料封面固定特写，封面仅写“会议资料”，不出现员工姓名或发言内容。在封面画面上叠加横向、竖向取景框作构图示意，主体始终为该封面，不展示软件界面。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "描述封面拍摄与构图示意，未声称自动调整比例，也未虚构产品按钮、界面布局或操作步骤。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "duration_check预计第1镜4秒、第2镜5秒，分别对应14和18个旁白单位，并满足4秒、5秒的最低停留。第1镜可阅读字幕并观察会议室，第2镜可观察封面及横竖取景框；两镜介绍不同功能，没有重复事实或空镜凑时长。宿主总长估算为9秒，已通过20秒上限检查。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
