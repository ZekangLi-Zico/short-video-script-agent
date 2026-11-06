# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成3镜头脚本，预计22.9秒，介绍添加字幕与手动改字。画面仅拍笼牌、牵引绳和志愿者手部，不含真实姓名或联系方式；全部检查已通过。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 给领养日花絮加字幕、改文字

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 连读旁白

领养日结束，我想给志愿者整理牵引绳的小片段，配上简单的文字。

用剪影练习版，可以给这些花絮添加字幕。

字幕文字也能手动修改，比如改成“谢谢今天来帮忙的伙伴”。用一句简单的感谢，留下今天的记录。

### 分镜 1

镜头目的：交代领养日花絮的记录场景

画面：近拍志愿者手部整理牵引绳，旁边放仅写“领养日”的道具笼牌；画面不出现其他主体或个人信息。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–7.3 秒**

旁白：领养日结束，我想给志愿者整理牵引绳的小片段，配上简单的文字。

预计镜头时长：7.3 秒

### 分镜 2

镜头目的：介绍为花絮添加字幕的具体用法

画面：志愿者双手将牵引绳整齐放在笼牌旁；后期叠加示例字幕“准备迎接新伙伴”。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–4.8 秒**

旁白：用剪影练习版，可以给这些花絮添加字幕。

依据：P01/P01.F1

屏幕文字：准备迎接新伙伴

预计镜头时长：4.8 秒

### 分镜 3

镜头目的：说明字幕文字可手动修改并收束分享

画面：继续近拍手部整理牵引绳；后期示例字幕由“准备迎接新伙伴”替换为“谢谢今天来帮忙的伙伴”，不展示软件界面。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–6.5 秒**

旁白：字幕文字也能手动修改，比如改成“谢谢今天来帮忙的伙伴”。

依据：P01/P01.F2

屏幕文字：谢谢今天来帮忙的伙伴

**第 2 拍 · 镜内 6.5–10.8 秒**

旁白：用一句简单的感谢，留下今天的记录。

预计镜头时长：10.8 秒

## 审稿备注（不进入视频，不计入时长）

供创作者核对修改与资料缺口，不是经过事实认证的产品介绍。

已修正开场语义搭配，并补明确说话人；其余文案和镜头保持不变。

## 实际修订

位置按镜头索引比较；日志关联的是实际反馈，不证明模型因果推理。

- 修改：editor_notes, shot:1/block:1；保留原镜头 2 个、原文案块 5 个。
- 修订前失败检查：requirements_check

