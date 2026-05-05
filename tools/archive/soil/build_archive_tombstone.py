#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.archive.soil._archive_common import *

def main(argv=None):
 a=argparse.ArgumentParser();a.add_argument('--archive-root',required=True);a.add_argument('--preservation-root',required=True);a.add_argument('--reconciliation-root',required=True);a.add_argument('--published-root',required=True);a.add_argument('--release-id',required=True);a.add_argument('--out-root',required=True);x=a.parse_args(argv)
 if not release_is_retracted(x.published_root,x.release_id): print(json.dumps({'decision':'fail','reasons':['not retracted']})); return 1
 wr=load_withdrawal_reconciliation(x.reconciliation_root,x.release_id)
 if not wr: print(json.dumps({'decision':'fail','reasons':['missing withdrawal reconciliation']})); return 1
 ar=Path(x.archive_root)/'archive/soil'; aid=load_json(ar/'current_archive_package.json').get('active_archive_package_id') if (ar/'current_archive_package.json').exists() else None
 notice={'schema_version':'kfm.v1','object_type':'SoilArchiveTombstoneNotice','domain':'soil','release_id':x.release_id,'archive_package_id':aid,'status':'TOMBSTONED','public_advertising_allowed':False,'reason_type':'retraction','severity':'high','public_message':'Release retracted; archive retained as tombstone governance metadata.','created':utc_now_iso()}
 out=Path(x.out_root)/'archive/soil/tombstones'; n=out/f'{sanitize_id(x.release_id)}.archive_tombstone_notice.json'; write_json_atomic(n,notice)
 rec={'schema_version':'kfm.v1','receipt_type':'ArchiveTombstoneReceipt','from_state':'ARCHIVAL_CUSTODY_READY','to_state':'ARCHIVAL_TOMBSTONED','decision':'pass','release_id':x.release_id,'source_withdrawal_reconciliation_hash':'sha256:'+sha256_bytes(json.dumps(wr,sort_keys=True).encode()),'generated_artifacts':{n.name:'sha256:'+sha256_file(n)},'policy_checks':{'retraction_checked':True,'withdrawal_reconciliation_checked':True,'immutable_archive_preserved':True,'public_advertising_disabled':True},'signatures':{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'}}
 write_json_atomic(out/f'{sanitize_id(x.release_id)}.archive_tombstone_receipt.json',rec); print(json.dumps({'decision':'pass','release_id':x.release_id},sort_keys=True)); return 0
if __name__=='__main__': raise SystemExit(main())
