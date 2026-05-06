import argparse,json,sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[2]))
from kfm.air_quality.airnow.closure_archive_index_preservation.run_closure_archive_index_preservation_plan import run_closure_archive_index_preservation_plan

def main():
 p=argparse.ArgumentParser();p.add_argument('--manifest',required=True);p.add_argument('--out-dir',required=True);p.add_argument('--created-at',required=True);a=p.parse_args()
 r=run_closure_archive_index_preservation_plan(a.manifest,a.out_dir,a.created_at)
 print(json.dumps(r,indent=2,sort_keys=True))
 return 0 if r.get('validation_outcome')=='PASS' and r.get('finite_outcome')=='ANSWER' else 1
if __name__=='__main__': raise SystemExit(main())
