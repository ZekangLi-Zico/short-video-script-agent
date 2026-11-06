# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成旧稿审核与修改：保留原标题、添加字幕和手动编辑字幕两项已确认功能及原镜头顺序；删除自动识别示意和“准确率达到99%”说法；首镜停留由8秒缩短至4秒。当前估时12秒，符合28秒上限，三项检查均通过。审稿备注已说明删除原因：相关说法尚未确认，不代表产品不支持；如需恢复，须向项目维护者提供可核验的功能说明及准确率测试依据。

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

保留原标题及原第一、第三镜的画面、事实文案和顺序。根据节奏审核反馈，将第一镜停留由8秒缩短至4秒，保留原第三镜8秒停留。两镜事实文案均作旁白。已删除原第二镜的自动识别示意及“自动识别人声，字幕准确率达到99%。”。客户未提供相关功能依据及准确率数据，两项说法均未确认；删除不代表确认产品不支持该能力。若需恢复相关表述，需向项目维护者提供可核验的官方功能说明及准确率测试依据。本备注不进入视频。

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
  "script_hash": "178ca0d94d70b1801795c0e04b660ff84592d9cfa705ee469ff05809620a6dec",
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
  "script_hash": "178ca0d94d70b1801795c0e04b660ff84592d9cfa705ee469ff05809620a6dec",
  "request_hash": "7fb52283cc4eb7795933e6f2730cfb020711e034af85be6312f908b57de4f30b",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "审核并修改所附字幕介绍旧稿",
      "verdict": "met",
      "evidence": "当前稿保留旧稿第一、第三镜并维持顺序，删除旧稿第二镜；editor_notes准确说明实际删改，且不进入视频。"
    },
    {
      "field": "topic",
      "requirement": "保留可确认的产品功能",
      "verdict": "met",
      "evidence": "当前第1镜保留“剪影练习版支持为视频添加字幕。”，第2镜保留“字幕文字可以手动编辑。”；rules_check已分别核对P01.F1、P01.F2并通过。"
    },
    {
      "field": "topic",
      "requirement": "明确处理无法确认的说法",
      "verdict": "met",
      "evidence": "已删除“显示自动识别示意”及“自动识别人声，字幕准确率达到99%。”。editor_notes明确说明客户未提供相关功能依据及准确率数据，两项说法未确认，且删除不代表产品不支持，说明与实际修改一致。"
    },
    {
      "field": "audience",
      "requirement": "新手内容创作者",
      "verdict": "met",
      "evidence": "两镜分别介绍添加字幕和手动编辑字幕，措辞直接，无专业术语；第2镜“便签上手改错字”提供易理解的动作示意。"
    },
    {
      "field": "platform",
      "requirement": "小红书",
      "verdict": "met",
      "evidence": "标题“口播字幕小帮手”明确主题，两镜聚焦字幕功能，旁白简短，配合话筒和改字画面，适合短视频浏览。"
    },
    {
      "field": "style",
      "requirement": "客观",
      "verdict": "met",
      "evidence": "旁白仅陈述已核对的添加字幕、手动编辑功能；未保留自动识别、99%准确率或其他未经支持的效果承诺。"
    },
    {
      "field": "style",
      "requirement": "实用",
      "verdict": "met",
      "evidence": "第1镜说明可以添加字幕，第2镜说明字幕文字可以手动修改，并以手改错字画面呈现具体用途。"
    }
  ],
  "summary": "需求已落实：保留两项可确认功能，删除自动识别及99%准确率的未确认说法，审稿备注与实际修改一致。表达审核和镜头节奏均通过。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "口播字幕小帮手",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于主题概括和拟人化表达，未承诺自动识别、准确率或具体效率效果。"
    },
    {
      "location": "shot:1/visual",
      "text": "桌上的采访话筒",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于口播、采访背景的拍摄安排，不声称产品具备采访录音或自动转写能力。"
    },
    {
      "location": "shot:2/visual",
      "text": "便签上手改错字",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于手动改字的生活化动作示意，没有虚构产品按钮、界面或操作流程。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "duration_check给出第1镜4秒、14个旁白单位，第2镜8秒、10个旁白单位，均满足对应最低停留时间。第1镜内容简短；第2镜的手写改错动作可支撑旁白后的观察时间，两镜介绍不同功能，没有重复同一事实凑时长。总长预计12秒，宿主已判定满足28秒上限。"
  },
  "expression_review_passed": true
}
```

## 执行路径

estimate_duration → check_rules → search_materials → write_script → estimate_duration → check_rules → check_requirements → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
