# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成早餐摊备料场景的三镜脚本，只介绍添加字幕，按蒸笼、手写菜单、打包台排序，各镜均安排避开顾客正脸。预计17秒，符合25秒上限，三项检查均通过，本轮无需删改。时长为估算，实际以成片为准。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 早餐备料口播，加上字幕

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

画面：蒸笼近景，热气升起，只拍摊主揭盖的手。摊主画外音讲今日备料，同文字幕叠加在画面上。不出现顾客正脸。

旁白/字幕：今天先蒸包子，豆浆也备好了。

来源：

预计镜头时长：3.5 秒

### 分镜 2

画面：切到手写菜单近景，摊主把菜单摆正。第一段为摊主画外音，配同文字幕；第二段为同事分享口吻的产品介绍旁白，镜头仍保持菜单近景，不展示软件界面。不出现顾客正脸。

旁白/字幕：今日菜单写好，准备开摊。剪影练习版支持为视频添加字幕。

来源：P01/P01.F1

预计镜头时长：6.5 秒

### 分镜 3

画面：切到打包台俯拍，摊主双手整理打包盒。第一段为摊主画外音，配同文字幕；第二段为产品介绍旁白。保持桌面与手部构图，不出现顾客正脸。

旁白/字幕：打包盒摆好，今天的备料就这些。拍备料口播时，试着加上字幕吧。

来源：

预计镜头时长：7.0 秒

## 审稿备注（不进入视频，不计入时长）

供创作者核对修改与资料缺口，不是经过事实认证的产品介绍。

早餐备料台词为拍摄示例。产品介绍仅使用添加字幕这一项功能；画面呈现添加字幕后的示意效果，不设计未经确认的软件界面或操作步骤。所有文案块均作为口播串行安排，同文字幕不另读一遍。

