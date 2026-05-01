#!/usr/bin/env python3
import argparse, json
from pathlib import Path
from tools.incident_closure.soil._incident_closure_common import *
ALLOWED={'not_required','allow_active_delivery','remain_governance_only','disable_until_new_delivery_verification','require_reprobe'}
def main(argv=None):
 a=argparse.ArgumentParser(); a.add_argument('--incident-root',required=True); a.add_argument('--closure-root',required=True); a.add_argument('--approval',required=True); ns=a.parse_args(argv)
 req=load_json(ns.approval); irid=req.get('incident_response_id') or load_current_delivery_incident_response(ns.incident_root)['active_incident_response_id']
 decl=load_delivery_incident_declaration_registry(ns.incident_root,irid).get('incidents',[])
 fails=[]
 if req.get('exit_type') not in ALLOWED: fails.append('unknown exit_type')
 if req.get('exit_type')=='allow_active_delivery' and not req.get('recovery_verification_ids'): fails.append('missing recovery evidence')
 if any(i.get('severity') in {'high','critical'} and i.get('root_cause_category') in {'security','rights','privacy','access_log_safety'} and i.get('status')!='resolved' for i in decl) and req.get('exit_type')=='allow_active_delivery': fails.append('unresolved blocking incident')
 sr=req.get('steward_review',{})
 if not(sr.get('required') is True and sr.get('decision')=='approved'): fails.append('missing steward approval')
 if scan_payload_for_forbidden_terms(req) or scan_payload_for_contact_or_secret_terms(req): fails.append('unsafe terms')
 if fails: print(json.dumps({'recorded':False,'incident_response_id':irid,'reasons':fails})); return 1
 aid=sanitize_id(req.get('approval_id') or ('safe-mode-'+stable_payload_hash(req).split(':')[1][:16]))
 out=Path(ns.closure_root)/'incident_closure/soil/safe_mode'/irid
 app={**req,'schema_version':'kfm.v1','object_type':'SoilSafeModeExitApproval','domain':'soil','incident_response_id':irid,'approval_id':aid,'created':utc_now_iso()}
 rec={'schema_version':'kfm.v1','receipt_type':'SoilSafeModeExitApprovalReceipt','domain':'soil','incident_response_id':irid,'approval_id':aid,'approval_ref':str((out/f'{aid}.safe_mode_exit_approval.json')),'approval_sha256':stable_payload_hash(app),'signatures':[{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'}]}
 write_json_atomic(out/f'{aid}.safe_mode_exit_approval.json',app); write_json_atomic(out/f'{aid}.safe_mode_exit_approval_receipt.json',rec)
 print(json.dumps({'recorded':True,'approval_id':aid,'incident_response_id':irid})); return 0
if __name__=='__main__': raise SystemExit(main())
