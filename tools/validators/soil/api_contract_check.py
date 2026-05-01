#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from urllib import request
REQ=["/health","/openapi.json","/soil/current","/soil/releases","/soil/releases/{release_id}/manifest","/soil/releases/{release_id}/publication-receipt","/soil/records","/soil/records/{bundle_or_safe_bundle_id}","/soil/focus-cards/{safe_bundle_id}","/soil/triplets/{safe_bundle_id}.nt","/soil/governance/retractions","/soil/governance/status"]
BAD=["raw","work","quarantine","processed","api_key","token","secret","password","bearer","private_key","access_key"]
def fetch(base,path):
    with request.urlopen(base.rstrip('/')+path) as r:
        return r.headers, json.loads(r.read().decode())
def main(argv=None):
    ap=argparse.ArgumentParser(); ap.add_argument('--base-url',required=True); ap.add_argument('--openapi',required=True); a=ap.parse_args(argv)
    ok=True; reasons=[]
    h,health=fetch(a.base_url,'/health'); _,oapi_live=fetch(a.base_url,'/openapi.json'); _,cur=fetch(a.base_url,'/soil/current'); _,recs=fetch(a.base_url,'/soil/records'); _,gov=fetch(a.base_url,'/soil/governance/status')
    oapi=json.loads(open(a.openapi).read())
    if oapi.get('info',{}).get('title')!='KFM Soil Public API' or oapi.get('info',{}).get('version')!='v1': ok=False; reasons.append('openapi metadata invalid')
    for r in REQ:
        if r not in oapi.get('paths',{}): ok=False; reasons.append(f'missing route {r}')
    for k in ['X-KFM-Domain','X-KFM-State','X-KFM-Audit-Passed']:
        if not h.get(k): ok=False; reasons.append('missing KFM headers')
    txt=json.dumps(recs).lower()
    for b in BAD:
        if b in txt: ok=False; reasons.append(f'forbidden term {b}')
    out={"ok":ok,"reasons":sorted(set(reasons)),"checked":[health,cur,gov],"live_openapi_title":oapi_live.get('info',{}).get('title')}
    print(json.dumps(out,sort_keys=True)); return 0 if ok else 1
if __name__=='__main__': raise SystemExit(main())
