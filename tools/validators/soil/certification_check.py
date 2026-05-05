#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
from tools.certification.soil._certification_common import *

def main(argv=None):
 a=argparse.ArgumentParser();a.add_argument('--certification-root',required=True);a.add_argument('--certification-id');x=a.parse_args(argv)
 cid=x.certification_id or load_json(Path(x.certification_root)/'certification/soil/current_certification.json')['active_certification_id']
 d=Path(x.certification_root)/f'certification/soil/certifications/{cid}'; fail=[]
 m=load_json(d/'certification_manifest.json'); r=load_json(d/'certification_receipt.json'); c=load_json(d/'control_matrix.json'); rc=load_json(d/'receipt_chain.json')
 if m.get('object_type')!='SoilTrustCertificationManifest': fail.append('bad manifest')
 if m.get('certification_status')!='TRUST_CERTIFIED': fail.append('bad status')
 if r.get('receipt_type')!='TrustCertificationReceipt' or r.get('decision')!='pass': fail.append('bad receipt')
 if not r.get('signatures'): fail.append('missing signatures')
 for fn,h in m.get('artifact_hashes',{}).items():
  p=d/fn
  if not p.exists() or 'sha256:'+sha256_file(p)!=h: fail.append(f'hash mismatch {fn}')
 if c.get('object_type')!='SoilTrustCertificationControlMatrix' or any(x.get('required') and x.get('status')!='pass' for x in c.get('controls',[])): fail.append('control failure')
 if rc.get('chain_integrity_passed') is not True: fail.append('chain failed')
 if scan_payload_for_forbidden_terms(load_json(d/'public_trust_report.json')): fail.append('forbidden terms')
 ok=not fail; print(json.dumps({'certification_valid':ok,'certification_id':cid,'archive_package_id':m.get('archive_package_id'),'release_id':m.get('release_id'),'failure_reasons':fail},sort_keys=True)); return 0 if ok else 1
if __name__=='__main__': raise SystemExit(main())
