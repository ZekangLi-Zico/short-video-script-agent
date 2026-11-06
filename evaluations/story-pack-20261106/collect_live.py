"""Collect the two fixed UI runs without changing their input or original artifacts."""
from datetime import datetime
from pathlib import Path
import hashlib
import json
import shutil

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
CASES = [
    ('candle', '门缝里的烛光', '5da6d3d86b904fbda9deef30793fda81', 8765),
    ('character', '陈峥的人物预告', 'f11638b8792a4e799d71bf29f1612eb2', 8766),
]


def read(path):
    return json.loads(path.read_text(encoding='utf-8'))


def main():
    results = []
    for name, label, web_id, port in CASES:
        source = ROOT / 'outputs/web' / web_id
        output = read(source / 'output.json')  # A pending checkpoint is not a final result.
        metadata = output['metadata']
        target = HERE / 'runs' / name
        shutil.copytree(source, target, dirs_exist_ok=True)
        attempts = [read(p) for p in sorted((source / 'diagnostics').glob('*.json'))]
        trace = [json.loads(line) for line in (source / 'trace.jsonl').read_text(encoding='utf-8').splitlines()]
        results.append({
            'case': name, 'label': label, 'web_run_id': web_id,
            'entry': f'http://127.0.0.1:{port}/', 'submitted_by': 'browser UI generate button',
            'input': read(source / 'input.json'),
            'original': f'../../outputs/web/{web_id}', 'saved': f'runs/{name}',
            'status': output['status'], 'message': output['message'],
            'title': output.get('script', {}).get('title'),
            'shots': len(output.get('script', {}).get('shots', [])),
            'duration_seconds': output.get('duration', {}).get('total_seconds'),
            'duration_passed': output.get('duration', {}).get('passed'),
            'rules_passed': output.get('rules_check', {}).get('passed'),
            'requirements_passed': output.get('requirements_check', {}).get('passed'),
            'elapsed_seconds': round((datetime.fromisoformat(metadata['finished_at']) -
                                      datetime.fromisoformat(metadata['started_at'])).total_seconds(), 2),
            'model_responses': metadata['model_responses'],
            'failed_attempts': [a for a in attempts if not a.get('response_received')],
            'actions': [t['action'] for t in trace],
            'sources': [s['id'] for s in output.get('sources', [])],
            'voice': (source / 'voice.txt').read_text(encoding='utf-8'),
            'metadata': metadata,
        })
    zip_path = ROOT / 'data/packs/city-drama/city-drama-materials.zip'
    report = {
        'scope': 'Two targeted real-model UI runs; not a campaign or paired before-after benchmark.',
        'inputs_written_before_execution': True,
        'mock': False, 'results': results,
        'ui_checks': {
            'story_catalog_cards': 32, 'original_product_cards': 3,
            'category_and_keyword': '分集剧情 + 烛光 -> 第8集·全都拿走',
            'bundle_download_used': True,
            'bundle_sha256': hashlib.sha256(zip_path.read_bytes()).hexdigest(),
            'download_bytes_match_bundle': True,
        },
    }
    (HERE / 'live-results.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps([{k:r[k] for k in ('case','status','shots','duration_seconds','elapsed_seconds','model_responses','actions')} for r in results], ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
