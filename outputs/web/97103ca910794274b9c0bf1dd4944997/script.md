# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成《课程记录中的字幕》四镜头稿，仅介绍字幕添加，包含擦净的黑板、课程讲义和空座位，表达平实克制，无问句、感叹号、下载引导或效果保证。首稿通过检查，无需删改。估算19.6秒，符合18至20秒目标范围，实际时长以成片为准。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 课程记录中的字幕

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

画面：课堂全景：擦净的黑板、桌上的课程讲义和空座位同时入画，镜头缓慢推近。文字块为旁白。

旁白/字幕：一节课结束，黑板已经擦净，讲义还摊在桌上。

来源：

预计镜头时长：5.0 秒

### 分镜 2

画面：课程讲义近景，背景保留擦净的黑板和空座位。文字块为产品事实旁白，同步作为字幕叠加在画面下方，不展示软件界面。

旁白/字幕：剪影练习版支持为视频添加字幕。

来源：P01/P01.F1

预计镜头时长：4.0 秒

### 分镜 3

画面：手翻开课程讲义，镜头沿纸面缓慢移动，讲义上的字不作为额外文案。文字块为场景旁白，同步作为字幕叠加，展示添加字幕后的画面。

旁白/字幕：翻开课程讲义，镜头沿着本页的笔记缓缓移动。

来源：

预计镜头时长：5.3 秒

### 分镜 4

画面：镜头从课程讲义缓缓移向空座位，擦净的黑板留在背景。文字块为旁白，同步显示为字幕，随旁白结束收尾。

旁白/字幕：留出阅读字幕的时间，再结束这一段课堂记录。

来源：

预计镜头时长：5.3 秒

时长要求：18.0–20 秒（接近目标）。

