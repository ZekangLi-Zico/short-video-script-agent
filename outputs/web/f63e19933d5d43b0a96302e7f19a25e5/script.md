# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成3镜配音脚本，示范添加字幕、手动改正咖啡名，预计24.8秒。时长、规则及需求检查全部通过。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 门店视频小教学：加字幕、改对咖啡名

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 连读旁白

今天用拍好的手冲和端杯录像，练习加字幕、改咖啡名。

在剪影练习版里，可以给视频添加字幕，比如给注水画面配上“手冲咖啡制作中”。

字幕文字也能手动编辑。这杯是耶加雪菲，把写错的“飞”改成“菲”。再看一遍，确认咖啡名写对了。

### 分镜 1

场景：咖啡店工作台旁，示范店员和同事一起看屏幕，展示已有的手冲注水与端杯出餐录像。

镜头目的：交代已有录像和本次练习任务

| 时间（镜内） | 动作与画面 | 对白与声音 |
|---|---|---|
| 0–6.0 秒 | 示范店员向同事展示两段已有录像，同事看着屏幕。<br>镜头：屏幕近景，依次展示注水和端杯画面。 | 示范店员：今天用拍好的手冲和端杯录像，练习加字幕、改咖啡名。 |

来源：动作安排见表达审核

预计镜头时长：6.0 秒

### 分镜 2

场景：录屏展示剪影练习版中为手冲注水画面添加字幕的实际过程。

镜头目的：示范为已有视频添加字幕

| 时间（镜内） | 动作与画面 | 对白与声音 |
|---|---|---|
| 0–8.5 秒 | 示范店员使用实际字幕功能，为注水画面添加“手冲咖啡制作中”，同事观察字幕出现在视频上。<br>镜头：录屏近景，保留实际操作过程和字幕结果。 | 示范店员：在剪影练习版里，可以给视频添加字幕，比如给注水画面配上“手冲咖啡制作中”。 |

来源：P01/P01.F1

预计镜头时长：8.5 秒

### 分镜 3

场景：端杯录像上的示例字幕将“耶加雪菲”误写为“耶加雪飞”，展示手动修改与改后画面。

镜头目的：示范手动改正咖啡名并查看修改结果

| 时间（镜内） | 动作与画面 | 对白与声音 |
|---|---|---|
| 0–6.8 秒 | 示范店员展示端杯画面的错误字幕“耶加雪飞”，通过实际文字编辑功能把“飞”改为“菲”。<br>镜头：录屏近景，让修改前后的字清楚可见。 | 示范店员：字幕文字也能手动编辑。这杯是耶加雪菲，把写错的“飞”改成“菲”。 |
| 6.8–10.3 秒 | 展示改后字幕“耶加雪菲”与端杯画面，同事看完点头。<br>镜头：停留在改后的字幕和端杯画面。 | 示范店员：再看一遍，确认咖啡名写对了。 |

来源：P01/P01.F2

预计镜头时长：10.3 秒

