"""Replay one recorded decision with the real adapter; save only public output and safe diagnostics."""
import argparse
import hashlib
import json
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
import src.providers as providers
from src.schema import ACTION_SCHEMA

HERE = Path(__file__).resolve().parent
RUN = ROOT / 'outputs/web/a4c3fd45ef0243d1a78c8506e5b5228a'


def read(p):
    return json.loads(p.read_text(encoding='utf-8'))


def safe_events(stdout, stderr):
    if isinstance(stdout, bytes): stdout = stdout.decode('utf-8', errors='replace')
    if isinstance(stderr, bytes): stderr = stderr.decode('utf-8', errors='replace')
    events = []
    for line in (stdout or '').splitlines():
        try: event = json.loads(line)
        except ValueError: continue
        item = event.get('item', {})
        safe = {'type':event.get('type')}
        if item.get('type'): safe['item_type'] = item['type']
        if event.get('usage'): safe['usage'] = event['usage']
        if event.get('thread_id'): safe['thread_id'] = event['thread_id']
        message = str(event.get('message', '')) + str(event.get('error', ''))
        safe['signals'] = [key for key in ('capacity','429','401','403','timeout','stream disconnected','retry','reconnect','connection') if key in message.lower()]
        events.append(safe)
    return {'events':events, 'stderr_bytes':len((stderr or '').encode()),
            'stderr_signals':{key:(stderr or '').lower().count(key) for key in ('mcp','timeout','capacity','429','401','403','error','failed','retry','connect')}}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', choices=['baseline','isolated'], required=True)
    parser.add_argument('--timeout', type=int, default=180)
    args = parser.parse_args()
    result = read(RUN/'output.json')
    request = read(RUN/'input.json')
    history = [json.loads(s) for s in (RUN/'trace.jsonl').read_text(encoding='utf-8').splitlines()]
    history = [h for h in history if h['action'] != 'model_error']
    state = {'request':request, 'script':result['script'],
             'retrieved':{s['id']:s for s in result['sources']},
             'duration':result['duration'], 'rules_check':result['rules_check'],
             'requirements_check':result['requirements_check'], 'history':history, 'max_steps':12}
    rules = read(RUN/'data_snapshot.json')['rules']
    content = providers.payload(state, rules)
    report = {'mode':args.mode,'source_run':RUN.name,'timeout_seconds':args.timeout,
              'payload_bytes':len(content.encode()),'payload_sha256':hashlib.sha256(content.encode()).hexdigest(),
              'invocation_overrides':{'ignore_user_config':args.mode=='isolated',
                                      'explicit_model':'gpt-6-astra' if args.mode=='isolated' else None}}
    folder = HERE / args.mode
    folder.mkdir(parents=True, exist_ok=True)
    (folder/'state.json').write_text(json.dumps(state,ensure_ascii=False,indent=2),encoding='utf-8')
    model = providers.CodexModel(timeout=args.timeout)
    model.diagnostics_dir = folder/'diagnostics'
    original_run = providers.run_cli

    def capture(command, **kw):
        if args.mode == 'isolated':
            command = command[:2]+['--ignore-user-config','--model','gpt-6-astra']+command[2:]
        out = Path(command[command.index('--output-last-message')+1])
        (folder/'active.json').write_text(json.dumps({'output_file':str(out),'pid':__import__('os').getpid()}),encoding='utf-8')
        try:
            process = original_run(command, **kw)
            report.update(safe_events(process.stdout,process.stderr))
            return process
        except subprocess.TimeoutExpired as exc:
            report.update(safe_events(exc.stdout,exc.stderr))
            raise
        finally:
            report['output_file_exists_at_exit'] = out.exists()
            if out.exists():
                try: report['output_at_exit'] = read(out)
                except (ValueError,OSError): report['output_at_exit_invalid'] = True
    providers.run_cli = capture
    tick = time.monotonic()
    try:
        action,meta = model._generate(providers.SYSTEM+providers.NARRATIVE_SYSTEM,content,ACTION_SCHEMA)
        report.update(ok=True,action=action,metadata=meta)
    except Exception as exc:
        report.update(ok=False,error_type=type(exc).__name__,error=str(exc))
    finally:
        report['elapsed_seconds'] = round(time.monotonic()-tick,2)
        (folder/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(report,ensure_ascii=False,indent=2))
    return 0 if report['ok'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
