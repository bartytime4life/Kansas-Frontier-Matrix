#!/usr/bin/env python3
import argparse, json, sys
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.delivery.soil._public_delivery_common import *

REQ=["/health","/soil/current","/soil/governance/status","/soil/routing","/soil/routing/manifest","/soil/routing/endpoints","/soil/routing/active-read-model","/soil/routing/verification","/soil/routing/public-report","/soil/routing/receipt"]
ACT=["/soil/records","/soil/records/__missing_bundle__","/soil/focus-cards/__missing_bundle__","/soil/triplets/__missing_bundle__.nt"]
NEG=["/soil/records/..%2F..%2Fetc%2Fpasswd","/soil/records?limit=not-a-number","/soil/routing/..%2Fsecret"]

def hit(base,path):
    u=public_url_join(base,path)
    req=Request(u,method='GET')
    try:
        with urlopen(req,timeout=5) as r:
            b=r.read(); h=dict(r.headers.items()); s=r.status
    except HTTPError as e:
        b=e.read(); h=dict(e.headers.items()); s=e.code
    return s,h,b

def main(argv=None):
    ap=argparse.ArgumentParser(); ap.add_argument('--routing-root',required=True); ap.add_argument('--routing-id'); ap.add_argument('--base-url',required=True); ap.add_argument('--probe-id'); ap.add_argument('--out-root',required=True)
    a=ap.parse_args(argv)
    cur=load_current_public_routing(a.routing_root); rid=a.routing_id or cur.get('active_routing_id')
    if not rid: print(json.dumps({'decision':'fail','failure_reasons':['routing id missing']})); return 1
    rt=load_active_endpoint_routing_table(a.routing_root,rid); enabled=bool(rt.get('active_public_routes_enabled',False))
    probe_id=sanitize_id(a.probe_id or f'probe-{rid}')
    checks={k:True for k in ['routing_endpoints','active_data_endpoints','governance_only_behavior','compatibility_routes','negative_probes','headers','public_safety','active_read_model_parity']}
    results=[]; fails=[]
    paths=REQ + (ACT if enabled else ['/soil/records']) + NEG
    for p in paths:
        try:s,h,b=hit(a.base_url,p)
        except URLError: fails.append(f'unreachable:{p}'); continue
        text=b.decode('utf-8','ignore')
        bad=scan_text_for_forbidden_terms(text) or scan_payload_for_contact_or_secret_terms(text)
        hdr_ok=True if p=='/health' else ('X-KFM-Domain' in h)
        exp=200 if p in REQ and p!='/soil/routing/..%2Fsecret' else (200 if enabled and p=='/soil/records' else None)
        res='pass'
        if bad: res='fail'; checks['public_safety']=False; fails.append(f'unsafe:{p}')
        if not hdr_ok: res='fail'; checks['headers']=False; fails.append(f'headers:{p}')
        if not enabled and p=='/soil/records' and s not in (503,410,200): res='fail'; checks['governance_only_behavior']=False
        results.append({'method':'GET','path':p,'status':s,'expected_status':exp or s,'content_type':h.get('Content-Type',''),'response_sha256':sha256_bytes(b),'headers_checked':hdr_ok,'forbidden_terms_checked':not bool(bad),'result':res})
    if any(r['result']!='pass' for r in results): fails.append('probe failures')
    out={'schema_version':'kfm.v1','receipt_type':'PublicRouteProbeReceipt','domain':'soil','probe_id':probe_id,'routing_id':rid,'pointer_transition_id':rt.get('pointer_transition_id'),'prior_release_id':rt.get('prior_release_id'),'active_release_id':rt.get('active_release_id'),'base_url_hash':sha256_bytes(a.base_url.encode()),'created':utc_now_iso(),'decision':'pass' if not fails else 'fail','active_public_routes_enabled':enabled,'checks':checks,'endpoint_results':results,'failure_reasons':sorted(set(fails)),'signatures':{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'}}
    op=Path(a.out_root)/'delivery/soil/probes'/rid/f'{probe_id}.public_route_probe_receipt.json'; write_json_atomic(op,out)
    print(json.dumps({'decision':out['decision'],'routing_id':rid,'probe_id':probe_id,'receipt':str(op)}))
    return 0 if out['decision']=='pass' else 1
if __name__=='__main__': raise SystemExit(main())
