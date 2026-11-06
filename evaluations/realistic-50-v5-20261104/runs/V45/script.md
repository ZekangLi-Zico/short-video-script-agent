# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成《记录里的每句话》三镜脚本，保留原标题、原文及添加字幕和手动改字两个功能。三镜停留调整为4、5、4秒，预计总长13秒，符合25秒上限，未新增功能。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 记录里的每句话

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

镜头目的：用店主备料的日常画面引出视频记录。

画面：店主背对镜头，在备料台上摆好食材，再擦净台面。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–3.0 秒**

旁白＋同步字幕：一天的准备，从这里开始。

镜头末尾保持画面：3.0–4.0 秒（保留最后一拍屏幕文字）

预计镜头时长：4.0 秒

### 分镜 2

镜头目的：通过字幕示意展示为视频添加字幕的功能。

画面：延续备料台画面，将本镜文案作为字幕示意卡叠加在画面下方，不展示具体产品界面。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–4.0 秒**

旁白＋同步字幕：剪影练习版支持为视频添加字幕。

依据：P01/P01.F1

镜头末尾保持画面：4.0–5.0 秒（保留最后一拍屏幕文字）

预计镜头时长：5.0 秒

### 分镜 3

镜头目的：用纸上改错字的动作说明字幕文字可以手动修改。

画面：特写店主在纸上划掉一个错字，在旁边写上正确字，作为手动改字幕的示意；叠加本镜文案。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–3.0 秒**

旁白＋同步字幕：字幕文字可以手动编辑。

依据：P01/P01.F2

镜头末尾保持画面：3.0–4.0 秒（保留最后一拍屏幕文字）

预计镜头时长：4.0 秒

## 审稿备注（不进入视频，不计入时长）

供创作者核对修改与资料缺口，不是经过事实认证的产品介绍。

保留原标题、三镜顺序和全部原文，仅介绍添加字幕与手动改字。三镜最低停留由各15秒调整为4秒、5秒、4秒；迁移至新版格式，补充拍摄动作及声画标记。

## 实际修订

位置按镜头索引比较；日志关联的是实际反馈，不证明模型因果推理。

- 修改：format_version, editor_notes, shot:1/visual, shot:1/hold_seconds, shot:1/purpose, shot:1/block:1, shot:2/visual, shot:2/hold_seconds, shot:2/purpose, shot:2/block:1, shot:3/visual, shot:3/hold_seconds, shot:3/purpose, shot:3/block:1；保留原镜头 0 个、原文案块 0 个。
- 修订前失败检查：duration

