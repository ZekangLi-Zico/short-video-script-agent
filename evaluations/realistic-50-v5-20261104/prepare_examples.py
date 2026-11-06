"""Copy representative actual records for the exam's examples/ review entry."""
import json, shutil
from pathlib import Path
B=Path(__file__).resolve().parent
target=B.parents[1]/'examples/v5-live'
items={'V22':'双语事实表达与声画同步','V30':'八秒三功能短表达','V45':'旧稿45秒到13秒的有效修订',
       'V25':'超出单功能范围后实际修订','V46':'删除无依据宣传并保留叙事',
       'V34':'收费资料不足的明确缺口','V05':'真实模型超时与已保存失败记录'}
target.mkdir(parents=True,exist_ok=True)
lines=['# v5真实网页证据精选','',
       '以下全部来自冻结版本的50次真实网页实验，复制原始记录，没有重新生成或修饰结果。完整50组及旧版对照在 `evaluations/realistic-50-v5-20261104/`。','',
       '|例子|核对重点|实际结果|证据|','|---|---|---|---|']
for case,title in items.items():
    source=B/'runs'/case
    shutil.copytree(source,target/case)
    o=json.loads((source/'output.json').read_text(encoding='utf8'))
    lines.append(f'|{case}|{title}|{o["status"]}|[输入]({case}/input.json) · [输出]({case}/script.md) · [Trace]({case}/trace.jsonl) · [评阅]({case}/review.json)|')
lines += ['', '正常、资料不足、模型故障及多种动态修订均可直接查看。原题完整的8类验收（含缺必填字段、空素材、受控业务工具故障）仍在 `examples/live/`、`examples/mock/` 和历史定向实验中，均保留原版本标签；本次自然场景50组未注入故障，不将历史故障实验冒充v5新跑结果。',
          '', '自动测试的新结果见 `evaluations/realistic-50-v5-20261104/development-tests/final/`，118项全部通过；离线测试不计入50次真实实验。']
(target/'evaluation.md').write_text('\n'.join(lines)+'\n',encoding='utf8')
print(str(target))
