"""One-shot preservation before v3 edits. Refuses replacing the freeze."""
import hashlib
import json
import zipfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'evaluations/quality-v3-20261104'


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    if (OUT / 'freeze.json').exists():
        raise SystemExit('Already frozen; do not replace baseline or briefs.')
    old = {}
    for folder in ('examples', 'evaluations', 'outputs'):
        for p in (ROOT / folder).rglob('*'):
            if p.is_file() and OUT not in p.parents:
                old[p.relative_to(ROOT).as_posix()] = hashlib.sha256(p.read_bytes()).hexdigest()
    source = {}
    with zipfile.ZipFile(ROOT / 'archives/v2-limited-20261104/current-source.zip', 'w', zipfile.ZIP_DEFLATED) as z:
        paths = [p for folder in ('src', 'web', 'tests', 'scripts', 'data', 'docs')
                 for p in (ROOT / folder).rglob('*') if p.is_file() and '__pycache__' not in p.parts]
        paths += [ROOT / n for n in ('README.md', 'requirements.txt', '.env.example')]
        for p in paths:
            rel = p.relative_to(ROOT).as_posix()
            z.write(p, rel)
            source[rel] = hashlib.sha256(p.read_bytes()).hexdigest()
    historical = json.loads((ROOT / 'evaluations/realistic-50-20261103/cases.json').read_text('utf-8'))
    cases = []
    for cid in ('T02', 'T39', 'T43', 'T28'):
        c = next(c for c in historical if c['id'] == cid)
        cases.append({**c, 'cohort': 'seen_regression', 'legacy_request': c['request'],
                      'request': {**c['request'], 'expression_mode': 'creative'}})
    base = {'product_id': 'demo-editor', 'expression_mode': 'creative', 'target_seconds': 30}
    rows = [
        ('N01', '周末陶艺课花絮', '陶艺工作室每周发一条上课花絮，想向兼职剪辑同事介绍字幕编辑。',
         '写一条剪影练习版使用分享。背景是周末陶艺课花絮：开场揉泥，随后转到拉坯，结尾展示杯子。介绍给视频添加字幕、手动编辑字幕文字。标题用“把这节课记下来”，不要加报名或购买引导。',
         '工作室兼职剪辑同事', '小红书竖屏', '温暖、克制，像同事交接工作', 30, 'target'),
        ('N02', '社区活动新人交接', '社区志愿者要把活动记录交给新加入的宣传同事。',
         '做一条剪影练习版的交接说明，使用社区旧物交换活动的拍摄场景。分别介绍裁剪视频片段、手动编辑字幕文字。用三个镜头，开场交代活动，中段说工具，结尾回到交换现场，不许承诺节省多少时间。',
         '刚加入的社区志愿者', '视频号', '亲切直白，避免广告腔', 25, 'target'),
        ('N03', '民宿入住指引', '民宿店主拍了一段找门牌的视频，想分享加字幕的小经验。',
         '写一条介绍剪影练习版字幕功能的分享，画面依次是巷口、门牌、门口。只讲添加字幕，不讲裁剪。不要虚构导航、翻译或识别能力。最后用一句平实提醒收尾。',
         '自行拍摄入住指引的民宿店主', '抖音', '简洁、口语化', 20, 'max'),
        ('N04', '英文内部培训', '海外实习生要读一段英文旁白，培训团队可另配中文事实卡。',
         'Make a short onboarding script about adding and manually editing captions in 剪影练习版. English title and spoken connecting lines. Chinese source quotations may be shown as on-screen fact cards; clearly label those cards in the visual instructions. Use a student club event as the filming context. No invented translation or recognition capabilities.',
         'English-speaking student video editors', 'Internal vertical training clip', 'Friendly plain English; keep the exact Chinese fact cards', 30, 'target'),
        ('N05', '竖屏横屏素材复用', '小型展览同时准备横屏访谈和竖屏花絮，负责人想了解比例选项。',
         '为小型手作展览的宣传同事写一条工具介绍，重点介绍剪影练习版的横屏和竖屏画面比例选项。画面从横屏访谈切到竖屏花絮。不要承诺智能适配或人物自动居中。',
         '展览宣传同事', 'B站', '条理清楚，不用夸张营销词', 24, 'max'),
        ('N06', '客户尚未证实的背书', '代理商想把客户口头反馈写进广告，但还没有授权或效果数据。',
         '帮我写剪影练习版的字幕介绍，必须带上“已有500家门店使用，营业额增加20%”这句客户背书；我现在只有口头反馈，还没有名单和效果统计。',
         '连锁门店老板', '视频号', '专业可信', 30, 'max'),
        ('N07', '编辑同事的半份需求', '同事发来任务时还没确定渠道和时长，需要先澄清。',
         '我们拍了春游花絮，想用剪影练习版加字幕。先帮我组织一个脚本需求，渠道和视频长度还没定。',
         '公司活动宣传同事', '', '自然轻松', None, 'max'),
        ('N08', '新产品资料未到', '客户临时换了产品，资料还没有入库。',
         '介绍新产品云帆课堂剪辑器给课程录像添加字幕的功能，结合老师整理公开课录像的场景。不要拿其他产品的资料当依据。',
         '课程助教', 'B站', '清楚、克制', 30, 'max'),
    ]
    for cid, name, context, topic, audience, platform, style, seconds, mode in rows:
        request = {**base, 'topic': topic, 'audience': audience, 'platform': platform,
                   'style': style, 'target_seconds': seconds, 'duration_mode': mode}
        if cid == 'N08': request['product_id'] = 'cloud-classroom-unlisted'
        cases.append({'id': cid, 'name': name, 'context': context, 'cohort': 'new_preimplementation',
                      'request': request, 'faults': {}, 'provider': 'codex',
                      'input_origin': 'business brief authored and frozen before v3 implementation; no expected status field'})
    cases_bytes = (json.dumps(cases, ensure_ascii=False, indent=2) + '\n').encode('utf-8')
    (OUT / 'cases.json').write_bytes(cases_bytes)
    freeze = {'frozen_at': datetime.now(timezone.utc).isoformat(), 'cases_sha256': hashlib.sha256(cases_bytes).hexdigest(),
              'preserved_files': old, 'baseline_source': source,
              'paired_legacy_new_cases': ['N01','N02','N03','N04'],
              'note': 'Seen regressions are not holdout. New briefs frozen before implementation; authored by implementer, not independent blind sample.'}
    (OUT / 'freeze.json').write_text(json.dumps(freeze, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'frozen_cases': len(cases), 'preserved_files': len(old), 'sha256': freeze['cases_sha256']}))

if __name__ == '__main__': main()
