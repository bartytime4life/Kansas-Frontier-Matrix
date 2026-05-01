#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, sys
from urllib import request, error, parse

def get(base,path):
    req=request.Request(base.rstrip('/')+path)
    with request.urlopen(req) as r:
        h=r.headers
        if h.get('X-KFM-Domain')!='soil' or h.get('X-KFM-State')!='PUBLISHED' or h.get('X-KFM-Audit-Passed')!='true': raise ValueError('invalid KFM headers')
        return json.loads(r.read().decode())
def main(argv=None):
    ap=argparse.ArgumentParser(); ap.add_argument('--base-url',required=True); ap.add_argument('--list',action='store_true'); ap.add_argument('--bundle-id'); ap.add_argument('--health',action='store_true')
    a=ap.parse_args(argv)
    try:
        if a.health: p=get(a.base_url,'/health')
        elif a.list: p=get(a.base_url,'/soil/records'); assert p.get('object_type')=='SoilPublicReadModel'
        elif a.bundle_id: p=get(a.base_url,'/soil/records/'+parse.quote(a.bundle_id,safe=''))
        else: raise ValueError('select operation')
        print(json.dumps(p,sort_keys=True)); return 0
    except (error.HTTPError,error.URLError,ValueError,AssertionError) as e:
        print(json.dumps({"error":True,"reason":str(e)},sort_keys=True)); return 1
if __name__=='__main__': raise SystemExit(main())
