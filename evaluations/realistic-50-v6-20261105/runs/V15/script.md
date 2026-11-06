# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成4镜脚本，预计27秒：以蔬菜、空餐盘和食谱本为背景，展示添加字幕与手动改字；不含营养功效或儿童正脸。全部检查通过。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 把做饭前的小准备，写进视频字幕

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

镜头目的：交代家庭料理记录场景及准备写入字幕的内容。

画面：俯拍桌面：洗好的蔬菜放在篮中，旁边是空餐盘和翻开的食谱本。成人双手将蔬菜篮移近餐盘，再指向食谱本。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–5.8 秒**

旁白＋同步字幕：菜洗好了，盘子也摆好了。先把做饭前的准备记下来。

镜头末尾保持画面：5.8–7.0 秒（保留最后一拍屏幕文字）

预计镜头时长：7.0 秒

### 分镜 2

镜头目的：展示为这段料理准备视频添加字幕。

画面：手机置于桌面，蔬菜、空餐盘和食谱本仍在背景中。录屏展示同一段素材添加字幕前后的变化，新增字幕为“今天准备做晚饭”；不特写未经核实的按钮名称。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–7.0 秒**

旁白：用剪影练习版，可以给这段视频添加字幕。

依据：P01/P01.F1

屏幕文字：今天准备做晚饭

预计镜头时长：7.0 秒

### 分镜 3

镜头目的：用具体改字示范手动编辑字幕文字。

画面：保持同一桌面背景。录屏展示成人手动将字幕“今天准备做晚饭”改为“蔬菜洗好了，准备照着食谱做晚饭”，停留查看改好的文字；不指定按钮或菜单路径。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–8.0 秒**

旁白：字幕文字可以手动编辑。

依据：P01/P01.F2

旁白：把刚才那句改具体一点，写下眼前这一步。

屏幕文字：蔬菜洗好了，准备照着食谱做晚饭

预计镜头时长：8.0 秒

### 分镜 4

镜头目的：回看带有修改后字幕的家庭料理片段。

画面：播放改好字幕的片段：成人双手翻过一页食谱，洗好的蔬菜与空餐盘保持入镜。画面始终不出现儿童正脸。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–5.0 秒**

屏幕文字：蔬菜洗好了，准备照着食谱做晚饭

预计镜头时长：5.0 秒

时长要求：27.0–30 秒（接近目标）。

