# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成4镜脚本，预计38秒。用手写练习本和手机背面讲解字幕添加、手动改字，适合长者初学者；全部检查已通过。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 跟着练习本认识字幕：添加文字，再手动改字

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

镜头目的：用手写句子说明字幕是什么，建立长者熟悉的理解方式。

画面：俯拍桌面，手机背面朝上放在手写练习本旁。手指沿着本上的“今天去公园散步”缓慢移动，再指向旁边手写的“字幕”二字。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–6.3 秒**

旁白：视频里配上的文字，就是字幕。我们先用练习本，看个例子。

镜头末尾保持画面：6.3–8.0 秒（保留最后一拍屏幕文字）

预计镜头时长：8.0 秒

### 分镜 2

镜头目的：介绍添加字幕的能力，并明确练习本只是文字示意。

画面：保持手机背面朝上。翻开练习本，露出手绘的视频方框，把写着“今天去公园散步”的纸条放在方框下方，停留供学员观察。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–4.0 秒**

旁白：剪影练习版可以给视频添加字幕。

依据：P01/P01.F1

**第 2 拍 · 镜内 4.0–9.3 秒**

旁白：本子上只是示意：让这句话，陪着画面一起出现。

镜头末尾保持画面：9.3–10.0 秒（保留最后一拍屏幕文字）

预计镜头时长：10.0 秒

### 分镜 3

镜头目的：说明字幕可以手动改字，用纸上纠错呈现改字前后的区别。

画面：翻到写着“今天去公圆散步”的一页。用笔圈出“圆”，在下方写出“园”，再写一遍完整的正确句子。手机始终只露背面。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–3.0 秒**

旁白：字幕文字可以手动修改。

依据：P01/P01.F2

**第 2 拍 · 镜内 3.0–9.8 秒**

旁白：比如这里写错了。公园的“园”，应该是这个字。我们在纸上练一遍。

镜头末尾保持画面：9.8–11.0 秒（保留最后一拍屏幕文字）

预计镜头时长：11.0 秒

### 分镜 4

镜头目的：通过逐字核对收束练习，帮助初学者记住添加后还要检查文字。

画面：镜头靠近练习本上改好的“今天去公园散步”。手指逐字点过，最后在句子旁画一个勾。画面保留手机背面与完整句子。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–8.3 秒**

旁白：文字加好后，再慢慢读一遍。看看有没有错字。今天先记住：添加字幕，手动改字。

镜头末尾保持画面：8.3–9.0 秒（保留最后一拍屏幕文字）

预计镜头时长：9.0 秒

时长要求：36.0–40 秒（接近目标）。

