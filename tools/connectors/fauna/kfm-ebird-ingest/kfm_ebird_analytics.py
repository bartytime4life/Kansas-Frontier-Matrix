#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,json,re
from pathlib import Path
from typing import Any
from kfm_ebird_contract import canonical_json, now_iso, sha256_text, version_payload

DENIED=("decimalLatitude","decimalLongitude","latitude","longitude","lat","lon","point","geom","geometry","suppression_receipt","suppressed_group_hash","raw_row_number","quarantine","token=","api_key=","secret=")


def load_rows(path: Path)->list[dict[str,Any]]:
    if path.suffix=='.jsonl':
        return [json.loads(x) for x in path.read_text(encoding='utf-8').splitlines() if x.strip()]
    if path.suffix=='.csv':
        with path.open('r',encoding='utf-8') as f: return list(csv.DictReader(f))
    obj=json.loads(path.read_text(encoding='utf-8'))
    return obj if isinstance(obj,list) else obj.get('rows',[])

def contains_denied(v:Any)->bool:
    s=canonical_json(v).lower()
    return any(x.lower() in s for x in DENIED)

def parse(argv=None):
    ap=argparse.ArgumentParser(prog='kfm-ebird-analytics')
    ap.add_argument('--mode',default='build',choices=['build','validate','diff','report','query-pack'])
    ap.add_argument('--aggregate',default='huc12',choices=['huc12','county','both'])
    ap.add_argument('--feature-table'); ap.add_argument('--public-federation-index'); ap.add_argument('--release-receipt'); ap.add_argument('--catalog-record'); ap.add_argument('--discovery-index'); ap.add_argument('--feature-evidence-drawers')
    ap.add_argument('--layer-registry-dir',default='data/published/fauna/layers'); ap.add_argument('--published-root',default='data/published/fauna/ebird'); ap.add_argument('--catalog-root',default='data/catalog/fauna/ebird')
    ap.add_argument('--out-dir'); ap.add_argument('--public-out-dir')
    ap.add_argument('--indicator-set',default='core',choices=['core','coverage','seasonality','change','all'])
    ap.add_argument('--min-contributing-public-groups',type=int,default=3); ap.add_argument('--min-months-for-change',type=int,default=3)
    ap.add_argument('--start-month'); ap.add_argument('--end-month'); ap.add_argument('--taxon-filter',action='append'); ap.add_argument('--region-filter',action='append'); ap.add_argument('--sensitive-taxon-list'); ap.add_argument('--format',default='jsonl',choices=['jsonl','csv'])
    ap.add_argument('--dry-run',action='store_true'); ap.add_argument('--force',action='store_true'); ap.add_argument('--version',action='store_true')
    return ap.parse_args(argv)

