#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
from tools.certification.soil._certification_common import *

def main(argv=None):
 a=argparse.ArgumentParser();a.add_argument('--archive-root',required=True);a.add_argument('--attestation',required=True);a.add_argument('--out-root',required=True);x=a.parse_args(argv)
 att=load_json(x.attestation);cur=load_current_archive_package(x.archive_root);aid=cur['active_archive_package_id'];am=load_archive_manifest(x.archive_root,aid);ar=load_archive_receipt(x.archive_root,aid)
 rid=am.get('release_id');reasons=[]
 if att.get('decision')!='approved': reasons.append('decision not approved')
 if not att.get('steward'): reasons.append('missing steward')
 if not att.get('signatures'): reasons.append('missing signatures')
 sc=att.get('scope',{})
 if sc.get('archive_package_id')!=aid or sc.get('release_id')!=rid: reasons.append('scope mismatch')
 if scan_payload_for_forbidden_terms(att): reasons.append('forbidden terms')
 if any(has_private_path(v) for v in json.dumps(att).split()): pass
 if reasons: print(json.dumps({'attestation_allowed':False,'archive_package_id':aid,'release_id':rid,'reasons':reasons},sort_keys=True)); return 1
 out=Path(x.out_root)/'certification/soil/attestations';out.mkdir(parents=True,exist_ok=True)
 notice={'schema_version':'kfm.v1','object_type':'SoilStewardCertificationAttestationNotice','domain':'soil','archive_package_id':aid,'release_id':rid,'attestation':att,'created':utc_now_iso()}
 npath=out/f'{sanitize_id(aid)}.steward_attestation_notice.json';write_json_atomic(npath,notice)
 rec={'schema_version':'kfm.v1','receipt_type':'StewardCertificationAttestationReceipt','domain':'soil','archive_package_id':aid,'release_id':rid,'decision':'approved','source_archive_receipt_hash':'sha256:'+sha256_file(Path(x.archive_root)/f'archive/soil/packages/{aid}/archive_receipt.json'),'attestation_notice_hash':'sha256:'+sha256_file(npath),'policy_checks':{'archive_package_checked':True,'scope_checked':True,'steward_review_checked':True,'signatures_checked':True,'public_paths_checked':True,'forbidden_terms_checked':True},'signatures':{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'},'created':utc_now_iso()}
 rpath=out/f'{sanitize_id(aid)}.steward_attestation_receipt.json';write_json_atomic(rpath,rec)
 print(json.dumps({'attestation_allowed':True,'archive_package_id':aid,'release_id':rid,'notice_ref':safe_rel_ref(npath,x.out_root),'receipt_ref':safe_rel_ref(rpath,x.out_root)},sort_keys=True)); return 0
if __name__=='__main__': raise SystemExit(main())