预计总时长：27.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "dbb1439134d7e9cbc407d1e46c21f7b69484ac4b67e4e88f30e1805b33679953",
  "passed": true,
  "issues": [],
  "citations": [
    {
      "location": "shot:2/block:1",
      "source_id": "P01",
      "fact_id": "P01.F1",
      "quote": "剪影练习版支持为视频添加字幕。",
      "version": "2026-11-01",
      "text": "用剪影练习版，可以给这段视频添加字幕。",
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
      "text": "把做饭前的小准备，写进视频字幕"
    },
    {
      "location": "shot:1/visual",
      "text": "俯拍桌面：洗好的蔬菜放在篮中，旁边是空餐盘和翻开的食谱本。成人双手将蔬菜篮移近餐盘，再指向食谱本。"
    },
    {
      "location": "shot:1/block:1",
      "text": "菜洗好了，盘子也摆好了。先把做饭前的准备记下来。"
    },
    {
      "location": "shot:2/visual",
      "text": "手机置于桌面，蔬菜、空餐盘和食谱本仍在背景中。录屏展示同一段素材添加字幕前后的变化，新增字幕为“今天准备做晚饭”；不特写未经核实的按钮名称。"
    },
    {
      "location": "shot:2/block:1",
      "text": "用剪影练习版，可以给这段视频添加字幕。"
    },
    {
      "location": "shot:2/block:2",
      "text": "今天准备做晚饭"
    },
    {
      "location": "shot:3/visual",
      "text": "保持同一桌面背景。录屏展示成人手动将字幕“今天准备做晚饭”改为“蔬菜洗好了，准备照着食谱做晚饭”，停留查看改好的文字；不指定按钮或菜单路径。"
    },
    {
      "location": "shot:3/block:1",
      "text": "字幕文字可以手动编辑。"
    },
    {
      "location": "shot:3/block:2",
      "text": "把刚才那句改具体一点，写下眼前这一步。"
    },
    {
      "location": "shot:3/block:3",
      "text": "蔬菜洗好了，准备照着食谱做晚饭"
    },
    {
      "location": "shot:4/visual",
      "text": "播放改好字幕的片段：成人双手翻过一页食谱，洗好的蔬菜与空餐盘保持入镜。画面始终不出现儿童正脸。"
    },
    {
      "location": "shot:4/block:1",
      "text": "蔬菜洗好了，准备照着食谱做晚饭"
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
  "script_hash": "dbb1439134d7e9cbc407d1e46c21f7b69484ac4b67e4e88f30e1805b33679953",
  "request_hash": "f0cdde0bd1d754eaa019cd4f805619d55970619edd7cffce8ab94facc5e33052",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "添加字幕",
      "verdict": "met",
      "evidence": "第2镜展示添加字幕前后变化，并说明可以为视频添加字幕。"
    },
    {
      "field": "topic",
      "requirement": "手动编辑文字",
      "verdict": "met",
      "evidence": "第3镜将“今天准备做晚饭”手动改成具体的料理准备描述。"
    },
    {
      "field": "topic",
      "requirement": "以洗好的蔬菜、空餐盘和食谱本为背景",
      "verdict": "met",
      "evidence": "第1镜明确布置三项背景，第2至4镜持续保留同一桌面场景。"
    },
    {
      "field": "topic",
      "requirement": "不要代写营养功效",
      "verdict": "met",
      "evidence": "全部文案仅描述料理准备与字幕操作，没有营养功效说法。"
    },
    {
      "field": "topic",
      "requirement": "不出现儿童正脸",
      "verdict": "met",
      "evidence": "画面仅安排成人双手，第4镜进一步明确始终不出现儿童正脸。"
    },
    {
      "field": "audience",
      "requirement": "记录家庭料理的普通用户",
      "verdict": "met",
      "evidence": "以晚饭准备为实例，使用简单的添加字幕和改字演示，适合普通用户理解。"
    },
    {
      "field": "platform",
      "requirement": "小红书",
      "verdict": "met",
      "evidence": "家庭料理桌面场景搭配简短字幕演示，符合生活记录类短视频表达。"
    },
    {
      "field": "style",
      "requirement": "亲切",
      "verdict": "met",
      "evidence": "“菜洗好了，盘子也摆好了”等口语自然亲近。"
    },
    {
      "field": "style",
      "requirement": "不营销",
      "verdict": "met",
      "evidence": "仅介绍操作并回看片段，没有购买引导、夸大效果或促销话术。"
    }
  ],
  "summary": "当前稿已落实两项字幕功能、指定料理背景和内容限制，产品声明有资料支持。预计27秒，达到宿主目标区间，逐镜节奏合理。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "把做饭前的小准备，写进视频字幕",
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
      "evidence": "将料理准备文字写入字幕，由添加字幕及手动编辑文字能力支持。"
    },
    {
      "location": "shot:1/visual",
      "text": "俯拍桌面：洗好的蔬菜放在篮中，旁边是空餐盘和翻开的食谱本。成人双手将蔬菜篮移近餐盘，再指向食谱本。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅描述背景布置与成人手部动作，不含产品承诺。"
    },
    {
      "location": "shot:1/block:1",
      "text": "菜洗好了，盘子也摆好了。先把做饭前的准备记下来。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于料理场景描述和记录意图，没有产品效果声明。"
    },
    {
      "location": "shot:2/visual",
      "text": "手机置于桌面，蔬菜、空餐盘和食谱本仍在背景中。录屏展示同一段素材添加字幕前后的变化，新增字幕为“今天准备做晚饭”；不特写未经核实的按钮名称。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "展示添加字幕能力，未指定未经支持的按钮、布局或自动流程。"
    },
    {
      "location": "shot:2/block:1",
      "text": "用剪影练习版，可以给这段视频添加字幕。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "与原文支持为视频添加字幕的含义一致。"
    },
    {
      "location": "shot:2/block:2",
      "text": "今天准备做晚饭",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于料理记录的示例字幕，不涉及产品承诺。"
    },
    {
      "location": "shot:3/visual",
      "text": "保持同一桌面背景。录屏展示成人手动将字幕“今天准备做晚饭”改为“蔬菜洗好了，准备照着食谱做晚饭”，停留查看改好的文字；不指定按钮或菜单路径。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F2"
        }
      ],
      "evidence": "具体改字示范属于手动编辑字幕文字，未新增操作路径或自动化能力。"
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
      "evidence": "文案与该事实原文一致。"
    },
    {
      "location": "shot:3/block:2",
      "text": "把刚才那句改具体一点，写下眼前这一步。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于示例文字的写作指导，没有新增产品能力声明。"
    },
    {
      "location": "shot:3/block:3",
      "text": "蔬菜洗好了，准备照着食谱做晚饭",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "仅描述当前料理准备状态，不涉及营养或产品效果。"
    },
    {
      "location": "shot:4/visual",
      "text": "播放改好字幕的片段：成人双手翻过一页食谱，洗好的蔬菜与空餐盘保持入镜。画面始终不出现儿童正脸。",
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
      "evidence": "回看添加并手动修改字幕的示意成果，其余为拍摄安排，未宣称额外播放功能。"
    },
    {
      "location": "shot:4/block:1",
      "text": "蔬菜洗好了，准备照着食谱做晚饭",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "为回看片段保留的料理记录字幕，不含产品承诺。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "第1镜7秒容纳5.75秒旁白和摆放动作；第2镜7秒展示字幕前后变化；第3镜8秒容纳7.25秒旁白及改字演示；第4镜5秒用于阅读成稿和翻页回看，重复字幕有成果展示作用。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
