# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：分镜稿已完成，预计13秒，符合25秒上限。仅介绍添加字幕，按蒸笼、手写菜单、打包台的顺序呈现早餐备料，各镜均注明不拍顾客正脸。本次无需删改；拍摄前请按实际备料确认情境台词。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 早餐备料日常｜添加字幕

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

画面：蒸笼近景：只拍摊主的手掀开笼盖，露出包子。摊主画外音讲今日备料，下方逐字叠加对应字幕。不出现顾客正脸。

旁白/字幕：今天先备包子，再备豆浆。

来源：

预计镜头时长：4.0 秒

### 分镜 2

画面：切到手写菜单特写，菜单写着“包子、豆浆”，摊主的手将菜单摆正。介绍旁白读出本镜事实文字，下方同步显示对应字幕；不展示软件界面。不出现顾客正脸。

旁白/字幕：剪影练习版支持为视频添加字幕。

来源：P01/P01.F1

预计镜头时长：5.0 秒

### 分镜 3

画面：切到打包台近景：只拍摊主双手摆齐打包盒和纸袋。摊主继续讲备料，下方逐字叠加对应字幕，展示添加字幕后的生活片段。不出现顾客正脸。

旁白/字幕：打包盒也备好了，准备开摊。

来源：

预计镜头时长：4.0 秒

## 审稿备注（不进入视频，不计入时长）

供创作者核对修改与资料缺口，不是经过事实认证的产品介绍。

仅介绍添加字幕。早餐备料台词为拍摄情境示例，拍摄前按摊主实际备料确认。所有文字块均作为口播，字幕与口播同步，不另设串行事实卡。只展示字幕叠加效果，不虚构软件按钮或操作路径。

