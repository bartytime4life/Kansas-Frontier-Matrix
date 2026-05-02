#!/usr/bin/env python3
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.recommissioning.soil._recommissioning_common import *

def main(argv=None):
 p=argparse.ArgumentParser(); p.add_argument('--recommissioning-root',required=True); p.add_argument('--recommissioning-id'); a=p.parse_args(argv)
 ptr=load_json(Path(a.recommissioning_root)/'recommissioning/soil/current_delivery_recommissioning.json'); rid=a.recommissioning_id or ptr['active_recommissioning_id']; d=Path(a.recommissioning_root)/f'recommissioning/soil/cycles/{rid}'
 m=load_json(d/'delivery_recommissioning_manifest.json'); r=load_json(d/'delivery_recommissioning_receipt.json'); fails=[]
 if m.get('object_type')!='SoilDeliveryRecommissioningManifest': fails.append('bad manifest')
 if r.get('receipt_type')!='DeliveryRecommissioningReceipt': fails.append('bad receipt')
 if not r.get('signatures'): fails.append('missing signatures')
 for k,v in r.get('generated_artifacts',{}).items():
  pth=d/k
  if not pth.exists() or sha256_file(pth)!=v: fails.append('hash mismatch '+k)
 out={'delivery_recommissioning_valid':not fails and m.get('recommissioning_state')!='blocked','recommissioning_id':rid,'resilience_id':m.get('resilience_id'),'closure_id':m.get('closure_id'),'delivery_id':m.get('delivery_id'),'routing_id':m.get('routing_id'),'prior_release_id':m.get('prior_release_id'),'active_release_id':m.get('active_release_id'),'recommissioning_state':m.get('recommissioning_state'),'failure_reasons':fails}
 print(json.dumps(out)); return 0 if out['delivery_recommissioning_valid'] else 1
if __name__=='__main__': raise SystemExit(main())
