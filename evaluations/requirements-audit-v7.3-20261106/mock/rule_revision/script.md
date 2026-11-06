# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`offline_mock_not_model_evidence`
- 说明：当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 字幕，让表达被看见

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 旧稿合并文案（未区分声画）

剪影练习版支持为视频添加字幕。

### 分镜 1

画面：产品功能文字卡片，不展示未经提供的界面

旁白/字幕：剪影练习版支持为视频添加字幕。

来源：P01/P01.F1

预计镜头时长：4.0 秒

## 实际修订

位置按镜头索引比较；日志关联的是实际反馈，不证明模型因果推理。

- 修改：shot:1/visual, shot:1/block:1, shot:2:removed；保留原镜头 0 个、原文案块 0 个。
- 修订前失败检查：rules_check

预计总时长：4.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "dee0c4cf8a9e7629e42ce06857ea4023f4187e26e99fccc4b0594db0e3fe4996",
  "passed": true,
  "issues": [],
  "citations": [
    {
      "location": "shot:1/block:1",
      "source_id": "P01",
      "fact_id": "P01.F1",
      "quote": "剪影练习版支持为视频添加字幕。",
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
  "script_hash": "dee0c4cf8a9e7629e42ce06857ea4023f4187e26e99fccc4b0594db0e3fe4996",
  "request_hash": "189f54e56fb872316428df1c242be854aa7b82bf239d32cbac2c2e0d6ad1c30d",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "介绍字幕功能",
      "verdict": "met",
      "evidence": "固定离线桩返回；仅验证接线，不证明语义符合。"
    },
    {
      "field": "audience",
      "requirement": "第一次制作口播短视频的创作者",
      "verdict": "met",
      "evidence": "固定离线桩返回；仅验证接线，不证明语义符合。"
    },
    {
      "field": "platform",
      "requirement": "抖音",
      "verdict": "met",
      "evidence": "固定离线桩返回；仅验证接线，不证明语义符合。"
    },
    {
      "field": "style",
      "requirement": "清楚、友好、克制",
      "verdict": "met",
      "evidence": "固定离线桩返回；仅验证接线，不证明语义符合。"
    }
  ],
  "summary": "固定离线需求检查，不证明真实语义判断。",
  "method": "model_assessment_not_deterministic_proof"
}
```

## 执行路径

search_materials → estimate_duration → check_rules → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
