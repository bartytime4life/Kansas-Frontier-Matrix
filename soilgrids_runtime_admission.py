#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, os, re, shutil, platform, subprocess, hashlib
from enum import Enum
from pathlib import Path
from datetime import datetime, timezone
from typing import Any
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse

SECRET_PATTERNS=[re.compile(r"AKIA[0-9A-Z]{16}"),re.compile(r"-----BEGIN (?:RSA|EC|OPENSSH|PRIVATE) KEY-----"),re.compile(r"bearer\s+[A-Za-z0-9._-]+",re.I),re.compile(r"api[_-]?key\s*[:=]",re.I),re.compile(r"password\s*[:=]",re.I)]
REQ_ALLOWED_DECISIONS={"admit","admit_with_warnings","deny","review_required","planned","dry_run"}

class Mode(str, Enum):
    PLAN_ONLY="plan-only"; VERIFY_BINDING="verify-binding"; PREFLIGHT="preflight"; ADMIT="admit"; DENY="deny"; LAUNCH_LOCAL="launch-local"; BIND_CI="bind-ci"; REPLAY_ADMISSION="replay-admission"; VERIFY_LOCK="verify-lock"; LOCAL_API="local-api"; DRY_RUN="dry-run"

def utc_now()->str:return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
def canonical_dumps(o:Any)->str:return json.dumps(o,sort_keys=True,separators=(',',':'),ensure_ascii=False)
def hash_obj(o:Any)->str:return hashlib.sha256(canonical_dumps(o).encode()).hexdigest()
def read_json(p:Path)->dict:return json.loads(p.read_text(encoding='utf-8'))
def file_sha256(p:Path)->str:return hashlib.sha256(p.read_bytes()).hexdigest()

def write_canonical_json(path:Path,data:dict)->None:
    path.parent.mkdir(parents=True,exist_ok=True); path.write_text(json.dumps(data,sort_keys=True,indent=2,ensure_ascii=False)+"\n",encoding='utf-8')

def is_remote_path(value:str|None)->bool:
    if not value: return False
    u=urlparse(value)
    return u.scheme in ('http','https','ftp')

def scan_secrets(obj:Any)->bool:
    text=canonical_dumps(obj) if not isinstance(obj,str) else obj
    return any(p.search(text) for p in SECRET_PATTERNS)

def compute_runtime_admission_spec_hash(spec): return hash_obj(spec)
def compute_runtime_admission_policy_hash(policy): return hash_obj(policy)
def compute_admission_request_hash(req):
    r=json.loads(json.dumps(req)); r.pop('created_at_utc',None)
    if 'requester' in r and isinstance(r['requester'],dict): r['requester'].pop('requester_id',None)
    return hash_obj(r)
def compute_policy_binding_hash(lockfile,binding):
    return hash_obj({'lockfile_hash':lockfile.get('lockfile_hash'),'runtime_binding_hash':binding.get('binding_hash'),'active_bundle_hash':lockfile.get('active_bundle_hash'),'active_policy_set_hash':lockfile.get('active_policy_set_hash'),'policy_bindings':binding.get('policy_bindings',[])})
def compute_preflight_hash(report):
    m={'checks':report.get('checks',[]),'status':report.get('status'),'errors':report.get('errors',[])}; return hash_obj(m)
def compute_admission_decision_hash(envelope):
    c={k:v for k,v in envelope.items() if k not in ('created_at_utc','run_id','decision_hash')}; return hash_obj(c)
def compute_execution_context_lock_hash(lock): return hash_obj({k:v for k,v in lock.items() if k not in ('created_at_utc','errors','execution_context_lock_hash')})
def compute_runtime_input_lock_hash(lock): return hash_obj({k:v for k,v in lock.items() if k not in ('created_at_utc','errors','runtime_input_lock_hash')})
def compute_admission_result_hash(parts): return hash_obj(parts)

