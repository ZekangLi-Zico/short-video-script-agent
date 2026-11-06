# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成三镜脚本，覆盖添加字幕、手动改字及修改前后示例。实拍仅含空白笼牌、牵引绳和志愿者手部，不使用真实姓名或联系方式，风格温暖但不煽情。当前稿无需删改，三项检查均通过；估时15.1秒，符合28秒上限，此数值为工具估算，并非成片实测。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 给领养日花絮添上字幕

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

画面：近景只拍志愿者手部整理牵引绳，旁边放置无文字的笼牌。镜头不带入人物面部、动物或其他物件。旁白配同文字幕。

旁白/字幕：领养日花絮，从整理牵引绳开始。

来源：

预计镜头时长：3.8 秒

### 分镜 2

画面：延续手部整理牵引绳的花絮近景，空白笼牌留在画面边缘。将本镜产品事实作为旁白和同文字幕叠加在素材上，不展示软件界面。

旁白/字幕：剪影练习版支持为视频添加字幕。

来源：P01/P01.F1

预计镜头时长：4.0 秒

### 分镜 3

画面：志愿者双手将整理好的牵引绳放在空白笼牌旁。产品事实以旁白说明；随后在同一段花絮上依次展示修改前、修改后的示例字幕，表示手动修改文字的结果，不展示按钮、键盘或软件界面。

旁白/字幕：字幕文字可以手动编辑。修改前：整理牵引绳。修改后：牵引绳已备好。

来源：P01/P01.F2

预计镜头时长：7.3 秒

## 审稿备注（不进入视频，不计入时长）

供创作者核对修改与资料缺口，不是经过事实认证的产品介绍。

仅介绍添加字幕和手动修改字幕文字。全片实拍内容限空白笼牌、牵引绳及志愿者手部，不出现真实姓名、联系方式或其他可识别资料。修改前后两句为屏幕文字示例，不配旁白；估时工具仍会将全部文字串行计算，不能据此声称精确测得字幕阅读时间。示例以普通切换展示，不暗示自动修改。

