#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.resolution.soil._resolution_common import *

def main(argv=None):
 a=argparse.ArgumentParser(); a.add_argument('--resolution-root',required=True); a.add_argument('--resolution-id'); x=a.parse_args(argv)
 rid=x.resolution_id or load_json(Path(x.resolution_root)/'resolution/soil/current_resolution.json')['active_resolution_id']
 c=Path(x.resolution_root)/f'resolution/soil/cycles/{rid}'; fail=[]
 m=load_json(c/'resolution_manifest.json'); r=load_json(c/'resolution_receipt.json')
 if m.get('object_type')!='SoilCorrectionResolutionManifest': fail.append('bad manifest')
 if m.get('resolution_status')!='CORRECTION_RESOLUTION_READY': fail.append('bad status')
 if r.get('receipt_type')!='CorrectionResolutionReceipt' or r.get('from_state')!='PUBLIC_ACCOUNTABILITY_READY' or r.get('to_state')!='CORRECTION_RESOLUTION_READY' or r.get('decision') not in {'pass','degraded'}: fail.append('bad receipt')
 if not r.get('signatures'): fail.append('missing signature')
 for k,v in r.get('generated_artifacts',{}).items():
  if not (c/k).exists() or ('sha256:'+sha256_file(c/k))!=v: fail.append('hash mismatch '+k)
 t=load_json(c/'resolution_transparency_log.json');
 if t.get('object_type')!='SoilResolutionTransparencyLog': fail.append('bad transparency')
 ok=not fail; print(json.dumps({'resolution_valid':ok,'resolution_id':rid,'accountability_id':m.get('accountability_id'),'registry_id':m.get('registry_id'),'release_id':m.get('release_id'),'resolution_state':m.get('resolution_state'),'failure_reasons':fail},sort_keys=True)); return 0 if ok else 1
if __name__=='__main__': raise SystemExit(main())
