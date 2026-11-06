# 短视频脚本运行结果

- 状态：`completed`
- 证据类型：`real_model`
- 说明：已完成3镜脚本，预计18秒。保留擦净的黑板、课程讲义和空座位场景，仅介绍字幕添加；已删除超出范围的手动编辑演示。

当前稿已通过来源、规则和预计时长检查，模型需求核对未发现遗漏；仍为可编辑脚本，未生成或发布视频。

## 字幕，让表达被看见

> 未完成或检查失败时，下列内容仅为未通过验收的草稿。

### 分镜 1

镜头目的：建立课程结束后的场景，引出课程片尾字幕。

画面：固定机位拍摄擦净的黑板和前排空座位。助教将课程讲义放到桌上，翻开片尾内容所在页，标题缓慢显现。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–4.0 秒**

屏幕文字：字幕，让表达被看见

预计镜头时长：4.0 秒

### 分镜 2

镜头目的：通过课程片尾画面出现字幕，展示字幕添加的用途。

画面：切至电脑预览画面特写，只拍视频区域。视频里是同一间教室的黑板与空座位，底部出现课程结束语字幕；讲义的一角留在电脑旁。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–7.0 秒**

旁白：剪影练习版支持为视频添加字幕。

依据：P01/P01.F1

屏幕文字：本节课到这里结束。

预计镜头时长：7.0 秒

### 分镜 3

镜头目的：通过助教对照讲义核看结束语，展示添加字幕后的课程片尾。

画面：过肩拍摄，课程讲义与电脑预览同时入镜。助教指尖沿讲义上的结束语移动，再指向屏幕上的同一句字幕，核看后合上讲义。电脑画面保留擦净的黑板、空座位和上一镜的字幕，文字不变。

同拍同步，不同拍依次播放。

**第 1 拍 · 镜内 0–7.0 秒**

屏幕文字：本节课到这里结束。

预计镜头时长：7.0 秒

## 审稿备注（不进入视频，不计入时长）

供创作者核对修改与资料缺口，不是经过事实认证的产品介绍。

已删除第3镜的手动编辑旁白、键盘输入和字幕改写演示，因其超出仅介绍字幕添加的范围；改为对照讲义核看添加后的字幕。标题及前两镜保持不变。

## 实际修订

位置按镜头索引比较；日志关联的是实际反馈，不证明模型因果推理。

- 修改：editor_notes, shot:3/visual, shot:3/purpose, shot:3/block:1, shot:3/block:2；保留原镜头 2 个、原文案块 3 个。
- 修订前失败检查：requirements_check

时长要求：18.0–20 秒（接近目标）。

预计总时长：18.0 秒（基于语速与镜头停留估算，非成片实测）。

## 检查结果与来源

