"""Human-readable script and machine-readable reproducibility artifacts."""

import json
from pathlib import Path


def render_report(result):
    lines = ["# 短视频脚本运行结果", "", f"- 状态：`{result['status']}`",
             f"- 证据类型：`{result['metadata']['evidence_kind']}`",
             f"- 说明：{result['message']}", ""]
    script = result.get("script")
    if script:
        lines += [f"## {script['title']}", "", "> 未完成或检查失败时，下列内容仅为未通过验收的草稿。", ""]
        timings = {s["shot"]: s["estimated_seconds"] for s in (result.get("duration") or {}).get("shots", [])}
        for i, shot in enumerate(script["shots"], 1):
            lines += [f"### 分镜 {i}", "", f"画面：{shot['visual']}", "",
                      "旁白/字幕：" + "".join(b["text"] for b in shot["blocks"]), "",
                      "来源：" + ", ".join(b["source_id"] + "/" + b["fact_id"] for b in shot["blocks"] if b["source_id"]), "",
                      f"预计镜头时长：{timings.get(i, '未检查')} 秒", ""]
    duration = result.get("duration") or {}
    lines += [f"预计总时长：{duration.get('total_seconds', '未检查')} 秒（基于语速与镜头停留估算，非成片实测）。", "",
              "## 检查结果与来源", "", "```json", json.dumps(result.get("rules_check"), ensure_ascii=False, indent=2), "```", "",
              "## 执行路径", "", " → ".join(t["action"] for t in result["trace"]), "",
              "逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。", ""]
    return "\n".join(lines)


def save_run(directory, request, result, tools):
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    files = {"input.json": request, "output.json": {k: v for k, v in result.items() if k != "trace"},
             "data_snapshot.json": {"materials": tools.materials, "rules": tools.rules},
             "manifest.json": {**result["metadata"], "fault_injection": tools.initial_failures if hasattr(tools, "initial_failures") else {}}}
    for name, content in files.items():
        (directory / name).write_text(json.dumps(content, ensure_ascii=False, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    (directory / "trace.jsonl").write_text("".join(json.dumps(e, ensure_ascii=False, allow_nan=False) + "\n" for e in result["trace"]), encoding="utf-8")
    (directory / "script.md").write_text(render_report(result), encoding="utf-8")
