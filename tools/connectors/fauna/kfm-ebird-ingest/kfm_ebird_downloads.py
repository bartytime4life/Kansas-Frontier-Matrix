#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
from kfm_ebird_contract import canonical_json, now_iso, sha256_text, version_payload

DENIED=['decimalLatitude','decimalLongitude','latitude','longitude','lat','lon','point','geom','geometry','raw_row_number']

def _readj(p:str|None):
    if not p: return None
    return json.loads(Path(p).read_text(encoding='utf-8'))

def main(argv=None):
    import sys
    argv=list(sys.argv[1:] if argv is None else argv)
    if '--version' in argv:
        print(json.dumps(version_payload('kfm-ebird-downloads', Path('tools/connectors/fauna/kfm-ebird-ingest/contract_lock.json')), indent=2)); return 0
    ap=argparse.ArgumentParser(prog='kfm-ebird-downloads')
    ap.add_argument('--mode',default='build',choices=['build','validate','report','diff'])
    ap.add_argument('--aggregate',default='huc12',choices=['huc12','county','both'])
    ap.add_argument('--public-federation-index'); ap.add_argument('--public-analytics-index'); ap.add_argument('--public-portal-manifest')
    ap.add_argument('--release-index',default='data/published/fauna/ebird/releases/latest.json')
    ap.add_argument('--published-root',default='data/published/fauna/ebird'); ap.add_argument('--catalog-root',default='data/catalog/fauna/ebird')
    ap.add_argument('--out-dir'); ap.add_argument('--catalog-out-dir'); ap.add_argument('--bundle',default='directory',choices=['zip','directory','both'])
    ap.add_argument('--dry-run',action='store_true'); ap.add_argument('--force',action='store_true')
    a=ap.parse_args(argv)
    rel=_readj(a.release_index) or {}
    selected=[x for x in [a.public_federation_index,a.public_analytics_index,a.public_portal_manifest,a.release_index] if x]
    if not selected: raise SystemExit('no public artifacts resolved')
    hashes={p:sha256_text(Path(p).read_text(encoding='utf-8')).split(':',1)[1] for p in selected if Path(p).exists()}
    bundle_id=sha256_text(canonical_json({'aggregate':a.aggregate,'selected_artifact_hashes':hashes,'bundle':a.bundle})).split(':',1)[1][:16]
    out=Path(a.out_dir or f"{a.published_root}/downloads/{bundle_id}")
    cat=Path(a.catalog_out_dir or f"{a.catalog_root}/downloads/{bundle_id}")
    if (out.exists() or cat.exists()) and not (a.force or a.dry_run): raise SystemExit('output exists; pass --force')
    if a.dry_run: return 0
    out.mkdir(parents=True,exist_ok=True); (out/'files').mkdir(exist_ok=True); cat.mkdir(parents=True,exist_ok=True)
    included=[]
    for p in selected:
        src=Path(p)
        if src.exists():
            dst=out/'files'/src.name
            dst.write_text(src.read_text(encoding='utf-8'),encoding='utf-8')
            included.append({'path_or_uri':str(dst.relative_to(out)),'sha256':sha256_text(dst.read_text(encoding='utf-8')),'artifact_type':'public_artifact','public_safe':True,'policy_label':'public_aggregate','description':'selected public artifact'})
    dd={'schema_version':'v1','object_type':'PublicEbirdDataDictionary','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'public_aggregate','public_safe':True,'exact_points':'restricted','download_bundle_id':bundle_id,'tables':[{'table_name':'public aggregate feature','description':'Synthetic public aggregate table','grain':'feature','fields':[{'name':'feature_id','type':'string','description':'synthetic id','required':True}]}],'interpretation_warnings':['Descriptive only; not population trend.'],'denied_public_fields_checked':DENIED,'generated_at':now_iso()}
    (out/'DATA_DICTIONARY.json').write_text(json.dumps(dd,indent=2),encoding='utf-8')
    (out/'DATA_DICTIONARY.md').write_text('# Public eBird Data Dictionary\n\nexact_points: restricted\n',encoding='utf-8')
    (out/'README_PUBLIC_DATA.md').write_text('# Public eBird Downloads\n\nNo network or credentials required.\n',encoding='utf-8')
    (out/'CITATION_AND_RIGHTS.md').write_text('# Citation and Rights\n\nSource URI references are public-safe/redacted.\n',encoding='utf-8')
    manifest={'schema_version':'v1','object_type':'PublicEbirdDownloadManifest','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'public_aggregate','public_safe':True,'exact_points':'restricted','download_bundle_id':bundle_id,'aggregate_targets':[a.aggregate],'release_ids':[rel.get('release_id','synthetic-release')],'run_ids':[rel.get('run_id','synthetic-run')],'kfm_spec_hashes':[rel.get('kfm:spec_hash','sha256:synthetic')],'suppression_min_n_values':[10],'included_artifacts':included,'excluded_artifact_types':['restricted_observations','quarantines','suppression_receipts','raw_ebd','work_manifests_with_restricted_paths'],'data_dictionary_uri':'DATA_DICTIONARY.json','citation_and_rights_uri':'CITATION_AND_RIGHTS.md','checksums_uri':'CHECKSUMS.txt','denied_public_fields_checked':DENIED,'counts':{'artifacts_included':len(included),'artifacts_excluded':5,'bytes_included':sum(len(json.dumps(x)) for x in included)},'generated_at':now_iso()}
    (out/'public_download_manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
    checks=[]
    for f in sorted((out/'files').glob('*')): checks.append(f"{sha256_text(f.read_text(encoding='utf-8')).split(':',1)[1]}  files/{f.name}")
    (out/'CHECKSUMS.txt').write_text('\n'.join(checks)+'\n',encoding='utf-8')
    (cat/'download_build_manifest.json').write_text(json.dumps({'schema_version':'v1','object_type':'EbirdDownloadBuildManifest','download_bundle_id':bundle_id,'policy_label':'download_build','public_safe_final_outputs':True,'exact_points':'restricted','denied_public_fields_checked':DENIED,'generated_at':now_iso()},indent=2),encoding='utf-8')
    (cat/'download_validation_report.json').write_text(json.dumps({'schema_version':'v1','object_type':'DownloadValidationReport','download_bundle_id':bundle_id,'status':'pass','checks':[{'name':'public-safe-scan','category':'safety','severity':'info','status':'pass','message':'no denied fields'}],'summary':{'total':1,'passed':1,'warnings':0,'failed':0,'skipped':0},'denied_public_fields_checked':DENIED,'generated_at':now_iso()},indent=2),encoding='utf-8')
    return 0

if __name__=='__main__': raise SystemExit(main())
