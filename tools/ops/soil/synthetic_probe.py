#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
import argparse, json, sys, urllib.request, urllib.error
from pathlib import Path
from tools.ops.soil._ops_common import *

def get(url):
 try:
  with urllib.request.urlopen(url,timeout=4) as r: return r.status, dict(r.headers.items()), r.read(), None
 except urllib.error.HTTPError as e: return e.code, dict(e.headers.items()), e.read(), None
 except Exception as e: return None,{},b'',str(e)

def main(argv=None):
 a=argparse.ArgumentParser();a.add_argument('--base-url',required=True);a.add_argument('--expected-release-id');a.add_argument('--probe-id');a.add_argument('--out-root');x=a.parse_args(argv)
 checks={k:False for k in ['health','openapi','current','records','focus_card','triplets','governance_status','negative_probes','headers','forbidden_terms','public_paths_only']}; fr=[]; er=[]; rel=''
 req=['/health','/openapi.json','/soil/current','/soil/releases','/soil/records','/soil/governance/status']
 payload_for_id={'base_url':x.base_url,'expected_release_id':x.expected_release_id}; pid=sanitize_id(x.probe_id or deterministic_probe_id(payload_for_id))
 for ep in req:
  s,h,b,e=get(x.base_url+ep); item={'endpoint':ep,'status':s,'error':e}; er.append(item)
  if e: fr.append(f'{ep} unreachable'); continue
  try: body=json.loads(b.decode()) if ep!='/openapi.json' or b[:1] in [b'{',b'['] else json.loads(b.decode())
  except Exception: body=None
  if ep=='/health': checks['health']=s==200 and isinstance(body,dict) and body.get('status')=='ok'
  if ep=='/openapi.json': checks['openapi']=s==200 and isinstance(body,dict)
  if ep=='/soil/current': checks['current']=s==200 and isinstance(body,dict)
  if ep=='/soil/records': checks['records']=s==200 and isinstance(body,dict)
  if ep=='/soil/governance/status': checks['governance_status']=s==200 and isinstance(body,dict) and body.get('public_access_allowed') is True
  if h.get('X-KFM-Domain')=='soil' and h.get('X-KFM-State')=='PUBLISHED' and h.get('X-KFM-Audit-Passed')=='true' and h.get('X-KFM-Release-ID'): checks['headers']=True; rel=h.get('X-KFM-Release-ID')
  if scan_text_for_forbidden_terms(b.decode(errors='ignore')): fr.append(f'forbidden terms in {ep}')
 if x.expected_release_id and rel and x.expected_release_id!=rel: fr.append('expected release mismatch')
 s,h,b,_=get(x.base_url+'/soil/records'); recs=(json.loads(b.decode()).get('records') if s==200 else []) or []
 if recs:
  bid=recs[0].get('bundle_id',''); sid=recs[0].get('safe_bundle_id',sanitize_id(bid))
  s1,_,b1,_=get(x.base_url+'/soil/records/'+urllib.parse.quote(bid,safe='')); s2,_,_,_=get(x.base_url+'/soil/focus-cards/'+sid); s3,_,t3,_=get(x.base_url+'/soil/triplets/'+sid+'.nt')
  checks['focus_card']=s2==200; checks['triplets']=s3==200 and bool(t3.decode(errors='ignore').strip())
  er+=[{'endpoint':'/soil/records/{bundle_id}','status':s1},{'endpoint':'/soil/focus-cards/{safe_bundle_id}','status':s2},{'endpoint':'/soil/triplets/{safe_bundle_id}.nt','status':s3}]
 neg=['/soil/records/__missing_bundle__','/soil/records/..%2F..%2Fetc%2Fpasswd','/soil/records?limit=not-a-number']
 ok=True
 for ep in neg:
  s,_,b,_=get(x.base_url+ep)
  try:j=json.loads(b.decode())
  except: j={}
  ok=ok and (s and s>=400 and isinstance(j,dict) and j.get('error') is True)
 checks['negative_probes']=ok; checks['forbidden_terms']=not fr; checks['public_paths_only']=True
 decision='pass' if all(checks.values()) else 'fail'
 if decision=='fail' and not fr: fr=['one or more checks failed']
 out={"schema_version":"kfm.v1","receipt_type":"SyntheticProbeReceipt","domain":"soil","probe_id":pid,"base_url_hash":sha256_bytes(x.base_url.encode()),"release_id":rel,"created":utc_now_iso(),"decision":decision,"checks":checks,"endpoint_results":er,"failure_reasons":fr,"signatures":{"dsse":"PROPOSED-COSIGN","key_ref":"kfm://keys/ci"}}
 if x.out_root: write_json_atomic(Path(x.out_root)/'ops/soil/probes'/f'{pid}.probe_receipt.json',out)
 print(json.dumps(out,sort_keys=True))
 return 0 if decision=='pass' else 1
if __name__=='__main__': raise SystemExit(main())
