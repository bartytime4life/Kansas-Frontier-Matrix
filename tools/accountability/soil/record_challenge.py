#!/usr/bin/env python3
from __future__ import annotations
from tools.accountability.soil._accountability_common import *
import argparse,json
from pathlib import Path

def main(argv=None):
 a=argparse.ArgumentParser();[a.add_argument(x,required=True) for x in ['--assurance-root','--registry-root','--accountability-root','--challenge']];a.add_argument('--assurance-id');x=a.parse_args(argv)
 aid=x.assurance_id or load_current_assurance(x.assurance_root)['active_assurance_id']; am=load_assurance_manifest(x.assurance_root,aid); p=load_json(x.challenge)
 fail=[]
 if p.get('challenge_type') not in {'reproducibility','metric_discrepancy','provenance_question','rights_question','accessibility_issue'}: fail.append('bad type')
 if p.get('severity') not in {'low','medium','high','critical'} or not p.get('claim') or not p.get('public_message'): fail.append('bad fields')
 if not p.get('steward_review'): fail.append('missing review')
 if scan_payload_for_forbidden_terms(p) or has_private_path(json.dumps(p)): fail.append('unsafe')
 if fail: print(json.dumps({'accepted':False,'reasons':fail},sort_keys=True)); return 1
 cid='ch-'+stable_payload_hash(p)[:16]; out=Path(x.accountability_root)/f'accountability/soil/challenges/{aid}'
 n={'schema_version':'kfm.v1','object_type':'SoilReproducibilityChallengeNotice','domain':'soil','challenge_id':cid,'assurance_id':aid,'registry_id':am['registry_id'],'release_id':am['release_id'],'challenge_type':p['challenge_type'],'severity':p['severity'],'status':'accepted_for_review','affected_bundle_id':p.get('affected_bundle_id'),'claim':p['claim'],'public_message':p['public_message'],'expected_result':p.get('expected_result'),'observed_result':p.get('observed_result'),'evidence_refs':p.get('evidence_refs',[]),'truth_policy':{'public_challenge_is_not_truth_source':True,'steward_review_required_for_correction':True,'evidence_bound_resolution_required':True},'created':utc_now_iso()}
 write_json_atomic(out/f'{cid}.challenge_notice.json',n); write_json_atomic(out/f'{cid}.challenge_receipt.json',{'schema_version':'kfm.v1','receipt_type':'ReproducibilityChallengeReceipt','challenge_id':cid,'challenge_notice_hash':'sha256:'+stable_payload_hash(n),'signatures':{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'},'created':utc_now_iso()}); print(json.dumps({'accepted':True,'challenge_id':cid},sort_keys=True)); return 0
if __name__=='__main__': raise SystemExit(main())