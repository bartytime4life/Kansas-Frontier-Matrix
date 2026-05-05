#!/usr/bin/env python3
import argparse, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from kfm.air_quality.airnow.preservation_closure_finalization.run_preservation_closure_finalization import run_preservation_closure_finalization

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--manifest',required=True); ap.add_argument('--out-dir',required=True); ap.add_argument('--created-at',required=True)
    a=ap.parse_args()
    try:
        r=run_preservation_closure_finalization(a.manifest,a.out_dir,a.created_at)
        print(json.dumps(r,indent=2,sort_keys=True))
        return 0 if r.get('validation_outcome')=='PASS' else 2
    except Exception as e:
        print(json.dumps({'error':str(e)}), file=sys.stderr)
        return 1
if __name__=='__main__': raise SystemExit(main())