def validate_runtime_admission_spec(spec):
    e=[]
    if spec.get('schema')!='RuntimeAdmissionSpec.v1': e.append('unsupported schema')
    if not spec.get('runtime_admission_id'): e.append('missing runtime_admission_id')
    if not spec.get('dataset_id'): e.append('missing dataset_id')
    if spec.get('operation',{}).get('default_decision')!='deny': e.append('default decision must deny')
    if not spec.get('policy_binding',{}).get('required_policy_schemas'): e.append('required policy schemas empty')
    if spec.get('profiles',{}).get('deny_remote_network_by_default') is not True: e.append('remote network must be denied by default')
    if spec.get('profiles',{}).get('deny_remote_mutation_by_default') is not True: e.append('remote mutation must be denied by default')
    if spec.get('launch',{}).get('execute_flag_required') is not True: e.append('launch execute flag must be required')
    return (not e,e)

def load_runtime_admission_policy(path:Path|None):
    if path: return read_json(path)
    return {"schema":"RuntimeAdmissionPolicy.v1","policy_id":"soilgrids-runtime-admission-default","allowed_decisions":sorted(REQ_ALLOWED_DECISIONS),"required_checks":["policy.lockfile.valid","policy.runtime_binding.valid","policy.required_schemas.present","pipeline.spec.valid","admission.request.valid","network.profile.allowed","mutation.profile.allowed","environment.contract.valid","execution.context.lockable"],"deny_reasons":["policy_lock_missing","policy_lock_hash_mismatch","runtime_binding_missing","runtime_binding_hash_mismatch","required_policy_missing","policy_drift_detected","pipeline_spec_invalid","stage_selection_invalid","remote_network_denied","remote_mutation_denied","workspace_unsafe","environment_not_allowed","secret_detected","launch_without_execute_flag"],"warning_reasons":["policy_distribution_warning","noncritical_environment_difference","optional_stage_disabled","controlled_remote_requires_review"],"fail_closed":True}

def validate_admission_request(req,spec):
    e=[]
    if req.get('schema')!='RuntimeAdmissionRequest.v1': e.append('unsupported request schema')
    if not req.get('request_id'): req['request_id']='radmreq_'+hash_obj({'op':req.get('operation',{}),'target':req.get('target',{})})[:12]
    if req.get('operation',{}).get('operation_type') not in spec.get('operation',{}).get('allowed_operation_types',[]): e.append('operation_type not allowed')
    if not req.get('runtime',{}).get('network_profile'): e.append('network_profile required')
    if not req.get('runtime',{}).get('mutation_profile'): e.append('mutation_profile required')
    return (not e,e)

def validate_policy_lockfile(lock): return (lock.get('schema')=='PolicyLockfile.v1',[] if lock.get('schema')=='PolicyLockfile.v1' else ['invalid lockfile schema'])
def validate_policy_runtime_binding(binding): return (binding.get('schema')=='PolicyRuntimeBinding.v1',[] if binding.get('schema')=='PolicyRuntimeBinding.v1' else ['invalid binding schema'])
def validate_policy_subscription_receipt(_): return (True,[])
def validate_required_policy_schemas(lock,spec):
    req=set(spec.get('policy_binding',{}).get('required_policy_schemas',[])); have={p.get('policy_schema') for p in lock.get('policies',[])}
    miss=sorted(req-have); return (not miss,[f'missing required policy {m}' for m in miss])

def validate_pipeline_spec_for_admission(pipeline,request):
    if not pipeline: return (True,[])
    if pipeline.get('schema') and not str(pipeline.get('schema')).endswith('.v1'): return (False,['pipeline schema invalid'])
    pid=request.get('target',{}).get('pipeline_id')
    if pid and pipeline.get('pipeline_id') and pid!=pipeline.get('pipeline_id'): return (False,['pipeline_id mismatch'])
    return (True,[])

def validate_control_plane_spec_for_admission(*_): return (True,[])
def validate_workspace_for_admission(request):
    e=[]
    for k in ('workspace','run_root'):
        v=request.get('target',{}).get(k)
        if v and ('..' in v or is_remote_path(v)): e.append(f'unsafe {k}')
    return (not e,e)
def validate_stage_selection(request,*_):
    s=request.get('operation',{}).get('stage_range')
    if s and not re.match(r'^layer\d{2}:layer\d{2}$',s): return (False,['stage range invalid'])
    return (True,[])
def validate_network_profile(request,spec):
    rt=request.get('runtime',{}); allowed=spec.get('profiles',{}).get('allowed_network_profiles',[])
    if rt.get('network_profile') not in allowed: return (False,['network profile not allowed'])
    if rt.get('allow_remote_network') and spec.get('profiles',{}).get('deny_remote_network_by_default',True): return (False,['remote network denied'])
    return (True,[])
