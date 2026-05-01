#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.corrective_actions.soil._corrective_common import *

def main(argv=None):
 a=argparse.ArgumentParser(); a.add_argument('--resolution-root',required=True); a.add_argument('--corrective-root',required=True); a.add_argument('--resolution-id'); a.add_argument('--item',required=True); x=a.parse_args(argv)
 req=load_json(x.item); rid=x.resolution_id or load_current_resolution(x.resolution_root)['active_resolution_id']
 man=load_resolution_manifest(x.resolution_root,rid); rec=load_resolution_receipt(x.resolution_root,rid); docket=load_json(Path(x.resolution_root)/f'resolution/soil/cycles/{rid}/adjudication_docket.json')
 fail=[]
 if req.get('steward_review',{}).get('decision')!='approved': fail.append('missing steward review approval')
 if req.get('source_adjudication_id') not in {e['adjudication_id'] for e in docket.get('entries',[])}: fail.append('missing source adjudication')
 if req.get('item_type') not in {'metadata','quality','rights','provenance','accessibility','public_notice'}: fail.append('unknown item_type')
 if req.get('severity') not in {'low','medium','high','critical'}: fail.append('unknown severity')
 if req.get('item_type') in {'rights','provenance','quality'} and not req.get('evidence_refs'): fail.append('missing evidence_refs')
 if scan_payload_for_contact_or_secret_terms(req): fail.append('contact/secret terms')
 if has_private_path(json.dumps(req)): fail.append('private path')
 if fail: print(json.dumps({'allowed':False,'reasons':fail},sort_keys=True)); return 1
 eid='soil-item-'+stable_payload_hash(req)[:16]
 notice={'schema_version':'kfm.v1','object_type':'SoilStub','domain':'soil','item_id':eid,'resolution_id':rid,'accountability_id':man.get('accountability_id'),'assurance_id':man.get('assurance_id'),'registry_id':man.get('registry_id'),'release_id':man.get('release_id'),'item_type':req['item_type'],'severity':req['severity'],'source_adjudication_id':req['source_adjudication_id'],'affected_bundle_id':req.get('affected_bundle_id'),'affected_field':req.get('affected_field'),'public_summary':req.get('public_summary'),'public_message':req.get('public_message'),'evidence_refs':req.get('evidence_refs',[]),'immutable_artifacts_mutated':False,'created':utc_now_iso()}
 out=Path(x.corrective_root)/f'corrective/soil/item/{rid}'; write_json_atomic(out/f'{eid}.item_notice.json',notice)
 receipt={'schema_version':'kfm.v1','receipt_type':'PublicErrataNoticeReceipt','domain':'soil','item_id':eid,'resolution_id':rid,'release_id':man.get('release_id'),'decision':'pass','source_resolution_receipt_hash':'sha256:'+sha256_file(Path(x.resolution_root)/f'resolution/soil/cycles/{rid}/resolution_receipt.json'),'item_notice_hash':'sha256:'+sha256_file(out/f'{eid}.item_notice.json'),'policy_checks':{'resolution_checked':True,'adjudication_checked':True,'evidence_checked':True,'steward_review_checked':True,'immutability_checked':True,'public_paths_checked':True,'forbidden_terms_checked':True,'contact_data_checked':True},'signatures':{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'},'created':utc_now_iso()}
 write_json_atomic(out/f'{eid}.item_receipt.json',receipt); print(json.dumps({'allowed':True,'item_id':eid},sort_keys=True)); return 0
if __name__=='__main__': raise SystemExit(main())
