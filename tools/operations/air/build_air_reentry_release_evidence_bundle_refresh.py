#!/usr/bin/env python
import argparse, json, hashlib, sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent))
from _reentry_release_candidate_common import *

def load(p): return json.loads(Path(p).read_text())
def h(p): return sha_path(p)
def outj(path,obj,dry=False):
    if not dry: writej(path,obj)

def event(out_dir, et, result='pass', dry=False):
    if dry: return
    p=Path(out_dir)/'reentry_release_candidate_refresh_events.jsonl'
    with p.open('a') as f: f.write(json.dumps({'event_type':et,'result':result},sort_keys=True)+'\n')
p=argparse.ArgumentParser();p.add_argument('--out-dir',required='PRINT' not in 'reentry_release_evidence_bundle_refresh.json');p.add_argument('--release-candidate-refresh-dir',action='append');p.add_argument('--release-candidate-refresh-package');p.add_argument('--qa-revalidation-refresh');p.add_argument('--evidence-bundle-refresh');p.add_argument('--release-manifest-refresh-candidate');p.add_argument('--release-candidate-refresh-decision');p.add_argument('--lineage-bridge-refresh');p.add_argument('--release-candidate-refresh-ledger');p.add_argument('--as-of');p.add_argument('--fixture-only',action='store_true');p.add_argument('--allow-fixture-postcheck',action='store_true');p.add_argument('--allow-fixture-ledger',action='store_true');p.add_argument('--dry-run',action='store_true');a=p.parse_args();
obj={'schema_version':'1.0.0','domain':'atmosphere.air','status':'fixture','generated_at':ts(a.as_of),'as_of':ts(a.as_of)};chk_obj(obj);out=Path(a.out_dir);outj(out/'reentry_release_evidence_bundle_refresh.json',obj,a.dry_run);event(out,'evidence_bundle_refresh_created',dry=a.dry_run);print('PASS')
