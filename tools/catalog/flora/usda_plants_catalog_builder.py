from __future__ import annotations
import argparse, hashlib, json
from datetime import datetime, timezone
from pathlib import Path
SOURCE_URI='https://plants.sc.egov.usda.gov/downloads'; ROOT=Path(__file__).resolve().parents[3]; SCHEMA=ROOT/'schemas/flora/usda_plants_catalog.schema.json'
def now(): return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
def can(o): return json.dumps(o,sort_keys=True,separators=(',',':'),ensure_ascii=False)
def w(p,o): p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
def main():
 a=argparse.ArgumentParser();a.add_argument('--processed-dir',type=Path,required=True);a.add_argument('--evidence-dir',type=Path,required=True);a.add_argument('--proof-manifest',type=Path,required=True);a.add_argument('--snapshot-date',required=True);a.add_argument('--generated-at');a.add_argument('--out-dir',type=Path,required=True);x=a.parse_args();g=x.generated_at or now()
 ds=[]
 for p in sorted(x.processed_dir.glob('*.json')):
  d=json.loads(p.read_text());s=d['properties']['plants:symbol'];ds.append({'id':d['id'],'plants_symbol':s,'scientificName':d['properties']['scientificName'],'family':d['properties']['family'],'spec_hash':d['spec_hash'],'dataset_ref':f'processed/flora/usda_plants/{s}.json','evidence_link_ref':f'evidence/flora/usda_plants/{s}.evidence_link.json'})
 c={"schema_version":"1.0.0","object_type":"usda_plants_catalog","catalog_id":f"kfm.catalog.flora.usda_plants.{x.snapshot_date}","domain":"flora","catalog_profile":"kfm_dcat_stac_adjacent_v1","snapshot_date":x.snapshot_date,"generated_at":g,"source":{"source_id":"usda_plants","source_uri":SOURCE_URI},"rights":{"license":"USDA / U.S. Public Domain","rightsHolder":"United States Department of Agriculture","policy_label":"public"},"datasets":ds,"catalog_refs":{"dcat_like":"catalog/flora/usda_plants/dcat_like_catalog.json","stac_like":"catalog/flora/usda_plants/stac_like_collection.json","prov_like":"catalog/flora/usda_plants/prov_like_lineage.json"},"proof_refs":["proofs/flora/usda_plants/spec_hash_manifest.json"],"receipt_refs":[],"release_candidate_refs":[]}
 c['catalog_hash']='sha256:'+hashlib.sha256(can(c).encode()).hexdigest();
 from jsonschema import Draft202012Validator; errs=list(Draft202012Validator(json.loads(SCHEMA.read_text())).iter_errors(c));
 if errs: raise ValueError(str(errs[0]))
 w(x.out_dir/'catalog.json',c);w(x.out_dir/'dcat_like_catalog.json',{'profile':'dcat_like','title':'USDA PLANTS fixture catalog candidate','description':'DCAT-like JSON only','publisher':'USDA PLANTS Database','license':'USDA / U.S. Public Domain','datasets':[i['id'] for i in ds],'distribution_refs':[i['dataset_ref'] for i in ds]});w(x.out_dir/'stac_like_collection.json',{'profile':'stac_like','stac_role':'collection_candidate','id':c['catalog_id'],'description':'STAC-like collection candidate','license':'proprietary','links':[],'assets':{i['plants_symbol']:{'href':i['dataset_ref']} for i in ds}});w(x.out_dir/'prov_like_lineage.json',{'profile':'prov_like','generated_at':g,'agent':'USDA PLANTS Database','entity_dataset_refs':[i['dataset_ref'] for i in ds],'activity':['ingest','validate','catalog']})
if __name__=='__main__': main()
