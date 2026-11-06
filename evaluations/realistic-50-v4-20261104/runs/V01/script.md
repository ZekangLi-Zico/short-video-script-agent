# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：脚本已完成，无需删改。仅介绍添加字幕，以早餐摊主讲今日备料串联蒸笼、手写菜单、打包台，明确避开顾客正脸。估时约15秒，符合25秒上限；实际成片时长及事实卡阅读节奏需在剪辑时确认。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 今日备料，配上字幕

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

画面：蒸笼近景，蒸汽升起，只拍摊主揭盖的手。摊主画外音讲今日备料，成片叠加与旁白一致的字幕，展示添加字幕后的效果。不出现顾客正脸。

旁白/字幕：今天先把包子蒸上。

来源：

预计镜头时长：4.0 秒

### 分镜 2

画面：切到手写菜单特写，摊主写下包子、豆浆。第一块为摊主旁白及对应字幕；随后在菜单画面上展示第二块产品事实卡，事实卡不配旁白，留出阅读时间。不展示软件界面，不出现顾客正脸。

旁白/字幕：今天的菜单，包子、豆浆。剪影练习版支持为视频添加字幕。

来源：P01/P01.F1

预计镜头时长：7.0 秒

### 分镜 3

画面：切到打包台俯拍，摊主双手摆齐打包盒。摊主继续画外音，成片叠加与旁白一致的字幕，只展示添加字幕的效果。不出现顾客正脸。

旁白/字幕：打包盒也摆好了，准备开摊。

来源：

预计镜头时长：4.0 秒

