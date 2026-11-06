# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成早餐摊主讲今日备料的三镜头脚本，仅介绍添加字幕，按蒸笼→手写菜单→打包台排列，明确避开顾客正脸。当前稿无需删改，三项检查均通过。估算约14.1秒，低于25秒上限；实际时长以成片为准。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 给早餐摊的备料视频加字幕

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

画面：蒸笼特写，只拍蒸汽、包子和摊主的手，不出现顾客正脸。第一段为同事口吻的画外音；第二段为摊主口播，并以同文字幕叠加在画面上。

旁白/字幕：拍今日备料，记得配上字幕。今天备料，先把包子上笼。

来源：

预计镜头时长：5.8 秒

### 分镜 2

画面：切到手写菜单特写，摊主的手把菜单摆好，不出现顾客正脸。叠加独立产品事实卡，内容为本镜头事实块；留给观众阅读，不配旁白，不展示软件界面。

旁白/字幕：剪影练习版支持为视频添加字幕。

来源：P01/P01.F1

预计镜头时长：5.0 秒

### 分镜 3

画面：最后切到打包台，俯拍摊主摆好豆浆杯和打包袋，只展示台面与双手，不出现顾客正脸。摊主继续画外音讲备料，同文字幕叠加在画面上，展示添加字幕后的效果。

旁白/字幕：豆浆装好，打包袋也备齐了。

来源：

预计镜头时长：3.3 秒

