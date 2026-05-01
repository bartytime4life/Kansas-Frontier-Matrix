#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
import argparse, json
from pathlib import Path
from tools.federation.soil._federation_common import *
from tools.validators.soil.federation_check import main as fcheck

def main(argv=None):
 a=argparse.ArgumentParser();a.add_argument('--federation-root',required=True);a.add_argument('--target',required=True);a.add_argument('--registry-fixture',required=True);a.add_argument('--out-root',required=True);x=a.parse_args(argv)
 if fcheck(['--federation-root',x.federation_root])!=0: print(json.dumps({'mock_submission_recorded':False,'reasons':['invalid federation']})); return 1
 rg=load_json(x.registry_fixture); ptr=load_json(Path(x.federation_root)/'federation/soil/current_federation.json'); fid=ptr['active_federation_id']; rel=Path(x.federation_root)/'federation/soil/releases'/fid
 pmap={'ckan':'targets/ckan/package.json','dcat':'targets/dcat/catalog.dataset.jsonld','data_gov':'targets/data_gov/dcat-us.json','stac':'targets/stac/catalog.json','ogc_records':'targets/ogc_records/records.json','schemaorg':'targets/schemaorg/catalog.jsonld','mirror':'mirror/mirror_manifest.json','notifications':'notifications/change_notice.json'}
 payload=load_json(rel/pmap[x.target]); req=[k for k in rg.get('required_fields',[]) if k not in payload]
 if rg.get('decision')!='accept' or req: print(json.dumps({'mock_submission_recorded':False,'target':x.target,'reasons':['rejected' if rg.get('decision')!='accept' else f'missing fields {req}']})); return 1
 out=Path(x.out_root)/f'federation/soil/submissions/{fid}'; request={'schema_version':'kfm.v1','object_type':'MockFederationSubmissionRequest','target':x.target,'federation_id':fid,'payload':payload}; write_json_atomic(out/f'{x.target}.submission_request.json',request)
 receipt={'schema_version':'kfm.v1','receipt_type':'MockFederationSubmissionReceipt','domain':'soil','federation_id':fid,'release_id':ptr['release_id'],'discovery_id':ptr['discovery_id'],'target':x.target,'registry_id':rg.get('registry_id'),'decision':'accepted','live_submission_performed':False,'submitted_payload_hash':stable_payload_hash(payload),'source_federation_receipt_hash':sha256_file(rel/'federation_receipt.json'),'policy_checks':{'federation_valid':True,'public_only':True,'no_forbidden_terms':True,'no_private_paths':True,'live_submission_performed_false':True},'signatures':{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'}}
 write_json_atomic(out/f'{x.target}.submission_receipt.json',receipt)
 print(json.dumps({'mock_submission_recorded':True,'target':x.target,'decision':'accepted','live_submission_performed':False,'outputs':{'request':str(out/f'{x.target}.submission_request.json'),'receipt':str(out/f'{x.target}.submission_receipt.json')}})); return 0
if __name__=='__main__': raise SystemExit(main())
