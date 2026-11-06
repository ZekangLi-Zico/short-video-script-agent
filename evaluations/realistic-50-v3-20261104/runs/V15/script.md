# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成四镜头脚本，涵盖添加字幕与手动编辑文字，保留洗好的蔬菜、空餐盘和食谱本背景，风格亲切、不营销，无营养功效文案，不安排儿童出镜。现稿无需删改。估算27.5秒，符合30秒目标的27—30秒范围；这是脚本估时，实际成片时长需制作后确认。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 厨房里的记录，配上自己写的话

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

画面：俯拍厨房台面，依次展示洗好的蔬菜、空餐盘和食谱本。成人双手摆好餐盘、翻开食谱，镜头随动作缓慢移动。文字块作旁白。全片只拍台面与成人双手，不出现儿童。

旁白/字幕：洗好蔬菜，摆上空餐盘，翻开食谱本，今天慢慢做。

来源：

预计镜头时长：6.5 秒

### 分镜 2

画面：延续厨房俯拍素材，先展示没有字幕的画面，再示意叠加创作示例字幕。产品事实块作旁白；“今天做家常菜。”仅作屏显字幕，不朗读。背景同时保留蔬菜、空餐盘和食谱本，不展示软件界面或按钮。

旁白/字幕：剪影练习版支持为视频添加字幕。今天做家常菜。

来源：P01/P01.F1

预计镜头时长：7.0 秒

### 分镜 3

画面：保持相同厨房构图，用修改前后的字幕对照示意手动编辑文字：先保留上一镜的字幕，再换成“今天想做清炒时蔬。”，给观众阅读时间。产品事实块作旁白，新句仅作屏显创作示例，不朗读。不虚构编辑界面、按钮或操作步骤。

旁白/字幕：字幕文字可以手动编辑。今天想做清炒时蔬。

来源：P01/P01.F2

预计镜头时长：7.0 秒

### 分镜 4

画面：回看修改后的厨房短片，沿洗好的蔬菜、空餐盘、翻开的食谱本依次取景，最后回到完整台面构图。保留上一镜已出现的示例字幕供阅读，文字块作旁白。不展示成菜，不加入营养功效或其他功能。

旁白/字幕：回看这一小段，读读字幕，再看看蔬菜、空餐盘和食谱本。

来源：

预计镜头时长：7.0 秒

时长要求：27.0–30 秒（接近目标）。

