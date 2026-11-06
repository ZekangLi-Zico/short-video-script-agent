# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成三镜头字幕教程，预计19秒：采访现场→剪辑桌面→放映幕布。仅讲添加字幕和手动改字，简短中文旁白配同步英文字幕，结尾停在幕布，无购买号召。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 字幕，让表达被看见

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

镜头目的：从摄影社刚拍完的校园采访，引出整理字幕的任务。

画面：校园采访现场，受访同学说完话，采访者收回话筒；摄影社新同学放下相机，低头回看刚拍的画面。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–3.3 秒**

旁白：采访拍好了，来给它配字幕。

屏幕文字：The interview is filmed. Let's add subtitles.

预计镜头时长：4.0 秒

### 分镜 2

镜头目的：依次展示添加字幕、发现错字后手动修改两个动作。

画面：俯拍剪辑同学的桌面，用采访画面与字幕叠层示意：第一拍，画面下方出现字幕；第二拍，放大其中一个错字，同学敲键盘，错字变为正确文字。示意画面不出现具体软件按钮或菜单。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–4.0 秒**

旁白：先给采访视频添加字幕。

依据：P01/P01.F1

屏幕文字：First, add subtitles to the interview video.

依据：P01/P01.F1

**第 2 拍 · 镜内 4.0–8.0 秒**

旁白：字幕里有错字，可以手动改。

依据：P01/P01.F2

屏幕文字：You can manually correct typos in the subtitles.

依据：P01/P01.F2

预计镜头时长：10.0 秒

### 分镜 3

镜头目的：在放映场景中核对修正后的字幕，结束教程。

画面：放映室幕布上播放刚才的采访片段，保留修正后的字幕；前排同学抬头观看。教程英文字幕放在幕布下方留白处，结尾始终停在幕布画面。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–4.5 秒**

旁白：最后放一遍，跟着采访核对字幕。

屏幕文字：Play it back and check the subtitles against the interview.

预计镜头时长：5.0 秒

