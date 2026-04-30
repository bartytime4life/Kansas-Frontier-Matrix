#!/usr/bin/env python3
from __future__ import annotations
import argparse,csv,hashlib,json,sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[4]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from packages.evidence.evidencebundle_hash import canonical_json
from tools.validators.fauna.validate_evidencebundle import main as validate_bundle_main

DENIED_FIELDS=["decimalLatitude","decimalLongitude","latitude","longitude","lat","lon","raw_latitude","raw_longitude","point","geom","geometry"]


def fail(msg:str)->None:
    print(f"ERROR: {msg}", file=sys.stderr); raise SystemExit(2)

def sha256_file(path:Path)->str:
    d=hashlib.sha256();
    with path.open('rb') as f:
        for c in iter(lambda:f.read(65536), b''): d.update(c)
    return f"sha256:{d.hexdigest()}"

def parse_rows(path:Path, fmt:str)->list[dict[str,Any]]:
    if fmt=='jsonl':
        return [json.loads(l) for l in path.read_text(encoding='utf-8').splitlines() if l.strip()]
    with path.open('r', encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))

def write_rows(path:Path, fmt:str, rows:list[dict[str,Any]])->None:
    if fmt=='jsonl':
        path.write_text(''.join(json.dumps(r,sort_keys=True)+"\n" for r in rows), encoding='utf-8'); return
    fields=list(rows[0].keys()) if rows else []
    with path.open('w', encoding='utf-8', newline='') as f:
        w=csv.DictWriter(f, fieldnames=fields); w.writeheader(); w.writerows(rows)

def parse_args(argv:list[str])->argparse.Namespace:
    p=argparse.ArgumentParser(prog='kfm-ebird-promote')
    p.add_argument('--aggregate-file', required=True); p.add_argument('--aggregate-manifest', required=True)
    p.add_argument('--evidencebundle', required=True); p.add_argument('--aggregate', required=True, choices=('county','huc12'))
    p.add_argument('--publish-dir'); p.add_argument('--catalog-dir'); p.add_argument('--layer-registry')
    p.add_argument('--promotion-receipt'); p.add_argument('--format', choices=('jsonl','csv'), default='jsonl')
    p.add_argument('--run-id'); p.add_argument('--dry-run', action='store_true'); p.add_argument('--overwrite', action='store_true')
    return p.parse_args(argv)

