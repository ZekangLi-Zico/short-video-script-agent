# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成4镜头脚本，用签到桌、旧书摊、打包纸箱串联添加字幕和手动纠正物品名称，结尾回到整理纸箱现场，无下载宣传。当前稿无需删改。估算28秒，符合27—30秒目标；实际时长以成片为准。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 旧物交换拍完后：给志愿者的字幕小经验

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

画面：签到桌现场，志愿者整理签到用品。以下文字作为旁白，镜头从桌面移向活动记录者。

旁白/字幕：旧物交换拍完了，给志愿者伙伴分享两个字幕小经验。

来源：

预计镜头时长：6.0 秒

### 分镜 2

画面：继续使用签到桌片段，演示叠加字幕“旧物交换签到处”，留出阅读时间。以下两段均作为旁白，不另设事实卡；只展示视频与字幕效果，不虚构软件按钮或菜单。

旁白/字幕：剪影练习版支持为视频添加字幕。签到这段，配上现场说明。

来源：P01/P01.F1

预计镜头时长：8.0 秒

### 分镜 3

画面：切到旧书摊实拍，镜头看清摊上的书。以字幕文字示意呈现误写的“旧衣”，再展示手动改成“旧书”的结果，留出前后核对时间。以下文字作为旁白，不展示未经核实的软件界面。

旁白/字幕：字幕文字可以手动编辑。旧书写成旧衣？手动改回旧书。

来源：P01/P01.F2

预计镜头时长：8.0 秒

### 分镜 4

画面：回到整理纸箱的现场：志愿者把旧书放进纸箱，核对物品后合上箱盖。以下文字作为旁白，结尾停在整理纸箱的动作上，保留现场声。

旁白/字幕：纸箱装好前，再看一遍，字幕里的物品名对不对。

来源：

预计镜头时长：6.0 秒

时长要求：27.0–30 秒（接近目标）。

