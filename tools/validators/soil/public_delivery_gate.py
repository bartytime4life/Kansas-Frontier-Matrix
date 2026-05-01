#!/usr/bin/env python3
import argparse, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.validators.soil.public_delivery_check import main as check_main
from tools.delivery.soil._public_delivery_common import *

def main(argv=None):
    ap=argparse.ArgumentParser();
    for k in ['delivery-root','routing-root','active-root','lineage-root','outcome-root','remediation-root','corrective-root','resolution-root','accountability-root','assurance-root','registry-root','certification-root','archive-root','preservation-root','reconciliation-root','federation-root','discovery-root','published-root','ops-root']:
        ap.add_argument('--'+k,required=True)
    a=ap.parse_args(argv)
    rc=check_main(['--delivery-root',a.delivery_root])
    ptr=load_json(Path(a.delivery_root)/'delivery/soil/current_public_delivery.json')
    cur=load_current_public_routing(a.routing_root)
    fails=[]
    if rc!=0: fails.append('public delivery check failed')
    if cur.get('active_routing_id')!=ptr.get('routing_id'): fails.append('routing mismatch')
    decision='pass' if not fails else 'block'
    out={'public_delivery_advertising_allowed':not fails,'prior_release_id':ptr.get('prior_release_id'),'active_release_id':ptr.get('active_release_id'),'delivery_id':ptr.get('active_delivery_id'),'delivery_state':ptr.get('delivery_state'),'decision':decision,'failure_reasons':fails}
    print(json.dumps(out)); return 0 if not fails else 1
if __name__=='__main__': raise SystemExit(main())
