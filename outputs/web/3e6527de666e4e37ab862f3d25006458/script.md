# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成：全程展示“开讲”卡片，旁白仅为“剪影练习版支持为视频添加字幕。”无寒暄、无第二个功能。估算4秒，符合6秒上限；三项检查均通过，无需删改，无待补事项。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 开讲

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

画面：一张写着“开讲”的静态卡片，全程保持。

旁白/字幕：剪影练习版支持为视频添加字幕。

来源：P01/P01.F1

预计镜头时长：4.0 秒

## 审稿备注（不进入视频，不计入时长）

供创作者核对修改与资料缺口，不是经过事实认证的产品介绍。

事实块用作旁白；“开讲”为卡片文字，不作口播。

预计总时长：4.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "f3f0e450e61222730b4e707145a9eee0ad87632b5ba96d3eb5ecad9d813e6ba8",
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
  "rules_version": "2026-11-03-v1",
  "requires_expression_review": true,
  "expression_slots": [
    {
      "location": "title",
      "text": "开讲"
    },
    {
      "location": "shot:1/visual",
      "text": "一张写着“开讲”的静态卡片，全程保持。"
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
  "script_hash": "f3f0e450e61222730b4e707145a9eee0ad87632b5ba96d3eb5ecad9d813e6ba8",
  "request_hash": "0d282f89aa8e9846961d0637ec6061a9078d699019bca1b92d101b914577a3e9",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "六秒以内",
      "verdict": "met",
      "evidence": "duration_check估算总长4.0秒，passed=true，符合6秒上限。"
    },
    {
      "field": "topic",
      "requirement": "剪影练习版支持为视频添加字幕。",
      "verdict": "met",
      "evidence": "第1镜唯一旁白为“剪影练习版支持为视频添加字幕。”，rules_check已核对P01.F1并通过。"
    },
    {
      "field": "topic",
      "requirement": "只介绍剪影练习版支持为视频添加字幕。",
      "verdict": "met",
      "evidence": "第1镜仅介绍添加字幕；标题与画面仅出现“开讲”，未介绍字幕编辑、视频裁剪或画面比例等其他功能。"
    },
    {
      "field": "topic",
      "requirement": "不要开场寒暄",
      "verdict": "met",
      "evidence": "第1镜旁白直接说明添加字幕功能，没有问候或寒暄。"
    },
    {
      "field": "topic",
      "requirement": "不加第二个功能",
      "verdict": "met",
      "evidence": "全稿只有第1镜的一句添加字幕功能说明，没有第二项功能。"
    },
    {
      "field": "topic",
      "requirement": "画面是一张写着“开讲”的卡片。",
      "verdict": "met",
      "evidence": "第1镜画面明确为“一张写着‘开讲’的静态卡片，全程保持。”"
    },
    {
      "field": "audience",
      "requirement": "刚进入课程页的访客",
      "verdict": "met",
      "evidence": "“开讲”卡片配合一句直白的功能说明，无需产品知识即可理解，适合初次进入课程页的访客。"
    },
    {
      "field": "platform",
      "requirement": "抖音",
      "verdict": "met",
      "evidence": "单镜头预计4.0秒，直接传达一个功能，卡片文字仅“开讲”，适合短视频快速观看。"
    },
    {
      "field": "style",
      "requirement": "极简",
      "verdict": "met",
      "evidence": "全稿仅一张静态卡片和一句旁白，无额外镜头或装饰性文案。"
    },
    {
      "field": "style",
      "requirement": "信息优先",
      "verdict": "met",
      "evidence": "旁白开头即说明产品支持添加字幕，没有铺垫或无关内容。"
    }
  ],
  "summary": "当前稿满足全部明确要求：预计4秒，仅介绍添加字幕，无寒暄或第二个功能，全程展示“开讲”卡片。表达与节奏检查均通过。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "开讲",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于开场提示，不包含产品能力或效果承诺。"
    },
    {
      "location": "shot:1/visual",
      "text": "一张写着“开讲”的静态卡片，全程保持。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅描述卡片文字和拍摄安排，不涉及产品功能、界面或操作步骤。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "第1镜预计4.0秒，承载14个旁白单位和“开讲”卡片，停留有完整旁白支撑，无重复或空镜凑时长。hold_seconds=0仅表示没有额外延长；editor_notes不计入口播。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
