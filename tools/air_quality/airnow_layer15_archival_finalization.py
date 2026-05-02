
import argparse, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from kfm.air_quality.airnow.archival_finalization.run_archival_finalization import run_archival_finalization

def main():
 p=argparse.ArgumentParser()
 p.add_argument('--manifest',required=True)
 p.add_argument('--out-dir',required=True)
 p.add_argument('--created-at',required=True)
 a=p.parse_args()
 r=run_archival_finalization(a.manifest,a.out_dir,a.created_at)
 print(json.dumps(r,indent=2,sort_keys=True))
 ok={"ARCHIVAL_FINALIZATION_COMPLETE_INTERNAL_ONLY","ARCHIVAL_FINALIZATION_COMPLETE_WITH_WARNINGS","ARCHIVAL_FINALIZATION_PARTIAL","ARCHIVAL_FINALIZATION_NEEDS_MORE_INPUT"}
 sys.exit(0 if r.get('workflow_outcome') in ok and r.get('finite_outcome')!='DENY' else 1)
if __name__=='__main__': main()
