#!/usr/bin/env python3
import pathlib,sys
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[2]))
import argparse,json
from kfm.air_quality.airnow.manual_evidence import run_manual_evidence_verification
p=argparse.ArgumentParser(); p.add_argument('--manifest',required=True); p.add_argument('--out-dir',required=True); p.add_argument('--created-at',required=True)
a=p.parse_args(); r=run_manual_evidence_verification(a.manifest,a.out_dir,a.created_at); print(json.dumps(r,indent=2,sort_keys=True));
sys.exit(0 if r.get('workflow_outcome') in {'MANUAL_EVIDENCE_ACCEPTED_FOR_RERUN','MANUAL_EVIDENCE_PARTIALLY_ACCEPTED','MANUAL_EVIDENCE_NEEDS_MORE_INPUT'} and r.get('finite_outcome')!='DENY' else 1)
