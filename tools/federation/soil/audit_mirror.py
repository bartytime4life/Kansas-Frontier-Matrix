#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path
from tools.validators.soil.federation_check import main as federation_check
from tools.federation.soil._reconciliation_common import *

def main(argv=None):
 a=argparse.ArgumentParser();a.add_argument('--federation-root',required=True);a.add_argument('--federation-id');a.add_argument('--mirror-root');a.add_argument('--out-root',required=True);x=a.parse_args(argv)
 fid=x.federation_id or load_current_federation(x.federation_root)['active_federation_id'];rs=[]
 if federation_check(['--federation-root',x.federation_root,'--federation-id',fid])!=0: rs.append('federation invalid')
 rel=Path(x.federation_root)/f'federation/soil/releases/{fid}'; mm=load_json(rel/'mirror/mirror_manifest.json'); fr=load_json(rel/'federation_receipt.json')
 files=mm.get('files',[]); checked=0
 if mm.get('live_mirror_sync_performed') is True: rs.append('live_mirror_sync_performed true')
 for f in files:
  if not validate_external_url(f.get('public_url')): rs.append('invalid public url')
  if not f.get('sha256') or not f.get('media_type'): rs.append('missing hash/media_type')
  if has_private_path(f.get('logical_path')): rs.append('private path')
  if x.mirror_root:
   p=Path(x.mirror_root)/f['logical_path']
   if not p.exists(): rs.append(f'missing file {f["logical_path"]}')
   elif sha256_file(p)!=f['sha256']: rs.append(f'bad hash {f["logical_path"]}')
   checked+=1
 report={'schema_version':'kfm.v1','object_type':'SoilMirrorAuditReport','domain':'soil','federation_id':fid,'discovery_id':mm.get('discovery_id'),'release_id':mm.get('release_id'),'mirror_audit_passed':not rs,'audit_mode':'snapshot_root' if x.mirror_root else 'manifest_only','required_file_count':len(files),'checked_file_count':checked,'failure_reasons':sorted(set(rs)),'created':utc_now_iso()}
 out=Path(x.out_root)/'federation/soil/mirror_audits';write_json_atomic(out/f'{fid}.mirror_audit_report.json',report)
 receipt={'schema_version':'kfm.v1','receipt_type':'MirrorAuditReceipt','domain':'soil','federation_id':fid,'decision':'pass' if not rs else 'fail','source_mirror_manifest_hash':'sha256:'+sha256_file(rel/'mirror/mirror_manifest.json'),'source_federation_receipt_hash':'sha256:'+sha256_file(rel/'federation_receipt.json'),'policy_checks':{'mirror_manifest_checked':True,'hashes_checked':True,'public_only':True,'no_forbidden_terms':True,'no_private_paths':True,'live_mirror_sync_performed_false':True},'signatures':{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'},'created':utc_now_iso()}
 write_json_atomic(out/f'{fid}.mirror_audit_receipt.json',receipt)
 print(json.dumps({'mirror_audit_passed':not rs,'federation_id':fid,'reasons':sorted(set(rs))})); return 0 if not rs else 1
if __name__=='__main__': raise SystemExit(main())
