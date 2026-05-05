#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
from tools.assurance.soil._assurance_common import *
from tools.validators.soil.assurance_check import main as assurance_check

def main(argv=None):
 a=argparse.ArgumentParser(); a.add_argument('--assurance-root',required=True); a.add_argument('--registry-root',required=True); a.add_argument('--assurance-id'); a.add_argument('--reaffirmation-id'); a.add_argument('--out-root',required=True); x=a.parse_args(argv)
 if assurance_check(['--assurance-root',x.assurance_root]+(['--assurance-id',x.assurance_id] if x.assurance_id else []))!=0: print(json.dumps({'reaffirmation_allowed':False,'reasons':['assurance_check failed']})); return 1
 aid=x.assurance_id or load_json(Path(x.assurance_root)/'assurance/soil/current_assurance.json')['active_assurance_id']
 d=Path(x.assurance_root)/f'assurance/soil/cycles/{aid}'
 cls=load_json(d/'certificate_lifecycle_status.json'); dr=load_json(d/'drift_report.json'); rr=load_json(d/'renewal_recommendation.json')
 if cls.get('certificate_status')!='active' or dr.get('drift_detected') or rr.get('safe_to_reaffirm') is not True or rr.get('recommendation') in {'suspend','revoke','tombstone'}:
  print(json.dumps({'reaffirmation_allowed':False,'reasons':['unsafe']})); return 1
 rid=sanitize_id(x.reaffirmation_id or f"soil-reaffirmation-{stable_payload_hash({'aid':aid})[:16]}")
 out=Path(x.out_root)/f'assurance/soil/reaffirmations/{rid}'
 notice={'schema_version':'kfm.v1','object_type':'SoilTrustRegistryReaffirmationNotice','domain':'soil','reaffirmation_id':rid,'assurance_id':aid,'registry_id':cls['registry_id'],'release_id':cls['release_id'],'status':'REAFFIRMED','certificate_status':'active','public_advertising_allowed':True,'created':utc_now_iso()}
 write_json_atomic(out/'reaffirmation_notice.json',notice)
 receipt={'schema_version':'kfm.v1','receipt_type':'TrustRegistryReaffirmationReceipt','from_state':'CONTINUOUS_ASSURANCE_READY','to_state':'TRUST_REGISTRY_REAFFIRMED','decision':'pass','domain':'soil','reaffirmation_id':rid,'assurance_id':aid,'registry_id':cls['registry_id'],'release_id':cls['release_id'],'source_assurance_receipt_hash':'sha256:'+sha256_file(d/'assurance_receipt.json'),'generated_artifacts':{'reaffirmation_notice.json':'sha256:'+sha256_file(out/'reaffirmation_notice.json')},'policy_checks':{'assurance_checked':True,'certificate_active':True,'drift_checked':True,'blocking_exceptions_checked':True,'public_paths_checked':True,'forbidden_terms_checked':True},'signatures':{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'},'created':utc_now_iso()}
 write_json_atomic(out/'reaffirmation_receipt.json',receipt)
 print(json.dumps({'reaffirmation_allowed':True,'reaffirmation_id':rid,'assurance_id':aid},sort_keys=True)); return 0
if __name__=='__main__': raise SystemExit(main())
