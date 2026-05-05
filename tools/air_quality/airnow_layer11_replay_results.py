import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
import argparse, json
from kfm.air_quality.airnow.replay_results.run_replay_result_intake import run_replay_result_intake

if __name__=='__main__':
 p=argparse.ArgumentParser()
 p.add_argument('--manifest',required=True); p.add_argument('--out-dir',required=True); p.add_argument('--created-at',required=True)
 a=p.parse_args()
 r=run_replay_result_intake(a.manifest,a.out_dir,a.created_at)
 print(json.dumps(r,sort_keys=True,indent=2))
 raise SystemExit(0 if r['workflow_outcome'] in {'REPLAY_RESULTS_ACCEPTED_FOR_INTERNAL_REVIEW','REPLAY_RESULTS_ACCEPTED_WITH_WARNINGS','REPLAY_RESULTS_PARTIAL','REPLAY_RESULTS_NEED_MORE_INPUT'} else 1)
