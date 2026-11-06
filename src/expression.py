"""Enumerated public surfaces and structural guards for fallible semantic review."""
from .schema import TEXT, fingerprint, obj
from .staging import staging_text

EXPRESSION_SCHEMA = obj({'location': TEXT, 'text': TEXT,
    'verdict': {'type': 'string', 'enum': ['plain_expression', 'supported_claim', 'unsupported_claim', 'uncertain']},
    'references': {'type': 'array', 'items': obj({'source_id': TEXT, 'fact_id': TEXT})}, 'evidence': TEXT})
PACING_SCHEMA = obj({'verdict': {'type':'string', 'enum':['met','unmet','uncertain']}, 'evidence':TEXT})


def extended_review(request):
    return request.get('expression_mode', 'strict') == 'creative' or request.get('duration_mode', 'max') == 'target'


def expression_slots(script):
    slots = [{'location': 'title', 'text': script['title']}]
    for i, shot in enumerate(script['shots'], 1):
        slots.append({'location': f'shot:{i}/visual', 'text': shot['visual']})
        for stage in shot.get('staging',[]):
            slots.append({'location':f"shot:{i}/staging:{stage['beat']}", 'text':staging_text(stage)})
        for j, block in enumerate(shot['blocks'], 1):
            if script.get('format_version') in (2, 3) or (not block['source_id'] and not block['fact_id']):
                slots.append({'location': f'shot:{i}/block:{j}', 'text': block['text']})
    return slots


def validate_expression_review(review, request, script, checked):
    if not checked or not checked.get('ok') or checked.get('script_hash') != fingerprint(script):
        raise ValueError('表达审核缺少当前稿件的实际规则检查')
    creative = request.get('expression_mode', 'strict') == 'creative'
    slots = expression_slots(script) if creative else []
    if creative and not checked.get('requires_expression_review'):
        raise ValueError('创作模式缺少逐表面审核依据')
    expressions = review['expressions']
    if not isinstance(expressions, list) or len(expressions) != len(slots):
        raise ValueError('表达审核必须覆盖每一个公开表面，且不可重复')
    expected = {s['location']: s['text'] for s in slots}
    allowed = {(f['source_id'], f['fact_id']) for f in checked.get('available_facts', [])}
    bound = {c['location']:(c['source_id'],c['fact_id']) for c in checked.get('citations',[])} if script.get('format_version') in (2, 3) else {}
    seen = set()
    for item in expressions:
        if not isinstance(item, dict) or set(item) != set(EXPRESSION_SCHEMA['properties']):
            raise ValueError('表达审核字段错误')
        location = item['location']
        if not isinstance(location, str) or location not in expected or location in seen or item['text'] != expected[location]:
            raise ValueError('表达审核位置或原文不一致')
        seen.add(location)
        if item['verdict'] not in EXPRESSION_SCHEMA['properties']['verdict']['enum']:
            raise ValueError('表达审核分类错误')
        if not isinstance(item['evidence'], str) or not 1 <= len(item['evidence'].strip()) <= 2000:
            raise ValueError('表达审核缺少依据')
        refs = item['references']
        if not isinstance(refs, list) or len(refs) > 16:
            raise ValueError('表达审核引用格式错误')
        for ref in refs:
            if (not isinstance(ref, dict) or set(ref) != {'source_id','fact_id'}
                    or any(not isinstance(v,str) for v in ref.values())
                    or (ref['source_id'], ref['fact_id']) not in allowed):
                raise ValueError('表达审核引用不在已检索事实中')
        if item['verdict'] == 'supported_claim' and not refs:
            raise ValueError('资料支持声明必须给出实际事实引用')
        if item['verdict'] == 'plain_expression' and refs:
            raise ValueError('普通表达不可伪装成已核对事实引用')
        if location in bound and item['verdict'] in {'plain_expression','supported_claim'}:
            if item['verdict']!='supported_claim' or bound[location] not in {(r['source_id'],r['fact_id']) for r in refs}:
                raise ValueError('有来源的文案必须由其标注原文支持，不能作为普通表达放行')
    pacing = review['pacing']
    if (not isinstance(pacing, dict) or set(pacing) != {'verdict','evidence'}
            or not isinstance(pacing['verdict'], str)
            or pacing['verdict'] not in {'met','unmet','uncertain'}
            or not isinstance(pacing['evidence'],str) or not 1 <= len(pacing['evidence'].strip()) <= 2000):
        raise ValueError('节奏审核格式错误')
    return all(e['verdict'] in {'plain_expression','supported_claim'} for e in expressions) and pacing['verdict']=='met'
