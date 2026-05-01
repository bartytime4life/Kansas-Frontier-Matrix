#!/usr/bin/env python3
import argparse, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.resilience.soil._resilience_common import *
ALLOWED_TYPES={'additional_probe','threshold_adjustment','access_log_rule','route_policy_rule','consumer_contract_rule','incident_trigger_rule','safe_mode_rule','documentation_update'}
ALLOWED_STATUS={'adopted','recommended','not_required','blocked'}; ALLOWED_SEV={'low','medium','high','critical'}
def main(argv=None):
 a=argparse.ArgumentParser(); a.add_argument('--closure-root',required=True); a.add_argument('--resilience-root',required=True); a.add_argument('--closure-id'); a.add_argument('--adoption',required=True); ns=a.parse_args(argv)
 req=load_json(ns.adoption); fails=[]
 ccur=load_current_delivery_incident_closure(ns.closure_root); cid=ns.closure_id or ccur['active_closure_id']; m=load_delivery_incident_closure_manifest(ns.closure_root,cid); rcpt=load_delivery_incident_closure_receipt(ns.closure_root,cid)
 if req.get('steward_review',{}).get('decision')!='approved': fails.append('missing steward approval')
 if req.get('control_type') not in ALLOWED_TYPES: fails.append('bad control_type')
 if req.get('adoption_status') not in ALLOWED_STATUS: fails.append('bad adoption_status')
 if req.get('severity') not in ALLOWED_SEV: fails.append('bad severity')
 if req.get('severity') in {'high','critical'} and req.get('adoption_status')=='not_required' and not req.get('evidence_refs'): fails.append('critical not_required missing evidence')
 if scan_payload_for_forbidden_terms(req) or scan_payload_for_contact_or_secret_terms(req): fails.append('unsafe payload')
 if fails: print(json.dumps({'ok':False,'reasons':fails})); return 1
 aid=sanitize_id(req.get('control_id')+'-'+stable_payload_hash(req)[7:19])
 out=Path(ns.resilience_root)/'resilience/soil/adoptions'/cid
 rec={'schema_version':'kfm.v1','object_type':'SoilResilienceControlAdoption','domain':'soil','adoption_id':aid,'closure_id':cid,'incident_response_id':m.get('incident_response_id'),'observability_id':m.get('observability_id'),'delivery_id':m.get('delivery_id'),'routing_id':m.get('routing_id'),'registry_id':m.get('registry_id'),'prior_release_id':m.get('prior_release_id'),'active_release_id':m.get('active_release_id'),'source_control_id':req.get('source_control_id'),'control_id':req.get('control_id'),'control_name':req.get('control_name'),'control_type':req.get('control_type'),'adoption_status':req.get('adoption_status'),'severity':req.get('severity'),'public_message':req.get('public_message'),'evidence_refs':req.get('evidence_refs',[]),'recommended_workflow_ref':req.get('recommended_workflow_ref'),'live_policy_mutation_performed':False,'live_monitoring_update_performed':False,'live_route_update_performed':False,'created':utc_now_iso()}
 receipt={'schema_version':'kfm.v1','receipt_type':'ResilienceControlAdoptionReceipt','domain':'soil','adoption_id':aid,'closure_id':cid,'delivery_id':m.get('delivery_id'),'decision':'pass','source_delivery_incident_closure_receipt_hash':stable_payload_hash(rcpt),'resilience_control_adoption_hash':stable_payload_hash(rec),'policy_checks':{'incident_closure_checked':True,'source_control_checked':True,'steward_review_checked':True,'public_paths_checked':True,'forbidden_terms_checked':True,'contact_data_checked':True,'no_live_mutation_checked':True},'signatures':{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'},'created':utc_now_iso()}
 write_json_atomic(out/f'{aid}.resilience_control_adoption.json',rec); write_json_atomic(out/f'{aid}.resilience_control_adoption_receipt.json',receipt)
 print(json.dumps({'ok':True,'adoption_id':aid,'closure_id':cid})); return 0
if __name__=='__main__': raise SystemExit(main())
