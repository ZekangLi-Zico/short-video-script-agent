"""Exact spoken-text projection; never rewrite or grade the script."""


def join_copy(parts):
    text = ''
    for part in parts:
        if text and text[-1:].isascii() and part[:1].isascii():
            text += ' '
        text += part
    return text


def listening_copy(script):
    if not script:
        return {'kind':'empty','text':'','shots':[]}
    modern = script.get('format_version') in (2, 3)
    shots = []
    for i, shot in enumerate(script.get('shots', []), 1):
        blocks = shot.get('blocks', [])
        if modern:
            blocks = sorted((b for b in blocks if b['channel'] in ('voice','both')),key=lambda b:b['beat'])
        text = join_copy([b['text'] for b in blocks])
        if text:
            shots.append({'shot':i,'text':text})
    return {'kind':('voice' if shots else 'silent') if modern else 'legacy_unspecified',
            'text':'\n\n'.join(s['text'] for s in shots),'shots':shots}
