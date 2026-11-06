# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成字幕添加与手动编辑功能的四镜脚本，估时17.3秒，符合25秒上限。未采用未经统计核实和授权的“播放量提高30%”说法，并明确提醒口头反馈不等于效果证明。三项检查均通过。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 字幕能做什么，先说清楚

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

画面：店员摆好手机，准备录制商品口播。本镜文字为旁白。

旁白/字幕：店铺口播，先从字幕开始。

来源：

预计镜头时长：3.0 秒

### 分镜 2

画面：字幕功能事实卡，屏幕显示本镜事实文字，旁白同步朗读，不展示具体软件界面。

旁白/字幕：剪影练习版支持为视频添加字幕。

来源：P01/P01.F1

预计镜头时长：4.0 秒

### 分镜 3

画面：店员对照纸质口播稿核对字幕文案，圈出需要修改的字。本镜事实文字作为旁白，不展示软件操作流程。

旁白/字幕：字幕文字可以手动编辑。

来源：P01/P01.F2

预计镜头时长：3.0 秒

### 分镜 4

画面：简洁背景展示本镜提示文字，旁白同步朗读。

旁白/字幕：口头反馈不是效果证明。播放量变化需统计核实，公开引用需授权。

来源：

预计镜头时长：7.3 秒

预计总时长：17.3 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "3ba84aa1a16fd855179f648d3b67a1b5f980ff48d82bc3179f4e82cc548a3301",
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
      "text": "字幕能做什么，先说清楚"
    },
    {
      "location": "shot:1/visual",
      "text": "店员摆好手机，准备录制商品口播。本镜文字为旁白。"
    },
    {
      "location": "shot:1/block:1",
      "text": "店铺口播，先从字幕开始。"
    },
    {
      "location": "shot:2/visual",
      "text": "字幕功能事实卡，屏幕显示本镜事实文字，旁白同步朗读，不展示具体软件界面。"
    },
    {
      "location": "shot:3/visual",
      "text": "店员对照纸质口播稿核对字幕文案，圈出需要修改的字。本镜事实文字作为旁白，不展示软件操作流程。"
    },
    {
      "location": "shot:4/visual",
      "text": "简洁背景展示本镜提示文字，旁白同步朗读。"
    },
    {
      "location": "shot:4/block:1",
      "text": "口头反馈不是效果证明。播放量变化需统计核实，公开引用需授权。"
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
  "script_hash": "3ba84aa1a16fd855179f648d3b67a1b5f980ff48d82bc3179f4e82cc548a3301",
  "request_hash": "93972873cc931936e79f564ca370d65259052b284f9983eeaaba7d87a79a6a9d",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "请写一条介绍字幕功能的脚本",
      "verdict": "met",
      "evidence": "第2镜介绍“支持为视频添加字幕”，第3镜介绍“字幕文字可以手动编辑”，均已通过宿主事实检查。"
    },
    {
      "field": "topic",
      "requirement": "处理这个说法",
      "verdict": "met",
      "evidence": "第4镜用“口头反馈不是效果证明。播放量变化需统计核实，公开引用需授权”回应口头反馈、缺少统计和授权的问题，未将30%的数字作为宣传依据。"
    },
    {
      "field": "topic",
      "requirement": "不要把口头反馈包装成已验证效果",
      "verdict": "met",
      "evidence": "第4镜明确区分口头反馈与效果证明；标题、画面及旁白均未声称字幕已带来播放量提升。"
    },
    {
      "field": "audience",
      "requirement": "店铺内容运营",
      "verdict": "met",
      "evidence": "第1镜安排店员录制商品口播，第3镜安排核对字幕文案，具体体现店铺内容制作场景。"
    },
    {
      "field": "platform",
      "requirement": "抖音",
      "verdict": "met",
      "evidence": "四个简短镜头结合商品口播场景、字幕功能卡和核验提示，内容直接，适合短视频呈现；宿主估算总长17.3秒。"
    },
    {
      "field": "style",
      "requirement": "可信",
      "verdict": "met",
      "evidence": "第2、3镜功能陈述分别获P01.F1、P01.F2支持；第4镜说明口头反馈的证据边界，没有夸大效果。"
    },
    {
      "field": "style",
      "requirement": "少口号",
      "verdict": "met",
      "evidence": "正文主要为两条功能说明和一条核验提示；开场“店铺口播，先从字幕开始”简短，没有反复口号或夸张宣传。"
    }
  ],
  "summary": "需求已落实：介绍了字幕功能，妥善处理了未经统计和授权的口头反馈，没有将30%的播放量提升包装成已验证效果。受众、平台、风格及镜头节奏均符合要求。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "字幕能做什么，先说清楚",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "用于引出字幕功能介绍，未承诺具体产品能力或效果。"
    },
    {
      "location": "shot:1/visual",
      "text": "店员摆好手机，准备录制商品口播。本镜文字为旁白。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于店铺拍摄场景和旁白安排，没有声称真实客户背书或产品自动化能力。"
    },
    {
      "location": "shot:1/block:1",
      "text": "店铺口播，先从字幕开始。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于内容制作建议和开场连接语，没有播放量或其他效果承诺。"
    },
    {
      "location": "shot:2/visual",
      "text": "字幕功能事实卡，屏幕显示本镜事实文字，旁白同步朗读，不展示具体软件界面。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅安排已核对正文的文字卡呈现及同步旁白，未增加产品声明或虚构软件界面。"
    },
    {
      "location": "shot:3/visual",
      "text": "店员对照纸质口播稿核对字幕文案，圈出需要修改的字。本镜事实文字作为旁白，不展示软件操作流程。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "展示人工核对文案的生活场景，没有暗示软件自动纠错，也未虚构按钮、界面或操作步骤。"
    },
    {
      "location": "shot:4/visual",
      "text": "简洁背景展示本镜提示文字，旁白同步朗读。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅描述背景、文字展示及旁白安排，没有产品能力或效果声明。"
    },
    {
      "location": "shot:4/block:1",
      "text": "口头反馈不是效果证明。播放量变化需统计核实，公开引用需授权。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于针对原始需求的核验与授权提醒，没有宣称播放量确已提升，也没有作出产品效果承诺。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "宿主预计第1至4镜分别为3.0、4.0、3.0、7.3秒，对应旁白单位数10、14、10、27。第1镜准备口播、第2镜阅读功能卡、第3镜核对并圈字、第4镜阅读核验提示，均有明确内容支撑停留；未发现重复事实或空镜凑时长。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
