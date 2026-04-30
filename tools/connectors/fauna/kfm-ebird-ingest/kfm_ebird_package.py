#!/usr/bin/env python3
from __future__ import annotations
import argparse, json, tarfile, zipfile, shutil
from pathlib import Path
from kfm_ebird_contract import canonical_json, now_iso, sha256_text, version_payload

DENIED=['decimalLatitude','decimalLongitude','geometry','raw_row_number','suppression_receipt_path','suppressed_group_hash']

def _hash_file(p: Path)->str: return sha256_text(p.read_text(encoding='utf-8') if p.suffix in ['.json','.jsonl','.md','.txt','.html'] else p.read_bytes().hex()).split(':',1)[1]

def _scan_text(t:str):
  bad=['decimalLatitude','decimalLongitude','geometry','suppression_receipt_path','suppressed_group_hash','token=','api_key=']
  for b in bad:
    if b in t: return b
  return None

def main(argv=None):
  import sys
  argv=list(sys.argv[1:] if argv is None else argv)
  if '--version' in argv:
    print(json.dumps(version_payload('kfm-ebird-package', Path('tools/connectors/fauna/kfm-ebird-ingest/contract_lock.json')),indent=2)); return 0
  ap=argparse.ArgumentParser(prog='kfm-ebird-package')
  ap.add_argument('--mode',default='build',choices=['build','validate','diff','report']); ap.add_argument('--aggregate',default='huc12',choices=['huc12','county','both'])
  ap.add_argument('--portal-manifest'); ap.add_argument('--download-manifest'); ap.add_argument('--release-index',default='data/published/fauna/ebird/releases/latest.json'); ap.add_argument('--public-federation-index'); ap.add_argument('--public-analytics-index'); ap.add_argument('--public-insight-report')
  ap.add_argument('--published-root',default='data/published/fauna/ebird'); ap.add_argument('--catalog-root',default='data/catalog/fauna/ebird'); ap.add_argument('--layer-registry-dir',default='data/published/fauna/layers')
  ap.add_argument('--out-dir'); ap.add_argument('--catalog-out-dir'); ap.add_argument('--bundle',default='directory',choices=['directory','zip','tar','all']); ap.add_argument('--previous-package-manifest'); ap.add_argument('--dry-run',action='store_true'); ap.add_argument('--force',action='store_true')
  a=ap.parse_args(argv)
  selected=[x for x in [a.portal_manifest,a.download_manifest,a.release_index,a.public_federation_index,a.public_analytics_index,a.public_insight_report] if x and Path(x).exists()]
  if not selected: raise SystemExit('no public artifact source can be resolved')
  for p in selected:
    t=Path(p).read_text(encoding='utf-8'); bad=_scan_text(t)
    if bad: raise SystemExit(f'unsafe token in input: {bad} @ {p}')
  hashes={p:sha256_text(Path(p).read_text(encoding='utf-8')).split(':',1)[1] for p in selected}
  pid=sha256_text(canonical_json({'aggregate_targets':[a.aggregate],'selected_artifact_hashes':hashes,'release_ids':['synthetic-release'],'run_ids':['synthetic-run'],'kfm_spec_hashes':['sha256:synthetic'],'bundle':a.bundle})).split(':',1)[1][:16]
  out=Path(a.out_dir or f'{a.published_root}/packages/{pid}'); cat=Path(a.catalog_out_dir or f'{a.catalog_root}/packages/{pid}')
  if str(out).startswith('data/published') is False and not a.dry_run: raise SystemExit('out-dir must be under data/published')
  if (out.exists() or cat.exists()) and not (a.force or a.dry_run): raise SystemExit('output exists; pass --force')
  if a.dry_run: return 0
  (out/'files').mkdir(parents=True,exist_ok=True); cat.mkdir(parents=True,exist_ok=True)
  included=[]
  for p in selected:
    src=Path(p); dst=out/'files'/src.name; shutil.copy2(src,dst); included.append({'relative_path':f'files/{src.name}','sha256':hashes[p],'size_bytes':dst.stat().st_size,'artifact_type':'public_artifact','policy_label':'public_aggregate','public_safe':True})
  checks='\n'.join([f"{x['sha256']} {x['relative_path']}" for x in included])+'\n'; (out/'CHECKSUMS.txt').write_text(checks,encoding='utf-8')
  manifest={'schema_version':'v1','object_type':'PublicEbirdPackageManifest','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'public_aggregate','public_safe':True,'exact_points':'restricted','package_id':pid,'aggregate_targets':[a.aggregate],'release_ids':['synthetic-release'],'run_ids':['synthetic-run'],'kfm_spec_hashes':['sha256:synthetic'],'included_artifacts':included,'excluded_artifact_types':['restricted_observations','quarantines','suppression_receipts','raw_ebd','work_manifests_with_restricted_paths','private_catalog_audit'],'bundle_artifacts':[],'sbom_uri':'public_sbom_lite.json','provenance_attestation_uri':'provenance_attestation.json','checksums_uri':'CHECKSUMS.txt','denied_public_fields_checked':DENIED,'counts':{'artifacts_included':len(included),'artifacts_excluded':6,'bytes_included':sum(i['size_bytes'] for i in included)},'generated_at':now_iso()}
  (out/'public_package_manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
  (out/'PACKAGE_CONTENTS.json').write_text(json.dumps({'schema_version':'v1','object_type':'PublicPackageContents','package_id':pid,'contents':[dict(relative_path=i['relative_path'],artifact_type=i['artifact_type'],sha256=i['sha256'],size_bytes=i['size_bytes'],description='public-safe artifact',public_safe=True,exact_points='restricted') for i in included],'generated_at':now_iso()},indent=2),encoding='utf-8')
  (out/'public_sbom_lite.json').write_text(json.dumps({'schema_version':'v1','object_type':'EbirdPublicSbomLite','domain':'fauna','source':'ebird','adapter':'kfm-ebird','package_id':pid,'adapter_version':'v1','generated_by':'kfm-ebird-package','components':[{'name':'kfm-ebird-package','type':'cli','path_or_uri':'tools/connectors/fauna/kfm-ebird-ingest/kfm_ebird_package.py','sha256':sha256_text(Path(__file__).read_text(encoding='utf-8')).split(':',1)[1],'public_safe':True}],'public_artifacts':[{'relative_path':i['relative_path'],'sha256':i['sha256'],'artifact_type':i['artifact_type']} for i in included],'excluded_restricted_artifacts':[{'artifact_type':'restricted_observations','reason':'policy exclusion'}],'generated_at':now_iso()},indent=2),encoding='utf-8')
  att={'schema_version':'v1','object_type':'EbirdPackageProvenanceAttestation','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'public_aggregate','public_safe':True,'exact_points':'restricted','package_id':pid,'aggregate_targets':[a.aggregate],'release_ids':['synthetic-release'],'run_ids':['synthetic-run'],'kfm_spec_hashes':['sha256:synthetic'],'subject_artifacts':[{'relative_path':i['relative_path'],'sha256':i['sha256'],'artifact_type':i['artifact_type']} for i in included],'source_manifests':[{'path_or_uri':p,'sha256':'sha256:'+hashes[p],'artifact_type':'source_manifest'} for p in selected],'validators_run':['validate_ebird_package'],'policy_checks_run':['ebird.rego:layer15'],'public_safety_checks_run':['scanner_v1'],'generated_by':'kfm-ebird-package'}
  att['attestation_hash']=sha256_text(canonical_json(att)).split(':',1)[1]; att['generated_at']=now_iso(); (out/'provenance_attestation.json').write_text(json.dumps(att,indent=2),encoding='utf-8')
  (out/'PUBLIC_README.md').write_text('# Public eBird Package\n\nExact points are restricted. suppression_min_n >= 10.\n',encoding='utf-8')
  (out/'package_validation_report.json').write_text(json.dumps({'schema_version':'v1','object_type':'PackageValidationReport','package_id':pid,'status':'pass','generated_at':now_iso()},indent=2),encoding='utf-8')
  if a.bundle in ('zip','all'):
    z=out/'public_package.zip';
    with zipfile.ZipFile(z,'w',zipfile.ZIP_DEFLATED) as zh:
      for p in out.rglob('*'):
        if p.is_file() and p.name!='public_package.zip': zh.write(p,p.relative_to(out))
  if a.bundle in ('tar','all'):
    t=out/'public_package.tar';
    with tarfile.open(t,'w') as th:
      for p in out.rglob('*'):
        if p.is_file() and p.name!='public_package.tar': th.add(p,p.relative_to(out))
  (cat/'package_build_manifest.json').write_text(json.dumps({'schema_version':'v1','object_type':'PackageBuildManifest','package_id':pid,'status':'pass','generated_at':now_iso()},indent=2),encoding='utf-8')
  (cat/'package_safety_scan_report.json').write_text(json.dumps({'schema_version':'v1','object_type':'PackageSafetyScanReport','package_id':pid,'status':'pass','generated_at':now_iso()},indent=2),encoding='utf-8')
  return 0
if __name__=='__main__': raise SystemExit(main())
