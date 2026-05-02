#!/usr/bin/env python3
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.recommissioning.soil._recommissioning_common import *
def main(argv=None):
 p=argparse.ArgumentParser(); p.add_argument('--resilience-root',required=True); p.add_argument('--recommissioning-root',required=True); p.add_argument('--completion',required=True); p.add_argument('--resilience-id'); ns=p.parse_args(argv)
 req=load_json(ns.completion); bad=scan_payload_for_contact_or_secret_terms(req)
 if bad or req.get('steward_review',{}).get('decision')!='approved': print(json.dumps({'ok':False,'reasons':['invalid completion']})); return 1
 rid=ns.resilience_id or load_current_public_resilience(ns.resilience_root)['active_resilience_id']
 mid=sanitize_id('fup-'+req.get('work_order_id','none')+'-'+req.get('completion_type','x'))
 rec={'schema_version':'kfm.v1','object_type':'SoilResilienceFollowupCompletion','domain':'soil','completion_id':mid,'resilience_id':rid,'closure_id':None,'delivery_id':None,'routing_id':None,'work_order_id':req.get('work_order_id'),'completion_type':req.get('completion_type'),'completion_status':req.get('completion_status'),'public_message':req.get('public_message',''),'evidence_refs':req.get('evidence_refs',[]),'completion_receipt_ref':req.get('completion_receipt_ref'),'completion_receipt_sha256':req.get('completion_receipt_sha256'),'live_workflow_invoked_by_this_layer':False,'live_policy_mutation_performed':False,'live_route_update_performed':False,'created':utc_now_iso()}
 out=Path(ns.recommissioning_root)/f'recommissioning/soil/followup_completions/{rid}/{mid}.followup_completion.json'; write_json_atomic(out,rec)
 rcp={'schema_version':'kfm.v1','receipt_type':'SoilResilienceFollowupCompletionReceipt','completion_id':mid,'decision':'pass','signatures':{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'}}
 write_json_atomic(str(out).replace('.json','_receipt.json'),rcp); print(json.dumps({'ok':True,'completion_id':mid})); return 0
if __name__=='__main__': raise SystemExit(main())