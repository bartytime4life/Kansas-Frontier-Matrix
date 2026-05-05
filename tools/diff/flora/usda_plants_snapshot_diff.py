from __future__ import annotations
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,write_json

def main():
 a=argparse.ArgumentParser();a.add_argument('--base-lock');a.add_argument('--head-lock');a.add_argument('--base-proof');a.add_argument('--head-proof');a.add_argument('--generated-at',required=True);a.add_argument('--out',required=True);x=a.parse_args()
 mode1=bool(x.base_lock and x.head_lock);mode2=bool(x.base_proof and x.head_proof)
 if mode1==mode2: print('USDA_PLANTS_DIFF_MODE_AMBIGUOUS'); return 2
 added=[];removed=[];changed=[];unch=[]
 if mode1:
  b=json.loads(Path(x.base_lock).read_text());h=json.loads(Path(x.head_lock).read_text());bm={i['role']:i for i in b['locked_files']};hm={i['role']:i for i in h['locked_files']}
  for k in sorted(set(bm)|set(hm)):
   if k not in bm: added.append({'id':k,'plants_symbol':k,'spec_hash':hm[k]['sha256']})
   elif k not in hm: removed.append({'id':k,'plants_symbol':k,'spec_hash':bm[k]['sha256']})
   elif bm[k]['sha256']!=hm[k]['sha256']: changed.append({'id':k,'plants_symbol':k,'base_spec_hash':bm[k]['sha256'],'head_spec_hash':hm[k]['sha256']})
   else: unch.append({'id':k,'plants_symbol':k,'spec_hash':bm[k]['sha256']})
  bs=b['snapshot_date'];hs=h['snapshot_date'];br=x.base_lock;hr=x.head_lock
 else:
  b=json.loads(Path(x.base_proof).read_text());h=json.loads(Path(x.head_proof).read_text());bm={i['id']:i for i in b['entries']};hm={i['id']:i for i in h['entries']}
  for k in sorted(set(bm)|set(hm)):
   if k not in bm: added.append(hm[k])
   elif k not in hm: removed.append(bm[k])
   elif bm[k]['spec_hash']!=hm[k]['spec_hash']: changed.append({'id':k,'plants_symbol':bm[k].get('plants_symbol'),'base_spec_hash':bm[k]['spec_hash'],'head_spec_hash':hm[k]['spec_hash']})
   else: unch.append(bm[k])
  bs=b.get('snapshot_date','base');hs=h.get('snapshot_date','head');br=x.base_proof;hr=x.head_proof
 o={'schema_version':'1.0.0','object_type':'usda_plants_snapshot_diff','diff_id':f'kfm.snapshot_diff.flora.usda_plants.{hs}','domain':'flora','source_id':'usda_plants','generated_at':x.generated_at,'base_snapshot_date':bs,'head_snapshot_date':hs,'base_ref':br,'head_ref':hr,'summary':{'added':len(added),'removed':len(removed),'changed':len(changed),'unchanged':len(unch)},'added':added,'removed':removed,'changed':changed,'unchanged':unch,'status':'pass','reason_codes':[]}
 o['diff_hash']=canonical_hash(o,'diff_hash');write_json(Path(x.out),o)
if __name__=='__main__': main()
