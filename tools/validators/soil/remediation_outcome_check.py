#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.remediation.soil._outcome_common import load_json,sha256_file,stable_payload_hash

def main(argv=None):
 ap=argparse.ArgumentParser(); ap.add_argument('--outcome-root',required=True); ap.add_argument('--outcome-cycle-id'); a=ap.parse_args(argv)
 cur=load_json(Path(a.outcome_root)/'outcomes/soil/current_remediation_outcome.json'); oc=a.outcome_cycle_id or cur['active_outcome_cycle_id']; c=Path(a.outcome_root)/f'outcomes/soil/cycles/{oc}'
 m=load_json(c/'remediation_outcome_manifest.json'); r=load_json(c/'remediation_outcome_receipt.json'); t=load_json(c/'remediation_outcome_transparency_log.json')
 ok=True; reasons=[]
 if m.get('object_type')!='SoilRemediationOutcomeManifest': ok=False; reasons.append('bad manifest type')
 if r.get('receipt_type')!='RemediationOutcomeReceipt': ok=False; reasons.append('bad receipt type')
 for fn,h in m.get('artifact_hashes',{}).items():
  if fn=='remediation_outcome_manifest.json': continue
  if sha256_file(c/fn)!=h.split(':',1)[-1]: ok=False; reasons.append('artifact hash mismatch'); break
 prev=None; prev_ordinal=None
 for e in t.get('entries',[]):
  x=dict(e); eh=x.pop('entry_hash',None)
  if 'sha256:'+stable_payload_hash(x)!=eh: ok=False; reasons.append('bad log hash'); break
  if prev is None:
   if e.get('previous_entry_hash') not in (None,''): ok=False; reasons.append('bad previous entry hash'); break
  else:
   if e.get('previous_entry_hash')!=prev: ok=False; reasons.append('bad previous entry hash'); break
  if 'ordinal' in e:
   if prev_ordinal is None:
    if e.get('ordinal')!=1: ok=False; reasons.append('bad log ordinal'); break
   else:
    if e.get('ordinal')!=prev_ordinal+1: ok=False; reasons.append('bad log ordinal'); break
   prev_ordinal=e.get('ordinal')
  prev=eh
 if t.get('log_root')!=prev: ok=False; reasons.append('log root mismatch')
 out={'remediation_outcome_valid':ok,'outcome_cycle_id':oc,'remediation_id':m.get('remediation_id'),'registry_id':m.get('registry_id'),'release_id':m.get('release_id'),'outcome_state':m.get('outcome_state'),'failure_reasons':reasons}
 print(json.dumps(out,sort_keys=True)); return 0 if ok else 1
if __name__=='__main__': raise SystemExit(main())
