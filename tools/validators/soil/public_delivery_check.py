#!/usr/bin/env python3
import argparse, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.delivery.soil._public_delivery_common import *

def main(argv=None):
    ap=argparse.ArgumentParser(); ap.add_argument('--delivery-root',required=True); ap.add_argument('--delivery-id')
    a=ap.parse_args(argv)
    if a.delivery_id: did=a.delivery_id
    else: did=load_json(Path(a.delivery_root)/'delivery/soil/current_public_delivery.json')['active_delivery_id']
    d=Path(a.delivery_root)/'delivery/soil/cycles'/did
    fails=[]
    m=load_json(d/'public_delivery_manifest.json'); r=load_json(d/'public_delivery_receipt.json')
    if m.get('object_type')!='SoilPublicDeliveryManifest': fails.append('bad manifest')
    if m.get('public_delivery_status')!='PUBLIC_DELIVERY_VERIFIED': fails.append('bad status')
    if r.get('receipt_type')!='PublicDeliveryReceipt': fails.append('bad receipt')
    if r.get('from_state')!='PUBLIC_ROUTING_RECONCILED' or r.get('to_state')!='PUBLIC_DELIVERY_VERIFIED': fails.append('bad transition')
    if r.get('decision') not in {'pass','degraded','governance_only'}: fails.append('bad decision')
    if not r.get('signatures'): fails.append('missing signatures')
    for k,v in r.get('generated_artifacts',{}).items():
        p=d/k
        if not p.exists() or sha256_file(p)!=v: fails.append(f'hash mismatch:{k}')
    out={'public_delivery_valid':not fails,'delivery_id':did,'routing_id':m.get('routing_id'),'prior_release_id':m.get('prior_release_id'),'active_release_id':m.get('active_release_id'),'delivery_state':m.get('delivery_state'),'failure_reasons':fails}
    print(json.dumps(out)); return 0 if not fails else 1
if __name__=='__main__': raise SystemExit(main())
