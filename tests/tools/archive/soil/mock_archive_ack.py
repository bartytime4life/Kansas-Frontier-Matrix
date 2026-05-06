#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.archive.soil._archive_common import *
from tools.validators.soil.archive_package_check import main as pkg_check

def main(argv=None):
 a=argparse.ArgumentParser();a.add_argument('--archive-root',required=True);a.add_argument('--ack-fixture',required=True);a.add_argument('--out-root',required=True);x=a.parse_args(argv)
 if pkg_check(['--archive-root',x.archive_root])!=0: print(json.dumps({'ack_recorded':False,'reasons':['invalid archive package']})); return 1
 ar=Path(x.archive_root)/'archive/soil'; aid=load_json(ar/'current_archive_package.json')['active_archive_package_id']
 ack=load_json(x.ack_fixture); rs=[]
 if ack.get('ack_status') not in {'accepted','pending','rejected','tombstoned'}: rs.append('unknown ack_status')
 if not ack.get('archive_target'): rs.append('missing archive_target')
 if not validate_base_public_url(ack.get('archive_record_url')): rs.append('invalid archive_record_url')
 if ack.get('ack_status')=='accepted' and ack.get('public_accessible') is not True: rs.append('accepted requires public_accessible')
 if scan_payload_for_forbidden_terms(ack): rs.append('forbidden terms')
 if rs: print(json.dumps({'ack_recorded':False,'reasons':rs},sort_keys=True)); return 1
 out=Path(x.out_root)/'archive/soil/acks'; notice=out/f'{aid}.archive_ack_notice.json'; receipt=out/f'{aid}.archive_ack_receipt.json'; created=utc_now_iso()
 n={'schema_version':'kfm.v1','object_type':'SoilArchiveAckNotice','archive_package_id':aid,**ack}
 r={'schema_version':'kfm.v1','receipt_type':'SoilArchiveAckReceipt','archive_package_id':aid,'decision':'pass' if ack['ack_status'] in {'accepted','pending'} else 'fail','archive_ack_status':ack['ack_status'],'signatures':{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'},'created':created}
 write_json_atomic(notice,n); write_json_atomic(receipt,r); print(json.dumps({'ack_recorded':True,'archive_package_id':aid},sort_keys=True)); return 0 if r['decision']=='pass' else 1
if __name__=='__main__': raise SystemExit(main())
