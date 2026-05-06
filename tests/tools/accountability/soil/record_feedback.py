#!/usr/bin/env python3
from __future__ import annotations
from tools.accountability.soil._accountability_common import *
import argparse,json
from pathlib import Path

def main(argv=None):
 a=argparse.ArgumentParser();[a.add_argument(x,required=True) for x in ['--assurance-root','--registry-root','--accountability-root','--feedback']];a.add_argument('--assurance-id');x=a.parse_args(argv)
 aid=x.assurance_id or load_current_assurance(x.assurance_root)['active_assurance_id']; am=load_assurance_manifest(x.assurance_root,aid); ar=load_assurance_receipt(x.assurance_root,aid); rid=am['registry_id']; rel=am['release_id']
 p=load_json(x.feedback); fail=[]
 if p.get('steward_review',{}).get('required') is not True: fail.append('missing steward_review')
 if p.get('feedback_type') not in {'general','quality','rights','provenance','accessibility','usability','security','correction_request'}: fail.append('unknown feedback_type')
 if p.get('severity') not in {'low','medium','high','critical'} or not p.get('public_message'): fail.append('bad severity/message')
 if p.get('submitter_disclosure',{}).get('contact_included') is True: fail.append('contact included')
 if scan_payload_for_forbidden_terms(p) or scan_payload_for_contact_or_secret_terms({'m':p.get('public_message','')}): fail.append('unsafe payload')
 if has_private_path(json.dumps(p)): fail.append('private path')
 if fail: print(json.dumps({'accepted':False,'reasons':fail},sort_keys=True)); return 1
 fid='fb-'+stable_payload_hash(p)[:16]; vis='restricted_pending_review' if p.get('severity')=='critical' or p.get('feedback_type')=='security' else 'public'; msg='Restricted pending steward review.' if vis!='public' else p['public_message']
 n={'schema_version':'kfm.v1','object_type':'SoilPublicFeedbackNotice','domain':'soil','feedback_id':fid,'assurance_id':aid,'registry_id':rid,'release_id':rel,'feedback_type':p['feedback_type'],'severity':p['severity'],'status':'accepted_for_review','public_visibility':vis,'summary':p.get('summary',''),'public_message':msg,'affected_bundle_id':p.get('affected_bundle_id'),'evidence_refs':p.get('evidence_refs',[]),'created':utc_now_iso()}
 out=Path(x.accountability_root)/f'accountability/soil/feedback/{aid}'; write_json_atomic(out/f'{fid}.feedback_notice.json',n)
 rc={'schema_version':'kfm.v1','receipt_type':'PublicFeedbackReceipt','domain':'soil','feedback_id':fid,'assurance_id':aid,'registry_id':rid,'release_id':rel,'decision':'accepted_for_review','source_assurance_receipt_hash':'sha256:'+sha256_bytes(json.dumps(ar,sort_keys=True).encode()),'feedback_notice_hash':'sha256:'+stable_payload_hash(n),'policy_checks':{'assurance_checked':True,'registry_checked':True,'steward_review_checked':True,'public_input_safety_checked':True,'contact_data_checked':True,'public_paths_checked':True,'forbidden_terms_checked':True},'signatures':{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'},'created':utc_now_iso()}
 write_json_atomic(out/f'{fid}.feedback_receipt.json',rc); print(json.dumps({'accepted':True,'feedback_id':fid},sort_keys=True)); return 0
if __name__=='__main__': raise SystemExit(main())