#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, os, re, shutil
from enum import Enum
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
from typing import Any

class Exit:
    SUCCESS=0; DRY_RUN=5; WARNING=10; BLOCKED=20; MALFORMED=30; RESOLVER=40; REMOTE=50; LOCK=60; BIND=70; DRIFT=80; API=90; UNSAFE=100; SECRET=110; LEDGER=120; INTERNAL=130

class Mode(str, Enum):
    PLAN_ONLY="plan-only"; VERIFY_LOCAL="verify-local"; FETCH_REMOTE="fetch-remote"; SYNC_LOCAL="sync-local"; LOCK="lock"; BIND_RUNTIME="bind-runtime"; DRIFT_CHECK="drift-check"; ROLLBACK_LOCKFILE="rollback-lockfile"; LOCAL_API="local-api"; DRY_RUN="dry-run"

SECRET_PATTERNS=[re.compile(r"AKIA[0-9A-Z]{16}"),re.compile(r"-----BEGIN (?:RSA|EC|OPENSSH|PRIVATE) KEY-----"),re.compile(r"api[_-]?key\\s*[:=]",re.I)]
REQ_POLICIES=["TrustDecisionPolicy.v1","EnforcementPolicy.v1","DataUsePolicy.v1","NotificationDeliveryPolicy.v1"]

def utc_now()->str:return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
def canonical_dumps(o:Any)->str:return json.dumps(o,sort_keys=True,separators=(',',':'),ensure_ascii=False)
def hash_obj(o:Any)->str:return sha256(canonical_dumps(o).encode()).hexdigest()
def readj(p:Path)->dict:return json.loads(p.read_text())
def writej(p:Path,d:dict): p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(d,sort_keys=True,indent=2)+"\n")

def validate_policy_subscription_spec(s:dict):
    e=[]
    if s.get('schema')!='PolicySubscriptionSpec.v1': e.append('unsupported schema')
    for k in ('policy_subscription_id','dataset_id','subscription_profile','resolver','lockfile','cache','api'):
        if k not in s: e.append(f'missing {k}')
    if s.get('subscription_profile') not in (None,'strict','standard'): e.append('unsupported subscription_profile')
    if s.get('resolver',{}).get('source') not in (None,'local','remote'): e.append('unsupported resolver source')
    if s.get('resolver',{}).get('source')=='remote' and not s.get('resolver',{}).get('allow_remote_network',False): e.append('remote resolver without explicit allow flag')
    if s.get('lockfile',{}).get('write_lockfile') and not s.get('lockfile',{}).get('execute_flag_required',False): e.append('execute_flag_required must be true')
    return (not e,e)

def validate_schema(o:dict, schema:str): return o.get('schema')==schema

def scan_secrets_text(t:str): return any(p.search(t) for p in SECRET_PATTERNS)

def scan_secrets_path(path:Path):
    for f in path.rglob('*'):
        if f.is_file() and f.suffix in ('.json','.rego','.txt','.pem'):
            if scan_secrets_text(f.read_text(errors='ignore')): return True
    return False

def build_snapshot(spec, dist):
    pol=[]
    for k,v in dist.get('by_schema',{}).items(): pol.append({'policy_schema':k,'sha256':v['sha256'],'cache_path':v['path']})
    s={'schema':'PolicySubscriptionSnapshot.v1','snapshot_id':'','created_at_utc':utc_now(),'policy_subscription_id':spec['policy_subscription_id'],'active_bundle_id':dist['pointer']['active_bundle_id'],'active_bundle_hash':dist['pointer']['active_bundle_hash'],'active_policy_set_hash':dist['set']['active_policy_set_hash'],'runtime_policy_catalog_hash':dist['catalog']['runtime_policy_catalog_hash'],'resolver_index_hash':dist['index']['resolver_index_hash'],'policies':sorted(pol,key=lambda x:x['policy_schema'])}
    s['snapshot_hash']=hash_obj({k:v for k,v in s.items() if k not in ('snapshot_id','created_at_utc')}); s['snapshot_id']='psubsnap_'+s['snapshot_hash'][:12]; return s

def build_lockfile(spec,s):
    l={'schema':'PolicyLockfile.v1','policy_subscription_id':spec['policy_subscription_id'],'created_at_utc':utc_now(),'active_bundle_hash':s['active_bundle_hash'],'active_policy_set_hash':s['active_policy_set_hash'],'runtime_policy_catalog_hash':s['runtime_policy_catalog_hash'],'resolver_index_hash':s['resolver_index_hash'],'policies':[{'policy_schema':p['policy_schema'],'sha256':p['sha256'],'locked_path':p['cache_path']} for p in s['policies']]}
    l['lockfile_hash']=hash_obj({k:v for k,v in l.items() if k!='created_at_utc'}); return l

