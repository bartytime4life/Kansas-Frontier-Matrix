#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
from tools.validators.soil.federation_check import main as federation_check
from tools.federation.soil._reconciliation_common import *

def main(argv=None):
 a=argparse.ArgumentParser();a.add_argument('--federation-root',required=True);a.add_argument('--submissions-root',required=True);a.add_argument('--target',required=True);a.add_argument('--ack-fixture',required=True);a.add_argument('--out-root',required=True);x=a.parse_args(argv)
 rs=[]
 if x.target not in TARGETS: rs.append('unknown target')
 if federation_check(['--federation-root',x.federation_root])!=0: rs.append('federation invalid')
 ptr=load_current_federation(x.federation_root);fid=ptr['active_federation_id'];fr=load_federation_receipt(x.federation_root,fid)
 subs=load_mock_submission_receipts(x.submissions_root,fid); sub=subs.get(x.target)
 if not sub: rs.append('missing submission receipt')
 ack=load_json(x.ack_fixture)
 if ack.get('target')!=x.target: rs.append('target mismatch')
 if not ack.get('registry_id'): rs.append('registry_id missing')
 if ack.get('ack_status') not in ACK_STATUSES: rs.append('unknown ack_status')
 if scan_payload_for_forbidden_terms(ack): rs.append('forbidden terms in fixture')
 if not validate_external_url(ack.get('external_record_url')) or has_private_path(ack.get('external_record_url')): rs.append('invalid external_record_url')
 if ack.get('ack_status')=='accepted' and ack.get('public_accessible') is not True: rs.append('accepted must be public_accessible')
 if sub and ack.get('hash_echo') and ack.get('hash_echo')!=sub.get('submitted_payload_hash'): rs.append('submitted payload hash mismatch')
 if rs: print(json.dumps({'mock_ack_recorded':False,'target':x.target,'reasons':rs},sort_keys=True)); return 1
 out=Path(x.out_root)/f'federation/soil/acks/{fid}'
 notice={'schema_version':'kfm.v1','object_type':'SoilMockRegistryAckNotice','domain':'soil','federation_id':fid,'discovery_id':ptr.get('discovery_id'),'release_id':ptr.get('release_id'),'target':x.target,'registry_id':ack['registry_id'],'ack_status':ack['ack_status'],'external_record_id':ack.get('external_record_id'),'external_record_url':ack.get('external_record_url'),'public_accessible':ack.get('public_accessible',False),'live_registry_poll_performed':False,'created':utc_now_iso()}
 write_json_atomic(out/f'{x.target}.ack_notice.json',notice)
 rec={'schema_version':'kfm.v1','receipt_type':'MockRegistryAckReceipt','domain':'soil','federation_id':fid,'discovery_id':ptr.get('discovery_id'),'release_id':ptr.get('release_id'),'target':x.target,'registry_id':ack['registry_id'],'decision':ack['ack_status'],'live_registry_poll_performed':False,'source_submission_receipt_hash':'sha256:'+sha256_file(Path(x.submissions_root)/f'federation/soil/submissions/{fid}/{x.target}.submission_receipt.json'),'source_federation_receipt_hash':'sha256:'+sha256_file(Path(x.federation_root)/f'federation/soil/releases/{fid}/federation_receipt.json'),'ack_notice_hash':'sha256:'+sha256_file(out/f'{x.target}.ack_notice.json'),'policy_checks':{'federation_valid':True,'submission_receipt_checked':True,'public_only':True,'no_forbidden_terms':True,'no_private_paths':True,'live_registry_poll_performed_false':True},'signatures':{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'},'created':utc_now_iso()}
 write_json_atomic(out/f'{x.target}.ack_receipt.json',rec)
 print(json.dumps({'mock_ack_recorded':True,'target':x.target,'decision':ack['ack_status'],'live_registry_poll_performed':False,'outputs':{'ack_notice':str(out/f'{x.target}.ack_notice.json'),'ack_receipt':str(out/f'{x.target}.ack_receipt.json')}})); return 0
if __name__=='__main__': raise SystemExit(main())
