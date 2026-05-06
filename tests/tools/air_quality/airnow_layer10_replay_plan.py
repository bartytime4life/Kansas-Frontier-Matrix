import pathlib, sys
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parents[2]))
import argparse, json, sys
from kfm.air_quality.airnow.replay import run_replay_planner

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--manifest',required=True)
    ap.add_argument('--out-dir',required=True)
    ap.add_argument('--created-at',required=True)
    a=ap.parse_args()
    rec=run_replay_planner(a.manifest,a.out_dir,a.created_at)
    print(json.dumps(rec,indent=2,sort_keys=True))
    ok={"REPLAY_PLAN_READY","REPLAY_PLAN_READY_WITH_WARNINGS","REPLAY_PLAN_NEEDS_MORE_EVIDENCE"}
    sys.exit(0 if rec.get('workflow_outcome') in ok and rec.get('finite_outcome')!='DENY' else 1)
if __name__=='__main__':
    main()
