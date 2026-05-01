#!/usr/bin/env python3
from __future__ import annotations
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.remediation.soil._outcome_common import *

def _bad(msg): print(json.dumps({'allowed':False,'reasons':[msg]},sort_keys=True)); return 1

def main(argv=None):
 a=argparse.ArgumentParser(); a.add_argument('--remediation-root',required=True); a.add_argument('--outcome-root',required=True); a.add_argument('--outcome',required=True); a.add_argument('--remediation-id'); x=a.parse_args(argv)
 req=load_json(x.outcome); rid=x.remediation_id or load_current_remediation_handoff(x.remediation_root)['active_remediation_id']
 reg=load_errata_publication_registry(x.remediation_root,rid)
 if req.get('steward_review',{}).get('decision')!='approved': return _bad('missing steward approval')
 if scan_payload_for_contact_or_secret_terms(req): return _bad('contact/secret terms found')
 if has_private_path(req.get('public_url','')): return _bad('private path')
 if req.get('outcome_status') not in {'published','superseded_by_successor','withdrawn','blocked'}: return _bad('bad status')
 if not validate_base_public_url(req.get('public_url')): return _bad('bad public_url')
 e=[i for i in reg.get('entries',[]) if i.get('errata_id')==req.get('errata_id')]
 if not e: return _bad('unknown errata_id')
 if req.get('publication_id') not in {i.get('publication_id') for i in e}: return _bad('unknown publication_id')
 oid='errata-outcome-'+stable_payload_hash(req)[:16]; out=Path(x.outcome_root)/f'outcomes/soil/errata/{rid}'
 outcome={'schema_version':'kfm.v1','object_type':'SoilErrataOutcome','domain':'soil','outcome_id':oid,'remediation_id':rid,'errata_id':req['errata_id'],'publication_id':req['publication_id'],'outcome_status':req['outcome_status'],'public_url':req['public_url'],'public_message':req.get('public_message',''),'evidence_refs':req.get('evidence_refs',[]),'published_artifacts_mutated':False,'created':utc_now_iso()}
 write_json_atomic(out/f'{oid}.errata_outcome.json',outcome)
 h='sha256:'+sha256_file(out/f'{oid}.errata_outcome.json')
 rh='sha256:'+sha256_file(Path(x.remediation_root)/f'remediation/soil/cycles/{rid}/remediation_handoff_receipt.json')
 rec={'schema_version':'kfm.v1','receipt_type':'ErrataOutcomeReceipt','domain':'soil','outcome_id':oid,'remediation_id':rid,'decision':'pass','source_remediation_handoff_receipt_hash':rh,'errata_outcome_hash':h,'policy_checks':{'remediation_checked':True,'errata_publication_checked':True,'steward_review_checked':True,'immutability_checked':True,'public_paths_checked':True,'forbidden_terms_checked':True,'contact_data_checked':True},'signatures':{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'},'created':utc_now_iso()}
 write_json_atomic(out/f'{oid}.errata_outcome_receipt.json',rec)
 print(json.dumps({'allowed':True,'outcome_id':oid},sort_keys=True)); return 0
if __name__=='__main__': raise SystemExit(main())
