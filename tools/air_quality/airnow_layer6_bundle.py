#!/usr/bin/env python3
import argparse, json, sys
from pathlib import Path as _P
sys.path.insert(0,str(_P(__file__).resolve().parents[2]))
from kfm.air_quality.airnow.bundle import build_bundle

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--manifest',required=True); ap.add_argument('--out-dir',required=True); ap.add_argument('--created-at',required=True)
    a=ap.parse_args()
    try:
        rec=build_bundle(a.manifest,a.out_dir,a.created_at)
        print(json.dumps(rec,indent=2,sort_keys=True)); return 0
    except Exception as e:
        print(json.dumps({"validation_outcome":"FAIL","error":str(e)}))
        return 2
if __name__=='__main__': raise SystemExit(main())
