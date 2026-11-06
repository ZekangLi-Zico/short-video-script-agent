# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成3镜脚本，预计14秒。仅用键盘、便签和空白笔记本，以便签换字示意手动编辑字幕；无人物、人物照片或手机界面，陈述式开场，表达安静。全部检查已通过。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 不露脸的知识分享：手动改好字幕文字

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

镜头目的：以字幕文案引出不露脸知识分享的准备场景。

画面：俯拍键盘、摊开的空白笔记本和一张便签。便签写着“今天分享三个方法”。镜头缓慢靠近便签，全程无人或手部入画。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–4.0 秒**

旁白：知识分享，从一句清楚的字幕开始。

预计镜头时长：4.0 秒

### 分镜 2

镜头目的：说明字幕文字可手动编辑，以便签换字示意文案修订。

画面：保持同一构图，通过停机替换便签再切镜，将“三个方法”换为“两个方法”。便签底部印小字“文案修改示意”。笔记本内页保持空白，不展示软件操作。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–4.5 秒**

旁白：剪影练习版的字幕文字可以手动编辑。

依据：P01/P01.F2

镜头末尾保持画面：4.5–6.0 秒（保留最后一拍屏幕文字）

预计镜头时长：6.0 秒

### 分镜 3

镜头目的：引导创作者读一遍修改后的字幕，确认表达。

画面：特写修改后的便签“今天分享两个方法”，键盘和空白笔记本保留在画面边缘。镜头静止，让观众看清最终文字。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–4.0 秒**

旁白：逐句读一遍，留下你想表达的文字。

预计镜头时长：4.0 秒

预计总时长：14.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "e34ddda670ae468ce980fb01e9ec9bb51e9e23e7424cb1df4ad396d41cdfdc9b",
  "passed": true,
  "issues": [],
  "citations": [
    {
      "location": "shot:2/block:1",
      "source_id": "P01",
      "fact_id": "P01.F2",
      "quote": "字幕文字可以手动编辑。",
      "version": "2026-11-01",
      "text": "剪影练习版的字幕文字可以手动编辑。",
      "requires_semantic_review": true
    }
  ],
  "rules_version": "2026-11-03-v1",
  "requires_expression_review": true,
  "expression_slots": [
    {
      "location": "title",
      "text": "不露脸的知识分享：手动改好字幕文字"
    },
    {
      "location": "shot:1/visual",
      "text": "俯拍键盘、摊开的空白笔记本和一张便签。便签写着“今天分享三个方法”。镜头缓慢靠近便签，全程无人或手部入画。"
    },
    {
      "location": "shot:1/block:1",
      "text": "知识分享，从一句清楚的字幕开始。"
    },
    {
      "location": "shot:2/visual",
      "text": "保持同一构图，通过停机替换便签再切镜，将“三个方法”换为“两个方法”。便签底部印小字“文案修改示意”。笔记本内页保持空白，不展示软件操作。"
    },
    {
      "location": "shot:2/block:1",
      "text": "剪影练习版的字幕文字可以手动编辑。"
    },
    {
      "location": "shot:3/visual",
      "text": "特写修改后的便签“今天分享两个方法”，键盘和空白笔记本保留在画面边缘。镜头静止，让观众看清最终文字。"
    },
    {
      "location": "shot:3/block:1",
      "text": "逐句读一遍，留下你想表达的文字。"
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
  "script_hash": "e34ddda670ae468ce980fb01e9ec9bb51e9e23e7424cb1df4ad396d41cdfdc9b",
  "request_hash": "57e9fad560a4df02ef94972a7997aa3a52eb81ff2e4a84f66cfd2fd6df778bd6",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "介绍手动编辑字幕文字",
      "verdict": "met",
      "evidence": "第2镜旁白明确介绍“字幕文字可以手动编辑”，并以便签换字示意修改。"
    },
    {
      "field": "topic",
      "requirement": "全部画面只用键盘、便签和空白笔记本",
      "verdict": "met",
      "evidence": "三镜均限定为键盘、便签和空白笔记本，第2镜明确内页保持空白。"
    },
    {
      "field": "topic",
      "requirement": "不出现人物、人物照片或手机界面",
      "verdict": "met",
      "evidence": "第1镜明确无人或手部入画，后两镜沿用物品构图，未安排人物照片或手机界面。"
    },
    {
      "field": "topic",
      "requirement": "不使用问句开场",
      "verdict": "met",
      "evidence": "开场“知识分享，从一句清楚的字幕开始。”为陈述句。"
    },
    {
      "field": "audience",
      "requirement": "不想出镜的知识分享者",
      "verdict": "met",
      "evidence": "标题明确“不露脸的知识分享”，全片以物品及文字示意呈现，无需创作者出镜。"
    },
    {
      "field": "platform",
      "requirement": "小红书",
      "verdict": "met",
      "evidence": "标题聚焦不露脸创作需求，三镜围绕一个字幕编辑功能展开，适合简短知识分享内容。"
    },
    {
      "field": "style",
      "requirement": "陈述式",
      "verdict": "met",
      "evidence": "前两镜以陈述介绍主题和功能，结尾为平静行动提示，全片无设问。"
    },
    {
      "field": "style",
      "requirement": "安静",
      "verdict": "met",
      "evidence": "第1镜缓慢靠近、第3镜静止观察，旁白简短，无喧闹或强刺激安排。"
    }
  ],
  "summary": "当前稿落实了功能介绍、限定道具、不出镜和陈述式安静表达等要求，公开功能声明有资料支持。预计总长14秒，符合18秒上限，镜头停留有对应的阅读和修改观察内容。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "不露脸的知识分享：手动改好字幕文字",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "手动修改字幕文字由资料支持，“不露脸”描述本片呈现方式，未新增产品能力。"
    },
    {
      "location": "shot:1/visual",
      "text": "俯拍键盘、摊开的空白笔记本和一张便签。便签写着“今天分享三个方法”。镜头缓慢靠近便签，全程无人或手部入画。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅包含道具、示例文案和拍摄安排，没有产品承诺。"
    },
    {
      "location": "shot:1/block:1",
      "text": "知识分享，从一句清楚的字幕开始。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于主题引入，未声称产品自动生成或改善字幕。"
    },
    {
      "location": "shot:2/visual",
      "text": "保持同一构图，通过停机替换便签再切镜，将“三个方法”换为“两个方法”。便签底部印小字“文案修改示意”。笔记本内页保持空白，不展示软件操作。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "明确为便签文案修改的拍摄示意，没有虚构软件按钮、界面或操作流程。"
    },
    {
      "location": "shot:2/block:1",
      "text": "剪影练习版的字幕文字可以手动编辑。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "与所引原文“字幕文字可以手动编辑。”含义一致，未增加效果或自动化声明。"
    },
    {
      "location": "shot:3/visual",
      "text": "特写修改后的便签“今天分享两个方法”，键盘和空白笔记本保留在画面边缘。镜头静止，让观众看清最终文字。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "展示便签示例及静止观察安排，不包含额外产品能力声明。"
    },
    {
      "location": "shot:3/block:1",
      "text": "逐句读一遍，留下你想表达的文字。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于创作者检查文案的行动提示，未承诺产品执行检查或筛选。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "三镜预计分别4、6、4秒；第1镜观察便签并听开场，第2镜4.5秒旁白后留1.5秒观察换字，第3镜静止阅读最终文字并听提示，停留有具体内容支撑。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
