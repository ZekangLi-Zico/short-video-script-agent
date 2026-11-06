"""Human-readable script and machine-readable reproducibility artifacts."""

import json
import os
import tempfile
import html
from pathlib import Path
from .listening import listening_copy
from .staging import shot_rows


def atomic_text(path, text):
    """Replace one artifact only after a complete, flushed write on the same disk."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', newline='\n',
                                         dir=path.parent, prefix='.'+path.name+'.', suffix='.tmp', delete=False) as handle:
            temporary = Path(handle.name)
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    finally:
        if temporary is not None:
            try:
                temporary.unlink(missing_ok=True)
            except OSError:
                pass


def atomic_json(path, content):
    atomic_text(path, json.dumps(content, ensure_ascii=False, indent=2, allow_nan=False)+'\n')


def render_report(result):
    lines = ["# 短视频脚本运行结果", "", f"- 状态：`{result['status']}`",
             f"- 证据类型：`{result['metadata']['evidence_kind']}`",
             f"- 说明：{result['message']}", ""]
    script = result.get("script")
    if script:
        lines += [f"## {script['title']}", "", "> 未完成或检查失败时，下列内容仅为未通过验收的草稿。", ""]
        spoken = listening_copy(script)
        narrative = (result.get('rules_check') or {}).get('material_kind') == 'narrative'
        heading = ('连读台词与旁白' if narrative else '连读旁白') if spoken['kind']=='voice' else '旧稿合并文案（未区分声画）'
        if spoken['text']:
            lines += [f'### {heading}', '', spoken['text'], '']
        else:
            lines += ['本稿没有配音，请按下方动作与屏幕文字制作。' if script.get('format_version')==3
                      else '本稿没有旁白，按分镜中的屏幕文字制作。', '']
        timings = {s["shot"]: s["estimated_seconds"] for s in (result.get("duration") or {}).get("shots", [])}
        for i, shot in enumerate(script["shots"], 1):
            if script.get('format_version') == 3:
                def cell(value):
                    return html.escape(str(value)).replace('|','\\|').replace('\n','<br>')
                lines += [f'### 分镜 {i}', '', f"场景：{shot['visual']}", '', f"镜头目的：{shot['purpose']}", '',
                          '| 时间（镜内） | 动作与画面 | 对白与声音 |', '|---|---|---|']
                timing=next((x for x in (result.get('duration') or {}).get('shots',[]) if x['shot']==i),{})
                for row in shot_rows(shot,timing):
                    label=f"{row['start_seconds']}–{row['end_seconds']} 秒" if row['start_seconds'] is not None else '待估时'
                    action=row['action'] or ('保持本镜画面' if row['tail'] else '')
                    if row['camera']: action+='\n镜头：'+row['camera']
                    audio=[]
                    for b in row['blocks']:
                        prefix='屏幕文字' if b['channel']=='screen' else b['speaker']
                        audio.append(prefix+'：'+b['text']+('（同步字幕）' if b['channel']=='both' else ''))
                    if not audio: audio.append('无新增台词' if row['tail'] else '无对白')
                    if row['sound']: audio.append('现场声：'+row['sound'])
                    if row['subtitle_hold']: audio.append('保留本段字幕')
                    lines.append(f"| {cell(label)} | {cell(action)} | {cell(chr(10).join(audio))} |")
                refs=list(dict.fromkeys(b['source_id']+'/'+b['fact_id'] for b in shot['blocks'] if b['source_id']))
                lines += ['', '来源：'+(', '.join(refs) or '动作安排见表达审核'), '', f"预计镜头时长：{timings.get(i,'未检查')} 秒", '']
                continue
            if script.get('format_version') == 2:
                lines += [f"### 分镜 {i}", '', f"镜头目的：{shot['purpose']}", '', f"画面：{shot['visual']}", '',
                          '同一时段的配音和屏幕文字同时播放，各时段按顺序进行。', '']
                timing=next((x for x in (result.get('duration') or {}).get('shots',[]) if x['shot']==i),{})
                for beat in sorted({b['beat'] for b in shot['blocks']}):
                    t=next((b for b in timing.get('beats',[]) if b['beat']==beat),{})
                    lines += [f"**第 {beat} 拍 · 镜内 {t.get('start_seconds','?')}–{t.get('end_seconds','?')} 秒**", '']
                    for b in [b for b in shot['blocks'] if b['beat']==beat]:
                        label=({'voice':'配音','screen':'屏幕文字','both':'配音＋同步字幕'} if narrative else
                               {'voice':'旁白','screen':'屏幕文字','both':'旁白＋同步字幕'})[b['channel']]
                        lines += [f"{label}：{b['text']}", '']
                        if b['source_id']:
                            lines += [f"依据：{b['source_id']}/{b['fact_id']}", '']
                if timing.get('tail_hold_seconds',0)>0:
                    last=max(b['beat'] for b in shot['blocks'])
                    subtitle='（保留本段字幕）' if any(b['beat']==last and b['channel'] in ('screen','both') for b in shot['blocks']) else ''
                    lines += [f"镜头末尾保持画面：{timing['beats'][-1]['end_seconds']}–{timing['estimated_seconds']} 秒{subtitle}", '']
                lines += [f"预计镜头时长：{timings.get(i,'未检查')} 秒", '']
                continue
            lines += [f"### 分镜 {i}", "", f"画面：{shot['visual']}", "",
                      "旁白/字幕：" + "".join(b["text"] for b in shot["blocks"]), "",
                      "来源：" + ", ".join(b["source_id"] + "/" + b["fact_id"] for b in shot["blocks"] if b["source_id"]), "",
                      f"预计镜头时长：{timings.get(i, '未检查')} 秒", ""]
        if script.get('editor_notes'):
            lines += ['## 审稿备注（不进入视频，不计入时长）', '',
                      '供创作者核对修改与资料缺口，不是经过事实认证的产品介绍。', '',
                      script['editor_notes'], '']
    duration = result.get("duration") or {}
    revisions = [t['observation']['revision'] for t in result['trace'] if t.get('action') == 'write_script'
                 and t['observation'].get('revision', {}).get('before_hash')]
    if revisions:
        lines += ['## 实际修订', '', '位置按镜头索引比较；日志关联的是实际反馈，不证明模型因果推理。', '']
        for rev in revisions:
            lines += [f"- 修改：{', '.join(rev['changed_fields']) or '未改变'}；保留原镜头 {rev['unchanged_shots']} 个、原文案块 {rev['unchanged_blocks']} 个。",
                      '- 修订前失败检查：' + ', '.join(f['check'] for f in rev['feedback'])]
        lines += ['']
    if duration.get('duration_mode') == 'target':
        lines += [f"时长要求：{duration['min_seconds']}–{duration['target_seconds']} 秒（接近目标）。", '']
    lines += [f"预计总时长：{duration.get('total_seconds', '未检查')} 秒（基于语速与镜头停留估算，非成片实测）。", "",
              "## 检查结果与来源", "", "```json", json.dumps(result.get("rules_check"), ensure_ascii=False, indent=2), "```", "",
              "## 需求覆盖核对", "", "以下为模型评估，可能漏判或误判，仍需人工确认。", "",
              "```json", json.dumps(result.get('requirements_check'), ensure_ascii=False, indent=2), "```", "",
              "## 执行路径", "", " → ".join(t["action"] for t in result["trace"]), "",
              "逐步参数、观察和简短决策依据见 trace.jsonl。未记录模型内部思维过程。", ""]
    return "\n".join(lines)


def save_run(directory, request, result, tools):
    directory = Path(directory)
    directory.mkdir(parents=True, exist_ok=True)
    files = {"input.json": request, "output.json": {k: v for k, v in result.items() if k != "trace"},
             "data_snapshot.json": {"materials": tools.materials, "rules": tools.rules},
             "manifest.json": {**result["metadata"], "fault_injection": tools.initial_failures if hasattr(tools, "initial_failures") else {}}}
    for name, content in files.items():
        if name != 'output.json':
            atomic_json(directory / name, content)
    atomic_text(directory / "trace.jsonl", "".join(json.dumps(e, ensure_ascii=False, allow_nan=False) + "\n" for e in result["trace"]))
    atomic_text(directory / "script.md", render_report(result))
    spoken = listening_copy(result.get('script'))
    atomic_json(directory / 'listening.json', spoken)
    export_label = '旧稿合并文案（未区分声画，不能直接视为旁白）\n\n' if spoken['kind']=='legacy_unspecified' else ''
    atomic_text(directory / 'voice.txt', export_label+spoken['text']+'\n')
    atomic_json(directory / 'output.json', files['output.json'])
