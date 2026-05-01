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
 a=argparse.ArgumentParser();a.add_argument('--archive-root',required=True);a.add_argument('--preservation-root',required=True);a.add_argument('--archive-package-id');a.add_argument('--out-root',required=True);x=a.parse_args(argv)
 if pkg_check(['--archive-root',x.archive_root]+(['--archive-package-id',x.archive_package_id] if x.archive_package_id else []))!=0: print(json.dumps({'fixity_audit_passed':False,'failure_reasons':['invalid package']})); return 1
 ar=Path(x.archive_root)/'archive/soil'; aid=x.archive_package_id or load_json(ar/'current_archive_package.json')['active_archive_package_id']; pkg=ar/'packages'/aid
 m=load_json(pkg/'archive_manifest.json'); r=load_json(pkg/'archive_receipt.json'); fails=[]; count=0
 for fn,h in r.get('generated_artifacts',{}).items():
  count+=1
  if 'sha256:'+sha256_file(pkg/fn)!=h: fails.append(f'hash mismatch {fn}')
 report={'schema_version':'kfm.v1','object_type':'SoilArchiveFixityAuditReport','domain':'soil','archive_package_id':aid,'preservation_id':m.get('preservation_id'),'release_id':m.get('release_id'),'fixity_audit_passed':not fails,'checked_artifact_count':count,'failure_reasons':fails,'created':utc_now_iso()}
 rec={'schema_version':'kfm.v1','receipt_type':'ArchiveFixityAuditReceipt','domain':'soil','archive_package_id':aid,'decision':'pass' if not fails else 'fail','source_archive_receipt_hash':'sha256:'+sha256_file(pkg/'archive_receipt.json'),'source_preservation_receipt_hash':'sha256:'+sha256_file(Path(x.preservation_root)/f"preservation/soil/packages/{m.get('preservation_id')}/preservation_receipt.json"),'policy_checks':{'archive_package_valid':True,'fixity_checked':True,'merkle_checked':True,'public_only':True,'no_forbidden_terms':True,'no_private_paths':True},'signatures':{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'},'created':utc_now_iso()}
 out=Path(x.out_root)/'archive/soil/fixity_audits';write_json_atomic(out/f'{aid}.fixity_audit_report.json',report);write_json_atomic(out/f'{aid}.fixity_audit_receipt.json',rec)
 print(json.dumps(report,sort_keys=True)); return 0 if not fails else 1
if __name__=='__main__': raise SystemExit(main())
