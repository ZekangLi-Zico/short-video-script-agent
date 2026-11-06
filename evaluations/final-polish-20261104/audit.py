"""Read-only checks of saved runs; writes only this campaign's audit.json."""
import hashlib
import json
import sys
from collections import Counter
from datetime import datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))
from scripts.evaluate import check_case
from scripts.verify_evidence import verify_run

HERE = Path(__file__).resolve().parent
read = lambda p: json.loads(p.read_text(encoding='utf-8-sig'))
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
baseline = read(HERE / 'baseline.json')
source = read(HERE / 'tested-source.json')
cases = read(HERE / 'cases.json')
errors, rows = [], []
for label, manifest in [('historical', baseline['preserved_files']), ('tested_source', source)]:
    for name, digest in manifest.items():
        p = ROOT / name
        if not p.is_file() or sha(p) != digest:
            errors.append(f'{label}: {name} changed or missing')
if sha(ROOT / baseline['archive']) != baseline['archive_sha256']:
    errors.append('source archive changed')
if sha(HERE / 'cases.json') != (HERE / 'cases.sha256').read_text().strip():
    errors.append('frozen cases changed')
for c in cases:
    d = HERE / 'runs' / c['id']
    if not (d / 'capture.json').exists():
        errors.append(f"{c['id']}: capture missing")
        continue
    out, inp, manifest, capture = [read(d / n) for n in ('output.json','input.json','manifest.json','capture.json')]
    # Saved output deliberately keeps Trace in a separate JSONL artifact.
    out['trace'] = [json.loads(line) for line in (d/'trace.jsonl').read_text(encoding='utf-8').splitlines()]
    row_errors = []
    if inp != c['request']: row_errors.append('input differs from frozen request')
    ui = read(d/'ui-input.json')
    if datetime.fromisoformat(manifest['started_at']) < datetime.fromisoformat(ui['submitted_at'].replace('Z','+00:00')) - timedelta(seconds=2):
        row_errors.append('result predates UI submission')
    if manifest['fault_injection'] != c['failures']: row_errors.append('fault settings differ')
    row_errors += verify_run(d)
    scenario = {'P01':'rule_revision','P02':'normal','P03':'over_duration','P04':'rule_revision'}.get(c['id'], c['source'])
    expected = {'missing_information':{'needs_input'}, 'no_material':{'needs_input','blocked'},
                'tool_failure':{'blocked','step_limit'}}.get(scenario, {'completed'})
    row_errors += check_case(scenario, out, expected)
    diagnostics = [read(p) for p in (d / 'diagnostics').glob('*.json')]
    response_ids = {e['call_id'] for e in diagnostics if e.get('response_received')}
    trace_ids = {e[k]['call_id'] for e in out['trace'] for k in ('model','review_model')
                 if isinstance(e.get(k),dict) and e[k].get('call_id')}
    if response_ids != trace_ids: row_errors.append('diagnostic/trace call IDs differ')
    if len(response_ids) != manifest['model_responses']: row_errors.append('response count differs')
    if manifest['provider'] != 'codex': row_errors.append('wrong provider')
    if c['id'] == 'P05':
        if response_ids: row_errors.append('missing-field validation called model')
    elif not response_ids: row_errors.append('no real-model response')
    origin = ROOT / 'outputs/web' / capture['run_id']
    for p in origin.rglob('*'):
        if p.is_file():
            copied = d / p.relative_to(origin)
            if not copied.is_file() or sha(p) != sha(copied): row_errors.append('backend copy mismatch: '+p.name)
    if not (d/'page.png').is_file() or not (d/'ui-input.json').is_file(): row_errors.append('UI evidence missing')
    rows.append({**capture,'checks_passed':not row_errors,'errors':row_errors,
                 'path':' -> '.join(e['action'] for e in out['trace']),
                 'diagnostic_responses':len(response_ids)})
    errors += [c['id']+': '+e for e in row_errors]
old_errors = []
old_dirs = sorted((ROOT/'evaluations/realistic-50-v4-20261104/runs').glob('V[0-9][0-9]'))
for d in old_dirs:
    old_errors += [d.name+': '+e for e in verify_run(d)]
errors += old_errors
report = {'passed':not errors,'errors':errors,'old_files_unchanged':len(baseline['preserved_files']),
          'tested_source_files':len(source),'previous_v4_runs_replayed':len(old_dirs),
          'web_cases':len(rows),'real_model_runs':sum(r['responses']>0 for r in rows),
          'model_responses':sum(r['responses'] for r in rows),
          'statuses':dict(Counter(r['status'] for r in rows)), 'rows':rows,
          'scope':'Internal evidence consistency and deterministic tool replay, not independent semantic certification.'}
(HERE/'audit.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in report.items() if k!='rows'},ensure_ascii=False))
sys.exit(0 if report['passed'] else 1)
