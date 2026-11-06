# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成《收摊以后》三镜脚本，按折叠桌、旧书、收摊纸箱的顺序介绍裁剪片段与添加字幕，结尾无关注点赞。当前稿无需进一步删改。工具估时14.6秒，符合22秒上限；成片仍需复核功能事实卡的阅读时间与字幕同步效果。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 收摊以后

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

画面：折叠桌近景：摊主折起桌腿。选取收桌动作的一小段，表现裁剪后的片段；旁白后叠加裁剪功能事实卡，不展示软件界面。

旁白/字幕：桌子收起，市集散了。剪影练习版支持裁剪视频片段。

来源：P02/P02.F1

预计镜头时长：5.8 秒

### 分镜 2

画面：旧书近景：摊主把旧书一本本摞齐。将本镜旁白“旧书摞好，带回家。”作为字幕叠加在画面上，随后展示添加字幕功能事实卡。

旁白/字幕：旧书摞好，带回家。剪影练习版支持为视频添加字幕。

来源：P01/P01.F1

预计镜头时长：5.8 秒

### 分镜 3

画面：收摊纸箱近景：摊主将装好物品的纸箱合上，双手在箱盖上轻轻压平，画面结束。

旁白/字幕：纸箱合上，今天收摊了。

来源：

预计镜头时长：3.0 秒

## 审稿备注（不进入视频，不计入时长）

供创作者核对修改与资料缺口，不是经过事实认证的产品介绍。

有来源的文字用于屏幕功能事实卡，不作旁白；无来源文字用于旁白，第二镜同时作为字幕示例。事实卡与旁白在镜头内依次呈现，字幕与对应旁白同步。按折叠桌、旧书、收摊纸箱的顺序拍摄，仅介绍裁剪片段与添加字幕。时长待工具估算，屏幕卡阅读与字幕同步效果仍需成片复核。

