"""Project authored staging and measured estimates; never invent legacy actions."""


def staging_text(stage):
    return '\n'.join(f'{label}：{stage[key]}' for key,label in
                     [('action','动作'),('camera','镜头'),('sound','现场声')] if stage.get(key))


def shot_rows(shot, timing=None):
    timing=timing or {}
    stages={s['beat']:s for s in shot.get('staging',[])}
    timings={t['beat']:t for t in timing.get('beats',[])}
    rows=[]
    for beat in sorted(set(stages) | {b['beat'] for b in shot.get('blocks',[])}):
        stage=stages.get(beat,{})
        timed=timings.get(beat,{})
        rows.append(dict(beat=beat,start_seconds=timed.get('start_seconds'),end_seconds=timed.get('end_seconds'),
                         action=stage.get('action',''),camera=stage.get('camera',''),sound=stage.get('sound',''),
                         blocks=[dict(b) for b in shot['blocks'] if b['beat']==beat],tail=False,subtitle_hold=False))
    if timing.get('tail_hold_seconds',0)>0 and rows:
        rows.append(dict(beat=None,start_seconds=rows[-1]['end_seconds'],end_seconds=timing['estimated_seconds'],
                         action='',camera='',sound='',blocks=[],tail=True,
                         subtitle_hold=any(b['channel'] in ('screen','both') for b in rows[-1]['blocks'])))
    return rows


def storyboard_rows(script, duration=None):
    if not script or script.get('format_version') not in (2,3): return []
    timings={s['shot']:s for s in (duration or {}).get('shots',[])}
    return [shot_rows(shot,timings.get(i)) for i,shot in enumerate(script['shots'],1)]