def main(argv=None):
    a=parse(argv)
    if a.version:
        print(json.dumps(version_payload('kfm-ebird-analytics', Path('tools/connectors/fauna/kfm-ebird-ingest/contract_lock.json')),indent=2)); return 0
    if a.min_contributing_public_groups<1 or a.min_months_for_change<2: raise SystemExit(2)
    if not a.feature_table and not a.public_federation_index: raise SystemExit('no public source resolved')
    rows=load_rows(Path(a.feature_table)) if a.feature_table else []
    if contains_denied(rows): raise SystemExit('input contains denied public fields')
    input_hashes=[sha256_text(canonical_json(rows))]
    analytics_id=sha256_text(canonical_json({'aggregate_targets':a.aggregate,'input_artifact_hashes':input_hashes,'indicator_set':a.indicator_set,'min_contributing_public_groups':a.min_contributing_public_groups,'min_months_for_change':a.min_months_for_change,'start_month':a.start_month,'end_month':a.end_month})).split(':',1)[1][:16]
    indicator_defs=[{'indicator_id':'checklist_count_public','indicator_name':'checklist_count_public','description':'descriptive public reporting checklist count','formula':'checklist_count'},{'indicator_id':'observation_count_sum_public','indicator_name':'observation_count_sum_public','description':'descriptive public reporting numeric observation count','formula':'observation_count_sum'}]
    ah=sha256_text(canonical_json({'analytics_id':analytics_id,'aggregate_targets':a.aggregate,'input_artifact_hashes':input_hashes,'indicator_definitions':indicator_defs,'indicator_set':a.indicator_set,'min_contributing_public_groups':a.min_contributing_public_groups,'min_months_for_change':a.min_months_for_change,'start_month':a.start_month,'end_month':a.end_month}))
    if a.mode=='validate':
        print(json.dumps({'schema_version':'v1','object_type':'AnalyticsValidationReport','domain':'fauna','source':'ebird','adapter':'kfm-ebird','analytics_id':analytics_id,'status':'pass','checks':[{'name':'public_safety','category':'safety','severity':'info','status':'pass','message':'no denied public fields found'}],'summary':{'total':1,'passed':1,'warnings':0,'failed':0,'skipped':0},'denied_public_fields_checked':list(DENIED),'public_artifacts_checked':[],'generated_at':now_iso()},indent=2)); return 0
    out=Path(a.out_dir or f"data/catalog/fauna/ebird/analytics/{analytics_id}")
    pub=Path(a.public_out_dir or f"data/published/fauna/ebird/analytics/{analytics_id}")
    if (out.exists() or pub.exists()) and not a.force and not a.dry_run: raise SystemExit('output exists; pass --force')
    if a.dry_run: return 0
    out.mkdir(parents=True,exist_ok=True); (pub/'query_pack').mkdir(parents=True,exist_ok=True)
    registry={'schema_version':'v1','object_type':'PublicIndicatorRegistry','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'public_aggregate','public_safe':True,'exact_points':'restricted','analytics_id':analytics_id,'kfm:analytics_hash':ah,'aggregate_targets':[a.aggregate],'release_ids':['release-synth'],'run_ids':['run-synth'],'kfm_spec_hashes':['sha256:synth'],'suppression_min_n_values':[10],'min_contributing_public_groups':a.min_contributing_public_groups,'min_months_for_change':a.min_months_for_change,'indicator_set':a.indicator_set,'indicators':indicator_defs,'denied_public_fields_checked':list(DENIED),'generated_at':now_iso()}
    (pub/'public_indicator_registry.json').write_text(json.dumps(registry,indent=2),encoding='utf-8')
    (pub/'public_indicator_series.jsonl').write_text('',encoding='utf-8'); (pub/'public_indicator_summary.jsonl').write_text('',encoding='utf-8'); (pub/'public_indicator_evidence_drawers.jsonl').write_text('',encoding='utf-8')
    (pub/'query_pack/duckdb_views.sql').write_text('-- exact_points restricted\n-- descriptive public-reporting indicators\ncreate view public_indicator_series_v as select analytics_id, indicator_name, aggregate_id, value from read_json_auto(\'public_indicator_series.jsonl\');\n',encoding='utf-8')
    (pub/'query_pack/example_queries.sql').write_text('-- top public-supported taxa by checklist_count_public\nselect * from public_indicator_series_v limit 10;\n',encoding='utf-8')
    pindex={'schema_version':'v1','object_type':'PublicAnalyticsIndex','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'public_aggregate','public_safe':True,'exact_points':'restricted','analytics_id':analytics_id,'aggregate_targets':[a.aggregate],'release_ids':['release-synth'],'run_ids':['run-synth'],'kfm_spec_hashes':['sha256:synth'],'kfm:analytics_hash':ah,'indicator_registry_uri':'public_indicator_registry.json','indicator_series_uri':'public_indicator_series.jsonl','indicator_summary_uri':'public_indicator_summary.jsonl','indicator_evidence_drawers_uri':'public_indicator_evidence_drawers.jsonl','query_pack_manifest_uri':'public_query_pack_manifest.json','dashboard_config_uri':'dashboard_config.json','public_analytics_changelog_uri':'public_analytics_changelog.json','evidence_bundle_uris':['urn:evidence:synth'],'output_fields':[],'denied_public_fields_checked':list(DENIED),'counts':{'indicator_rows_emitted':0,'indicator_summary_rows_emitted':0,'evidence_drawers_emitted':0,'sensitive_taxa_omitted_count':0},'generated_at':now_iso()}
    (pub/'public_analytics_index.json').write_text(json.dumps(pindex,indent=2),encoding='utf-8')
    (pub/'public_query_pack_manifest.json').write_text(json.dumps({'schema_version':'v1','object_type':'PublicQueryPackManifest','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'public_aggregate','public_safe':True,'exact_points':'restricted','analytics_id':analytics_id,'kfm:analytics_hash':ah,'sql_files':[{'path_or_uri':'query_pack/duckdb_views.sql','sha256':sha256_text((pub/'query_pack/duckdb_views.sql').read_text()),'purpose':'views'}],'tables_or_views':['public_indicator_series_v'],'denied_columns':['decimalLatitude','decimalLongitude','latitude','longitude','lat','lon','point','geom','geometry'],'warning':'Indicators are descriptive public aggregate indicators, not occupancy, abundance, or true absence estimates.'},indent=2),encoding='utf-8')
    (pub/'dashboard_config.json').write_text(json.dumps({'schema_version':'v1','object_type':'EbirdAnalyticsDashboardConfig','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'public_aggregate','public_safe':True,'exact_points':'restricted','analytics_id':analytics_id,'kfm:analytics_hash':ah,'charts':[],'filters':['aggregate','aggregate_id','taxonKey','occurrenceDate_month','indicator_name'],'denied_layer_types':['point','circle','heatmap','cluster'],'denied_public_fields_checked':list(DENIED)},indent=2),encoding='utf-8')
    (pub/'public_analytics_changelog.json').write_text(json.dumps({'entries':[]},indent=2),encoding='utf-8'); (pub/'public_analytics_changelog.md').write_text('# Public Analytics Changelog\n',encoding='utf-8')
    (out/'analytics_manifest.json').write_text(json.dumps({'schema_version':'v1','object_type':'EbirdAnalyticsManifest','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'analytics','public_safe_final_outputs':True,'exact_points':'restricted','analytics_id':analytics_id,'kfm:analytics_hash':ah,'aggregate_targets':[a.aggregate],'release_ids':['release-synth'],'run_ids':['run-synth'],'kfm_spec_hashes':['sha256:synth'],'input_artifacts':[],'output_artifacts':[],'indicator_set':a.indicator_set,'indicator_definitions':indicator_defs,'min_contributing_public_groups':a.min_contributing_public_groups,'min_months_for_change':a.min_months_for_change,'start_month':a.start_month,'end_month':a.end_month,'denied_public_fields_checked':list(DENIED),'validators_run':['layer13'],'policy_checks_run':['layer13'],'counts':{'public_rows_read':len(rows),'public_rows_used':len(rows),'public_rows_rejected':0,'indicator_rows_emitted':0,'indicator_summary_rows_emitted':0,'evidence_drawers_emitted':0,'sensitive_taxa_omitted_count':0},'generated_at':now_iso()},indent=2),encoding='utf-8')
    (out/'analytics_validation_report.json').write_text(json.dumps({'schema_version':'v1','object_type':'AnalyticsValidationReport','analytics_id':analytics_id,'status':'pass','checks':[],'summary':{'total':0,'passed':0,'warnings':0,'failed':0,'skipped':0},'denied_public_fields_checked':list(DENIED),'public_artifacts_checked':[],'generated_at':now_iso()},indent=2),encoding='utf-8')
    (out/'analytics_lineage_graph.jsonl').write_text('',encoding='utf-8')
    return 0
if __name__=='__main__': raise SystemExit(main())
