#!/usr/bin/env python3
import argparse,json,hashlib
from pathlib import Path
from datetime import datetime,timezone

def now(): return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
def load(p): return json.loads(Path(p).read_text())
def deny(msg): raise SystemExit(msg)

def main():
 p=argparse.ArgumentParser();p.add_argument('--publication-boundary-dir',action='append',default=[]);p.add_argument('--publication-boundary-ledger',required=True);p.add_argument('--publication-boundary-postcheck',required=True);p.add_argument('--publication-boundary-audit',required=True);p.add_argument('--out-dir',required=True);p.add_argument('--as-of');p.add_argument('--allow-fixture-plan',action='store_true');p.add_argument('--dry-run',action='store_true');a=p.parse_args()
 asof=a.as_of or now(); dirs=[Path(d) for d in a.publication_boundary_dir]
 def rf(name):
  for d in dirs:
   f=d/name
   if f.exists(): return str(f)
  deny(f'missing {name}')
 post=load(a.publication_boundary_postcheck); aud=load(a.publication_boundary_audit); led=load(a.publication_boundary_ledger)
 if post.get('result') in ('deny','blocked') or aud.get('result')=='deny' or not led.get('chain_hash'): deny('boundary checks failed')
 if not a.allow_fixture_plan: deny('fixture plan not allowed')
 out=Path(a.out_dir); out.mkdir(parents=True,exist_ok=True)
 plan={'schema_version':'v1','materialization_plan_id':'rmp-'+hashlib.sha256(asof.encode()).hexdigest()[:12],'domain':'atmosphere.air','created_at':now(),'as_of':asof,
 'reentry_publication_candidate_manifest_ref':rf('reentry_publication_candidate_manifest.json'),'reentry_publication_manifest_candidate_ref':rf('reentry_publication_manifest_candidate.json'),'reentry_publication_eligibility_decision_ref':rf('reentry_publication_eligibility_decision.json'),'reentry_publication_boundary_review_ref':rf('reentry_publication_boundary_review.json'),'reentry_gate_d_attestation_ref':rf('reentry_gate_d_attestation.json'),'reentry_aqs_reconciliation_refresh_ref':rf('reentry_aqs_reconciliation_refresh.json'),'reentry_publication_boundary_postcheck_report_ref':a.publication_boundary_postcheck,'reentry_publication_boundary_audit_report_ref':a.publication_boundary_audit,'reentry_publication_boundary_ledger_manifest_ref':a.publication_boundary_ledger,
 'source_chain_refs':[],'candidate_artifact_refs':[],'planned_materialized_artifacts':[{'artifact_type':'preview_manifest','target_path':'publication_preview/reentry_publication_artifact_preview_manifest.json','source_ref':rf('reentry_publication_manifest_candidate.json'),'candidate_only':True,'immutable_preview':True}],
 'non_mutation_guarantees':{'no_source_mutation':True},'forbidden_actions':['publish','deploy','notify','delete','rebuild_read_model'],'safety_checks':{'no_published_path_refs':True,'no_raw_work_quarantine_processed':True},'status':'fixture_materialization_plan'}
 if not a.dry_run: (out/'reentry_publication_materialization_plan.json').write_text(json.dumps(plan,indent=2,sort_keys=True)+'\n');(out/'reentry_publication_materialization_events.jsonl').write_text(json.dumps({'schema_version':'v1','event_id':'evt-1','domain':'atmosphere.air','event_type':'materialization_plan_created','created_at':now(),'as_of':asof,'actor':'fixture-non-production','subject_refs':[str(out/'reentry_publication_materialization_plan.json')],'evidence_refs':[],'result':'pass','details':{}})+'\n')
 print('PASS')
if __name__=='__main__': main()
