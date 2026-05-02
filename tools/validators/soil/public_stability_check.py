#!/usr/bin/env python3
import argparse, json, sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[3]))
from pathlib import Path
from tools.stability.soil._stability_common import *

def main():
 p=argparse.ArgumentParser();p.add_argument('--stability-root',required=True);p.add_argument('--stability-id');a=p.parse_args()
 if a.stability_id: sid=a.stability_id
 else: sid=load_json(Path(a.stability_root)/'stability/soil/current_public_delivery_stability.json')['active_stability_id']
 cyc=Path(a.stability_root)/'stability/soil/cycles'/sid
 m=load_json(cyc/'public_delivery_stability_manifest.json'); r=load_json(cyc/'public_delivery_stability_receipt.json')
 ok=m.get('object_type')=='SoilPublicDeliveryStabilityManifest' and r.get('receipt_type')=='PublicDeliveryStabilityReceipt' and r.get('signatures')
 out={"public_stability_valid":bool(ok),"stability_id":sid,"continuity_id":m.get('continuity_id'),"stability_state":m.get('stability_state'),'failure_reasons':[] if ok else ['invalid']}
 print(json.dumps(out)); return 0 if ok else 2
if __name__=='__main__': sys.exit(main())
