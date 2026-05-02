#!/usr/bin/env python3
import argparse,json,urllib.request
from pathlib import Path
from tools.restoration.soil._delivery_restoration_common import *

def main(argv=None):
 p=argparse.ArgumentParser(); p.add_argument('--recommissioning-root',required=True); p.add_argument('--base-url',required=True); p.add_argument('--out-root',required=True); p.add_argument('--recommissioning-id'); p.add_argument('--probe-id'); ns=p.parse_args(argv)
 rid=ns.recommissioning_id or load_current_delivery_recommissioning(ns.recommissioning_root)['active_recommissioning_id']; m=load_delivery_recommissioning_manifest(ns.recommissioning_root,rid)
 pid=sanitize_id(ns.probe_id or f'soil-restoration-probe-{rid}')
 endpoints=['/health','/soil/current','/soil/recommissioning','/soil/recommissioning/public-report','/soil/delivery','/soil/routing']
 checks=[]; ok=True
 for ep in endpoints:
  try:
   r=urllib.request.urlopen(ns.base_url.rstrip('/')+ep,timeout=3); checks.append({'endpoint':ep,'status':r.status})
  except Exception:
   ok=False; checks.append({'endpoint':ep,'status':0})
 rec={'schema_version':'kfm.v1','object_type':'SoilRestorationProbeReceipt','domain':'soil','probe_id':pid,'recommissioning_id':rid,'decision':'pass' if ok else 'fail','active_public_delivery_restored':m.get('recommissioning_state')=='recommissioned_active','endpoint_count':len(checks),'checks':checks,'created':utc_now_iso()}
 out=Path(ns.out_root)/f'restoration/soil/probes/{rid}/{pid}.restoration_probe_receipt.json'; write_json_atomic(out,rec); print(json.dumps(rec)); return 0 if ok else 1
if __name__=='__main__': raise SystemExit(main())