预计总时长：14.1 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "07ebe61d2109f6b4a9c322223639578f71a86a060e7e0cd7b9db03d609ef5b8c",
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
      "text": "给早餐摊的备料视频加字幕"
    },
    {
      "location": "shot:1/visual",
      "text": "蒸笼特写，只拍蒸汽、包子和摊主的手，不出现顾客正脸。第一段为同事口吻的画外音；第二段为摊主口播，并以同文字幕叠加在画面上。"
    },
    {
      "location": "shot:1/block:1",
      "text": "拍今日备料，记得配上字幕。"
    },
    {
      "location": "shot:1/block:2",
      "text": "今天备料，先把包子上笼。"
    },
    {
      "location": "shot:2/visual",
      "text": "切到手写菜单特写，摊主的手把菜单摆好，不出现顾客正脸。叠加独立产品事实卡，内容为本镜头事实块；留给观众阅读，不配旁白，不展示软件界面。"
    },
    {
      "location": "shot:3/visual",
      "text": "最后切到打包台，俯拍摊主摆好豆浆杯和打包袋，只展示台面与双手，不出现顾客正脸。摊主继续画外音讲备料，同文字幕叠加在画面上，展示添加字幕后的效果。"
    },
    {
      "location": "shot:3/block:1",
      "text": "豆浆装好，打包袋也备齐了。"
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
  "script_hash": "07ebe61d2109f6b4a9c322223639578f71a86a060e7e0cd7b9db03d609ef5b8c",
  "request_hash": "4299792130470435332510610b8526e5f391e330ac68588a7ba5d1498ead5ad2",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "做一条剪影练习版字幕功能介绍",
      "verdict": "met",
      "evidence": "镜头2明确展示“剪影练习版支持为视频添加字幕。”，镜头1、3安排字幕效果示意。"
    },
    {
      "field": "topic",
      "requirement": "背景是早餐摊主讲今日备料",
      "verdict": "met",
      "evidence": "镜头1由摊主口播“今天备料，先把包子上笼。”；镜头3继续讲“豆浆装好，打包袋也备齐了。”，明确体现早餐摊备料场景。"
    },
    {
      "field": "topic",
      "requirement": "只介绍添加字幕",
      "verdict": "met",
      "evidence": "产品介绍仅有镜头2的添加字幕事实及镜头1、3的字幕示意；未介绍字幕编辑、视频裁剪或画面比例等其他功能。镜头切换属于拍摄安排。"
    },
    {
      "field": "topic",
      "requirement": "画面按蒸笼、手写菜单、打包台的顺序",
      "verdict": "met",
      "evidence": "镜头1为“蒸笼特写”，镜头2为“手写菜单特写”，镜头3为“最后切到打包台”，顺序一致。"
    },
    {
      "field": "topic",
      "requirement": "不要出现顾客正脸",
      "verdict": "met",
      "evidence": "三个镜头均明确“不出现顾客正脸”，取景限定为蒸笼、菜单、台面及摊主双手。"
    },
    {
      "field": "audience",
      "requirement": "小店新媒体兼职",
      "verdict": "met",
      "evidence": "以小店备料视频为实例，用“拍今日备料，记得配上字幕。”引入单一基础功能，无专业术语，适合兼职制作店铺内容的人群。"
    },
    {
      "field": "platform",
      "requirement": "抖音",
      "verdict": "met",
      "evidence": "采用三个生活场景特写、简短口播及画面字幕，主题直接，适合抖音短视频表达。"
    },
    {
      "field": "style",
      "requirement": "像同事分享经验",
      "verdict": "met",
      "evidence": "镜头1明确安排“同事口吻的画外音”，开场“拍今日备料，记得配上字幕。”呈现自然提醒的交流语气。"
    },
    {
      "field": "style",
      "requirement": "短句",
      "verdict": "met",
      "evidence": "文案采用“今天备料，先把包子上笼。”“豆浆装好，打包袋也备齐了。”等短句；产品事实卡也仅有一句。"
    }
  ],
  "summary": "明确需求均已落实：早餐摊备料场景完整，画面顺序正确，仅介绍添加字幕，并明确避开顾客正脸。未发现无依据的产品声明或明显凑时长。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "给早餐摊的备料视频加字幕",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "标题体现为视频添加字幕的能力，由P01.F1直接支持；早餐摊备料仅是应用场景。"
    },
    {
      "location": "shot:1/visual",
      "text": "蒸笼特写，只拍蒸汽、包子和摊主的手，不出现顾客正脸。第一段为同事口吻的画外音；第二段为摊主口播，并以同文字幕叠加在画面上。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "“以同文字幕叠加在画面上”示意添加字幕，符合P01.F1；未声称自动识别语音或自动生成字幕，其余内容为场景和拍摄安排。"
    },
    {
      "location": "shot:1/block:1",
      "text": "拍今日备料，记得配上字幕。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "这是给拍摄者的行动建议，未承诺产品性能、自动化能力或使用效果。"
    },
    {
      "location": "shot:1/block:2",
      "text": "今天备料，先把包子上笼。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "这是早餐摊主的场景台词，仅描述备料动作，不含产品声明或真实客户背书。"
    },
    {
      "location": "shot:2/visual",
      "text": "切到手写菜单特写，摊主的手把菜单摆好，不出现顾客正脸。叠加独立产品事实卡，内容为本镜头事实块；留给观众阅读，不配旁白，不展示软件界面。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "该段规定取景、事实卡呈现和阅读安排，本身未新增产品能力声明，也未虚构软件按钮、界面布局或操作步骤；所指事实块已由rules_check核对。"
    },
    {
      "location": "shot:3/visual",
      "text": "最后切到打包台，俯拍摊主摆好豆浆杯和打包袋，只展示台面与双手，不出现顾客正脸。摊主继续画外音讲备料，同文字幕叠加在画面上，展示添加字幕后的效果。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "“同文字幕叠加在画面上，展示添加字幕后的效果”仅展示P01.F1支持的添加字幕能力，没有延伸为自动转写、自动同步或经营收益承诺。"
    },
    {
      "location": "shot:3/block:1",
      "text": "豆浆装好，打包袋也备齐了。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "这是备料场景的收尾台词，描述豆浆和打包袋的准备情况，不含产品能力或效果声明。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "镜头1的hold_seconds为0，两句短口播配合蒸笼特写及字幕，没有额外空停；镜头2停留5秒，安排摆菜单动作及阅读“剪影练习版支持为视频添加字幕。”，有明确观察和阅读内容；镜头3的hold_seconds为0，一句备料台词配合摆放豆浆杯、打包袋及字幕示意。三个镜头各有内容任务，未见明显重复凑时长。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
