# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成《把读书会的话留下》三分镜脚本，预计24秒。以签到桌、书页和分享者背影串联字幕添加与手动改字，全部检查通过。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 把读书会的话留下

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

镜头目的：用签到场景交代读书会记录的用途。

画面：固定拍摄签到桌近景：志愿者摆好签到本，参与者写下姓名、合上笔帽，随后拿起书走向座位。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–4.3 秒**

旁白＋同步字幕：签到之后，把今天读书会的话也留下。

镜头末尾保持画面：4.3–7.0 秒（保留最后一拍屏幕文字）

预计镜头时长：7.0 秒

### 分镜 2

镜头目的：在书页画面上展示添加字幕，让分享的话随画面呈现。

画面：拍摄手指停在书页一行文字上的近景；切到该片段的编辑画面，展示添加字幕后的预览，字幕为“这句话，让我想起了家”。不特写未经确认的按钮。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–3.8 秒**

旁白＋同步字幕：用剪影练习版，为视频添加字幕。

依据：P01/P01.F1

镜头末尾保持画面：3.8–8.0 秒（保留最后一拍屏幕文字）

预计镜头时长：8.0 秒

### 分镜 3

镜头目的：展示手动修改字幕文字，落回分享者背影。

画面：以分享者背影片段为预览，展示手动把字幕中的“想起了加”改为“想起了家”；随后全屏播放修改后的背影片段，字幕停留供观众核对。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–3.0 秒**

旁白＋同步字幕：字幕文字可以手动编辑。

依据：P01/P01.F2

**第 2 拍 · 镜内 3.0–6.5 秒**

旁白：发现错字，就把这句话改准确。

镜头末尾保持画面：6.5–9.0 秒（保留最后一拍屏幕文字）

预计镜头时长：9.0 秒

时长要求：21.6–24 秒（接近目标）。

预计总时长：24.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "c09a3c72088099df6b4d32da3f5b492ad9d5e33964200cd9edbc9598179f45a4",
  "passed": true,
  "issues": [],
  "citations": [
    {
      "location": "shot:2/block:1",
      "source_id": "P01",
      "fact_id": "P01.F1",
      "quote": "剪影练习版支持为视频添加字幕。",
      "version": "2026-11-01",
      "text": "用剪影练习版，为视频添加字幕。",
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
      "text": "把读书会的话留下"
    },
    {
      "location": "shot:1/visual",
      "text": "固定拍摄签到桌近景：志愿者摆好签到本，参与者写下姓名、合上笔帽，随后拿起书走向座位。"
    },
    {
      "location": "shot:1/block:1",
      "text": "签到之后，把今天读书会的话也留下。"
    },
    {
      "location": "shot:2/visual",
      "text": "拍摄手指停在书页一行文字上的近景；切到该片段的编辑画面，展示添加字幕后的预览，字幕为“这句话，让我想起了家”。不特写未经确认的按钮。"
    },
    {
      "location": "shot:2/block:1",
      "text": "用剪影练习版，为视频添加字幕。"
    },
    {
      "location": "shot:3/visual",
      "text": "以分享者背影片段为预览，展示手动把字幕中的“想起了加”改为“想起了家”；随后全屏播放修改后的背影片段，字幕停留供观众核对。"
    },
    {
      "location": "shot:3/block:1",
      "text": "字幕文字可以手动编辑。"
    },
    {
      "location": "shot:3/block:2",
      "text": "发现错字，就把这句话改准确。"
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
  "script_hash": "c09a3c72088099df6b4d32da3f5b492ad9d5e33964200cd9edbc9598179f45a4",
  "request_hash": "19501a3419a2e7a54b42e8fa42d7c37ee31f2ee574c4a5de11438014ffcdbf26",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "字幕添加",
      "verdict": "met",
      "evidence": "第2镜展示添加字幕后的预览，并明确说明“为视频添加字幕”。"
    },
    {
      "field": "topic",
      "requirement": "手动编辑字幕文字",
      "verdict": "met",
      "evidence": "第3镜展示手动将“想起了加”改为“想起了家”，配有手动编辑说明。"
    },
    {
      "field": "topic",
      "requirement": "画面围绕签到桌、书页、分享者背影",
      "verdict": "met",
      "evidence": "第1镜拍签到桌，第2镜拍书页，第3镜以分享者背影片段展示字幕修改。"
    },
    {
      "field": "topic",
      "requirement": "恰好三个分镜",
      "verdict": "met",
      "evidence": "当前稿件包含且仅包含3个分镜。"
    },
    {
      "field": "topic",
      "requirement": "标题用“把读书会的话留下”",
      "verdict": "met",
      "evidence": "标题为“把读书会的话留下”，与要求一致。"
    },
    {
      "field": "audience",
      "requirement": "图书馆活动志愿者",
      "verdict": "met",
      "evidence": "签到组织、读书会记录和字幕纠错均贴合图书馆活动志愿者的工作场景。"
    },
    {
      "field": "platform",
      "requirement": "视频号",
      "verdict": "met",
      "evidence": "24秒三镜结构结合简短字幕与具体活动画面，适合视频号观看。"
    },
    {
      "field": "style",
      "requirement": "温和",
      "verdict": "met",
      "evidence": "“把今天读书会的话也留下”语气柔和，签到、翻阅书页和分享背影营造平静氛围。"
    },
    {
      "field": "style",
      "requirement": "清楚",
      "verdict": "met",
      "evidence": "第2镜介绍添加字幕，第3镜用具体错字修改示例说明手动编辑，信息明确。"
    }
  ],
  "summary": "稿件落实了两项功能、三个指定场景、分镜数量和标题要求，公开表达均有支持或属于普通场景表达。预计24秒，画面动作及字幕核对内容能够支撑停留，节奏合理。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "把读书会的话留下",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于读书会记录主题表达，不含具体产品能力承诺。"
    },
    {
      "location": "shot:1/visual",
      "text": "固定拍摄签到桌近景：志愿者摆好签到本，参与者写下姓名、合上笔帽，随后拿起书走向座位。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅安排签到场景和人物动作，不涉及产品事实或真实客户背书。"
    },
    {
      "location": "shot:1/block:1",
      "text": "签到之后，把今天读书会的话也留下。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于记录活动的邀请与衔接语，没有新增产品承诺。"
    },
    {
      "location": "shot:2/visual",
      "text": "拍摄手指停在书页一行文字上的近景；切到该片段的编辑画面，展示添加字幕后的预览，字幕为“这句话，让我想起了家”。不特写未经确认的按钮。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "字幕示意由添加字幕能力支持，未指定未经证实的按钮、布局或自动流程。"
    },
    {
      "location": "shot:2/block:1",
      "text": "用剪影练习版，为视频添加字幕。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "准确改写原文“剪影练习版支持为视频添加字幕”，未扩大功能范围。"
    },
    {
      "location": "shot:3/visual",
      "text": "以分享者背影片段为预览，展示手动把字幕中的“想起了加”改为“想起了家”；随后全屏播放修改后的背影片段，字幕停留供观众核对。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "手动替换错字属于字幕文字编辑，全屏播放是成片展示安排，未声称自动纠错。"
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
      "evidence": "文案与所标注事实原文一致。"
    },
    {
      "location": "shot:3/block:2",
      "text": "发现错字，就把这句话改准确。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "结合前一节拍及手动改字画面，表达用户手动纠正字幕，未承诺自动识别或纠错。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "第1镜7秒由签到连续动作支撑；第2镜8秒容纳书页切换及字幕观察；第3镜9秒含依次进行的3秒与3.5秒文案节拍及2.5秒核对停留，未见重复空镜凑时长。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
