#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path
from tools.accountability.soil._accountability_common import *
def main(argv=None):
 a=argparse.ArgumentParser(); a.add_argument('--accountability-root',required=True); a.add_argument('--accountability-id');x=a.parse_args(argv)
 aid=x.accountability_id or load_json(Path(x.accountability_root)/'accountability/soil/current_accountability.json')['active_accountability_id']
 c=Path(x.accountability_root)/f'accountability/soil/cycles/{aid}'; fail=[]
 m=load_json(c/'accountability_manifest.json'); r=load_json(c/'accountability_receipt.json')
 if m.get('object_type')!='SoilPublicAccountabilityManifest': fail.append('bad manifest')
 if r.get('receipt_type')!='PublicAccountabilityReceipt' or r.get('from_state')!='CONTINUOUS_ASSURANCE_READY' or r.get('to_state')!='PUBLIC_ACCOUNTABILITY_READY' or r.get('decision') not in {'pass','degraded'} or not r.get('signatures'): fail.append('bad receipt')
 for fn,h in r.get('generated_artifacts',{}).items():
  if 'sha256:'+sha256_file(c/fn)!=h: fail.append('hash mismatch '+fn)
 ok=not fail; print(json.dumps({'accountability_valid':ok,'accountability_id':aid,'assurance_id':m.get('assurance_id'),'registry_id':m.get('registry_id'),'release_id':m.get('release_id'),'accountability_state':m.get('accountability_state'),'failure_reasons':fail},sort_keys=True)); return 0 if ok else 1
if __name__=='__main__': raise SystemExit(main())
