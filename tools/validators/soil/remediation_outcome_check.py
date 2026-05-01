#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.remediation.soil._outcome_common import load_json,sha256_file,stable_payload_hash

def main(argv=None):
 ap=argparse.ArgumentParser(); ap.add_argument('--outcome-root',required=True); ap.add_argument('--outcome-cycle-id'); a=ap.parse_args(argv)
 if a.outcome_cycle_id: oid=a.outcome_cycle_id
 else: oid=load_json(Path(a.outcome_root)/'outcomes/soil/current_remediation_outcome.json')['active_outcome_cycle_id']
 c=Path(a.outcome_root)/f'outcomes/soil/cycles/{oid}'
 m=load_json(c/'remediation_outcome_manifest.json'); r=load_json(c/'remediation_outcome_receipt.json'); t=load_json(c/'remediation_outcome_transparency_log.json')
 ok=m.get('object_type')=='SoilRemediationOutcomeManifest' and r.get('receipt_type')=='RemediationOutcomeReceipt' and r.get('signatures')
 for k,v in r.get('generated_artifacts',{}).items():
  if k=='remediation_outcome_manifest.json':
   continue
  if ('sha256:'+sha256_file(c/k))!=v: ok=False
 prev=None
 for e in t.get('entries',[]):
  x=dict(e); eh=x.pop('entry_hash',None)
  if stable_payload_hash(x)!=eh: ok=False
  prev=eh
 ok=ok and t.get('log_root')==prev
 print(json.dumps({'remediation_outcome_valid':bool(ok),'outcome_cycle_id':oid,'remediation_id':m.get('remediation_id'),'registry_id':m.get('registry_id'),'release_id':m.get('release_id'),'outcome_state':m.get('outcome_state'),'failure_reasons':[] if ok else ['validation failed']},sort_keys=True))
 return 0 if ok else 1
if __name__=='__main__': raise SystemExit(main())
