# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成三镜字幕功能脚本，预计17.3秒，介绍添加字幕和手动编辑。未采用缺少统计材料与授权的“播放量提高30%”口头反馈，处理原因已记入编辑备注。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 店铺口播视频，字幕怎么配

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 连读旁白

这条店铺口播，我想把商品名称和介绍配上字幕。

用剪影练习版，可以给视频添加字幕。

字幕文字也能手动编辑。我再对照口播核对一遍，把内容写准确。

### 分镜 1

镜头目的：交代店铺口播配字幕的具体场景

画面：店铺运营回看一段商品介绍视频，暂停在介绍商品名称的位置，旁边放着商品信息卡。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–5.5 秒**

旁白＋同步字幕：这条店铺口播，我想把商品名称和介绍配上字幕。

预计镜头时长：5.5 秒

### 分镜 2

镜头目的：展示为视频添加字幕的能力

画面：展示同一段商品介绍视频添加字幕后的画面，字幕对应正在介绍的商品。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–4.3 秒**

旁白＋同步字幕：用剪影练习版，可以给视频添加字幕。

依据：P01/P01.F1

预计镜头时长：4.3 秒

### 分镜 3

镜头目的：展示手动编辑字幕并完成核对

画面：运营对照商品信息卡手动修改字幕中的商品名称，随后回放修改后的片段，核对字幕与口播。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–3.0 秒**

旁白＋同步字幕：字幕文字也能手动编辑。

依据：P01/P01.F2

**第 2 拍 · 镜内 3.0–7.5 秒**

旁白＋同步字幕：我再对照口播核对一遍，把内容写准确。

预计镜头时长：7.5 秒

## 审稿备注（不进入视频，不计入时长）

供创作者核对修改与资料缺口，不是经过事实认证的产品介绍。

未采用客户口头反馈中的播放量提高30%：目前缺少统计材料及授权，不作为已验证效果或公开客户案例。

预计总时长：17.3 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "836ba54f2ac83e40ec28f2f4155f21b1cb8e98a8310a138c093a17f391aae768",
  "passed": true,
  "issues": [],
  "citations": [
    {
      "location": "shot:2/block:1",
      "source_id": "P01",
      "fact_id": "P01.F1",
      "quote": "剪影练习版支持为视频添加字幕。",
      "version": "2026-11-01",
      "text": "用剪影练习版，可以给视频添加字幕。",
      "requires_semantic_review": true
    },
    {
      "location": "shot:3/block:1",
      "source_id": "P01",
      "fact_id": "P01.F2",
      "quote": "字幕文字可以手动编辑。",
      "version": "2026-11-01",
      "text": "字幕文字也能手动编辑。",
      "requires_semantic_review": true
    }
  ],
  "rules_version": "2026-11-03-v1",
  "requires_expression_review": true,
  "expression_slots": [
    {
      "location": "title",
      "text": "店铺口播视频，字幕怎么配"
    },
    {
      "location": "shot:1/visual",
      "text": "店铺运营回看一段商品介绍视频，暂停在介绍商品名称的位置，旁边放着商品信息卡。"
    },
    {
      "location": "shot:1/block:1",
      "text": "这条店铺口播，我想把商品名称和介绍配上字幕。"
    },
    {
      "location": "shot:2/visual",
      "text": "展示同一段商品介绍视频添加字幕后的画面，字幕对应正在介绍的商品。"
    },
    {
      "location": "shot:2/block:1",
      "text": "用剪影练习版，可以给视频添加字幕。"
    },
    {
      "location": "shot:3/visual",
      "text": "运营对照商品信息卡手动修改字幕中的商品名称，随后回放修改后的片段，核对字幕与口播。"
    },
    {
      "location": "shot:3/block:1",
      "text": "字幕文字也能手动编辑。"
    },
    {
      "location": "shot:3/block:2",
      "text": "我再对照口播核对一遍，把内容写准确。"
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
  "script_hash": "836ba54f2ac83e40ec28f2f4155f21b1cb8e98a8310a138c093a17f391aae768",
  "request_hash": "93972873cc931936e79f564ca370d65259052b284f9983eeaaba7d87a79a6a9d",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "请写一条介绍字幕功能的脚本",
      "verdict": "met",
      "evidence": "第2镜介绍添加字幕，第3镜介绍手动编辑字幕文字，均有资料支持。"
    },
    {
      "field": "topic",
      "requirement": "处理这个说法",
      "verdict": "met",
      "evidence": "公开文案未采用播放量提高30%的说法，editor_notes明确说明缺少统计材料及授权，因此不作为效果或公开客户案例。"
    },
    {
      "field": "topic",
      "requirement": "不要把口头反馈包装成已验证效果",
      "verdict": "met",
      "evidence": "旁白、字幕和画面均未声称播放量提升，也未展示客户背书或效果数据。"
    },
    {
      "field": "audience",
      "requirement": "店铺内容运营",
      "verdict": "met",
      "evidence": "第1镜以商品介绍口播切入，第3镜对照商品信息卡核对名称，具体体现店铺内容运营场景。"
    },
    {
      "field": "platform",
      "requirement": "抖音",
      "verdict": "met",
      "evidence": "三镜按场景、添加字幕、编辑核对展开，声画同步且预计17.3秒，适合短视频观看。"
    },
    {
      "field": "style",
      "requirement": "可信，少口号",
      "verdict": "met",
      "evidence": "连续旁白从配字幕需求自然衔接到添加、编辑与人工核对，仅陈述有依据的能力，无夸张效果或口号。"
    }
  ],
  "summary": "当前稿满足需求：字幕功能介绍清楚，店铺场景具体，未将未经证实的口头反馈包装成效果承诺。公开表达有依据，预计17.3秒，节奏合理。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "店铺口播视频，字幕怎么配",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "标题点明场景和介绍主题，不包含效果或额外能力承诺。"
    },
    {
      "location": "shot:1/visual",
      "text": "店铺运营回看一段商品介绍视频，暂停在介绍商品名称的位置，旁边放着商品信息卡。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于店铺运营的拍摄场景安排，未指定产品界面或操作流程。"
    },
    {
      "location": "shot:1/block:1",
      "text": "这条店铺口播，我想把商品名称和介绍配上字幕。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "表达使用者的配字幕意图，没有宣称自动识别或效果提升。"
    },
    {
      "location": "shot:2/visual",
      "text": "展示同一段商品介绍视频添加字幕后的画面，字幕对应正在介绍的商品。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "添加字幕后的示意画面由添加字幕能力支持，未声称自动生成或匹配。"
    },
    {
      "location": "shot:2/block:1",
      "text": "用剪影练习版，可以给视频添加字幕。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "与原文“剪影练习版支持为视频添加字幕”含义一致。"
    },
    {
      "location": "shot:3/visual",
      "text": "运营对照商品信息卡手动修改字幕中的商品名称，随后回放修改后的片段，核对字幕与口播。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "手动修改字幕由资料支持，随后回放核对属于人工观察安排，未虚构按钮或自动流程。"
    },
    {
      "location": "shot:3/block:1",
      "text": "字幕文字也能手动编辑。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "与原文“字幕文字可以手动编辑”含义一致。"
    },
    {
      "location": "shot:3/block:2",
      "text": "我再对照口播核对一遍，把内容写准确。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "描述使用者主动核对的动作与目的，没有承诺产品自动纠错或保证准确率。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "第1镜5.5秒交代场景，第2镜4.3秒展示添加结果，第3镜按3秒、4.5秒两个节拍展示编辑与回放核对；声画并行且动作明确，无重复事实或空镜凑时长。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
