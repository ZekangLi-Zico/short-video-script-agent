"""Durable last-completed-step evidence; never resume model calls implicitly."""
import copy
import json
import os
import uuid
from datetime import datetime, timezone
from pathlib import Path

from .agent import Agent
from .reporting import atomic_json, save_run
from .version import APP_VERSION


def now():
    return datetime.now(timezone.utc).isoformat()


def owner_running(pid):
    """Conservative liveness check; never use os.kill(pid, 0) on Windows."""
    if type(pid) is not int or pid <= 0:
        return False
    if pid == os.getpid():
        return True
    if os.name == 'nt':
        import ctypes
        from ctypes import wintypes
        kernel = ctypes.WinDLL('kernel32', use_last_error=True)
        kernel.OpenProcess.argtypes = [wintypes.DWORD,wintypes.BOOL,wintypes.DWORD]
        kernel.OpenProcess.restype = wintypes.HANDLE
        kernel.GetExitCodeProcess.argtypes = [wintypes.HANDLE,ctypes.POINTER(wintypes.DWORD)]
        kernel.GetExitCodeProcess.restype = wintypes.BOOL
        kernel.CloseHandle.argtypes = [wintypes.HANDLE]
        handle = kernel.OpenProcess(0x1000,False,pid)
        if not handle:
            return ctypes.get_last_error() != 87  # Unknown/access-denied: do not recover.
        try:
            code = wintypes.DWORD()
            return not kernel.GetExitCodeProcess(handle,ctypes.byref(code)) or code.value == 259
        finally:
            kernel.CloseHandle(handle)
    try:
        os.kill(pid,0)
        return True
    except ProcessLookupError:
        return False
    except PermissionError:
        return True


class EvidenceSaveError(OSError):
    pass


def interrupted(result, error_type, message):
    result = copy.deepcopy(result)
    result.update(status='blocked', message=message,
                  interruption={'error_type': error_type, 'in_flight_step_may_be_missing': True})
    result['metadata']['finished_at'] = now()
    return result


def run_recorded(directory, request, model, tools, max_steps=12, on_event=None, cancel_event=None):
    directory = Path(directory)
    record = {'run_id': uuid.uuid4().hex, 'state':'recording', 'started_at':now(), 'owner_pid':os.getpid()}
    last = {'status':'in_progress', 'message':'任务执行中，尚未完成。',
            'script':copy.deepcopy(request.get('initial_script')) if isinstance(request,dict) else None,
            'duration':None, 'rules_check':None, 'requirements_check':None, 'sources':[], 'trace':[],
            'metadata':{'app_version':APP_VERSION,'started_at':record['started_at'], 'finished_at':record['started_at'],
                        'provider':model.name, 'evidence_kind':model.evidence_kind,
                        'data_hash':tools.data_hash, 'synthetic_data':tools.synthetic_data,
                        'tool_contracts':{'search_materials':tools.search_contract},
                        'steps':0, 'max_steps':max_steps, 'model_responses':0}}
    atomic_json(directory/'run.json',record)
    atomic_json(directory/'input.json',request)
    atomic_json(directory/'data_snapshot.json',{'materials':tools.materials,'rules':tools.rules})
    if hasattr(model,'diagnostics_dir'):
        model.diagnostics_dir = directory/'diagnostics'

    def progress(event):
        nonlocal last
        last = copy.deepcopy(event['snapshot'])
        last['metadata'].update(run_id=record['run_id'], persistence='checkpoint_v1',
                                fault_injection=tools.initial_failures)
        atomic_json(directory/'checkpoint.json',{'format':'checkpoint_v1','recorded_at':now(),
                    'last_event':{'kind':event['kind'],'step':event['step']},'result':last})
        if on_event:
            on_event(event)

    progress({'kind':'starting','step':0,'snapshot':last, **{k:last[k] for k in
              ('script','duration','rules_check','requirements_check','trace')}})
    try:
        result = Agent(model,tools,max_steps,on_event=progress,cancel_event=cancel_event).run(request)
    except Exception as exc:
        result = interrupted(last, type(exc).__name__, '运行异常，任务未完成；已保留此前的草稿、检查与执行记录。')
    result['metadata'].update(run_id=record['run_id'],persistence='checkpoint_v1')
    try:
        save_run(directory,request,result,tools)
        atomic_json(directory/'run.json',{**record,'state':'finished','finished_at':now()})
    except OSError as exc:
        # The last checkpoint is independent of the final artifact writes.
        try:
            atomic_json(directory/'run.json',{**record,'state':'save_failed','failed_at':now()})
        except OSError:
            pass  # A fully unwritable disk cannot be made durable by software.
        raise EvidenceSaveError('最终记录未保存完成；如检查点已写入，可下载检查点或重启网页服务恢复。') from exc
    return result


def recover_run(directory):
    """Finalize an interruption; None means a live owner must be left untouched."""
    directory = Path(directory)
    if not (directory/'run.json').is_file():
        return False  # Legacy, already-saved runs are left byte-for-byte unchanged.
    record = json.loads((directory/'run.json').read_text(encoding='utf-8'))
    if record['state'] == 'finished':
        return False
    checkpoint = json.loads((directory/'checkpoint.json').read_text(encoding='utf-8'))
    if checkpoint['result']['metadata'].get('run_id') != record['run_id']:
        raise ValueError('检查点与本次运行不匹配')
    if record['state'] == 'recording' and owner_running(record.get('owner_pid')):
        return None
    request = json.loads((directory/'input.json').read_text(encoding='utf-8'))
    snapshot = json.loads((directory/'data_snapshot.json').read_text(encoding='utf-8'))
    from .tools import ToolBox
    tools = ToolBox(snapshot['materials'],snapshot['rules'],
                    checkpoint['result']['metadata'].get('fault_injection',{}))
    result = interrupted(checkpoint['result'],'process_interrupted',
                         '上次运行或保存被中断；已恢复最后写入的检查点，任务未完成，未自动重跑模型。')
    result['recovered_from_checkpoint'] = checkpoint['last_event']
    save_run(directory,request,result,tools)
    atomic_json(directory/'run.json',{**record,'state':'finished','recovered_at':now()})
    return True
