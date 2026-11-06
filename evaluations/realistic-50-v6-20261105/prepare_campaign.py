"""Prepare new analysis helpers; never alter a previous campaign."""
from pathlib import Path
B=Path(__file__).resolve().parent
OLD=B.parent/'realistic-50-v5-20261104'
for name in ('inspect_pairs.py','record_review.py','compare_metrics.py','audit_campaign.py','build_report.py'):
    text=(OLD/name).read_text(encoding='utf8')
    text=text.replace('realistic-50-v41-20261104','realistic-50-v5-20261104')
    text=text.replace('旧v4.1','旧v5').replace('新v5','新v6')
    text=text.replace('== 7788','== 9944').replace('沿用v4.1','沿用v5')
    text=text.replace('# v5','# v6').replace('15-v5-effective-scripts.md','16-v6-titles-latency.md')
    with (B/name).open('x',encoding='utf8') as f:f.write(text)
print('Prepared 5 helpers')
