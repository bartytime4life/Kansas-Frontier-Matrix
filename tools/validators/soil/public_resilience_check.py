#!/usr/bin/env python3
import argparse, json
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.resilience.soil._resilience_common import *
def main(argv=None):
 ap=argparse.ArgumentParser(); ap.add_argument('--resilience-root',required=True); ap.add_argument('--resilience-id'); a=ap.parse_args(argv)
 cur=load_json(Path(a.resilience_root)/'resilience/soil/current_public_delivery_resilience.json'); rid=a.resilience_id or cur['active_resilience_id']; d=Path(a.resilience_root)/'resilience/soil/cycles'/rid
 m=load_json(d/'public_delivery_resilience_manifest.json'); r=load_json(d/'public_delivery_resilience_receipt.json'); fails=[]
 if m.get('object_type')!='SoilPublicDeliveryResilienceManifest': fails.append('bad manifest')
 if m.get('public_resilience_status')!='PUBLIC_DELIVERY_RESILIENCE_READY': fails.append('bad status')
 if r.get('receipt_type')!='PublicDeliveryResilienceReceipt': fails.append('bad receipt')
 if not r.get('signatures'): fails.append('missing signatures')
 for k,v in r.get('generated_artifacts',{}).items():
  p=d/k
  if not p.exists() or sha256_file(p)!=v: fails.append(f'hash mismatch:{k}')
 if scan_payload_for_forbidden_terms(m) or scan_payload_for_contact_or_secret_terms(m): fails.append('unsafe payload')
 out={'public_resilience_valid':not fails and m.get('resilience_state')!='blocked','resilience_id':rid,'closure_id':m.get('closure_id'),'incident_response_id':m.get('incident_response_id'),'delivery_id':m.get('delivery_id'),'routing_id':m.get('routing_id'),'prior_release_id':m.get('prior_release_id'),'active_release_id':m.get('active_release_id'),'resilience_state':m.get('resilience_state'),'failure_reasons':fails}
 print(json.dumps(out)); return 0 if out['public_resilience_valid'] else 1
if __name__=='__main__': raise SystemExit(main())
