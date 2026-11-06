# 短视频脚本运行结果

- 状态：`needs_input`
- 证据类型：`real_model`
- 说明：现稿估算17秒，时长和规则检查均通过，但未体现餐饮门店拍菜单介绍视频的场景。请在 brand_rules.creative_copy 和 visuals 中补充获准使用的菜单场景文案与画面，以便保留现有结构并针对性修订。

## 字幕，让表达被看见

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

画面：日常生活素材蒙太奇

旁白/字幕：从一段日常记录开始。

来源：

预计镜头时长：3.5 秒

### 分镜 2

画面：将旁白作为字幕叠加在日常画面上

旁白/字幕：剪影练习版支持为视频添加字幕。

来源：P01/P01.F1

预计镜头时长：5.0 秒

### 分镜 3

画面：产品功能文字卡片，不展示未经提供的界面

旁白/字幕：字幕文字可以手动编辑。

来源：P01/P01.F2

预计镜头时长：5.0 秒

### 分镜 4

画面：简洁背景展示结尾文字

旁白/字幕：把想说的话，放进画面里。

来源：

预计镜头时长：3.5 秒

预计总时长：17.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "8ed608dfc58355b65155574551ac583a835b78e8b3a08af4950cdbd99580a35e",
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

## 执行路径

search_materials → write_script → estimate_duration → check_rules → search_materials → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
