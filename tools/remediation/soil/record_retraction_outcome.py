#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.remediation.soil._outcome_common import *

def main(argv=None):
 ap=argparse.ArgumentParser(); ap.add_argument('--remediation-root',required=True); ap.add_argument('--published-root',required=True); ap.add_argument('--archive-root',required=True); ap.add_argument('--registry-root',required=True); ap.add_argument('--outcome-root',required=True); ap.add_argument('--outcome',required=True); ap.add_argument('--remediation-id'); a=ap.parse_args(argv)
 req=load_json(a.outcome); rid=a.remediation_id or load_current_remediation_handoff(a.remediation_root)['active_remediation_id']; b=load_retraction_review_intake_bundle(a.remediation_root,rid); man=load_remediation_handoff_manifest(a.remediation_root,rid)
 i=next((x for x in b.get('intakes',[]) if x.get('intake_id')==req.get('intake_id')),None); reasons=[]
 if req.get('steward_review',{}).get('decision')!='approved': reasons.append('missing steward')
 if not i or i.get('work_order_id')!=req.get('work_order_id'): reasons.append('missing intake/work order')
 if req.get('outcome_status') in {'retracted','tombstoned','withdrawal_reconciled'} and not req.get('retraction_receipt_ref'): reasons.append('missing retraction receipt')
 if req.get('outcome_status')=='tombstoned' and not req.get('archive_tombstone_receipt_ref'): reasons.append('missing tombstone receipt')
 if scan_payload_for_contact_or_secret_terms(req) or scan_payload_for_forbidden_terms(req): reasons.append('unsafe payload')
 if reasons: print(json.dumps({'recorded':False,'reasons':reasons},sort_keys=True)); return 1
 oid='retraction-outcome-'+stable_payload_hash(req)[:16]; d=Path(a.outcome_root)/f'outcomes/soil/retractions/{rid}'
 out={'schema_version':'kfm.v1','object_type':'SoilRetractionOutcome','domain':'soil','outcome_id':oid,'remediation_id':rid,'release_id':man.get('release_id'),**req,'retraction_performed_by_this_layer':False,'created':utc_now_iso()}
 op=d/f'{oid}.retraction_outcome.json'; write_json_atomic(op,out); rp=d/f'{oid}.retraction_outcome_receipt.json'; write_json_atomic(rp,{'schema_version':'kfm.v1','receipt_type':'RetractionOutcomeReceipt','domain':'soil','outcome_id':oid,'remediation_id':rid,'decision':'pass','hash':'sha256:'+sha256_file(op),'signatures':{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'},'created':utc_now_iso()})
 print(json.dumps({'recorded':True,'outcome_id':oid},sort_keys=True)); return 0
if __name__=='__main__': raise SystemExit(main())
