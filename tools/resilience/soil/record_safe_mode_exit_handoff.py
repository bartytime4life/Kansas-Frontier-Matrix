#!/usr/bin/env python3
import argparse, json
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.resilience.soil._resilience_common import *
TYPES={'not_required','allow_active_delivery_after_rebuild','remain_governance_only','require_delivery_reprobe','require_routing_rebuild','blocked'}
def main(argv=None):
 ap=argparse.ArgumentParser(); ap.add_argument('--closure-root',required=True); ap.add_argument('--resilience-root',required=True); ap.add_argument('--handoff',required=True); ap.add_argument('--closure-id'); ns=ap.parse_args(argv)
 req=load_json(ns.handoff); ccur=load_current_delivery_incident_closure(ns.closure_root); cid=ns.closure_id or req.get('closure_id') or ccur['active_closure_id']; m=load_delivery_incident_closure_manifest(ns.closure_root,cid); rv=load_recovery_closure_verification_registry(ns.closure_root,cid); fails=[]
 if req.get('steward_review',{}).get('decision')!='approved': fails.append('missing steward approval')
 if req.get('exit_handoff_type') not in TYPES: fails.append('bad type')
 if req.get('active_public_delivery_recommended_after_handoff') and not m.get('active_public_delivery_allowed_after_closure',False): fails.append('active disallowed by closure')
 if req.get('exit_handoff_type')=='allow_active_delivery_after_rebuild' and not rv.get('recovery_verified'): fails.append('missing recovery evidence')
 if scan_payload_for_forbidden_terms(req) or scan_payload_for_contact_or_secret_terms(req): fails.append('unsafe payload')
 if fails: print(json.dumps({'ok':False,'reasons':fails})); return 1
 hid=sanitize_id(req.get('exit_handoff_type')+'-'+stable_payload_hash(req)[7:19]); out=Path(ns.resilience_root)/'resilience/soil/safe_mode'/cid
 rec={'schema_version':'kfm.v1','object_type':'SoilSafeModeExitHandoff','domain':'soil','handoff_id':hid,'closure_id':cid,'incident_response_id':m.get('incident_response_id'),'delivery_id':m.get('delivery_id'),'routing_id':m.get('routing_id'),'exit_handoff_type':req.get('exit_handoff_type'),'public_message':req.get('public_message'),'evidence_refs':req.get('evidence_refs',[]),'required_future_workflow_refs':req.get('required_future_workflow_refs',[]),'active_public_delivery_recommended_after_handoff':bool(req.get('active_public_delivery_recommended_after_handoff')),'live_route_update_performed':False,'created':utc_now_iso()}
 receipt={'schema_version':'kfm.v1','receipt_type':'SafeModeExitHandoffReceipt','domain':'soil','handoff_id':hid,'closure_id':cid,'decision':'pass','safe_mode_exit_handoff_hash':stable_payload_hash(rec),'signatures':{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'},'created':utc_now_iso()}
 write_json_atomic(out/f'{hid}.safe_mode_exit_handoff.json',rec); write_json_atomic(out/f'{hid}.safe_mode_exit_handoff_receipt.json',receipt)
 print(json.dumps({'ok':True,'handoff_id':hid,'closure_id':cid})); return 0
if __name__=='__main__': raise SystemExit(main())
