# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：脚本已通过来源、规则与预计时长检查；仍为可编辑脚本，未生成或发布视频。

## 字幕，让表达被看见

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

画面：人物面对镜头提出问题

旁白/字幕：想让画面里的表达更清楚？

来源：

预计镜头时长：3.3 秒

### 分镜 2

画面：产品功能文字卡片，不展示未经提供的界面

旁白/字幕：剪影练习版支持为视频添加字幕。字幕文字可以手动编辑。

来源：P01/P01.F1, P01/P01.F2

预计镜头时长：6.5 秒

预计总时长：9.8 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "4de99b05c5109ae5b829a23f96e054c2b145a7b099f14377a915c6f509636cd9",
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
      "location": "shot:2/block:2",
      "source_id": "P01",
      "fact_id": "P01.F2",
      "quote": "字幕文字可以手动编辑。",
      "version": "2026-11-01"
    }
  ],
  "rules_version": "2026-11-03-v1"
}
```

## 执行路径

estimate_duration → check_rules → search_materials → write_script → estimate_duration → check_rules → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
