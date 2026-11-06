# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成局部修改：保留原标题、添加字幕和手动编辑字幕两项功能及原有顺序；删除未证实的自动识别画面与99%准确率说法；第一镜停留由8秒缩短至4秒。当前稿估时12秒，符合28秒上限，三项检查均通过。删除原因已写入创作者备注；如需恢复相关说法，需向项目维护者提供功能证明及准确率测试资料。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 口播字幕小帮手

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

画面：桌上的采访话筒

旁白/字幕：剪影练习版支持为视频添加字幕。

来源：P01/P01.F1

预计镜头时长：4.0 秒

### 分镜 2

画面：便签上手改错字

旁白/字幕：字幕文字可以手动编辑。

来源：P01/P01.F2

预计镜头时长：8.0 秒

## 审稿备注（不进入视频，不计入时长）

供创作者核对修改与资料缺口，不是经过事实认证的产品介绍。

局部修改：删除旧稿第二镜，包括“显示自动识别示意”画面和“自动识别人声，字幕准确率达到99%。”文案。客户未提供自动识别能力证明及准确率测试资料，现有素材也无法确认这些说法；删除不代表认定产品不支持该能力。如需恢复，应由项目维护者补充相应功能说明及准确率测试条件、方法和结果。保留原标题、旧稿第一和第三镜的画面、事实原文及相对顺序，仅介绍字幕相关功能。本次针对节奏审核反馈，将第一镜停留从8秒缩短至4秒；便签改字镜头仍为8秒，其余内容不变。以上为创作者审稿备注，不进入视频。

## 实际修订

位置按镜头索引比较；日志关联的是实际反馈，不证明模型因果推理。

- 修改：editor_notes, shot:2/visual, shot:2/block:1, shot:3:removed；保留原镜头 1 个、原文案块 1 个。
- 修订前失败检查：rules_check
- 修改：editor_notes, shot:1/hold_seconds；保留原镜头 1 个、原文案块 2 个。
- 修订前失败检查：requirements_check

预计总时长：12.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "1652fb1fb96317a5bb5b8c73766915a9d125837e8742108e0a0070b06e40560c",
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
      "text": "口播字幕小帮手"
    },
    {
      "location": "shot:1/visual",
      "text": "桌上的采访话筒"
    },
    {
      "location": "shot:2/visual",
      "text": "便签上手改错字"
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
  "script_hash": "1652fb1fb96317a5bb5b8c73766915a9d125837e8742108e0a0070b06e40560c",
  "request_hash": "7fb52283cc4eb7795933e6f2730cfb020711e034af85be6312f908b57de4f30b",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "审核并修改所附字幕介绍旧稿",
      "verdict": "met",
      "evidence": "当前稿删除旧稿第二镜的自动识别画面及准确率文案，保留原标题和原第一、第三镜，并将第一镜最低停留缩短至4秒。"
    },
    {
      "field": "topic",
      "requirement": "保留可确认的产品功能",
      "verdict": "met",
      "evidence": "当前第一镜保留“剪影练习版支持为视频添加字幕。”，第二镜保留“字幕文字可以手动编辑。”；rules_check已分别核对P01.F1、P01.F2并通过。"
    },
    {
      "field": "topic",
      "requirement": "明确处理无法确认的说法",
      "verdict": "met",
      "evidence": "“显示自动识别示意”和“自动识别人声，字幕准确率达到99%。”均已删除。editor_notes明确说明缺少能力证明及准确率测试资料，并准确区分“无法确认”与“不支持”；说明未进入面向观众的内容。"
    },
    {
      "field": "audience",
      "requirement": "新手内容创作者",
      "verdict": "met",
      "evidence": "两镜分别介绍添加字幕和手动编辑文字，表述直白，无需专业知识；“便签上手改错字”提供容易理解的修改示意。"
    },
    {
      "field": "platform",
      "requirement": "小红书",
      "verdict": "met",
      "evidence": "标题“口播字幕小帮手”简短明确，两镜围绕字幕实用功能展开，搭配采访话筒和改字画面，适合简短的创作工具介绍。"
    },
    {
      "field": "style",
      "requirement": "客观",
      "verdict": "met",
      "evidence": "旁白仅保留已获资料支持的两项功能，已删除自动识别及99%准确率声明，没有添加效果保证。"
    },
    {
      "field": "style",
      "requirement": "实用",
      "verdict": "met",
      "evidence": "内容直接说明可以添加字幕、手动编辑字幕文字，第二镜以改错字动作对应具体使用需求。"
    }
  ],
  "summary": "已落实审核修改要求：保留两项可确认的字幕功能，删除未证实的自动识别及准确率说法，并在审稿备注中准确说明处理原因。受众、平台、风格和节奏均符合要求。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "口播字幕小帮手",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于字幕主题的概括性标题，“小帮手”未构成具体性能或效果承诺。"
    },
    {
      "location": "shot:1/visual",
      "text": "桌上的采访话筒",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅安排采访相关道具与场景，没有宣称产品能力或真实客户案例。"
    },
    {
      "location": "shot:2/visual",
      "text": "便签上手改错字",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于便签上的手动改字拍摄安排，未虚构产品按钮、界面或操作流程。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "duration_check给出第一镜4秒、14个旁白单位，足以呈现简短说明与话筒画面；第二镜8秒、10个旁白单位，同时安排手改错字动作，有观察内容支撑停留。两镜功能不同，无重复凑时长；总长估算12秒，已通过28秒上限检查，editor_notes不参与计时。"
  },
  "expression_review_passed": true
}
```

## 执行路径

estimate_duration → check_rules → search_materials → write_script → estimate_duration → check_rules → check_requirements → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
