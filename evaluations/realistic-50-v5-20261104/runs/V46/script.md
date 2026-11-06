# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成《口播字幕小帮手》三镜修订稿，预计24秒。保留原标题、添加字幕及手动编辑功能；删除无依据的识别能力、99%准确率宣称及相关示意，并在备注中说明原因。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 口播字幕小帮手

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

镜头目的：通过一段口播展示添加字幕的用途。

画面：桌上的采访话筒旁，创作者录下一句口播；切到这段口播的后期示意画面，从无字幕变为显示对应字幕，不展示产品按钮。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–4.0 秒**

旁白＋同步字幕：剪影练习版支持为视频添加字幕。

依据：P01/P01.F1

镜头末尾保持画面：4.0–8.0 秒（保留最后一拍屏幕文字）

预计镜头时长：8.0 秒

### 分镜 2

镜头目的：展示核对字幕的动作，为下一镜手动改字建立具体需求。

画面：创作者回放刚才的口播，对照纸上抄写的字幕逐字核对，发现一处错字后用笔圈出；近景停留，让观众看清需要修改的位置。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–3.0 秒**

旁白＋同步字幕：把想说的话，放进画面里。

镜头末尾保持画面：3.0–8.0 秒（保留最后一拍屏幕文字）

预计镜头时长：8.0 秒

### 分镜 3

镜头目的：展示手动编辑字幕文字，完成从发现错字到修正的过程。

画面：便签上手改刚才圈出的错字；随后以字幕文字示意呈现修改前后的变化，最后回到口播画面展示修正后的字幕，不虚构产品界面或操作按钮。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–3.0 秒**

旁白＋同步字幕：字幕文字可以手动编辑。

依据：P01/P01.F2

镜头末尾保持画面：3.0–8.0 秒（保留最后一拍屏幕文字）

预计镜头时长：8.0 秒

## 审稿备注（不进入视频，不计入时长）

供创作者核对修改与资料缺口，不是经过事实认证的产品介绍。

已删除旧稿第二镜的语音识别能力及99%准确率宣称和相关示意，现有资料未提供依据。保留原标题、三镜结构、原有停留时长及两句已确认功能文案；第二镜改为字幕核对场景，并补全声画标记。

## 实际修订

位置按镜头索引比较；日志关联的是实际反馈，不证明模型因果推理。

- 修改：format_version, editor_notes, shot:1/visual, shot:1/purpose, shot:1/block:1, shot:2/visual, shot:2/purpose, shot:2/block:1, shot:3/visual, shot:3/purpose, shot:3/block:1；保留原镜头 0 个、原文案块 0 个。
- 修订前失败检查：rules_check

