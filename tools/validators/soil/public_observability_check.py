#!/usr/bin/env python3
import argparse, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT)) if str(ROOT) not in sys.path else None
from tools.observability.soil._delivery_observability_common import *
def main(argv=None):
 ap=argparse.ArgumentParser();ap.add_argument('--observability-root',required=True);ap.add_argument('--observability-id');x=ap.parse_args(argv)
 oid=x.observability_id or load_json(Path(x.observability_root)/'observability/soil/current_public_observability.json')['active_observability_id']
 d=Path(x.observability_root)/f'observability/soil/cycles/{oid}'; fails=[]
 m=load_json(d/'public_delivery_observability_manifest.json'); r=load_json(d/'public_observability_receipt.json')
 if m.get('object_type')!='SoilPublicDeliveryObservabilityManifest': fails.append('bad manifest')
 if m.get('public_observability_status')!='PUBLIC_DELIVERY_OBSERVABILITY_READY': fails.append('bad status')
 if r.get('receipt_type')!='PublicObservabilityReceipt': fails.append('bad receipt')
 if not r.get('signatures'): fails.append('missing signatures')
 for k,v in r.get('generated_artifacts',{}).items():
  p=d/k
  if not p.exists() or sha256_file(p)!=v: fails.append(f'hash mismatch:{k}')
 print(json.dumps({'public_observability_valid':not fails,'observability_id':oid,'delivery_id':m.get('delivery_id'),'routing_id':m.get('routing_id'),'prior_release_id':m.get('prior_release_id'),'active_release_id':m.get('active_release_id'),'observability_state':m.get('observability_state'),'failure_reasons':fails}))
 return 0 if not fails else 1
if __name__=='__main__': raise SystemExit(main())