预计总时长：22.9 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "968acf189ce0250a70649437aadef924b16056fb7091d38759b04ed27777908d",
  "passed": true,
  "issues": [],
  "citations": [
    {
      "location": "shot:2/block:1",
      "source_id": "P01",
      "fact_id": "P01.F1",
      "quote": "剪影练习版支持为视频添加字幕。",
      "version": "2026-11-01",
      "text": "用剪影练习版，可以给这些花絮添加字幕。",
      "requires_semantic_review": true
    },
    {
      "location": "shot:3/block:1",
      "source_id": "P01",
      "fact_id": "P01.F2",
      "quote": "字幕文字可以手动编辑。",
      "version": "2026-11-01",
      "text": "字幕文字也能手动修改，比如改成“谢谢今天来帮忙的伙伴”。",
      "requires_semantic_review": true
    }
  ],
  "rules_version": "2026-11-03-v1",
  "requires_expression_review": true,
  "expression_slots": [
    {
      "location": "title",
      "text": "给领养日花絮加字幕、改文字"
    },
    {
      "location": "shot:1/visual",
      "text": "近拍志愿者手部整理牵引绳，旁边放仅写“领养日”的道具笼牌；画面不出现其他主体或个人信息。"
    },
    {
      "location": "shot:1/block:1",
      "text": "领养日结束，我想给志愿者整理牵引绳的小片段，配上简单的文字。"
    },
    {
      "location": "shot:2/visual",
      "text": "志愿者双手将牵引绳整齐放在笼牌旁；后期叠加示例字幕“准备迎接新伙伴”。"
    },
    {
      "location": "shot:2/block:1",
      "text": "用剪影练习版，可以给这些花絮添加字幕。"
    },
    {
      "location": "shot:2/block:2",
      "text": "准备迎接新伙伴"
    },
    {
      "location": "shot:3/visual",
      "text": "继续近拍手部整理牵引绳；后期示例字幕由“准备迎接新伙伴”替换为“谢谢今天来帮忙的伙伴”，不展示软件界面。"
    },
    {
      "location": "shot:3/block:1",
      "text": "字幕文字也能手动修改，比如改成“谢谢今天来帮忙的伙伴”。"
    },
    {
      "location": "shot:3/block:2",
      "text": "谢谢今天来帮忙的伙伴"
    },
    {
      "location": "shot:3/block:3",
      "text": "用一句简单的感谢，留下今天的记录。"
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
  "script_hash": "968acf189ce0250a70649437aadef924b16056fb7091d38759b04ed27777908d",
  "request_hash": "5c0b0575b38040eae7c360d4797877a9d0ce4b18e4b26ee4c709496cad63c2dd",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "做一条工具介绍",
      "verdict": "met",
      "evidence": "第2镜点名“剪影练习版”，第2、3镜分别介绍添加字幕和手动修改文字。"
    },
    {
      "field": "topic",
      "requirement": "说明可为领养日花絮添加字幕",
      "verdict": "met",
      "evidence": "第1镜以领养日笼牌和整理牵引绳交代场景，第2镜明确说“可以给这些花絮添加字幕”。"
    },
    {
      "field": "topic",
      "requirement": "并手动修改文字",
      "verdict": "met",
      "evidence": "第3镜说明“字幕文字也能手动修改”，并安排示例字幕替换。"
    },
    {
      "field": "topic",
      "requirement": "画面只拍笼牌、牵引绳和志愿者手部",
      "verdict": "met",
      "evidence": "三镜拍摄主体均限于笼牌、牵引绳和手部，字幕为后期叠加，第3镜明确不展示软件界面。"
    },
    {
      "field": "topic",
      "requirement": "不使用真实姓名和联系方式",
      "verdict": "met",
      "evidence": "道具笼牌仅写“领养日”，全部公开文案及画面安排均无真实姓名或联系方式。"
    },
    {
      "field": "audience",
      "requirement": "动物救助志愿者",
      "verdict": "met",
      "evidence": "领养日、整理牵引绳及感谢帮忙伙伴的内容贴合志愿者记录活动的用途，旁白指代连贯。"
    },
    {
      "field": "platform",
      "requirement": "视频号",
      "verdict": "met",
      "evidence": "三镜围绕一个具体用途展开，旁白配简短字幕，预计22.9秒，适合短视频观看。"
    },
    {
      "field": "style",
      "requirement": "温暖但不煽情",
      "verdict": "met",
      "evidence": "“准备迎接新伙伴”和“谢谢今天来帮忙的伙伴”表达克制的关怀与感谢，连续旁白语义完整，无夸张煽情。"
    }
  ],
  "summary": "当前稿已落实领养日花絮加字幕、手动改字和拍摄隐私限制，表达温暖克制。产品声明有资料支持，预计22.9秒，镜头节奏合理。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "给领养日花絮加字幕、改文字",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        },
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "标题中的加字幕和改文字分别由添加字幕、手动编辑字幕的事实支持。"
    },
    {
      "location": "shot:1/visual",
      "text": "近拍志愿者手部整理牵引绳，旁边放仅写“领养日”的道具笼牌；画面不出现其他主体或个人信息。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅规定拍摄主体、道具及隐私边界，不含产品承诺。"
    },
    {
      "location": "shot:1/block:1",
      "text": "领养日结束，我想给志愿者整理牵引绳的小片段，配上简单的文字。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "表达记录者为活动片段配文字的意愿，未宣称产品能力。"
    },
    {
      "location": "shot:2/visual",
      "text": "志愿者双手将牵引绳整齐放在笼牌旁；后期叠加示例字幕“准备迎接新伙伴”。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于手部动作与后期字幕的拍摄安排，未虚构产品界面或操作流程。"
    },
    {
      "location": "shot:2/block:1",
      "text": "用剪影练习版，可以给这些花絮添加字幕。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "原文支持为视频添加字幕，应用于领养日花絮未增加能力承诺。"
    },
    {
      "location": "shot:2/block:2",
      "text": "准备迎接新伙伴",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "作为领养日示例字幕表达期待，不含可验证的产品声明。"
    },
    {
      "location": "shot:3/visual",
      "text": "继续近拍手部整理牵引绳；后期示例字幕由“准备迎接新伙伴”替换为“谢谢今天来帮忙的伙伴”，不展示软件界面。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "安排后期示例文字切换，不声称自动修改或展示未经证实的软件操作。"
    },
    {
      "location": "shot:3/block:1",
      "text": "字幕文字也能手动修改，比如改成“谢谢今天来帮忙的伙伴”。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "手动修改与原文“字幕文字可以手动编辑”一致，所举文字仅为编辑示例。"
    },
    {
      "location": "shot:3/block:2",
      "text": "谢谢今天来帮忙的伙伴",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "是场景中的感谢语，不构成产品效果或用户背书。"
    },
    {
      "location": "shot:3/block:3",
      "text": "用一句简单的感谢，留下今天的记录。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于活动记录的情绪收束，没有新增产品功能或效果承诺。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "第1镜7.3秒对应场景旁白和整理动作，第2镜4.8秒同步介绍功能与展示字幕，第3镜按6.5秒改字示例、4.3秒感谢收束依次展开；均有具体内容支撑，无额外空镜凑时长。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → check_requirements → write_script → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
