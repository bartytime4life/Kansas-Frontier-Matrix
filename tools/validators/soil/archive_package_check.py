#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.archive.soil._archive_common import *

def main(argv=None):
 a=argparse.ArgumentParser();a.add_argument('--archive-root',required=True);a.add_argument('--archive-package-id');x=a.parse_args(argv)
 ar=Path(x.archive_root)/'archive/soil'; rs=[]
 aid=x.archive_package_id or load_json(ar/'current_archive_package.json')['active_archive_package_id']
 pkg=ar/'packages'/aid
 m=load_json(pkg/'archive_manifest.json'); r=load_json(pkg/'archive_receipt.json')
 if m.get('object_type')!='SoilArchiveManifest': rs.append('manifest type')
 if m.get('archival_custody_status')!='ARCHIVAL_CUSTODY_READY': rs.append('custody status')
 if r.get('receipt_type')!='ArchiveCustodyReceipt' or r.get('from_state')!='PRESERVATION_READY' or r.get('to_state')!='ARCHIVAL_CUSTODY_READY' or r.get('decision')!='pass': rs.append('receipt invalid')
 if not r.get('signatures'): rs.append('missing signatures')
 if r.get('live_archive_upload_performed') is not False: rs.append('live upload true')
 for g,h in r.get('generated_artifacts',{}).items():
  p=pkg/g
  if not p.exists() or ('sha256:'+sha256_file(p))!=h: rs.append(f'hash mismatch {g}')
 for f in ['accession_request.json','custody_ledger.json','retention_schedule.json','fixity_audit_plan.json','archive_inventory.json','public_archive_index.json']:
  if not (pkg/f).exists(): rs.append(f'missing {f}')
 for obj,fn in [('SoilArchiveAccessionRequest','accession_request.json'),('SoilArchiveCustodyLedger','custody_ledger.json'),('SoilArchiveRetentionSchedule','retention_schedule.json'),('SoilArchiveFixityAuditPlan','fixity_audit_plan.json'),('SoilArchiveInventory','archive_inventory.json'),('SoilPublicArchiveIndex','public_archive_index.json')]:
  if load_json(pkg/fn).get('object_type')!=obj: rs.append(f'bad type {fn}')
 out={'archive_package_valid':not rs,'archive_package_id':aid,'preservation_id':m.get('preservation_id'),'release_id':m.get('release_id'),'failure_reasons':sorted(set(rs))}
 print(json.dumps(out,sort_keys=True)); return 0 if not rs else 1
if __name__=='__main__': raise SystemExit(main())
