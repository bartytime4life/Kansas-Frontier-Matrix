#!/usr/bin/env python3
import argparse, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.recommissioning.soil._recommissioning_common import *

def main(argv=None):
 a=argparse.ArgumentParser();a.add_argument('--resilience-root',required=True);a.add_argument('--recommissioning-root',required=True);a.add_argument('--completion',required=True);a.add_argument('--resilience-id');x=a.parse_args(argv)
 req=load_json(x.completion); cur=load_current_public_resilience(x.resilience_root); rid=x.resilience_id or cur['active_resilience_id']
 if req.get('steward_review',{}).get('decision')!='approved': print(json.dumps({'ok':False,'reason':'missing steward approval'})); return 1
 if scan_payload_for_forbidden_terms(req) or scan_payload_for_contact_or_secret_terms(req): print(json.dumps({'ok':False,'reason':'unsafe payload'})); return 1
 cid=sanitize_id(req.get('work_order_id') or stable_payload_hash(req).split(':')[1][:12])
 rec={"schema_version":"kfm.v1","object_type":"SoilResilienceFollowupCompletion","domain":"soil","completion_id":cid,"resilience_id":rid,"work_order_id":req.get('work_order_id'),"completion_type":req.get('completion_type'),"completion_status":req.get('completion_status'),"public_message":req.get('public_message',''),"evidence_refs":req.get('evidence_refs',[]),"completion_receipt_ref":req.get('completion_receipt_ref'),"completion_receipt_sha256":req.get('completion_receipt_sha256'),"live_workflow_invoked_by_this_layer":False,"live_policy_mutation_performed":False,"live_route_update_performed":False,"created":utc_now_iso()}
 out=Path(x.recommissioning_root)/f'recommissioning/soil/followup_completions/{rid}/{cid}.followup_completion.json';write_json_atomic(out,rec)
 rcp=Path(x.recommissioning_root)/f'recommissioning/soil/followup_completions/{rid}/{cid}.followup_completion_receipt.json';write_json_atomic(rcp,{"schema_version":"kfm.v1","receipt_type":"SoilResilienceFollowupCompletionReceipt","completion_id":cid,"decision":"pass","signatures":[{"dsse":"PROPOSED-COSIGN","key_ref":"kfm://keys/ci"}],"created":utc_now_iso()})
 print(json.dumps({'ok':True,'completion_id':cid,'resilience_id':rid,'record_ref':str(out)})); return 0
if __name__=='__main__': raise SystemExit(main())
