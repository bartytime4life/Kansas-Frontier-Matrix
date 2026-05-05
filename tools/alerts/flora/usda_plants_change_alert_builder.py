from __future__ import annotations
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,write_json,validate
REQ={'checklist','state_distribution','county_distribution'}
a=argparse.ArgumentParser();a.add_argument('--observation',type=Path,required=True);a.add_argument('--previous-watch-state',type=Path);a.add_argument('--current-watch-state',type=Path,required=True);a.add_argument('--generated-at',required=True);a.add_argument('--out',type=Path,required=True);x=a.parse_args()
o=json.loads(x.observation.read_text());c=json.loads(x.current_watch_state.read_text());p=json.loads(x.previous_watch_state.read_text()) if x.previous_watch_state and x.previous_watch_state.exists() else None
sev='none';rc=[];review=False
if p is None: sev='info';rc.append('USDA_PLANTS_ALERT_NO_PRIOR_STATE')
pm={(i['role'],i['url']):i for i in (p.get('resources',[]) if p else [])}
for v in c['resources']:
 k=(v['role'],v['url']);pv=pm.get(k)
 if v['status'] in ('missing','failed') and v['role'] in REQ:sev='critical';review=True;rc.append('USDA_PLANTS_ALERT_REQUIRED_RESOURCE_FAILED')
 if pv and any([pv.get('etag')!=v.get('etag'),pv.get('last_modified')!=v.get('last_modified'),pv.get('content_length')!=v.get('content_length'),pv.get('sha256')!=v.get('sha256')]) and v['role'] in REQ and sev!='critical':sev='warning';review=True;rc.append('USDA_PLANTS_ALERT_REQUIRED_RESOURCE_CHANGED')
 if not pv and v['role']=='unknown' and sev in ('none','info'):sev='info';review=True;rc.append('USDA_PLANTS_ALERT_UNKNOWN_RESOURCE_ADDED')
ao={'schema_version':'1.0.0','object_type':'usda_plants_change_alert','alert_id':f"kfm.change_alert.flora.usda_plants.{x.generated_at.replace(':','').replace('-','')}",'domain':'flora','source_id':'usda_plants','source_uri':o['source_uri'],'generated_at':x.generated_at,'severity':sev,'requires_human_review':review,'observation_ref':f"work/flora/usda_plants/scheduled/{x.generated_at[:10]}/scheduled_observation.json",'previous_watch_state_ref':None if p is None else str(x.previous_watch_state),'current_watch_state_ref':str(x.current_watch_state),'findings':[],'recommended_actions':[],'publication_blocked':True,'promotion_blocked':True,'status':'fail' if sev=='critical' else ('warn' if sev in ('info','warning') else 'pass'),'reason_codes':sorted(set(rc))}
ao['alert_hash']=canonical_hash(ao,'alert_hash');validate(ROOT/'schemas/flora/usda_plants_change_alert.schema.json',ao);write_json(x.out,ao)