def build_binding(spec,l):
    b={'schema':'PolicyRuntimeBinding.v1','policy_subscription_id':spec['policy_subscription_id'],'created_at_utc':utc_now(),'lockfile_hash':l['lockfile_hash'],'fail_closed':True,'remote_policy_fetch_allowed':False,'policy_bindings':[{'policy_schema':p['policy_schema'],'path':p['locked_path'],'sha256':p['sha256']} for p in l['policies']]}
    b['binding_hash']=hash_obj({k:v for k,v in b.items() if k!='created_at_utc'}); return b

def load_distribution(root:Path):
    d={'manifest':readj(root/'policy_distribution_manifest.json'),'receipt':readj(root/'policy_distribution_receipt.json'),'index':readj(root/'policy_resolver_index.json'),'pointer':readj(root/'active_policy_pointer.json'),'set':readj(root/'active_policy_set.json'),'catalog':readj(root/'runtime_policy_catalog.json')}
    by={}
    bdir=root/'by-schema'
    if bdir.exists():
        for p in bdir.glob('*.json'):
            o=readj(p); by[o['schema']]={'path':str(p),'sha256':sha256(p.read_bytes()).hexdigest()}
    d['by_schema']=by; return d

def run_policy_subscription(args):
    try:
        spec=readj(Path(args.policy_subscription_spec))
    except Exception:
        print(json.dumps({'status':'error','error_count':1,'policy_subscription_receipt_path':None,'policy_subscription_run_id':None}),file=os.sys.stderr); return Exit.MALFORMED
    ok,errs=validate_policy_subscription_spec(spec)
    if not ok:
        print(json.dumps({'status':'error','error_count':len(errs),'policy_subscription_receipt_path':None,'policy_subscription_run_id':None}),file=os.sys.stderr); return Exit.MALFORMED
    if args.mode==Mode.FETCH_REMOTE.value and not args.allow_remote_network: return Exit.REMOTE
    dist=load_distribution(Path(args.policy_distribution_root)) if args.policy_distribution_root else None
    if dist and (not validate_schema(dist['manifest'],'PolicyDistributionManifest.v1') or not validate_schema(dist['receipt'],'PolicyDistributionReceipt.v1') or dist['receipt'].get('status') not in ('success','warning','verified') or not validate_schema(dist['index'],'PolicyResolverIndex.v1') or not validate_schema(dist['pointer'],'ActivePolicyPointer.v1') or not validate_schema(dist['set'],'ActivePolicySet.v1') or not validate_schema(dist['catalog'],'RuntimePolicyCatalog.v1')):
        return Exit.RESOLVER
    if dist and scan_secrets_path(Path(args.policy_distribution_root)) and not args.allow_secret_findings: return Exit.SECRET
    if dist:
        for r in args.required_policy_schema:
            if r not in dist['by_schema']: return Exit.RESOLVER
        snap=build_snapshot(spec,dist)
    else:
        snap=None
    lock=build_lockfile(spec,snap) if snap else None
    bind=build_binding(spec,lock) if lock else None
    run_id=(spec['policy_subscription_id']+'_'+args.mode).replace('/','_')
    run=Path(args.output_root)/run_id; run.mkdir(parents=True,exist_ok=True)
    receipt={'schema':'PolicySubscriptionReceipt.v1','policy_subscription_run_id':run_id,'status':'success','mode':args.mode}
    if snap: writej(run/'snapshot/policy_subscription_snapshot.json',snap)
    if lock: writej(run/'lock/policy_lockfile.json',lock)
    if bind: writej(run/'binding/policy_runtime_binding.json',bind)
    writej(run/'policy_subscription_receipt.json',receipt)
    print(str(run/'policy_subscription_receipt.json'))
    return Exit.DRY_RUN if args.mode==Mode.DRY_RUN.value else Exit.SUCCESS

def _arg_parser():
    p=argparse.ArgumentParser()
    p.add_argument('--policy-subscription-spec',required=True); p.add_argument('--output-root',required=True); p.add_argument('--mode',required=True,choices=[m.value for m in Mode]); p.add_argument('--policy-distribution-root'); p.add_argument('--subscription-root',default='.')
    p.add_argument('--allow-remote-network',action='store_true'); p.add_argument('--allow-secret-findings',action='store_true'); p.add_argument('--required-policy-schema',action='append',default=[])
    p.add_argument('--policy-subscription-policy'); p.add_argument('--policy-lockfile'); p.add_argument('--rollback-lockfile'); p.add_argument('--policy-subscription-ledger'); p.add_argument('--public-base-url'); p.add_argument('--execute-lock',action='store_true')
    return p

if __name__=='__main__': raise SystemExit(run_policy_subscription(_arg_parser().parse_args()))
