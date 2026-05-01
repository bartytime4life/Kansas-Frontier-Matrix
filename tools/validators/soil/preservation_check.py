#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path
from tools.preservation.soil._preservation_common import *

def main(argv=None):
 a=argparse.ArgumentParser();a.add_argument('--preservation-root',required=True);a.add_argument('--preservation-id');x=a.parse_args(argv)
 root=Path(x.preservation_root)/'preservation/soil'; pid=x.preservation_id or load_json(root/'current_preservation.json')['active_preservation_id']; pkg=root/'packages'/pid; rs=[]
 m=load_json(pkg/'preservation_manifest.json'); r=load_json(pkg/'preservation_receipt.json'); f=load_json(pkg/'fixity_manifest.json'); t=load_json(pkg/'merkle_tree.json')
 if m.get('object_type')!='SoilPreservationManifest': rs.append('manifest type')
 if r.get('receipt_type')!='PreservationReceipt' or r.get('decision')!='pass' or not r.get('signatures'): rs.append('receipt invalid')
 if r.get('live_archive_upload_performed') is not False or r.get('live_doi_minting_performed') is not False: rs.append('live flags true')
 for g,h in r.get('generated_artifacts',{}).items():
  p=pkg/g
  if not p.exists() or 'sha256:'+sha256_file(p)!=h: rs.append(f'hash mismatch {g}')
 out={'preservation_valid':not rs,'preservation_id':pid,'reconciliation_id':m.get('reconciliation_id'),'release_id':m.get('release_id'),'merkle_root':t.get('merkle_root'),'failure_reasons':sorted(set(rs))}; print(json.dumps(out,sort_keys=True)); return 0 if not rs else 1
if __name__=='__main__': raise SystemExit(main())
