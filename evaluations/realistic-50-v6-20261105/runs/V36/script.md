# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成3镜字幕功能脚本，预计14.3秒，符合25秒上限。展示添加字幕、手动编辑及商品名称核对；未采用“播放量提高30%”的口头反馈，并在备注中说明缺少统计材料与授权。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 店铺口播：添加字幕，再核对文字

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

镜头目的：建立店铺口播加字幕的具体场景

画面：店员在货架前录制商品介绍；切到同一段视频的预览画面，准备添加字幕。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–3.5 秒**

旁白＋同步字幕：店铺口播拍好了，接着加字幕。

预计镜头时长：3.5 秒

### 分镜 2

镜头目的：展示为视频添加字幕的能力

画面：展示同一段商品口播添加字幕前后的画面，字幕内容对应店员说出的商品介绍。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–4.0 秒**

旁白＋同步字幕：剪影练习版支持为视频添加字幕。

依据：P01/P01.F1

预计镜头时长：4.0 秒

### 分镜 3

镜头目的：展示手动编辑字幕并核对商品名称的动作

画面：录屏展示手动修改字幕中的商品名称，再播放修改后的片段，核对字幕与口播是否一致；不指定未经资料确认的按钮名称。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–3.0 秒**

旁白＋同步字幕：字幕文字可以手动编辑。

依据：P01/P01.F2

**第 2 拍 · 镜内 3.0–6.8 秒**

旁白＋同步字幕：发布前，把商品名称再核对一遍。

预计镜头时长：6.8 秒

## 审稿备注（不进入视频，不计入时长）

供创作者核对修改与资料缺口，不是经过事实认证的产品介绍。

未将客户口头反馈的播放量提高30%写入公开文案；该反馈缺少统计材料与授权，不能作为已验证效果或客户案例使用。

预计总时长：14.3 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "7cc42b86253d44a734d1329346a749d9ca984a138cc37f7266da04b1830b6f36",
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
      "text": "店铺口播：添加字幕，再核对文字"
    },
    {
      "location": "shot:1/visual",
      "text": "店员在货架前录制商品介绍；切到同一段视频的预览画面，准备添加字幕。"
    },
    {
      "location": "shot:1/block:1",
      "text": "店铺口播拍好了，接着加字幕。"
    },
    {
      "location": "shot:2/visual",
      "text": "展示同一段商品口播添加字幕前后的画面，字幕内容对应店员说出的商品介绍。"
    },
    {
      "location": "shot:2/block:1",
      "text": "剪影练习版支持为视频添加字幕。"
    },
    {
      "location": "shot:3/visual",
      "text": "录屏展示手动修改字幕中的商品名称，再播放修改后的片段，核对字幕与口播是否一致；不指定未经资料确认的按钮名称。"
    },
    {
      "location": "shot:3/block:1",
      "text": "字幕文字可以手动编辑。"
    },
    {
      "location": "shot:3/block:2",
      "text": "发布前，把商品名称再核对一遍。"
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
  "script_hash": "7cc42b86253d44a734d1329346a749d9ca984a138cc37f7266da04b1830b6f36",
  "request_hash": "93972873cc931936e79f564ca370d65259052b284f9983eeaaba7d87a79a6a9d",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "请写一条介绍字幕功能的脚本",
      "verdict": "met",
      "evidence": "第2镜介绍添加字幕，第3镜展示手动编辑字幕，两项能力均有资料支持。"
    },
    {
      "field": "topic",
      "requirement": "处理这个说法",
      "verdict": "met",
      "evidence": "公开文案未采用播放量提高30%的反馈，editor_notes明确说明缺少统计材料与授权。"
    },
    {
      "field": "topic",
      "requirement": "不要把口头反馈包装成已验证效果",
      "verdict": "met",
      "evidence": "标题、画面及文案均未宣称播放量提升，也未将口头反馈作为客户案例。"
    },
    {
      "field": "audience",
      "requirement": "店铺内容运营",
      "verdict": "met",
      "evidence": "第1镜呈现货架前商品口播，第3镜核对商品名称，符合店铺内容制作场景。"
    },
    {
      "field": "platform",
      "requirement": "抖音",
      "verdict": "met",
      "evidence": "三镜以商品口播、字幕对比和文字修改直观演示功能，适合短视频观看。"
    },
    {
      "field": "style",
      "requirement": "可信",
      "verdict": "met",
      "evidence": "功能介绍限于资料支持的添加字幕和手动编辑，未公开未经验证的效果反馈。"
    },
    {
      "field": "style",
      "requirement": "少口号",
      "verdict": "met",
      "evidence": "文案围绕加字幕和核对商品名称展开，没有夸大口号。"
    }
  ],
  "summary": "稿件落实了字幕功能介绍，并通过删除公开效果说法、在审稿备注中说明资料缺口，妥善处理了口头反馈。公开表达有依据，场景与节奏适配，预计14.3秒符合25秒上限。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "店铺口播：添加字幕，再核对文字",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "添加字幕由P01.F1支持，核对文字是人工操作建议。"
    },
    {
      "location": "shot:1/visual",
      "text": "店员在货架前录制商品介绍；切到同一段视频的预览画面，准备添加字幕。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "店铺背景属于拍摄安排，准备添加字幕对应已证实能力，未指定产品界面或自动流程。"
    },
    {
      "location": "shot:1/block:1",
      "text": "店铺口播拍好了，接着加字幕。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "加字幕由P01.F1支持，未增加自动识别等能力承诺。"
    },
    {
      "location": "shot:2/visual",
      "text": "展示同一段商品口播添加字幕前后的画面，字幕内容对应店员说出的商品介绍。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "画面示意为视频添加对应内容的字幕，未声称自动生成或识别准确率。"
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
      "evidence": "与所标注P01.F1原文一致。"
    },
    {
      "location": "shot:3/visual",
      "text": "录屏展示手动修改字幕中的商品名称，再播放修改后的片段，核对字幕与口播是否一致；不指定未经资料确认的按钮名称。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "修改商品名称属于手动编辑字幕，回放核对是演示安排，没有虚构具体按钮或自动校对能力。"
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
      "evidence": "与所标注P01.F2原文一致。"
    },
    {
      "location": "shot:3/block:2",
      "text": "发布前，把商品名称再核对一遍。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于人工核对建议，没有宣称产品自动检查或保证正确。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "三镜预计3.5、4.0、6.8秒，分别承载场景切换、字幕前后对比、修改与回放核对；第3镜两拍依次展开且满足6秒最低停留，没有空镜凑时长。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