预计总时长：24.8 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "9fac6a641ef872c33d43a7c034ecfbecd088fe4447586bb91d5c66907f999976",
  "passed": true,
  "issues": [],
  "citations": [
    {
      "location": "shot:2/block:1",
      "source_id": "P01",
      "fact_id": "P01.F1",
      "quote": "剪影练习版支持为视频添加字幕。",
      "version": "2026-11-01",
      "text": "在剪影练习版里，可以给视频添加字幕，比如给注水画面配上“手冲咖啡制作中”。",
      "requires_semantic_review": true
    },
    {
      "location": "shot:3/block:1",
      "source_id": "P01",
      "fact_id": "P01.F2",
      "quote": "字幕文字可以手动编辑。",
      "version": "2026-11-01",
      "text": "字幕文字也能手动编辑。这杯是耶加雪菲，把写错的“飞”改成“菲”。",
      "requires_semantic_review": true
    }
  ],
  "rules_version": "2026-11-03-v1",
  "requires_expression_review": true,
  "expression_slots": [
    {
      "location": "title",
      "text": "门店视频小教学：加字幕、改对咖啡名"
    },
    {
      "location": "shot:1/visual",
      "text": "咖啡店工作台旁，示范店员和同事一起看屏幕，展示已有的手冲注水与端杯出餐录像。"
    },
    {
      "location": "shot:1/staging:1",
      "text": "动作：示范店员向同事展示两段已有录像，同事看着屏幕。\n镜头：屏幕近景，依次展示注水和端杯画面。"
    },
    {
      "location": "shot:1/block:1",
      "text": "今天用拍好的手冲和端杯录像，练习加字幕、改咖啡名。"
    },
    {
      "location": "shot:2/visual",
      "text": "录屏展示剪影练习版中为手冲注水画面添加字幕的实际过程。"
    },
    {
      "location": "shot:2/staging:1",
      "text": "动作：示范店员使用实际字幕功能，为注水画面添加“手冲咖啡制作中”，同事观察字幕出现在视频上。\n镜头：录屏近景，保留实际操作过程和字幕结果。"
    },
    {
      "location": "shot:2/block:1",
      "text": "在剪影练习版里，可以给视频添加字幕，比如给注水画面配上“手冲咖啡制作中”。"
    },
    {
      "location": "shot:3/visual",
      "text": "端杯录像上的示例字幕将“耶加雪菲”误写为“耶加雪飞”，展示手动修改与改后画面。"
    },
    {
      "location": "shot:3/staging:1",
      "text": "动作：示范店员展示端杯画面的错误字幕“耶加雪飞”，通过实际文字编辑功能把“飞”改为“菲”。\n镜头：录屏近景，让修改前后的字清楚可见。"
    },
    {
      "location": "shot:3/staging:2",
      "text": "动作：展示改后字幕“耶加雪菲”与端杯画面，同事看完点头。\n镜头：停留在改后的字幕和端杯画面。"
    },
    {
      "location": "shot:3/block:1",
      "text": "字幕文字也能手动编辑。这杯是耶加雪菲，把写错的“飞”改成“菲”。"
    },
    {
      "location": "shot:3/block:2",
      "text": "再看一遍，确认咖啡名写对了。"
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
  "scope": "source_identity_and_brand_checks; every public claim requires semantic entailment review"
}
```

## 需求覆盖核对

以下为模型评估，可能漏判或误判，仍需人工确认。

```json
{
  "ok": true,
  "script_hash": "9fac6a641ef872c33d43a7c034ecfbecd088fe4447586bb91d5c66907f999976",
  "request_hash": "84d72cf1f198754e66409bec80b9d56de54899e987c8fea1b5c6c3a0cb8f0159",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "咖啡店准备给店员做一条剪辑小教学。",
      "verdict": "met",
      "evidence": "第1镜设置咖啡店工作台和店员示范，第2、3镜分别演示字幕添加与修改。"
    },
    {
      "field": "topic",
      "requirement": "已有手冲注水和端杯出餐的录像",
      "verdict": "met",
      "evidence": "第1镜展示两段已有录像，后续分别使用注水与端杯画面。"
    },
    {
      "field": "topic",
      "requirement": "用剪影练习版给视频添加字幕",
      "verdict": "met",
      "evidence": "第2镜明确使用剪影练习版，为注水画面添加“手冲咖啡制作中”。"
    },
    {
      "field": "topic",
      "requirement": "再把字幕里写错的咖啡名字手动改好",
      "verdict": "met",
      "evidence": "第3镜接在添加字幕之后，手动将“耶加雪飞”修改为“耶加雪菲”。"
    },
    {
      "field": "topic",
      "requirement": "写一条可以配音的短视频脚本",
      "verdict": "met",
      "evidence": "三镜均提供由示范店员朗读的voice文案，连续配音内容完整。"
    },
    {
      "field": "topic",
      "requirement": "让没用过这款工具的同事看懂这两个用途",
      "verdict": "met",
      "evidence": "第2镜展示添加过程及结果，第3镜展示错字修改前后，两个用途均配有具体例子。"
    },
    {
      "field": "audience",
      "requirement": "负责门店短视频、刚接触剪辑的店员",
      "verdict": "met",
      "evidence": "使用店员熟悉的咖啡制作和出餐录像，配音无专业术语，并安排实际操作近景。"
    },
    {
      "field": "platform",
      "requirement": "视频号",
      "verdict": "met",
      "evidence": "三镜组成简短门店教学，录屏近景突出字幕变化，适合视频号观看场景。"
    },
    {
      "field": "style",
      "requirement": "像同事示范",
      "verdict": "met",
      "evidence": "示范店员边操作边讲解，同事观看并在确认结果后点头。"
    },
    {
      "field": "style",
      "requirement": "直接、自然、步骤好理解",
      "verdict": "met",
      "evidence": "配音按交代任务、添加字幕、修改错字、确认结果推进，“把写错的‘飞’改成‘菲’”表达具体且衔接清楚。"
    }
  ],
  "summary": "稿件覆盖两项用途、咖啡店场景及新手店员需求，公开功能表述均有资料支持。预计24.8秒，镜头内容与停留时间匹配。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "门店视频小教学：加字幕、改对咖啡名",
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
      "evidence": "添加字幕与手动编辑文字分别有来源支持，标题未承诺自动纠错。"
    },
    {
      "location": "shot:1/visual",
      "text": "咖啡店工作台旁，示范店员和同事一起看屏幕，展示已有的手冲注水与端杯出餐录像。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于门店背景和观看素材的拍摄安排，无产品能力声明。"
    },
    {
      "location": "shot:1/staging:1",
      "text": "动作：示范店员向同事展示两段已有录像，同事看着屏幕。\n镜头：屏幕近景，依次展示注水和端杯画面。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅安排人物观看录像及镜头顺序。"
    },
    {
      "location": "shot:1/block:1",
      "text": "今天用拍好的手冲和端杯录像，练习加字幕、改咖啡名。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "交代本次练习任务，未新增产品承诺。"
    },
    {
      "location": "shot:2/visual",
      "text": "录屏展示剪影练习版中为手冲注水画面添加字幕的实际过程。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "添加字幕由F1支持，未虚构按钮或界面布局。"
    },
    {
      "location": "shot:2/staging:1",
      "text": "动作：示范店员使用实际字幕功能，为注水画面添加“手冲咖啡制作中”，同事观察字幕出现在视频上。\n镜头：录屏近景，保留实际操作过程和字幕结果。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "示例字幕是已支持的添加字幕功能的具体应用，未增加自动化能力。"
    },
    {
      "location": "shot:2/block:1",
      "text": "在剪影练习版里，可以给视频添加字幕，比如给注水画面配上“手冲咖啡制作中”。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "全部功能含义均由原块引用的F1支持，制作场景仅作示例。"
    },
    {
      "location": "shot:3/visual",
      "text": "端杯录像上的示例字幕将“耶加雪菲”误写为“耶加雪飞”，展示手动修改与改后画面。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "示例错字的手动修改属于F2支持的字幕文字编辑。"
    },
    {
      "location": "shot:3/staging:1",
      "text": "动作：示范店员展示端杯画面的错误字幕“耶加雪飞”，通过实际文字编辑功能把“飞”改为“菲”。\n镜头：录屏近景，让修改前后的字清楚可见。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "以手动编辑完成单字替换，有F2支持且未虚构操作路径。"
    },
    {
      "location": "shot:3/staging:2",
      "text": "动作：展示改后字幕“耶加雪菲”与端杯画面，同事看完点头。\n镜头：停留在改后的字幕和端杯画面。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于修改结果的展示和人物自然反应，无新增能力或真实用户背书。"
    },
    {
      "location": "shot:3/block:1",
      "text": "字幕文字也能手动编辑。这杯是耶加雪菲，把写错的“飞”改成“菲”。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "手动编辑能力由原块引用的F2支持，咖啡名称承接画面中的示例设定。"
    },
    {
      "location": "shot:3/block:2",
      "text": "再看一遍，确认咖啡名写对了。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "邀请人工复核修改结果，未宣称工具能自动核验。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "第1镜6秒展示两段素材，第2镜8.5秒配合添加字幕，第3镜6.8秒修改、3.5秒查看结果；各段均有配音和对应画面任务，无明显凑时长。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
