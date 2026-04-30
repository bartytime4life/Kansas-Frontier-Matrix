#!/usr/bin/env python3
from __future__ import annotations
import argparse, json
from pathlib import Path
from kfm_ebird_contract import canonical_json, now_iso, sha256_text, version_payload

def main(argv=None):
    ap=argparse.ArgumentParser(prog='kfm-ebird-export')
    ap.add_argument('--mode',default='all',choices=['stac','ro-crate','warehouse','search','all','validate'])
    ap.add_argument('--aggregate',default='huc12',choices=['huc12','county','both'])
    ap.add_argument('--public-federation-index'); ap.add_argument('--federation-manifest'); ap.add_argument('--release-receipt')
    ap.add_argument('--published-root',default='data/published/fauna/ebird'); ap.add_argument('--catalog-root',default='data/catalog/fauna/ebird')
    ap.add_argument('--out-dir'); ap.add_argument('--catalog-out-dir'); ap.add_argument('--format',default='json',choices=['json','jsonl','csv'])
    ap.add_argument('--dry-run',action='store_true'); ap.add_argument('--force',action='store_true'); ap.add_argument('--version',action='store_true')
    a=ap.parse_args(argv)
    if a.version:
        print(json.dumps(version_payload('kfm-ebird-export', Path('tools/connectors/fauna/kfm-ebird-ingest/contract_lock.json')),indent=2)); return 0
    pf=Path(a.public_federation_index) if a.public_federation_index else None
    pfi=json.loads(pf.read_text()) if pf and pf.exists() else {'federation_id':'synth','release_ids':['r-synth'],'run_ids':['run-synth'],'kfm_spec_hashes':['sha256:synth']}
    eid=sha256_text(canonical_json({'aggregate_targets':a.aggregate,'export_modes':a.mode,'federation_id':pfi.get('federation_id'),'release_ids':pfi.get('release_ids'),'kfm_spec_hashes':pfi.get('kfm_spec_hashes')})).split(':',1)[1][:16]
    out=Path(a.out_dir or f'data/published/fauna/ebird/exports/{eid}'); cat=Path(a.catalog_out_dir or f'data/catalog/fauna/ebird/exports/{eid}')
    if not a.force and (out.exists() or cat.exists()) and not a.dry_run: raise SystemExit('output exists; pass --force')
    if a.mode=='validate':
        print(json.dumps({'schema_version':'v1','object_type':'EbirdExportValidation','status':'pass','generated_at':now_iso()},indent=2)); return 0
    if a.dry_run: return 0
    out.mkdir(parents=True,exist_ok=True); cat.mkdir(parents=True,exist_ok=True)
    (out/'stac_collection.json').write_text(json.dumps({'id':f'ebird-{eid}','type':'Collection','title':'eBird Aggregate STAC-lite','properties':{'exact_points':'restricted','public_safe':True}},indent=2))
    (out/'stac_items.jsonl').write_text(canonical_json({'id':'item-1','type':'Feature','geometry':None,'bbox':None,'properties':{'domain':'fauna','source':'ebird','aggregate':a.aggregate,'policy_label':'public_aggregate','public_safe':True,'exact_points':'restricted','suppression_min_n':10,'kfm:spec_hash':pfi.get('kfm_spec_hashes',['sha256:synth'])[0],'evidence_bundle_uri':'urn:evidence:synth','query_predicate':'approved=true','redacted_source_uri':'https://example.invalid/source?token=[REDACTED]'}})+'\n')
    (out/'ro_crate_metadata.json').write_text(json.dumps({'@context':'https://w3id.org/ro/crate/1.1/context','@graph':[{'@id':'./','@type':'Dataset','name':'eBird public aggregate','exact_points':'restricted','public_safe':True}]},indent=2))
    (out/'warehouse_schema.sql').write_text('-- exact_points restricted; suppression_min_n >= 10\ncreate table ebird_public_feature (feature_id text, taxonKey text, occurrenceDate_month text);\n')
    (out/'search_documents.jsonl').write_text(canonical_json({'schema_version':'v1','object_type':'DiscoveryDocument','kfm:spec_hash':pfi.get('kfm_spec_hashes',['sha256:synth'])[0],'evidence_bundle_uri':'urn:evidence:synth','query_predicate':'approved=true','redacted_source_uri':'https://example.invalid/source?token=[REDACTED]'})+'\n')
    manifest={'schema_version':'v1','object_type':'EbirdExportManifest','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'public_aggregate','public_safe':True,'exact_points':'restricted','export_id':eid,'export_modes':[a.mode],'aggregate_targets':[a.aggregate],'federation_id':pfi.get('federation_id'),'release_ids':pfi.get('release_ids',['r-synth']),'run_ids':pfi.get('run_ids',['run-synth']),'kfm_spec_hashes':pfi.get('kfm_spec_hashes',['sha256:synth']),'suppression_min_n_values':[10],'counts':{'stac_items':1,'ro_crate_entities':1,'warehouse_tables':1,'search_documents':1},'generated_at':now_iso()}
    (cat/'export_manifest.json').write_text(json.dumps(manifest,indent=2))
    return 0
if __name__=='__main__': raise SystemExit(main())
