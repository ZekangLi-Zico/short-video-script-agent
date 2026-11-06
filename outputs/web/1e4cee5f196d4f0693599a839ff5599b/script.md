# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成三镜脚本《字幕，让表达被看见》，预计16秒。按蒸笼→手写菜单→打包台展开，只介绍添加字幕，不出现顾客正脸。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 字幕，让表达被看见

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

镜头目的：用今日备料口播配合同句字幕，展示字幕在早餐摊视频中的使用场景。

画面：近拍蒸笼，摊主双手把包子逐个摆入笼屉，再盖上笼盖。摊主边操作边说，下方同步出现同句字幕。仅拍手、蒸笼和食物。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–3.5 秒**

旁白＋同步字幕：今天备料，先把包子摆进蒸笼。

镜头末尾保持画面：3.5–5.0 秒（保留最后一拍屏幕文字）

预计镜头时长：5.0 秒

### 分镜 2

镜头目的：接续备料记录，明确剪影练习版可以给视频添加字幕。

画面：切到手写菜单的俯拍，摊主把菜单摆正，用笔在包子一项旁打勾。功能介绍随摊主口播显示为底部字幕，避开菜单内容。只拍手和菜单。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–4.5 秒**

旁白＋同步字幕：给这段视频加字幕，可以用剪影练习版。

依据：P01/P01.F1

镜头末尾保持画面：4.5–6.0 秒（保留最后一拍屏幕文字）

预计镜头时长：6.0 秒

### 分镜 3

镜头目的：以打包台准备完成收束备料过程，继续展示口播与字幕同步的样子。

画面：切到打包台近景，摊主整理一叠打包袋，再把袋口撑开摆好。备料口播同步显示为底部字幕，最后停在整理好的台面。画面不出现顾客。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–3.3 秒**

旁白＋同步字幕：打包袋也备好了，准备开摊。

镜头末尾保持画面：3.3–5.0 秒（保留最后一拍屏幕文字）

预计镜头时长：5.0 秒

