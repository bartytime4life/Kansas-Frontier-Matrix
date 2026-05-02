#!/usr/bin/env python3
import argparse,json
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.recommissioning.soil._recommissioning_common import *
def main(argv=None):
 p=argparse.ArgumentParser(); [p.add_argument(a,required=True) for a in ['--resilience-root','--recommissioning-root','--verification']]; ns=p.parse_args(argv)
 req=load_json(ns.verification)
 if scan_payload_for_contact_or_secret_terms(req) or req.get('steward_review',{}).get('decision')!='approved': print(json.dumps({'ok':False})); return 1
 if req.get('active_public_delivery_ready') and not (req.get('evidence_refs') or req.get('monitor_receipt_refs')): print(json.dumps({'ok':False,'reasons':['missing monitor evidence']})); return 1
 rid=load_current_public_resilience(ns.resilience_root)['active_resilience_id']; vid=sanitize_id('sm-'+req.get('safe_mode_handoff_id','x'))
 rec={'schema_version':'kfm.v1','object_type':'SoilSafeModeExitVerification','domain':'soil','verification_id':vid,'resilience_id':rid,'safe_mode_handoff_id':req.get('safe_mode_handoff_id'),'verification_status':req.get('verification_status'),'active_public_delivery_ready':bool(req.get('active_public_delivery_ready')),'public_message':req.get('public_message',''),'evidence_refs':req.get('evidence_refs',[]),'monitor_receipt_refs':req.get('monitor_receipt_refs',[]),'created':utc_now_iso()}
 out=Path(ns.recommissioning_root)/f'recommissioning/soil/safe_mode_verifications/{rid}/{vid}.safe_mode_exit_verification.json'; write_json_atomic(out,rec); write_json_atomic(str(out).replace('.json','_receipt.json'),{'schema_version':'kfm.v1','receipt_type':'SoilSafeModeExitVerificationReceipt','verification_id':vid,'decision':'pass','signatures':{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'}})
 print(json.dumps({'ok':True,'verification_id':vid})); return 0
if __name__=='__main__': raise SystemExit(main())