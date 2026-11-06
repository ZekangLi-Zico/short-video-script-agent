# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成三镜头旁白脚本，预计19秒。保留擦咖啡机、收杯子、关灯的顺序，以自然口吻分享添加字幕的做法，结尾无关注号召；全部检查通过。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 打烊后的三个画面，我这样加字幕

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 连读旁白

今天打烊，我随手拍了段收工日常。我用剪影练习版给视频加上字幕。

字幕文字能手动改，收杯子这段，我就写“杯子归位”。

最后关灯，配一句“今天收工”，这段日常就记下来了。

### 分镜 1

镜头目的：交代这次分享的日常视频和添加字幕的做法

画面：店员擦拭咖啡机，从擦蒸汽杆切到擦机身，保留收工时的日常节奏。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–4.0 秒**

旁白：今天打烊，我随手拍了段收工日常。

**第 2 拍 · 镜内 4.0–8.0 秒**

旁白：我用剪影练习版给视频加上字幕。

依据：P01/P01.F1

预计镜头时长：8.0 秒

### 分镜 2

镜头目的：用收杯子的画面说明手动编辑字幕文字

画面：店员把杯子逐个收好；画面下方出现示例字幕“杯子归位”。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–5.5 秒**

旁白：字幕文字能手动改，收杯子这段，我就写“杯子归位”。

依据：P01/P01.F2

屏幕文字：杯子归位

预计镜头时长：5.5 秒

### 分镜 3

镜头目的：给关灯画面配上字幕，自然结束分享

画面：店员按下灯的开关，店内暗下来；字幕“今天收工”随画面结束。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–5.5 秒**

旁白：最后关灯，配一句“今天收工”，这段日常就记下来了。

屏幕文字：今天收工

预计镜头时长：5.5 秒

