from __future__ import annotations
import argparse,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,write_json,validate,sha256_file
a=argparse.ArgumentParser();a.add_argument('--artifact-name',required=True);a.add_argument('--root-dir',type=Path,required=True);a.add_argument('--generated-at',required=True);a.add_argument('--out',type=Path,required=True);x=a.parse_args()
refs=[]
for f in ['scheduled_observation.json','watch_state.json','change_alert.json','reviewer_queue.json']:
 p=x.root_dir/f;rel=f'work/flora/usda_plants/scheduled/{x.root_dir.name}/{f}'
 if rel.startswith('published/'):raise SystemExit(2)
 refs.append({'role':f.replace('.json',''),'path':rel,'sha256':sha256_file(p)})
b={'schema_version':'1.0.0','object_type':'usda_plants_artifact_bundle','bundle_id':f"kfm.artifact_bundle.flora.usda_plants.{x.generated_at.replace(':','').replace('-','')}",'domain':'flora','source_id':'usda_plants','generated_at':x.generated_at,'artifact_name':x.artifact_name,'artifact_only':True,'publication_state':'not_published','promotion_state':'not_promoted','refs':refs,'status':'pass','reason_codes':[]}
b['bundle_hash']=canonical_hash(b,'bundle_hash');validate(ROOT/'schemas/flora/usda_plants_artifact_bundle.schema.json',b);write_json(x.out,b)
