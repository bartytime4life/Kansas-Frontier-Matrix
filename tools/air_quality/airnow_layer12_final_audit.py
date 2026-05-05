import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import argparse, json, sys
from kfm.air_quality.airnow.audit import run_final_audit


def main():
 p=argparse.ArgumentParser()
 p.add_argument('--manifest',required=True)
 p.add_argument('--out-dir',required=True)
 p.add_argument('--created-at',required=True)
 a=p.parse_args()
 r=run_final_audit(a.manifest,a.out_dir,a.created_at)
 print(json.dumps(r,indent=2,sort_keys=True))
 ok={"FINAL_AUDIT_COMPLETE_INTERNAL_ONLY","FINAL_AUDIT_COMPLETE_WITH_WARNINGS","FINAL_AUDIT_PARTIAL","FINAL_AUDIT_NEEDS_MORE_INPUT"}
 sys.exit(0 if r.get('workflow_outcome') in ok and r.get('finite_outcome')!='DENY' else 1)

if __name__=='__main__':
 main()