```json
{
  "ok": true,
  "script_hash": "972e3719a3a834dee4db7d381d70d83623fd4c0e1627e419d7228a4df79fa8f2",
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
      "text": "固定机位拍摄擦净的黑板和前排空座位。助教将课程讲义放到桌上，翻开片尾内容所在页，标题缓慢显现。"
    },
    {
      "location": "shot:1/block:1",
      "text": "字幕，让表达被看见"
    },
    {
      "location": "shot:2/visual",
      "text": "切至电脑预览画面特写，只拍视频区域。视频里是同一间教室的黑板与空座位，底部出现课程结束语字幕；讲义的一角留在电脑旁。"
    },
    {
      "location": "shot:2/block:1",
      "text": "剪影练习版支持为视频添加字幕。"
    },
    {
      "location": "shot:2/block:2",
      "text": "本节课到这里结束。"
    },
    {
      "location": "shot:3/visual",
      "text": "过肩拍摄，课程讲义与电脑预览同时入镜。助教指尖沿讲义上的结束语移动，再指向屏幕上的同一句字幕，核看后合上讲义。电脑画面保留擦净的黑板、空座位和上一镜的字幕，文字不变。"
    },
    {
      "location": "shot:3/block:1",
      "text": "本节课到这里结束。"
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
  "script_hash": "972e3719a3a834dee4db7d381d70d83623fd4c0e1627e419d7228a4df79fa8f2",
  "request_hash": "fe513b9257dbed69caead2482b20e7d77c4402d6ab34c67d59e7319e8c7156e7",
  "passed": true,
  "items": [
    {
      "field": "topic",
      "requirement": "介绍字幕添加",
      "verdict": "met",
      "evidence": "第2镜旁白明确介绍“剪影练习版支持为视频添加字幕。”，画面展示带课程结束语字幕的视频。"
    },
    {
      "field": "topic",
      "requirement": "擦净的黑板",
      "verdict": "met",
      "evidence": "第1镜拍摄“擦净的黑板”，第3镜明确保留这一背景。"
    },
    {
      "field": "topic",
      "requirement": "课程讲义",
      "verdict": "met",
      "evidence": "第1镜助教放下并翻开课程讲义，第3镜对照讲义核看字幕。"
    },
    {
      "field": "topic",
      "requirement": "空座位",
      "verdict": "met",
      "evidence": "第1镜出现“前排空座位”，第2、3镜的视频画面也保留空座位。"
    },
    {
      "field": "topic",
      "requirement": "不要问句",
      "verdict": "met",
      "evidence": "标题和所有公开文案均无问句；“本节课到这里结束。”为陈述句。"
    },
    {
      "field": "topic",
      "requirement": "感叹号",
      "verdict": "met",
      "evidence": "全文公开标题、旁白及屏幕文字均未使用被禁止的感叹号。"
    },
    {
      "field": "topic",
      "requirement": "下载引导",
      "verdict": "met",
      "evidence": "所有镜头均无下载提示；第3镜以核看字幕、合上讲义结束。"
    },
    {
      "field": "topic",
      "requirement": "“轻松搞定”式保证",
      "verdict": "met",
      "evidence": "第2镜仅陈述字幕添加能力，未承诺操作轻松、效率提升或必然效果；标题属于修辞表达。"
    },
    {
      "field": "topic",
      "requirement": "只讲这个功能。",
      "verdict": "met",
      "evidence": "公开内容仅介绍和展示字幕添加。第3镜是人工对照讲义核看既有字幕，明确“文字不变”，没有演示字幕编辑、视频裁剪或其他产品功能。"
    },
    {
      "field": "audience",
      "requirement": "线上课程剪辑助教",
      "verdict": "met",
      "evidence": "第2镜展示课程片尾字幕，第3镜由助教对照讲义检查结束语，符合课程剪辑助教的工作场景。"
    },
    {
      "field": "platform",
      "requirement": "B站",
      "verdict": "met",
      "evidence": "稿件以课程场景、简短功能旁白和字幕示例组成完整短视频，适合B站发布；无需直接写出平台名称。"
    },
    {
      "field": "style",
      "requirement": "平实，克制",
      "verdict": "met",
      "evidence": "第2镜采用事实陈述，其他屏幕文案为简短标题和课程结束语；固定机位、对照讲义等画面安排克制，无夸张宣传。"
    }
  ],
  "summary": "需求均已落实，公开内容只涉及字幕添加，场景元素齐全，禁用表达均未出现。功能声明有资料支持；预计18秒已通过目标时长检查，各镜头也有相应阅读或动作支撑。",
  "method": "model_assessment_not_deterministic_proof",
  "expressions": [
    {
      "location": "title",
      "text": "字幕，让表达被看见",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于字幕主题的修辞标题，不承诺可量化效果、自动化能力或操作便利性。"
    },
    {
      "location": "shot:1/visual",
      "text": "固定机位拍摄擦净的黑板和前排空座位。助教将课程讲义放到桌上，翻开片尾内容所在页，标题缓慢显现。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "内容是教室场景、人物动作和标题呈现安排，没有将标题显现宣称为产品功能。"
    },
    {
      "location": "shot:1/block:1",
      "text": "字幕，让表达被看见",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "为屏幕标题的修辞表达，不含需要额外证据的产品承诺。"
    },
    {
      "location": "shot:2/visual",
      "text": "切至电脑预览画面特写，只拍视频区域。视频里是同一间教室的黑板与空座位，底部出现课程结束语字幕；讲义的一角留在电脑旁。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "视频中呈现已添加的字幕，由“剪影练习版支持为视频添加字幕。”支持。字幕内容及位置属于示例成片安排，没有虚构产品按钮、界面布局或自动操作流程。"
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
      "evidence": "文案与P01.F1原文完全一致，引用保持原块标注的来源及事实编号，没有新增能力或效果。"
    },
    {
      "location": "shot:2/block:2",
      "text": "本节课到这里结束。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "属于课程结束语字幕示例，不构成产品功能、效果或真实客户背书声明。"
    },
    {
      "location": "shot:3/visual",
      "text": "过肩拍摄，课程讲义与电脑预览同时入镜。助教指尖沿讲义上的结束语移动，再指向屏幕上的同一句字幕，核看后合上讲义。电脑画面保留擦净的黑板、空座位和上一镜的字幕，文字不变。",
      "verdict": "supported_claim",
      "references": [
        {
          "source_id": "P01",
          "fact_id": "P01.F1"
        }
      ],
      "evidence": "产品能力展示仍是视频中存在已添加的字幕，由P01.F1支持。对照、指向及合上讲义均为人物动作，未宣称产品自动校对，也未展示字幕编辑。"
    },
    {
      "location": "shot:3/block:1",
      "text": "本节课到这里结束。",
      "verdict": "plain_expression",
      "references": [],
      "evidence": "延续上一镜的课程结束语示例，无产品性能或效果声明。"
    }
  ],
  "pacing": {
    "verdict": "met",
    "evidence": "按duration_check，第1镜4秒，标题阅读估算2.5秒，并有放下、翻开讲义的动作；第2镜7秒，4秒旁白与字幕同beat并行，其余时间可观察字幕成片；第3镜7秒虽沿用同一句字幕，但安排了沿讲义核看、指向屏幕、合上讲义的连续动作，停留有具体任务支撑。总长18秒已通过18—20秒目标区间检查，editor_notes不计入播放时间。"
  },
  "expression_review_passed": true
}
```

## 执行路径

search_materials → write_script → estimate_duration → check_rules → check_requirements → write_script → estimate_duration → check_rules → check_requirements → finish

逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。
