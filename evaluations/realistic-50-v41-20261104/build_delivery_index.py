"""Build evidence navigation from final audited records; no model calls."""
import json
from datetime import datetime, timezone
from pathlib import Path

B = Path(__file__).resolve().parent
load = lambda p: json.loads(p.read_text(encoding="utf-8-sig"))
r, obs = load(B / "results.json"), load(B / "observations.json")
assert r["archived"] == 50 and not r["errors"] and obs["reviewed"] == 50
lines = ["# v4.1：50 次真实模型网页复测证据", "",
    "50 次网页真实模型实验，317 次响应：36 completed、14 needs_input。每次只提交一次，无零响应补跑，无Mock或故障注入。原始输入与v4完全一致；结果不是50次全通过。", "",
    "- [完整复盘](复盘报告.md)", "- [两轮量化对照](前后对照.csv)",
    "- [两轮逐稿评阅](逐条复盘.csv)", "- [最终审计](results.json)",
    "- [观察与自然异常汇总](observations.json)", "- [冻结输入](cases.json)",
    "- [实验方法](实验方法.md)及[并发调整](protocol-amendment-01.md)",
    "- [评阅口径](评阅标准.md)", "- [修改前v4记录](../realistic-50-v4-20261104/README.md)",
    "- [同版本定向验收与故障测试](../final-polish-20261104/README.md)", "",
    "每个目录包含brief、实际网页字段、提交前后DOM、截图、输入、输出、Trace、数据快照、脚本、manifest、checkpoint/run、调用诊断、review与audit。截图默认显示执行过程；最终纠错脚本预览另见 [final-web.png](final-web.png)。", "",
    "|案例|场景|状态|步数 / 响应|估时秒|原始记录|", "|---|---|---|---:|---:|---|"]
for x in r["runs"]:
    d = "runs/" + x["folder"]
    sec = "—" if x["seconds"] is None else str(x["seconds"])
    lines.append(f"|{x['case']}|{x['name']}|{x['status']}|{x['steps']} / {x['responses']}|{sec}|[需求]({d}/brief.json) · [输出]({d}/script.md) · [Trace]({d}/trace.jsonl) · [截图]({d}/page.png) · [评阅]({d}/review.json)|")
lines += ["", "真实运行窗口08:55:22—09:54:52（北京时间）。这些是AI执行与等待时间，不是候选人个人手写耗时。原完整工作区审计核对41项版本文件和5820项历史文件；提交快照不嵌套全部旧根ZIP，其完整性以包内DELIVERY.json和外部校验文件为准。", ""]
(B / "README.md").write_text("\n".join(lines), encoding="utf-8")
(B / "work-session.json").write_text(json.dumps({
    "kind": "real_model_web_campaign", "version": "v4.1-final-polish",
    "model_started_at": obs["first_started_at"], "model_finished_at": obs["last_finished_at"],
    "reported_at": datetime.now(timezone.utc).isoformat(), "cases": 50, "unique_inputs": 49,
    "responses": 317, "application_changed": False, "zero_response_attempts": 0,
    "fault_injection": False, "mock_runs": 0, "submission_path": "browser form UI",
    "initial_concurrency": 2, "later_concurrency": 4,
    "review_helper_event": {"exit_code": -1073741502,
        "action": "V44 review.json writer process failed to start; absence verified then writer rerun",
        "model_experiment_repeated": False},
    "note": "AI execution and model waiting, not candidate independent work time. No GitHub push or exam submission."
}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
print(json.dumps({"indexed": len(r["runs"]), "reviewed": obs["reviewed"]}))