预计总时长：13.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "1e915bd05863ed1915548c11509a1189abe84dcb7baab6c2b3b481316e57c9b4",
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
      "text": "记录里的每句话"
    },
    {
      "location": "shot:1/visual",
      "text": "店主背对镜头，在备料台上摆好食材，再擦净台面。"
    },
    {
      "location": "shot:1/block:1",
      "text": "一天的准备，从这里开始。"
    },
    {
      "location": "shot:2/visual",
      "text": "延续备料台画面，将本镜文案作为字幕示意卡叠加在画面下方，不展示具体产品界面。"
    },
    {
      "location": "shot:2/block:1",
      "text": "剪影练习版支持为视频添加字幕。"
    },
    {
      "location": "shot:3/visual",
      "text": "特写店主在纸上划掉一个错字，在旁边写上正确字，作为手动改字幕的示意；叠加本镜文案。"
    },
    {
      "location": "shot:3/block:1",
      "text": "字幕文字可以手动编辑。"
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
    },
    {
      "source_id": "P03",
      "fact_id": "P03.F1",
      "quote": "剪影练习版提供横屏和竖屏画面比例选项。",
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
  "script_hash": "1e915bd05863ed1915548c11509a1189abe84dcb7baab6c2b3b481316e57c9b4",
  "request_hash": "e65b14b1e8059398f2345dd2e1671d2b818db82a54d1ef482bc3f6497e0b06dd",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "把所附旧稿压缩到25秒以内",
      "verdict": "met",
      "evidence": "当前 duration_check 估算三镜分别为4、5、4秒，总长13秒，passed=true，满足25秒上限。"
    },
    {
      "field": "topic",
      "requirement": "添加字幕",
      "verdict": "met",
      "evidence": "第2镜以字幕示意卡配合同步声画文案“剪影练习版支持为视频添加字幕。”保留该功能。"
    },
    {
      "field": "topic",
      "requirement": "手动改字",
      "verdict": "met",
      "evidence": "第3镜展示纸上划掉错字并写上正确字，同步声画文案为“字幕文字可以手动编辑。”"
    },
    {
      "field": "topic",
      "requirement": "标题保持“记录里的每句话”",
      "verdict": "met",
      "evidence": "当前标题为“记录里的每句话”，与旧稿一致。"
    },
    {
      "field": "topic",
      "requirement": "优先改冗长停留",
      "verdict": "met",
      "evidence": "三镜最低停留由旧稿各15秒调整为4、5、4秒；原标题、三镜顺序及全部文案均保留，主要通过缩短停留完成压缩。"
    },
    {
      "field": "topic",
      "requirement": "不要额外添功能",
      "verdict": "met",
      "evidence": "逐镜核对：第1镜为备料场景，第2镜仅介绍添加字幕，第3镜仅介绍手动改字；没有加入资料中其他功能，如裁剪视频或画面比例选项。"
    },
    {
      "field": "audience",
      "requirement": "第一次拍口播的店主",
      "verdict": "met",
      "evidence": "第1镜使用店主备料场景，第2、3镜用直白短句及改错字示意介绍字幕基础能力，无专业术语，适合初次拍口播的店主理解。"
    },
    {
      "field": "platform",
      "requirement": "抖音",
      "verdict": "met",
      "evidence": "全片预计13秒，三镜短句配合同步字幕和具体动作，适合短视频观看；无需在文案中直接出现平台名称。"
    },
    {
      "field": "style",
      "requirement": "自然",
      "verdict": "met",
      "evidence": "“一天的准备，从这里开始。”配合备料台动作自然引入，后续功能表达平实，没有夸张效果承诺。"
    },
    {
      "field": "style",
      "requirement": "紧凑",
      "verdict": "met",
      "evidence": "三镜分别承担场景引入、添加字幕、手动改字，预计4、5、4秒；各镜声画结束后仅余1秒观察时间，没有重复介绍功能或长空镜。"
    }
  ],
  "summary": "当前稿满足原始要求：保留原标题和两个指定功能，未新增功能，主要通过缩短停留将预计总长压至13秒。公开表达有依据，场景、文风及节奏适配。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "记录里的每句话",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于主题标题，未声称自动识别、识别准确率或完整记录能力。"
    },
    {
      "location": "shot:1/visual",
      "text": "店主背对镜头，在备料台上摆好食材，再擦净台面。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于生活场景与拍摄动作安排，没有产品能力或真实客户背书声明。"
    },
    {
      "location": "shot:1/block:1",
      "text": "一天的准备，从这里开始。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于场景引入语，不包含可验证的产品承诺。"
    },
    {
      "location": "shot:2/visual",
      "text": "延续备料台画面，将本镜文案作为字幕示意卡叠加在画面下方，不展示具体产品界面。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅规定字幕示意卡的拍摄呈现方式，未将画面位置描述为产品界面布局，也未虚构按钮或操作流程。"
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
      "evidence": "与P01.F1原文完全一致，仅声明支持添加字幕，没有新增自动化或效果承诺。"
    },
    {
      "location": "shot:3/visual",
      "text": "特写店主在纸上划掉一个错字，在旁边写上正确字，作为手动改字幕的示意；叠加本镜文案。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "示意的手动修改字幕能力由P01.F2“字幕文字可以手动编辑。”支持；纸上动作明确为示意，未冒充产品操作步骤。"
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
      "evidence": "与P01.F2原文完全一致，没有扩展为自动纠错等其他能力。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "按当前duration_check，第1镜4秒包含3秒同步声画及1秒尾部停留，摆食材、擦台面提供动作内容；第2镜5秒包含4秒同步声画及1秒字幕观察；第3镜4秒包含3秒同步声画及1秒改字观察。both同拍声画无需相加，三镜内容各有作用，无明显重复或空镜凑时长；editor_notes不参与计时。"
  },
  "expression_review_passed": true
}
```

## 执行路径

estimate_duration → search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