预计总时长：28.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "92c4b4dc705971f29a9d217b192096d7a208055d2b93187c977d91b60c1a81fd",
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
      "text": "旧物交换拍完后：给志愿者的字幕小经验"
    },
    {
      "location": "shot:1/visual",
      "text": "签到桌现场，志愿者整理签到用品。以下文字作为旁白，镜头从桌面移向活动记录者。"
    },
    {
      "location": "shot:1/block:1",
      "text": "旧物交换拍完了，给志愿者伙伴分享两个字幕小经验。"
    },
    {
      "location": "shot:2/visual",
      "text": "继续使用签到桌片段，演示叠加字幕“旧物交换签到处”，留出阅读时间。以下两段均作为旁白，不另设事实卡；只展示视频与字幕效果，不虚构软件按钮或菜单。"
    },
    {
      "location": "shot:2/block:2",
      "text": "签到这段，配上现场说明。"
    },
    {
      "location": "shot:3/visual",
      "text": "切到旧书摊实拍，镜头看清摊上的书。以字幕文字示意呈现误写的“旧衣”，再展示手动改成“旧书”的结果，留出前后核对时间。以下文字作为旁白，不展示未经核实的软件界面。"
    },
    {
      "location": "shot:3/block:2",
      "text": "旧书写成旧衣？手动改回旧书。"
    },
    {
      "location": "shot:4/visual",
      "text": "回到整理纸箱的现场：志愿者把旧书放进纸箱，核对物品后合上箱盖。以下文字作为旁白，结尾停在整理纸箱的动作上，保留现场声。"
    },
    {
      "location": "shot:4/block:1",
      "text": "纸箱装好前，再看一遍，字幕里的物品名对不对。"
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
  "script_hash": "92c4b4dc705971f29a9d217b192096d7a208055d2b93187c977d91b60c1a81fd",
  "request_hash": "db0dc7143d26b2be4b7c66bc087e8dd5fdcdc6a636fe7a51942e0df40c1ae4a1",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "社区旧物交换活动",
      "verdict": "met",
      "evidence": "标题及镜头1旁白明确写“旧物交换”，后续签到、旧书摊和纸箱整理均围绕该活动展开。"
    },
    {
      "field": "topic",
      "requirement": "给志愿者看的剪辑经验分享",
      "verdict": "met",
      "evidence": "镜头1以“给志愿者伙伴分享两个字幕小经验”开场，镜头2、3给出活动字幕示例和纠错示例。"
    },
    {
      "field": "topic",
      "requirement": "签到桌",
      "verdict": "met",
      "evidence": "镜头1为“签到桌现场”，镜头2继续使用签到桌片段。"
    },
    {
      "field": "topic",
      "requirement": "旧书摊",
      "verdict": "met",
      "evidence": "镜头3明确“切到旧书摊实拍，镜头看清摊上的书”。"
    },
    {
      "field": "topic",
      "requirement": "打包纸箱",
      "verdict": "met",
      "evidence": "镜头4安排志愿者把旧书放进纸箱、核对物品并合上箱盖，体现打包过程。"
    },
    {
      "field": "topic",
      "requirement": "三个场景串起来",
      "verdict": "met",
      "evidence": "镜头1、2呈现签到桌，镜头3转到旧书摊，镜头4回到纸箱整理，以添加说明、纠正名称、装箱前复核串联三个场景。"
    },
    {
      "field": "topic",
      "requirement": "介绍怎样给活动视频添加字幕",
      "verdict": "met",
      "evidence": "镜头2演示在签到桌片段叠加“旧物交换签到处”，并用“签到这段，配上现场说明”说明字幕内容的选择。添加字幕能力已由P01.F1核对支持。"
    },
    {
      "field": "topic",
      "requirement": "手动修改字幕里写错的物品名称",
      "verdict": "met",
      "evidence": "镜头3展示字幕误写“旧衣”后手动改成“旧书”的结果，旁白为“旧书写成旧衣？手动改回旧书。”手动编辑能力已由P01.F2核对支持。"
    },
    {
      "field": "topic",
      "requirement": "标题请贴合这次活动",
      "verdict": "met",
      "evidence": "标题“旧物交换拍完后：给志愿者的字幕小经验”同时点明活动、志愿者和字幕经验。"
    },
    {
      "field": "topic",
      "requirement": "语气像同事分享实际经验",
      "verdict": "met",
      "evidence": "“志愿者伙伴”“签到这段，配上现场说明”“手动改回旧书”等表达直接、口语化，围绕实际片段分享做法。"
    },
    {
      "field": "topic",
      "requirement": "结尾回到整理纸箱的现场",
      "verdict": "met",
      "evidence": "镜头4明确回到整理纸箱现场，结尾停在整理动作上并保留现场声。"
    },
    {
      "field": "topic",
      "requirement": "不做软件下载宣传",
      "verdict": "met",
      "evidence": "全稿没有下载链接、安装引导或下载号召；结尾为装箱前核对字幕物品名称。"
    },
    {
      "field": "audience",
      "requirement": "负责活动记录的社区志愿者",
      "verdict": "met",
      "evidence": "使用志愿者记录活动时遇到的签到说明、物品名称纠错和装箱复核情境，无需专业剪辑知识即可理解。"
    },
    {
      "field": "platform",
      "requirement": "视频号",
      "verdict": "met",
      "evidence": "采用现场画面、口语旁白和直观字幕前后对照，主题集中，适合视频号中的活动记录经验分享。"
    },
    {
      "field": "style",
      "requirement": "自然",
      "verdict": "met",
      "evidence": "镜头1以“旧物交换拍完了”自然开场，镜头4保留现场声，以整理纸箱动作收尾。"
    },
    {
      "field": "style",
      "requirement": "具体",
      "verdict": "met",
      "evidence": "明确给出“旧物交换签到处”的字幕内容，以及“旧衣”改为“旧书”的纠错实例。"
    },
    {
      "field": "style",
      "requirement": "短句",
      "verdict": "met",
      "evidence": "旁白采用“签到这段，配上现场说明。”“旧书写成旧衣？手动改回旧书。”等短句。"
    }
  ],
  "summary": "稿件落实了三个活动场景、添加字幕与手动纠错、同事分享语气和纸箱现场收尾，没有下载宣传。表达均有依据或属于拍摄与内容安排，各镜头停留合理。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "旧物交换拍完后：给志愿者的字幕小经验",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "标题说明活动背景、分享对象和主题，不含产品能力或效果承诺。"
    },
    {
      "location": "shot:1/visual",
      "text": "签到桌现场，志愿者整理签到用品。以下文字作为旁白，镜头从桌面移向活动记录者。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "整段为签到场景、人物动作和镜头移动安排，没有产品声明。"
    },
    {
      "location": "shot:1/block:1",
      "text": "旧物交换拍完了，给志愿者伙伴分享两个字幕小经验。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于活动背景与开场介绍；两个经验对应后文添加字幕及手动纠错，不涉及产品性能数字。"
    },
    {
      "location": "shot:2/visual",
      "text": "继续使用签到桌片段，演示叠加字幕“旧物交换签到处”，留出阅读时间。以下两段均作为旁白，不另设事实卡；只展示视频与字幕效果，不虚构软件按钮或菜单。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "“演示叠加字幕”由“剪影练习版支持为视频添加字幕”支持；具体字幕属于活动内容示例。其余为阅读时间与呈现安排，未增加自动化能力、按钮名称或操作步骤。"
    },
    {
      "location": "shot:2/block:2",
      "text": "签到这段，配上现场说明。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "建议签到片段使用现场说明作为字幕内容，属于内容安排，没有新增产品能力或效果承诺。"
    },
    {
      "location": "shot:3/visual",
      "text": "切到旧书摊实拍，镜头看清摊上的书。以字幕文字示意呈现误写的“旧衣”，再展示手动改成“旧书”的结果，留出前后核对时间。以下文字作为旁白，不展示未经核实的软件界面。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "将字幕文字从“旧衣”手动改为“旧书”属于P01.F2支持的手动编辑。旧书摊及核对时间为拍摄安排，没有虚构自动纠错、界面布局或具体操作步骤。"
    },
    {
      "location": "shot:3/block:2",
      "text": "旧书写成旧衣？手动改回旧书。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "手动替换误写的字幕文字由“字幕文字可以手动编辑”直接支持，未声称系统自动识别或修改错误。"
    },
    {
      "location": "shot:4/visual",
      "text": "回到整理纸箱的现场：志愿者把旧书放进纸箱，核对物品后合上箱盖。以下文字作为旁白，结尾停在整理纸箱的动作上，保留现场声。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "整段为志愿者装箱、核对物品及收尾声音安排，没有宣称软件自动核对物品或处理声音。"
    },
    {
      "location": "shot:4/block:1",
      "text": "纸箱装好前，再看一遍，字幕里的物品名对不对。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "提醒记录者人工复核字幕名称，属于行动建议，不承诺产品具备校验功能。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "镜头1为6秒，配简短开场及从桌面移向记录者的动作；镜头2为8秒，包含两句短旁白和字幕阅读；镜头3为8秒，安排观察旧书、阅读误写文字并核对修改结果；镜头4为6秒，配一句复核提醒及放书、核对、合盖动作。各镜头均有明确观察或动作内容，未见重复同一事实或空镜凑时长。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
