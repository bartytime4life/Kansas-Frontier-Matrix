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
p=argparse.ArgumentParser();p.add_argument('--candidate-reentry-refresh-dir',action='append',required=True);p.add_argument('--candidate-reentry-refresh-ledger',required=True);p.add_argument('--candidate-reentry-refresh-postcheck',required=True);p.add_argument('--candidate-reentry-refresh-audit',required=True);p.add_argument('--out-dir',required=True);p.add_argument('--as-of');p.add_argument('--fixture-only',action='store_true');p.add_argument('--dry-run',action='store_true');a=p.parse_args();
if load(a.candidate_reentry_refresh_postcheck).get('result') in ('deny','blocked'): deny('candidate reentry postcheck invalid')
obj={'schema_version':'1.0.0','release_candidate_refresh_id':'rcrf-001','domain':'atmosphere.air','created_at':ts(a.as_of),'as_of':ts(a.as_of),'candidate_reentry_refresh_manifest_ref':a.candidate_reentry_refresh_dir[0]+'/candidate_reentry_manifest.json','candidate_reentry_refresh_package_ref':a.candidate_reentry_refresh_dir[0]+'/candidate_reentry_package.json','candidate_reentry_refresh_promotion_decision_ref':a.candidate_reentry_refresh_dir[0]+'/candidate_reentry_promotion_decision.json','candidate_reentry_refresh_postcheck_report_ref':a.candidate_reentry_refresh_postcheck,'candidate_reentry_refresh_audit_report_ref':a.candidate_reentry_refresh_audit,'candidate_reentry_refresh_ledger_manifest_ref':a.candidate_reentry_refresh_ledger,'refreshed_baseline_refresh_recertification_ref':'fixture://baseline','refresh_compatibility_gate_report_ref':'fixture://compat','sunset_refresh_review_queue_ref':'fixture://sunset_queue','sunset_refresh_review_decision_refs':[],'source_chain_refs':a.candidate_reentry_refresh_dir,'candidate_artifact_refs':[{'artifact_type':'candidate_reentry_refresh','path':a.candidate_reentry_refresh_postcheck,'sha256':h(a.candidate_reentry_refresh_postcheck),'source_ref':a.candidate_reentry_refresh_postcheck,'candidate_only':True,'immutable_preview':True}],'candidate_read_model_refs':[],'candidate_delivery_refs':[],'candidate_baseline_refs':[],'non_mutation_guarantees':['no_source_mutation'],'safety_checks':['no_published_writes'],'status':'fixture_release_candidate_refresh_package' if a.fixture_only else 'candidate_release_candidate_refresh_package'};chk_obj(obj)
out=Path(a.out_dir);outj(out/'reentry_release_candidate_refresh_package.json',obj,a.dry_run);event(out,'release_candidate_refresh_package_created',dry=a.dry_run);print('PASS')