预计总时长：14.6 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "d57da7b9ee800fac75599b03ccf834b75ebf72ec7a67e586bd651ff64accac4b",
  "passed": true,
  "issues": [],
  "citations": [
    {
      "location": "shot:1/block:2",
      "source_id": "P02",
      "fact_id": "P02.F1",
      "quote": "剪影练习版支持裁剪视频片段。",
      "version": "2026-11-01"
    },
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
      "text": "收摊以后"
    },
    {
      "location": "shot:1/visual",
      "text": "折叠桌近景：摊主折起桌腿。选取收桌动作的一小段，表现裁剪后的片段；旁白后叠加裁剪功能事实卡，不展示软件界面。"
    },
    {
      "location": "shot:1/block:1",
      "text": "桌子收起，市集散了。"
    },
    {
      "location": "shot:2/visual",
      "text": "旧书近景：摊主把旧书一本本摞齐。将本镜旁白“旧书摞好，带回家。”作为字幕叠加在画面上，随后展示添加字幕功能事实卡。"
    },
    {
      "location": "shot:2/block:1",
      "text": "旧书摞好，带回家。"
    },
    {
      "location": "shot:3/visual",
      "text": "收摊纸箱近景：摊主将装好物品的纸箱合上，双手在箱盖上轻轻压平，画面结束。"
    },
    {
      "location": "shot:3/block:1",
      "text": "纸箱合上，今天收摊了。"
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
  "script_hash": "d57da7b9ee800fac75599b03ccf834b75ebf72ec7a67e586bd651ff64accac4b",
  "request_hash": "bceb0659a6ebdae1e0dc6ecf8ecaa4c0a9a8ee07337ab0c24112bb4db60db25d",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "介绍裁剪片段",
      "verdict": "met",
      "evidence": "第1镜选取收桌动作的一小段展示裁剪结果，并展示事实卡“剪影练习版支持裁剪视频片段。”"
    },
    {
      "field": "topic",
      "requirement": "添加字幕",
      "verdict": "met",
      "evidence": "第2镜将“旧书摞好，带回家。”叠加为字幕，并展示事实卡“剪影练习版支持为视频添加字幕。”"
    },
    {
      "field": "topic",
      "requirement": "画面顺序为折叠桌、旧书、收摊纸箱",
      "verdict": "met",
      "evidence": "第1镜为折叠桌近景，第2镜为旧书近景，第3镜为收摊纸箱近景，顺序一致。"
    },
    {
      "field": "topic",
      "requirement": "标题用“收摊以后”",
      "verdict": "met",
      "evidence": "script.title为“收摊以后”。"
    },
    {
      "field": "topic",
      "requirement": "结尾不说关注点赞",
      "verdict": "met",
      "evidence": "第3镜以合上纸箱和“纸箱合上，今天收摊了。”结束，没有关注或点赞邀请。"
    },
    {
      "field": "audience",
      "requirement": "周末市集摊主",
      "verdict": "met",
      "evidence": "三镜连续呈现摊主收桌、整理旧书、合上收摊纸箱，旁白明确提到“市集散了”，符合目标受众的经营场景。"
    },
    {
      "field": "platform",
      "requirement": "抖音",
      "verdict": "met",
      "evidence": "采用三个简短生活镜头、短旁白及功能事实卡；宿主估算总长14.6秒，适合短视频观看。"
    },
    {
      "field": "style",
      "requirement": "朴素",
      "verdict": "met",
      "evidence": "使用折桌腿、摞旧书、合纸箱等日常动作，配合“旧书摞好，带回家。”等直白文案，没有夸张宣传。"
    },
    {
      "field": "style",
      "requirement": "轻叙事",
      "verdict": "met",
      "evidence": "从“市集散了”到整理旧书，再到“今天收摊了”，以收摊过程形成简洁的连续叙事。"
    }
  ],
  "summary": "全部明确要求均已落实。两项功能都有画面示例和资料支持，标题、画面顺序及结尾符合要求，表达与节奏未发现明确问题。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "收摊以后",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "叙事标题，不含产品能力或效果承诺。"
    },
    {
      "location": "shot:1/visual",
      "text": "折叠桌近景：摊主折起桌腿。选取收桌动作的一小段，表现裁剪后的片段；旁白后叠加裁剪功能事实卡，不展示软件界面。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P02",
          "fact_id": "P02.F1"
        }
      ],
      "evidence": "“表现裁剪后的片段”及裁剪功能事实卡均由“剪影练习版支持裁剪视频片段。”支持；其余为拍摄安排，没有虚构操作界面或额外能力。"
    },
    {
      "location": "shot:1/block:1",
      "text": "桌子收起，市集散了。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "描述收摊场景，不含产品声明。"
    },
    {
      "location": "shot:2/visual",
      "text": "旧书近景：摊主把旧书一本本摞齐。将本镜旁白“旧书摞好，带回家。”作为字幕叠加在画面上，随后展示添加字幕功能事实卡。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "字幕示例和添加字幕功能事实卡由“剪影练习版支持为视频添加字幕。”支持；未声称自动识别、自动同步或其他未证实能力。"
    },
    {
      "location": "shot:2/block:1",
      "text": "旧书摞好，带回家。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "生活场景旁白兼字幕示例，不含产品承诺。"
    },
    {
      "location": "shot:3/visual",
      "text": "收摊纸箱近景：摊主将装好物品的纸箱合上，双手在箱盖上轻轻压平，画面结束。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "描述合箱与压平箱盖的拍摄动作，不含产品能力或效果声明。"
    },
    {
      "location": "shot:3/block:1",
      "text": "纸箱合上，今天收摊了。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "用于结束收摊叙事，不含产品声明。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "宿主预计第1、2镜各5.8秒，第3镜3秒，均满足4秒、4秒、3秒的最低停留要求。前两镜分别有收桌、摞书动作，短旁白后展示对应功能卡，第2镜字幕与旁白同步，内容足以支撑停留；末镜以合箱、压平箱盖和短句收尾。未见重复事实或空镜凑时长，总长14.6秒已通过22秒上限检查。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