预计总时长：16.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "54dd7bc8eec82a4310ec7cdc8a6d4f82be0d5b6680eb9af4a974e51a5d5219fd",
  "passed": true,
  "issues": [],
  "citations": [
    {
      "location": "shot:2/block:1",
      "source_id": "P01",
      "fact_id": "P01.F1",
      "quote": "剪影练习版支持为视频添加字幕。",
      "version": "2026-11-01",
      "text": "给这段视频加字幕，可以用剪影练习版。",
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
      "text": "近拍蒸笼，摊主双手把包子逐个摆入笼屉，再盖上笼盖。摊主边操作边说，下方同步出现同句字幕。仅拍手、蒸笼和食物。"
    },
    {
      "location": "shot:1/block:1",
      "text": "今天备料，先把包子摆进蒸笼。"
    },
    {
      "location": "shot:2/visual",
      "text": "切到手写菜单的俯拍，摊主把菜单摆正，用笔在包子一项旁打勾。功能介绍随摊主口播显示为底部字幕，避开菜单内容。只拍手和菜单。"
    },
    {
      "location": "shot:2/block:1",
      "text": "给这段视频加字幕，可以用剪影练习版。"
    },
    {
      "location": "shot:3/visual",
      "text": "切到打包台近景，摊主整理一叠打包袋，再把袋口撑开摆好。备料口播同步显示为底部字幕，最后停在整理好的台面。画面不出现顾客。"
    },
    {
      "location": "shot:3/block:1",
      "text": "打包袋也备好了，准备开摊。"
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
  "script_hash": "54dd7bc8eec82a4310ec7cdc8a6d4f82be0d5b6680eb9af4a974e51a5d5219fd",
  "request_hash": "4299792130470435332510610b8526e5f391e330ac68588a7ba5d1498ead5ad2",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "做一条剪影练习版字幕功能介绍",
      "verdict": "met",
      "evidence": "第2镜明确说“给这段视频加字幕，可以用剪影练习版。”三镜均展示口播对应字幕。"
    },
    {
      "field": "topic",
      "requirement": "背景是早餐摊主讲今日备料",
      "verdict": "met",
      "evidence": "第1镜摊主摆包子并说“今天备料，先把包子摆进蒸笼。”第3镜整理打包袋并说“打包袋也备好了，准备开摊。”场景具体落实。"
    },
    {
      "field": "topic",
      "requirement": "只介绍添加字幕",
      "verdict": "met",
      "evidence": "唯一明确介绍的产品功能是第2镜的“给这段视频加字幕”；其余镜头展示备料和成片字幕，未介绍手动编辑字幕、裁剪视频或其他功能。"
    },
    {
      "field": "topic",
      "requirement": "画面按蒸笼、手写菜单、打包台的顺序",
      "verdict": "met",
      "evidence": "第1镜“近拍蒸笼”，第2镜“切到手写菜单的俯拍”，第3镜“切到打包台近景”，顺序一致。"
    },
    {
      "field": "topic",
      "requirement": "不要出现顾客正脸",
      "verdict": "met",
      "evidence": "第1镜“仅拍手、蒸笼和食物”，第2镜“只拍手和菜单”，第3镜明确“画面不出现顾客”。"
    },
    {
      "field": "audience",
      "requirement": "小店新媒体兼职",
      "verdict": "met",
      "evidence": "用早餐摊备料这一小店内容场景演示字幕，功能说明直白，拍摄安排以手部和台面近景为主，适合兼职内容制作者理解和参考。"
    },
    {
      "field": "platform",
      "requirement": "抖音",
      "verdict": "met",
      "evidence": "三镜围绕单一功能展开，口播与字幕同步，具有具体操作画面；宿主估算总长16秒，适合短视频观看。"
    },
    {
      "field": "style",
      "requirement": "像同事分享经验",
      "verdict": "met",
      "evidence": "“给这段视频加字幕，可以用剪影练习版。”采用日常建议语气，结合摊主备料口吻，没有夸张推销。"
    },
    {
      "field": "style",
      "requirement": "短句",
      "verdict": "met",
      "evidence": "每镜仅一句文案，如“打包袋也备好了，准备开摊。”句式简短，表达直接。"
    }
  ],
  "summary": "全部明确需求均已落实：只介绍添加字幕，早餐摊备料场景具体，镜头顺序正确且避开顾客正脸。产品声明有来源支持，预计16秒，节奏合理。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "字幕，让表达被看见",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于字幕主题的修辞表达，未承诺播放量、传播效果或额外产品能力。"
    },
    {
      "location": "shot:1/visual",
      "text": "近拍蒸笼，摊主双手把包子逐个摆入笼屉，再盖上笼盖。摊主边操作边说，下方同步出现同句字幕。仅拍手、蒸笼和食物。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "描述备料动作、取景范围及成片声画编排；字幕同步呈现没有被描述为产品自动识别或自动生成流程。"
    },
    {
      "location": "shot:1/block:1",
      "text": "今天备料，先把包子摆进蒸笼。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "早餐摊主的场景口播，不含产品能力或效果承诺。"
    },
    {
      "location": "shot:2/visual",
      "text": "切到手写菜单的俯拍，摊主把菜单摆正，用笔在包子一项旁打勾。功能介绍随摊主口播显示为底部字幕，避开菜单内容。只拍手和菜单。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "描述菜单动作、字幕排版和取景安排，没有虚构产品按钮、界面布局或自动避让文字的能力。"
    },
    {
      "location": "shot:2/block:1",
      "text": "给这段视频加字幕，可以用剪影练习版。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "原文“剪影练习版支持为视频添加字幕。”完整支持该改写；引用与原块一致，没有增加自动化、效率或其他功能声明。"
    },
    {
      "location": "shot:3/visual",
      "text": "切到打包台近景，摊主整理一叠打包袋，再把袋口撑开摆好。备料口播同步显示为底部字幕，最后停在整理好的台面。画面不出现顾客。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于打包台动作、字幕呈现和结尾停留的拍摄安排，没有声称产品自动完成字幕或其他操作。"
    },
    {
      "location": "shot:3/block:1",
      "text": "打包袋也备好了，准备开摊。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "交代备料进度并结束场景，不含产品承诺。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "第1镜预计5秒，同步声画占3.5秒，余下1.5秒可展示摆包子和盖笼；第2镜预计6秒，同步声画占4.5秒，余下1.5秒有摆正菜单、打勾及观察内容支撑；第3镜预计5秒，同步声画占3.3秒，余下1.7秒可展示撑袋和整理好的台面。三镜动作不同，无重复事实或明显空镜凑时长；总长16秒，宿主已判定通过25秒上限。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
