#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.remediation.soil._outcome_common import *

def main(argv=None):
 ap=argparse.ArgumentParser(); ap.add_argument('--remediation-root',required=True); ap.add_argument('--registry-root',required=True); ap.add_argument('--outcome-root',required=True); ap.add_argument('--outcome',required=True); ap.add_argument('--remediation-id'); a=ap.parse_args(argv)
 req=load_json(a.outcome); rid=a.remediation_id or load_current_remediation_handoff(a.remediation_root)['active_remediation_id']; tr=load_certificate_event_execution_tracker(a.remediation_root,rid); man=load_remediation_handoff_manifest(a.remediation_root,rid)
 ex=next((x for x in tr.get('executions',[]) if x.get('execution_id')==req.get('execution_id')),None); reasons=[]
 if req.get('steward_review',{}).get('decision')!='approved': reasons.append('missing steward')
 if not ex: reasons.append('missing execution')
 else:
  if ex.get('dispatch_id')!=req.get('dispatch_id') or ex.get('event_type')!=req.get('event_type'): reasons.append('event mismatch')
 if req.get('event_type') in {'suspend','revoke','tombstone'} and not req.get('certificate_event_receipt_ref'): reasons.append('missing receipt')
 if req.get('event_type')=='suspend' and req.get('certificate_status_after')!='suspended': reasons.append('status mismatch')
 if req.get('event_type')=='revoke' and req.get('certificate_status_after')!='revoked': reasons.append('status mismatch')
 if req.get('event_type')=='tombstone' and req.get('certificate_status_after')!='tombstoned': reasons.append('status mismatch')
 if scan_payload_for_forbidden_terms(req) or scan_payload_for_contact_or_secret_terms(req): reasons.append('unsafe payload')
 if reasons: print(json.dumps({'recorded':False,'reasons':reasons},sort_keys=True)); return 1
 oid='cert-outcome-'+stable_payload_hash(req)[:16]; d=Path(a.outcome_root)/f'outcomes/soil/certificate_events/{rid}'
 out={'schema_version':'kfm.v1','object_type':'SoilCertificateEventOutcome','domain':'soil','outcome_id':oid,'remediation_id':rid,'registry_id':man.get('registry_id'),'release_id':man.get('release_id'),**{k:req.get(k) for k in ['execution_id','dispatch_id','event_type','event_status','certificate_status_after','certificate_event_receipt_ref','certificate_event_receipt_sha256','public_message']},'evidence_refs':req.get('evidence_refs',[]),'certificate_status_mutated_by_this_layer':False,'created':utc_now_iso()}
 op=d/f'{oid}.certificate_event_outcome.json'; write_json_atomic(op,out)
 rc={'schema_version':'kfm.v1','receipt_type':'CertificateEventOutcomeReceipt','domain':'soil','outcome_id':oid,'remediation_id':rid,'decision':'pass','certificate_event_outcome_hash':'sha256:'+sha256_file(op),'signatures':{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'},'created':utc_now_iso()}
 rp=d/f'{oid}.certificate_event_outcome_receipt.json'; write_json_atomic(rp,rc)
 print(json.dumps({'recorded':True,'outcome_id':oid},sort_keys=True)); return 0
if __name__=='__main__': raise SystemExit(main())
