"""Record an explicit case assessment after reading evidence; never auto-grade."""
import argparse
import json
from pathlib import Path

p = argparse.ArgumentParser()
p.add_argument('case')
p.add_argument('assessment')
p.add_argument('note')
p.add_argument('--stale-note', action='store_true')
p.add_argument('--violation', action='store_true')
a = p.parse_args()
directory = Path(__file__).resolve().parent / 'runs' / a.case
assert (directory/'capture.json').is_file()
record = {'case': a.case, 'assessment': a.assessment, 'note': a.note,
          'reviewer': 'AI开发助手，阅读原需求、实际稿件与Trace；非独立盲评',
          'hard_requirement_violation_observed': a.violation,
          'editorial_note_staleness': a.stale_note}
with (directory/'review.json').open('x', encoding='utf-8') as f:
    json.dump(record, f, ensure_ascii=False, indent=2)
print(a.case + ' review saved')
