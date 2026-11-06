# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成旧稿审核与修改：保留原题、添加字幕和手动编辑功能，删除无法确认的人声识别及99%准确率说法，并在备注说明原因。成稿共2镜，预计16秒，全部检查通过。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 口播字幕小帮手

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

镜头目的：展示为口播视频添加字幕的功能

画面：桌上的采访话筒旁，创作者录制一句口播；随后展示同一视频带有字幕的画面。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–4.0 秒**

旁白＋同步字幕：剪影练习版支持为视频添加字幕。

依据：P01/P01.F1

镜头末尾保持画面：4.0–8.0 秒（保留最后一拍屏幕文字）

预计镜头时长：8.0 秒

### 分镜 2

镜头目的：展示字幕文字可手动修改

画面：先拍便签上手改错字，再切到视频字幕文字的编辑演示：将一个错字手动改正，最后展示修改后的字幕。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–3.0 秒**

旁白＋同步字幕：字幕文字可以手动编辑。

依据：P01/P01.F2

镜头末尾保持画面：3.0–8.0 秒（保留最后一拍屏幕文字）

预计镜头时长：8.0 秒

## 审稿备注（不进入视频，不计入时长）

供创作者核对修改与资料缺口，不是经过事实认证的产品介绍。

保留原题及原稿两句已获资料支持的功能文案。客户未提供人声识别能力及字幕准确率数据，已删除相关声明、99%数字及对应示意镜头；仅保留添加字幕和手动编辑文字两项已确认功能。

## 实际修订

位置按镜头索引比较；日志关联的是实际反馈，不证明模型因果推理。

- 修改：format_version, editor_notes, shot:1/visual, shot:1/purpose, shot:1/block:1, shot:2/visual, shot:2/purpose, shot:2/block:1, shot:3:removed；保留原镜头 0 个、原文案块 0 个。
- 修订前失败检查：rules_check

预计总时长：16.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "f2b3b5311b5f7cb9c3c3d43306cde4a94e6a29deb60320ff06487e078b42dbbd",
  "passed": true,
  "issues": [],
  "citations": [
    {
      "location": "shot:1/block:1",
      "source_id": "P01",
      "fact_id": "P01.F1",
      "quote": "剪影练习版支持为视频添加字幕。",
      "version": "2026-11-01",
      "text": "剪影练习版支持为视频添加字幕。",
      "requires_semantic_review": true
    },
    {
      "location": "shot:2/block:1",
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
      "text": "口播字幕小帮手"
    },
    {
      "location": "shot:1/visual",
      "text": "桌上的采访话筒旁，创作者录制一句口播；随后展示同一视频带有字幕的画面。"
    },
    {
      "location": "shot:1/block:1",
      "text": "剪影练习版支持为视频添加字幕。"
    },
    {
      "location": "shot:2/visual",
      "text": "先拍便签上手改错字，再切到视频字幕文字的编辑演示：将一个错字手动改正，最后展示修改后的字幕。"
    },
    {
      "location": "shot:2/block:1",
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
    },
    {
      "source_id": "P03",
      "fact_id": "P03.F1",
      "quote": "剪影练习版提供横屏和竖屏画面比例选项。",
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
  "script_hash": "f2b3b5311b5f7cb9c3c3d43306cde4a94e6a29deb60320ff06487e078b42dbbd",
  "request_hash": "7fb52283cc4eb7795933e6f2730cfb020711e034af85be6312f908b57de4f30b",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "审核并修改所附字幕介绍旧稿",
      "verdict": "met",
      "evidence": "当前稿保留添加字幕和手动编辑两镜，删除旧稿自动识别示意及其声明。"
    },
    {
      "field": "topic",
      "requirement": "客户没有提供自动识别和准确率数据",
      "verdict": "met",
      "evidence": "公开内容已移除自动识别人声及99%准确率，editor_notes准确说明资料缺口。"
    },
    {
      "field": "topic",
      "requirement": "保留可确认的产品功能",
      "verdict": "met",
      "evidence": "第1、2镜分别保留原稿中有P01.F1、P01.F2支持的添加字幕和手动编辑功能。"
    },
    {
      "field": "topic",
      "requirement": "明确处理无法确认的说法",
      "verdict": "met",
      "evidence": "editor_notes明确说明删除相关声明、99%数字及对应示意镜头，与实际删改一致。"
    },
    {
      "field": "audience",
      "requirement": "新手内容创作者",
      "verdict": "met",
      "evidence": "两镜以录制口播、展示字幕和改正错字解释基础功能，文字简明易懂。"
    },
    {
      "field": "platform",
      "requirement": "小红书",
      "verdict": "met",
      "evidence": "以简短标题、同步声画和具体功能演示组成16秒短视频，适合平台浏览。"
    },
    {
      "field": "style",
      "requirement": "客观",
      "verdict": "met",
      "evidence": "两句公开功能文案均与素材原文一致，没有准确率或自动化夸大。"
    },
    {
      "field": "style",
      "requirement": "实用",
      "verdict": "met",
      "evidence": "第2镜展示手动改正字幕错字及修改结果，提供具体使用示例。"
    }
  ],
  "summary": "当前稿已落实旧稿审核与修改要求，保留两项已确认功能，并在审稿备注中准确说明未证实说法的删除处理。公开内容有资料支持，时长与镜头节奏合理。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "口播字幕小帮手",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于概括主题的轻量标题，不包含具体性能或效果承诺。"
    },
    {
      "location": "shot:1/visual",
      "text": "桌上的采访话筒旁，创作者录制一句口播；随后展示同一视频带有字幕的画面。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "字幕结果展示由添加字幕功能支持，口播录制属于拍摄场景，未宣称自动识别。"
    },
    {
      "location": "shot:1/block:1",
      "text": "剪影练习版支持为视频添加字幕。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "与P01.F1原文完全一致。"
    },
    {
      "location": "shot:2/visual",
      "text": "先拍便签上手改错字，再切到视频字幕文字的编辑演示：将一个错字手动改正，最后展示修改后的字幕。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "手动改正字幕错字属于文字编辑能力，未虚构按钮、界面布局或自动流程。"
    },
    {
      "location": "shot:2/block:1",
      "text": "字幕文字可以手动编辑。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "与P01.F2原文完全一致。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "两镜各8秒：第1镜声画同步4秒后可观察口播与字幕结果，第2镜同步3秒后有改字动作及结果展示支撑停留；总计16秒，通过28秒上限检查。"
  },
  "expression_review_passed": true
}
```

## 执行路径

check_rules → search_materials → write_script → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
