"""Loopback-only manual testing UI, using the same Agent as the CLI."""

import argparse
import copy
import hmac
import json
import os
import re
import secrets
import threading
import uuid
import webbrowser
from datetime import datetime, timezone
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse

from scripts.evaluate import scenarios
from .agent import Agent
from .cli import make_model
from .providers import discover_codex
from .reporting import save_run
from .schema import validate_request
from .tools import ROOT, ToolBox

PRESET_NAMES = {"normal": "正常生成", "missing_information": "缺少关键信息", "no_material": "没有产品素材",
                "tool_failure": "工具持续失败", "recoverable_failure": "一次故障后恢复", "over_duration": "38 秒旧稿修订",
                "rule_revision": "无依据宣传纠错", "impossible_duration": "无法满足的时长"}
DOWNLOADS = {"script.md", "input.json", "output.json", "trace.jsonl", "manifest.json", "data_snapshot.json"}


class BusyError(ValueError):
    pass


class RunManager:
    def __init__(self, output_root=None, model_factory=make_model):
        self.output_root = Path(output_root or ROOT / "outputs/web")
        self.model_factory = model_factory
        self.lock = threading.RLock()
        self.jobs = {}
        self.active_id = None
        self._restore()

    def _restore(self):
        """Restore only completed, saved runs; never resume model calls implicitly."""
        if not self.output_root.exists():
            return
        folders = sorted((p for p in self.output_root.iterdir() if p.is_dir() and re.fullmatch(r"[a-f0-9]{32}", p.name)),
                         key=lambda p: p.stat().st_mtime)[-32:]
        for folder in folders:
            try:
                request = json.loads((folder / "input.json").read_text(encoding="utf-8"))
                result = json.loads((folder / "output.json").read_text(encoding="utf-8"))
                manifest = json.loads((folder / "manifest.json").read_text(encoding="utf-8"))
                trace = [json.loads(line) for line in (folder / "trace.jsonl").read_text(encoding="utf-8").splitlines()]
                result["trace"] = trace
                self.jobs[folder.name] = {"id": folder.name, "provider": result["metadata"]["provider"],
                    "request": request, "created_at": result["metadata"]["started_at"], "state": "finished",
                    "phase": "finished", "step": len(trace), "result": result, "error": None, "saved": True,
                    "cancel_requested": False, "cancel_event": threading.Event(), "scenario_id": "custom",
                    "failures": manifest.get("fault_injection", {}),
                    **{key: result[key] for key in ("trace", "script", "duration", "rules_check")}}
            except (OSError, ValueError, KeyError, TypeError):
                continue

    def config(self):
        tools = ToolBox()
        presets = [{"id": name, "name": PRESET_NAMES[name], "request": request, "failures": failures,
                    "expected_status": sorted(expected)} for name, request, failures, expected in scenarios()]
        with self.lock:
            return {"app": "short-video-script-agent", "presets": presets, "materials": tools.materials[:3], "active_id": self.active_id,
                    "codex_available": bool(discover_codex()),
                    "api_available": bool(os.environ.get("MODEL_API_KEY") and os.environ.get("MODEL_NAME"))}

    def start(self, body):
        if not isinstance(body, dict):
            raise ValueError("请求必须为 JSON 对象")
        provider = body.get("provider", "codex")
        if provider not in {"codex", "mock", "api"}:
            raise ValueError("请选择有效的模型入口")
        request = body.get("request")
        validate_request(request)  # Missing fields are a valid manual negative test.
        failures = body.get("failures", {})
        if not isinstance(failures, dict) or any(k not in {"search_materials", "estimate_duration", "check_rules"}
                                                or type(v) is not int or not -1 <= v <= 3 for k, v in failures.items()):
            raise ValueError("故障设置无效")
        with self.lock:
            if self.active_id:
                raise BusyError("已有任务运行中，请等待完成或停止后续步骤。")
            if len(self.jobs) >= 32:
                self.jobs.pop(next(iter(self.jobs)))
            run_id = uuid.uuid4().hex
            job = {"id": run_id, "provider": provider, "request": copy.deepcopy(request),
                   "scenario_id": body.get("scenario_id") if body.get("scenario_id") in PRESET_NAMES else "custom",
                   "failures": copy.deepcopy(failures),
                   "created_at": datetime.now(timezone.utc).isoformat(), "state": "running", "phase": "starting",
                   "step": 0, "trace": [], "script": request.get("initial_script"), "duration": None,
                   "rules_check": None, "result": None, "error": None, "saved": False,
                   "cancel_requested": False, "cancel_event": threading.Event()}
            self.jobs[run_id] = job
            self.active_id = run_id
            worker = threading.Thread(target=self._work, args=(run_id, copy.deepcopy(failures)), daemon=True)
            worker.start()
            return run_id

    def _work(self, run_id, failures):
        with self.lock:
            job = self.jobs[run_id]
        def progress(event):
            with self.lock:
                job.update({"phase": event["kind"], **{k: event[k] for k in ("step", "trace", "script", "duration", "rules_check")}})
        try:
            model = self.model_factory(job["provider"], 180)
            tools = ToolBox(failures=failures)
            result = Agent(model, tools, on_event=progress, cancel_event=job["cancel_event"]).run(job["request"])
            save_run(self.output_root / run_id, job["request"], result, tools)
            with self.lock:
                job.update({"result": result, "state": "finished", "phase": "finished", "saved": True,
                            **{k: result[k] for k in ("trace", "script", "duration", "rules_check")}})
        except (ValueError, OSError) as exc:
            with self.lock:
                job.update(state="error", error=f"启动或保存失败：{exc}", phase="error")
        except Exception:
            # Never send a traceback or environment data to the browser.
            with self.lock:
                job.update(state="error", error="运行遇到异常，请检查本地服务日志后重试。", phase="error")
        finally:
            with self.lock:
                if self.active_id == run_id:
                    self.active_id = None

    def get(self, run_id):
        with self.lock:
            job = self.jobs.get(run_id)
            return copy.deepcopy({k: v for k, v in job.items() if k != "cancel_event"}) if job else None

    def recent(self):
        with self.lock:
            return [{"id": j["id"], "topic": j["request"].get("topic", "未命名需求"), "provider": j["provider"],
                     "state": j["state"], "status": (j["result"] or {}).get("status"), "created_at": j["created_at"]}
                    for j in reversed(list(self.jobs.values()))]

    def cancel(self, run_id):
        with self.lock:
            job = self.jobs.get(run_id)
            if not job:
                return False
            if job["state"] == "running":
                job["cancel_requested"] = True
                job["cancel_event"].set()
            return True


