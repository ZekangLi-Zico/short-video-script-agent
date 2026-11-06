# v3 · 50次真实模型网页实验

先冻结现实需求，再从网页提交；全部选择真实Codex，没有Mock，没有人工注入故障。初始四个相同版本本地实例交错运行，文件占用异常后降低并发；见protocol-amendment-01.md。耗时不是单用户性能基准。

已归档 50/50；实际模型运行 50；可确认模型响应至少 330；部分记录 3。

另保留 1 次零模型响应的失败尝试：[V43 首次尝试](attempts/V43-no-response-01/retry-note.md)，不计入上述 50 次。50 次包含 49 份不同输入，V50 为预先安排的 V01 原样重复。

程序completed不等于语义或业务合格。具体评阅与局限见复盘报告。旧版本和旧测试不覆盖。

[复盘报告](复盘报告.md) · [逐条复盘CSV](逐条复盘.csv) · [实验方法](实验方法.md) · [最终核验](validation.json)

[冻结需求](测试清单.md) · [基线哈希](baseline.json) · [结果CSV](results.csv) · [机器摘要](results.json)

|编号|场景|实际状态|估时/输入|步数|模型响应|原始证据|
|---|---|---|---|---|---|---|
|V01|早餐摊口播|completed|14.1 / 25 (max)|6|7|[脚本](runs/V01/script.md) · [Trace](runs/V01/trace.jsonl) · [复算](runs/V01/audit.json) · [页面](runs/V01/page.jpg)|
|V02|古镇步行记录|completed|27.5 / 30 (target)|6|7|[脚本](runs/V02/script.md) · [Trace](runs/V02/trace.jsonl) · [复算](runs/V02/audit.json) · [页面](runs/V02/page.jpg)|
|V03|图书馆活动交接|completed|22.6 / 24 (target)|6|7|[脚本](runs/V03/script.md) · [Trace](runs/V03/trace.jsonl) · [复算](runs/V03/audit.json) · [页面](runs/V03/page.jpg)|
|V04|陶艺作品展|infrastructure_error|11 / 20 (max)|8|至少9|[部分输出](runs/V04/partial-output.json) · [页面步骤](runs/V04/partial-trace-ui.json) · [运行故障](runs/V04/infrastructure-error.json) · [页面](runs/V04/page.jpg)|
|V05|自行车修理教学|infrastructure_error|32.3 / 35 (target)|4|至少4|[部分输出](runs/V05/partial-output.json) · [页面步骤](runs/V05/partial-trace-ui.json) · [运行故障](runs/V05/infrastructure-error.json) · [页面](runs/V05/page.jpg)|
|V06|宠物领养日|completed|15.3 / 28 (max)|6|7|[脚本](runs/V06/script.md) · [Trace](runs/V06/trace.jsonl) · [复算](runs/V06/audit.json) · [页面](runs/V06/page.jpg)|
|V07|服装店换季展示|completed|22.0 / 24 (target)|10|12|[脚本](runs/V07/script.md) · [Trace](runs/V07/trace.jsonl) · [复算](runs/V07/audit.json) · [页面](runs/V07/page.jpg)|
|V08|乐队排练留档|completed|12.3 / 20 (max)|6|7|[脚本](runs/V08/script.md) · [Trace](runs/V08/trace.jsonl) · [复算](runs/V08/audit.json) · [页面](runs/V08/page.jpg)|
|V09|露营打包清单|infrastructure_error|27 / 30 (target)|4|至少4|[部分输出](runs/V09/partial-output.json) · [页面步骤](runs/V09/partial-trace-ui.json) · [运行故障](runs/V09/infrastructure-error.json) · [页面](runs/V09/page.jpg)|
|V10|博物馆志愿者|completed|12.0 / 26 (max)|6|7|[脚本](runs/V10/script.md) · [Trace](runs/V10/trace.jsonl) · [复算](runs/V10/audit.json) · [页面](runs/V10/page.jpg)|
|V11|社区长者课堂|completed|37.1 / 40 (target)|6|7|[脚本](runs/V11/script.md) · [Trace](runs/V11/trace.jsonl) · [复算](runs/V11/audit.json) · [页面](runs/V11/page.jpg)|
|V12|花店晨间记录|completed|12.0 / 18 (max)|6|7|[脚本](runs/V12/script.md) · [Trace](runs/V12/trace.jsonl) · [复算](runs/V12/audit.json) · [页面](runs/V12/page.jpg)|
|V13|会议花絮交付|completed|9.0 / 20 (max)|6|7|[脚本](runs/V13/script.md) · [Trace](runs/V13/trace.jsonl) · [复算](runs/V13/audit.json) · [页面](runs/V13/page.jpg)|
|V14|运动社团招新|completed|37.9 / 40 (target)|6|7|[脚本](runs/V14/script.md) · [Trace](runs/V14/trace.jsonl) · [复算](runs/V14/audit.json) · [页面](runs/V14/page.jpg)|
|V15|家庭食谱归档|completed|27.5 / 30 (target)|6|7|[脚本](runs/V15/script.md) · [Trace](runs/V15/trace.jsonl) · [复算](runs/V15/audit.json) · [页面](runs/V15/page.jpg)|
|V16|二手市集回顾|completed|14.5 / 22 (max)|6|7|[脚本](runs/V16/script.md) · [Trace](runs/V16/trace.jsonl) · [复算](runs/V16/audit.json) · [页面](runs/V16/page.jpg)|
|V17|小型展览静音屏|completed|24.0 / 25 (target)|6|7|[脚本](runs/V17/script.md) · [Trace](runs/V17/trace.jsonl) · [复算](runs/V17/audit.json) · [页面](runs/V17/page.jpg)|
|V18|不出镜办公桌|completed|9.5 / 18 (max)|6|7|[脚本](runs/V18/script.md) · [Trace](runs/V18/trace.jsonl) · [复算](runs/V18/audit.json) · [页面](runs/V18/page.jpg)|
|V19|指定片名的活动|completed|26.0 / 28 (target)|10|12|[脚本](runs/V19/script.md) · [Trace](runs/V19/trace.jsonl) · [复算](runs/V19/audit.json) · [页面](runs/V19/page.jpg)|
|V20|横竖屏双交付|completed|11.0 / 25 (max)|6|7|[脚本](runs/V20/script.md) · [Trace](runs/V20/trace.jsonl) · [复算](runs/V20/audit.json) · [页面](runs/V20/page.jpg)|
|V21|英语社团入门|completed|33.0 / 35 (target)|8|9|[脚本](runs/V21/script.md) · [Trace](runs/V21/trace.jsonl) · [复算](runs/V21/audit.json) · [页面](runs/V21/page.jpg)|
|V22|双语展览说明|needs_input|None / 30 (target)|3|3|[脚本](runs/V22/script.md) · [Trace](runs/V22/trace.jsonl) · [复算](runs/V22/audit.json) · [页面](runs/V22/page.jpg)|
|V23|英文标题中文正文|completed|12.0 / 25 (max)|6|7|[脚本](runs/V23/script.md) · [Trace](runs/V23/trace.jsonl) · [复算](runs/V23/audit.json) · [页面](runs/V23/page.jpg)|
|V24|方言口播请求|needs_input|None / 30 (max)|3|3|[脚本](runs/V24/script.md) · [Trace](runs/V24/trace.jsonl) · [复算](runs/V24/audit.json) · [页面](runs/V24/page.jpg)|
|V25|课程宣传纯说明|completed|19.6 / 20 (target)|6|7|[脚本](runs/V25/script.md) · [Trace](runs/V25/trace.jsonl) · [复算](runs/V25/audit.json) · [页面](runs/V25/page.jpg)|
|V26|六秒片头位置|completed|4.0 / 6 (max)|10|12|[脚本](runs/V26/script.md) · [Trace](runs/V26/trace.jsonl) · [复算](runs/V26/audit.json) · [页面](runs/V26/page.jpg)|
|V27|十秒固定两镜|completed|8.8 / 10 (max)|10|12|[脚本](runs/V27/script.md) · [Trace](runs/V27/trace.jsonl) · [复算](runs/V27/audit.json) · [页面](runs/V27/page.jpg)|
|V28|四十五秒体验讲解|completed|44.1 / 45 (target)|11|14|[脚本](runs/V28/script.md) · [Trace](runs/V28/trace.jsonl) · [复算](runs/V28/audit.json) · [页面](runs/V28/page.jpg)|
|V29|一分钟工作交接|blocked|55.6 / 60 (target)|7|9|[脚本](runs/V29/script.md) · [Trace](runs/V29/trace.jsonl) · [复算](runs/V29/audit.json) · [页面](runs/V29/page.jpg)|
|V30|八秒三能力|needs_input|12.8 / 8 (max)|5|5|[脚本](runs/V30/script.md) · [Trace](runs/V30/trace.jsonl) · [复算](runs/V30/audit.json) · [页面](runs/V30/page.jpg)|
|V31|屏幕大字限制|needs_input|None / 20 (max)|3|3|[脚本](runs/V31/script.md) · [Trace](runs/V31/trace.jsonl) · [复算](runs/V31/audit.json) · [页面](runs/V31/page.jpg)|
|V32|慢节奏教学卡|completed|23.5 / 25 (target)|6|7|[脚本](runs/V32/script.md) · [Trace](runs/V32/trace.jsonl) · [复算](runs/V32/audit.json) · [页面](runs/V32/page.jpg)|
|V33|自动识别宣传|needs_input|None / 30 (max)|3|3|[脚本](runs/V33/script.md) · [Trace](runs/V33/trace.jsonl) · [复算](runs/V33/audit.json) · [页面](runs/V33/page.jpg)|
|V34|收费说明咨询|needs_input|None / 30 (max)|3|3|[脚本](runs/V34/script.md) · [Trace](runs/V34/trace.jsonl) · [复算](runs/V34/audit.json) · [页面](runs/V34/page.jpg)|
|V35|离线培训素材|needs_input|None / 35 (max)|3|3|[脚本](runs/V35/script.md) · [Trace](runs/V35/trace.jsonl) · [复算](runs/V35/audit.json) · [页面](runs/V35/page.jpg)|
|V36|客户增长数字|completed|15.8 / 25 (max)|6|7|[脚本](runs/V36/script.md) · [Trace](runs/V36/trace.jsonl) · [复算](runs/V36/audit.json) · [页面](runs/V36/page.jpg)|
|V37|竞品功能价格对比|needs_input|None / 45 (max)|3|3|[脚本](runs/V37/script.md) · [Trace](runs/V37/trace.jsonl) · [复算](runs/V37/audit.json) · [页面](runs/V37/page.jpg)|
|V38|字幕文件交付|needs_input|None / 30 (max)|3|3|[脚本](runs/V38/script.md) · [Trace](runs/V38/trace.jsonl) · [复算](runs/V38/audit.json) · [页面](runs/V38/page.jpg)|
|V39|导出画质水印|blocked|None / 30 (max)|3|2|[脚本](runs/V39/script.md) · [Trace](runs/V39/trace.jsonl) · [复算](runs/V39/audit.json) · [页面](runs/V39/page.jpg)|
|V40|本周更新通知|needs_input|None / 25 (max)|2|2|[脚本](runs/V40/script.md) · [Trace](runs/V40/trace.jsonl) · [复算](runs/V40/audit.json) · [页面](runs/V40/page.jpg)|
|V41|面包新品没资料|needs_input|None / 25 (max)|2|2|[脚本](runs/V41/script.md) · [Trace](runs/V41/trace.jsonl) · [复算](runs/V41/audit.json) · [页面](runs/V41/page.jpg)|
|V42|露营灯新品|needs_input|None / 30 (max)|3|3|[脚本](runs/V42/script.md) · [Trace](runs/V42/trace.jsonl) · [复算](runs/V42/audit.json) · [页面](runs/V42/page.jpg)|
|V43|游戏活动预告|needs_input|None / 30 (max)|2|2|[脚本](runs/V43/script.md) · [Trace](runs/V43/trace.jsonl) · [复算](runs/V43/audit.json) · [页面](runs/V43/page.jpg)|
|V44|课程招生缺细则|needs_input|None / 35 (max)|3|3|[脚本](runs/V44/script.md) · [Trace](runs/V44/trace.jsonl) · [复算](runs/V44/audit.json) · [页面](runs/V44/page.jpg)|
|V45|字幕旧稿压缩|completed|13.0 / 25 (max)|8|9|[脚本](runs/V45/script.md) · [Trace](runs/V45/trace.jsonl) · [复算](runs/V45/audit.json) · [页面](runs/V45/page.jpg)|
|V46|旧稿能力核对|blocked|19.8 / 28 (max)|12|14|[脚本](runs/V46/script.md) · [Trace](runs/V46/trace.jsonl) · [复算](runs/V46/audit.json) · [页面](runs/V46/page.jpg)|
|V47|四镜头顺序锁定|completed|15.0 / 22 (max)|8|9|[脚本](runs/V47/script.md) · [Trace](runs/V47/trace.jsonl) · [复算](runs/V47/audit.json) · [页面](runs/V47/page.jpg)|
|V48|只留字幕的客户返修|completed|10.0 / 20 (max)|8|9|[脚本](runs/V48/script.md) · [Trace](runs/V48/trace.jsonl) · [复算](runs/V48/audit.json) · [页面](runs/V48/page.jpg)|
|V49|比例短片返修|completed|9.0 / 15 (max)|8|9|[脚本](runs/V49/script.md) · [Trace](runs/V49/trace.jsonl) · [复算](runs/V49/audit.json) · [页面](runs/V49/page.jpg)|
|V50|隔日再次交付|completed|16.3 / 25 (max)|6|7|[脚本](runs/V50/script.md) · [Trace](runs/V50/trace.jsonl) · [复算](runs/V50/audit.json) · [页面](runs/V50/page.jpg)|