预计总时长：27.5 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "219ee887dcfadebbd6de669c02c702e6f27aaa9fa4e70e9202db5ba18c1b68dd",
  "passed": true,
  "issues": [],
  "citations": [
    {
      "location": "shot:2/block:1",
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
      "text": "厨房里的记录，配上自己写的话"
    },
    {
      "location": "shot:1/visual",
      "text": "俯拍厨房台面，依次展示洗好的蔬菜、空餐盘和食谱本。成人双手摆好餐盘、翻开食谱，镜头随动作缓慢移动。文字块作旁白。全片只拍台面与成人双手，不出现儿童。"
    },
    {
      "location": "shot:1/block:1",
      "text": "洗好蔬菜，摆上空餐盘，翻开食谱本，今天慢慢做。"
    },
    {
      "location": "shot:2/visual",
      "text": "延续厨房俯拍素材，先展示没有字幕的画面，再示意叠加创作示例字幕。产品事实块作旁白；“今天做家常菜。”仅作屏显字幕，不朗读。背景同时保留蔬菜、空餐盘和食谱本，不展示软件界面或按钮。"
    },
    {
      "location": "shot:2/block:2",
      "text": "今天做家常菜。"
    },
    {
      "location": "shot:3/visual",
      "text": "保持相同厨房构图，用修改前后的字幕对照示意手动编辑文字：先保留上一镜的字幕，再换成“今天想做清炒时蔬。”，给观众阅读时间。产品事实块作旁白，新句仅作屏显创作示例，不朗读。不虚构编辑界面、按钮或操作步骤。"
    },
    {
      "location": "shot:3/block:2",
      "text": "今天想做清炒时蔬。"
    },
    {
      "location": "shot:4/visual",
      "text": "回看修改后的厨房短片，沿洗好的蔬菜、空餐盘、翻开的食谱本依次取景，最后回到完整台面构图。保留上一镜已出现的示例字幕供阅读，文字块作旁白。不展示成菜，不加入营养功效或其他功能。"
    },
    {
      "location": "shot:4/block:1",
      "text": "回看这一小段，读读字幕，再看看蔬菜、空餐盘和食谱本。"
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
  "script_hash": "219ee887dcfadebbd6de669c02c702e6f27aaa9fa4e70e9202db5ba18c1b68dd",
  "request_hash": "f0cdde0bd1d754eaa019cd4f805619d55970619edd7cffce8ab94facc5e33052",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "介绍添加字幕",
      "verdict": "met",
      "evidence": "镜头2旁白“剪影练习版支持为视频添加字幕。”，并用无字幕画面与叠加示例字幕的画面对照介绍该功能。"
    },
    {
      "field": "topic",
      "requirement": "手动编辑文字",
      "verdict": "met",
      "evidence": "镜头3旁白“字幕文字可以手动编辑。”，画面将“今天做家常菜。”改为“今天想做清炒时蔬。”。"
    },
    {
      "field": "topic",
      "requirement": "以洗好的蔬菜、空餐盘和食谱本为背景",
      "verdict": "met",
      "evidence": "镜头1依次展示三种背景元素；镜头2明确同时保留蔬菜、空餐盘和食谱本；镜头3保持相同构图；镜头4再次沿三者取景。"
    },
    {
      "field": "topic",
      "requirement": "不要代写营养功效",
      "verdict": "met",
      "evidence": "全部旁白及示例字幕均未描述营养功效；镜头4还明确“不加入营养功效”。"
    },
    {
      "field": "topic",
      "requirement": "不出现儿童正脸",
      "verdict": "met",
      "evidence": "镜头1明确“全片只拍台面与成人双手，不出现儿童”，后续镜头均延续厨房台面构图。"
    },
    {
      "field": "audience",
      "requirement": "记录家庭料理的普通用户",
      "verdict": "met",
      "evidence": "厨房台面、食谱本及“今天做家常菜。”对应家庭料理记录；两项功能用简单旁白和字幕前后对照解释，无专业术语门槛。"
    },
    {
      "field": "platform",
      "requirement": "小红书",
      "verdict": "met",
      "evidence": "家庭料理生活场景、厨房俯拍和简短字幕对照适合小红书生活记录内容，稿件未出现明显平台适配冲突。"
    },
    {
      "field": "style",
      "requirement": "亲切",
      "verdict": "met",
      "evidence": "镜头1“今天慢慢做。”及镜头4“读读字幕，再看看蔬菜、空餐盘和食谱本。”语气自然温和。"
    },
    {
      "field": "style",
      "requirement": "不营销",
      "verdict": "met",
      "evidence": "产品介绍仅陈述添加字幕和手动编辑文字，没有夸张效果、购买引导或促销话术；结尾为回看画面的邀请。"
    }
  ],
  "summary": "稿件已覆盖两项功能、指定厨房背景及内容限制，符合普通家庭料理记录用户、小红书和亲切不营销的要求。表达有资料支持，各镜头停留也有对应动作或阅读内容。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "厨房里的记录，配上自己写的话",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        },
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "“配上自己写的话”在本稿中对应添加字幕及手动编辑字幕文字，由两项事实共同支持；未承诺自动生成或其他效果。"
    },
    {
      "location": "shot:1/visual",
      "text": "俯拍厨房台面，依次展示洗好的蔬菜、空餐盘和食谱本。成人双手摆好餐盘、翻开食谱，镜头随动作缓慢移动。文字块作旁白。全片只拍台面与成人双手，不出现儿童。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "全部为厨房场景、成人动作、镜头移动和人物出镜限制，没有产品能力或效果承诺。"
    },
    {
      "location": "shot:1/block:1",
      "text": "洗好蔬菜，摆上空餐盘，翻开食谱本，今天慢慢做。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "描述料理准备动作及生活语气，不涉及产品能力、营养功效或真实用户背书。"
    },
    {
      "location": "shot:2/visual",
      "text": "延续厨房俯拍素材，先展示没有字幕的画面，再示意叠加创作示例字幕。产品事实块作旁白；“今天做家常菜。”仅作屏显字幕，不朗读。背景同时保留蔬菜、空餐盘和食谱本，不展示软件界面或按钮。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "无字幕到叠加字幕的示意对应“支持为视频添加字幕”。其余为场景和音画安排，没有虚构软件界面、按钮或自动化流程。"
    },
    {
      "location": "shot:2/block:2",
      "text": "今天做家常菜。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "作为屏显创作示例描述家庭料理主题，不作产品承诺。"
    },
    {
      "location": "shot:3/visual",
      "text": "保持相同厨房构图，用修改前后的字幕对照示意手动编辑文字：先保留上一镜的字幕，再换成“今天想做清炒时蔬。”，给观众阅读时间。产品事实块作旁白，新句仅作屏显创作示例，不朗读。不虚构编辑界面、按钮或操作步骤。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "修改前后的字幕对照仅示意“字幕文字可以手动编辑”，未推断自动改写能力，也未编造实际操作步骤。"
    },
    {
      "location": "shot:3/block:2",
      "text": "今天想做清炒时蔬。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "描述计划制作的菜品，是字幕创作示例，不包含营养功效或产品效果声明。"
    },
    {
      "location": "shot:4/visual",
      "text": "回看修改后的厨房短片，沿洗好的蔬菜、空餐盘、翻开的食谱本依次取景，最后回到完整台面构图。保留上一镜已出现的示例字幕供阅读，文字块作旁白。不展示成菜，不加入营养功效或其他功能。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        },
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "展示保留手动修改后字幕的短片，由添加字幕和手动编辑文字两项事实支持。“回看”和依次取景是成片展示安排，未声称产品另有回放、导出或自动处理能力。"
    },
    {
      "location": "shot:4/block:1",
      "text": "回看这一小段，读读字幕，再看看蔬菜、空餐盘和食谱本。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "邀请观众阅读字幕、观察背景，没有新增产品能力或效果承诺。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "镜头1的6.5秒安排摆盘、翻食谱及移动取景，配简短旁白；镜头2的7秒用于无字幕与有字幕画面对照，并阅读不朗读的示例字幕；镜头3的7秒用于修改前后对照及新句阅读；镜头4的7秒配完整观察邀请，依次取景三个物件后回到全景。末镜虽复用字幕，但有明确观察任务，未见明显空镜或重复事实凑时长。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
