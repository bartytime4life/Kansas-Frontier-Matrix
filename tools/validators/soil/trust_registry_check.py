#!/usr/bin/env python3
from __future__ import annotations
import sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
import argparse, json
from pathlib import Path
from tools.trust_registry.soil._trust_registry_common import *

def main(argv=None):
 a=argparse.ArgumentParser(); a.add_argument('--registry-root',required=True); a.add_argument('--registry-id'); x=a.parse_args(argv)
 root=Path(x.registry_root)/'trust_registry/soil'; rid=x.registry_id or load_json(root/'current_registry.json')['active_registry_id']; d=root/'registrations'/rid; fail=[]
 m=load_json(d/'registry_manifest.json'); rc=load_json(d/'registry_receipt.json'); c=load_json(d/'trust_certificate.json'); s=load_json(d/'certificate_status.json'); t=load_json(d/'transparency_log.json'); b=(d/'badge.svg').read_text(encoding='utf-8')
 if m.get('object_type')!='SoilTrustRegistryManifest': fail.append('bad manifest')
 if rc.get('receipt_type')!='TrustRegistryReceipt' or rc.get('decision')!='pass' or not rc.get('signatures'): fail.append('bad receipt/signature')
 if c.get('object_type')!='SoilTrustCertificate' or not c.get('signatures'): fail.append('bad certificate/signature')
 if s.get('object_type')!='SoilTrustCertificateStatus' or s.get('certificate_status')!='active' or s.get('public_advertising_allowed') is not True: fail.append('bad status')
 if t.get('object_type')!='SoilTrustTransparencyLog': fail.append('bad transparency')
 _,root_hash=build_hash_chain([{k:v for k,v in e.items() if k not in ['ordinal','previous_entry_hash','entry_hash']} for e in t.get('entries',[])])
 if root_hash!=t.get('log_root'): fail.append('transparency root mismatch')
 if '<script' in b.lower(): fail.append('badge script')
 for fn,h in rc.get('generated_artifacts',{}).items():
  if not (d/fn).exists() or 'sha256:'+sha256_file(d/fn)!=h: fail.append(f'hash mismatch {fn}')
 if scan_payload_for_forbidden_terms({'m':m,'c':c,'s':s,'t':t}) or has_private_path(json.dumps(m)): fail.append('forbidden/private')
 ok=not fail; print(json.dumps({'trust_registry_valid':ok,'registry_id':rid,'certification_id':m.get('certification_id'),'release_id':m.get('release_id'),'certificate_status':s.get('certificate_status'),'failure_reasons':fail},sort_keys=True)); return 0 if ok else 1
if __name__=='__main__': raise SystemExit(main())