预计总时长：38.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "2f7a96b0b254f6aae0a73323ccb4198e6cdb61738079cc0169d11d4f55c91767",
  "passed": true,
  "issues": [],
  "citations": [
    {
      "location": "shot:2/block:1",
      "source_id": "P01",
      "fact_id": "P01.F1",
      "quote": "剪影练习版支持为视频添加字幕。",
      "version": "2026-11-01",
      "text": "剪影练习版可以给视频添加字幕。",
      "requires_semantic_review": true
    },
    {
      "location": "shot:3/block:1",
      "source_id": "P01",
      "fact_id": "P01.F2",
      "quote": "字幕文字可以手动编辑。",
      "version": "2026-11-01",
      "text": "字幕文字可以手动修改。",
      "requires_semantic_review": true
    }
  ],
  "rules_version": "2026-11-03-v1",
  "requires_expression_review": true,
  "expression_slots": [
    {
      "location": "title",
      "text": "跟着练习本认识字幕：添加文字，再手动改字"
    },
    {
      "location": "shot:1/visual",
      "text": "俯拍桌面，手机背面朝上放在手写练习本旁。手指沿着本上的“今天去公园散步”缓慢移动，再指向旁边手写的“字幕”二字。"
    },
    {
      "location": "shot:1/block:1",
      "text": "视频里配上的文字，就是字幕。我们先用练习本，看个例子。"
    },
    {
      "location": "shot:2/visual",
      "text": "保持手机背面朝上。翻开练习本，露出手绘的视频方框，把写着“今天去公园散步”的纸条放在方框下方，停留供学员观察。"
    },
    {
      "location": "shot:2/block:1",
      "text": "剪影练习版可以给视频添加字幕。"
    },
    {
      "location": "shot:2/block:2",
      "text": "本子上只是示意：让这句话，陪着画面一起出现。"
    },
    {
      "location": "shot:3/visual",
      "text": "翻到写着“今天去公圆散步”的一页。用笔圈出“圆”，在下方写出“园”，再写一遍完整的正确句子。手机始终只露背面。"
    },
    {
      "location": "shot:3/block:1",
      "text": "字幕文字可以手动修改。"
    },
    {
      "location": "shot:3/block:2",
      "text": "比如这里写错了。公园的“园”，应该是这个字。我们在纸上练一遍。"
    },
    {
      "location": "shot:4/visual",
      "text": "镜头靠近练习本上改好的“今天去公园散步”。手指逐字点过，最后在句子旁画一个勾。画面保留手机背面与完整句子。"
    },
    {
      "location": "shot:4/block:1",
      "text": "文字加好后，再慢慢读一遍。看看有没有错字。今天先记住：添加字幕，手动改字。"
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
  "script_hash": "2f7a96b0b254f6aae0a73323ccb4198e6cdb61738079cc0169d11d4f55c91767",
  "request_hash": "5d5f844deb8a130965b069c67d1de997138a045e7ec49210ef6cb066698c7050",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "介绍字幕添加与手动改字",
      "verdict": "met",
      "evidence": "第2镜介绍添加字幕，第3镜介绍手动修改，并用纸上改错字示意。"
    },
    {
      "field": "topic",
      "requirement": "给第一次剪视频的长者看",
      "verdict": "met",
      "evidence": "第1镜先解释字幕，第3镜以“圆”改为“园”的熟悉例子辅助理解。"
    },
    {
      "field": "topic",
      "requirement": "用手写练习本和手机背面作画面",
      "verdict": "met",
      "evidence": "四镜均使用手写练习本，手机始终背面朝上或只露背面。"
    },
    {
      "field": "topic",
      "requirement": "不假设能一键自动完成",
      "verdict": "met",
      "evidence": "第3镜明确“字幕文字可以手动修改”，全稿没有一键或自动完成的说法。"
    },
    {
      "field": "topic",
      "requirement": "避免年轻人网络用语",
      "verdict": "met",
      "evidence": "旁白使用“看个例子”“慢慢读一遍”等日常表达，无网络用语。"
    },
    {
      "field": "audience",
      "requirement": "社区手机课堂学员",
      "verdict": "met",
      "evidence": "练习本示意、纸上纠错和逐字核对适合社区课堂初学者跟随理解。"
    },
    {
      "field": "platform",
      "requirement": "视频号",
      "verdict": "met",
      "evidence": "四镜围绕单一教学主题展开，38秒的直观演示适合短视频观看。"
    },
    {
      "field": "style",
      "requirement": "耐心",
      "verdict": "met",
      "evidence": "第1镜手指缓慢移动，第4镜提示“再慢慢读一遍”，留有观察时间。"
    },
    {
      "field": "style",
      "requirement": "短句",
      "verdict": "met",
      "evidence": "使用“比如这里写错了”“看看有没有错字”等短句分步讲解。"
    },
    {
      "field": "style",
      "requirement": "无术语",
      "verdict": "met",
      "evidence": "除主题所需且已解释的“字幕”外，没有剪辑专业术语。"
    }
  ],
  "summary": "当前稿已落实各项需求，字幕添加和手动改字的表述均有资料支持。预计38秒，符合目标区间，画面动作与讲解节奏合理。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "跟着练习本认识字幕：添加文字，再手动改字",
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
      "evidence": "标题所述字幕添加与手动改字均由两条资料支持。"
    },
    {
      "location": "shot:1/visual",
      "text": "俯拍桌面，手机背面朝上放在手写练习本旁。手指沿着本上的“今天去公园散步”缓慢移动，再指向旁边手写的“字幕”二字。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅安排练习本、手机背面及指读动作，没有产品操作或效果承诺。"
    },
    {
      "location": "shot:1/block:1",
      "text": "视频里配上的文字，就是字幕。我们先用练习本，看个例子。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "为字幕的通俗解释和教学引导，不新增产品能力。"
    },
    {
      "location": "shot:2/visual",
      "text": "保持手机背面朝上。翻开练习本，露出手绘的视频方框，把写着“今天去公园散步”的纸条放在方框下方，停留供学员观察。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "纸条与手绘方框属于教学道具安排，没有虚构产品界面或操作步骤。"
    },
    {
      "location": "shot:2/block:1",
      "text": "剪影练习版可以给视频添加字幕。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "与原文“支持为视频添加字幕”含义一致。"
    },
    {
      "location": "shot:2/block:2",
      "text": "本子上只是示意：让这句话，陪着画面一起出现。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "描述添加字幕后文字伴随画面出现，未扩展到自动生成或同步能力。"
    },
    {
      "location": "shot:3/visual",
      "text": "翻到写着“今天去公圆散步”的一页。用笔圈出“圆”，在下方写出“园”，再写一遍完整的正确句子。手机始终只露背面。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "为纸上纠错的拍摄安排，不冒充软件实际操作流程。"
    },
    {
      "location": "shot:3/block:1",
      "text": "字幕文字可以手动修改。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "“手动修改”是原文“手动编辑”的准确改写。"
    },
    {
      "location": "shot:3/block:2",
      "text": "比如这里写错了。公园的“园”，应该是这个字。我们在纸上练一遍。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅解释示例错字并邀请纸上练习，没有产品承诺。"
    },
    {
      "location": "shot:4/visual",
      "text": "镜头靠近练习本上改好的“今天去公园散步”。手指逐字点过，最后在句子旁画一个勾。画面保留手机背面与完整句子。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "为人工核对文字的画面安排，没有声称产品自动检查。"
    },
    {
      "location": "shot:4/block:1",
      "text": "文字加好后，再慢慢读一遍。看看有没有错字。今天先记住：添加字幕，手动改字。",
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
      "evidence": "功能回顾由两条资料支持，读一遍检查错字属于人工练习建议。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "四镜预计8、10、11、9秒，分别有指读、摆纸条、圈错字并重写、逐字核对支撑停留；各镜旁白节拍均在镜头时长内，结尾回顾结合检查动作，没有明显空镜凑时。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