预计总时长：15.1 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "b4ae61eb00e806983b0d64087b424ec8d99b3df12f34cb67fb15f15ca386ab3f",
  "passed": true,
  "issues": [],
  "citations": [
    {
      "location": "shot:2/block:1",
      "source_id": "P01",
      "fact_id": "P01.F1",
      "quote": "剪影练习版支持为视频添加字幕。",
      "version": "2026-11-01"
    },
    {
      "location": "shot:3/block:1",
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
      "text": "给领养日花絮添上字幕"
    },
    {
      "location": "shot:1/visual",
      "text": "近景只拍志愿者手部整理牵引绳，旁边放置无文字的笼牌。镜头不带入人物面部、动物或其他物件。旁白配同文字幕。"
    },
    {
      "location": "shot:1/block:1",
      "text": "领养日花絮，从整理牵引绳开始。"
    },
    {
      "location": "shot:2/visual",
      "text": "延续手部整理牵引绳的花絮近景，空白笼牌留在画面边缘。将本镜产品事实作为旁白和同文字幕叠加在素材上，不展示软件界面。"
    },
    {
      "location": "shot:3/visual",
      "text": "志愿者双手将整理好的牵引绳放在空白笼牌旁。产品事实以旁白说明；随后在同一段花絮上依次展示修改前、修改后的示例字幕，表示手动修改文字的结果，不展示按钮、键盘或软件界面。"
    },
    {
      "location": "shot:3/block:2",
      "text": "修改前：整理牵引绳。"
    },
    {
      "location": "shot:3/block:3",
      "text": "修改后：牵引绳已备好。"
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
  "script_hash": "b4ae61eb00e806983b0d64087b424ec8d99b3df12f34cb67fb15f15ca386ab3f",
  "request_hash": "5c0b0575b38040eae7c360d4797877a9d0ce4b18e4b26ee4c709496cad63c2dd",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "做一条工具介绍",
      "verdict": "met",
      "evidence": "第2镜点名“剪影练习版”并介绍添加字幕，第3镜介绍手动编辑字幕文字，构成工具介绍。"
    },
    {
      "field": "topic",
      "requirement": "说明可为领养日花絮添加字幕",
      "verdict": "met",
      "evidence": "标题为“给领养日花絮添上字幕”；第1镜明确领养日场景，第2镜在手部整理牵引绳的花絮上叠加字幕，并说明“剪影练习版支持为视频添加字幕。”"
    },
    {
      "field": "topic",
      "requirement": "手动修改文字",
      "verdict": "met",
      "evidence": "第3镜说明“字幕文字可以手动编辑。”，并依次展示“修改前：整理牵引绳。”和“修改后：牵引绳已备好。”，画面明确表示手动修改的结果。"
    },
    {
      "field": "topic",
      "requirement": "画面只拍笼牌、牵引绳和志愿者手部",
      "verdict": "met",
      "evidence": "第1镜仅拍手部、牵引绳和无文字笼牌，明确排除面部、动物及其他物件；第2镜延续同一构图；第3镜仅拍双手放置牵引绳，且明确不展示按钮、键盘或软件界面。"
    },
    {
      "field": "topic",
      "requirement": "不使用真实姓名",
      "verdict": "met",
      "evidence": "全部旁白和示例字幕均无人名；三镜笼牌均设为空白，没有承载真实姓名的画面内容。"
    },
    {
      "field": "topic",
      "requirement": "不使用真实姓名和联系方式",
      "verdict": "met",
      "evidence": "联系方式方面，标题、旁白及字幕均无电话、账号或地址；实拍仅包含空白笼牌、牵引绳和手部，没有展示联系方式的安排。"
    },
    {
      "field": "audience",
      "requirement": "动物救助志愿者",
      "verdict": "met",
      "evidence": "以领养日准备牵引绳的志愿服务场景切入，介绍花絮字幕及文字修改，用语直白，符合志愿者记录活动的需求。"
    },
    {
      "field": "platform",
      "requirement": "视频号",
      "verdict": "met",
      "evidence": "采用三镜短视频结构、近景动作、旁白配同文字幕及修改前后示例，内容可通过观看和阅读理解，适合视频号呈现。"
    },
    {
      "field": "style",
      "requirement": "温暖",
      "verdict": "met",
      "evidence": "第1镜以“领养日花絮，从整理牵引绳开始。”配合志愿者手部准备动作，呈现平实、关怀的氛围。"
    },
    {
      "field": "style",
      "requirement": "不煽情",
      "verdict": "met",
      "evidence": "全片围绕准备动作和两项字幕功能展开，没有悲情叙述、苦难画面或情绪施压式呼吁。"
    }
  ],
  "summary": "当前脚本落实了功能、领养日场景、拍摄范围及隐私要求，受众、平台和风格适配。未发现无依据的产品承诺；预计15.1秒，符合28秒上限，节奏合理。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "给领养日花絮添上字幕",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "标题将添加视频字幕的能力应用于领养日花絮，P01.F1支持该能力，未增加自动化或效果承诺。"
    },
    {
      "location": "shot:1/visual",
      "text": "近景只拍志愿者手部整理牵引绳，旁边放置无文字的笼牌。镜头不带入人物面部、动物或其他物件。旁白配同文字幕。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "内容为取景范围、手部动作及旁白字幕的制作安排，没有可验证的产品能力或效果承诺。"
    },
    {
      "location": "shot:1/block:1",
      "text": "领养日花絮，从整理牵引绳开始。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "这是领养日场景的开场描述，与本镜整理牵引绳的动作对应，不含产品声明。"
    },
    {
      "location": "shot:2/visual",
      "text": "延续手部整理牵引绳的花絮近景，空白笼牌留在画面边缘。将本镜产品事实作为旁白和同文字幕叠加在素材上，不展示软件界面。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "规定素材构图及已核对文案的呈现方式，没有新增产品承诺，也没有虚构软件界面或操作步骤。"
    },
    {
      "location": "shot:3/visual",
      "text": "志愿者双手将整理好的牵引绳放在空白笼牌旁。产品事实以旁白说明；随后在同一段花絮上依次展示修改前、修改后的示例字幕，表示手动修改文字的结果，不展示按钮、键盘或软件界面。",
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
      "evidence": "画面示意视频字幕及手动编辑文字的结果，分别由P01.F1、P01.F2支持；没有暗示自动改写，也未虚构按钮、界面布局或具体操作流程。"
    },
    {
      "location": "shot:3/block:2",
      "text": "修改前：整理牵引绳。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "这是描述画面动作的示例字幕，修改前标签用于组织演示，不含额外产品承诺。"
    },
    {
      "location": "shot:3/block:3",
      "text": "修改后：牵引绳已备好。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "这是与牵引绳整理完成画面对应的修改后示例文字，没有宣称自动生成、识别或修改能力。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "第1镜预计3.8秒，承载简短开场及整理动作；第2镜4.0秒，承载一句添加字幕的功能介绍；第3镜7.3秒，承载放置动作、手动编辑说明及两句短字幕依次展示。依editor_notes，修改前后文字仅供阅读、不配旁白，备注本身不参与计时。三镜内容有推进，没有空镜或重复事实凑时长；宿主估算总长15.1秒，已通过28秒上限检查。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
