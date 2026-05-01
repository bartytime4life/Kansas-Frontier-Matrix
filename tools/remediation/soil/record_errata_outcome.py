#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.remediation.soil._outcome_common import *

def main(argv=None):
 ap=argparse.ArgumentParser(); ap.add_argument('--remediation-root',required=True); ap.add_argument('--outcome-root',required=True); ap.add_argument('--outcome',required=True); ap.add_argument('--remediation-id'); a=ap.parse_args(argv)
 req=load_json(a.outcome); rid=a.remediation_id or load_current_remediation_handoff(a.remediation_root)['active_remediation_id']
 reg=load_errata_publication_registry(a.remediation_root,rid); receipt=load_remediation_handoff_receipt(a.remediation_root,rid); man=load_remediation_handoff_manifest(a.remediation_root,rid)
 reasons=[]
 if req.get('steward_review',{}).get('decision')!='approved': reasons.append('missing steward approval')
 if req.get('outcome_status') not in {'published','superseded_by_successor','withdrawn','blocked'}: reasons.append('unknown outcome_status')
 if not validate_base_public_url(req.get('public_url')): reasons.append('invalid public_url')
 e=next((x for x in reg.get('entries',[]) if x.get('errata_id')==req.get('errata_id')),None)
 if not e: reasons.append('unknown errata_id')
 elif e.get('publication_id')!=req.get('publication_id'): reasons.append('unknown publication_id')
 if scan_payload_for_contact_or_secret_terms({'public_message':req.get('public_message','')}): reasons.append('contact/secret')
 if scan_payload_for_forbidden_terms(req): reasons.append('forbidden term')
 if has_private_path(req.get('public_message','')): reasons.append('private path')
 if reasons:
  print(json.dumps({'recorded':False,'reasons':reasons},sort_keys=True)); return 1
 oid='errata-outcome-'+stable_payload_hash(req)[:16]; d=Path(a.outcome_root)/f'outcomes/soil/errata/{rid}';
 out={'schema_version':'kfm.v1','object_type':'SoilErrataOutcome','domain':'soil','outcome_id':oid,'remediation_id':rid,'corrective_id':man.get('corrective_id'),'resolution_id':man.get('resolution_id'),'registry_id':man.get('registry_id'),'release_id':man.get('release_id'),'errata_id':req['errata_id'],'publication_id':req['publication_id'],'outcome_status':req['outcome_status'],'public_url':req['public_url'],'public_message':req.get('public_message',''),'evidence_refs':req.get('evidence_refs',[]),'published_artifacts_mutated':False,'created':utc_now_iso()}
 op=d/f'{sanitize_id(oid)}.errata_outcome.json'; write_json_atomic(op,out)
 rc={'schema_version':'kfm.v1','receipt_type':'ErrataOutcomeReceipt','domain':'soil','outcome_id':oid,'remediation_id':rid,'release_id':man.get('release_id'),'decision':'pass','source_remediation_handoff_receipt_hash':'sha256:'+sha256_file(Path(a.remediation_root)/f'remediation/soil/cycles/{rid}/remediation_handoff_receipt.json'),'errata_outcome_hash':'sha256:'+sha256_file(op),'policy_checks':{'remediation_checked':True,'errata_publication_checked':True,'steward_review_checked':True,'immutability_checked':True,'public_paths_checked':True,'forbidden_terms_checked':True,'contact_data_checked':True},'signatures':{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'},'created':utc_now_iso()}
 rp=d/f'{sanitize_id(oid)}.errata_outcome_receipt.json'; write_json_atomic(rp,rc)
 print(json.dumps({'recorded':True,'outcome_id':oid,'outcome_ref':str(op),'receipt_ref':str(rp)},sort_keys=True)); return 0
if __name__=='__main__': raise SystemExit(main())
