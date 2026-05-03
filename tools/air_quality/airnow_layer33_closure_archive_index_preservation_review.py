import argparse, json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path: sys.path.insert(0, str(ROOT))
from kfm.air_quality.airnow.closure_archive_index_preservation_review import run_closure_archive_index_preservation_review

def main()->int:
    ap=argparse.ArgumentParser()
    ap.add_argument('--manifest',required=True)
    ap.add_argument('--out-dir',required=True)
    ap.add_argument('--created-at',required=True)
    a=ap.parse_args()
    try:
        r=run_closure_archive_index_preservation_review(a.manifest,a.out_dir,a.created_at)
        sys.stdout.write(json.dumps(r,indent=2,sort_keys=True)+'\n')
        return 0 if r.get('validation_outcome')=='PASS' else 1
    except Exception as ex:
        sys.stderr.write(f'RUNTIME_FAILURE:{ex}\n')
        return 2
if __name__=='__main__': raise SystemExit(main())
