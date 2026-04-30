from __future__ import annotations
import argparse,shutil,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,write_json,validate,sha256_file
REQ=['checklist','state_distribution','county_distribution']
URI='https://plants.sc.egov.usda.gov/downloads'
def main():
 a=argparse.ArgumentParser();a.add_argument('--raw-dir',type=Path,required=True);a.add_argument('--snapshot-date',required=True);a.add_argument('--generated-at',required=True);a.add_argument('--out-dir',type=Path,required=True);x=a.parse_args()
 x.out_dir.mkdir(parents=True,exist_ok=True)
 raw=[];reasons=[];qrefs=[]
 for f in sorted(x.raw_dir.iterdir()):
  if not f.is_file():continue
  role=f.stem if f.name in [r+'.csv' for r in REQ] else 'unknown'
  dest=x.out_dir/f.name;shutil.copy2(f,dest)
  st='accepted' if role!='unknown' and f.suffix=='.csv' else 'quarantined'
  if role=='unknown': reasons.append('USDA_PLANTS_RAW_UNKNOWN_FILE')
  s=dest.stat().st_size
  if s==0: reasons.append('USDA_PLANTS_RAW_EMPTY_FILE')
  raw.append({'role':role,'path':f'raw/flora/usda_plants/{x.snapshot_date}/{f.name}','file_name':f.name,'media_type':'text/csv' if f.suffix=='.csv' else 'application/octet-stream','size_bytes':s,'sha256':sha256_file(dest),'required':role in REQ,'status':st})
 miss=[r for r in REQ if not (x.raw_dir/f'{r}.csv').exists()]
 if miss: reasons.append('USDA_PLANTS_RAW_MISSING_REQUIRED_FILE')
 status='fail' if miss else ('quarantined' if any(r['role']=='unknown' for r in raw) else 'pass')
 m={'schema_version':'1.0.0','object_type':'usda_plants_raw_snapshot_manifest','manifest_id':f'kfm.raw_snapshot.flora.usda_plants.{x.snapshot_date}','domain':'flora','source_id':'usda_plants','source_uri':URI,'network_mode':'disabled','snapshot_date':x.snapshot_date,'generated_at':x.generated_at,'raw_files':raw,'required_roles':REQ,'missing_roles':miss,'quarantine_refs':qrefs,'status':status,'reason_codes':sorted(set(reasons))}
 m['manifest_hash']=canonical_hash(m,'manifest_hash');validate(ROOT/'schemas/flora/usda_plants_raw_snapshot_manifest.schema.json',m);write_json(x.out_dir/'raw_snapshot_manifest.json',m)
 if status=='quarantined':
  q={'schema_version':'1.0.0','object_type':'usda_plants_quarantine_report','quarantine_id':f'kfm.quarantine.flora.usda_plants.{x.snapshot_date}','domain':'flora','source_id':'usda_plants','snapshot_date':x.snapshot_date,'generated_at':x.generated_at,'quarantined_refs':[r['path'] for r in raw if r['role']=='unknown'],'reason_codes':['USDA_PLANTS_RAW_UNKNOWN_FILE'],'recommended_action':'review_required','status':'open'}
  q['quarantine_hash']=canonical_hash(q,'quarantine_hash');validate(ROOT/'schemas/flora/usda_plants_quarantine_report.schema.json',q);write_json(x.out_dir/'quarantine_report.json',q)
if __name__=='__main__':main()
