#!/usr/bin/env python3
import argparse,json
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.recommissioning.soil._recommissioning_common import *
def main(argv=None):
 p=argparse.ArgumentParser(); p.add_argument('--recommissioning-root',required=True); p.add_argument('--recommissioning-id'); ns=p.parse_args(argv)
 cid=ns.recommissioning_id or load_json(Path(ns.recommissioning_root)/'recommissioning/soil/current_delivery_recommissioning.json')['active_recommissioning_id']
 root=Path(ns.recommissioning_root)/f'recommissioning/soil/cycles/{cid}'
 m=load_json(root/'delivery_recommissioning_manifest.json'); r=load_json(root/'delivery_recommissioning_receipt.json')
 ok=m.get('object_type')=='SoilDeliveryRecommissioningManifest' and r.get('receipt_type')=='DeliveryRecommissioningReceipt' and r.get('signatures')
 print(json.dumps({'delivery_recommissioning_valid':bool(ok and m.get('recommissioning_state')!='blocked'),'recommissioning_id':cid,'resilience_id':m.get('resilience_id'),'closure_id':m.get('closure_id'),'delivery_id':m.get('delivery_id'),'routing_id':m.get('routing_id'),'prior_release_id':m.get('prior_release_id'),'active_release_id':m.get('active_release_id'),'recommissioning_state':m.get('recommissioning_state'),'failure_reasons':[] if ok else ['invalid']}))
 return 0 if ok and m.get('recommissioning_state')!='blocked' else 1
if __name__=='__main__': raise SystemExit(main())
