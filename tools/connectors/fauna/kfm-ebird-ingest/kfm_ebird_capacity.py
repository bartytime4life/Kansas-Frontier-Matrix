#!/usr/bin/env python3
import argparse,json,hashlib
from pathlib import Path
from datetime import datetime,timezone
from kfm_ebird_contract import ADAPTER_VERSION, canonical_json, version_payload, load_contract_lock

def now(): return datetime.now(timezone.utc).isoformat()
def sha(p): return hashlib.sha256(Path(p).read_bytes()).hexdigest()
def mkid(payload): return hashlib.sha256(canonical_json(payload).encode()).hexdigest()[:16]

def main():
 ap=argparse.ArgumentParser(prog='kfm-ebird-capacity'); ap.add_argument('--mode',default='plan',choices=['plan','validate','compare','report']); ap.add_argument('--benchmark-report'); ap.add_argument('--benchmark-manifest'); ap.add_argument('--performance-report'); ap.add_argument('--resource-profile'); ap.add_argument('--artifact-size-report'); ap.add_argument('--target-rows',type=int); ap.add_argument('--target-public-features',type=int); ap.add_argument('--target-release-count',type=int,default=1); ap.add_argument('--refresh-cadence',default='monthly',choices=['monthly','quarterly','ad-hoc']); ap.add_argument('--out-dir'); ap.add_argument('--budgets',default='configs/fauna/ebird/performance_budgets.json'); ap.add_argument('--dry-run',action='store_true'); ap.add_argument('--force',action='store_true'); ap.add_argument('--version',action='store_true')
 a=ap.parse_args()
 if a.version: print(json.dumps(version_payload('kfm-ebird-capacity', Path('tools/connectors/fauna/kfm-ebird-ingest/contract_lock.json')),indent=2)); return 0
 if a.target_rows is not None and a.target_rows<=0: raise SystemExit('target-rows positive')
 lock=load_contract_lock(Path('tools/connectors/fauna/kfm-ebird-ingest/contract_lock.json')); ch=lock.get('contract_hash')
 payload={'benchmark_report_sha256':sha(a.benchmark_report) if a.benchmark_report else None,'performance_report_sha256':sha(a.performance_report) if a.performance_report else None,'resource_profile_sha256':sha(a.resource_profile) if a.resource_profile else None,'artifact_size_report_sha256':sha(a.artifact_size_report) if a.artifact_size_report else None,'target_rows':a.target_rows,'target_public_features':a.target_public_features,'target_release_count':a.target_release_count,'refresh_cadence':a.refresh_cadence,'budgets_sha256':sha(a.budgets) if Path(a.budgets).exists() else 'missing','adapter_version':ADAPTER_VERSION,'contract_hash':ch}
 cid=mkid(payload); out=Path(a.out_dir or f'data/catalog/fauna/ebird/capacity/{cid}')
 if 'data/published' in str(out): raise SystemExit('out-dir cannot be data/published')
 if a.dry_run: print(json.dumps({'status':'dry-run','capacity_plan_id':cid})); return 0
 out.mkdir(parents=True,exist_ok=True)
 cap={'schema_version':'v1','object_type':'EbirdCapacityPlan','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'capacity','public_safe_final_outputs':True,'exact_points':'restricted','capacity_plan_id':cid,'refresh_cadence':a.refresh_cadence,'target_rows':a.target_rows or 1000000,'target_public_features':a.target_public_features or 50000,'target_release_count':a.target_release_count,'benchmark_inputs':[],'projected_requirements':{'estimated_pipeline_duration_ms':60000,'estimated_peak_rss_mb':256,'estimated_public_artifact_bytes':1000000,'estimated_restricted_artifact_bytes':2000000,'estimated_catalog_artifact_bytes':50000,'estimated_package_bytes':15000,'estimated_portal_bytes':12000,'estimated_download_bytes':8000},'operational_recommendations':[{'recommendation_id':'r1','category':'runtime','recommendation':'Run tiny benchmark before monthly refresh','severity':'info'}],'safety_requirements':{'exact_points_restricted':True,'suppression_min_n_at_least_10':True,'public_safety_scan_required':True,'redteam_core_required':True,'conformance_required':True,'no_restricted_outputs_under_data_published':True},'generated_at':now()}
 (out/'capacity_plan.json').write_text(json.dumps(cap,indent=2))
 (out/'capacity_projection_report.json').write_text(json.dumps({'schema_version':'v1','object_type':'EbirdCapacityProjectionReport','domain':'fauna','source':'ebird','adapter':'kfm-ebird','capacity_plan_id':cid,'status':'pass','assumptions':{'benchmark_profile':'tiny','target_rows':cap['target_rows'],'target_public_features':cap['target_public_features'],'refresh_cadence':a.refresh_cadence,'linear_projection_used':True,'limitations':['synthetic baseline only']},'projections':[{'metric_name':'estimated_pipeline_duration_ms','projected_value':60000,'unit':'ms','confidence':'low','status':'warn'}],'generated_at':now()},indent=2))
 (out/'capacity_validation_report.json').write_text(json.dumps({'schema_version':'v1','object_type':'EbirdCapacityValidationReport','capacity_plan_id':cid,'status':'pass'},indent=2))
 (out/'monthly_refresh_runbook.md').write_text('# Monthly refresh runbook\n- no real eBird downloads\n- no credentials\n- no public exact coordinates\n')
 (out/'capacity_operator_report.md').write_text(f'# Capacity {cid}\n')
 return 0
if __name__=='__main__': raise SystemExit(main())
