#!/usr/bin/env python3
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.recommissioning.soil._recommissioning_common import *

def main(argv=None):
 p=argparse.ArgumentParser(); [p.add_argument(a,required=True) for a in ['--resilience-root','--recommissioning-root','--verification']]; p.add_argument('--resilience-id'); a=p.parse_args(argv)
 req=load_json(a.verification); rid=a.resilience_id or load_current_public_resilience(a.resilience_root)['active_resilience_id']
 if req.get('steward_review',{}).get('decision')!='approved': print(json.dumps({'ok':False})); return 1
 if req.get('active_public_delivery_ready') and not req.get('monitor_receipt_refs') and not req.get('evidence_refs'): print(json.dumps({'ok':False,'reason':'missing monitor evidence'})); return 1
 if scan_payload_for_forbidden_terms(req) or scan_payload_for_contact_or_secret_terms(req): print(json.dumps({'ok':False,'reason':'unsafe'})); return 1
 vid=sanitize_id(stable_payload_hash(req).split(':')[1][:12])
 rec={'schema_version':'kfm.v1','object_type':'SoilSafeModeExitVerification','domain':'soil','verification_id':vid,'resilience_id':rid,'safe_mode_handoff_id':req.get('safe_mode_handoff_id'),'verification_status':req.get('verification_status'),'active_public_delivery_ready':bool(req.get('active_public_delivery_ready')),'public_message':req.get('public_message',''),'evidence_refs':req.get('evidence_refs',[]),'monitor_receipt_refs':req.get('monitor_receipt_refs',[]),'created':utc_now_iso()}
 out=Path(a.recommissioning_root)/f'recommissioning/soil/safe_mode_verifications/{rid}/{vid}.safe_mode_exit_verification.json'; write_json_atomic(out,rec)
 write_json_atomic(out.with_name(f'{vid}.safe_mode_exit_verification_receipt.json'),{'schema_version':'kfm.v1','receipt_type':'SoilSafeModeExitVerificationReceipt','verification_id':vid,'decision':'pass','signatures':[{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'}],'created':utc_now_iso()})
 print(json.dumps({'ok':True,'verification_id':vid})); return 0
if __name__=='__main__': raise SystemExit(main())
