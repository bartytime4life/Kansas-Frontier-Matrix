#!/usr/bin/env python3
import argparse, json, sys
from pathlib import Path as _P
sys.path.insert(0,str(_P(__file__).resolve().parents[2]))
from kfm.air_quality.airnow.gate import run_gate

def main():
    p=argparse.ArgumentParser(); p.add_argument('--manifest',required=True); p.add_argument('--out-dir',required=True); p.add_argument('--created-at',required=True)
    a=p.parse_args()
    try:
        r=run_gate(a.manifest,a.out_dir,a.created_at)
        print(json.dumps(r,indent=2,sort_keys=True))
        return 0 if r['decision_outcome'] in ('ALLOW_INTERNAL_REVIEW_ONLY','NEEDS_REMEDIATION') and r['finite_outcome']!='DENY' else 2
    except Exception as e:
        print(json.dumps({"validation_outcome":"FAIL","error":str(e)}))
        return 2
if __name__=='__main__': raise SystemExit(main())
