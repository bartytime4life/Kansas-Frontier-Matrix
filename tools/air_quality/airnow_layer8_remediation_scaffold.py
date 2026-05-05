#!/usr/bin/env python3
import pathlib,sys
sys.path.insert(0,str(pathlib.Path(__file__).resolve().parents[2]))
import argparse, json, sys
from kfm.air_quality.airnow.remediation import run_remediation_scaffold
p=argparse.ArgumentParser()
p.add_argument('--manifest',required=True); p.add_argument('--out-dir',required=True); p.add_argument('--created-at',required=True)
a=p.parse_args(); r=run_remediation_scaffold(a.manifest,a.out_dir,a.created_at); print(json.dumps(r,indent=2,sort_keys=True));
sys.exit(0 if r.get('workflow_outcome') in {'REMEDIATION_SCAFFOLD_READY','REMEDIATION_SCAFFOLD_WARNINGS_ONLY','REMEDIATION_SCAFFOLD_NEEDS_INPUT'} and r.get('finite_outcome')!='DENY' and r.get('validation_outcome')=='PASS' else 1)