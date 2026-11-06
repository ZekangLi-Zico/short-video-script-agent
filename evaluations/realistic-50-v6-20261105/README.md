# v6 · 50次真实模型网页实验

固定49种现实需求及1次预定重复，共50次。所有输入逐字沿用v5，未根据新版输出调整需求。四个网页实例通过表单提交真实Codex，未注入工具故障，未以Mock替代。

每例目录保留 brief、网页输入、提交前后DOM、截图、input、output、script、Trace、检查点、运行清单、模型诊断、逐例评阅和完整性核验。

[完整复盘](复盘报告.md) · [逐条评阅CSV](逐条复盘.csv) · [状态与耗时](results.csv) · [机器摘要](summary.json) · [冻结协议](protocol.json)

|案例|实际需求|旧状态→新状态|质量评阅|证据|
|---|---|---|---|---|
|V01|早餐摊口播|completed → completed|改进|[稿件](runs/V01/script.md) · [Trace](runs/V01/trace.jsonl) · [截图](runs/V01/page.png) · [评阅](runs/V01/review.json)|
|V02|古镇步行记录|completed → completed|改进|[稿件](runs/V02/script.md) · [Trace](runs/V02/trace.jsonl) · [截图](runs/V02/page.png) · [评阅](runs/V02/review.json)|
|V03|图书馆活动交接|completed → completed|相当|[稿件](runs/V03/script.md) · [Trace](runs/V03/trace.jsonl) · [截图](runs/V03/page.png) · [评阅](runs/V03/review.json)|
|V04|陶艺作品展|completed → completed|相当|[稿件](runs/V04/script.md) · [Trace](runs/V04/trace.jsonl) · [截图](runs/V04/page.png) · [评阅](runs/V04/review.json)|
|V05|自行车修理教学|blocked → completed|改进|[稿件](runs/V05/script.md) · [Trace](runs/V05/trace.jsonl) · [截图](runs/V05/page.png) · [评阅](runs/V05/review.json)|
|V06|宠物领养日|completed → completed|改进|[稿件](runs/V06/script.md) · [Trace](runs/V06/trace.jsonl) · [截图](runs/V06/page.png) · [评阅](runs/V06/review.json)|
|V07|服装店换季展示|completed → completed|改进|[稿件](runs/V07/script.md) · [Trace](runs/V07/trace.jsonl) · [截图](runs/V07/page.png) · [评阅](runs/V07/review.json)|
|V08|乐队排练留档|completed → completed|相当|[稿件](runs/V08/script.md) · [Trace](runs/V08/trace.jsonl) · [截图](runs/V08/page.png) · [评阅](runs/V08/review.json)|
|V09|露营打包清单|completed → completed|改进|[稿件](runs/V09/script.md) · [Trace](runs/V09/trace.jsonl) · [截图](runs/V09/page.png) · [评阅](runs/V09/review.json)|
|V10|博物馆志愿者|completed → completed|改进|[稿件](runs/V10/script.md) · [Trace](runs/V10/trace.jsonl) · [截图](runs/V10/page.png) · [评阅](runs/V10/review.json)|
|V11|社区长者课堂|completed → completed|改进|[稿件](runs/V11/script.md) · [Trace](runs/V11/trace.jsonl) · [截图](runs/V11/page.png) · [评阅](runs/V11/review.json)|
|V12|花店晨间记录|completed → completed|改进|[稿件](runs/V12/script.md) · [Trace](runs/V12/trace.jsonl) · [截图](runs/V12/page.png) · [评阅](runs/V12/review.json)|
|V13|会议花絮交付|completed → completed|改进|[稿件](runs/V13/script.md) · [Trace](runs/V13/trace.jsonl) · [截图](runs/V13/page.png) · [评阅](runs/V13/review.json)|
|V14|运动社团招新|completed → completed|改进|[稿件](runs/V14/script.md) · [Trace](runs/V14/trace.jsonl) · [截图](runs/V14/page.png) · [评阅](runs/V14/review.json)|
|V15|家庭食谱归档|completed → completed|改进|[稿件](runs/V15/script.md) · [Trace](runs/V15/trace.jsonl) · [截图](runs/V15/page.png) · [评阅](runs/V15/review.json)|
|V16|二手市集回顾|completed → completed|相当|[稿件](runs/V16/script.md) · [Trace](runs/V16/trace.jsonl) · [截图](runs/V16/page.png) · [评阅](runs/V16/review.json)|
|V17|小型展览静音屏|completed → completed|改进|[稿件](runs/V17/script.md) · [Trace](runs/V17/trace.jsonl) · [截图](runs/V17/page.png) · [评阅](runs/V17/review.json)|
|V18|不出镜办公桌|completed → completed|相当|[稿件](runs/V18/script.md) · [Trace](runs/V18/trace.jsonl) · [截图](runs/V18/page.png) · [评阅](runs/V18/review.json)|
|V19|指定片名的活动|completed → completed|相当|[稿件](runs/V19/script.md) · [Trace](runs/V19/trace.jsonl) · [截图](runs/V19/page.png) · [评阅](runs/V19/review.json)|
|V20|横竖屏双交付|completed → completed|改进|[稿件](runs/V20/script.md) · [Trace](runs/V20/trace.jsonl) · [截图](runs/V20/page.png) · [评阅](runs/V20/review.json)|
|V21|英语社团入门|completed → completed|相当|[稿件](runs/V21/script.md) · [Trace](runs/V21/trace.jsonl) · [截图](runs/V21/page.png) · [评阅](runs/V21/review.json)|
|V22|双语展览说明|completed → completed|改进|[稿件](runs/V22/script.md) · [Trace](runs/V22/trace.jsonl) · [截图](runs/V22/page.png) · [评阅](runs/V22/review.json)|
|V23|英文标题中文正文|completed → completed|相当|[稿件](runs/V23/script.md) · [Trace](runs/V23/trace.jsonl) · [截图](runs/V23/page.png) · [评阅](runs/V23/review.json)|
|V24|方言口播请求|needs_input → needs_input|仍需补充|[稿件](runs/V24/script.md) · [Trace](runs/V24/trace.jsonl) · [截图](runs/V24/page.png) · [评阅](runs/V24/review.json)|
|V25|课程宣传纯说明|completed → completed|改进|[稿件](runs/V25/script.md) · [Trace](runs/V25/trace.jsonl) · [截图](runs/V25/page.png) · [评阅](runs/V25/review.json)|
|V26|六秒片头位置|completed → completed|改进|[稿件](runs/V26/script.md) · [Trace](runs/V26/trace.jsonl) · [截图](runs/V26/page.png) · [评阅](runs/V26/review.json)|
|V27|十秒固定两镜|completed → completed|改进|[稿件](runs/V27/script.md) · [Trace](runs/V27/trace.jsonl) · [截图](runs/V27/page.png) · [评阅](runs/V27/review.json)|
|V28|四十五秒体验讲解|blocked → completed|改进|[稿件](runs/V28/script.md) · [Trace](runs/V28/trace.jsonl) · [截图](runs/V28/page.png) · [评阅](runs/V28/review.json)|
|V29|一分钟工作交接|completed → completed|改进|[稿件](runs/V29/script.md) · [Trace](runs/V29/trace.jsonl) · [截图](runs/V29/page.png) · [评阅](runs/V29/review.json)|
|V30|八秒三能力|completed → completed|相当|[稿件](runs/V30/script.md) · [Trace](runs/V30/trace.jsonl) · [截图](runs/V30/page.png) · [评阅](runs/V30/review.json)|
|V31|屏幕大字限制|completed → completed|改进|[稿件](runs/V31/script.md) · [Trace](runs/V31/trace.jsonl) · [截图](runs/V31/page.png) · [评阅](runs/V31/review.json)|
|V32|慢节奏教学卡|completed → completed|改进|[稿件](runs/V32/script.md) · [Trace](runs/V32/trace.jsonl) · [截图](runs/V32/page.png) · [评阅](runs/V32/review.json)|
|V33|自动识别宣传|needs_input → needs_input|仍需补充|[稿件](runs/V33/script.md) · [Trace](runs/V33/trace.jsonl) · [截图](runs/V33/page.png) · [评阅](runs/V33/review.json)|
|V34|收费说明咨询|needs_input → needs_input|仍需补充|[稿件](runs/V34/script.md) · [Trace](runs/V34/trace.jsonl) · [截图](runs/V34/page.png) · [评阅](runs/V34/review.json)|
|V35|离线培训素材|needs_input → needs_input|仍需补充|[稿件](runs/V35/script.md) · [Trace](runs/V35/trace.jsonl) · [截图](runs/V35/page.png) · [评阅](runs/V35/review.json)|
|V36|客户增长数字|completed → completed|改进|[稿件](runs/V36/script.md) · [Trace](runs/V36/trace.jsonl) · [截图](runs/V36/page.png) · [评阅](runs/V36/review.json)|
|V37|竞品功能价格对比|needs_input → needs_input|仍需补充|[稿件](runs/V37/script.md) · [Trace](runs/V37/trace.jsonl) · [截图](runs/V37/page.png) · [评阅](runs/V37/review.json)|
|V38|字幕文件交付|needs_input → needs_input|仍需补充|[稿件](runs/V38/script.md) · [Trace](runs/V38/trace.jsonl) · [截图](runs/V38/page.png) · [评阅](runs/V38/review.json)|
|V39|导出画质水印|needs_input → needs_input|仍需补充|[稿件](runs/V39/script.md) · [Trace](runs/V39/trace.jsonl) · [截图](runs/V39/page.png) · [评阅](runs/V39/review.json)|
|V40|本周更新通知|needs_input → needs_input|仍需补充|[稿件](runs/V40/script.md) · [Trace](runs/V40/trace.jsonl) · [截图](runs/V40/page.png) · [评阅](runs/V40/review.json)|
|V41|面包新品没资料|needs_input → needs_input|仍需补充|[稿件](runs/V41/script.md) · [Trace](runs/V41/trace.jsonl) · [截图](runs/V41/page.png) · [评阅](runs/V41/review.json)|
|V42|露营灯新品|needs_input → needs_input|仍需补充|[稿件](runs/V42/script.md) · [Trace](runs/V42/trace.jsonl) · [截图](runs/V42/page.png) · [评阅](runs/V42/review.json)|
|V43|游戏活动预告|needs_input → needs_input|仍需补充|[稿件](runs/V43/script.md) · [Trace](runs/V43/trace.jsonl) · [截图](runs/V43/page.png) · [评阅](runs/V43/review.json)|
|V44|课程招生缺细则|needs_input → needs_input|仍需补充|[稿件](runs/V44/script.md) · [Trace](runs/V44/trace.jsonl) · [截图](runs/V44/page.png) · [评阅](runs/V44/review.json)|
|V45|字幕旧稿压缩|completed → completed|改进|[稿件](runs/V45/script.md) · [Trace](runs/V45/trace.jsonl) · [截图](runs/V45/page.png) · [评阅](runs/V45/review.json)|
|V46|旧稿能力核对|completed → completed|改进|[稿件](runs/V46/script.md) · [Trace](runs/V46/trace.jsonl) · [截图](runs/V46/page.png) · [评阅](runs/V46/review.json)|
|V47|四镜头顺序锁定|completed → completed|相当|[稿件](runs/V47/script.md) · [Trace](runs/V47/trace.jsonl) · [截图](runs/V47/page.png) · [评阅](runs/V47/review.json)|
|V48|只留字幕的客户返修|completed → completed|相当|[稿件](runs/V48/script.md) · [Trace](runs/V48/trace.jsonl) · [截图](runs/V48/page.png) · [评阅](runs/V48/review.json)|
|V49|比例短片返修|completed → completed|相当|[稿件](runs/V49/script.md) · [Trace](runs/V49/trace.jsonl) · [截图](runs/V49/page.png) · [评阅](runs/V49/review.json)|
|V50|隔日再次交付|completed → completed|改进|[稿件](runs/V50/script.md) · [Trace](runs/V50/trace.jsonl) · [截图](runs/V50/page.png) · [评阅](runs/V50/review.json)|
