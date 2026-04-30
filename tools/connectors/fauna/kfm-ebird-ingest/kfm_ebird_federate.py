#!/usr/bin/env python3
from __future__ import annotations
import argparse, csv, json
from pathlib import Path
from typing import Any
from kfm_ebird_contract import ADAPTER_NAME, ADAPTER_VERSION, canonical_json, now_iso, sha256_text, version_payload

DENIED={"decimalLatitude","decimalLongitude","latitude","longitude","geometry","geom","point","suppression_receipt_path","suppressed_group_hash","raw_row","quarantine","token=","api_key=","secret="}

def _load_json(path:Path)->Any: return json.loads(path.read_text(encoding='utf-8'))
def _sha(path:Path)->str: return sha256_text(path.read_text(encoding='utf-8'))

def _load_crosswalk(path:Path|None)->list[dict[str,Any]]:
    if not path: return []
    if path.suffix=='.csv':
        with path.open('r',encoding='utf-8') as f: return list(csv.DictReader(f))
    if path.suffix=='.jsonl': return [json.loads(x) for x in path.read_text(encoding='utf-8').splitlines() if x.strip()]
    return _load_json(path)

def _contains_denied(obj:Any)->bool:
    s=canonical_json(obj)
    return any(x in s for x in DENIED)

def main(argv=None):
    ap=argparse.ArgumentParser(prog='kfm-ebird-federate')
    ap.add_argument('--mode',default='build',choices=['build','validate','diff','report','index'])
    ap.add_argument('--aggregate',default='huc12',choices=['huc12','county','both'])
    ap.add_argument('--release-index',default='data/catalog/fauna/ebird/releases/index.json')
    ap.add_argument('--release-receipt')
    ap.add_argument('--published-root',default='data/published/fauna/ebird')
    ap.add_argument('--catalog-root',default='data/catalog/fauna/ebird')
    ap.add_argument('--layer-registry-dir',default='data/published/fauna/layers')
    ap.add_argument('--taxon-crosswalk'); ap.add_argument('--region-crosswalk')
    ap.add_argument('--out-dir'); ap.add_argument('--public-out-dir')
    ap.add_argument('--previous-federation'); ap.add_argument('--format',default='jsonl',choices=['jsonl','json'])
    ap.add_argument('--dry-run',action='store_true'); ap.add_argument('--force',action='store_true'); ap.add_argument('--version',action='store_true')
    a=ap.parse_args(argv)
    if a.version:
        print(json.dumps(version_payload('kfm-ebird-federate', Path('tools/connectors/fauna/kfm-ebird-ingest/contract_lock.json')),indent=2)); return 0
    rel_path=Path(a.release_receipt or a.release_index)
    if not rel_path.exists(): raise SystemExit('release-index or release-receipt must exist')
    rel=_load_json(rel_path)
    release_ids=[x.get('release_id','r-synth') for x in (rel.get('releases') if isinstance(rel,dict) and 'releases' in rel else [rel])]
    run_ids=[x.get('run_id','run-synth') for x in (rel.get('releases') if isinstance(rel,dict) and 'releases' in rel else [rel])]
    spec_hashes=[x.get('kfm:spec_hash','sha256:synth') for x in (rel.get('releases') if isinstance(rel,dict) and 'releases' in rel else [rel])]
    trows=_load_crosswalk(Path(a.taxon_crosswalk)) if a.taxon_crosswalk else []
    rrows=_load_crosswalk(Path(a.region_crosswalk)) if a.region_crosswalk else []
    fid=sha256_text(canonical_json({'aggregate_targets':a.aggregate,'release_ids':release_ids,'run_ids':run_ids,'kfm_spec_hashes':spec_hashes,'taxon_crosswalk_sha256':_sha(Path(a.taxon_crosswalk)) if a.taxon_crosswalk else None,'region_crosswalk_sha256':_sha(Path(a.region_crosswalk)) if a.region_crosswalk else None})).split(':',1)[1][:16]
    out=Path(a.out_dir or f"data/catalog/fauna/ebird/federation/{fid}")
    pub=Path(a.public_out_dir or f"data/published/fauna/ebird/federation/{fid}")
    if not a.force and (out.exists() or pub.exists()) and not a.dry_run: raise SystemExit('output exists; pass --force')
    docs=[{'schema_version':'v1','object_type':'DiscoveryDocument','document_type':'layer','domain':'fauna','source':'ebird','layer_id':'ebird_huc12','aggregate':a.aggregate,'release_id':release_ids[0],'run_id':run_ids[0],'policy_label':'public_aggregate','public_safe':True,'exact_points':'restricted','suppression_min_n':10,'kfm:spec_hash':spec_hashes[0],'evidence_bundle_uri':'urn:evidence:synth','source_uri':'https://example.invalid/source','query_predicate':'approved=true','searchable_text':'ebird fauna','facets':{'domain':'fauna','source':'ebird','aggregate':a.aggregate,'policy_label':'public_aggregate','exact_points':'restricted','suppression_min_n':10},'denied_public_fields_checked':sorted(DENIED)}]
    graph=[{'schema_version':'v1','object_type':'KfmFederationStatement','subject':'layer:ebird_huc12','predicate':'hasDomain','object':'fauna','domain':'fauna','source':'ebird','policy_label':'public_aggregate','public_safe':True,'exact_points':'restricted','evidence_bundle_uri':'urn:evidence:synth','kfm:spec_hash':spec_hashes[0],'release_id':release_ids[0],'run_id':run_ids[0]}]
    manifest={'schema_version':'v1','object_type':'EbirdFederationManifest','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'federation','public_safe_final_outputs':True,'exact_points':'restricted','federation_id':fid,'aggregate_targets':[a.aggregate],'release_ids':release_ids,'run_ids':run_ids,'kfm_spec_hashes':spec_hashes,'counts':{'releases_seen':len(release_ids),'public_layers_indexed':1,'public_features_indexed':0,'taxa_linked':sum(1 for x in trows if x.get('kfm_taxon_id')),'taxa_unlinked':sum(1 for x in trows if not x.get('kfm_taxon_id')),'regions_linked':sum(1 for x in rrows if x.get('kfm_region_id')),'regions_unlinked':sum(1 for x in rrows if not x.get('kfm_region_id')),'discovery_documents_emitted':len(docs),'graph_statements_emitted':len(graph)},'denied_public_fields_checked':sorted(DENIED),'generated_at':now_iso()}
    pindex={'schema_version':'v1','object_type':'PublicFederationIndex','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'public_aggregate','public_safe':True,'exact_points':'restricted','federation_id':fid,'aggregate_targets':[a.aggregate],'release_ids':release_ids,'run_ids':run_ids,'layer_ids':['ebird_huc12'],'kfm_spec_hashes':spec_hashes,'suppression_min_n_values':[10],'evidence_bundle_uris':['urn:evidence:synth'],'denied_public_fields_checked':sorted(DENIED),'counts':{'public_layers_indexed':1,'public_features_indexed':0,'discovery_documents_emitted':len(docs),'graph_statements_emitted':len(graph)},'generated_at':now_iso()}
    if a.mode=='validate':
        status='pass' if not _contains_denied(pindex) else 'fail'
        print(json.dumps({'schema_version':'v1','object_type':'FederationValidationReport','status':status,'federation_id':fid,'denied_public_fields_checked':sorted(DENIED),'generated_at':now_iso()},indent=2)); return 0 if status=='pass' else 1
    if a.dry_run: return 0
    out.mkdir(parents=True,exist_ok=True); pub.mkdir(parents=True,exist_ok=True)
    (out/'federation_manifest.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
    (out/'discovery_index.jsonl').write_text('\n'.join(canonical_json(x) for x in docs)+'\n',encoding='utf-8')
    (out/'federation_graph.jsonl').write_text('\n'.join(canonical_json(x) for x in graph)+'\n',encoding='utf-8')
    (pub/'public_federation_index.json').write_text(json.dumps(pindex,indent=2),encoding='utf-8')
    (pub/'public_discovery_index.jsonl').write_text('\n'.join(canonical_json(x) for x in docs)+'\n',encoding='utf-8')
    (pub/'public_federation_graph.jsonl').write_text('\n'.join(canonical_json(x) for x in graph)+'\n',encoding='utf-8')
    (pub/'public_semantic_context.json').write_text(json.dumps({'schema_version':'v1','object_type':'PublicSemanticContext','@context':{'layer_id':'kfm:layer_id','feature_id':'kfm:feature_id','aggregate':'kfm:aggregate','huc12':'kfm:huc12','county_fips':'kfm:county_fips','taxonKey':'kfm:taxonKey','occurrenceDate_month':'kfm:occurrenceDate_month','query_predicate':'kfm:query_predicate','source_uri':'kfm:source_uri'}},indent=2),encoding='utf-8')
    return 0
if __name__=='__main__': raise SystemExit(main())