def make_server(port=8765, manager=None):
    manager = manager or RunManager()
    token = secrets.token_urlsafe(32)

    class Handler(BaseHTTPRequestHandler):
        def log_message(self, format, *args):
            pass

        def _headers(self, status, content_type, length):
            self.send_response(status)
            self.send_header("Content-Type", content_type)
            self.send_header("Content-Length", str(length))
            self.send_header("Cache-Control", "no-store")
            self.send_header("X-Content-Type-Options", "nosniff")
            self.send_header("Content-Security-Policy", "default-src 'self'; script-src 'self'; style-src 'self'; img-src 'self' data:; connect-src 'self'; frame-ancestors 'none'")
            self.send_header("Referrer-Policy", "no-referrer")

        def _send(self, status, payload, content_type="application/json; charset=utf-8", filename=None):
            data = json.dumps(payload, ensure_ascii=False, allow_nan=False).encode("utf-8") if isinstance(payload, (dict, list)) else payload
            self._headers(status, content_type, len(data))
            if filename:
                self.send_header("Content-Disposition", f'attachment; filename="{filename}"')
            self.end_headers()
            try:
                self.wfile.write(data)
            except (BrokenPipeError, ConnectionResetError):
                pass

        def _host_ok(self):
            allowed = {f"127.0.0.1:{self.server.server_port}", f"localhost:{self.server.server_port}"}
            return self.headers.get("Host") in allowed

        def do_GET(self):
            if not self._host_ok():
                return self._send(403, {"error": "仅允许本机访问"})
            path = urlparse(self.path).path
            static = {"/": ("index.html", "text/html; charset=utf-8"), "/app.js": ("app.js", "text/javascript; charset=utf-8"),
                      "/style.css": ("style.css", "text/css; charset=utf-8"), "/favicon.svg": ("favicon.svg", "image/svg+xml")}
            if path in static:
                name, kind = static[path]
                return self._send(200, (ROOT / "web" / name).read_bytes(), kind)
            if path == "/api/config":
                return self._send(200, {**manager.config(), "token": token})
            if path == "/api/runs":
                return self._send(200, manager.recent())
            match = re.fullmatch(r"/api/runs/([a-f0-9]{32})(?:/download/([a-z_.]+))?", path)
            if match:
                run_id, filename = match.groups()
                job = manager.get(run_id)
                if job and not filename:
                    return self._send(200, job)
                if job and job["saved"] and filename in DOWNLOADS:
                    try:
                        return self._send(200, (manager.output_root / run_id / filename).read_bytes(), "application/octet-stream", filename)
                    except OSError:
                        return self._send(404, {"error": "记录文件不可用"})
            return self._send(404, {"error": "未找到任务或文件"})

        def do_POST(self):
            origin = self.headers.get("Origin")
            allowed_origins = {f"http://127.0.0.1:{self.server.server_port}", f"http://localhost:{self.server.server_port}"}
            if (not self._host_ok() or (origin and origin not in allowed_origins)
                    or not hmac.compare_digest(self.headers.get("X-Local-Token", ""), token)):
                return self._send(403, {"error": "请求校验失败，请刷新本地页面"})
            try:
                length = int(self.headers.get("Content-Length", "0"))
                if not 0 < length <= 65536:
                    return self._send(413, {"error": "请求过大或为空"})
                if self.headers.get_content_type() != "application/json":
                    return self._send(415, {"error": "需要 JSON 请求"})
                body = json.loads(self.rfile.read(length), parse_constant=lambda _: (_ for _ in ()).throw(ValueError("非法数值")))
                path = urlparse(self.path).path
                if path == "/api/runs":
                    return self._send(202, {"id": manager.start(body)})
                match = re.fullmatch(r"/api/runs/([a-f0-9]{32})/cancel", path)
                if match and manager.cancel(match.group(1)):
                    return self._send(200, {"ok": True})
                return self._send(404, {"error": "任务不存在"})
            except BusyError as exc:
                return self._send(409, {"error": str(exc)})
            except (ValueError, TypeError) as exc:
                return self._send(400, {"error": str(exc)})

    server = ThreadingHTTPServer(("127.0.0.1", port), Handler)
    server.daemon_threads = True
    return server


def main():
    parser = argparse.ArgumentParser(description="短视频脚本 Agent 本地人工测试页面")
    parser.add_argument("--port", type=int, default=8765)
    parser.add_argument("--open", action="store_true", help="启动后打开浏览器")
    args = parser.parse_args()
    if not 1 <= args.port <= 65535:
        parser.error("端口应为 1–65535")
    try:
        server = make_server(args.port)
    except OSError:
        if args.open:
            try:
                from urllib.request import urlopen
                with urlopen(f"http://127.0.0.1:{args.port}/api/config", timeout=2) as response:
                    if json.load(response).get("app") == "short-video-script-agent":
                        webbrowser.open(f"http://127.0.0.1:{args.port}")
                        return
            except (OSError, ValueError):
                pass
        parser.exit(2, f"端口 {args.port} 无法使用；若网页已启动可直接访问，否则使用 --port 指定其他端口。\n")
    url = f"http://127.0.0.1:{server.server_port}"
    print(f"脚本测试页面已启动：{url}\n关闭本窗口或按 Ctrl+C 停止服务。", flush=True)
    if args.open:
        webbrowser.open(url)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
