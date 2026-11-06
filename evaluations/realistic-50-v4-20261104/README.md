# v4 修复后 50 次真实模型网页实验

已完成：50次网页提交、315次真实模型响应；35 completed、15 needs_input。无Mock替代，无故障注入，无补跑覆盖。50次完整记录均核验通过；两次自然清理PermissionError被处理并保留诊断。应用与资料19项、旧证据3481项哈希不变。

本轮沿用v3冻结需求，49份不同输入＋V01/V50预定重复。产品与工作场景为合成资料，不是真实客户项目。程序状态不等于业务质量。

- [完整复盘与前后比较](复盘报告.md)
- [逐条评阅 CSV](逐条复盘.csv) · [前后对照 CSV](前后对照.csv)
- [机器统计与核验](results.json) · [比较数据](comparison.json)
- [冻结需求](cases.json) · [实验方法](实验方法.md) · [评阅口径](rubric.md)
- [版本与历史文件基线](baseline.json) · [诊断摘要](diagnostic-summary.json) · [执行时间](work-session.json)
- [最终网页脚本截图](final-web-script.png) · [最终执行过程截图](final-web-trace.png)
- [修复前实验](../realistic-50-v3-20261104/README.md)

每个运行目录保存 `brief.json`、`ui-input.json`、`before.txt`、`submitted.txt`、`after.txt`、`ui-record.json`、`page.png`，以及后台 `input.json`、`output.json`、`script.md`、`trace.jsonl`、`manifest.json`、`data_snapshot.json`、`checkpoint.json`、`run.json`、`diagnostics/`。`review.json`是逐稿阅读意见，`audit.json`验证文件一致性；没有保存模型内部推理。