预计总时长：19.6 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "a75d3852de1787b249cdaf28aecbad8f53b3cb9dcce0cc87875a4a1e6c2fcf9f",
  "passed": true,
  "issues": [],
  "citations": [
    {
      "location": "shot:2/block:1",
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
      "text": "课程记录中的字幕"
    },
    {
      "location": "shot:1/visual",
      "text": "课堂全景：擦净的黑板、桌上的课程讲义和空座位同时入画，镜头缓慢推近。文字块为旁白。"
    },
    {
      "location": "shot:1/block:1",
      "text": "一节课结束，黑板已经擦净，讲义还摊在桌上。"
    },
    {
      "location": "shot:2/visual",
      "text": "课程讲义近景，背景保留擦净的黑板和空座位。文字块为产品事实旁白，同步作为字幕叠加在画面下方，不展示软件界面。"
    },
    {
      "location": "shot:3/visual",
      "text": "手翻开课程讲义，镜头沿纸面缓慢移动，讲义上的字不作为额外文案。文字块为场景旁白，同步作为字幕叠加，展示添加字幕后的画面。"
    },
    {
      "location": "shot:3/block:1",
      "text": "翻开课程讲义，镜头沿着本页的笔记缓缓移动。"
    },
    {
      "location": "shot:4/visual",
      "text": "镜头从课程讲义缓缓移向空座位，擦净的黑板留在背景。文字块为旁白，同步显示为字幕，随旁白结束收尾。"
    },
    {
      "location": "shot:4/block:1",
      "text": "留出阅读字幕的时间，再结束这一段课堂记录。"
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
  "scope": "exact_quote_and_brand_checks_only; expression semantics require independent model review"
}
```

## 需求覆盖核对

以下为模型评估，可能漏判或误判，仍需人工确认。

```json
{
  "ok": true,
  "script_hash": "a75d3852de1787b249cdaf28aecbad8f53b3cb9dcce0cc87875a4a1e6c2fcf9f",
  "request_hash": "fe513b9257dbed69caead2482b20e7d77c4402d6ab34c67d59e7319e8c7156e7",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "介绍字幕添加",
      "verdict": "met",
      "evidence": "镜头2明确介绍“剪影练习版支持为视频添加字幕。”，镜头2至4安排字幕叠加展示。"
    },
    {
      "field": "topic",
      "requirement": "擦净的黑板",
      "verdict": "met",
      "evidence": "镜头1写明“擦净的黑板”，镜头2和镜头4也明确保留该背景。"
    },
    {
      "field": "topic",
      "requirement": "课程讲义",
      "verdict": "met",
      "evidence": "镜头1包含“桌上的课程讲义”，镜头2为讲义近景，镜头3安排翻开讲义。"
    },
    {
      "field": "topic",
      "requirement": "空座位",
      "verdict": "met",
      "evidence": "镜头1让空座位同时入画，镜头2保留空座位背景，镜头4移向空座位。"
    },
    {
      "field": "topic",
      "requirement": "不要问句",
      "verdict": "met",
      "evidence": "标题、全部画面说明和旁白均无问句；结尾为“留出阅读字幕的时间，再结束这一段课堂记录。”"
    },
    {
      "field": "topic",
      "requirement": "感叹号",
      "verdict": "met",
      "evidence": "全稿标题、画面说明和旁白均未出现感叹号，满足原句中的禁用要求。"
    },
    {
      "field": "topic",
      "requirement": "下载引导",
      "verdict": "met",
      "evidence": "全稿没有下载、安装或获取产品的引导，镜头4以课堂记录收尾。"
    },
    {
      "field": "topic",
      "requirement": "“轻松搞定”式保证",
      "verdict": "met",
      "evidence": "产品旁白仅陈述“支持为视频添加字幕”，没有省时、省力、必然成功等效果保证。"
    },
    {
      "field": "topic",
      "requirement": "只讲这个功能。",
      "verdict": "met",
      "evidence": "逐镜核对后，产品功能仅涉及添加字幕。未介绍资料中的手动编辑字幕或裁剪视频；翻讲义、移动镜头及结束记录均为拍摄安排，没有扩展产品功能范围。"
    },
    {
      "field": "audience",
      "requirement": "线上课程剪辑助教",
      "verdict": "met",
      "evidence": "课程讲义、黑板和课堂记录构成明确课程场景，镜头2至4展示课程画面添加字幕后的呈现，与助教处理课程视频的用途相符。"
    },
    {
      "field": "platform",
      "requirement": "B站",
      "verdict": "met",
      "evidence": "以中文旁白、连续课堂画面和字幕示意组成短视频，内容可独立理解，适合B站视频呈现；无需直接写出平台名称。"
    },
    {
      "field": "style",
      "requirement": "平实，克制",
      "verdict": "met",
      "evidence": "标题“课程记录中的字幕”直接点题；旁白采用场景描述和单句功能陈述，缓慢推近与移镜配合，无夸张口号或强推销表达。"
    }
  ],
  "summary": "原始需求均已落实：仅介绍添加字幕，指定课堂背景齐全，表达平实克制，无禁用句式、下载引导或效果保证。未发现无依据的产品声明或明显凑时长安排。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "课程记录中的字幕",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "标题说明内容主题，没有宣称产品能力、性能或效果。"
    },
    {
      "location": "shot:1/visual",
      "text": "课堂全景：擦净的黑板、桌上的课程讲义和空座位同时入画，镜头缓慢推近。文字块为旁白。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅包含课堂布景、镜头运动及旁白安排，不含产品承诺。"
    },
    {
      "location": "shot:1/block:1",
      "text": "一节课结束，黑板已经擦净，讲义还摊在桌上。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于课后场景描述，没有产品事实或真实用户背书。"
    },
    {
      "location": "shot:2/visual",
      "text": "课程讲义近景，背景保留擦净的黑板和空座位。文字块为产品事实旁白，同步作为字幕叠加在画面下方，不展示软件界面。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "画面中的产品能力仅为添加字幕，由P01.F1“剪影练习版支持为视频添加字幕。”支持。字幕位置和与旁白同步呈现属于制作安排，没有声称自动生成或自动同步，也未虚构软件界面。"
    },
    {
      "location": "shot:3/visual",
      "text": "手翻开课程讲义，镜头沿纸面缓慢移动，讲义上的字不作为额外文案。文字块为场景旁白，同步作为字幕叠加，展示添加字幕后的画面。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "“展示添加字幕后的画面”直接示意P01.F1支持的字幕添加能力；翻页和移镜是拍摄动作，未宣称识别讲义文字或其他额外功能。"
    },
    {
      "location": "shot:3/block:1",
      "text": "翻开课程讲义，镜头沿着本页的笔记缓缓移动。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅描述翻页及镜头移动，不含产品能力或效果声明。"
    },
    {
      "location": "shot:4/visual",
      "text": "镜头从课程讲义缓缓移向空座位，擦净的黑板留在背景。文字块为旁白，同步显示为字幕，随旁白结束收尾。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "显示字幕的能力由P01.F1支持；镜头移动、旁白同步呈现和结束收尾均为制作安排，未声称产品自动完成这些操作。"
    },
    {
      "location": "shot:4/block:1",
      "text": "留出阅读字幕的时间，再结束这一段课堂记录。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于阅读节奏和收尾安排，不承诺产品自动控制时长或提升阅读效果。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "四个镜头的hold_seconds均为0，未设置额外停留。镜头1的场景旁白配合全景推近；镜头2用一句功能旁白配合字幕示意；镜头3的旁白配合翻页和沿纸面移动；镜头4配合移向空座位并随旁白收尾。各镜头均有对应的观察或动作内容，字幕可随旁白阅读，未见重复口播同一产品事实或以空镜额外凑时长。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
