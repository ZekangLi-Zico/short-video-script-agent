# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：脚本已通过来源、规则与预计时长检查；仍为可编辑脚本，未生成或发布视频。

## 字幕，让表达被看见

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

画面：产品功能文字卡片，不展示未经提供的界面

旁白/字幕：剪影练习版支持为视频添加字幕。

来源：P01/P01.F1

预计镜头时长：5.5 秒

预计总时长：5.5 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "d7eafe07e6b90bfc91fd5ccabd73498fe2ac2ee3794853a4231de44ee87f710a",
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

## 执行路径

search_materials → write_script → estimate_duration → check_rules → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
