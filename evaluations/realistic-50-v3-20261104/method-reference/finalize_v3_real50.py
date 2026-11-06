"""Validate archived real web experiments; never invoke a model or Mock."""
import csv
import hashlib
import json
import zipfile
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
B = ROOT / 'evaluations/realistic-50-v3-20261104'
load = lambda p: json.loads(p.read_text(encoding='utf-8-sig'))
sha = lambda data: hashlib.sha256(data).hexdigest()
cases = load(B / 'cases.json')
results = load(B / 'results.json')
baseline = load(B / 'baseline.json')
assert len(cases) == results['archived'] == results['actual_model_runs'] == 50
assert results['old_files_checked'] == len(baseline['preserved_sha256'])
assert not results['old_files_changed'] and results['all_available_replays_passed']
assert {r['case'] for r in results['runs']} == {c['id'] for c in cases}
assert len({r['run_id'] for r in results['runs']}) == 50
by_id = {r['case']: r for r in results['runs']}
reviews = []
copied_files = 0
for c in cases:
    d = B / 'runs' / c['id']
    assert load(d / 'brief.json') == c
    ui = load(d / 'ui-input.json')['fields']
    req = c['request']
    for field, key in {'topic':'topic', 'audience':'audience', 'platform':'platform',
                       'style':'style', 'product':'product_id',
                       'duration-mode':'duration_mode', 'expression-mode':'expression_mode'}.items():
        assert ui[field] == req[key], (c['id'], field)
    assert float(ui['target-seconds']) == req['target_seconds']
    assert ui['provider'] == 'codex' and ui['fault'] == 'none'
    assert (json.loads(ui['initial-script']) if ui['initial-script'] else None) == req.get('initial_script')
    assert all((d / name).is_file() for name in ('before.txt','submitted.txt','after.txt','page.jpg','capture.json','review.json'))
    row = by_id[c['id']]
    review = load(d / 'review.json')
    reviews.append({**row, **review, 'evidence':f"runs/{c['id']}/"})
    if row['responses'] is not None:
        m = load(d / 'manifest.json')
        assert m['provider'] == 'codex' and m['evidence_kind'] == 'real_model'
        assert m['model_responses'] > 0 and not m['fault_injection']
        for name in ('input.json','output.json','trace.jsonl','manifest.json','data_snapshot.json','script.md'):
            assert (d / name).read_bytes() == (ROOT / 'outputs/web' / row['run_id'] / name).read_bytes()
            copied_files += 1
    else:
        assert row['response_lower_bound'] > 0
        assert all((d / n).is_file() for n in ('partial-output.json','partial-trace-ui.json','infrastructure-error.json'))

distinct = {json.dumps(c['request'],ensure_ascii=False,sort_keys=True) for c in cases}
assert len(distinct) == 49 and cases[0]['request'] == cases[49]['request']
attempts = []
for d in sorted((B / 'attempts').iterdir()):
    if not d.is_dir():
        continue
    capture = load(d / 'capture.json')
    manifest = load(d / 'manifest.json')
    assert manifest['provider'] == 'codex' and manifest['model_responses'] == 0
    for name in ('input.json','output.json','trace.jsonl','manifest.json','data_snapshot.json','script.md'):
        assert (d / name).read_bytes() == (ROOT / 'outputs/web' / capture['run_id'] / name).read_bytes()
    attempts.append({'folder':d.relative_to(B).as_posix(), **capture})
zip_path = ROOT / '小影科技笔试_第4题_v3优化版.zip'
with zipfile.ZipFile(zip_path) as z:
    names = z.namelist()
    release_match = {}
    for relative, expected in baseline['source_sha256'].items():
        candidates = [n for n in names if n == relative or n.endswith('/' + relative)]
        assert len(candidates) == 1, (relative, candidates)
        release_match[relative] = sha(z.read(candidates[0])) == expected
assert all(release_match.values())
with (B / '逐条复盘.csv').open('w',encoding='utf-8-sig',newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['case','name','status','assessment','note','seconds','target','duration_mode','steps','responses','response_lower_bound','evidence','reviewer'], extrasaction='ignore')
    writer.writeheader(); writer.writerows(reviews)
validation = {
    'verified_at':datetime.now(timezone.utc).isoformat(),
    'archived_experiments':50, 'distinct_requests':49, 'unique_run_ids':50,
    'additional_zero_response_attempts':len(attempts),
    'additional_attempts':attempts,
    'all_ui_inputs_match_frozen':True, 'all_ui_provider_codex':True,
    'fault_injection':False, 'per_case_screenshots_and_reviews':50,
    'canonical_files_equal_backend':copied_files,
    'canonical_records':results['complete_records_replayed'],
    'partial_records':results['partial_records'],
    'exact_response_count_available_subset':results['model_responses_exact_subset'],
    'total_model_responses_lower_bound':results['model_responses_lower_bound'],
    'cases_sha256':sha((B/'cases.json').read_bytes()),
    'source_and_data_unchanged':True,
    'source_files_matching_v3_release':len(release_match),
    'v3_release_zip_sha256':sha(zip_path.read_bytes()),
    'old_files_unchanged':results['old_files_checked'],
    'statuses':results['statuses'],
    'review_assessments':dict(Counter(r['assessment'] for r in reviews)),
    'limits':['Developer AI review, not independent blind review',
              'Real model calls with synthetic briefs and product data',
              'Saved-record replay checks consistency, not semantic truth',
              'Three partial records do not have canonical backend artifacts',
              'V50 intentionally repeats V01; no independent repeatability estimate'],
}
(B/'validation.json').write_text(json.dumps(validation,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps(validation,ensure_ascii=False))
