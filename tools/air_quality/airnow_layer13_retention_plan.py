import os, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
#!/usr/bin/env python3
import argparse, json, sys
from kfm.air_quality.airnow.retention import run_retention_plan

p=argparse.ArgumentParser()
p.add_argument("--manifest",required=True)
p.add_argument("--out-dir",required=True)
p.add_argument("--created-at",required=True)
a=p.parse_args()
r=run_retention_plan(a.manifest,a.out_dir,a.created_at)
print(json.dumps(r,indent=2,sort_keys=True))
sys.exit(0 if r.get("workflow_outcome") in {"RETENTION_PLAN_COMPLETE_INTERNAL_ONLY","RETENTION_PLAN_COMPLETE_WITH_WARNINGS","RETENTION_PLAN_PARTIAL","RETENTION_PLAN_NEEDS_MORE_INPUT"} and r.get("finite_outcome")!="DENY" else 1)
