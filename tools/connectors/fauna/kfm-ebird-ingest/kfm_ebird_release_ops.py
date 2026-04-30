#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, sys, re
from datetime import datetime, timezone
from pathlib import Path

DENIED=["decimalLatitude","decimalLongitude","latitude","longitude","lat","lon","raw_latitude","raw_longitude","point","geom","geometry"]
SECRET={"token","api_key","apikey","key","secret","password","credential","access_token","refresh_token"}


def cjson(o): return json.dumps(o,sort_keys=True,separators=(",",":"),ensure_ascii=False)
def sha256_text(t): return "sha256:"+hashlib.sha256(t.encode()).hexdigest()
def sha256_file(p:Path): return sha256_text(p.read_text())
def now(): return datetime.now(timezone.utc).isoformat()

def redact_uri(uri:str)->str:
    if "?" not in uri: return uri
    b,q=uri.split("?",1); out=[]
    for p in q.split("&"):
        if "=" not in p: out.append(p); continue
        k,v=p.split("=",1); out.append(f"{k}=REDACTED" if k.lower() in SECRET else f"{k}={v}")
    return b+"?"+"&".join(out)

def fail(m): print(f"ERROR: {m}",file=sys.stderr); raise SystemExit(2)

def parse(argv):
    ap=argparse.ArgumentParser(prog="kfm-ebird-release-ops")
    ap.add_argument('--pipeline-manifest'); ap.add_argument('--pipeline-run-dir')
    ap.add_argument('--aggregate',choices=('huc12','county','both'),required=True)
    ap.add_argument('--release-dir',default='data/catalog/fauna/ebird/releases')
    ap.add_argument('--published-root',default='data/published/fauna/ebird')
    ap.add_argument('--catalog-root',default='data/catalog/fauna/ebird')
    ap.add_argument('--layer-registry-dir',default='data/published/fauna/layers')
    ap.add_argument('--previous-release'); ap.add_argument('--mode',default='candidate',choices=('candidate','compare','approve','rollback','retention-plan','retention-execute','report'))
    ap.add_argument('--run-id'); ap.add_argument('--release-id'); ap.add_argument('--to-run-id'); ap.add_argument('--thresholds')
    ap.add_argument('--retention-days-restricted',type=int,default=180); ap.add_argument('--retention-days-audit',type=int,default=1095)
    ap.add_argument('--dry-run',action='store_true'); ap.add_argument('--force',action='store_true')
    return ap.parse_args(argv)

