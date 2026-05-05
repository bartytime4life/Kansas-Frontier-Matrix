#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
from tools.assurance.soil._assurance_common import *
from tools.validators.soil.trust_registry_check import main as trust_registry_check

def main(argv=None):
 a=argparse.ArgumentParser(); a.add_argument('--registry-root',required=True); a.add_argument('--assurance-root',required=True); a.add_argument('--registry-id'); a.add_argument('--exception',required=True); x=a.parse_args(argv)
 req=load_json(x.exception); rid=x.registry_id or load_current_registry(x.registry_root)['active_registry_id']
 reasons=[]
 if trust_registry_check(['--registry-root',x.registry_root,'--registry-id',rid])!=0: reasons.append('registry check failed')
 if req.get('steward_review',{}).get('required') and req.get('steward_review',{}).get('decision')!='approved': reasons.append('missing steward approval')
 if req.get('exception_type') not in {'quality','rights','provenance','operations','archive_fixity','registry','security','administrative'}: reasons.append('unknown exception_type')
 if req.get('severity') not in {'low','medium','high','critical'}: reasons.append('unknown severity')
 if req.get('status') not in {'open','accepted_non_blocking','resolved'}: reasons.append('unknown status')
 if not req.get('public_message'): reasons.append('missing public_message')
 if scan_payload_for_forbidden_terms(req): reasons.append('forbidden terms')
 if has_private_path(json.dumps(req)): reasons.append('private path')
 if req.get('blocking') is False and req.get('severity')=='critical': reasons.append('critical cannot be non-blocking')
 if req.get('blocking') is False and req.get('severity')=='high' and req.get('exception_type') in {'security','rights'}: reasons.append('high security/rights cannot be non-blocking')
 if reasons: print(json.dumps({'exception_recorded':False,'registry_id':rid,'reasons':reasons},sort_keys=True)); return 1
 m=load_registry_manifest(x.registry_root,rid); exid=sanitize_id(stable_payload_hash(req)[:16])
 notice={'schema_version':'kfm.v1','object_type':'SoilAssuranceExceptionNotice','domain':'soil','exception_id':exid,'registry_id':rid,'certification_id':m.get('certification_id'),'release_id':m.get('release_id'),'exception_type':req['exception_type'],'severity':req['severity'],'status':req['status'],'blocking':bool(req.get('blocking')),'public_message':req['public_message'],'evidence_refs':req.get('evidence_refs',[]),'created':utc_now_iso()}
 out=Path(x.assurance_root)/f'assurance/soil/exceptions/{rid}'
 write_json_atomic(out/f'{exid}.exception_notice.json',notice)
 rr=load_registry_receipt(x.registry_root,rid)
 receipt={'schema_version':'kfm.v1','receipt_type':'AssuranceExceptionReceipt','domain':'soil','exception_id':exid,'registry_id':rid,'decision':'blocking' if notice['blocking'] else ('resolved' if notice['status']=='resolved' else 'accepted_non_blocking'),'source_registry_receipt_hash':'sha256:'+stable_payload_hash(rr),'exception_notice_hash':'sha256:'+sha256_file(out/f'{exid}.exception_notice.json'),'policy_checks':{'registry_checked':True,'steward_review_checked':True,'blocking_classification_checked':True,'public_paths_checked':True,'forbidden_terms_checked':True},'signatures':{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'},'created':utc_now_iso()}
 write_json_atomic(out/f'{exid}.exception_receipt.json',receipt)
 print(json.dumps({'exception_recorded':True,'registry_id':rid,'exception_id':exid},sort_keys=True)); return 0
if __name__=='__main__': raise SystemExit(main())
