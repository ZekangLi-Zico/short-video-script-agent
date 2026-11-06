# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成4镜脚本，预计37秒。以手写练习本和手机背面展示字幕添加与手动改字，旁白耐心易懂，符合长者课堂需求，全部检查通过。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 手机课堂：给视频加字幕，写错的字手动改

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 连读旁白

现在一起给视频配上文字。先在练习本上，写下视频里要说的一句话。

剪影练习版可以给视频添加字幕。比如这句：“今天，我来学做一道菜。”

如果字幕里有字写错了，可以手动修改。我们在本子上练一练：圈出错字，写上正确的字。

改好后，再读一遍，看看是不是自己想说的话。今天先练好一句，不着急。

### 分镜 1

镜头目的：先用练习本准备一句字幕

画面：俯拍桌面，手机背面朝上放在练习本旁。手翻开本子，慢慢写下“今天，我来学做一道菜。”

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–7.5 秒**

旁白：现在一起给视频配上文字。先在练习本上，写下视频里要说的一句话。

镜头末尾保持画面：7.5–9.0 秒（保留最后一拍屏幕文字）

预计镜头时长：9.0 秒

### 分镜 2

镜头目的：说明可以添加字幕，并给出生活例句

画面：镜头靠近练习本，手指沿着刚写好的句子缓慢移动。手机保持背面朝上，不展示操作界面。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–4.0 秒**

旁白：剪影练习版可以给视频添加字幕。

依据：P01/P01.F1

**第 2 拍 · 镜内 4.0–7.8 秒**

旁白：比如这句：“今天，我来学做一道菜。”

镜头末尾保持画面：7.8–9.0 秒（保留最后一拍屏幕文字）

预计镜头时长：9.0 秒

### 分镜 3

镜头目的：说明字幕可手动改字，用纸笔演示纠错思路

画面：练习本另一行预先写着“今天，我来学做一道莱。”手圈出“莱”，在旁边写下正确的“菜”。手机背面留在画面中。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–4.5 秒**

旁白：如果字幕里有字写错了，可以手动修改。

依据：P01/P01.F2

**第 2 拍 · 镜内 4.5–9.8 秒**

旁白：我们在本子上练一练：圈出错字，写上正确的字。

镜头末尾保持画面：9.8–10.0 秒（保留最后一拍屏幕文字）

预计镜头时长：10.0 秒

### 分镜 4

镜头目的：通过复读收尾，鼓励一次练好一句

画面：手在练习本下方重新写好完整的正确句子，逐字指读后画一个勾。最后停在正确句子与手机背面的同框画面。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–7.5 秒**

旁白：改好后，再读一遍，看看是不是自己想说的话。今天先练好一句，不着急。

镜头末尾保持画面：7.5–9.0 秒（保留最后一拍屏幕文字）

预计镜头时长：9.0 秒

时长要求：36.0–40 秒（接近目标）。

