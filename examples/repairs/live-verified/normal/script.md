# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成面向口播新手的4镜字幕功能介绍稿，涵盖添加字幕和手动编辑，保留当前稿，无需删改。预计12.8秒，在30秒上限内；三项检查均通过。时长为估算，需求覆盖已通过模型审核。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 字幕，让表达被看见

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

画面：人物面对镜头提出问题

旁白/字幕：想让画面里的表达更清楚？

来源：

预计镜头时长：3.3 秒

### 分镜 2

画面：产品功能文字卡片，不展示未经提供的界面

旁白/字幕：剪影练习版支持为视频添加字幕。

来源：P01/P01.F1

预计镜头时长：4.0 秒

### 分镜 3

画面：将旁白作为字幕叠加在日常画面上

旁白/字幕：字幕文字可以手动编辑。

来源：P01/P01.F2

预计镜头时长：3.0 秒

### 分镜 4

画面：简洁背景展示结尾文字

旁白/字幕：先从一条短片开始。

来源：

预计镜头时长：2.5 秒

预计总时长：12.8 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "41567b6bac00727b808114f6e804596f99f9618d4ced7889b0880e4ffdf1f75f",
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
  "rules_version": "2026-11-03-v1"
}
```

## 需求覆盖核对

以下为模型评估，可能漏判或误判，仍需人工确认。

```json
{
  "ok": true,
  "script_hash": "41567b6bac00727b808114f6e804596f99f9618d4ced7889b0880e4ffdf1f75f",
  "request_hash": "405fda7ba61c0d7613c9cdcba2f46e53964582afa08d59d1d10281de288afaef",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "介绍字幕功能",
      "verdict": "met",
      "evidence": "第2镜介绍“支持为视频添加字幕”，第3镜介绍“字幕文字可以手动编辑”，覆盖字幕功能介绍。"
    },
    {
      "field": "audience",
      "requirement": "第一次制作口播短视频的创作者",
      "verdict": "met",
      "evidence": "第1镜采用人物面对镜头的口播场景，后续用简单语言介绍添加字幕和手动编辑，没有专业术语门槛，适合初次创作的受众。"
    },
    {
      "field": "platform",
      "requirement": "抖音",
      "verdict": "met",
      "evidence": "以“想让画面里的表达更清楚？”提问开场，随后通过功能文字卡片和字幕叠加画面传达单一主题，适合短视频浏览。"
    },
    {
      "field": "style",
      "requirement": "清楚",
      "verdict": "met",
      "evidence": "第2、3镜分别说明添加字幕和手动编辑，每镜表达一个功能点，句意明确。"
    },
    {
      "field": "style",
      "requirement": "友好",
      "verdict": "met",
      "evidence": "开场以提问引入，结尾“先从一条短片开始。”给予温和鼓励，没有责备或施压表达。"
    },
    {
      "field": "style",
      "requirement": "克制",
      "verdict": "met",
      "evidence": "正文直接说明字幕功能，没有夸张效果承诺、最高级宣传或强迫转化话术。"
    }
  ],
  "summary": "当前稿件已覆盖字幕功能介绍，适合初次制作口播短视频的创作者及抖音场景，表达清楚、友好、克制。",
  "method": "model_assessment_not_deterministic_proof"
}
```

## 执行路径

search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