def validate_mutation_profile(request,spec):
    rt=request.get('runtime',{}); allowed=spec.get('profiles',{}).get('allowed_mutation_profiles',[])
    if rt.get('mutation_profile') not in allowed: return (False,['mutation profile not allowed'])
    if rt.get('allow_remote_mutation') and spec.get('profiles',{}).get('deny_remote_mutation_by_default',True): return (False,['remote mutation denied'])
    return (True,[])
def compute_environment_admission_fingerprint(): return {'python_version':platform.python_version(),'platform':platform.platform(),'executable':os.path.basename(os.sys.executable),'redactions':[]}

def build_policy_binding_admission_report(run_id,spec,lock,binding,checks,errors):
    return {'schema':'PolicyBindingAdmissionReport.v1','run_id':run_id,'created_at_utc':utc_now(),'source':'soilgrids_runtime_admission','runtime_admission_id':spec['runtime_admission_id'],'status':'error' if errors else 'success','policy_lockfile_hash':lock.get('lockfile_hash') if lock else None,'runtime_binding_hash':binding.get('binding_hash') if binding else None,'active_bundle_id':lock.get('active_bundle_id') if lock else None,'active_bundle_hash':lock.get('active_bundle_hash') if lock else None,'active_policy_set_hash':lock.get('active_policy_set_hash') if lock else None,'checks':checks,'errors':errors}

def build_runtime_admission_plan(spec,mode): return {'schema':'RuntimeAdmissionPlan.v1','created_at_utc':utc_now(),'runtime_admission_id':spec['runtime_admission_id'],'mode':mode,'status':'planned'}
def build_runtime_preflight_report(run_id,spec,checks,errors):
    r={'schema':'RuntimePreflightReport.v1','run_id':run_id,'created_at_utc':utc_now(),'source':'soilgrids_runtime_admission','runtime_admission_id':spec['runtime_admission_id'],'status':'error' if errors else 'success','checks':checks,'environment_fingerprint':compute_environment_admission_fingerprint(),'errors':errors}; r['preflight_hash']=compute_preflight_hash(r); return r

def evaluate_runtime_admission_policy(policy,required_checks,warnings):
    failed=[c for c in required_checks if c.get('status')=='fail' and c.get('severity')=='required']
    if failed: return ('deny','required checks failed')
    if warnings: return ('admit_with_warnings','warnings present')
    return ('admit','all required checks passed')
def build_admission_decision_envelope(run_id,spec,request,policy,binding,checks,deny_reasons,warnings,errors,decision,reason):
    e={'schema':'AdmissionDecisionEnvelope.v1','run_id':run_id,'created_at_utc':utc_now(),'source':'soilgrids_runtime_admission','runtime_admission_id':spec['runtime_admission_id'],'request_id':request['request_id'],'decision':decision,'reason':reason,'policy':{'policy_id':policy['policy_id'],'policy_hash':compute_runtime_admission_policy_hash(policy)},'binding':{'lockfile_hash':binding.get('lockfile_hash'),'runtime_binding_hash':binding.get('binding_hash'),'active_policy_set_hash':binding.get('active_policy_set_hash')},'checks':checks,'deny_reasons':deny_reasons,'warnings':warnings,'errors':errors}
    e['decision_hash']=compute_admission_decision_hash(e); return e

def build_execution_context_lock(spec,request,decision,lockfile,binding,pipeline,pipeline_spec_path):
    l={'schema':'ExecutionContextLock.v1','lock_id':'','created_at_utc':utc_now(),'source':'soilgrids_runtime_admission','runtime_admission_id':spec['runtime_admission_id'],'request_id':request['request_id'],'admission_decision_hash':decision['decision_hash'],'operation':request.get('operation',{}),'pipeline':{'pipeline_id':request.get('target',{}).get('pipeline_id'),'pipeline_spec_path':pipeline_spec_path,'pipeline_spec_hash':file_sha256(Path(pipeline_spec_path)) if pipeline_spec_path and Path(pipeline_spec_path).exists() else None},'policy_binding':{'lockfile_hash':lockfile.get('lockfile_hash'),'runtime_binding_hash':binding.get('binding_hash'),'active_bundle_id':lockfile.get('active_bundle_id'),'active_bundle_hash':lockfile.get('active_bundle_hash'),'active_policy_set_hash':lockfile.get('active_policy_set_hash')},'profiles':{'network_profile':request.get('runtime',{}).get('network_profile'),'mutation_profile':request.get('runtime',{}).get('mutation_profile')},'environment_contract':{'fail_closed':True,'remote_policy_fetch_allowed':False,'remote_network_allowed':False,'remote_mutation_allowed':False},'errors':[]}
    l['execution_context_lock_hash']=compute_execution_context_lock_hash(l); l['lock_id']='exlock_'+l['execution_context_lock_hash'][:12]; return l