预计总时长：37.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "588f71a761e1c7c1daf3b5a3f80de6036a20da8adee80a2682426218c8fc2978",
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
      "text": "如果字幕里有字写错了，可以手动修改。",
      "requires_semantic_review": true
    }
  ],
  "rules_version": "2026-11-03-v1",
  "requires_expression_review": true,
  "expression_slots": [
    {
      "location": "title",
      "text": "手机课堂：给视频加字幕，写错的字手动改"
    },
    {
      "location": "shot:1/visual",
      "text": "俯拍桌面，手机背面朝上放在练习本旁。手翻开本子，慢慢写下“今天，我来学做一道菜。”"
    },
    {
      "location": "shot:1/block:1",
      "text": "现在一起给视频配上文字。先在练习本上，写下视频里要说的一句话。"
    },
    {
      "location": "shot:2/visual",
      "text": "镜头靠近练习本，手指沿着刚写好的句子缓慢移动。手机保持背面朝上，不展示操作界面。"
    },
    {
      "location": "shot:2/block:1",
      "text": "剪影练习版可以给视频添加字幕。"
    },
    {
      "location": "shot:2/block:2",
      "text": "比如这句：“今天，我来学做一道菜。”"
    },
    {
      "location": "shot:3/visual",
      "text": "练习本另一行预先写着“今天，我来学做一道莱。”手圈出“莱”，在旁边写下正确的“菜”。手机背面留在画面中。"
    },
    {
      "location": "shot:3/block:1",
      "text": "如果字幕里有字写错了，可以手动修改。"
    },
    {
      "location": "shot:3/block:2",
      "text": "我们在本子上练一练：圈出错字，写上正确的字。"
    },
    {
      "location": "shot:4/visual",
      "text": "手在练习本下方重新写好完整的正确句子，逐字指读后画一个勾。最后停在正确句子与手机背面的同框画面。"
    },
    {
      "location": "shot:4/block:1",
      "text": "改好后，再读一遍，看看是不是自己想说的话。今天先练好一句，不着急。"
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
  "script_hash": "588f71a761e1c7c1daf3b5a3f80de6036a20da8adee80a2682426218c8fc2978",
  "request_hash": "5d5f844deb8a130965b069c67d1de997138a045e7ec49210ef6cb066698c7050",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "字幕添加",
      "verdict": "met",
      "evidence": "第2镜明确介绍“剪影练习版可以给视频添加字幕”，并给出一句字幕示例。"
    },
    {
      "field": "topic",
      "requirement": "手动改字",
      "verdict": "met",
      "evidence": "第3镜说明字幕可手动修改，并用练习本演示将“莱”改为“菜”。"
    },
    {
      "field": "topic",
      "requirement": "给第一次剪视频的长者看",
      "verdict": "met",
      "evidence": "连续旁白按写一句话、介绍字幕、改错字、复读的顺序展开，以纸笔示例帮助初学者理解。"
    },
    {
      "field": "topic",
      "requirement": "用手写练习本和手机背面作画面",
      "verdict": "met",
      "evidence": "四镜均围绕练习本手写内容展开，手机保持背面入画，没有展示产品操作界面。"
    },
    {
      "field": "topic",
      "requirement": "不假设能一键自动完成",
      "verdict": "met",
      "evidence": "第3镜明确说“可以手动修改”，全稿没有一键或自动完成的承诺。"
    },
    {
      "field": "topic",
      "requirement": "避免年轻人网络用语",
      "verdict": "met",
      "evidence": "旁白使用“写下”“圈出错字”“再读一遍”等日常表达，没有网络用语。"
    },
    {
      "field": "audience",
      "requirement": "社区手机课堂学员",
      "verdict": "met",
      "evidence": "练习本、手机和“一起”“练一练”的引导形成课堂练习情境，声画衔接清楚。"
    },
    {
      "field": "platform",
      "requirement": "视频号",
      "verdict": "met",
      "evidence": "四镜围绕一个学习主题展开，预计37秒，生活化画面和简明旁白适合短视频呈现。"
    },
    {
      "field": "style",
      "requirement": "耐心",
      "verdict": "met",
      "evidence": "第4镜以“今天先练好一句，不着急”收尾，画面安排缓慢指读和复读。"
    },
    {
      "field": "style",
      "requirement": "短句",
      "verdict": "met",
      "evidence": "旁白按单个动作分句，如“圈出错字，写上正确的字”，连续听读意思完整。"
    },
    {
      "field": "style",
      "requirement": "无术语",
      "verdict": "met",
      "evidence": "除主题所需的“字幕”外，均以配文字、改字等通俗表达说明，没有专业剪辑术语。"
    }
  ],
  "summary": "当前稿落实了字幕添加、手动改字及长者课堂的表达要求，公开能力声明均有资料支持。预计37秒，符合宿主给出的目标区间，镜头停留有相应练习动作支撑。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "手机课堂：给视频加字幕，写错的字手动改",
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
      "evidence": "添加字幕和手动改字分别由两条资料支持，未新增能力。"
    },
    {
      "location": "shot:1/visual",
      "text": "俯拍桌面，手机背面朝上放在练习本旁。手翻开本子，慢慢写下“今天，我来学做一道菜。”",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于纸笔练习的拍摄安排，没有产品操作或效果声明。"
    },
    {
      "location": "shot:1/block:1",
      "text": "现在一起给视频配上文字。先在练习本上，写下视频里要说的一句话。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于学习邀请和纸笔准备步骤，没有额外产品承诺。"
    },
    {
      "location": "shot:2/visual",
      "text": "镜头靠近练习本，手指沿着刚写好的句子缓慢移动。手机保持背面朝上，不展示操作界面。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅安排观察和指读，没有虚构产品界面或操作步骤。"
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
      "text": "比如这句：“今天，我来学做一道菜。”",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于字幕内容示例，不声明产品能力。"
    },
    {
      "location": "shot:3/visual",
      "text": "练习本另一行预先写着“今天，我来学做一道莱。”手圈出“莱”，在旁边写下正确的“菜”。手机背面留在画面中。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "明确用纸笔演示纠错，没有暗示产品自动识别或纠错。"
    },
    {
      "location": "shot:3/block:1",
      "text": "如果字幕里有字写错了，可以手动修改。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "原文“字幕文字可以手动编辑”支持手动修改错字。"
    },
    {
      "location": "shot:3/block:2",
      "text": "我们在本子上练一练：圈出错字，写上正确的字。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "明确限定为本子上的练习，不是产品操作说明。"
    },
    {
      "location": "shot:4/visual",
      "text": "手在练习本下方重新写好完整的正确句子，逐字指读后画一个勾。最后停在正确句子与手机背面的同框画面。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于复写、指读及收尾构图，不包含产品效果承诺。"
    },
    {
      "location": "shot:4/block:1",
      "text": "改好后，再读一遍，看看是不是自己想说的话。今天先练好一句，不着急。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于复核建议和鼓励，承接上一镜的纸笔改字练习。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "四镜预计9、9、10、9秒，分别由书写、指读、纠错、复写复读支撑；旁白节拍均落在镜头时长内，重复例句承担示范与复核作用，没有明显空镜凑时长。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
