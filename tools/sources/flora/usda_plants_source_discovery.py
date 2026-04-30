from __future__ import annotations
import argparse,sys
from pathlib import Path
from html.parser import HTMLParser
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,write_json,validate
URI='https://plants.sc.egov.usda.gov/downloads'
class P(HTMLParser):
    def __init__(self):super().__init__();self.links=[];self.href=None;self.txt=''
    def handle_starttag(self,t,a):
        if t=='a':self.href=dict(a).get('href','');self.txt=''
    def handle_data(self,d):
        if self.href is not None:self.txt+=d
    def handle_endtag(self,t):
        if t=='a' and self.href is not None:self.links.append((self.txt.strip(),self.href.strip()));self.href=None

def r(lbl,href):
 s=(lbl+' '+href).lower()
 if 'checklist' in s:return 'checklist'
 if 'state' in s and 'distribution' in s:return 'state_distribution'
 if 'county' in s and 'distribution' in s:return 'county_distribution'
 return 'unknown'

def main():
 a=argparse.ArgumentParser();a.add_argument('--downloads-html',type=Path,required=True);a.add_argument('--snapshot-date',required=True);a.add_argument('--generated-at',required=True);a.add_argument('--out',type=Path,required=True);x=a.parse_args()
 if not x.downloads_html.exists(): raise SystemExit('USDA_PLANTS_DISCOVERY_HTML_MISSING')
 p=P();p.feed(x.downloads_html.read_text())
 d=[]
 for lbl,href in p.links:
  role=r(lbl,href)
  d.append({'resource_role':role,'label':lbl,'href':href,'media_type':'text/csv' if href.endswith('.csv') else 'application/octet-stream','required':role in {'checklist','state_distribution','county_distribution'}})
 found={i['resource_role'] for i in d};warn=[]
 if not {'checklist','state_distribution','county_distribution'}.issubset(found):warn.append('USDA_PLANTS_DISCOVERY_REQUIRED_RESOURCE_MISSING')
 o={'schema_version':'1.0.0','object_type':'usda_plants_source_discovery','discovery_id':f'kfm.source_discovery.flora.usda_plants.{x.snapshot_date}','domain':'flora','source_id':'usda_plants','source_uri':URI,'network_mode':'disabled','snapshot_date':x.snapshot_date,'generated_at':x.generated_at,'discovered_resources':d,'warnings':warn}
 o['discovery_hash']=canonical_hash(o,'discovery_hash');validate(ROOT/'schemas/flora/usda_plants_source_discovery.schema.json',o);write_json(x.out,o)
if __name__=='__main__':main()
