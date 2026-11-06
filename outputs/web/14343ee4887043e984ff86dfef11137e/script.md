# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成3镜字幕功能脚本，预计13.3秒，符合25秒上限。介绍添加字幕和手动编辑能力；公开文案未采用“播放量提高30%”，备注已说明统计依据及授权缺口。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 字幕，让表达被看见

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

镜头目的：通过店铺口播回放引出字幕需求。

画面：店员在货架前录制商品口播，运营拿起手机回看。镜头从拍摄现场切到尚未添加字幕的素材预览；本镜文案置于预览画面外。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–3.3 秒**

旁白＋同步字幕：想让画面里的表达更清楚？

预计镜头时长：3.3 秒

### 分镜 2

镜头目的：展示为店铺视频添加字幕的能力。

画面：延续同一段店铺素材，从无字幕画面切到叠加本镜文案的画面，停留展示字幕。采用成片示意，不展示具体产品界面或按钮。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–4.0 秒**

旁白＋同步字幕：剪影练习版支持为视频添加字幕。

依据：P01/P01.F1

镜头末尾保持画面：4.0–5.0 秒（保留最后一拍屏幕文字）

预计镜头时长：5.0 秒

### 分镜 3

镜头目的：展示字幕文字可以手动修改。

画面：运营对照视频核对文字，镜头切到手部敲键；中性编辑示意中，本镜字幕文字被选中并手动重新输入，最后切回带字幕的视频预览。不展示具体产品按钮。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–3.0 秒**

旁白＋同步字幕：字幕文字可以手动编辑。

依据：P01/P01.F2

镜头末尾保持画面：3.0–5.0 秒（保留最后一拍屏幕文字）

预计镜头时长：5.0 秒

## 审稿备注（不进入视频，不计入时长）

供创作者核对修改与资料缺口，不是经过事实认证的产品介绍。

未将客户口述的“播放量提高30%”用于标题、旁白或屏幕文字：目前缺少统计依据及使用授权，不能作为已验证效果或公开案例。正文仅介绍已有资料支持的字幕能力。

