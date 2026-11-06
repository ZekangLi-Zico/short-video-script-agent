# 50 次现实需求测试记录

**已完成 50/50。** [复盘报告](复盘报告.md) · [逐条复盘](逐条复盘.csv) · [最终验证](validation.json)

清单在首条运行前冻结，见 [测试清单](测试清单.md) 与 [baseline.json](baseline.json)。全部经网页表单提交；未使用 Mock 或直接调用提交接口。应用代码、提示词、素材和规则保持不变。

程序状态是实际返回，**completed 不自动等于满足全部需求**。语义评审见后续复盘。

已归档：50/50。

| 案例 | 实际状态 | 估时/上限 | 步数 | 运行耗时 | 产物 |
|---|---|---|---|---|---|
| T01 新手口播 | completed | 26.0 / 30 | 5 | 87.9秒 | [脚本](runs/T01/script.md) · [Trace](runs/T01/trace.jsonl) · [页面](runs/T01/page.jpg) · [复算](runs/T01/audit.json) |
| T02 校园采访 | completed | 22.0 / 25 | 5 | 135.5秒 | [脚本](runs/T02/script.md) · [Trace](runs/T02/trace.jsonl) · [页面](runs/T02/page.jpg) · [复算](runs/T02/audit.json) |
| T03 餐饮菜单字幕 | needs_input | 17.0 / 20 | 6 | 153.9秒 | [脚本](runs/T03/script.md) · [Trace](runs/T03/trace.jsonl) · [页面](runs/T03/page.jpg) · [复算](runs/T03/audit.json) |
| T04 读书分享 | completed | 13.0 / 15 | 5 | 88.3秒 | [脚本](runs/T04/script.md) · [Trace](runs/T04/trace.jsonl) · [页面](runs/T04/page.jpg) · [复算](runs/T04/audit.json) |
| T05 宠物片段 | completed | 10.0 / 12 | 5 | 112.2秒 | [脚本](runs/T05/script.md) · [Trace](runs/T05/trace.jsonl) · [页面](runs/T05/page.jpg) · [复算](runs/T05/audit.json) |
| T06 旅行片段 | needs_input | None / 20 | 4 | 108.4秒 | [脚本](runs/T06/script.md) · [Trace](runs/T06/trace.jsonl) · [页面](runs/T06/page.jpg) · [复算](runs/T06/audit.json) |
| T07 运动录像 | completed | 13.0 / 15 | 5 | 84.0秒 | [脚本](runs/T07/script.md) · [Trace](runs/T07/trace.jsonl) · [页面](runs/T07/page.jpg) · [复算](runs/T07/audit.json) |
| T08 手工过程 | completed | 22.0 / 25 | 5 | 85.7秒 | [脚本](runs/T08/script.md) · [Trace](runs/T08/trace.jsonl) · [页面](runs/T08/page.jpg) · [复算](runs/T08/audit.json) |
| T09 竖屏发布 | completed | 17.0 / 20 | 5 | 78.4秒 | [脚本](runs/T09/script.md) · [Trace](runs/T09/trace.jsonl) · [页面](runs/T09/page.jpg) · [复算](runs/T09/audit.json) |
| T10 家庭记录 | completed | 27.0 / 30 | 5 | 92.3秒 | [脚本](runs/T10/script.md) · [Trace](runs/T10/trace.jsonl) · [页面](runs/T10/page.jpg) · [复算](runs/T10/audit.json) |
| T11 产品概览 | completed | 41.0 / 45 | 5 | 97.0秒 | [脚本](runs/T11/script.md) · [Trace](runs/T11/trace.jsonl) · [页面](runs/T11/page.jpg) · [复算](runs/T11/audit.json) |
| T12 一分钟介绍 | completed | 58.0 / 60 | 5 | 100.6秒 | [脚本](runs/T12/script.md) · [Trace](runs/T12/trace.jsonl) · [页面](runs/T12/page.jpg) · [复算](runs/T12/audit.json) |
| T13 六秒入口 | completed | 5.5 / 6 | 5 | 83.5秒 | [脚本](runs/T13/script.md) · [Trace](runs/T13/trace.jsonl) · [页面](runs/T13/page.jpg) · [复算](runs/T13/audit.json) |
| T14 十秒双功能 | completed | 9.0 / 10 | 5 | 85.2秒 | [脚本](runs/T14/script.md) · [Trace](runs/T14/trace.jsonl) · [页面](runs/T14/page.jpg) · [复算](runs/T14/audit.json) |
| T15 十五秒概览 | completed | 13.0 / 15 | 5 | 87.2秒 | [脚本](runs/T15/script.md) · [Trace](runs/T15/trace.jsonl) · [页面](runs/T15/page.jpg) · [复算](runs/T15/audit.json) |
| T16 中年初学者 | completed | 26.0 / 30 | 5 | 87.5秒 | [脚本](runs/T16/script.md) · [Trace](runs/T16/trace.jsonl) · [页面](runs/T16/page.jpg) · [复算](runs/T16/audit.json) |
| T17 英文受众 | needs_input | None / 20 | 2 | 55.5秒 | [脚本](runs/T17/script.md) · [Trace](runs/T17/trace.jsonl) · [页面](runs/T17/page.jpg) · [复算](runs/T17/audit.json) |
| T18 双语字幕 | needs_input | None / 25 | 3 | 69.6秒 | [脚本](runs/T18/script.md) · [Trace](runs/T18/trace.jsonl) · [页面](runs/T18/page.jpg) · [复算](runs/T18/audit.json) |
| T19 四镜头交付 | completed | 21.0 / 24 | 5 | 83.2秒 | [脚本](runs/T19/script.md) · [Trace](runs/T19/trace.jsonl) · [页面](runs/T19/page.jpg) · [复算](runs/T19/audit.json) |
| T20 按钮教程 | needs_input | None / 40 | 3 | 62.7秒 | [脚本](runs/T20/script.md) · [Trace](runs/T20/trace.jsonl) · [页面](runs/T20/page.jpg) · [复算](runs/T20/audit.json) |
| T21 自动字幕咨询 | needs_input | None / 25 | 3 | 63.6秒 | [脚本](runs/T21/script.md) · [Trace](runs/T21/trace.jsonl) · [页面](runs/T21/page.jpg) · [复算](runs/T21/audit.json) |
| T22 翻译字幕咨询 | needs_input | None / 25 | 3 | 56.2秒 | [脚本](runs/T22/script.md) · [Trace](runs/T22/trace.jsonl) · [页面](runs/T22/page.jpg) · [复算](runs/T22/audit.json) |
| T23 字幕文件交付 | needs_input | None / 30 | 3 | 70.7秒 | [脚本](runs/T23/script.md) · [Trace](runs/T23/trace.jsonl) · [页面](runs/T23/page.jpg) · [复算](runs/T23/audit.json) |
| T24 费用说明 | needs_input | None / 25 | 3 | 67.1秒 | [脚本](runs/T24/script.md) · [Trace](runs/T24/trace.jsonl) · [页面](runs/T24/page.jpg) · [复算](runs/T24/audit.json) |
| T25 离线与隐私 | needs_input | None / 30 | 3 | 63.3秒 | [脚本](runs/T25/script.md) · [Trace](runs/T25/trace.jsonl) · [页面](runs/T25/page.jpg) · [复算](runs/T25/audit.json) |
| T26 导出质量 | needs_input | None / 30 | 3 | 66.4秒 | [脚本](runs/T26/script.md) · [Trace](runs/T26/trace.jsonl) · [页面](runs/T26/page.jpg) · [复算](runs/T26/audit.json) |
| T27 竞品选择 | needs_input | None / 45 | 3 | 69.1秒 | [脚本](runs/T27/script.md) · [Trace](runs/T27/trace.jsonl) · [页面](runs/T27/page.jpg) · [复算](runs/T27/audit.json) |
| T28 客户效果说法 | completed | 22.0 / 25 | 5 | 106.3秒 | [脚本](runs/T28/script.md) · [Trace](runs/T28/trace.jsonl) · [页面](runs/T28/page.jpg) · [复算](runs/T28/audit.json) |
| T29 老年学习需求 | needs_input | None / 35 | 3 | 70.3秒 | [脚本](runs/T29/script.md) · [Trace](runs/T29/trace.jsonl) · [页面](runs/T29/page.jpg) · [复算](runs/T29/audit.json) |
| T30 更新公告 | needs_input | None / 30 | 3 | 66.2秒 | [脚本](runs/T30/script.md) · [Trace](runs/T30/trace.jsonl) · [页面](runs/T30/page.jpg) · [复算](runs/T30/audit.json) |
| T31 客户未定时长 | needs_input | None / None | 0 | 0.0秒 | [脚本](runs/T31/script.md) · [Trace](runs/T31/trace.jsonl) · [页面](runs/T31/page.jpg) · [复算](runs/T31/audit.json) |
| T32 受众未确定 | needs_input | None / 20 | 0 | 0.0秒 | [脚本](runs/T32/script.md) · [Trace](runs/T32/trace.jsonl) · [页面](runs/T32/page.jpg) · [复算](runs/T32/audit.json) |
| T33 风格未确定 | needs_input | None / 20 | 0 | 0.0秒 | [脚本](runs/T33/script.md) · [Trace](runs/T33/trace.jsonl) · [页面](runs/T33/page.jpg) · [复算](runs/T33/audit.json) |
| T34 不出镜拍摄 | completed | 18.0 / 20 | 5 | 102.1秒 | [脚本](runs/T34/script.md) · [Trace](runs/T34/trace.jsonl) · [页面](runs/T34/page.jpg) · [复算](runs/T34/audit.json) |
| T35 静音展位 | completed | 18.0 / 20 | 5 | 89.2秒 | [脚本](runs/T35/script.md) · [Trace](runs/T35/trace.jsonl) · [页面](runs/T35/page.jpg) · [复算](runs/T35/audit.json) |
| T36 不加营销结尾 | completed | 16.0 / 18 | 5 | 79.4秒 | [脚本](runs/T36/script.md) · [Trace](runs/T36/trace.jsonl) · [页面](runs/T36/page.jpg) · [复算](runs/T36/audit.json) |
| T37 只有两个素材位 | completed | 15.0 / 16 | 5 | 78.7秒 | [脚本](runs/T37/script.md) · [Trace](runs/T37/trace.jsonl) · [页面](runs/T37/page.jpg) · [复算](runs/T37/audit.json) |
| T38 不用问句开场 | completed | 17.5 / 20 | 5 | 87.5秒 | [脚本](runs/T38/script.md) · [Trace](runs/T38/trace.jsonl) · [页面](runs/T38/page.jpg) · [复算](runs/T38/audit.json) |
| T39 客户指定标题 | needs_input | None / 25 | 1 | 18.7秒 | [脚本](runs/T39/script.md) · [Trace](runs/T39/trace.jsonl) · [页面](runs/T39/page.jpg) · [复算](runs/T39/audit.json) |
| T40 大字卡片 | needs_input | None / 20 | 3 | 74.4秒 | [脚本](runs/T40/script.md) · [Trace](runs/T40/trace.jsonl) · [页面](runs/T40/page.jpg) · [复算](runs/T40/audit.json) |
| T41 压缩客户旧稿 | completed | 24.0 / 30 | 7 | 126.7秒 | [脚本](runs/T41/script.md) · [Trace](runs/T41/trace.jsonl) · [页面](runs/T41/page.jpg) · [复算](runs/T41/audit.json) |
| T42 十秒旧稿改版 | completed | 9.0 / 10 | 7 | 112.3秒 | [脚本](runs/T42/script.md) · [Trace](runs/T42/trace.jsonl) · [页面](runs/T42/page.jpg) · [复算](runs/T42/audit.json) |
| T43 审阅外包旧稿 | completed | 25.0 / 25 | 7 | 123.5秒 | [脚本](runs/T43/script.md) · [Trace](runs/T43/trace.jsonl) · [页面](runs/T43/page.jpg) · [复算](runs/T43/audit.json) |
| T44 镜头顺序锁定 | completed | 19.0 / 20 | 7 | 116.3秒 | [脚本](runs/T44/script.md) · [Trace](runs/T44/trace.jsonl) · [页面](runs/T44/page.jpg) · [复算](runs/T44/audit.json) |
| T45 混入旧产品名称 | completed | 24.0 / 25 | 7 | 137.5秒 | [脚本](runs/T45/script.md) · [Trace](runs/T45/trace.jsonl) · [页面](runs/T45/page.jpg) · [复算](runs/T45/audit.json) |
| T46 新门店资料 | needs_input | None / 20 | 3 | 72.6秒 | [脚本](runs/T46/script.md) · [Trace](runs/T46/trace.jsonl) · [页面](runs/T46/page.jpg) · [复算](runs/T46/audit.json) |
| T47 游戏活动资料 | needs_input | None / 30 | 2 | 49.3秒 | [脚本](runs/T47/script.md) · [Trace](runs/T47/trace.jsonl) · [页面](runs/T47/page.jpg) · [复算](runs/T47/audit.json) |
| T48 客户口语化需求 | completed | 18.0 / 20 | 5 | 89.5秒 | [脚本](runs/T48/script.md) · [Trace](runs/T48/trace.jsonl) · [页面](runs/T48/page.jpg) · [复算](runs/T48/audit.json) |
| T49 同需求第二次交付 | completed | 25.0 / 30 | 5 | 99.7秒 | [脚本](runs/T49/script.md) · [Trace](runs/T49/trace.jsonl) · [页面](runs/T49/page.jpg) · [复算](runs/T49/audit.json) |
| T50 概览再次交付 | completed | 40.0 / 45 | 5 | 105.8秒 | [脚本](runs/T50/script.md) · [Trace](runs/T50/trace.jsonl) · [页面](runs/T50/page.jpg) · [复算](runs/T50/audit.json) |

每条目录包含冻结 brief、提交前后页面文字、结果截图、页面原始结果、后端六类原始产物和离线复算摘要。冻结清单中的真实业务需求不因结果改变；失败、资料缺口和不完整输出均保留。
