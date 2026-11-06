"""Read preserved evidence, then write a separate limited-repair audit."""
import hashlib
import json
from datetime import datetime, timezone

from scripts.evaluate import check_case, scenarios
from scripts.verify_evidence import verify_run
from src.tools import ROOT, read_json


def load_result(directory):
    result = read_json(directory / 'output.json')
    result['trace'] = [json.loads(line) for line in (directory / 'trace.jsonl').read_text(encoding='utf-8').splitlines()]
    return result


def main():
    root = ROOT / 'examples/repairs'
    frozen = ROOT / 'evaluations/realistic-50-20261103'
    checksums = read_json(frozen / 'checksums.sha256.json')
    changed = [name for name, sha in checksums.items()
               if not (frozen / name).is_file() or hashlib.sha256((frozen / name).read_bytes()).hexdigest() != sha]
    cases = {case['id']: case for case in read_json(frozen / 'cases.json')}
    expected = {name: statuses for name, _, _, statuses in scenarios()}
    rows, comparisons, attempts = [], [], []
    groups = {'mock': list(expected), 'live-verified': list(expected), 'ui': ['T02', 'T28', 'T43'],
              'mock-final': list(expected), 'live-final': ['normal', 'over_duration'], 'ui-final': ['T43']}
    for group, names in groups.items():
        for name in names:
            directory = root / group / name
            if not (directory / 'output.json').is_file():
                rows.append({'run': f'{group}/{name}', 'passed': False, 'errors': ['missing evidence']})
                continue
            result = load_result(directory)
            errors = verify_run(directory)
            if not group.startswith('ui'):
                errors += check_case(name, result, expected[name])
            else:
                if read_json(directory / 'input.json') != cases[name]['request']:
                    errors.append('网页输入与冻结简报不一致')
                if read_json(directory / 'ui-result.json') != result:
                    errors.append('网页结果与落盘结果/Trace不一致')
                old = read_json(frozen / 'runs' / name / 'output.json')
                comparisons.append({'case': name, 'group': group, 'before_status': old['status'], 'after_status': result['status'],
                                    'before_message': old['message'], 'after_message': result['message'],
                                    'requirements_review_executed': result['requirements_check'] is not None,
                                    'note': 'States are actual outputs, not a business pass-rate label.'})
            rows.append({'run': f'{group}/{name}', 'passed': not errors, 'errors': errors,
                         'actual_status': result['status'], 'steps': result['metadata']['steps'],
                         'model_responses': result['metadata']['model_responses'],
                         'path': [t['action'] for t in result['trace']]})
    # Keep the original startup-failure outputs and their old evaluator index intact.
    for name, statuses in expected.items():
        directory = root / 'live' / name
        if (directory / 'output.json').is_file():
            result = load_result(directory)
            errors = check_case(name, result, statuses)
            attempts.append({'case': name, 'actual_status': result['status'], 'passed_after_reassessment': not errors,
                             'errors': errors, 'model_responses': result['metadata']['model_responses']})
    report = {'checked_at': datetime.now(timezone.utc).isoformat(),
              'scope': 'Deterministic replay, state binding, UI/input equivalence and acceptance observations; not semantic proof or remote-model authentication.',
              'frozen_files_checked': len(checksums), 'frozen_files_changed': changed,
              'runs_checked': len(rows), 'passed': not changed and all(row['passed'] for row in rows),
              'runs': rows, 'ui_comparisons': comparisons, 'startup_attempt_reassessment': attempts}
    (root / 'audit.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({key: report[key] for key in ('runs_checked', 'frozen_files_checked', 'frozen_files_changed', 'passed')}, ensure_ascii=False))
    return 0 if report['passed'] else 1


if __name__ == '__main__':
    raise SystemExit(main())
