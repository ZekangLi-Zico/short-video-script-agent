# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成4镜头脚本，首稿通过检查，无需删改。涵盖添加字幕和手动编辑文字，以洗好的蔬菜、空餐盘和食谱本为背景，语气亲切、不营销；未写营养功效，并明确不出现儿童正脸。估算27.3秒，符合30秒目标的27—30秒范围。需求审核为模型判断，实际成片时长仍需拍摄剪辑后确认。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 给做饭日常添几行字幕

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

画面：俯拍料理台，洗好的蔬菜、空餐盘和食谱本同框。仅出现成年人的手：摆正餐盘，再翻开食谱本。文字块为旁白，全片不出现儿童正脸。

旁白/字幕：洗好蔬菜，摆好空餐盘，翻开食谱本，记录今天的做饭日常。

来源：

预计镜头时长：6.3 秒

### 分镜 2

画面：保持三样背景物同框，缓慢推近蔬菜。以简单文字叠加示意添加字幕，示例文字为“准备晚餐”，不展示产品界面或按钮。第一块为产品事实旁白，第二块为创作示例旁白。

旁白/字幕：剪影练习版支持为视频添加字幕。先写一句：准备晚餐。

来源：P01/P01.F1

预计镜头时长：7.0 秒

### 分镜 3

画面：延续料理台背景，用前后两版文字示意手动编辑：“准备晚餐”变为“今晚做家常菜”，依次留出阅读时间。不模拟操作界面，不暗示文字自动变化。第一块为产品事实旁白，第二块为编辑示例旁白。

旁白/字幕：字幕文字可以手动编辑。再把“准备晚餐”改成“今晚做家常菜”。

来源：P01/P01.F2

预计镜头时长：8.0 秒

### 分镜 4

画面：镜头回到俯拍全景，成年人的手沿食谱本上的文字缓慢移动，再将食谱本摆正；洗好的蔬菜和空餐盘始终可见。不突出任何营养功效文字。旁白结束后自然收镜。

旁白/字幕：对照食谱本，再读一遍文字，把这次的准备过程记下来。

来源：

预计镜头时长：6.0 秒

时长要求：27.0–30 秒（接近目标）。

