from __future__ import annotations
import argparse,os,sys,urllib.request,urllib.error
from pathlib import Path
from html.parser import HTMLParser
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,write_json,validate,sha256_file
URI='https://plants.sc.egov.usda.gov/downloads';REQ={'checklist','state_distribution','county_distribution'}
class P(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.h=None;self.t=''
 def handle_starttag(self,t,a):
  if t=='a':self.h=dict(a).get('href','');self.t=''
 def handle_data(self,d):
  if self.h is not None:self.t+=d
 def handle_endtag(self,t):
  if t=='a' and self.h is not None:self.links.append((self.t.strip(),self.h.strip()));self.h=None

def role(lbl,href):
 s=(lbl+' '+href).lower()
 if 'checklist' in s:return 'checklist'
 if 'state' in s and 'distribution' in s:return 'state_distribution'
 if 'county' in s and 'distribution' in s:return 'county_distribution'
 return 'unknown'
def join(base,href):
 return href if href.startswith('http') else base.rstrip('/')+'/'+href.lstrip('/')
def fetch_head(url):
 req=urllib.request.Request(url,method='HEAD')
 with urllib.request.urlopen(req,timeout=20) as r:
  return r.status,r.headers.get('ETag'),r.headers.get('Last-Modified'),int(r.headers.get('Content-Length')) if r.headers.get('Content-Length') else None

def main():
 a=argparse.ArgumentParser();a.add_argument('--mode',default='scheduled_mock',choices=['scheduled_mock','scheduled_observe_only']);a.add_argument('--downloads-html',type=Path);a.add_argument('--source-uri',default=URI);a.add_argument('--previous-watch-state',type=Path);a.add_argument('--snapshot-date',required=True);a.add_argument('--generated-at');a.add_argument('--out-dir',type=Path,required=True);x=a.parse_args()
 g=x.generated_at or f"{x.snapshot_date}T00:00:00Z";allow=x.mode=='scheduled_observe_only' and os.getenv('KFM_ALLOW_SCHEDULED_OBSERVATION')=='1'
 reasons=['USDA_PLANTS_SCHEDULE_PUBLICATION_BLOCKED','USDA_PLANTS_SCHEDULE_PROMOTION_BLOCKED'];res=[];status='pass';changed=0;added=0;removed=0;failed=0
 prev={}
 if x.previous_watch_state and x.previous_watch_state.exists():
  import json; prev={(r['role'],r['url']):r for r in json.loads(x.previous_watch_state.read_text()).get('resources',[])}
 else: reasons.append('USDA_PLANTS_SCHEDULE_NO_PRIOR_STATE')
 links=[]
 try:
  if x.mode=='scheduled_mock':
   p=P();p.feed(x.downloads_html.read_text());links=p.links
  else:
   if not allow: raise RuntimeError('USDA_PLANTS_SCHEDULE_NETWORK_NOT_ALLOWED')
   with urllib.request.urlopen(x.source_uri,timeout=20) as r:html=r.read().decode('utf-8','ignore')
   p=P();p.feed(html);links=p.links
 except Exception:
  status='fail';reasons.append('USDA_PLANTS_SCHEDULE_DISCOVERY_FAILED');links=[]
 found=set()
 for lbl,h in links:
  rl=role(lbl,h);u=join(x.source_uri,h);found.add(rl);item={'role':rl,'url':u,'status':'observed','http_status':None,'etag':None,'last_modified':None,'content_length':None,'sha256':None,'reason_codes':[]}
  if x.mode=='scheduled_mock' and h.endswith('.csv'):
   fp=Path('tests/fixtures/flora/usda_plants/live_mock')/Path(h).name
   if fp.exists():item['sha256']=sha256_file(fp)
  if allow:
   try:
    hs,et,lm,cl=fetch_head(u);item.update({'http_status':hs,'etag':et,'last_modified':lm,'content_length':cl})
   except Exception:
    item['status']='failed';item['reason_codes']=['USDA_PLANTS_SCHEDULE_SOURCE_UNREACHABLE'];failed+=1
  pv=prev.get((rl,u))
  if pv and any([pv.get('etag')!=item.get('etag'),pv.get('last_modified')!=item.get('last_modified'),pv.get('content_length')!=item.get('content_length'),pv.get('sha256')!=item.get('sha256')]):
   changed+=1;reasons.append('USDA_PLANTS_SCHEDULE_RESOURCE_CHANGED')
  if not pv: added+=1
  if rl=='unknown' and not pv: reasons.append('USDA_PLANTS_SCHEDULE_UNKNOWN_RESOURCE_ADDED')
  res.append(item)
 prev_keys=set(prev);now_keys={(r['role'],r['url']) for r in res};removed=len(prev_keys-now_keys)
 for rname in REQ:
  if rname not in found:
   failed+=1;changed+=1;reasons.append('USDA_PLANTS_SCHEDULE_REQUIRED_RESOURCE_MISSING')
   res.append({'role':rname,'url':x.source_uri+'/'+rname+'.csv','status':'missing','http_status':None,'etag':None,'last_modified':None,'content_length':None,'sha256':None,'reason_codes':['USDA_PLANTS_SCHEDULE_REQUIRED_RESOURCE_MISSING']})
 obs={'schema_version':'1.0.0','object_type':'usda_plants_scheduled_observation','observation_id':f'kfm.scheduled_observation.flora.usda_plants.{g.replace(":","").replace("-","")}','domain':'flora','source_id':'usda_plants','source_uri':x.source_uri,'generated_at':g,'mode':x.mode,'network_mode':'scheduled_observation' if allow else 'disabled','ci':os.getenv('CI','').lower()=='true','publishes':False,'promotes':False,'creates_pr':False,'downloads_raw':False,'resources':sorted(res,key=lambda i:(i['role'],i['url'])),'change_summary':{'changed':(changed+added+removed+failed)>0,'added':added,'removed':removed,'changed_resources':changed,'failed_resources':failed},'status':'fail' if failed else status,'reason_codes':sorted(set(reasons))}
 obs['observation_hash']=canonical_hash(obs,'observation_hash')
 st={'schema_version':'1.0.0','object_type':'usda_plants_watch_state','watch_state_id':'kfm.watch_state.flora.usda_plants.latest','domain':'flora','source_id':'usda_plants','source_uri':x.source_uri,'last_observed_at':g,'last_snapshot_date':x.snapshot_date,'last_observation_ref':f'work/flora/usda_plants/scheduled/{x.snapshot_date}/scheduled_observation.json','last_alert_ref':None,'resources':[{'role':i['role'],'url':i['url'],'etag':i['etag'],'last_modified':i['last_modified'],'content_length':i['content_length'],'sha256':i['sha256'],'status':i['status']} for i in obs['resources']]}
 st['state_hash']=canonical_hash(st,'state_hash')
 validate(ROOT/'schemas/flora/usda_plants_scheduled_observation.schema.json',obs);validate(ROOT/'schemas/flora/usda_plants_watch_state.schema.json',st)
 write_json(x.out_dir/'scheduled_observation.json',obs);write_json(x.out_dir/'watch_state.json',st)
if __name__=='__main__':main()