预计总时长：19.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "e9aa0c2a2ceff2d4317d765baa8ad1c1465c7a36e585fca497cfe72a904d8514",
  "passed": true,
  "issues": [],
  "citations": [
    {
      "location": "shot:1/block:2",
      "source_id": "P01",
      "fact_id": "P01.F1",
      "quote": "剪影练习版支持为视频添加字幕。",
      "version": "2026-11-01",
      "text": "我用剪影练习版给视频加上字幕。",
      "requires_semantic_review": true
    },
    {
      "location": "shot:2/block:1",
      "source_id": "P01",
      "fact_id": "P01.F2",
      "quote": "字幕文字可以手动编辑。",
      "version": "2026-11-01",
      "text": "字幕文字能手动改，收杯子这段，我就写“杯子归位”。",
      "requires_semantic_review": true
    }
  ],
  "rules_version": "2026-11-03-v1",
  "requires_expression_review": true,
  "expression_slots": [
    {
      "location": "title",
      "text": "打烊后的三个画面，我这样加字幕"
    },
    {
      "location": "shot:1/visual",
      "text": "店员擦拭咖啡机，从擦蒸汽杆切到擦机身，保留收工时的日常节奏。"
    },
    {
      "location": "shot:1/block:1",
      "text": "今天打烊，我随手拍了段收工日常。"
    },
    {
      "location": "shot:1/block:2",
      "text": "我用剪影练习版给视频加上字幕。"
    },
    {
      "location": "shot:2/visual",
      "text": "店员把杯子逐个收好；画面下方出现示例字幕“杯子归位”。"
    },
    {
      "location": "shot:2/block:1",
      "text": "字幕文字能手动改，收杯子这段，我就写“杯子归位”。"
    },
    {
      "location": "shot:2/block:2",
      "text": "杯子归位"
    },
    {
      "location": "shot:3/visual",
      "text": "店员按下灯的开关，店内暗下来；字幕“今天收工”随画面结束。"
    },
    {
      "location": "shot:3/block:1",
      "text": "最后关灯，配一句“今天收工”，这段日常就记下来了。"
    },
    {
      "location": "shot:3/block:2",
      "text": "今天收工"
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
  "script_hash": "e9aa0c2a2ceff2d4317d765baa8ad1c1465c7a36e585fca497cfe72a904d8514",
  "request_hash": "8d525fcd9d449364d0bfe25d2d6ed99470fe85ab9aee38ceb93d952bdf5509bc",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "咖啡店打烊后的三个画面：擦咖啡机、收杯子、关灯。",
      "verdict": "met",
      "evidence": "三个分镜依次呈现擦咖啡机、收杯子和关灯，旁白以“今天打烊”明确场景。"
    },
    {
      "field": "topic",
      "requirement": "想给其他店员分享一下，我怎样用剪影练习版给这段日常视频添加字幕。",
      "verdict": "met",
      "evidence": "第1镜介绍用剪影练习版添加字幕，第2、3镜用“杯子归位”“今天收工”说明具体配字。"
    },
    {
      "field": "topic",
      "requirement": "请写成一个店员能直接念出来的旁白",
      "verdict": "met",
      "evidence": "连续旁白以第一人称完整讲述拍摄、添加字幕及配字示例，没有混入创作指令。"
    },
    {
      "field": "topic",
      "requirement": "像收工后和同事聊天。",
      "verdict": "met",
      "evidence": "“我随手拍了段收工日常”“我就写”等表达口语化，前后意思衔接清楚。"
    },
    {
      "field": "topic",
      "requirement": "画面顺序保持不变",
      "verdict": "met",
      "evidence": "第1至3镜保持擦咖啡机、收杯子、关灯的原始顺序。"
    },
    {
      "field": "topic",
      "requirement": "结尾自然结束",
      "verdict": "met",
      "evidence": "第3镜随关灯说“这段日常就记下来了”，以“今天收工”字幕收尾。"
    },
    {
      "field": "topic",
      "requirement": "不用号召关注",
      "verdict": "met",
      "evidence": "全部旁白、字幕和画面均未出现关注号召。"
    },
    {
      "field": "audience",
      "requirement": "兼职做店铺账号的店员",
      "verdict": "met",
      "evidence": "用店员熟悉的打烊工作和两条具体字幕示例分享做法，无需专业剪辑知识即可理解。"
    },
    {
      "field": "platform",
      "requirement": "抖音",
      "verdict": "met",
      "evidence": "三个生活分镜搭配简短旁白和短字幕，预计19秒，适合短视频观看。"
    },
    {
      "field": "style",
      "requirement": "随口分享，自然亲切",
      "verdict": "met",
      "evidence": "旁白从“今天打烊”讲到“最后关灯”，语意完整、口吻平实，符合同事间分享。"
    }
  ],
  "summary": "当前稿件落实了三个打烊画面的顺序、店员口语分享和自然收尾要求，字幕能力表述有资料支持。预计19秒，声画安排与节奏合理。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "打烊后的三个画面，我这样加字幕",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "标题中的添加字幕能力由P01.F1支持，三个打烊画面来自用户场景。"
    },
    {
      "location": "shot:1/visual",
      "text": "店员擦拭咖啡机，从擦蒸汽杆切到擦机身，保留收工时的日常节奏。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅描述擦拭动作与拍摄安排，不声明产品功能。"
    },
    {
      "location": "shot:1/block:1",
      "text": "今天打烊，我随手拍了段收工日常。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于用户提供场景的第一人称叙述，无产品承诺。"
    },
    {
      "location": "shot:1/block:2",
      "text": "我用剪影练习版给视频加上字幕。",
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
      "location": "shot:2/visual",
      "text": "店员把杯子逐个收好；画面下方出现示例字幕“杯子归位”。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "示例画面展示受支持的添加字幕能力，下方字幕属于成片编排而非产品界面。"
    },
    {
      "location": "shot:2/block:1",
      "text": "字幕文字能手动改，收杯子这段，我就写“杯子归位”。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "手动修改文字及填写示例均在“字幕文字可以手动编辑”的范围内。"
    },
    {
      "location": "shot:2/block:2",
      "text": "杯子归位",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅为收杯子场景的字幕内容。"
    },
    {
      "location": "shot:3/visual",
      "text": "店员按下灯的开关，店内暗下来；字幕“今天收工”随画面结束。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "仅展示资料支持的字幕叠加，随成片结束不涉及额外自动化能力。"
    },
    {
      "location": "shot:3/block:1",
      "text": "最后关灯，配一句“今天收工”，这段日常就记下来了。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "配字幕由P01.F1支持，“日常就记下来了”是记录生活的叙述，没有新增性能承诺。"
    },
    {
      "location": "shot:3/block:2",
      "text": "今天收工",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅为关灯收工场景的结束字幕。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "第1镜8秒由两段旁白和擦拭动作支撑，第2、3镜各5.5秒容纳旁白、动作及四字同步字幕；总长19秒，无重复事实或空镜凑时长。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
