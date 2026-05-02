#!/usr/bin/env python3
import argparse, json, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
from kfm.air_quality.airnow.retention_review import run_retention_review
p=argparse.ArgumentParser()
p.add_argument('--manifest',required=True)
p.add_argument('--out-dir',required=True)
p.add_argument('--created-at',required=True)
a=p.parse_args()
r=run_retention_review(a.manifest,a.out_dir,a.created_at)
print(json.dumps(r,indent=2,sort_keys=True))
sys.exit(0 if r.get('workflow_outcome') in {'RETENTION_REVIEW_ACCEPTED_FOR_INTERNAL_ARCHIVAL_REVIEW','RETENTION_REVIEW_ACCEPTED_WITH_WARNINGS','RETENTION_REVIEW_PARTIAL','RETENTION_REVIEW_NEEDS_MORE_INPUT'} and r.get('finite_outcome')!='DENY' else 1)
