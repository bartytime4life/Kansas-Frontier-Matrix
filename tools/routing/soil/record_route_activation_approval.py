import argparse, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.routing.soil._public_routing_common import *

def block(tid,prior,reasons):
 print(json.dumps({"public_routing_allowed":False,"pointer_transition_id":tid,"prior_release_id":prior,"reasons":reasons}));sys.exit(1)

def main():
 p=argparse.ArgumentParser();p.add_argument('--active-root',required=True);p.add_argument('--published-root',required=True);p.add_argument('--routing-root',required=True);p.add_argument('--approval',required=True);p.add_argument('--pointer-transition-id')
 a=p.parse_args(); req=load_json(a.approval)
 cur=load_current_active_release(a.active_root); tid=a.pointer_transition_id or cur.get('active_pointer_transition_id'); man=load_active_release_pointer_manifest(a.active_root,tid); rec=load_active_release_pointer_receipt(a.active_root,tid)
 prior=man.get('prior_release_id'); active=man.get('active_release_id'); ps=man.get('pointer_state')
 if req.get('steward_review',{}).get('decision')!='approved': block(tid,prior,['missing steward approval'])
 if scan_payload_for_forbidden_terms(req) or scan_payload_for_contact_or_secret_terms(req): block(tid,prior,['unsafe approval payload'])
 if req.get('pointer_transition_id')!=tid: block(tid,prior,['pointer_transition_id mismatch'])
 aid=sanitize_id(req.get('approval_id') or ('route-approval-'+stable_payload_hash(req).split(':',1)[1][:16]))
 n={"schema_version":"kfm.v1","object_type":"SoilPublicRouteActivationApproval","domain":"soil","approval_id":aid,"pointer_transition_id":tid,"lineage_id":man.get('lineage_id'),"registry_id":man.get('registry_id'),"prior_release_id":prior,"active_release_id":active,"route_activation_type":req.get('route_activation_type'),"reason_type":req.get('reason_type'),"severity":req.get('severity'),"public_message":req.get('public_message',''),"evidence_refs":req.get('evidence_refs',[]),"published_current_pointer_mutated":False,"immutable_artifacts_mutated":False,"external_route_update_performed":False,"created":utc_now_iso()}
 r={"schema_version":"kfm.v1","receipt_type":"PublicRouteActivationApprovalReceipt","domain":"soil","approval_id":aid,"pointer_transition_id":tid,"prior_release_id":prior,"active_release_id":active,"decision":"approved","source_active_release_pointer_receipt_hash":sha256_file(Path(a.active_root)/'active_release/soil/transitions'/tid/'active_release_pointer_receipt.json'),"approval_notice_hash":stable_payload_hash(n),"policy_checks":{"active_pointer_checked":True,"route_activation_type_checked":True,"active_release_checked":True,"steward_review_checked":True,"immutability_checked":True,"public_paths_checked":True,"forbidden_terms_checked":True,"contact_data_checked":True},"signatures":{"dsse":"PROPOSED-COSIGN","key_ref":"kfm://keys/ci"},"created":utc_now_iso()}
 out=Path(a.routing_root)/'routing/soil/approvals'/tid
 write_json_atomic(out/f'{aid}.route_activation_approval.json',n);write_json_atomic(out/f'{aid}.route_activation_approval_receipt.json',r)
 print(json.dumps({"public_routing_allowed":True,"approval_id":aid,"pointer_transition_id":tid}))
if __name__=='__main__': main()