预计总时长：27.3 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "cb964d0808940dee50883b892d1eaf5d89666a2890acfdc55e86efc19e87bda8",
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
      "text": "给做饭日常添几行字幕"
    },
    {
      "location": "shot:1/visual",
      "text": "俯拍料理台，洗好的蔬菜、空餐盘和食谱本同框。仅出现成年人的手：摆正餐盘，再翻开食谱本。文字块为旁白，全片不出现儿童正脸。"
    },
    {
      "location": "shot:1/block:1",
      "text": "洗好蔬菜，摆好空餐盘，翻开食谱本，记录今天的做饭日常。"
    },
    {
      "location": "shot:2/visual",
      "text": "保持三样背景物同框，缓慢推近蔬菜。以简单文字叠加示意添加字幕，示例文字为“准备晚餐”，不展示产品界面或按钮。第一块为产品事实旁白，第二块为创作示例旁白。"
    },
    {
      "location": "shot:2/block:2",
      "text": "先写一句：准备晚餐。"
    },
    {
      "location": "shot:3/visual",
      "text": "延续料理台背景，用前后两版文字示意手动编辑：“准备晚餐”变为“今晚做家常菜”，依次留出阅读时间。不模拟操作界面，不暗示文字自动变化。第一块为产品事实旁白，第二块为编辑示例旁白。"
    },
    {
      "location": "shot:3/block:2",
      "text": "再把“准备晚餐”改成“今晚做家常菜”。"
    },
    {
      "location": "shot:4/visual",
      "text": "镜头回到俯拍全景，成年人的手沿食谱本上的文字缓慢移动，再将食谱本摆正；洗好的蔬菜和空餐盘始终可见。不突出任何营养功效文字。旁白结束后自然收镜。"
    },
    {
      "location": "shot:4/block:1",
      "text": "对照食谱本，再读一遍文字，把这次的准备过程记下来。"
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
  "script_hash": "cb964d0808940dee50883b892d1eaf5d89666a2890acfdc55e86efc19e87bda8",
  "request_hash": "f0cdde0bd1d754eaa019cd4f805619d55970619edd7cffce8ab94facc5e33052",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "介绍添加字幕",
      "verdict": "met",
      "evidence": "镜头2旁白“剪影练习版支持为视频添加字幕。”，并以“准备晚餐”示意字幕。"
    },
    {
      "field": "topic",
      "requirement": "手动编辑文字",
      "verdict": "met",
      "evidence": "镜头3旁白“字幕文字可以手动编辑。”，画面展示“准备晚餐”改为“今晚做家常菜”的前后对比。"
    },
    {
      "field": "topic",
      "requirement": "洗好的蔬菜",
      "verdict": "met",
      "evidence": "镜头1明确“洗好的蔬菜、空餐盘和食谱本同框”；镜头2、3延续背景，镜头4明确蔬菜始终可见。"
    },
    {
      "field": "topic",
      "requirement": "空餐盘",
      "verdict": "met",
      "evidence": "镜头1展示并摆正空餐盘；镜头2保持三样背景物同框，镜头4明确空餐盘始终可见。"
    },
    {
      "field": "topic",
      "requirement": "食谱本",
      "verdict": "met",
      "evidence": "镜头1翻开食谱本；镜头2、3延续背景，镜头4展示沿食谱文字移动手指并摆正食谱本。"
    },
    {
      "field": "topic",
      "requirement": "不要代写营养功效",
      "verdict": "met",
      "evidence": "标题、旁白及字幕示例均未宣称营养功效；镜头4另明确“不突出任何营养功效文字”。"
    },
    {
      "field": "topic",
      "requirement": "不出现儿童正脸",
      "verdict": "met",
      "evidence": "镜头1明确“仅出现成年人的手”“全片不出现儿童正脸”；其余镜头均为料理台、文字示意或成年人的手。"
    },
    {
      "field": "audience",
      "requirement": "记录家庭料理的普通用户",
      "verdict": "met",
      "evidence": "以准备晚餐、家常菜和食谱本为具体场景，使用“先写一句”“再把……改成……”等易懂表达，适合普通用户记录家庭料理。"
    },
    {
      "field": "platform",
      "requirement": "小红书",
      "verdict": "met",
      "evidence": "标题“给做饭日常添几行字幕”结合家庭料理画面和简短文字示例，符合生活记录、经验分享类短视频表达。"
    },
    {
      "field": "style",
      "requirement": "亲切",
      "verdict": "met",
      "evidence": "“记录今天的做饭日常”“先写一句：准备晚餐”等旁白自然、生活化，没有生硬术语。"
    },
    {
      "field": "style",
      "requirement": "不营销",
      "verdict": "met",
      "evidence": "产品介绍仅陈述添加字幕、手动编辑两项功能；结尾“把这次的准备过程记下来”没有购买引导、促销或夸大效果。"
    }
  ],
  "summary": "已满足功能介绍、三样背景物和两项禁止要求，受众、平台及语气适配。产品能力表达有资料支持，各镜头节奏合理。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "给做饭日常添几行字幕",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "标题涉及为视频添加字幕，P01.F1直接支持；未增加自动生成等能力承诺。"
    },
    {
      "location": "shot:1/visual",
      "text": "俯拍料理台，洗好的蔬菜、空餐盘和食谱本同框。仅出现成年人的手：摆正餐盘，再翻开食谱本。文字块为旁白，全片不出现儿童正脸。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "全部为背景、人物出镜范围、动作及旁白安排，不含产品能力声明。"
    },
    {
      "location": "shot:1/block:1",
      "text": "洗好蔬菜，摆好空餐盘，翻开食谱本，记录今天的做饭日常。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "描述料理准备动作和记录意图，不涉及产品性能或营养功效。"
    },
    {
      "location": "shot:2/visual",
      "text": "保持三样背景物同框，缓慢推近蔬菜。以简单文字叠加示意添加字幕，示例文字为“准备晚餐”，不展示产品界面或按钮。第一块为产品事实旁白，第二块为创作示例旁白。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "文字叠加示意的是P01.F1支持的添加字幕能力；其余为拍摄安排和示例文案，没有虚构产品界面或按钮。"
    },
    {
      "location": "shot:2/block:2",
      "text": "先写一句：准备晚餐。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅邀请拟写一句字幕示例，没有宣称自动生成文案或指定产品操作步骤。"
    },
    {
      "location": "shot:3/visual",
      "text": "延续料理台背景，用前后两版文字示意手动编辑：“准备晚餐”变为“今晚做家常菜”，依次留出阅读时间。不模拟操作界面，不暗示文字自动变化。第一块为产品事实旁白，第二块为编辑示例旁白。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "前后两版文字展示手动编辑字幕，P01.F2直接支持；画面明确排除自动变化和模拟产品界面。"
    },
    {
      "location": "shot:3/block:2",
      "text": "再把“准备晚餐”改成“今晚做家常菜”。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "结合本镜头语境，这是手动修改字幕内容的具体示例，属于P01.F2支持的能力，没有扩展操作承诺。"
    },
    {
      "location": "shot:4/visual",
      "text": "镜头回到俯拍全景，成年人的手沿食谱本上的文字缓慢移动，再将食谱本摆正；洗好的蔬菜和空餐盘始终可见。不突出任何营养功效文字。旁白结束后自然收镜。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅安排构图、手部动作、背景物和收镜方式，不含产品效果或营养功效声明。"
    },
    {
      "location": "shot:4/block:1",
      "text": "对照食谱本，再读一遍文字，把这次的准备过程记下来。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于复读检查和生活记录的行动邀请，未声称产品能够识别食谱或自动检查文字。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "镜头1预计6.3秒，支撑摆盘、翻书及旁白；镜头2预计7秒，包含推近、字幕示例和两块旁白；镜头3预计8秒，包含两版文字依次展示、阅读与编辑说明；镜头4预计6秒，包含对照食谱、移动手指和摆正食谱本。各镜头均有具体观察或动作内容，符合6、7、8、6秒的最低停留约束，未见重复功能或空镜凑时长。宿主估算总长27.3秒，目标区间判定已通过。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