预计总时长：24.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "e267265948ca221d9e34fae0ac75529ff4f2b2241ede5c8fbc65fb8db2a91d6b",
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
      "text": "口播字幕小帮手"
    },
    {
      "location": "shot:1/visual",
      "text": "桌上的采访话筒旁，创作者录下一句口播；切到这段口播的后期示意画面，从无字幕变为显示对应字幕，不展示产品按钮。"
    },
    {
      "location": "shot:1/block:1",
      "text": "剪影练习版支持为视频添加字幕。"
    },
    {
      "location": "shot:2/visual",
      "text": "创作者回放刚才的口播，对照纸上抄写的字幕逐字核对，发现一处错字后用笔圈出；近景停留，让观众看清需要修改的位置。"
    },
    {
      "location": "shot:2/block:1",
      "text": "把想说的话，放进画面里。"
    },
    {
      "location": "shot:3/visual",
      "text": "便签上手改刚才圈出的错字；随后以字幕文字示意呈现修改前后的变化，最后回到口播画面展示修正后的字幕，不虚构产品界面或操作按钮。"
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
  "script_hash": "e267265948ca221d9e34fae0ac75529ff4f2b2241ede5c8fbc65fb8db2a91d6b",
  "request_hash": "7fb52283cc4eb7795933e6f2730cfb020711e034af85be6312f908b57de4f30b",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "审核并修改所附字幕介绍旧稿",
      "verdict": "met",
      "evidence": "第2镜由自动识别示意改为人工回放、核对和圈出错字；editor_notes说明了实际删改内容。"
    },
    {
      "field": "topic",
      "requirement": "客户没有提供自动识别和准确率数据。",
      "verdict": "met",
      "evidence": "当前公开文案及画面均未宣称自动识别或99%准确率；第2镜明确由创作者人工核对字幕。"
    },
    {
      "field": "topic",
      "requirement": "保留可确认的产品功能",
      "verdict": "met",
      "evidence": "第1镜保留“剪影练习版支持为视频添加字幕。”，对应P01.F1；第3镜保留“字幕文字可以手动编辑。”，对应P01.F2。"
    },
    {
      "field": "topic",
      "requirement": "明确处理无法确认的说法。",
      "verdict": "met",
      "evidence": "旧稿“自动识别人声，字幕准确率达到99%。”及自动识别示意均已删除。editor_notes准确说明资料缺口和删除范围，公开内容未混入审稿说明。"
    },
    {
      "field": "audience",
      "requirement": "新手内容创作者",
      "verdict": "met",
      "evidence": "第1至3镜通过添加字幕、人工核对、修正错字的具体示意解释用途，文案简短且无专业术语门槛。"
    },
    {
      "field": "platform",
      "requirement": "小红书",
      "verdict": "met",
      "evidence": "采用中文短标题、三镜声画同步和字幕修改示意；宿主估算总长24秒，内容集中，适合短视频观看。"
    },
    {
      "field": "style",
      "requirement": "客观",
      "verdict": "met",
      "evidence": "两项功能文案均由提供的原文支持，已去除无依据的自动识别及准确率宣称，没有新增效果保证。"
    },
    {
      "field": "style",
      "requirement": "实用",
      "verdict": "met",
      "evidence": "第2镜展示逐字核对并圈出错字，第3镜展示修改前后和修正后的字幕，形成具体可理解的字幕检查过程。"
    }
  ],
  "summary": "当前稿满足需求：保留两项有资料支持的字幕功能，删除并在审稿备注中说明无法确认的自动识别及准确率说法。公开表达均可放行，预计24秒，节奏合理。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "口播字幕小帮手",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于主题性标题，没有具体性能、自动化或效果承诺。"
    },
    {
      "location": "shot:1/visual",
      "text": "桌上的采访话筒旁，创作者录下一句口播；切到这段口播的后期示意画面，从无字幕变为显示对应字幕，不展示产品按钮。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "无字幕到有字幕的后期示意仅展示为视频添加字幕，符合P01.F1；未声称自动识别或虚构操作界面。"
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
      "evidence": "与P01.F1原文一致，引用保留原块标注的来源和事实ID。"
    },
    {
      "location": "shot:2/visual",
      "text": "创作者回放刚才的口播，对照纸上抄写的字幕逐字核对，发现一处错字后用笔圈出；近景停留，让观众看清需要修改的位置。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "展示创作者人工核对和纸上标记的动作，没有声称产品自动查错，也未虚构产品按钮或操作步骤。"
    },
    {
      "location": "shot:2/block:1",
      "text": "把想说的话，放进画面里。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于字幕创作的行动邀请，没有新增可验证的产品能力或效果承诺。"
    },
    {
      "location": "shot:3/visual",
      "text": "便签上手改刚才圈出的错字；随后以字幕文字示意呈现修改前后的变化，最后回到口播画面展示修正后的字幕，不虚构产品界面或操作按钮。",
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
      "evidence": "修改前后示意由P01.F2的手动编辑能力支持，视频中的字幕呈现由P01.F1支持；未增加自动纠错或未经证实的操作流程。"
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
      "evidence": "与P01.F2原文一致，引用保留原块标注的来源和事实ID。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "宿主估算三镜各8秒，总长24秒，通过28秒上限。各镜同beat的both声画同步，文案分别占4、3、3秒；剩余停留分别有录制及字幕对比、逐字核对及圈错近景、手改及前后对比支撑，没有明显空镜或重复事实凑时长。"
  },
  "expression_review_passed": true
}
```

## 执行路径

check_rules → search_materials → invalid_model_action → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
