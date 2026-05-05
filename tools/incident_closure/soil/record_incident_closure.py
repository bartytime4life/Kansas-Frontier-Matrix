#!/usr/bin/env python3
import argparse, json
from pathlib import Path
from tools.incident_closure.soil._incident_closure_common import *
ALLOWED_CT={'no_active_incident','resolved','recovered','mitigated_governance_only','blocked_unresolved','duplicate','not_required'}
ALLOWED_RC={'none','availability','routing','delivery','data_contract','response_drift','access_log_safety','security','rights','privacy','quality','configuration','unknown'}
ALLOWED_SEV={'low','medium','high','critical'}
def main(argv=None):
 a=argparse.ArgumentParser(); a.add_argument('--incident-root',required=True); a.add_argument('--closure-root',required=True); a.add_argument('--closure',required=True); a.add_argument('--incident-response-id'); ns=a.parse_args(argv)
 req=load_json(ns.closure); irid=ns.incident_response_id or load_current_delivery_incident_response(ns.incident_root)['active_incident_response_id']
 decl=load_delivery_incident_declaration_registry(ns.incident_root,irid).get('incidents',[])
 fails=[]
 if req.get('closure_type') not in ALLOWED_CT: fails.append('unknown closure_type')
 if req.get('root_cause_category') not in ALLOWED_RC: fails.append('unknown root_cause_category')
 if req.get('severity') not in ALLOWED_SEV: fails.append('unknown severity')
 if not req.get('public_message'): fails.append('missing public_message')
 sr=req.get('steward_review',{})
 if not(sr.get('required') is True and sr.get('decision')=='approved'): fails.append('missing steward approval')
 if scan_payload_for_forbidden_terms(req) or scan_payload_for_contact_or_secret_terms(req): fails.append('unsafe terms')
 if req.get('closure_type')=='no_active_incident' and decl: fails.append('declarations exist')
 if req.get('closure_type') in {'resolved','recovered'} and req.get('severity') in {'high','critical'} and not req.get('evidence_refs'): fails.append('missing evidence_refs')
 if req.get('closure_type')=='recovered' and not req.get('recovery_verification_id'): fails.append('missing recovery_verification_id')
 if fails: print(json.dumps({'recorded':False,'incident_response_id':irid,'reasons':fails})); return 1
 cid=sanitize_id(req.get('closure_id') or ('closure-'+stable_payload_hash(req).split(':')[1][:16]))
 out=Path(ns.closure_root)/'incident_closure/soil/closures'/irid
 dec={**req,'schema_version':'kfm.v1','object_type':'SoilDeliveryIncidentClosureDecision','domain':'soil','incident_response_id':irid,'closure_id':cid,'created':utc_now_iso()}
 rec={'schema_version':'kfm.v1','receipt_type':'DeliveryIncidentClosureDecisionReceipt','domain':'soil','incident_response_id':irid,'closure_id':cid,'created':utc_now_iso(),'decision_ref':str((out/f'{cid}.incident_closure_decision.json')),'decision_sha256':stable_payload_hash(dec),'signatures':[{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'}]}
 write_json_atomic(out/f'{cid}.incident_closure_decision.json',dec); write_json_atomic(out/f'{cid}.incident_closure_decision_receipt.json',rec)
 print(json.dumps({'recorded':True,'incident_response_id':irid,'closure_id':cid})); return 0
if __name__=='__main__': raise SystemExit(main())
