"""Summarize the two fixed-input webpage replays without altering their records."""
import hashlib
import json
from datetime import datetime
from pathlib import Path

from scripts.verify_evidence import verify_run

ROOT = Path(__file__).resolve().parents[2]
OUT = Path(__file__).resolve().parent
RUNS = {'character': 'fed3daae67fe48dfbbfffadbe15017e0',
        'candle': '6a9f42fc29f34d1a9451b51fe4517fd9'}


def read(path):
    return json.loads(path.read_text(encoding='utf-8'))


def summarize(run_id):
    folder = ROOT / 'outputs/web' / run_id
    result = read(folder / 'output.json')
    metadata = result['metadata']
    trace = [json.loads(line) for line in (folder / 'trace.jsonl').read_text(encoding='utf-8').splitlines()]
    diagnostics = [read(p) for p in (folder / 'diagnostics').glob('*.json')]
    elapsed = (datetime.fromisoformat(metadata['finished_at']) -
               datetime.fromisoformat(metadata['started_at'])).total_seconds()
    return {
        'web_run_id': run_id, 'version': metadata['app_version'],
        'status': result['status'], 'elapsed_seconds': round(elapsed, 2),
        'estimated_video_seconds': (result.get('duration') or {}).get('total_seconds'),
        'model_responses': metadata['model_responses'], 'attempts': len(diagnostics),
        'timeouts': sum(d.get('error_code') == 'codex_timeout' for d in diagnostics),
        'recovered_responses': sum(bool(d['metadata'].get('recovered_attempts'))
                                   and d.get('response_received', False) for d in diagnostics),
        'checks': {k: bool(result.get(k, {}).get('ok') and result.get(k, {}).get('passed'))
                   for k in ('duration', 'rules_check', 'requirements_check')},
        'models': sorted({d['metadata']['model'] for d in diagnostics}),
        'configuration_modes': sorted({d['metadata'].get('configuration_mode', 'legacy_inherited')
                                        for d in diagnostics}),
        'actions': [e['action'] for e in trace],
        'input_sha256': hashlib.sha256((folder / 'input.json').read_bytes()).hexdigest(),
        'data_hash': metadata['data_hash'],
    }


if __name__ == '__main__':
    results = []
    for case in read(OUT / 'cases.json'):
        name = case['name']
        before, after = summarize(case['prior_run_id']), summarize(RUNS[name])
        folder = ROOT / 'outputs/web' / RUNS[name]
        results.append({
            'case': name, 'before': before, 'after': after,
            'input_unchanged': read(folder / 'input.json') == case['input'],
            'materials_unchanged': before['data_hash'] == after['data_hash'],
            'evidence_errors': verify_run(folder),
            'elapsed_reduction_seconds': round(before['elapsed_seconds'] - after['elapsed_seconds'], 2),
        })
    (OUT / 'live-results.json').write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding='utf-8')
    print(json.dumps(results, ensure_ascii=False, indent=2))
