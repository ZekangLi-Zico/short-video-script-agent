# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成三镜字幕功能脚本，介绍添加字幕和手动编辑，估时13.5秒，符合25秒上限。未采用“播放量提高30%”或效果提升暗示，审稿备注已说明缺少统计依据和授权；后续如需使用该案例，须向项目维护者提供可核验的统计材料及公开使用授权。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 字幕，让表达被看见

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

画面：店铺运营者在柜台旁查看商品介绍口播视频，准备核对字幕，不展示具体软件界面。

旁白/字幕：店铺口播发布前，留一步检查字幕。

来源：

预计镜头时长：4.0 秒

### 分镜 2

画面：商品介绍视频作为背景，前景展示产品功能文字卡片；卡片使用本镜事实原文，旁白同步读出，不另加效果数据。

旁白/字幕：剪影练习版支持为视频添加字幕。

来源：P01/P01.F1

预计镜头时长：4.0 秒

### 分镜 3

画面：展示字幕文字校对与手动修改的示意画面，不模拟软件按钮或界面布局。运营者对照口播逐句检查；事实卡与旁白同步呈现。

旁白/字幕：字幕文字可以手动编辑。对照口播，核对字幕内容。

来源：P01/P01.F2

预计镜头时长：5.5 秒

## 审稿备注（不进入视频，不计入时长）

供创作者核对修改与资料缺口，不是经过事实认证的产品介绍。

客户口头反馈“加字幕后播放量提高了30%”尚无统计表和公开使用授权，未确认其统计口径或因果关系。本稿不将该数字或播放量提升暗示用于标题、画面、字幕及旁白，仅介绍添加字幕和手动编辑文字。后续如需使用客户案例，需向项目维护者提供可核验的统计材料及公开使用授权，再审核可用表述。事实卡与同步旁白为同一段内容，不重复计文案；镜头停留以实际估时及剪辑复核为准。

预计总时长：13.5 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "6bee16ed93232937d919b38330c5f1ea31f9330c04f51a1d7fb1dfd1ac504c69",
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
      "text": "字幕，让表达被看见"
    },
    {
      "location": "shot:1/visual",
      "text": "店铺运营者在柜台旁查看商品介绍口播视频，准备核对字幕，不展示具体软件界面。"
    },
    {
      "location": "shot:1/block:1",
      "text": "店铺口播发布前，留一步检查字幕。"
    },
    {
      "location": "shot:2/visual",
      "text": "商品介绍视频作为背景，前景展示产品功能文字卡片；卡片使用本镜事实原文，旁白同步读出，不另加效果数据。"
    },
    {
      "location": "shot:3/visual",
      "text": "展示字幕文字校对与手动修改的示意画面，不模拟软件按钮或界面布局。运营者对照口播逐句检查；事实卡与旁白同步呈现。"
    },
    {
      "location": "shot:3/block:2",
      "text": "对照口播，核对字幕内容。"
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
  "script_hash": "6bee16ed93232937d919b38330c5f1ea31f9330c04f51a1d7fb1dfd1ac504c69",
  "request_hash": "93972873cc931936e79f564ca370d65259052b284f9983eeaaba7d87a79a6a9d",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "请写一条介绍字幕功能的脚本",
      "verdict": "met",
      "evidence": "第2镜介绍“剪影练习版支持为视频添加字幕。”，第3镜介绍“字幕文字可以手动编辑。”；两项均有已核对的资料支持。"
    },
    {
      "field": "topic",
      "requirement": "处理这个说法",
      "verdict": "met",
      "evidence": "editor_notes明确说明30%反馈缺少统计表和公开使用授权，统计口径及因果关系未确认；标题及三镜面向观众的内容确实均未采用该数字或播放量提升说法，备注与实际处理一致。"
    },
    {
      "field": "topic",
      "requirement": "不要把口头反馈包装成已验证效果",
      "verdict": "met",
      "evidence": "全部旁白仅介绍添加字幕、手动编辑和核对字幕，没有客户背书、30%数据或播放量提升承诺。标题“字幕，让表达被看见”属于修辞，没有将口头反馈呈现为验证结果。"
    },
    {
      "field": "audience",
      "requirement": "店铺内容运营",
      "verdict": "met",
      "evidence": "第1镜明确呈现店铺运营者在柜台旁查看商品介绍口播视频，旁白为“店铺口播发布前，留一步检查字幕。”，贴合店铺内容发布工作。"
    },
    {
      "field": "platform",
      "requirement": "抖音",
      "verdict": "met",
      "evidence": "三镜围绕一个功能主题，以店铺场景、简短事实卡和操作示意推进；旁白简洁，宿主估时13.5秒，适合短视频观看。"
    },
    {
      "field": "style",
      "requirement": "可信",
      "verdict": "met",
      "evidence": "第2、3镜的产品能力分别获P01.F1、P01.F2支持；未采用未经核实的客户效果数据，画面明确不虚构软件按钮或界面布局。"
    },
    {
      "field": "style",
      "requirement": "少口号",
      "verdict": "met",
      "evidence": "标题有一句修辞表达，正文均为具体功能介绍或字幕检查建议，没有连续口号或夸张效果宣传。"
    }
  ],
  "summary": "需求已落实。字幕功能介绍有资料支持，30%口头反馈已从观众内容中排除并在审稿备注中准确说明；店铺场景、表达风格和镜头节奏均适配。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "字幕，让表达被看见",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于字幕主题的修辞表达，没有声称增加曝光、播放量或其他可验证的产品效果。"
    },
    {
      "location": "shot:1/visual",
      "text": "店铺运营者在柜台旁查看商品介绍口播视频，准备核对字幕，不展示具体软件界面。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "描述店铺生活场景和人工检查准备，没有真实客户背书或具体产品操作声明。"
    },
    {
      "location": "shot:1/block:1",
      "text": "店铺口播发布前，留一步检查字幕。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于发布前检查字幕的行动建议，没有承诺产品能力或业务效果。"
    },
    {
      "location": "shot:2/visual",
      "text": "商品介绍视频作为背景，前景展示产品功能文字卡片；卡片使用本镜事实原文，旁白同步读出，不另加效果数据。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于背景、文字卡和旁白同步的拍摄安排，没有新增能力或效果声明；卡片引用的本镜正文已由宿主核对。"
    },
    {
      "location": "shot:3/visual",
      "text": "展示字幕文字校对与手动修改的示意画面，不模拟软件按钮或界面布局。运营者对照口播逐句检查；事实卡与旁白同步呈现。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "手动修改字幕文字由“字幕文字可以手动编辑。”支持；校对明确由运营者人工完成，没有暗示自动校对，也未虚构按钮、界面或操作流程。"
    },
    {
      "location": "shot:3/block:2",
      "text": "对照口播，核对字幕内容。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于人工核对字幕的行动建议，没有产品自动化或效果承诺。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "第1镜预计4.0秒，承载14个旁白单位和查看口播的场景；第2镜4.0秒，承载14个旁白单位及一条同步事实卡；第3镜5.5秒，承载20个旁白单位和人工核对、手动修改的简短示意。各镜均有明确内容支撑，无重复事实或空镜凑时长。hold_seconds为0仅表示没有额外最低停留；editor_notes不计入播放。宿主总估时13.5秒，已通过25秒上限判定。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
