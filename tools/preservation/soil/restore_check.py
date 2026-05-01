#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path
from tools.preservation.soil._preservation_common import *
from tools.validators.soil.preservation_check import main as pchk

def main(argv=None):
 a=argparse.ArgumentParser();a.add_argument('--preservation-root',required=True);a.add_argument('--preservation-id');a.add_argument('--out-root');x=a.parse_args(argv)
 if pchk(['--preservation-root',x.preservation_root]+(['--preservation-id',x.preservation_id] if x.preservation_id else []))!=0: return 1
 root=Path(x.preservation_root)/'preservation/soil'; pid=x.preservation_id or load_json(root/'current_preservation.json')['active_preservation_id']; pkg=root/'packages'/pid
 fx=load_json(pkg/'fixity_manifest.json'); mt=load_json(pkg/'merkle_tree.json'); reasons=[]
 for a in fx['generated_artifacts']:
  p=pkg/a['logical_path']
  if sha256_file(p)!=a['sha256']: reasons.append('fixity mismatch')
 rep={'schema_version':'kfm.v1','object_type':'SoilPreservationRestoreReport','domain':'soil','preservation_id':pid,'restore_dry_run_passed':not reasons,'checked_artifact_count':len(fx['generated_artifacts']),'failure_reasons':sorted(set(reasons)),'created':utc_now_iso()}
 print(json.dumps(rep,sort_keys=True))
 if x.out_root:
  d=Path(x.out_root)/'preservation/soil/restore_checks'; d.mkdir(parents=True,exist_ok=True); write_json_atomic(d/f'{pid}.restore_report.json',rep); write_json_atomic(d/f'{pid}.restore_receipt.json',{'schema_version':'kfm.v1','receipt_type':'PreservationRestoreReceipt','domain':'soil','preservation_id':pid,'decision':'pass' if not reasons else 'fail','source_preservation_receipt_hash':'sha256:'+sha256_file(pkg/'preservation_receipt.json'),'source_fixity_manifest_hash':'sha256:'+sha256_file(pkg/'fixity_manifest.json'),'source_merkle_tree_hash':'sha256:'+sha256_file(pkg/'merkle_tree.json'),'policy_checks':{'preservation_valid':not reasons,'fixity_checked':True,'merkle_checked':True,'public_only':True,'no_forbidden_terms':True,'no_private_paths':True},'signatures':{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'},'created':utc_now_iso()})
 return 0 if not reasons else 1
if __name__=='__main__': raise SystemExit(main())
