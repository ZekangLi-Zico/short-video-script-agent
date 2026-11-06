# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：脚本已通过来源、规则与预计时长检查；仍为可编辑脚本，未生成或发布视频。

## 从一段记录开始

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

画面：日常生活素材蒙太奇

旁白/字幕：从一段日常记录开始。

来源：

预计镜头时长：3.5 秒

### 分镜 2

画面：产品功能文字卡片，不展示未经提供的界面

旁白/字幕：剪影练习版支持裁剪视频片段。

来源：P02/P02.F1

预计镜头时长：6.0 秒

### 分镜 3

画面：简洁背景展示结尾文字

旁白/字幕：试试你的下一条短片吧。

来源：

预计镜头时长：3.5 秒

预计总时长：13.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "6025cc3c180005cd9b0293c4cb886ea93ea543de907e4e55ede0ba3fa5cfccc3",
  "passed": true,
  "issues": [],
  "citations": [
    {
      "location": "shot:2/block:1",
      "source_id": "P02",
      "fact_id": "P02.F1",
      "quote": "剪影练习版支持裁剪视频片段。",
      "version": "2026-11-01"
    }
  ],
  "rules_version": "2026-11-03-v1"
}
```

## 执行路径

search_materials → write_script → estimate_duration → check_rules → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
