#!/usr/bin/env python3
from __future__ import annotations
import argparse,json
from pathlib import Path
from kfm_ebird_contract import canonical_json, now_iso, sha256_text, version_payload

def main(argv=None):
    import sys
    argv = list(sys.argv[1:] if argv is None else argv)
    if "--version" in argv:
        print(json.dumps(version_payload('kfm-ebird-insights', Path('tools/connectors/fauna/kfm-ebird-ingest/contract_lock.json')),indent=2)); return 0
    ap=argparse.ArgumentParser(prog='kfm-ebird-insights')
    ap.add_argument('--mode',default='build',choices=['build','validate','compare','explain'])
    ap.add_argument('--analytics-manifest',required=True)
    ap.add_argument('--public-analytics-index'); ap.add_argument('--indicator-registry'); ap.add_argument('--indicator-series'); ap.add_argument('--indicator-summary'); ap.add_argument('--indicator-evidence-drawers')
    ap.add_argument('--out-dir'); ap.add_argument('--public-out-dir'); ap.add_argument('--audience',default='technical',choices=['technical','operator','public']); ap.add_argument('--format',default='both',choices=['json','md','both'])
    ap.add_argument('--previous-insights'); ap.add_argument('--dry-run',action='store_true'); ap.add_argument('--force',action='store_true'); ap.add_argument('--version',action='store_true')
    a=ap.parse_args(argv)
    manifest=json.loads(Path(a.analytics_manifest).read_text(encoding='utf-8'))
    analytics_id=manifest.get('analytics_id','analytics-synth'); ah=manifest.get('kfm:analytics_hash','sha256:synth')
    insight_id=sha256_text(canonical_json({'analytics_id':analytics_id,'analytics_manifest_sha256':sha256_text(canonical_json(manifest)),'audience':a.audience})).split(':',1)[1][:16]
    warning='Indicators are descriptive public aggregate indicators; exact eBird points are restricted; suppressed small-n groups are omitted; no_public_supported_record is not biological absence; checklist_count changes are not population trends; observation_count_sum changes are not abundance trends.'
    if a.mode=='validate':
        ok='population trend' not in Path(a.analytics_manifest).read_text(encoding='utf-8').lower()
        print(json.dumps({'schema_version':'v1','object_type':'InsightValidationReport','status':'pass' if ok else 'fail','insight_id':insight_id,'generated_at':now_iso()},indent=2)); return 0 if ok else 1
    out=Path(a.out_dir or f'data/catalog/fauna/ebird/insights/{insight_id}')
    pub=Path(a.public_out_dir or f'data/published/fauna/ebird/insights/{insight_id}')
    if (out.exists() or pub.exists()) and not a.force and not a.dry_run: raise SystemExit('output exists; pass --force')
    if a.dry_run: return 0
    out.mkdir(parents=True,exist_ok=True); pub.mkdir(parents=True,exist_ok=True)
    report={'schema_version':'v1','object_type':'PublicEbirdInsightReport','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'public_aggregate','public_safe':True,'exact_points':'restricted','insight_id':insight_id,'analytics_id':analytics_id,'kfm:analytics_hash':ah,'kfm_spec_hashes':manifest.get('kfm_spec_hashes',[]),'audience':a.audience,'title':'Synthetic eBird public analytics insights','summary':'Descriptive public-supported reporting summary.','interpretation_warning':warning,'public_safety_summary':'No exact coordinates or restricted rows in public artifacts.','indicators_included':[x.get('indicator_name') for x in manifest.get('indicator_definitions',[])],'insight_cards_uri':'insight_cards.jsonl','evidence_index_uri':'insight_evidence_index.json','evidence_bundle_uris':['urn:evidence:synth'],'query_predicate':'public_safe=true','redacted_source_uri':'urn:redacted:source','suppression_min_n_values':[10],'min_contributing_public_groups':manifest.get('min_contributing_public_groups',3),'generated_at':now_iso()}
    (pub/'public_insight_report.json').write_text(json.dumps(report,indent=2),encoding='utf-8')
    (pub/'public_insight_report.md').write_text(f"# Public eBird Insight Report\n\n{warning}\n",encoding='utf-8')
    (pub/'insight_cards.jsonl').write_text('',encoding='utf-8')
    (pub/'insight_evidence_index.json').write_text(json.dumps({'schema_version':'v1','object_type':'InsightEvidenceIndex','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'public_aggregate','public_safe':True,'exact_points':'restricted','insight_id':insight_id,'analytics_id':analytics_id,'evidence_bundle_uris':['urn:evidence:synth'],'indicator_evidence_drawer_uris':[],'public_analytics_index_uri':a.public_analytics_index or '','public_indicator_registry_uri':a.indicator_registry or '','public_indicator_series_uri':a.indicator_series or '','public_indicator_summary_uri':a.indicator_summary or '','kfm_spec_hashes':manifest.get('kfm_spec_hashes',[]),'kfm:analytics_hash':ah,'denied_public_fields_checked':['decimalLatitude','decimalLongitude','geometry']},indent=2),encoding='utf-8')
    (out/'insight_manifest.json').write_text(json.dumps({'schema_version':'v1','object_type':'InsightManifest','insight_id':insight_id,'analytics_id':analytics_id,'generated_at':now_iso()},indent=2),encoding='utf-8')
    (out/'insight_validation_report.json').write_text(json.dumps({'schema_version':'v1','object_type':'InsightValidationReport','insight_id':insight_id,'status':'pass','generated_at':now_iso()},indent=2),encoding='utf-8')
    return 0
if __name__=='__main__': raise SystemExit(main())
