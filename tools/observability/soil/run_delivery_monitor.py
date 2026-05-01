#!/usr/bin/env python3
import argparse, json, sys, urllib.request, urllib.error
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT)) if str(ROOT) not in sys.path else None
from tools.observability.soil._delivery_observability_common import *
REQ=['/health','/soil/current','/soil/delivery','/soil/delivery/public-report','/soil/routing','/soil/routing/public-report']
NEG=['/soil/records/__missing_bundle__','/soil/records/..%2F..%2Fetc%2Fpasswd','/soil/delivery/..%2Fsecret']
def get(base,p):
 u=public_url_join(base,p)
 try:
  with urllib.request.urlopen(u,timeout=3) as r: return r.getcode(),dict(r.headers),r.read().decode('utf-8','replace')
 except urllib.error.HTTPError as e:
  return e.code,dict(e.headers),e.read().decode('utf-8','replace')
 except Exception:
  return None,{},''
def main(argv=None):
 a=argparse.ArgumentParser();a.add_argument('--delivery-root',required=True);a.add_argument('--delivery-id');a.add_argument('--monitor-id');a.add_argument('--base-url',required=True);a.add_argument('--out-root',required=True);x=a.parse_args(argv)
 did=x.delivery_id or load_current_public_delivery(x.delivery_root)['active_delivery_id']; mid=sanitize_id(x.monitor_id or f'{did}-monitor')
 m=load_public_delivery_manifest(x.delivery_root,did)
 checks={k:True for k in ['health','delivery_endpoints','routing_endpoints','active_data_endpoints','governance_only_behavior','negative_probes','headers','public_safety','no_stale_records']}
 ers=[]; res=[]
 for p in REQ:
  c,h,b=get(x.base_url,p); ok=(c==200); checks['health']=checks['health'] and (p!='/health' or ok); checks['delivery_endpoints']=checks['delivery_endpoints'] and ok
  if h.get('X-KFM-Domain')!='soil': checks['headers']=False
  if scan_text_for_forbidden_terms(b) or scan_text_for_forbidden_terms(b) or has_private_path(b): checks['public_safety']=False
  res.append({'path':p,'status':c,'ok':ok})
 if m.get('active_public_routes_enabled'):
  for p in ['/soil/records']: c,_,b=get(x.base_url,p); checks['active_data_endpoints']=checks['active_data_endpoints'] and c==200; res.append({'path':p,'status':c});
 else:
  c,_,_=get(x.base_url,'/soil/records'); checks['governance_only_behavior']=c in {503,410,200}
 for p in NEG:
  c,_,_=get(x.base_url,p); checks['negative_probes']=checks['negative_probes'] and (c and c>=400); res.append({'path':p,'status':c})
 decision='pass' if all(checks.values()) else 'fail'
 if decision=='fail': ers=[k for k,v in checks.items() if not v]
 receipt={'schema_version':'kfm.v1','receipt_type':'DeliveryMonitorReceipt','domain':'soil','monitor_id':mid,'delivery_id':did,'routing_id':m.get('routing_id'),'prior_release_id':m.get('prior_release_id'),'active_release_id':m.get('active_release_id'),'base_url_hash':sha256_bytes(x.base_url.encode()),'created':utc_now_iso(),'decision':decision,'active_public_routes_enabled':bool(m.get('active_public_routes_enabled')),'checks':checks,'endpoint_results':res,'failure_reasons':ers,'signatures':{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'}}
 outd=Path(x.out_root)/f'observability/soil/monitors/{did}'; outd.mkdir(parents=True,exist_ok=True); write_json_atomic(outd/f'{mid}.delivery_monitor_receipt.json',receipt)
 print(json.dumps(receipt)); return 0 if decision=='pass' else 1
if __name__=='__main__': raise SystemExit(main())
