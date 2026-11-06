# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成三镜脚本，仅介绍手动编辑字幕文字。画面仅用键盘、空白便签和空白笔记本，不出现人物、人物照片或手机界面；开场为陈述句，整体安静。预计9秒，符合18秒上限。本轮无需删改，无待补材料；实际成片时长以剪辑为准。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 手动编辑字幕文字

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

画面：固定俯拍静物：键盘、空白便签和摊开的空白笔记本。柔和光线，画面无人物、手部、人物照片或任何设备界面。

旁白/字幕：字幕文字，值得逐字斟酌。

来源：

预计镜头时长：3.0 秒

### 分镜 2

画面：切换为键盘与空白便签的近景，空白笔记本边缘入画；保持静物构图，不出现人物、照片、屏幕或操作界面。

旁白/字幕：字幕文字可以手动编辑。

来源：P01/P01.F2

预计镜头时长：3.0 秒

### 分镜 3

画面：回到三件静物的俯拍构图，空白笔记本居中，键盘和空白便签位于两侧。镜头静止，不增加其他物件或图像。

旁白/字幕：读一遍，再推敲措辞。

来源：

预计镜头时长：3.0 秒

## 审稿备注（不进入视频，不计入时长）

供创作者核对修改与资料缺口，不是经过事实认证的产品介绍。

所有文字块均为旁白，不另设屏幕事实卡；语气平静、陈述式。全片仅拍键盘、空白便签和空白笔记本，避免人物、手部及人像倒影，不展示手机或产品界面。静物用于承载旁白，不作为产品操作演示。仅介绍手动编辑字幕文字，不扩展其他功能。

预计总时长：9.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "2df49b98e791e4453f21006f2ee04929896249d864b7f9d57d38a98c5120408a",
  "passed": true,
  "issues": [],
  "citations": [
    {
      "location": "shot:2/block:1",
      "source_id": "P01",
      "fact_id": "P01.F2",
      "quote": "字幕文字可以手动编辑。",
      "version": "2026-11-01"
    }
  ],
  "rules_version": "2026-11-03-v1",
  "requires_expression_review": true,
  "expression_slots": [
    {
      "location": "title",
      "text": "手动编辑字幕文字"
    },
    {
      "location": "shot:1/visual",
      "text": "固定俯拍静物：键盘、空白便签和摊开的空白笔记本。柔和光线，画面无人物、手部、人物照片或任何设备界面。"
    },
    {
      "location": "shot:1/block:1",
      "text": "字幕文字，值得逐字斟酌。"
    },
    {
      "location": "shot:2/visual",
      "text": "切换为键盘与空白便签的近景，空白笔记本边缘入画；保持静物构图，不出现人物、照片、屏幕或操作界面。"
    },
    {
      "location": "shot:3/visual",
      "text": "回到三件静物的俯拍构图，空白笔记本居中，键盘和空白便签位于两侧。镜头静止，不增加其他物件或图像。"
    },
    {
      "location": "shot:3/block:1",
      "text": "读一遍，再推敲措辞。"
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
  "script_hash": "2df49b98e791e4453f21006f2ee04929896249d864b7f9d57d38a98c5120408a",
  "request_hash": "57e9fad560a4df02ef94972a7997aa3a52eb81ff2e4a84f66cfd2fd6df778bd6",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "介绍手动编辑字幕文字",
      "verdict": "met",
      "evidence": "标题为“手动编辑字幕文字”，第2镜旁白“字幕文字可以手动编辑。”直接介绍该功能，且已获P01.F2支持。"
    },
    {
      "field": "topic",
      "requirement": "全部画面只用键盘、便签和空白笔记本",
      "verdict": "met",
      "evidence": "第1镜仅安排键盘、空白便签和空白笔记本；第2镜改变取景距离；第3镜回到三件静物，并明确“不增加其他物件或图像”。"
    },
    {
      "field": "topic",
      "requirement": "不出现人物",
      "verdict": "met",
      "evidence": "第1镜明确“画面无人物、手部”，第2镜明确“不出现人物”，第3镜仅安排三件静物。"
    },
    {
      "field": "topic",
      "requirement": "人物照片",
      "verdict": "met",
      "evidence": "按原文“不出现”的禁用要求核对：第1镜明确排除人物照片，第2镜排除照片，第3镜不增加其他图像。"
    },
    {
      "field": "topic",
      "requirement": "手机界面",
      "verdict": "met",
      "evidence": "按原文“不出现”的禁用要求核对：第1镜排除“任何设备界面”，第2镜排除“屏幕或操作界面”，第3镜仅展示指定静物。"
    },
    {
      "field": "topic",
      "requirement": "不使用问句开场",
      "verdict": "met",
      "evidence": "第1镜以“字幕文字，值得逐字斟酌。”开场，没有使用问句。"
    },
    {
      "field": "audience",
      "requirement": "不想出镜的知识分享者",
      "verdict": "met",
      "evidence": "全片以静物配旁白介绍字幕编辑，不需要人物出镜，内容与知识分享者处理文字表达的需求相符。"
    },
    {
      "field": "platform",
      "requirement": "小红书",
      "verdict": "met",
      "evidence": "标题直接点明主题，三镜采用简短旁白和统一静物构图，适合小红书的简短知识分享内容。"
    },
    {
      "field": "style",
      "requirement": "陈述式",
      "verdict": "met",
      "evidence": "开场“字幕文字，值得逐字斟酌。”和核心介绍“字幕文字可以手动编辑。”采用平实陈述，结尾为简短措辞建议，整体没有问答式展开。"
    },
    {
      "field": "style",
      "requirement": "安静",
      "verdict": "met",
      "evidence": "第1镜使用固定俯拍、柔和光线，第2镜保持静物构图，第3镜明确“镜头静止”；editor_notes规定旁白“语气平静”。"
    }
  ],
  "summary": "稿件覆盖全部明确要求，画面仅使用指定静物，开场和整体风格符合要求。产品声明有资料支持，三镜节奏合理。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "手动编辑字幕文字",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "P01.F2明确说明“字幕文字可以手动编辑。”，支持标题所述功能。"
    },
    {
      "location": "shot:1/visual",
      "text": "固定俯拍静物：键盘、空白便签和摊开的空白笔记本。柔和光线，画面无人物、手部、人物照片或任何设备界面。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅规定拍摄物件、光线、机位和排除元素，没有产品能力或操作界面声明。"
    },
    {
      "location": "shot:1/block:1",
      "text": "字幕文字，值得逐字斟酌。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于对措辞的主观建议，没有可验证的产品性能或效果承诺。"
    },
    {
      "location": "shot:2/visual",
      "text": "切换为键盘与空白便签的近景，空白笔记本边缘入画；保持静物构图，不出现人物、照片、屏幕或操作界面。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅描述近景构图与拍摄限制，没有虚构按钮、操作步骤或产品工作流程。"
    },
    {
      "location": "shot:3/visual",
      "text": "回到三件静物的俯拍构图，空白笔记本居中，键盘和空白便签位于两侧。镜头静止，不增加其他物件或图像。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅安排静物位置和镜头状态，不包含产品事实声明。"
    },
    {
      "location": "shot:3/block:1",
      "text": "读一遍，再推敲措辞。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于面向观众的文字检查建议，没有宣称产品自动检查或改写能力。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "duration_check显示三镜均预计3秒，与各镜3秒最低停留一致；旁白分别为10、10、8个语音单位，配合全景、近景、全景的静物观察，停留合理。功能事实仅介绍一次，没有重复凑时长；总长预计9秒，已通过18秒上限检查。editor_notes不计入旁白时长。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
