#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
from tools.assurance.soil._assurance_common import *

def main(argv=None):
 a=argparse.ArgumentParser(); a.add_argument('--assurance-root',required=True); a.add_argument('--assurance-id'); x=a.parse_args(argv)
 ridp=Path(x.assurance_root)/'assurance/soil/current_assurance.json'; aid=x.assurance_id or load_json(ridp)['active_assurance_id']
 d=Path(x.assurance_root)/f'assurance/soil/cycles/{aid}'
 fail=[]
 m=load_json(d/'assurance_manifest.json'); r=load_json(d/'assurance_receipt.json'); dr=load_json(d/'drift_report.json'); cls=load_json(d/'certificate_lifecycle_status.json')
 if m.get('object_type')!='SoilContinuousAssuranceManifest': fail.append('bad manifest')
 if r.get('receipt_type')!='ContinuousAssuranceReceipt' or r.get('from_state')!='TRUST_REGISTRY_READY' or r.get('to_state')!='CONTINUOUS_ASSURANCE_READY' or r.get('decision') not in {'pass','degraded'} or not r.get('signatures'): fail.append('bad receipt')
 if dr.get('drift_detected') is not False: fail.append('drift detected')
 if cls.get('certificate_status')!='active' or cls.get('public_advertising_allowed') is not True: fail.append('inactive cert')
 for fn,h in r.get('generated_artifacts',{}).items():
  if fn=='assurance_receipt.json': continue
  if not (d/fn).exists() or 'sha256:'+sha256_file(d/fn)!=h: fail.append(f'hash mismatch {fn}')
 if scan_payload_for_forbidden_terms({'m':m,'dr':dr}) or has_private_path(json.dumps(m)): fail.append('forbidden/private')
 ok=not fail; print(json.dumps({'assurance_valid':ok,'assurance_id':aid,'registry_id':m.get('registry_id'),'release_id':m.get('release_id'),'assurance_state':m.get('assurance_state'),'failure_reasons':fail},sort_keys=True)); return 0 if ok else 1
if __name__=='__main__': raise SystemExit(main())
