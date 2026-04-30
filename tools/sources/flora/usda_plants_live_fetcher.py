from __future__ import annotations
import argparse,os,sys,json,urllib.request,urllib.parse,re
from html.parser import HTMLParser
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,write_json,validate,sha256_file
URI='https://plants.sc.egov.usda.gov/downloads';REQ=['checklist','state_distribution','county_distribution']
class P(HTMLParser):
 def __init__(s): super().__init__();s.links=[]
 def handle_starttag(s,t,a):
  if t=='a':
   d=dict(a);h=d.get('href');
   if h:s.links.append(h)
def role(u):
 n=Path(urllib.parse.urlparse(u).path).name
 return n[:-4] if n in [f'{r}.csv' for r in REQ] else 'unknown'
def main():
 a=argparse.ArgumentParser();
 for k in ['source-uri','snapshot-date','out-dir']: a.add_argument('--'+k,required=True)
 a.add_argument('--generated-at',default='2026-04-30T00:00:00Z');a.add_argument('--plan-only',action='store_true');a.add_argument('--allow-network',action='store_true');a.add_argument('--operator-ack',action='store_true');a.add_argument('--allow-ci-network',action='store_true');a.add_argument('--allow-non-usda-source-for-tests',action='store_true')
 x=a.parse_args();out=Path(x.out_dir);out.mkdir(parents=True,exist_ok=True)
 man=x.allow_network and x.operator_ack and os.getenv('KFM_ALLOW_NETWORK')=='1'
 ci=os.getenv('CI','').lower()=='true';reasons=[]
 if x.allow_network and not x.operator_ack: reasons.append('USDA_PLANTS_LIVE_OPERATOR_ACK_MISSING')
 if x.allow_network and os.getenv('KFM_ALLOW_NETWORK')!='1': reasons.append('USDA_PLANTS_LIVE_NETWORK_NOT_ALLOWED')
 if ci and x.allow_network and not (x.allow_ci_network and os.getenv('KFM_ALLOW_CI_NETWORK')=='1' and urllib.parse.urlparse(x.source_uri).hostname in ('127.0.0.1','localhost')): reasons.append('USDA_PLANTS_LIVE_CI_NETWORK_REFUSED')
 if x.allow_network and urllib.parse.urlparse(x.source_uri).hostname not in ('plants.sc.egov.usda.gov','127.0.0.1','localhost'): reasons.append('USDA_PLANTS_LIVE_NON_USDA_SOURCE_REFUSED')
 nm='manual_enabled' if man and not reasons and not x.plan_only else 'disabled'
 plan={'schema_version':'1.0.0','object_type':'usda_plants_live_fetch_plan','plan_id':f'kfm.live_fetch_plan.flora.usda_plants.{x.snapshot_date}','domain':'flora','source_id':'usda_plants','source_uri':x.source_uri,'snapshot_date':x.snapshot_date,'generated_at':x.generated_at,'network_mode':nm,'operator_acknowledgement':bool(x.operator_ack),'ci_allowed':bool(x.allow_ci_network),'target_roles':REQ,'download_targets':[{'role':r,'url':urllib.parse.urljoin(x.source_uri,f'{r}.csv'),'file_name':f'{r}.csv','required':True} for r in REQ],'guards':{'requires_allow_network_flag':True,'requires_operator_ack':True,'refuses_ci_by_default':True,'writes_raw_only':True,'publishes':False,'promotes':False},'reason_codes':sorted(set(reasons))}
 plan['plan_hash']=canonical_hash(plan,'plan_hash');write_json(out/'live_fetch_plan.json',plan)
 if x.plan_only or reasons: return 0 if x.plan_only else 2
 h=P();h.feed(urllib.request.urlopen(x.source_uri).read().decode())
 files=[];status='pass'
 for href in h.links:
  u=urllib.parse.urljoin(x.source_uri,href);r=role(u)
  if r=='unknown':continue
  p=out/f'{r}.csv'
  with urllib.request.urlopen(u) as resp, p.open('wb') as f:
   ct=resp.headers.get('Content-Type','')
   if 'csv' not in ct and 'text/plain' not in ct: status='quarantined';reasons.append('USDA_PLANTS_LIVE_BAD_CONTENT_TYPE')
   while True:
    c=resp.read(65536)
    if not c:break
    f.write(c)
   hs=sha256_file(p)
   files.append({'role':r,'url':u,'path':f'raw/flora/usda_plants/{x.snapshot_date}/{p.name}','status':'downloaded','http_status':200,'size_bytes':p.stat().st_size,'sha256':hs,'etag':resp.headers.get('ETag'),'last_modified':resp.headers.get('Last-Modified')})
 for r in REQ:
  if r not in [f['role'] for f in files]: status='fail';reasons.append('USDA_PLANTS_LIVE_REQUIRED_TARGET_MISSING')
 rec={'schema_version':'1.0.0','object_type':'usda_plants_live_fetch_receipt','receipt_id':f'kfm.live_fetch_receipt.flora.usda_plants.{x.snapshot_date}','domain':'flora','source_id':'usda_plants','source_uri':x.source_uri,'snapshot_date':x.snapshot_date,'generated_at':x.generated_at,'network_mode':'manual_enabled','ci':ci,'plan_ref':f'raw/flora/usda_plants/{x.snapshot_date}/live_fetch_plan.json','downloaded_files':files,'status':status,'reason_codes':sorted(set(reasons)),'quarantine_refs':[]}
 rec['receipt_hash']=canonical_hash(rec,'receipt_hash');write_json(out/'live_fetch_receipt.json',rec)
 return 0 if status=='pass' else 2
if __name__=='__main__': raise SystemExit(main())