def main()->None:
    a=parse_args(sys.argv[1:])
    pub=Path(a.publish_dir or f"data/published/fauna/ebird/{a.aggregate}")
    cat=Path(a.catalog_dir or f"data/catalog/fauna/ebird/{a.aggregate}")
    regp=Path(a.layer_registry or f"data/published/fauna/layers/ebird_agg_{a.aggregate}.json")
    rec_override=Path(a.promotion_receipt) if a.promotion_receipt else None
    aggf,manf,ebf=Path(a.aggregate_file),Path(a.aggregate_manifest),Path(a.evidencebundle)
    for p in [aggf,manf,ebf,regp]:
        if not p.exists(): fail(f"Missing input file: {p}")
    if 'data/published' not in pub.as_posix(): fail('--publish-dir must be under data/published')

    old=sys.argv
    try:
        sys.argv=['validate_evidencebundle.py', str(ebf)]; validate_bundle_main()
    except SystemExit as e:
        if e.code!=0: fail('EvidenceBundle validation failed')
    finally: sys.argv=old

    bundle=json.loads(ebf.read_text(encoding='utf-8')); manifest=json.loads(manf.read_text(encoding='utf-8')); registry=json.loads(regp.read_text(encoding='utf-8'))
    rows=parse_rows(aggf,a.format)
    eb_sha,man_sha,agg_sha=sha256_file(ebf),sha256_file(manf),sha256_file(aggf)
    spec=bundle.get('kfm:spec_hash')
    if not spec: fail('Missing kfm:spec_hash in EvidenceBundle')
    if manifest.get('output_sha256') and manifest['output_sha256']!=agg_sha: fail('Aggregate file hash mismatch manifest output_sha256')
    if manifest.get('evidencebundle_sha256') and manifest['evidencebundle_sha256']!=eb_sha: fail('EvidenceBundle hash mismatch manifest evidencebundle_sha256')
    if manifest.get('kfm:spec_hash') and manifest['kfm:spec_hash']!=spec: fail('kfm:spec_hash mismatch between manifest and EvidenceBundle')

    min_n=int(manifest.get('suppression_min_n', bundle.get('suppression_min_n',10)))
    if min_n<10: fail('suppression_min_n must be >= 10')
    denied_low={x.lower() for x in DENIED_FIELDS}
    for i,r in enumerate(rows):
        if r.get('policy_label')!='public_aggregate': fail(f'row {i} policy_label must be public_aggregate')
        if str(r.get('kfm:spec_hash'))!=spec: fail('kfm:spec_hash mismatch across aggregate rows and EvidenceBundle')
        for k in r.keys():
            if k.lower() in denied_low: fail(f'aggregate row contains denied field: {k}')
        if int(r.get('checklist_count',0))<min_n: fail('aggregate row checklist_count below suppression_min_n')
    if registry.get('exact_points')!='restricted': fail('layer registry exact_points must be restricted')
    if registry.get('public_safe') is not True: fail('layer registry public_safe must be true')
    if any(f.lower() in denied_low for f in registry.get('allowlist_fields',[])): fail('layer registry allowlist contains denied fields')

    run_id=a.run_id or hashlib.sha256(canonical_json({"aggregate":a.aggregate,"aggregate_file_sha256":agg_sha,"aggregate_manifest_sha256":man_sha,"evidencebundle_sha256":eb_sha,"kfm_spec_hash":spec}).encode()).hexdigest()[:16]
    layer_id=f"ebird_agg_{a.aggregate}"
    run_dir=pub/run_id
    out_file=run_dir/f"aggregates.{a.format}"; out_manifest=run_dir/'aggregate_manifest.json'; out_bundle=run_dir/'evidencebundle.json'
    out_catalog=run_dir/'catalog_record.json'; out_triplets=run_dir/'triplets.jsonl'; out_drawer=run_dir/'evidence_drawer.json'; out_receipt=rec_override or run_dir/'promotion_receipt.json'
    for p in [out_file,out_manifest,out_bundle,out_catalog,out_triplets,out_drawer,out_receipt]:
        if p.exists() and not a.overwrite: fail(f'target exists (use --overwrite): {p}')
    if a.dry_run:
        print(json.dumps({"run_id":run_id,"plan":{"publish_dir":str(run_dir),"catalog_dir":str(cat)},"valid":True},indent=2)); return

    run_dir.mkdir(parents=True, exist_ok=True)
    write_rows(out_file,a.format,rows)
    out_manifest.write_text(json.dumps({k:v for k,v in manifest.items() if 'suppressed' not in k and 'suppression_receipt' not in k},indent=2,sort_keys=True)+"\n",encoding='utf-8')
    out_bundle.write_text(json.dumps(bundle,indent=2,sort_keys=True)+"\n",encoding='utf-8')
    out_sha=sha256_file(out_file)
    displayed=[f for f in registry.get('allowlist_fields',[]) if f not in {'kfm:spec_hash','evidence_bundle_uri'}]
    common_counts={k:manifest.get('counts',{}).get(k) for k in ["rows_seen","rows_assigned","rows_unassigned","rows_invalid","groups_seen","groups_published","groups_suppressed","observation_count_unknown"] if manifest.get('counts',{}).get(k) is not None}
    rec={"schema_version":"v1","object_type":"CatalogRecord","domain":"fauna","source":"ebird","layer_id":layer_id,"aggregate":a.aggregate,"policy_label":"public_aggregate","public_safe":True,"exact_points":"restricted","run_id":run_id,"kfm:spec_hash":spec,"evidence_bundle_uri":bundle.get('source_uri',str(out_bundle)),"source_uri":bundle.get('source_uri'),"query_predicate":bundle.get('query_predicate'),"suppression_min_n":min_n,"output_path":str(out_file),"output_sha256":out_sha,"aggregate_manifest_path":str(out_manifest),"aggregate_manifest_sha256":sha256_file(out_manifest),"evidencebundle_path":str(out_bundle),"evidencebundle_sha256":sha256_file(out_bundle),"layer_registry_path":str(regp),"layer_registry_sha256":sha256_file(regp),"output_fields":list(rows[0].keys()) if rows else registry.get('allowlist_fields',[]),"denied_public_fields_checked":DENIED_FIELDS,**common_counts}
    if 'rights_status' in bundle: rec['rights_status']=bundle['rights_status']
    if 'citation' in bundle: rec['citation']=bundle['citation']
    if 'citation_uri' in bundle: rec['citation_uri']=bundle['citation_uri']
    out_catalog.write_text(json.dumps(rec,indent=2,sort_keys=True)+"\n",encoding='utf-8')
    triplets=[{"subject":layer_id,"predicate":p,"object":o,"evidence_bundle_uri":rec['evidence_bundle_uri'],"kfm:spec_hash":spec,"policy_label":"public_aggregate"} for p,o in [("hasDomain","fauna"),("hasSource","ebird"),("hasAggregate",a.aggregate),("hasPolicyLabel","public_aggregate"),("hasExactPoints","restricted"),("hasSuppressionMinN",min_n),("hasSpecHash",spec),("hasEvidenceBundle",str(out_bundle)),("hasAggregateManifest",str(out_manifest)),("hasOutputHash",out_sha),("derivedFrom","EvidenceBundle"),("promotedBy","kfm-ebird-promote"),("hasRunId",run_id)]]
    out_triplets.write_text(''.join(json.dumps(t,sort_keys=True)+"\n" for t in triplets),encoding='utf-8')
    drawer={"schema_version":"v1","object_type":"EvidenceDrawer","domain":"fauna","source":"ebird","layer_id":layer_id,"aggregate":a.aggregate,"policy_label":"public_aggregate","public_safe":True,"exact_points":"restricted","source_uri":bundle.get('source_uri'),"query_predicate":bundle.get('query_predicate'),"kfm:spec_hash":spec,"evidence_bundle_uri":rec['evidence_bundle_uri'],"suppression_min_n":min_n,"mapping":bundle.get('mapping',{}),"displayed_fields":displayed,"hidden_fields":DENIED_FIELDS,"denied_public_fields_checked":DENIED_FIELDS}
    out_drawer.write_text(json.dumps(drawer,indent=2,sort_keys=True)+"\n",encoding='utf-8')
    receipt={"schema_version":"v1","object_type":"PromotionReceipt","domain":"fauna","source":"ebird","policy_label":"public_aggregate","public_safe":True,"run_id":run_id,"aggregate":a.aggregate,"layer_id":layer_id,"kfm:spec_hash":spec,"suppression_min_n":min_n,"validations_passed":["evidencebundle","aggregate_rows","manifest_hashes","registry_safety"],"input_hashes":{"aggregate_file_sha256":agg_sha,"aggregate_manifest_sha256":man_sha,"evidencebundle_sha256":eb_sha},"output_hashes":{"aggregates_sha256":out_sha,"catalog_record_sha256":sha256_file(out_catalog),"triplets_sha256":sha256_file(out_triplets),"evidence_drawer_sha256":sha256_file(out_drawer)},"published_paths":{"run_dir":str(run_dir),"aggregates":str(out_file)},"catalog_paths":{"catalog_record":str(out_catalog),"triplets":str(out_triplets),"evidence_drawer":str(out_drawer)},"denied_public_fields_checked":DENIED_FIELDS,"promoted_at":datetime.now(timezone.utc).isoformat(),"counts":common_counts}
    out_receipt.parent.mkdir(parents=True,exist_ok=True); out_receipt.write_text(json.dumps(receipt,indent=2,sort_keys=True)+"\n",encoding='utf-8')
    cat.mkdir(parents=True,exist_ok=True)
    idx=cat/'index.json'; data=json.loads(idx.read_text()) if idx.exists() else {"entries":{}}
    data['entries'][run_id]={"layer_id":layer_id,"aggregate":a.aggregate,"run_id":run_id,"kfm:spec_hash":spec,"catalog_record_path":str(out_catalog),"public_output_path":str(out_file),"evidence_drawer_path":str(out_drawer),"promotion_receipt_path":str(out_receipt),"output_sha256":out_sha,"promoted_at":receipt['promoted_at']}
    idx.write_text(json.dumps(data,indent=2,sort_keys=True)+"\n",encoding='utf-8')
    registry.update({"latest_run_id":run_id,"latest_catalog_record_path":str(out_catalog),"latest_evidence_drawer_path":str(out_drawer),"latest_output_path":str(out_file),"latest_output_sha256":out_sha,"denied_fields":DENIED_FIELDS,"public_safe":True,"exact_points":"restricted"})
    regp.write_text(json.dumps(registry,indent=2,sort_keys=True)+"\n",encoding='utf-8')

if __name__=='__main__': main()
