from __future__ import annotations
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,validate,write_json,sha256_file
BLOCK={'decimallatitude','decimallongitude','latitude','longitude','coordinates','geometry','bbox','tilejson','tiles'}
def scan(x):
 if isinstance(x,dict):
  for k,v in x.items():
   if k.lower() in BLOCK: raise SystemExit('USDA_PLANTS_PUBLICATION_COORDINATE_LEAK_REFUSED')
   scan(v)
 elif isinstance(x,list):
  for v in x: scan(v)

def main():
 p=argparse.ArgumentParser();p.add_argument('--execution-plan',type=Path,required=True);p.add_argument('--promoted-package',type=Path,required=True);p.add_argument('--out-root',type=Path,required=True);p.add_argument('--snapshot-date',required=True);p.add_argument('--generated-at',required=True);a=p.parse_args()
 pkg=json.loads(a.promoted_package.read_text()); scan(pkg)
 proot=a.out_root/f'published/flora/usda_plants/{a.snapshot_date}'; (proot/'evidence_drawer').mkdir(parents=True,exist_ok=True)
 recs=sorted(pkg.get('records',[]),key=lambda r:r.get('plants_symbol',''))
 ds=[];ev=[];cp=[]
 for r in recs:
  sym=r['plants_symbol']; payload={k:v for k,v in r.items() if k not in ['raw_ref','work_ref','quarantine_ref']}; scan(payload)
  ep=proot/f'evidence_drawer/{sym}.json'; write_json(ep,payload)
  ev.append({'plants_symbol':sym,'path':f'published/flora/usda_plants/{a.snapshot_date}/evidence_drawer/{sym}.json','sha256':sha256_file(ep)})
  fips=sorted(set([f for f in r.get('fips_codes',[]) if len(f)==5 and f.isdigit()]))
  cp += [{'plants_symbol':sym,'fips':f,'presence':'present','spec_hash':r['spec_hash']} for f in fips]
  ds.append({'plants_symbol':sym,'scientificName':r.get('scientificName',''),'nationalCommonName':r.get('nationalCommonName',''),'family':r.get('family',''),'state_count':len(set(f[:2] for f in fips)),'county_count':len(fips),'spec_hash':r['spec_hash'],'evidence_drawer_ref':ev[-1]['path'],'county_presence_ref':f'published/flora/usda_plants/{a.snapshot_date}/county_presence.json'})
 def with_hash(o,k): o[k]=canonical_hash(o,k); return o
 objs={
 'dataset_index.json':with_hash({"schema_version":"1.0.0","object_type":"usda_plants_published_dataset_index","index_id":f"kfm.published_index.flora.usda_plants.{a.snapshot_date}","domain":"flora","source_id":"usda_plants","snapshot_date":a.snapshot_date,"generated_at":a.generated_at,"records":ds,"rights":{"license":"USDA / U.S. Public Domain","rightsHolder":"United States Department of Agriculture","policy_label":"public"},"safety":{"contains_precise_coordinates":False,"contains_county_geometry":False}},'index_hash'),
 'evidence_drawer_index.json':with_hash({"schema_version":"1.0.0","object_type":"usda_plants_published_evidence_drawer_index","index_id":f"kfm.published_evidence_drawer_index.flora.usda_plants.{a.snapshot_date}","domain":"flora","source_id":"usda_plants","snapshot_date":a.snapshot_date,"generated_at":a.generated_at,"payloads":ev,"safety":{"contains_precise_coordinates":False,"contains_county_geometry":False}},'index_hash'),
 'county_presence.json':with_hash({"schema_version":"1.0.0","object_type":"usda_plants_published_county_presence","presence_id":f"kfm.published_county_presence.flora.usda_plants.{a.snapshot_date}","domain":"flora","source_id":"usda_plants","snapshot_date":a.snapshot_date,"generated_at":a.generated_at,"join_key":"fips","records":sorted(cp,key=lambda x:(x['plants_symbol'],x['fips'])),"safety":{"contains_precise_coordinates":False,"contains_county_geometry":False,"fips_only":True}},'presence_hash'),
 'map_descriptor.json':with_hash({"schema_version":"1.0.0","object_type":"usda_plants_published_map_descriptor","descriptor_id":f"kfm.published_map_descriptor.flora.usda_plants.{a.snapshot_date}","domain":"flora","source_id":"usda_plants","snapshot_date":a.snapshot_date,"generated_at":a.generated_at,"maplibre":{"source_id":"flora_usda_plants_county_presence","layer_id":"flora_usda_plants_county_presence_fill","source_type":"geojson_join_required","data_ref":f"published/flora/usda_plants/{a.snapshot_date}/county_presence.json","requires_external_county_geometry":True,"generates_geometry":False,"generates_tiles":False},"join":{"presence_key":"fips","geometry_key":"fips","taxon_key":"plants_symbol"},"style_fragment":{"version":8,"metadata":{"kfm:domain":"flora","kfm:source_id":"usda_plants","kfm:snapshot_date":a.snapshot_date},"sources":{},"layers":[]},"safety":{"contains_precise_coordinates":False,"contains_county_geometry":False,"contains_vector_tiles":False}},'descriptor_hash')}
 for fn,obj in objs.items(): write_json(proot/fn,obj)
 outputs=[]
 for role,fn in [('published_dataset_index','dataset_index.json'),('published_evidence_drawer_index','evidence_drawer_index.json'),('published_county_presence','county_presence.json'),('published_map_descriptor','map_descriptor.json')]: outputs.append({'role':role,'path':f'published/flora/usda_plants/{a.snapshot_date}/{fn}','sha256':sha256_file(proot/fn)})
 rel=with_hash({"schema_version":"1.0.0","object_type":"usda_plants_published_release_manifest","release_id":f"kfm.published_release.flora.usda_plants.{a.snapshot_date}","domain":"flora","source_id":"usda_plants","source_uri":"https://plants.sc.egov.usda.gov/downloads","snapshot_date":a.snapshot_date,"generated_at":a.generated_at,"publication_state":"published","package_root":f"published/flora/usda_plants/{a.snapshot_date}","source_promoted_package_ref":f"promoted/flora/usda_plants/{a.snapshot_date}/promoted_package.json","public_outputs":outputs,"rights":{"license":"USDA / U.S. Public Domain","rightsHolder":"United States Department of Agriculture","policy_label":"public","citation_required":True,"citation_text":f"USDA PLANTS Database, snapshot {a.snapshot_date}."},"safety":{"contains_precise_coordinates":False,"contains_county_geometry":False,"contains_vector_tiles":False,"public_ui_safe":True},"status":"pass","reason_codes":["USDA_PLANTS_PUBLICATION_RELEASE_CREATED"]},'release_hash')
 write_json(proot/'release_manifest.json',rel)
 rroot=a.out_root/f'publication/flora/usda_plants/{a.snapshot_date}'
 rec=with_hash({"schema_version":"1.0.0","object_type":"usda_plants_publication_receipt","publication_receipt_id":f"kfm.publication_receipt.flora.usda_plants.{a.snapshot_date}","domain":"flora","source_id":"usda_plants","snapshot_date":a.snapshot_date,"generated_at":a.generated_at,"execution_plan_ref":str(a.execution_plan),"published_release_manifest_ref":f"published/flora/usda_plants/{a.snapshot_date}/release_manifest.json","published_items":[{"role":o['role'],"target_ref":o['path'],"sha256":o['sha256'],"status":"published"} for o in outputs],"publication_state":"published","status":"pass","reason_codes":["USDA_PLANTS_PUBLICATION_EXECUTED"]},'receipt_hash')
 write_json(rroot/'publication_receipt.json',rec)
if __name__=='__main__':main()
