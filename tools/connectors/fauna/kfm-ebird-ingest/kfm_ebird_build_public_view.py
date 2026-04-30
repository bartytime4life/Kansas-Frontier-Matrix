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
    p=argparse.ArgumentParser(prog='kfm-ebird-build-public-view')
    p.add_argument('--promotion-dir', required=True)
    p.add_argument('--catalog-record'); p.add_argument('--aggregate-file'); p.add_argument('--aggregate-manifest')
    p.add_argument('--evidencebundle'); p.add_argument('--layer-evidence-drawer'); p.add_argument('--layer-registry')
    p.add_argument('--aggregate', required=True, choices=('county','huc12'))
    p.add_argument('--out-dir'); p.add_argument('--maplibre-out'); p.add_argument('--boundary-source-id'); p.add_argument('--boundary-source-uri')
    p.add_argument('--boundary-join-property'); p.add_argument('--format', choices=('jsonl','csv'), default='jsonl')
    p.add_argument('--dry-run', action='store_true'); p.add_argument('--overwrite', action='store_true')
    return p.parse_args(argv)

def main()->None:
    a=parse_args(sys.argv[1:]); promo=Path(a.promotion_dir)
    fmt=a.format
    aggf=Path(a.aggregate_file or (promo/f'aggregates.{fmt}' if (promo/f'aggregates.{fmt}').exists() else promo/'aggregates.jsonl'))
    catf=Path(a.catalog_record or promo/'catalog_record.json'); manf=Path(a.aggregate_manifest or promo/'aggregate_manifest.json')
    ebf=Path(a.evidencebundle or promo/'evidencebundle.json'); layer_drawer=Path(a.layer_evidence_drawer or promo/'evidence_drawer.json')
    regp=Path(a.layer_registry or f"data/published/fauna/layers/ebird_agg_{a.aggregate}.json")
    out_dir=Path(a.out_dir or promo/'api'); map_out=Path(a.maplibre_out or f"data/published/fauna/maplibre/ebird_agg_{a.aggregate}.json")
    join_prop=a.boundary_join_property or ('HUC12' if a.aggregate=='huc12' else 'GEOID')
    boundary_id=a.boundary_source_id or f"kfm_{a.aggregate}_boundaries"
    for p in [promo,aggf,catf,manf,ebf,layer_drawer,regp]:
        if not p.exists(): fail(f"Missing input file: {p}")
    old=sys.argv
    try:
        sys.argv=['validate_evidencebundle.py', str(ebf)]; validate_bundle_main()
    except SystemExit as e:
        if e.code!=0: fail('EvidenceBundle validation failed')
    finally: sys.argv=old
    rows=parse_rows(aggf,fmt); bundle=json.loads(ebf.read_text()); manifest=json.loads(manf.read_text()); cat=json.loads(catf.read_text()); registry=json.loads(regp.read_text()); ldrawer=json.loads(layer_drawer.read_text())
    spec=bundle.get('kfm:spec_hash')
    for o in [manifest,cat,ldrawer,registry]:
        if o.get('kfm:spec_hash') and o['kfm:spec_hash']!=spec: fail('kfm:spec_hash mismatch across inputs')
    agg_sha=sha256_file(aggf)
    man_out=manifest.get('output_sha256'); cat_out=cat.get('output_sha256')
    if man_out and cat_out and man_out!=cat_out and cat_out!=agg_sha: fail('aggregate hash mismatch catalog')
    if cat_out and cat_out!=agg_sha: fail('aggregate hash mismatch catalog')
    if registry.get('exact_points')!='restricted' or registry.get('public_safe') is not True: fail('layer registry safety mismatch')
    if any(f.lower() in {x.lower() for x in DENIED_FIELDS} for f in registry.get('allowlist_fields',[])): fail('layer registry allowlist contains denied fields')
    min_n=int(manifest.get('suppression_min_n',cat.get('suppression_min_n',10)))
    feats=[]; drawers=[]; rejected=0; unknown=0
    for r in rows:
        if r.get('policy_label')!='public_aggregate': fail('row policy_label must be public_aggregate')
        if int(r.get('suppression_min_n',min_n))<10 or int(r.get('checklist_count',0))<min_n: fail('suppression/checklist invalid')
        if any(k.lower() in {x.lower() for x in DENIED_FIELDS} for k in r.keys()): fail('aggregate row has denied fields')
        if str(r.get('kfm:spec_hash'))!=spec: fail('row kfm:spec_hash mismatch')
        aid=r['huc12'] if a.aggregate=='huc12' else r['county_fips']
        layer_id=f'ebird_agg_{a.aggregate}'
        fid=hashlib.sha256(canonical_json({"layer_id":layer_id,"aggregate":a.aggregate,"aggregate_id":aid,"taxonKey":r['taxonKey'],"occurrenceDate_month":r['occurrenceDate_month'],"kfm_spec_hash":spec}).encode()).hexdigest()[:24]
        if int(r.get('observation_count_unknown_count',0))>0: unknown+=1
        feat={"schema_version":"v1","object_type":"PublicAggregateFeature","domain":"fauna","source":"ebird","layer_id":layer_id,"feature_id":fid,"aggregate":a.aggregate,"taxonKey":r['taxonKey'],"occurrenceDate_month":r['occurrenceDate_month'],"checklist_count":int(r['checklist_count']),"observation_count_sum":int(r['observation_count_sum']),"observation_count_unknown_count":int(r.get('observation_count_unknown_count',0)),"species_count":int(r['species_count']),"suppression_min_n":min_n,"policy_label":"public_aggregate","public_safe":True,"exact_points":"restricted","kfm:spec_hash":spec,"evidence_bundle_uri":cat.get('evidence_bundle_uri',bundle.get('source_uri',str(ebf))),"evidence_drawer_uri":str(out_dir/'feature_evidence_drawers.jsonl')}
        feat['huc12' if a.aggregate=='huc12' else 'county_fips']=aid
        feats.append(feat)
        drawers.append({"schema_version":"v1","object_type":"FeatureEvidenceDrawer","domain":"fauna","source":"ebird","layer_id":layer_id,"feature_id":fid,"aggregate":a.aggregate,"aggregate_id":aid,"taxonKey":r['taxonKey'],"occurrenceDate_month":r['occurrenceDate_month'],"policy_label":"public_aggregate","public_safe":True,"exact_points":"restricted","source_uri":bundle.get('source_uri'),"query_predicate":bundle.get('query_predicate'),"mapping":bundle.get('mapping',{}),"kfm:spec_hash":spec,"evidence_bundle_uri":cat.get('evidence_bundle_uri',bundle.get('source_uri',str(ebf))),"suppression_min_n":min_n,"checklist_count":int(r['checklist_count']),"displayed_fields":registry.get('allowlist_fields',[]),"hidden_fields":DENIED_FIELDS,"denied_public_fields_checked":DENIED_FIELDS})
    features_path=out_dir/f'features.{fmt}'; drawer_path=out_dir/'feature_evidence_drawers.jsonl'; desc_path=out_dir/'layer_api_descriptor.json'; manifest_path=out_dir/'api_manifest.json'
    if not a.dry_run:
        out_dir.mkdir(parents=True, exist_ok=True); map_out.parent.mkdir(parents=True,exist_ok=True)
        for p in [features_path,drawer_path,desc_path,manifest_path,map_out]:
            if p.exists() and not a.overwrite: fail(f'target exists (use --overwrite): {p}')
        write_rows(features_path,fmt,feats); drawer_path.write_text(''.join(json.dumps(x,sort_keys=True)+"\n" for x in drawers),encoding='utf-8')
    desc={"schema_version":"v1","object_type":"LayerApiDescriptor","domain":"fauna","source":"ebird","layer_id":f"ebird_agg_{a.aggregate}","aggregate":a.aggregate,"policy_label":"public_aggregate","public_safe":True,"exact_points":"restricted","kfm:spec_hash":spec,"suppression_min_n":min_n,"feature_table_uri":str(features_path),"feature_evidence_drawers_uri":str(drawer_path),"layer_evidence_drawer_uri":str(layer_drawer),"catalog_record_uri":str(catf),"evidence_bundle_uri":cat.get('evidence_bundle_uri',bundle.get('source_uri',str(ebf))),"route_templates":{"layer_metadata":"/api/fauna/ebird/layers/{layerId}","features":"/api/fauna/ebird/layers/{layerId}/features","feature_evidence":"/api/fauna/ebird/layers/{layerId}/features/{featureId}/evidence"},"query_parameters":["aggregate_id","taxonKey","occurrenceDate_month"],"output_fields":list(feats[0].keys()) if feats else [],"denied_public_fields_checked":DENIED_FIELDS,"latest_run_id":registry.get('latest_run_id')}
    mapcfg={"schema_version":"v1","object_type":"MapLibreLayerConfig","domain":"fauna","source":"ebird","layer_id":f"ebird_agg_{a.aggregate}","aggregate":a.aggregate,"public_safe":True,"exact_points":"restricted","source":{"id":boundary_id,"join_property":join_prop},"data":{"feature_table_uri":str(features_path),"feature_id_field":"feature_id","aggregate_id_field":"huc12" if a.aggregate=='huc12' else 'county_fips'},"style":{"type":"fill","metric":"checklist_count"},"evidence":{"drawer_table_uri":str(drawer_path),"required_fields":["feature_id","evidence_drawer_uri","evidence_bundle_uri","kfm:spec_hash","source_uri","query_predicate","suppression_min_n"]},"denied_layer_types":["circle","heatmap","point","cluster"],"denied_public_fields_checked":DENIED_FIELDS}
    if a.boundary_source_uri: mapcfg['source']['uri']=a.boundary_source_uri
    if not a.dry_run:
        desc_path.write_text(json.dumps(desc,indent=2,sort_keys=True)+"\n",encoding='utf-8'); map_out.write_text(json.dumps(mapcfg,indent=2,sort_keys=True)+"\n",encoding='utf-8')
    apim={"schema_version":"v1","object_type":"ApiManifest","domain":"fauna","source":"ebird","layer_id":f"ebird_agg_{a.aggregate}","aggregate":a.aggregate,"policy_label":"public_aggregate","public_safe":True,"exact_points":"restricted","promotion_dir":str(promo),"catalog_record_path":str(catf),"catalog_record_sha256":sha256_file(catf),"aggregate_file_path":str(aggf),"aggregate_file_sha256":agg_sha,"aggregate_manifest_path":str(manf),"aggregate_manifest_sha256":sha256_file(manf),"evidencebundle_path":str(ebf),"evidencebundle_sha256":sha256_file(ebf),"layer_registry_path":str(regp),"layer_registry_sha256":sha256_file(regp),"features_path":str(features_path),"feature_evidence_drawers_path":str(drawer_path),"layer_api_descriptor_path":str(desc_path),"maplibre_config_path":str(map_out),"kfm:spec_hash":spec,"suppression_min_n":min_n,"output_fields":list(feats[0].keys()) if feats else [],"denied_public_fields_checked":DENIED_FIELDS,"counts":{"features_emitted":len(feats),"evidence_drawers_emitted":len(drawers),"rows_read":len(rows),"rows_rejected":rejected,"rows_with_unknown_observation_count":unknown},"generated_at":datetime.now(timezone.utc).isoformat()}
    if not a.dry_run:
        desc['output_sha256']={"features":sha256_file(features_path),"feature_evidence_drawers":sha256_file(drawer_path)}
        desc_path.write_text(json.dumps(desc,indent=2,sort_keys=True)+"\n",encoding='utf-8')
        apim["features_sha256"]=sha256_file(features_path); apim["feature_evidence_drawers_sha256"]=sha256_file(drawer_path); apim["layer_api_descriptor_sha256"]=sha256_file(desc_path); apim["maplibre_config_sha256"]=sha256_file(map_out)
        manifest_path.write_text(json.dumps(apim,indent=2,sort_keys=True)+"\n",encoding='utf-8')
    else:
        print(json.dumps({"valid":True,"rows":len(rows),"features_emitted":len(feats)},indent=2))

if __name__=='__main__': main()
