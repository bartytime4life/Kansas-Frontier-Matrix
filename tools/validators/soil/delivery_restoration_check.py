#!/usr/bin/env python3
import argparse, json
from pathlib import Path
from tools.restoration.soil._delivery_restoration_common import *

def main(argv=None):
 p=argparse.ArgumentParser(); p.add_argument('--restoration-root',required=True); p.add_argument('--restoration-id'); ns=p.parse_args(argv)
 rid=ns.restoration_id or load_json(Path(ns.restoration_root)/'restoration/soil/current_delivery_restoration.json')['active_restoration_id']
 root=Path(ns.restoration_root)/f'restoration/soil/cycles/{rid}'
 m=load_json(root/'delivery_restoration_manifest.json'); r=load_json(root/'delivery_restoration_receipt.json'); t=load_json(root/'restoration_transparency_log.json')
 ok=m.get('object_type')=='SoilDeliveryRestorationManifest' and m.get('delivery_restoration_status')=='PUBLIC_DELIVERY_RESTORATION_READY' and r.get('receipt_type')=='DeliveryRestorationReceipt' and r.get('from_state')=='PUBLIC_DELIVERY_RECOMMISSIONING_READY' and r.get('to_state')=='PUBLIC_DELIVERY_RESTORATION_READY' and r.get('signatures')
 print(json.dumps({'delivery_restoration_valid':bool(ok and m.get('restoration_state')!='blocked'),'restoration_id':rid,'recommissioning_id':m.get('recommissioning_id'),'delivery_id':m.get('delivery_id'),'routing_id':m.get('routing_id'),'prior_release_id':m.get('prior_release_id'),'active_release_id':m.get('active_release_id'),'restoration_state':m.get('restoration_state'),'failure_reasons':[] if ok else ['invalid']}))
 return 0 if ok and m.get('restoration_state')!='blocked' else 1
if __name__=='__main__': raise SystemExit(main())