预计总时长：17.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "2ed3c9cc898a7fb842c5d9f84414065bd0ecd4ce7b9bd81d85f7b0a3dcbef9c8",
  "passed": true,
  "issues": [],
  "citations": [
    {
      "location": "shot:2/block:2",
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
      "text": "早餐备料口播，加上字幕"
    },
    {
      "location": "shot:1/visual",
      "text": "蒸笼近景，热气升起，只拍摊主揭盖的手。摊主画外音讲今日备料，同文字幕叠加在画面上。不出现顾客正脸。"
    },
    {
      "location": "shot:1/block:1",
      "text": "今天先蒸包子，豆浆也备好了。"
    },
    {
      "location": "shot:2/visual",
      "text": "切到手写菜单近景，摊主把菜单摆正。第一段为摊主画外音，配同文字幕；第二段为同事分享口吻的产品介绍旁白，镜头仍保持菜单近景，不展示软件界面。不出现顾客正脸。"
    },
    {
      "location": "shot:2/block:1",
      "text": "今日菜单写好，准备开摊。"
    },
    {
      "location": "shot:3/visual",
      "text": "切到打包台俯拍，摊主双手整理打包盒。第一段为摊主画外音，配同文字幕；第二段为产品介绍旁白。保持桌面与手部构图，不出现顾客正脸。"
    },
    {
      "location": "shot:3/block:1",
      "text": "打包盒摆好，今天的备料就这些。"
    },
    {
      "location": "shot:3/block:2",
      "text": "拍备料口播时，试着加上字幕吧。"
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
  "script_hash": "2ed3c9cc898a7fb842c5d9f84414065bd0ecd4ce7b9bd81d85f7b0a3dcbef9c8",
  "request_hash": "4299792130470435332510610b8526e5f391e330ac68588a7ba5d1498ead5ad2",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "做一条剪影练习版字幕功能介绍",
      "verdict": "met",
      "evidence": "第2镜明确介绍“剪影练习版支持为视频添加字幕”，三镜均安排字幕效果示意。"
    },
    {
      "field": "topic",
      "requirement": "背景是早餐摊主讲今日备料",
      "verdict": "met",
      "evidence": "第1镜摊主讲“今天先蒸包子，豆浆也备好了”，第3镜讲“打包盒摆好，今天的备料就这些”，对应早餐摊备料场景。"
    },
    {
      "field": "topic",
      "requirement": "只介绍添加字幕",
      "verdict": "met",
      "evidence": "产品介绍和示意画面仅涉及添加字幕，未介绍手动编辑字幕、裁剪视频、画面比例或其他功能。"
    },
    {
      "field": "topic",
      "requirement": "画面按蒸笼、手写菜单、打包台的顺序",
      "verdict": "met",
      "evidence": "第1镜“蒸笼近景”，第2镜“手写菜单近景”，第3镜“打包台俯拍”，顺序一致。"
    },
    {
      "field": "topic",
      "requirement": "不要出现顾客正脸",
      "verdict": "met",
      "evidence": "三镜均明确“不出现顾客正脸”，构图分别限定为蒸笼与摊主手部、菜单近景、桌面与手部。"
    },
    {
      "field": "audience",
      "requirement": "小店新媒体兼职",
      "verdict": "met",
      "evidence": "使用早餐摊备料口播作为示例，并以“拍备料口播时，试着加上字幕吧”给出直接建议，表达简单，适合小店兼职内容制作人员。"
    },
    {
      "field": "platform",
      "requirement": "抖音",
      "verdict": "met",
      "evidence": "三镜围绕同一生活场景推进，搭配短口播与同文字幕；宿主估算总长17秒，适合短视频呈现。"
    },
    {
      "field": "style",
      "requirement": "像同事分享经验",
      "verdict": "met",
      "evidence": "第2镜指定“同事分享口吻”，第3镜用“拍备料口播时，试着加上字幕吧”自然提出建议。"
    },
    {
      "field": "style",
      "requirement": "短句",
      "verdict": "met",
      "evidence": "旁白使用“今日菜单写好，准备开摊”等短句，产品说明也仅为一句“剪影练习版支持为视频添加字幕”。"
    }
  ],
  "summary": "原始需求均已落实：早餐摊备料场景明确，只介绍添加字幕，镜头顺序正确，并避开顾客正脸。表达有资料支持，预计17秒，节奏合理。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "早餐备料口播，加上字幕",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "说明视频场景并提出添加字幕的行动邀请，未承诺自动化能力或额外效果。"
    },
    {
      "location": "shot:1/visual",
      "text": "蒸笼近景，热气升起，只拍摊主揭盖的手。摊主画外音讲今日备料，同文字幕叠加在画面上。不出现顾客正脸。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "“同文字幕叠加在画面上”展示添加字幕后的效果，由P01.F1支持；其余为拍摄安排，未声称自动生成字幕或展示未经确认的操作。"
    },
    {
      "location": "shot:1/block:1",
      "text": "今天先蒸包子，豆浆也备好了。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "早餐备料情境中的示例台词，不含产品能力或效果承诺。"
    },
    {
      "location": "shot:2/visual",
      "text": "切到手写菜单近景，摊主把菜单摆正。第一段为摊主画外音，配同文字幕；第二段为同事分享口吻的产品介绍旁白，镜头仍保持菜单近景，不展示软件界面。不出现顾客正脸。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "“配同文字幕”展示资料支持的添加字幕能力；菜单动作、旁白安排与构图均为拍摄说明，无额外产品声明。"
    },
    {
      "location": "shot:2/block:1",
      "text": "今日菜单写好，准备开摊。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "用于早餐摊场景衔接的示例台词，不含产品声明。"
    },
    {
      "location": "shot:3/visual",
      "text": "切到打包台俯拍，摊主双手整理打包盒。第一段为摊主画外音，配同文字幕；第二段为产品介绍旁白。保持桌面与手部构图，不出现顾客正脸。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "“配同文字幕”由添加字幕事实支持；整理打包盒、旁白与手部构图属于拍摄安排，未增加其他能力或操作步骤。"
    },
    {
      "location": "shot:3/block:1",
      "text": "打包盒摆好，今天的备料就这些。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "收束早餐备料场景的示例台词，不含产品性能或用户背书。"
    },
    {
      "location": "shot:3/block:2",
      "text": "拍备料口播时，试着加上字幕吧。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于行动邀请，未承诺字幕带来的观看、传播或经营效果。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "第1镜预计3.5秒，12个口播单位配合揭盖与蒸汽观察；第2镜预计6.5秒，24个口播单位配合摆正菜单和字幕示意；第3镜预计7秒，26个口播单位配合整理打包盒与收尾建议。各镜均有旁白和动作支撑，无明显空镜或重复凑时长。hold_seconds均为0，表示无额外最低停留要求；同文字幕不重复朗读。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
