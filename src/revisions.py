"""Observable draft differences, computed by the host rather than model self-report."""
import copy
from .schema import fingerprint


def revision_summary(before, after, feedback):
    changes = []
    unchanged_shots = unchanged_blocks = 0
    if before is None:
        changes = ['script:new']
    else:
        if before['title'] != after['title']:
            changes.append('title')
        if before.get('format_version') != after.get('format_version'):
            changes.append('format_version')
        if before.get('editor_notes', '') != after.get('editor_notes', ''):
            changes.append('editor_notes')
        for i in range(max(len(before['shots']), len(after['shots']))):
            old = before['shots'][i] if i < len(before['shots']) else None
            new = after['shots'][i] if i < len(after['shots']) else None
            loc = f'shot:{i+1}'
            if old is None or new is None:
                changes.append(loc + (':added' if old is None else ':removed'))
                continue
            unchanged_shots += old == new
            for field in ('visual', 'hold_seconds', 'purpose', 'staging'):
                if old.get(field) != new.get(field): changes.append(f'{loc}/{field}')
            for j in range(max(len(old['blocks']),len(new['blocks']))):
                a = old['blocks'][j] if j < len(old['blocks']) else None
                b = new['blocks'][j] if j < len(new['blocks']) else None
                if a == b: unchanged_blocks += 1
                else: changes.append(f'{loc}/block:{j+1}')
    return {'before_hash': fingerprint(before) if before else None, 'after_hash': fingerprint(after),
            'changed_fields': changes, 'unchanged_shots': unchanged_shots, 'unchanged_blocks': unchanged_blocks,
            'feedback': copy.deepcopy(feedback),
            'method': 'index_aligned_diff; feedback is observed context, not proof of causality'}


def failed_feedback(state):
    return [{'check': key, 'observation': copy.deepcopy(state[key])}
            for key in ('duration', 'rules_check', 'requirements_check')
            if state.get(key) and (not state[key].get('ok') or not state[key].get('passed'))]
