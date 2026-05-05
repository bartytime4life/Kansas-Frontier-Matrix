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
 a=argparse.ArgumentParser();a.add_argument('--archive-root',required=True);a.add_argument('--preservation-root',required=True);a.add_argument('--published-root',required=True);a.add_argument('--ops-root',required=True);a.add_argument('--out-root',required=True);x=a.parse_args(argv)
 if pkg_check(['--archive-root',x.archive_root])!=0: print(json.dumps({'decision':'fail'})); return 1
 ar=Path(x.archive_root)/'archive/soil'; aid=load_json(ar/'current_archive_package.json')['active_archive_package_id']; pkg=ar/'packages'/aid; m=load_json(pkg/'archive_manifest.json')
 ack=load_json(ar/f'acks/{aid}.archive_ack_receipt.json'); fix=load_json(ar/f'fixity_audits/{aid}.fixity_audit_receipt.json'); ops=load_operational_status(x.ops_root)
 st='ready'; decision='pass'; pa=True
 if ack.get('archive_ack_status')=='pending': st='degraded';decision='degraded'
 if ack.get('archive_ack_status') not in {'accepted','pending'} or fix.get('decision')!='pass' or not ops.get('public_access_allowed'): st='blocked';decision='fail';pa=False
 c={'schema_version':'kfm.v1','object_type':'SoilArchiveCustodyStatus','domain':'soil','archive_package_id':aid,'preservation_id':m.get('preservation_id'),'release_id':m.get('release_id'),'custody_state':st,'public_advertising_allowed':pa,'latest_fixity_audit_decision':fix.get('decision'),'archive_ack_status':ack.get('archive_ack_status'),'retracted':release_is_retracted(x.published_root,m.get('release_id')),'created':utc_now_iso()}
 r={'schema_version':'kfm.v1','receipt_type':'ArchiveCustodyStatusReceipt','domain':'soil','archive_package_id':aid,'decision':decision,'source_archive_receipt_hash':'sha256:'+sha256_file(pkg/'archive_receipt.json'),'source_fixity_audit_receipt_hash':'sha256:'+sha256_file(ar/f'fixity_audits/{aid}.fixity_audit_receipt.json'),'source_archive_ack_receipt_hash':'sha256:'+sha256_file(ar/f'acks/{aid}.archive_ack_receipt.json'),'policy_checks':{'archive_package_checked':True,'fixity_audit_checked':True,'archive_ack_checked':True,'retraction_checked':True,'incident_checked':True,'public_access_allowed':ops.get('public_access_allowed') is True},'signatures':{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'},'created':utc_now_iso()}
 out=Path(x.out_root)/'archive/soil/status';write_json_atomic(out/'current_custody_status.json',c);write_json_atomic(out/'custody_status_receipt.json',r);print(json.dumps(c,sort_keys=True));return 0 if decision!='fail' else 1
if __name__=='__main__': raise SystemExit(main())