预计总时长：13.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "e42312745114cff5ae37b6d67b8afe1eb7878ba95f62b4d65bd2e24e7d2395c9",
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
      "text": "早餐备料日常｜添加字幕"
    },
    {
      "location": "shot:1/visual",
      "text": "蒸笼近景：只拍摊主的手掀开笼盖，露出包子。摊主画外音讲今日备料，下方逐字叠加对应字幕。不出现顾客正脸。"
    },
    {
      "location": "shot:1/block:1",
      "text": "今天先备包子，再备豆浆。"
    },
    {
      "location": "shot:2/visual",
      "text": "切到手写菜单特写，菜单写着“包子、豆浆”，摊主的手将菜单摆正。介绍旁白读出本镜事实文字，下方同步显示对应字幕；不展示软件界面。不出现顾客正脸。"
    },
    {
      "location": "shot:3/visual",
      "text": "切到打包台近景：只拍摊主双手摆齐打包盒和纸袋。摊主继续讲备料，下方逐字叠加对应字幕，展示添加字幕后的生活片段。不出现顾客正脸。"
    },
    {
      "location": "shot:3/block:1",
      "text": "打包盒也备好了，准备开摊。"
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
  "script_hash": "e42312745114cff5ae37b6d67b8afe1eb7878ba95f62b4d65bd2e24e7d2395c9",
  "request_hash": "4299792130470435332510610b8526e5f391e330ac68588a7ba5d1498ead5ad2",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "做一条剪影练习版字幕功能介绍",
      "verdict": "met",
      "evidence": "第2镜明确口播“剪影练习版支持为视频添加字幕。”，三镜均安排字幕展示。"
    },
    {
      "field": "topic",
      "requirement": "背景是早餐摊主讲今日备料",
      "verdict": "met",
      "evidence": "第1镜摊主讲“今天先备包子，再备豆浆。”，第3镜讲“打包盒也备好了，准备开摊。”，对应蒸笼和打包台画面。"
    },
    {
      "field": "topic",
      "requirement": "只介绍添加字幕",
      "verdict": "met",
      "evidence": "产品功能仅涉及添加字幕及其叠加展示；未介绍手动编辑字幕、裁剪视频或画面比例选项。逐字叠加和字幕同步属于画面展示安排，未宣称自动生成或自动同步能力。"
    },
    {
      "field": "topic",
      "requirement": "画面按蒸笼、手写菜单、打包台的顺序",
      "verdict": "met",
      "evidence": "第1镜“蒸笼近景”，第2镜“手写菜单特写”，第3镜“打包台近景”，顺序一致。"
    },
    {
      "field": "topic",
      "requirement": "不要出现顾客正脸",
      "verdict": "met",
      "evidence": "三镜均明确写有“不出现顾客正脸”，画面限定为蒸笼、菜单、打包用品及摊主手部。"
    },
    {
      "field": "audience",
      "requirement": "小店新媒体兼职",
      "verdict": "met",
      "evidence": "以早餐小店的备料素材展示字幕用途，第2镜用一句话说明功能，内容直观，无专业术语负担。"
    },
    {
      "field": "platform",
      "requirement": "抖音",
      "verdict": "met",
      "evidence": "采用三个连续生活特写、简短口播和同步字幕，适合短视频观看；宿主估算总长13秒。"
    },
    {
      "field": "style",
      "requirement": "像同事分享经验",
      "verdict": "met",
      "evidence": "“今天先备包子，再备豆浆。”“打包盒也备好了，准备开摊。”采用自然日常口吻，功能说明直接，没有夸张推销。"
    },
    {
      "field": "style",
      "requirement": "短句",
      "verdict": "met",
      "evidence": "三镜各一句口播，分别说明备料、添加字幕和开摊准备，没有长句或复杂从句。"
    }
  ],
  "summary": "已落实全部明确需求，仅介绍添加字幕，早餐备料场景、画面顺序和避开顾客正脸均符合要求。表达有据，分镜节奏合理；宿主时长检查通过，预计13秒。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "早餐备料日常｜添加字幕",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "“早餐备料日常”为场景主题；“添加字幕”为资料明确支持的功能，没有附加效果承诺。"
    },
    {
      "location": "shot:1/visual",
      "text": "蒸笼近景：只拍摊主的手掀开笼盖，露出包子。摊主画外音讲今日备料，下方逐字叠加对应字幕。不出现顾客正脸。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "字幕叠加展示对应“支持为视频添加字幕”。逐字呈现为画面安排，未指定自动流程、软件按钮或操作步骤；其余为早餐摊拍摄内容。"
    },
    {
      "location": "shot:1/block:1",
      "text": "今天先备包子，再备豆浆。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "摊主备料的情境台词，不含产品能力、效果或真实客户背书。"
    },
    {
      "location": "shot:2/visual",
      "text": "切到手写菜单特写，菜单写着“包子、豆浆”，摊主的手将菜单摆正。介绍旁白读出本镜事实文字，下方同步显示对应字幕；不展示软件界面。不出现顾客正脸。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "本镜事实文字介绍添加字幕，字幕随旁白展示属于该能力的示意；未承诺自动同步。菜单内容、摆正动作及取景限制均为拍摄安排。"
    },
    {
      "location": "shot:3/visual",
      "text": "切到打包台近景：只拍摊主双手摆齐打包盒和纸袋。摊主继续讲备料，下方逐字叠加对应字幕，展示添加字幕后的生活片段。不出现顾客正脸。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "“展示添加字幕后的生活片段”由添加字幕事实支持；逐字叠加仅描述成片呈现，其余为打包台动作与取景安排，没有新增产品能力。"
    },
    {
      "location": "shot:3/block:1",
      "text": "打包盒也备好了，准备开摊。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "描述备料场景的进展，不涉及产品性能或效果承诺。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "宿主预计第1镜4秒、第2镜5秒、第3镜4秒，均满足对应最低停留时间。第1镜10个口播单位配掀笼盖和观察包子，第2镜14个口播单位配摆正菜单及字幕阅读，第3镜11个口播单位配摆齐打包用品，时长均有口播和动作支撑。字幕随不同台词持续展示，不属于重复口播同一事实或空镜凑时长；editor_notes不计入播放时长。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
