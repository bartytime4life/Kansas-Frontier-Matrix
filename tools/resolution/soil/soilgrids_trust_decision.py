#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, os, re, shutil, subprocess, tempfile
from pathlib import Path
from datetime import datetime, timezone
from urllib.parse import urlparse
from urllib.request import Request, urlopen

ALLOWED_DECISIONS={"allow","warn","review","block"}
ALLOWED_STATUSES={"active","under_review","suspended","revoked","superseded","quarantined","expired","unknown"}
EXIT={"ok":0,"dry":5,"warn":10,"review":15,"block":20,"malformed":30,"resolver":40,"request":50,"policy":60,"opa":70,"sdk":80,"remote":90,"unsafe":100,"secret":110,"internal":120}


def _utc_now(): return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
def _canonical_bytes(o): return json.dumps(o,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
def _sha256_obj(o): return hashlib.sha256(_canonical_bytes(o)).hexdigest()
def _sha256_file(p:Path): return hashlib.sha256(p.read_bytes()).hexdigest()
def _load_json(p:Path): return json.loads(p.read_text(encoding='utf-8'))
def write_canonical_json(p:Path,o):
    p.parent.mkdir(parents=True,exist_ok=True)
    p.write_text(json.dumps(o,sort_keys=True,indent=2)+'\n',encoding='utf-8')

def compute_trust_decision_spec_hash(spec): return _sha256_obj(spec)
def compute_policy_hash(policy): return _sha256_obj(policy)
def compute_decision_input_hash(bundle): b=dict(bundle); [b.pop(k,None) for k in ('created_at_utc','run_id','decision_input_hash')]; return _sha256_obj(b)
def compute_decision_hash(env): b=dict(env); [b.pop(k,None) for k in ('created_at_utc','run_id','decision_hash')]; return _sha256_obj(b)

def validate_trust_decision_spec(spec,allow_remote=False):
 e=[]
 if spec.get('schema')!='TrustDecisionSpec.v1': e.append('unsupported spec schema')
 if not spec.get('trust_decision_id'): e.append('trust_decision_id missing')
 pol=spec.get('policy',{})
 for k,v in pol.items():
  if k.endswith('_status_decision') and v not in ALLOWED_DECISIONS: e.append('unknown decision')
 if spec.get('resolver',{}).get('allow_remote_resolver') and not allow_remote: e.append('remote resolver not allowed')
 return e

def load_trust_decision_policy(spec):
 m={s:spec.get('policy',{}).get(f'{s}_status_decision', d) for s,d in [('active','allow'),('under_review','review'),('suspended','block'),('revoked','block'),('superseded','warn'),('quarantined','block'),('expired','block'),('unknown','block')]}
 return {'schema':'TrustDecisionPolicy.v1','policy_id':'default','allowed_decisions':sorted(ALLOWED_DECISIONS),'status_decision_map':m,'required_checks':['trust.object.resolved'],'blocking_reasons':['revoked','suspended','unknown_status'],'warning_reasons':['superseded']}

def validate_policy(policy):
 e=[]
 if policy.get('schema')!='TrustDecisionPolicy.v1': e.append('bad policy schema')
 if set(policy.get('status_decision_map',{}).keys())!=ALLOWED_STATUSES: e.append('incomplete status map')
 if any(v not in ALLOWED_DECISIONS for v in policy.get('status_decision_map',{}).values()): e.append('unknown decision value')
 return e

def validate_request(req,allow_unknown=False):
 e=[]
 if req.get('schema')!='TrustDecisionRequest.v1': e.append('schema')
 t=req.get('target',{})
 if not any(t.get(k) for k in ('trust_object_id','object_id','object_sha256','disclosure_packet_id','distribution_id','status_url')): e.append('no target')
 if t.get('object_sha256') and not re.fullmatch(r'[0-9a-f]{64}',t['object_sha256']): e.append('bad sha256')
 if t.get('status_url'):
  u=urlparse(t['status_url'])
  if u.scheme not in ('https','http') or '..' in u.path: e.append('unsafe status_url')
 if req.get('purpose') not in (None,'consumer-trust-decision') and not allow_unknown: e.append('unsupported purpose')
 if not req.get('request_id'): req['request_id']=_sha256_obj({'target':t,'purpose':req.get('purpose')})[:24]
 return e

def load_status_resolver_index(root:Path): return _load_json(root/'status_resolver_index.json')
def load_revocation_and_suspension_lists(root:Path): return _load_json(root/'trust_revocation_list.json'), _load_json(root/'trust_suspension_list.json')
def build_resolver_cache(index):
 c={k:{} for k in ['trust_object_id','object_id','object_sha256','disclosure_packet_id','distribution_id','status_url']}
 for o in index.get('objects',[]):
  for k in c:
   if o.get(k): c[k][o[k]]=o
 return c

def resolve_trust_object(cache,target):
 hits=[]
 for k,v in target.items():
  if k in cache and v:
   o=cache[k].get(v)
   if not o: return None,['not found']
   hits.append(o)
 if not hits: return None,['no target identifier provided']
 if len({h['trust_object_id'] for h in hits})!=1: return None,['target identifiers resolve to different objects']
 return hits[0],[]

def evaluate_builtin_policy(policy,resolution):
 r=resolution.get('resolved')
 if not r: return 'block','unresolved',[{'check_id':'trust.object.resolved','severity':'required','status':'fail'}],['resolver_unavailable'],[],['unresolved']
 st=r.get('current_status','unknown')
 d=policy['status_decision_map'].get(st,'block')
 blocks=[]; warns=[]
 if r.get('revoked') or st=='revoked': d='block'; blocks.append('revoked')
 if r.get('suspended') or st=='suspended': d='block'; blocks.append('suspended')
 if st in {'quarantined','expired','unknown'}: d='block'; blocks.append('unknown_status' if st=='unknown' else st)
 if st=='under_review': d='review'
 if st=='superseded': d='warn'; warns.append('superseded')
 return d,f'status={st}',[{'check_id':'trust.object.resolved','severity':'required','status':'pass'}],blocks,warns,[]

def evaluate_opa_policy_if_requested(inp,opa_policy,opa_query,runner=subprocess.run,allow_missing=False):
 if not opa_policy and not opa_query: return None,[]
 if not opa_policy or not opa_query: return None,['opa args missing']
 if '://' in opa_policy: return 'block',['remote opa bundle not allowed']
 try:
  cp=runner(['opa','eval','-f','json','-d',opa_policy,opa_query],input=json.dumps(inp),text=True,capture_output=True)
 except FileNotFoundError:
  return (None,[] if allow_missing else ['opa unavailable'])
 if cp.returncode!=0: return 'block',['opa nonzero']
 try:data=json.loads(cp.stdout)
 except Exception:return 'block',['opa malformed']
 decision=((data.get('decision') or data.get('result',{}).get('decision')))
 if decision not in ALLOWED_DECISIONS: return 'block',['opa malformed']
 return decision,[]

def main(argv=None):
 ap=argparse.ArgumentParser(); ap.add_argument('--trust-decision-spec',required=True); ap.add_argument('--output-root',required=True); ap.add_argument('--mode',required=True)
 ap.add_argument('--status-distribution-root'); ap.add_argument('--request'); ap.add_argument('--trust-object-id'); ap.add_argument('--allow-unknown-purpose',action='store_true'); ap.add_argument('--allow-remote-network',action='store_true'); ap.add_argument('--overwrite',action='store_true')
 a=ap.parse_args(argv)
 spec=_load_json(Path(a.trust_decision_spec))
 se=validate_trust_decision_spec(spec,a.allow_remote_network)
 if se: print(json.dumps({'status':'error','error_count':len(se),'trust_decision_receipt_path':None,'trust_decision_run_id':None}),file=os.sys.stderr); return EXIT['malformed']
 policy=load_trust_decision_policy(spec)
 run_id='run_'+compute_trust_decision_spec_hash(spec)[:10]
 out=Path(a.output_root)/run_id
 if out.exists() and not a.overwrite: return EXIT['unsafe']
 if out.exists(): shutil.rmtree(out)
 out.mkdir(parents=True)
 receipt={'schema':'TrustDecisionReceipt.v1','run_id':run_id,'status':'success'}
 decision='allow'
 if a.status_distribution_root:
  root=Path(a.status_distribution_root); idx=load_status_resolver_index(root); cache=build_resolver_cache(idx)
  req=_load_json(Path(a.request)) if a.request else {'schema':'TrustDecisionRequest.v1','target':{'trust_object_id':a.trust_object_id}}
  re=validate_request(req,a.allow_unknown_purpose)
  if re: print(json.dumps({'status':'error','error_count':len(re),'trust_decision_receipt_path':None,'trust_decision_run_id':run_id}),file=os.sys.stderr); return EXIT['request']
  t=req['target']; obj,errs=resolve_trust_object(cache,t)
  res={'schema':'TrustResolutionResult.v1','request_id':req['request_id'],'resolved':obj,'errors':errs}
  write_canonical_json(out/'trust_resolution_result.json',res)
  decision,_,_,blocks,warns,_=evaluate_builtin_policy(policy,res)
  env={'schema':'TrustDecisionEnvelope.v1','request_id':req['request_id'],'decision':decision,'blocking_reasons':blocks,'warnings':warns,'policy_hash':compute_policy_hash(policy),'resolution_result':res}
  env['decision_hash']=compute_decision_hash(env); write_canonical_json(out/'decision.json',env)
  receipt['decision_hash']=env['decision_hash']
 write_canonical_json(out/'trust_decision_receipt.json',receipt)
 print(str(out/'trust_decision_receipt.json'))
 return EXIT['block'] if decision=='block' else EXIT['review'] if decision=='review' else EXIT['warn'] if decision=='warn' else EXIT['ok']

if __name__=='__main__': raise SystemExit(main())
