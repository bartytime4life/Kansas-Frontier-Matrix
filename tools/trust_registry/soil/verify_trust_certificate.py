#!/usr/bin/env python3
from __future__ import annotations
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
import argparse, json
from pathlib import Path
from tools.trust_registry.soil._trust_registry_common import *
from tools.validators.soil.trust_registry_check import main as rcheck

def main(argv=None):
 a=argparse.ArgumentParser(); a.add_argument('--registry-root',required=True); a.add_argument('--registry-id'); a.add_argument('--out-root'); x=a.parse_args(argv)
 if rcheck(['--registry-root',x.registry_root]+(['--registry-id',x.registry_id] if x.registry_id else []))!=0:
  print(json.dumps({'verification_passed':False,'failure_reasons':['trust_registry_check failed']})); return 1
 root=Path(x.registry_root)/'trust_registry/soil'; rid=x.registry_id or load_json(root/'current_registry.json')['active_registry_id']; d=root/'registrations'/rid
 m=load_json(d/'registry_manifest.json'); s=load_json(d/'certificate_status.json'); rc=load_json(d/'registry_receipt.json'); c=load_json(d/'trust_certificate.json')
 fail=[]
 if s.get('certificate_status')!='active': fail.append('inactive status')
 if rc.get('decision')!='pass' or not rc.get('signatures') or not c.get('signatures'): fail.append('signature/decision failure')
 out={'verification_passed':not fail,'registry_id':rid,'certification_id':m.get('certification_id'),'release_id':m.get('release_id'),'failure_reasons':fail}
 if x.out_root:
  p=Path(x.out_root)/'trust_registry/soil/verifications';
  write_json_atomic(p/f'{rid}.verification_report.json',{'schema_version':'kfm.v1','object_type':'SoilTrustCertificateVerificationReport','domain':'soil',**out,'created':utc_now_iso()})
  write_json_atomic(p/f'{rid}.verification_receipt.json',{'schema_version':'kfm.v1','receipt_type':'TrustCertificateVerificationReceipt','domain':'soil','registry_id':rid,'decision':'pass' if not fail else 'fail','source_registry_receipt_hash':'sha256:'+sha256_file(d/'registry_receipt.json'),'source_verification_bundle_hash':'sha256:'+sha256_file(d/'verification_bundle.json'),'source_transparency_log_hash':'sha256:'+sha256_file(d/'transparency_log.json'),'policy_checks':{'registry_valid':not fail},'signatures':{'dsse':'PROPOSED-COSIGN','key_ref':'kfm://keys/ci'},'created':utc_now_iso()})
 print(json.dumps(out,sort_keys=True)); return 0 if not fail else 1
if __name__=='__main__': raise SystemExit(main())
