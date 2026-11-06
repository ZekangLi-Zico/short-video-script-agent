"""Copy selected actual records, preserving every byte of the original output."""
import json,shutil
from pathlib import Path
B=Path(__file__).resolve().parent;T=B.parents[1]/'examples/v6-live'
items={'V01':'早餐摊标题与场景','V05':'上轮超时的修理铺需求','V22':'中英双语需求','V28':'45秒功能介绍','V45':'旧稿压缩','V34':'收费资料缺口','V46':'旧稿无依据宣传'}
T.mkdir(parents=True,exist_ok=True)
lines=['# v6实际网页证据精选','','全部来自正式50次网页实验，复制实际产物，没有重新生成。完整结果见 [50次索引](../../evaluations/realistic-50-v6-20261105/README.md)。','','|案例|核对重点|实际状态|证据|','|---|---|---|---|']
for case,label in items.items():
    d=B/'runs'/case;shutil.copytree(d,T/case)
    o=json.loads((d/'output.json').read_text(encoding='utf8'))
    lines.append(f'|{case}|{label}|{o["status"]}|[输入]({case}/input.json) · [脚本]({case}/script.md) · [Trace]({case}/trace.jsonl) · [评阅]({case}/review.json)|')
lines+=['','历史故障实验仍在examples/live、examples/mock及旧评估目录，版本标签不变；正式50次不注入故障，不能当作本版重新执行了所有受控故障场景。129项离线自动测试仅证明代码契约，不计作真实模型实验。']
(T/'evaluation.md').write_text('\n'.join(lines)+'\n',encoding='utf8')
