#!/usr/bin/env python3
import argparse, json
from pathlib import Path
from tools.incident_closure.soil._incident_closure_common import *
def main(argv=None):
 ap=argparse.ArgumentParser(); ap.add_argument('--closure-root',required=True); ap.add_argument('--closure-id'); a=ap.parse_args(argv)
 croot=Path(a.closure_root)/'incident_closure/soil'; cid=a.closure_id or load_json(croot/'current_delivery_incident_closure.json')['active_closure_id']
 d=croot/'cycles'/cid
 fails=[]
 m=load_json(d/'delivery_incident_closure_manifest.json'); r=load_json(d/'delivery_incident_closure_receipt.json')
 if m.get('object_type')!='SoilDeliveryIncidentClosureManifest': fails.append('bad manifest type')
 if m.get('incident_closure_status')!='PUBLIC_DELIVERY_INCIDENT_CLOSURE_READY': fails.append('bad closure status')
 if r.get('receipt_type')!='DeliveryIncidentClosureReceipt': fails.append('bad receipt type')
 if not r.get('signatures'): fails.append('missing signatures')
 for k,v in r.get('generated_artifacts',{}).items():
  p=d/k
  if not p.exists() or sha256_file(p)!=v: fails.append(f'hash mismatch:{k}')
 if scan_payload_for_forbidden_terms(m) or scan_payload_for_contact_or_secret_terms(m): fails.append('unsafe manifest')
 out={'delivery_incident_closure_valid':not fails,'closure_id':cid,'incident_response_id':m.get('incident_response_id'),'observability_id':m.get('observability_id'),'delivery_id':m.get('delivery_id'),'routing_id':m.get('routing_id'),'prior_release_id':m.get('prior_release_id'),'active_release_id':m.get('active_release_id'),'closure_state':m.get('closure_state'),'failure_reasons':fails}
 print(json.dumps(out)); return 0 if not fails and m.get('closure_state')!='blocked' else 1
if __name__=='__main__': raise SystemExit(main())
