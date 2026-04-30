from __future__ import annotations
import argparse,json,sys,shutil
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,validate,write_json,sha256_file

def main():
 p=argparse.ArgumentParser();p.add_argument('--published-root',type=Path,required=True);p.add_argument('--snapshot-date',required=True);p.add_argument('--generated-at',required=True);p.add_argument('--out-root',type=Path,required=True);a=p.parse_args()
 site=a.out_root/'site/flora/usda_plants'/a.snapshot_date
 (site/'assets').mkdir(parents=True,exist_ok=True);(site/'data').mkdir(parents=True,exist_ok=True)
 refs=['release_manifest.json','dataset_index.json','evidence_drawer_index.json','county_presence.json','map_descriptor.json','map/county_presence.geojson','map/map_style.json','hosting/static_host_handoff.json','hosting/cache_integrity_manifest.json']
 for r in refs:
  src=a.published_root/r;dst=site/'data'/r;dst.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(src,dst)
 (site/'assets/kfm-usda-plants.css').write_text('body{font-family:sans-serif;}\n')
 (site/'assets/kfm-usda-plants.js').write_text('console.log("KFM USDA PLANTS static artifact site");\n')
 links=''.join([f'<li><a href="data/{r}">{r}</a></li>' for r in refs])
 (site/'index.html').write_text(f'<html><body><h1>USDA PLANTS {a.snapshot_date}</h1><p>Attribution: USDA PLANTS Database.</p><p>County geometry authority attribution included from published artifacts.</p><ul>{links}</ul></body></html>')
 manifest={'snapshot_date':a.snapshot_date,'local_only':True,'data_refs':[f'data/{r}' for r in refs]};write_json(site/'manifest.json',manifest)
 files=[]
 for fp in sorted([x for x in site.rglob('*') if x.is_file()]): files.append({'path':str(fp.relative_to(site)),'sha256':sha256_file(fp)})
 bundle={'schema_version':'1.0.0','object_type':'usda_plants_static_site_bundle_manifest','domain':'flora','source_id':'usda_plants','snapshot_date':a.snapshot_date,'generated_at':a.generated_at,'bundle_id':f'kfm.static_site.bundle.flora.usda_plants.{a.snapshot_date}','site_root':str(site),'files':files,'status':'pass','reason_codes':['USDA_PLANTS_STATIC_SITE_BUNDLE_PASS']}
 bundle['bundle_hash']=canonical_hash(bundle,'bundle_hash');validate(ROOT/'schemas/flora/usda_plants_static_site_bundle_manifest.schema.json',bundle);write_json(site/'static_site_bundle_manifest.json',bundle)
if __name__=='__main__':main()