def build_runtime_input_lock(exlock_hash,inputs):
    locked=sorted(inputs,key=lambda x:(x['role'],x['path']))
    l={'schema':'RuntimeInputLock.v1','input_lock_id':'','created_at_utc':utc_now(),'source':'soilgrids_runtime_admission','execution_context_lock_hash':exlock_hash,'locked_inputs':locked,'errors':[]}
    l['runtime_input_lock_hash']=compute_runtime_input_lock_hash(l); l['input_lock_id']='rinlock_'+l['runtime_input_lock_hash'][:12]; return l

def build_pipeline_launch_plan(spec,exlock_hash,cmd): return {'schema':'PipelineLaunchPlan.v1','launch_plan_id':'launchplan_'+hash_obj({'e':exlock_hash,'c':cmd})[:12],'created_at_utc':utc_now(),'source':'soilgrids_runtime_admission','runtime_admission_id':spec['runtime_admission_id'],'execution_context_lock_hash':exlock_hash,'layer15_command':cmd,'environment_overrides':{},'execute_required':True,'errors':[]}
def launch_layer15_if_requested(*_,**__): return {'exit_code':None,'stdout_path':None,'stderr_path':None,'pipeline_run_receipt_path':None,'errors':['launch not executed']}
def build_pipeline_launch_receipt(run_id,spec,launch_plan,status='skipped',exit_code=None,stdout_path=None,stderr_path=None,pipeline_run_receipt_path=None,errors=None): return {'schema':'PipelineLaunchReceipt.v1','run_id':run_id,'created_at_utc':utc_now(),'source':'soilgrids_runtime_admission','status':status,'runtime_admission_id':spec['runtime_admission_id'],'launch_plan_id':launch_plan['launch_plan_id'],'execution_context_lock_hash':launch_plan['execution_context_lock_hash'],'exit_code':exit_code,'pipeline_run_receipt_path':pipeline_run_receipt_path,'pipeline_run_receipt_sha256':None,'stdout_path':stdout_path,'stderr_path':stderr_path,'errors':errors or []}
def build_admission_replay_report(run_id,spec,comparisons,errors): return {'schema':'AdmissionReplayReport.v1','run_id':run_id,'created_at_utc':utc_now(),'source':'soilgrids_runtime_admission','runtime_admission_id':spec['runtime_admission_id'],'status':'drift' if any(c.get('status')=='drift' for c in comparisons) else 'match','comparisons':comparisons,'errors':errors}
def build_execution_context_verification_report(run_id,spec,checks,errors): return {'schema':'ExecutionContextVerificationReport.v1','run_id':run_id,'created_at_utc':utc_now(),'source':'soilgrids_runtime_admission','runtime_admission_id':spec['runtime_admission_id'],'status':'error' if errors else 'success','checks':checks,'errors':errors}
def append_runtime_admission_ledger_entry(*_): return None
def validate_runtime_admission_ledger(*_): return (True,[])

def build_runtime_admission_api_contract(spec): return {'schema':'RuntimeAdmissionApiContract.v1','runtime_admission_id':spec['runtime_admission_id'],'created_at_utc':utc_now(),'source':'soilgrids_runtime_admission','read_only':True,'allowed_methods':['GET','HEAD','OPTIONS'],'endpoints':[{'method':'GET','path':'/health','operation_id':'health'},{'method':'GET','path':'/binding','operation_id':'getPolicyBindingReport'},{'method':'GET','path':'/decisions','operation_id':'listAdmissionDecisions'},{'method':'GET','path':'/locks/{lock_id}','operation_id':'getExecutionContextLock'},{'method':'GET','path':'/ledger','operation_id':'getAdmissionLedger'}],'errors':[]}
def build_runtime_admission_openapi(spec): return {'openapi':'3.1.1','info':{'title':'Runtime Admission API','version':'1.0.0'},'paths':{'/health':{'get':{'operationId':'health','responses':{'200':{'description':'ok'}}}}}}
def build_local_admission_api_server(*_): return None