|案例|需求|状态|步/响应|实际稿件与证据|逐稿评阅|
|---|---|---|---|---|---|
|V01|早餐摊口播|completed|6/7|[结果](runs/V01/output.json) · [稿件](runs/V01/script.md) · [Trace](runs/V01/trace.jsonl) · [页面](runs/V01/page.png)|[脚本可用](runs/V01/review.json)|
|V02|古镇步行记录|completed|9/10|[结果](runs/V02/output.json) · [稿件](runs/V02/script.md) · [Trace](runs/V02/trace.jsonl) · [页面](runs/V02/page.png)|[脚本可用](runs/V02/review.json)|
|V03|图书馆活动交接|completed|6/7|[结果](runs/V03/output.json) · [稿件](runs/V03/script.md) · [Trace](runs/V03/trace.jsonl) · [页面](runs/V03/page.png)|[脚本可用](runs/V03/review.json)|
|V04|陶艺作品展|completed|6/7|[结果](runs/V04/output.json) · [稿件](runs/V04/script.md) · [Trace](runs/V04/trace.jsonl) · [页面](runs/V04/page.png)|[脚本可用](runs/V04/review.json)|
|V05|自行车修理教学|completed|6/7|[结果](runs/V05/output.json) · [稿件](runs/V05/script.md) · [Trace](runs/V05/trace.jsonl) · [页面](runs/V05/page.png)|[脚本可用](runs/V05/review.json)|
|V06|宠物领养日|completed|6/7|[结果](runs/V06/output.json) · [稿件](runs/V06/script.md) · [Trace](runs/V06/trace.jsonl) · [页面](runs/V06/page.png)|[脚本可用](runs/V06/review.json)|
|V07|服装店换季展示|completed|6/7|[结果](runs/V07/output.json) · [稿件](runs/V07/script.md) · [Trace](runs/V07/trace.jsonl) · [页面](runs/V07/page.png)|[脚本可用](runs/V07/review.json)|
|V08|乐队排练留档|completed|6/7|[结果](runs/V08/output.json) · [稿件](runs/V08/script.md) · [Trace](runs/V08/trace.jsonl) · [页面](runs/V08/page.png)|[脚本可用](runs/V08/review.json)|
|V09|露营打包清单|completed|6/7|[结果](runs/V09/output.json) · [稿件](runs/V09/script.md) · [Trace](runs/V09/trace.jsonl) · [页面](runs/V09/page.png)|[脚本可用](runs/V09/review.json)|
|V10|博物馆志愿者|completed|6/7|[结果](runs/V10/output.json) · [稿件](runs/V10/script.md) · [Trace](runs/V10/trace.jsonl) · [页面](runs/V10/page.png)|[脚本可用](runs/V10/review.json)|
|V11|社区长者课堂|completed|6/7|[结果](runs/V11/output.json) · [稿件](runs/V11/script.md) · [Trace](runs/V11/trace.jsonl) · [页面](runs/V11/page.png)|[脚本可用](runs/V11/review.json)|
|V12|花店晨间记录|completed|6/7|[结果](runs/V12/output.json) · [稿件](runs/V12/script.md) · [Trace](runs/V12/trace.jsonl) · [页面](runs/V12/page.png)|[脚本可用](runs/V12/review.json)|
|V13|会议花絮交付|completed|6/7|[结果](runs/V13/output.json) · [稿件](runs/V13/script.md) · [Trace](runs/V13/trace.jsonl) · [页面](runs/V13/page.png)|[脚本可用](runs/V13/review.json)|
|V14|运动社团招新|completed|6/7|[结果](runs/V14/output.json) · [稿件](runs/V14/script.md) · [Trace](runs/V14/trace.jsonl) · [页面](runs/V14/page.png)|[脚本可用](runs/V14/review.json)|
|V15|家庭食谱归档|completed|6/7|[结果](runs/V15/output.json) · [稿件](runs/V15/script.md) · [Trace](runs/V15/trace.jsonl) · [页面](runs/V15/page.png)|[脚本可用](runs/V15/review.json)|
|V16|二手市集回顾|completed|6/7|[结果](runs/V16/output.json) · [稿件](runs/V16/script.md) · [Trace](runs/V16/trace.jsonl) · [页面](runs/V16/page.png)|[脚本可用](runs/V16/review.json)|
|V17|小型展览静音屏|completed|6/7|[结果](runs/V17/output.json) · [稿件](runs/V17/script.md) · [Trace](runs/V17/trace.jsonl) · [页面](runs/V17/page.png)|[脚本可用](runs/V17/review.json)|
|V18|不出镜办公桌|completed|6/7|[结果](runs/V18/output.json) · [稿件](runs/V18/script.md) · [Trace](runs/V18/trace.jsonl) · [页面](runs/V18/page.png)|[脚本可用](runs/V18/review.json)|
|V19|指定片名的活动|completed|6/7|[结果](runs/V19/output.json) · [稿件](runs/V19/script.md) · [Trace](runs/V19/trace.jsonl) · [页面](runs/V19/page.png)|[脚本可用](runs/V19/review.json)|
|V20|横竖屏双交付|completed|6/7|[结果](runs/V20/output.json) · [稿件](runs/V20/script.md) · [Trace](runs/V20/trace.jsonl) · [页面](runs/V20/page.png)|[脚本可用](runs/V20/review.json)|
|V21|英语社团入门|completed|12/14|[结果](runs/V21/output.json) · [稿件](runs/V21/script.md) · [Trace](runs/V21/trace.jsonl) · [页面](runs/V21/page.png)|[脚本可用，但时长估算有限](runs/V21/review.json)|
|V22|双语展览说明|needs_input|3/3|[结果](runs/V22/output.json) · [稿件](runs/V22/script.md) · [Trace](runs/V22/trace.jsonl) · [页面](runs/V22/page.png)|[受引用策略限制](runs/V22/review.json)|
|V23|英文标题中文正文|completed|6/7|[结果](runs/V23/output.json) · [稿件](runs/V23/script.md) · [Trace](runs/V23/trace.jsonl) · [页面](runs/V23/page.png)|[脚本可用](runs/V23/review.json)|
|V24|方言口播请求|needs_input|3/3|[结果](runs/V24/output.json) · [稿件](runs/V24/script.md) · [Trace](runs/V24/trace.jsonl) · [页面](runs/V24/page.png)|[方言需求未交付](runs/V24/review.json)|
|V25|课程宣传纯说明|completed|6/7|[结果](runs/V25/output.json) · [稿件](runs/V25/script.md) · [Trace](runs/V25/trace.jsonl) · [页面](runs/V25/page.png)|[脚本可用](runs/V25/review.json)|
|V26|六秒片头位置|completed|6/7|[结果](runs/V26/output.json) · [稿件](runs/V26/script.md) · [Trace](runs/V26/trace.jsonl) · [页面](runs/V26/page.png)|[脚本可用；旧时长审核问题本次未复现](runs/V26/review.json)|
|V27|十秒固定两镜|completed|6/7|[结果](runs/V27/output.json) · [稿件](runs/V27/script.md) · [Trace](runs/V27/trace.jsonl) · [页面](runs/V27/page.png)|[脚本可用；旧时长审核问题本次未复现](runs/V27/review.json)|
|V28|四十五秒体验讲解|completed|6/7|[结果](runs/V28/output.json) · [稿件](runs/V28/script.md) · [Trace](runs/V28/trace.jsonl) · [页面](runs/V28/page.png)|[脚本可用；旧时长审核问题本次未复现](runs/V28/review.json)|
|V29|一分钟工作交接|completed|6/7|[结果](runs/V29/output.json) · [稿件](runs/V29/script.md) · [Trace](runs/V29/trace.jsonl) · [页面](runs/V29/page.png)|[脚本可用；修复前阻塞本次消除](runs/V29/review.json)|
|V30|八秒三能力|needs_input|5/5|[结果](runs/V30/output.json) · [稿件](runs/V30/script.md) · [Trace](runs/V30/trace.jsonl) · [页面](runs/V30/page.png)|[诚实未完成；受引用与估时策略限制](runs/V30/review.json)|
|V31|屏幕大字限制|needs_input|3/3|[结果](runs/V31/output.json) · [稿件](runs/V31/script.md) · [Trace](runs/V31/trace.jsonl) · [页面](runs/V31/page.png)|[短字卡需求未交付；受引用策略限制](runs/V31/review.json)|
|V32|慢节奏教学卡|completed|6/7|[结果](runs/V32/output.json) · [稿件](runs/V32/script.md) · [Trace](runs/V32/trace.jsonl) · [页面](runs/V32/page.png)|[脚本可用](runs/V32/review.json)|
|V33|自动识别宣传|needs_input|3/3|[结果](runs/V33/output.json) · [稿件](runs/V33/script.md) · [Trace](runs/V33/trace.jsonl) · [页面](runs/V33/page.png)|[资料不足时合理停止](runs/V33/review.json)|
|V34|收费说明咨询|needs_input|3/3|[结果](runs/V34/output.json) · [稿件](runs/V34/script.md) · [Trace](runs/V34/trace.jsonl) · [页面](runs/V34/page.png)|[资料不足时合理停止](runs/V34/review.json)|
|V35|离线培训素材|needs_input|3/3|[结果](runs/V35/output.json) · [稿件](runs/V35/script.md) · [Trace](runs/V35/trace.jsonl) · [页面](runs/V35/page.png)|[资料不足时合理停止](runs/V35/review.json)|
|V36|客户增长数字|completed|6/7|[结果](runs/V36/output.json) · [稿件](runs/V36/script.md) · [Trace](runs/V36/trace.jsonl) · [页面](runs/V36/page.png)|[脚本可用；表达偏说明型](runs/V36/review.json)|
|V37|竞品功能价格对比|needs_input|3/3|[结果](runs/V37/output.json) · [稿件](runs/V37/script.md) · [Trace](runs/V37/trace.jsonl) · [页面](runs/V37/page.png)|[资料不足时合理停止](runs/V37/review.json)|
|V38|字幕文件交付|needs_input|3/3|[结果](runs/V38/output.json) · [稿件](runs/V38/script.md) · [Trace](runs/V38/trace.jsonl) · [页面](runs/V38/page.png)|[资料不足时合理停止](runs/V38/review.json)|
|V39|导出画质水印|needs_input|3/3|[结果](runs/V39/output.json) · [稿件](runs/V39/script.md) · [Trace](runs/V39/trace.jsonl) · [页面](runs/V39/page.png)|[资料不足时合理停止](runs/V39/review.json)|
|V40|本周更新通知|needs_input|2/2|[结果](runs/V40/output.json) · [稿件](runs/V40/script.md) · [Trace](runs/V40/trace.jsonl) · [页面](runs/V40/page.png)|[资料不足时合理停止](runs/V40/review.json)|
|V41|面包新品没资料|needs_input|3/3|[结果](runs/V41/output.json) · [稿件](runs/V41/script.md) · [Trace](runs/V41/trace.jsonl) · [页面](runs/V41/page.png)|[资料不足时合理停止](runs/V41/review.json)|
|V42|露营灯新品|needs_input|3/3|[结果](runs/V42/output.json) · [稿件](runs/V42/script.md) · [Trace](runs/V42/trace.jsonl) · [页面](runs/V42/page.png)|[资料不足时合理停止](runs/V42/review.json)|
|V43|游戏活动预告|needs_input|2/2|[结果](runs/V43/output.json) · [稿件](runs/V43/script.md) · [Trace](runs/V43/trace.jsonl) · [页面](runs/V43/page.png)|[资料不足时合理停止](runs/V43/review.json)|
|V44|课程招生缺细则|needs_input|3/3|[结果](runs/V44/output.json) · [稿件](runs/V44/script.md) · [Trace](runs/V44/trace.jsonl) · [页面](runs/V44/page.png)|[资料不足时合理停止](runs/V44/review.json)|
|V45|字幕旧稿压缩|completed|8/9|[结果](runs/V45/output.json) · [稿件](runs/V45/script.md) · [Trace](runs/V45/trace.jsonl) · [页面](runs/V45/page.png)|[有效压缩旧稿](runs/V45/review.json)|
|V46|旧稿能力核对|completed|12/14|[结果](runs/V46/output.json) · [稿件](runs/V46/script.md) · [Trace](runs/V46/trace.jsonl) · [页面](runs/V46/page.png)|[纠错完成；修改说明仍需编辑安排](runs/V46/review.json)|
|V47|四镜头顺序锁定|completed|8/9|[结果](runs/V47/output.json) · [稿件](runs/V47/script.md) · [Trace](runs/V47/trace.jsonl) · [页面](runs/V47/page.png)|[有效压缩且保留固定结构](runs/V47/review.json)|
|V48|只留字幕的客户返修|completed|8/9|[结果](runs/V48/output.json) · [稿件](runs/V48/script.md) · [Trace](runs/V48/trace.jsonl) · [页面](runs/V48/page.png)|[满足删改约束；场景表达较简单](runs/V48/review.json)|
|V49|比例短片返修|completed|8/9|[结果](runs/V49/output.json) · [稿件](runs/V49/script.md) · [Trace](runs/V49/trace.jsonl) · [页面](runs/V49/page.png)|[有效压缩且保持事实边界](runs/V49/review.json)|
|V50|隔日再次交付|completed|6/7|[结果](runs/V50/output.json) · [稿件](runs/V50/script.md) · [Trace](runs/V50/trace.jsonl) · [页面](runs/V50/page.png)|[脚本可用；重复需求约束保持](runs/V50/review.json)|

needs_input行可能没有脚本；请看output.json中的停止理由。评阅由同一AI开发助手完成，不是独立盲评。

在完整项目根目录运行 `python evaluations/realistic-50-v4-20261104/audit_campaign.py --full --require-50` 可复算保存记录和历史哈希，不调用模型。独立补充ZIP的根目录 `verify_bundle.py` 只校验包内文件；它不包含所有其他历史归档和后台输出。
