from __future__ import annotations
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,write_json,validate

a=argparse.ArgumentParser();a.add_argument('--observation',type=Path,required=True);a.add_argument('--generated-at');a.add_argument('--out',type=Path,required=True);x=a.parse_args()
o=json.loads(x.observation.read_text());g=x.generated_at or o['generated_at'];snap=o['generated_at'][:10]
r=[{'role':i['role'],'url':i['url'],'etag':i['etag'],'last_modified':i['last_modified'],'content_length':i['content_length'],'sha256':i['sha256'],'status':i['status']} for i in sorted(o['resources'],key=lambda i:(i['role'],i['url']))]
s={'schema_version':'1.0.0','object_type':'usda_plants_watch_state','watch_state_id':'kfm.watch_state.flora.usda_plants.latest','domain':'flora','source_id':'usda_plants','source_uri':o['source_uri'],'last_observed_at':g,'last_snapshot_date':snap,'last_observation_ref':f'work/flora/usda_plants/scheduled/{snap}/scheduled_observation.json','last_alert_ref':None,'resources':r}
s['state_hash']=canonical_hash(s,'state_hash');validate(ROOT/'schemas/flora/usda_plants_watch_state.schema.json',s);write_json(x.out,s)