预计总时长：15.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "dc9928131cd4abd9e221feec9100f66492efb50bdd1139e108aea17b92a7b453",
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
      "text": "今日备料，配上字幕"
    },
    {
      "location": "shot:1/visual",
      "text": "蒸笼近景，蒸汽升起，只拍摊主揭盖的手。摊主画外音讲今日备料，成片叠加与旁白一致的字幕，展示添加字幕后的效果。不出现顾客正脸。"
    },
    {
      "location": "shot:1/block:1",
      "text": "今天先把包子蒸上。"
    },
    {
      "location": "shot:2/visual",
      "text": "切到手写菜单特写，摊主写下包子、豆浆。第一块为摊主旁白及对应字幕；随后在菜单画面上展示第二块产品事实卡，事实卡不配旁白，留出阅读时间。不展示软件界面，不出现顾客正脸。"
    },
    {
      "location": "shot:2/block:1",
      "text": "今天的菜单，包子、豆浆。"
    },
    {
      "location": "shot:3/visual",
      "text": "切到打包台俯拍，摊主双手摆齐打包盒。摊主继续画外音，成片叠加与旁白一致的字幕，只展示添加字幕的效果。不出现顾客正脸。"
    },
    {
      "location": "shot:3/block:1",
      "text": "打包盒也摆好了，准备开摊。"
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
  "script_hash": "dc9928131cd4abd9e221feec9100f66492efb50bdd1139e108aea17b92a7b453",
  "request_hash": "4299792130470435332510610b8526e5f391e330ac68588a7ba5d1498ead5ad2",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "做一条剪影练习版字幕功能介绍",
      "verdict": "met",
      "evidence": "镜2事实卡明确写出“剪影练习版支持为视频添加字幕。”，镜1、镜3展示添加字幕后的效果。"
    },
    {
      "field": "topic",
      "requirement": "背景是早餐摊主讲今日备料",
      "verdict": "met",
      "evidence": "镜1由摊主画外音讲“今天先把包子蒸上。”，镜2展示包子、豆浆菜单，镜3摆放打包盒并说“准备开摊”，明确体现早餐摊今日备料。"
    },
    {
      "field": "topic",
      "requirement": "只介绍添加字幕",
      "verdict": "met",
      "evidence": "各镜只展示添加字幕的效果，镜2产品事实卡也仅介绍添加字幕；未介绍手动编辑字幕、裁剪视频或画面比例等其他功能。"
    },
    {
      "field": "topic",
      "requirement": "画面按蒸笼、手写菜单、打包台的顺序",
      "verdict": "met",
      "evidence": "镜1“蒸笼近景”，镜2“切到手写菜单特写”，镜3“切到打包台俯拍”，顺序一致。"
    },
    {
      "field": "topic",
      "requirement": "不要出现顾客正脸",
      "verdict": "met",
      "evidence": "三镜均明确注明“不出现顾客正脸”，并采用蒸笼及手部近景、菜单特写、打包台俯拍。"
    },
    {
      "field": "audience",
      "requirement": "小店新媒体兼职",
      "verdict": "met",
      "evidence": "以小店备料素材示范字幕效果，镜2使用简短功能说明，无专业术语，适合小店兼职内容制作人员理解。"
    },
    {
      "field": "platform",
      "requirement": "抖音",
      "verdict": "met",
      "evidence": "采用三个明确生活场景、短旁白和可见字幕，预计总长15秒，适合短视频观看。"
    },
    {
      "field": "style",
      "requirement": "像同事分享经验",
      "verdict": "met",
      "evidence": "镜1“今天先把包子蒸上。”、镜3“打包盒也摆好了，准备开摊。”语气自然平实，结合实际备料画面分享字幕使用示例。"
    },
    {
      "field": "style",
      "requirement": "短句",
      "verdict": "met",
      "evidence": "旁白均为简短单句，如“今天的菜单，包子、豆浆。”；产品说明也仅用一句“剪影练习版支持为视频添加字幕。”。"
    }
  ],
  "summary": "当前稿已落实全部需求，仅介绍添加字幕，场景、镜头顺序和避开顾客正脸均明确。产品表达有资料支持，节奏合理；预计15秒，符合25秒上限。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "今日备料，配上字幕",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "标题描述备料场景及字幕呈现安排，没有额外产品性能、自动化或效果承诺。"
    },
    {
      "location": "shot:1/visual",
      "text": "蒸笼近景，蒸汽升起，只拍摊主揭盖的手。摊主画外音讲今日备料，成片叠加与旁白一致的字幕，展示添加字幕后的效果。不出现顾客正脸。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "“展示添加字幕后的效果”由支持为视频添加字幕的事实支持；“与旁白一致”描述成片内容，未声称自动识别或同步。其余内容为拍摄安排。"
    },
    {
      "location": "shot:1/block:1",
      "text": "今天先把包子蒸上。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "摊主描述备料动作，不含产品能力或效果声明。"
    },
    {
      "location": "shot:2/visual",
      "text": "切到手写菜单特写，摊主写下包子、豆浆。第一块为摊主旁白及对应字幕；随后在菜单画面上展示第二块产品事实卡，事实卡不配旁白，留出阅读时间。不展示软件界面，不出现顾客正脸。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "“摊主旁白及对应字幕”展示添加字幕能力，由P01.F1支持；事实卡对应的添加字幕说明已获核对。菜单书写、无旁白阅读和镜头限制均为拍摄安排，没有虚构产品界面或操作流程。"
    },
    {
      "location": "shot:2/block:1",
      "text": "今天的菜单，包子、豆浆。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "介绍早餐菜单，属于场景旁白，不含产品声明。"
    },
    {
      "location": "shot:3/visual",
      "text": "切到打包台俯拍，摊主双手摆齐打包盒。摊主继续画外音，成片叠加与旁白一致的字幕，只展示添加字幕的效果。不出现顾客正脸。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "“只展示添加字幕的效果”属于P01.F1支持的能力；字幕与旁白一致未被描述为自动生成。摆放打包盒和俯拍属于场景及拍摄安排。"
    },
    {
      "location": "shot:3/block:1",
      "text": "打包盒也摆好了，准备开摊。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "描述备料完成及准备开摊，不含产品承诺。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "镜1预计4秒，容纳短旁白、揭盖动作及蒸汽观察；镜2预计7秒，安排菜单书写、短旁白及随后无旁白的14字产品事实卡阅读；镜3预计4秒，容纳摆放打包盒和收尾旁白。三镜均有具体动作或阅读内容支撑停留，字幕效果伴随备料过程持续展示，没有空镜凑时长。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