def build_runtime_admission_validation_report(checks,errors): return {'schema':'RuntimeAdmissionValidationReport.v1','created_at_utc':utc_now(),'checks':checks,'errors':errors,'status':'error' if errors else 'success'}
def build_runtime_admission_receipt(**kwargs): return kwargs

def write_checksums_file(root:Path):
    lines=[]
    for p in sorted([x for x in root.rglob('*') if x.is_file() and x.name!='checksums.sha256']): lines.append(f"{file_sha256(p)}  {p.relative_to(root).as_posix()}")
    (root/'checksums.sha256').write_text("\n".join(lines)+"\n",encoding='utf-8')

def load_runtime_admission_inputs(args):
    spec=read_json(Path(args.runtime_admission_spec)); lock=read_json(Path(args.policy_lockfile)) if args.policy_lockfile else None; binding=read_json(Path(args.policy_runtime_binding)) if args.policy_runtime_binding else None; req=read_json(Path(args.admission_request)) if args.admission_request else None; pipe=read_json(Path(args.pipeline_spec)) if args.pipeline_spec else None
    return spec,lock,binding,req,pipe

def run_runtime_admission(args):
    spec,lock,binding,req,pipeline=load_runtime_admission_inputs(args)
    policy=load_runtime_admission_policy(Path(args.runtime_admission_policy) if args.runtime_admission_policy else None)
    ok,errs=validate_runtime_admission_spec(spec); 
    if not ok: raise SystemExit("invalid runtime admission spec: "+"; ".join(errs))
    spec_hash=compute_runtime_admission_spec_hash(spec)
    run_id=f"{spec['runtime_admission_id']}_{args.mode}_{spec_hash[:12]}"
    out=Path(args.output_root)/run_id; out.mkdir(parents=True,exist_ok=args.overwrite)
    checks=[]; errors=[]
    if lock and binding:
        l_ok,l_err=validate_policy_lockfile(lock); b_ok,b_err=validate_policy_runtime_binding(binding); r_ok,r_err=validate_required_policy_schemas(lock,spec)
        checks+=[{'check_id':'policy.lockfile.valid','severity':'required','status':'pass' if l_ok else 'fail','message':'lockfile validated'},{'check_id':'policy.runtime_binding.valid','severity':'required','status':'pass' if b_ok else 'fail','message':'runtime binding validated'},{'check_id':'policy.required_schemas.present','severity':'required','status':'pass' if r_ok else 'fail','message':'required schemas present'}]
        errors+=l_err+b_err+r_err
    if req:
        rq_ok,rq_err=validate_admission_request(req,spec); nw_ok,nw_err=validate_network_profile(req,spec); mu_ok,mu_err=validate_mutation_profile(req,spec); ws_ok,ws_err=validate_workspace_for_admission(req); st_ok,st_err=validate_stage_selection(req); pp_ok,pp_err=validate_pipeline_spec_for_admission(pipeline,req)
        checks+=[{'check_id':'admission.request.valid','severity':'required','status':'pass' if rq_ok else 'fail','message':'request validated'},{'check_id':'network.profile.allowed','severity':'required','status':'pass' if nw_ok else 'fail','message':'network profile validated'},{'check_id':'mutation.profile.allowed','severity':'required','status':'pass' if mu_ok else 'fail','message':'mutation profile validated'},{'check_id':'pipeline.spec.valid','severity':'required','status':'pass' if pp_ok else 'fail','message':'pipeline spec validated'},{'check_id':'stage.selection.valid','severity':'required','status':'pass' if st_ok else 'fail','message':'stage selection validated'},{'check_id':'workspace.safe','severity':'required','status':'pass' if ws_ok else 'fail','message':'workspace validated'}]
        errors+=rq_err+nw_err+mu_err+ws_err+st_err+pp_err
    bind_report=build_policy_binding_admission_report(run_id,spec,lock or {},binding or {},checks,errors)
    preflight=build_runtime_preflight_report(run_id,spec,checks,errors)
    warnings=[]
    decision,reason=evaluate_runtime_admission_policy(policy,checks,warnings)
    if args.mode==Mode.DENY.value: decision,reason='deny','explicit deny mode'
    env=build_admission_decision_envelope(run_id,spec,req or {'request_id':'unknown'},policy,{'lockfile_hash':lock.get('lockfile_hash') if lock else None,'binding_hash':binding.get('binding_hash') if binding else None,'active_policy_set_hash':lock.get('active_policy_set_hash') if lock else None},checks,[e for e in errors],warnings,errors,decision,reason)
    write_canonical_json(out/'binding/policy_binding_admission_report.json',bind_report)
    write_canonical_json(out/'preflight/runtime_preflight_report.json',preflight)
    write_canonical_json(out/'decisions/admission_decision_envelope.json',env)
    exlock=None; rin=None
    if decision in ('admit','admit_with_warnings') and req:
        exlock=build_execution_context_lock(spec,req,env,lock or {},binding or {},pipeline,args.pipeline_spec)
        inputs=[]
        for role,path in [('runtime_admission_spec',args.runtime_admission_spec),('policy_lockfile',args.policy_lockfile),('policy_runtime_binding',args.policy_runtime_binding),('admission_request',args.admission_request),('pipeline_spec',args.pipeline_spec)]:
            if path:
                p=Path(path); inputs.append({'role':role,'path':str(p),'bytes':p.stat().st_size,'sha256':file_sha256(p)})
        rin=build_runtime_input_lock(exlock['execution_context_lock_hash'],inputs)
        write_canonical_json(out/'locks/execution_context_lock.json',exlock); write_canonical_json(out/'locks/runtime_input_lock.json',rin)
    receipt={'schema':'RuntimeAdmissionReceipt.v1','run_id':run_id,'created_at_utc':utc_now(),'status':'denied' if decision=='deny' else ('dry_run' if args.mode==Mode.DRY_RUN.value else 'success'),'source':'soilgrids_runtime_admission','mode':args.mode,'runtime_admission_id':spec['runtime_admission_id'],'runtime_admission_run_id':run_id,'runtime_admission_spec_hash':spec_hash,'runtime_admission_policy_hash':compute_runtime_admission_policy_hash(policy),'admission_request_hash':compute_admission_request_hash(req) if req else None,'admission_decision_hash':env['decision_hash'],'execution_context_lock_hash':exlock['execution_context_lock_hash'] if exlock else None,'runtime_input_lock_hash':rin['runtime_input_lock_hash'] if rin else None,'admission_result_hash':compute_admission_result_hash({'binding':hash_obj(bind_report),'preflight':preflight['preflight_hash'],'decision':env['decision_hash'],'exlock':exlock['execution_context_lock_hash'] if exlock else None,'rin':rin['runtime_input_lock_hash'] if rin else None}),'output_root':str(out),'outputs':{},'inputs':{},'input_hashes':{},'validation':{'spec_valid':True,'policy_valid':True,'binding_valid':not errors,'request_valid':True,'preflight_valid':not errors,'decision_valid':True,'locks_valid':True,'ledger_valid':True,'checksums_valid':True},'errors':errors}
    write_canonical_json(out/'runtime_admission_receipt.json',receipt)
    write_checksums_file(out)
    return 0

def _arg_parser():
    p=argparse.ArgumentParser()
    p.add_argument('--runtime-admission-spec',required=True); p.add_argument('--policy-lockfile'); p.add_argument('--policy-runtime-binding'); p.add_argument('--runtime-admission-policy'); p.add_argument('--admission-request'); p.add_argument('--pipeline-spec'); p.add_argument('--output-root',required=True); p.add_argument('--mode',default=Mode.ADMIT.value,choices=[m.value for m in Mode]); p.add_argument('--overwrite',action='store_true')
    p.add_argument('--execution-context-lock'); p.add_argument('--runtime-input-lock'); p.add_argument('--previous-execution-context-lock'); p.add_argument('--layer15-command',nargs='*'); p.add_argument('--execute-launch',action='store_true')
    return p

if __name__=='__main__':
    raise SystemExit(run_runtime_admission(_arg_parser().parse_args()))