预计总时长：19.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "58d51e7c7af734de9623821dbeaecc71601f3ec550a93e9282c90b624397fcab",
  "passed": true,
  "issues": [],
  "citations": [
    {
      "location": "shot:2/block:1",
      "source_id": "P01",
      "fact_id": "P01.F1",
      "quote": "剪影练习版支持为视频添加字幕。",
      "version": "2026-11-01",
      "text": "先给采访视频添加字幕。",
      "requires_semantic_review": true
    },
    {
      "location": "shot:2/block:2",
      "source_id": "P01",
      "fact_id": "P01.F1",
      "quote": "剪影练习版支持为视频添加字幕。",
      "version": "2026-11-01",
      "text": "First, add subtitles to the interview video.",
      "requires_semantic_review": true
    },
    {
      "location": "shot:2/block:3",
      "source_id": "P01",
      "fact_id": "P01.F2",
      "quote": "字幕文字可以手动编辑。",
      "version": "2026-11-01",
      "text": "字幕里有错字，可以手动改。",
      "requires_semantic_review": true
    },
    {
      "location": "shot:2/block:4",
      "source_id": "P01",
      "fact_id": "P01.F2",
      "quote": "字幕文字可以手动编辑。",
      "version": "2026-11-01",
      "text": "You can manually correct typos in the subtitles.",
      "requires_semantic_review": true
    }
  ],
  "rules_version": "2026-11-03-v1",
  "requires_expression_review": true,
  "expression_slots": [
    {
      "location": "title",
      "text": "字幕，让表达被看见"
    },
    {
      "location": "shot:1/visual",
      "text": "校园采访现场，受访同学说完话，采访者收回话筒；摄影社新同学放下相机，低头回看刚拍的画面。"
    },
    {
      "location": "shot:1/block:1",
      "text": "采访拍好了，来给它配字幕。"
    },
    {
      "location": "shot:1/block:2",
      "text": "The interview is filmed. Let's add subtitles."
    },
    {
      "location": "shot:2/visual",
      "text": "俯拍剪辑同学的桌面，用采访画面与字幕叠层示意：第一拍，画面下方出现字幕；第二拍，放大其中一个错字，同学敲键盘，错字变为正确文字。示意画面不出现具体软件按钮或菜单。"
    },
    {
      "location": "shot:2/block:1",
      "text": "先给采访视频添加字幕。"
    },
    {
      "location": "shot:2/block:2",
      "text": "First, add subtitles to the interview video."
    },
    {
      "location": "shot:2/block:3",
      "text": "字幕里有错字，可以手动改。"
    },
    {
      "location": "shot:2/block:4",
      "text": "You can manually correct typos in the subtitles."
    },
    {
      "location": "shot:3/visual",
      "text": "放映室幕布上播放刚才的采访片段，保留修正后的字幕；前排同学抬头观看。教程英文字幕放在幕布下方留白处，结尾始终停在幕布画面。"
    },
    {
      "location": "shot:3/block:1",
      "text": "最后放一遍，跟着采访核对字幕。"
    },
    {
      "location": "shot:3/block:2",
      "text": "Play it back and check the subtitles against the interview."
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
  "script_hash": "58d51e7c7af734de9623821dbeaecc71601f3ec550a93e9282c90b624397fcab",
  "request_hash": "9227d87d70d9292c3a45961b43c35e593aeadca2771339e88b747a3c04e3eea5",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "我在学校摄影社教新同学整理校园采访短片",
      "verdict": "met",
      "evidence": "第1镜明确呈现校园采访、摄影社新同学及拍后回看；第2镜整理采访字幕，第3镜放映核对，落实教学场景。"
    },
    {
      "field": "topic",
      "requirement": "准备发一条字幕小教程",
      "verdict": "met",
      "evidence": "第2镜依次讲解“先给采访视频添加字幕”和“字幕里有错字，可以手动改”，配有对应动作示意。"
    },
    {
      "field": "topic",
      "requirement": "采访现场",
      "verdict": "met",
      "evidence": "第1镜为“校园采访现场”，包含受访者说完话、采访者收回话筒、新同学放下相机等动作。"
    },
    {
      "field": "topic",
      "requirement": "剪辑同学的桌面",
      "verdict": "met",
      "evidence": "第2镜明确“俯拍剪辑同学的桌面”，展示字幕出现及敲键盘改字。"
    },
    {
      "field": "topic",
      "requirement": "放映时的幕布",
      "verdict": "met",
      "evidence": "第3镜为放映室幕布播放采访片段；三镜依次对应采访现场、剪辑桌面、放映幕布。"
    },
    {
      "field": "topic",
      "requirement": "只讲添加字幕和手动改字",
      "verdict": "met",
      "evidence": "功能介绍仅包含第2镜的添加字幕、手动改字。回看与幕布放映属于检查和拍摄场景；教程英文字幕未被描述为产品翻译功能，全文未介绍裁剪等范围外功能。"
    },
    {
      "field": "topic",
      "requirement": "添加字幕",
      "verdict": "met",
      "evidence": "第2镜第1拍中英文字均介绍添加字幕，画面下方出现字幕；P01.F1支持该能力。"
    },
    {
      "field": "topic",
      "requirement": "手动改字",
      "verdict": "met",
      "evidence": "第2镜第2拍说明可手动改错字，并安排同学敲键盘将错字改正；P01.F2支持该能力。"
    },
    {
      "field": "topic",
      "requirement": "用简短中文旁白",
      "verdict": "met",
      "evidence": "全部voice块均为简短中文句子，如“先给采访视频添加字幕。”“字幕里有错字，可以手动改。”，没有英文朗读块。"
    },
    {
      "field": "topic",
      "requirement": "同时给外国交换生显示对应英文字幕",
      "verdict": "met",
      "evidence": "四段中文voice均有同beat的对应英文screen块；例如第2镜第2拍对应“You can manually correct typos in the subtitles.”，内容准确且同步显示。"
    },
    {
      "field": "topic",
      "requirement": "结尾停在幕布",
      "verdict": "met",
      "evidence": "第3镜明确“结尾始终停在幕布画面”，其后没有其他镜头。"
    },
    {
      "field": "topic",
      "requirement": "不要购买号召",
      "verdict": "met",
      "evidence": "标题、全部文案及画面均无购买引导；结尾是“最后放一遍，跟着采访核对字幕。”"
    },
    {
      "field": "audience",
      "requirement": "刚加入摄影社的中国学生和英语交换生",
      "verdict": "met",
      "evidence": "校园摄影社场景与添加字幕、手动改字的基础示意适合新同学；中文旁白配同步英文字幕，覆盖两类学生的理解需要。"
    },
    {
      "field": "platform",
      "requirement": "B站",
      "verdict": "met",
      "evidence": "脚本为校园经验分享式短教程，三镜构成完整教学过程，配中英声画信息，适合B站短视频呈现。"
    },
    {
      "field": "style",
      "requirement": "像同学分享经验",
      "verdict": "met",
      "evidence": "“采访拍好了，来给它配字幕。”“最后放一遍，跟着采访核对字幕。”采用自然的同伴交流口吻。"
    },
    {
      "field": "style",
      "requirement": "清楚自然",
      "verdict": "met",
      "evidence": "按拍好采访、添加字幕、手动改字、放映核对推进；句子简短，英文对应准确，没有内部审稿说明或生硬术语。"
    },
    {
      "field": "style",
      "requirement": "镜头有具体动作",
      "verdict": "met",
      "evidence": "第1镜收回话筒、放下相机并回看；第2镜出现字幕、敲键盘改字；第3镜播放采访，同学抬头观看，均有明确动作。"
    }
  ],
  "summary": "各项需求均已落实：三镜按指定场景展开，仅介绍添加字幕和手动改字，中文旁白与英文字幕对应，结尾停在幕布且无购买号召。产品声明均有资料支持，预计19秒，节奏合理。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "字幕，让表达被看见",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于围绕字幕的修辞性标题，没有可验证的产品性能或效果承诺。"
    },
    {
      "location": "shot:1/visual",
      "text": "校园采访现场，受访同学说完话，采访者收回话筒；摄影社新同学放下相机，低头回看刚拍的画面。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "描述校园采访及人物动作，属于拍摄安排，没有产品能力或真实客户背书声明。"
    },
    {
      "location": "shot:1/block:1",
      "text": "采访拍好了，来给它配字幕。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "交代采访完成并邀请进入字幕教程，没有宣称自动生成等产品能力。"
    },
    {
      "location": "shot:1/block:2",
      "text": "The interview is filmed. Let's add subtitles.",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "准确对应同拍中文开场，属于情境交代和行动邀请。"
    },
    {
      "location": "shot:2/visual",
      "text": "俯拍剪辑同学的桌面，用采访画面与字幕叠层示意：第一拍，画面下方出现字幕；第二拍，放大其中一个错字，同学敲键盘，错字变为正确文字。示意画面不出现具体软件按钮或菜单。",
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
      "evidence": "字幕出现由“支持为视频添加字幕”支持，人工敲键盘改字由“字幕文字可以手动编辑”支持。放大错字为画面示意，未虚构软件按钮、布局或自动纠错流程。"
    },
    {
      "location": "shot:2/block:1",
      "text": "先给采访视频添加字幕。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "P01.F1原文为“剪影练习版支持为视频添加字幕。”；采访视频是使用场景，没有增加自动化或其他能力。"
    },
    {
      "location": "shot:2/block:2",
      "text": "First, add subtitles to the interview video.",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "准确翻译同拍中文，全部功能含义由P01.F1的添加字幕能力支持。"
    },
    {
      "location": "shot:2/block:3",
      "text": "字幕里有错字，可以手动改。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "P01.F2原文为“字幕文字可以手动编辑。”；手动修正错字属于该能力，没有增加自动识别或纠错承诺。"
    },
    {
      "location": "shot:2/block:4",
      "text": "You can manually correct typos in the subtitles.",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "“manually correct typos”准确表达手动修改字幕错字，全部含义由P01.F2支持。"
    },
    {
      "location": "shot:3/visual",
      "text": "放映室幕布上播放刚才的采访片段，保留修正后的字幕；前排同学抬头观看。教程英文字幕放在幕布下方留白处，结尾始终停在幕布画面。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "描述已修正片段的幕布展示、观看动作和教程字幕位置，属于拍摄与呈现安排，没有宣称产品支持投影或自动翻译。"
    },
    {
      "location": "shot:3/block:1",
      "text": "最后放一遍，跟着采访核对字幕。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于人工观看核对的操作建议，没有宣称软件自动核对字幕。"
    },
    {
      "location": "shot:3/block:2",
      "text": "Play it back and check the subtitles against the interview.",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "对应同拍中文的播放与人工核对建议，没有新增产品功能承诺。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "采用duration_check的实际估算：第1镜4秒，同拍声画需3.3秒，采访收尾与回看动作支撑剩余停留；第2镜10秒，添加字幕、手动改字两拍各4秒，另2秒可观察修改结果；第3镜5秒，同拍声画需4.5秒，幕布播放与观看支撑停留。各镜均满足hold_seconds，声画按同拍并行计算，没有重复事实或无内容空镜凑时长；总长19秒，已通过25秒上限检查。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
