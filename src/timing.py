"""Explicit parallel voice/screen beats; estimates, not synthesized audio."""
import math
import re


def text_seconds(text, han_rate, latin_rate=2.5):
    han=len(re.findall(r'[\u3400-\u9fff]',text))
    words=len(re.findall(r"[A-Za-z]+(?:'[A-Za-z]+)?|\d+(?:\.\d+)?",text))
    # Other written languages still need a nonzero reading/speech budget.
    other=len(re.findall(r'[^\W\d_]', re.sub(r'[\u3400-\u9fffA-Za-z]', '',text)))
    return (han+other)/han_rate + words/latin_rate


def estimate_tracks(shot, rules):
    beats=[]; cursor=0
    stages={s['beat']:s for s in shot.get('staging',[])}
    for beat in sorted({b['beat'] for b in shot['blocks']} | set(stages)):
        blocks=[b for b in shot['blocks'] if b['beat']==beat]
        voice=[b for b in blocks if b['channel'] in ('voice','both')]
        screen=[b for b in blocks if b['channel'] in ('screen','both')]
        def seconds(items):
            return sum(text_seconds(b['text'],rules['speech_units_per_second']) for b in items) + (rules['shot_pause_seconds'] if items else 0)
        spoken, reading=seconds(voice),seconds(screen)
        held=max((b['display_seconds'] for b in screen),default=0)
        action_seconds=stages.get(beat,{}).get('min_seconds',0)
        length=math.ceil(max(spoken,reading,held,action_seconds)*10)/10
        beats.append(dict(beat=beat,start_seconds=round(cursor,1),end_seconds=round(cursor+length,1),
                          voice_seconds=round(spoken,2),screen_read_seconds=round(reading,2),
                          display_seconds=held,estimated_seconds=length))
        if stages: beats[-1]['action_seconds']=action_seconds
        cursor+=length
    total=math.ceil(max(cursor,shot['hold_seconds'],rules['min_shot_seconds'])*10)/10
    return dict(estimated_seconds=total,beats=beats,tail_hold_seconds=round(total-cursor,1))
