#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
import argparse, json
from pathlib import Path
from tools.federation.soil._federation_common import *
def main(argv=None):
 a=argparse.ArgumentParser();a.add_argument('--federation-root',required=True);a.add_argument('--published-root',required=True);a.add_argument('--release-id',required=True);a.add_argument('--out-root',required=True);x=a.parse_args(argv)
 if not release_is_retracted(x.published_root,x.release_id): print(json.dumps({'withdrawal_built':False,'reasons':['release not retracted']})); return 1
 notes=[n for n in load_retraction_notices(x.published_root) if n.get('release_id')==x.release_id]
 if not notes: print(json.dumps({'withdrawal_built':False,'reasons':['retraction notice missing']})); return 1
 ptrp=Path(x.federation_root)/'federation/soil/current_federation.json'; ptr=load_json(ptrp) if ptrp.exists() else {}
 out=Path(x.out_root)/'federation/soil/withdrawals'; rid=sanitize_id(x.release_id); n=notes[-1]
 notice={'schema_version':'kfm.v1','object_type':'SoilFederationWithdrawalNotice','domain':'soil','release_id':x.release_id,'federation_id':ptr.get('active_federation_id'),'discovery_id':ptr.get('discovery_id'),'status':'WITHDRAWAL_REQUIRED','reason_type':n.get('reason_type'),'severity':n.get('severity'),'public_message':n.get('public_message','retracted'),'created':utc_now_iso()}
 tw={'schema_version':'kfm.v1','object_type':'SoilFederationTargetWithdrawals','release_id':x.release_id,'live_withdrawal_performed':False,'targets':{t:{'action':'withdraw_tombstone','live_withdrawal_performed':False} for t in ['ckan','data_gov','stac','ogc_records','schemaorg','mirror','notifications']}}
 write_json_atomic(out/f'{rid}.withdrawal_notice.json',notice); write_json_atomic(out/f'{rid}.target_withdrawals.json',tw)
 gen={f'{rid}.withdrawal_notice.json':sha256_file(out/f'{rid}.withdrawal_notice.json'),f'{rid}.target_withdrawals.json':sha256_file(out/f'{rid}.target_withdrawals.json')}
 rc={'schema_version':'kfm.v1','receipt_type':'FederationWithdrawalReceipt','from_state':'FEDERATION_READY','to_state':'WITHDRAWAL_REQUIRED','decision':'pass','live_withdrawal_performed':False,'source_retraction_notice_hash':stable_payload_hash(n),'generated_artifacts':gen,'policy_checks':{'retraction_checked':True,'immutable_federation_preserved':True,'target_withdrawals_prepared':True,'live_withdrawal_performed_false':True},'signatures':{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'}}
 write_json_atomic(out/f'{rid}.withdrawal_receipt.json',rc); print(json.dumps({'withdrawal_built':True,'release_id':x.release_id})); return 0
if __name__=='__main__': raise SystemExit(main())