预计总时长：13.3 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "80b703f85fb37fcb68757bd501c711ef2d9982e0f68cd96b9acba3bd1c0d8854",
  "passed": true,
  "issues": [],
  "citations": [
    {
      "location": "shot:2/block:1",
      "source_id": "P01",
      "fact_id": "P01.F1",
      "quote": "剪影练习版支持为视频添加字幕。",
      "version": "2026-11-01",
      "text": "剪影练习版支持为视频添加字幕。",
      "requires_semantic_review": true
    },
    {
      "location": "shot:3/block:1",
      "source_id": "P01",
      "fact_id": "P01.F2",
      "quote": "字幕文字可以手动编辑。",
      "version": "2026-11-01",
      "text": "字幕文字可以手动编辑。",
      "requires_semantic_review": true
    }
  ],
  "rules_version": "2026-11-03-v1",
  "requires_expression_review": true,
  "expression_slots": [
    {
      "location": "title",
      "text": "字幕，让表达被看见"
    },
    {
      "location": "shot:1/visual",
      "text": "店员在货架前录制商品口播，运营拿起手机回看。镜头从拍摄现场切到尚未添加字幕的素材预览；本镜文案置于预览画面外。"
    },
    {
      "location": "shot:1/block:1",
      "text": "想让画面里的表达更清楚？"
    },
    {
      "location": "shot:2/visual",
      "text": "延续同一段店铺素材，从无字幕画面切到叠加本镜文案的画面，停留展示字幕。采用成片示意，不展示具体产品界面或按钮。"
    },
    {
      "location": "shot:2/block:1",
      "text": "剪影练习版支持为视频添加字幕。"
    },
    {
      "location": "shot:3/visual",
      "text": "运营对照视频核对文字，镜头切到手部敲键；中性编辑示意中，本镜字幕文字被选中并手动重新输入，最后切回带字幕的视频预览。不展示具体产品按钮。"
    },
    {
      "location": "shot:3/block:1",
      "text": "字幕文字可以手动编辑。"
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
  "scope": "source_identity_and_brand_checks; every public claim requires semantic entailment review"
}
```

## 需求覆盖核对

以下为模型评估，可能漏判或误判，仍需人工确认。

```json
{
  "ok": true,
  "script_hash": "80b703f85fb37fcb68757bd501c711ef2d9982e0f68cd96b9acba3bd1c0d8854",
  "request_hash": "93972873cc931936e79f564ca370d65259052b284f9983eeaaba7d87a79a6a9d",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "请写一条介绍字幕功能的脚本",
      "verdict": "met",
      "evidence": "第2镜介绍“支持为视频添加字幕”，第3镜介绍“字幕文字可以手动编辑”，均配有相应示意画面。"
    },
    {
      "field": "topic",
      "requirement": "处理这个说法",
      "verdict": "met",
      "evidence": "公开内容未使用“播放量提高30%”；editor_notes准确说明已删除该效果说法，并指出缺少统计依据及使用授权。"
    },
    {
      "field": "topic",
      "requirement": "不要把口头反馈包装成已验证效果",
      "verdict": "met",
      "evidence": "标题及全部分镜均未宣称播放量提升，也未将客户口述作为案例或背书；正文仅介绍有来源支持的字幕能力。"
    },
    {
      "field": "audience",
      "requirement": "店铺内容运营",
      "verdict": "met",
      "evidence": "第1镜呈现店员在货架前录制商品口播、运营回看素材；第3镜呈现运营核对并修改字幕，贴合店铺内容工作。"
    },
    {
      "field": "platform",
      "requirement": "抖音",
      "verdict": "met",
      "evidence": "采用问题开场、三镜短篇和同步声画文案，字幕能力通过直观示意展示，适合短视频观看；宿主估算总长13.3秒。"
    },
    {
      "field": "style",
      "requirement": "可信",
      "verdict": "met",
      "evidence": "第2、3镜功能文案分别由P01.F1、P01.F2直接支持，未使用未经验证的增长数字或客户背书。"
    },
    {
      "field": "style",
      "requirement": "少口号",
      "verdict": "met",
      "evidence": "标题“字幕，让表达被看见”为简短修辞；主体两镜直接说明添加字幕和手动编辑功能，没有连续口号或夸张效果承诺。"
    }
  ],
  "summary": "需求已落实。公开内容未使用“播放量提高30%”，审稿备注准确交代了统计依据及授权缺口；字幕功能介绍有资料支持，店铺场景和节奏合理。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "字幕，让表达被看见",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于与字幕主题相关的修辞标题，未承诺播放量、传播效果或额外产品能力。"
    },
    {
      "location": "shot:1/visual",
      "text": "店员在货架前录制商品口播，运营拿起手机回看。镜头从拍摄现场切到尚未添加字幕的素材预览；本镜文案置于预览画面外。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "描述店铺拍摄、回看和文案位置安排，未声称产品提供拍摄或预览功能，也未呈现具体产品界面。"
    },
    {
      "location": "shot:1/block:1",
      "text": "想让画面里的表达更清楚？",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "以问句引出表达需求，未断言产品能实现某种经验证的效果。"
    },
    {
      "location": "shot:2/visual",
      "text": "延续同一段店铺素材，从无字幕画面切到叠加本镜文案的画面，停留展示字幕。采用成片示意，不展示具体产品界面或按钮。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "无字幕到带字幕的成片示意对应“支持为视频添加字幕”，没有增加自动生成、识别或具体操作流程的声明。"
    },
    {
      "location": "shot:2/block:1",
      "text": "剪影练习版支持为视频添加字幕。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "与P01.F1原文完全一致，引用保留原块标注的来源和事实ID。"
    },
    {
      "location": "shot:3/visual",
      "text": "运营对照视频核对文字，镜头切到手部敲键；中性编辑示意中，本镜字幕文字被选中并手动重新输入，最后切回带字幕的视频预览。不展示具体产品按钮。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        },
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "选中文字并重新输入是手动编辑的中性示意，由P01.F2支持；带字幕的成片由P01.F1支持。未指定产品按钮、界面布局或自动流程。"
    },
    {
      "location": "shot:3/block:1",
      "text": "字幕文字可以手动编辑。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "与P01.F2原文完全一致，未增加自动纠错等能力，引用与原块标注一致。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "第1镜预计3.3秒，承载简短提问及拍摄现场转回看画面；第2镜5秒包含4秒同步声画和1秒字幕观察；第3镜5秒包含3秒同步声画和2秒编辑、成片观察余量。两处5秒最低停留均有具体画面任务，未重复同一事实凑时长。总长13.3秒，宿主已判定符合25秒上限；editor_notes不计入播放。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