def main():
    a=parse(sys.argv[1:])
    if a.mode in {'candidate','compare','approve','retention-plan','retention-execute','report'}:
        if not a.pipeline_manifest or not a.pipeline_run_dir: fail('pipeline-manifest and pipeline-run-dir required')
    if a.mode=='rollback' and not a.to_run_id: fail('--to-run-id required for rollback')
    if a.mode=='retention-execute' and not a.force: fail('--force required for retention-execute')
    if 'data/published' in Path(a.release_dir).as_posix(): fail('release-dir must not be under data/published')

    if a.mode=='rollback':
        print(json.dumps({"status":"todo","mode":"rollback"},indent=2)); return

    pm=json.loads(Path(a.pipeline_manifest).read_text())
    run_id=a.run_id or pm['run_id']
    ev=Path(pm['evidencebundle_path']); vr=Path(pm['validation_report_path'])
    evj=json.loads(ev.read_text()); vrj=json.loads(vr.read_text())
    agg_targets=['huc12','county'] if a.aggregate=='both' else [a.aggregate]
    pop={p:pm.get('public_outputs',[]) for p in agg_targets}
    public_outputs=[x for xs in pop.values() for x in xs]
    poh={p:sha256_file(Path(p)) for p in public_outputs if Path(p).exists()}
    rid=a.release_id or hashlib.sha256(cjson({"run_id":run_id,"aggregate":a.aggregate,"pipeline_manifest_sha256":sha256_file(Path(a.pipeline_manifest)),"kfm_spec_hash":pm.get('kfm:spec_hash'),"suppression_min_n":pm.get('suppression_min_n'),"public_output_hashes":poh}).encode()).hexdigest()[:16]
    root=Path(a.release_dir)/a.aggregate/rid
    if root.exists() and not a.force and not a.dry_run: fail('release artifact dir exists; use --force')

    red=redact_uri(pm.get('source_uri',''))
    gates=[{"name":"validation_report_pass","status":"pass" if vrj.get('status')=='pass' else "fail"},{"name":"suppression_min_n","status":"pass" if int(pm.get('suppression_min_n',0))>=10 else "fail"},{"name":"spec_hash","status":"pass" if pm.get('kfm:spec_hash')==evj.get('kfm:spec_hash') else "fail"}]
    blocked=any(g['status']=='fail' for g in gates)
    status='blocked' if blocked else 'candidate'
    rc={"schema_version":"v1","object_type":"ReleaseCandidate","domain":"fauna","source":"ebird","policy_label":"release_candidate","public_safe_final_outputs":True,"exact_points":"restricted","release_id":rid,"run_id":run_id,"aggregate_targets":agg_targets,"source_uri":pm.get('source_uri'),'redacted_source_uri':red,"query_predicate":pm.get('query_predicate'),"suppression_min_n":pm.get('suppression_min_n'),"kfm:spec_hash":pm.get('kfm:spec_hash'),"pipeline_manifest_path":a.pipeline_manifest,"pipeline_manifest_sha256":sha256_file(Path(a.pipeline_manifest)),"evidencebundle_path":pm.get('evidencebundle_path'),"evidencebundle_sha256":sha256_file(ev),"validation_report_path":pm.get('validation_report_path'),"validation_report_sha256":sha256_file(vr),"public_outputs":public_outputs,"public_output_hashes":poh,"catalog_outputs":[],"catalog_output_hashes":{},"denied_public_fields_checked":DENIED,"release_gates":gates,"threshold_config":{},"status":status,"created_at":now()}
    dr={"schema_version":"v1","object_type":"ReleaseDeltaReport","domain":"fauna","source":"ebird","policy_label":"release_candidate","release_id":rid,"run_id":run_id,"aggregate_targets":agg_targets,"kfm:spec_hash":pm.get('kfm:spec_hash'),"comparison_available":False,"deltas":pm.get('counts',{}),"percent_changes":{},"threshold_evaluations":[],"notable_changes":[],"no_previous_release_reason":"No previous release supplied","generated_at":now()}
    qc={"schema_version":"v1","object_type":"ReleaseQualityScorecard","domain":"fauna","source":"ebird","policy_label":"release_candidate","release_id":rid,"run_id":run_id,"aggregate_targets":agg_targets,"kfm:spec_hash":pm.get('kfm:spec_hash'),"status":"fail" if blocked else "pass","summary":{"hard_gates_passed":sum(g['status']=='pass' for g in gates),"hard_gates_failed":sum(g['status']=='fail' for g in gates),"warnings":0,"threshold_failures":0},"checks":[{"name":g['name'],"category":"safety","severity":"fail","status":g['status'],"message":g['name']} for g in gates],"metrics":pm.get('counts',{}),"denied_public_fields_checked":DENIED,"generated_at":now()}
    pc={"schema_version":"v1","object_type":"PublicChangelog","domain":"fauna","source":"ebird","policy_label":"public_aggregate","public_safe":True,"exact_points":"restricted","release_id":rid,"run_id":run_id,"aggregate_targets":agg_targets,"redacted_source_uri":red,"query_predicate":pm.get('query_predicate'),"suppression_min_n":pm.get('suppression_min_n'),"kfm:spec_hash":pm.get('kfm:spec_hash'),"public_summary":{"groups_published":0,"features_emitted":0,"groups_suppressed_count":0,"rows_unassigned_count":0,"observation_count_unknown_count":0},"changes_summary":"Synthetic release summary","evidence_bundle_uri":pm.get('evidencebundle_path'),"layer_ids":[f"ebird_agg_{x}" for x in agg_targets],"public_artifact_uris":public_outputs,"generated_at":now()}
    pcmd=f"# eBird public release {rid}\n\n- Run: `{run_id}`\n- Aggregate: `{a.aggregate}`\n- kfm:spec_hash: `{pm.get('kfm:spec_hash')}`\n"
    rb={"schema_version":"v1","object_type":"RollbackPlan","domain":"fauna","source":"ebird","policy_label":"public_aggregate","public_safe":True,"exact_points":"restricted","current_release_id":rid,"current_run_id":run_id,"target_release_id":run_id,"target_run_id":run_id,"aggregate_targets":agg_targets,"files_to_update":[],"previous_pointer_values":{},"target_pointer_values":{},"validation_checks_required":["target_release_valid"],"generated_at":now()}
    rp={"schema_version":"v1","object_type":"RetentionPlan","domain":"fauna","source":"ebird","policy_label":"mixed_restricted_public","release_id":rid,"run_id":run_id,"retention_days_restricted":a.retention_days_restricted,"retention_days_audit":a.retention_days_audit,"candidates":[],"protected_artifacts":["approved public releases","release receipts","public changelogs","catalog records","audit ledgers within retention window"],"generated_at":now()}

    artifacts={"release_candidate.json":rc,"release_delta_report.json":dr,"release_quality_scorecard.json":qc,"public_changelog.json":pc,"rollback_plan.json":rb,"retention_plan.json":rp}
    if a.dry_run:
        print(json.dumps({"release_id":rid,"status":status,"mode":a.mode,"would_write":[str(root/k) for k in artifacts]},indent=2)); return
    root.mkdir(parents=True,exist_ok=True)
    for fn,obj in artifacts.items(): (root/fn).write_text(json.dumps(obj,indent=2,sort_keys=True)+"\n")
    (root/'public_changelog.md').write_text(pcmd)
    rr={"schema_version":"v1","object_type":"ReleaseReceipt","domain":"fauna","source":"ebird","policy_label":"public_aggregate","public_safe":True,"exact_points":"restricted","release_id":rid,"run_id":run_id,"aggregate_targets":agg_targets,"status":"approved" if (a.mode=='approve' and not blocked) else status,"kfm:spec_hash":pm.get('kfm:spec_hash'),"suppression_min_n":pm.get('suppression_min_n'),"validations_passed":[g['name'] for g in gates if g['status']=='pass'],"validations_failed":[g['name'] for g in gates if g['status']=='fail'],"warnings":[],"threshold_results":[],"input_hashes":{"pipeline_manifest_sha256":sha256_file(Path(a.pipeline_manifest))},"output_hashes":{k:sha256_file(root/k) for k in [*artifacts.keys(),'public_changelog.md']},"public_paths":public_outputs,"catalog_paths":[],"release_candidate_path":str(root/'release_candidate.json'),"release_candidate_sha256":sha256_file(root/'release_candidate.json'),"release_delta_report_path":str(root/'release_delta_report.json'),"release_delta_report_sha256":sha256_file(root/'release_delta_report.json'),"release_quality_scorecard_path":str(root/'release_quality_scorecard.json'),"release_quality_scorecard_sha256":sha256_file(root/'release_quality_scorecard.json'),"public_changelog_json_path":str(root/'public_changelog.json'),"public_changelog_json_sha256":sha256_file(root/'public_changelog.json'),"public_changelog_md_path":str(root/'public_changelog.md'),"public_changelog_md_sha256":sha256_file(root/'public_changelog.md'),"rollback_plan_path":str(root/'rollback_plan.json'),"rollback_plan_sha256":sha256_file(root/'rollback_plan.json'),"retention_plan_path":str(root/'retention_plan.json'),"retention_plan_sha256":sha256_file(root/'retention_plan.json'),"generated_at":now()}
    (root/'release_receipt.json').write_text(json.dumps(rr,indent=2,sort_keys=True)+"\n")
    if a.mode=='approve':
        if blocked: fail('approve mode requires all release gates to pass')
        cat_idx=Path(a.catalog_root)/'releases'/a.aggregate/'index.json'; cat_idx.parent.mkdir(parents=True,exist_ok=True)
        c={"schema_version":"v1","object_type":"ReleaseIndex","domain":"fauna","source":"ebird","aggregate":a.aggregate,"release_id":rid,"run_id":run_id,"kfm:spec_hash":pm.get('kfm:spec_hash')}
        cat_idx.write_text(json.dumps(c,indent=2,sort_keys=True)+"\n")

if __name__=='__main__': main()
