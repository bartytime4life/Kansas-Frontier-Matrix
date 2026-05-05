from __future__ import annotations
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,validate,write_json,sha256_file


def main():
 p=argparse.ArgumentParser();p.add_argument('--published-root',type=Path,required=True);p.add_argument('--snapshot-date',required=True);p.add_argument('--generated-at',required=True);p.add_argument('--requested-by',required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
 arts=['release_manifest.json','dataset_index.json','evidence_drawer_index.json','county_presence.json','map_descriptor.json','map/county_presence.geojson','map/map_style.json','hosting/static_host_handoff.json','hosting/cache_integrity_manifest.json']
 refs=[str(Path(a.published_root)/x) for x in arts]
 o={'schema_version':'1.0.0','object_type':'usda_plants_static_deployment_request','domain':'flora','source_id':'usda_plants','snapshot_date':a.snapshot_date,'generated_at':a.generated_at,'request_id':f'kfm.static_deploy.request.flora.usda_plants.{a.snapshot_date}','published_root':str(a.published_root),'requested_by':a.requested_by,'artifacts':refs,'status':'pass','reason_codes':['USDA_PLANTS_STATIC_DEPLOYMENT_REQUEST_PASS']}
 o['request_hash']=canonical_hash(o,'request_hash');validate(ROOT/'schemas/flora/usda_plants_static_deployment_request.schema.json',o);write_json(a.out,o)
if __name__=='__main__':main()
