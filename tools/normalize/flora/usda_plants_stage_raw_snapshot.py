from __future__ import annotations
import argparse,csv,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,write_json,validate,sha256_file
ORDER={'checklist':['symbol','scientificName','nationalCommonName','family','nativeStatus','growthHabit','wetlandStatus'],'state_distribution':['symbol','state','presence'],'county_distribution':['symbol','fips','presence']}
def main():
 a=argparse.ArgumentParser();a.add_argument('--raw-dir',type=Path,required=True);a.add_argument('--raw-snapshot-manifest',type=Path,required=True);a.add_argument('--drift-report',type=Path,required=True);a.add_argument('--snapshot-date',required=True);a.add_argument('--generated-at',required=True);a.add_argument('--out-dir',type=Path,required=True);x=a.parse_args();x.out_dir.mkdir(parents=True,exist_ok=True)
 raw=json.loads(x.raw_snapshot_manifest.read_text());dr=json.loads(x.drift_report.read_text())
 if raw['status']!='pass': raise SystemExit('USDA_PLANTS_STAGE_RAW_MANIFEST_NOT_PASS')
 if dr['status']=='fail': raise SystemExit('USDA_PLANTS_STAGE_DRIFT_NOT_PASS')
 if dr['quarantine_required']: raise SystemExit('USDA_PLANTS_STAGE_QUARANTINE_REQUIRED')
 staged=[]
 for role,cols in ORDER.items():
  rows=[]
  with (x.raw_dir/f'{role}.csv').open() as f:
   for r in csv.DictReader(f):
    o={k:(r.get(k,'').strip()) for k in cols};o['symbol']=o['symbol'].upper()
    if 'state' in o:o['state']=o['state'].upper()
    if 'fips' in o:
      if o['fips'] and not o['fips'].isdigit(): raise SystemExit('USDA_PLANTS_STAGE_BAD_FIPS')
      o['fips']=o['fips'].zfill(5)
    rows.append(o)
  sortk={'checklist':lambda r:(r['symbol'],),'state_distribution':lambda r:(r['symbol'],r['state']),'county_distribution':lambda r:(r['symbol'],r['fips'])}[role]
  rows=sorted(rows,key=sortk)
  p=x.out_dir/f'{role}.csv'
  with p.open('w',newline='') as f:
   w=csv.DictWriter(f,fieldnames=cols);w.writeheader();w.writerows(rows)
  staged.append({'role':role,'path':f'work/flora/usda_plants/{x.snapshot_date}/staged/{role}.csv','sha256':sha256_file(p),'row_count':len(rows)})
 m={'schema_version':'1.0.0','object_type':'usda_plants_staged_input_manifest','manifest_id':f'kfm.staged_input.flora.usda_plants.{x.snapshot_date}','domain':'flora','source_id':'usda_plants','snapshot_date':x.snapshot_date,'generated_at':x.generated_at,'network_mode':'disabled','raw_snapshot_manifest_ref':f'raw/flora/usda_plants/{x.snapshot_date}/raw_snapshot_manifest.json','drift_report_ref':f'work/flora/usda_plants/{x.snapshot_date}/source_drift_report.json','staged_files':staged,'status':'pass','reason_codes':[]}
 m['manifest_hash']=canonical_hash(m,'manifest_hash');validate(ROOT/'schemas/flora/usda_plants_staged_input_manifest.schema.json',m);write_json(x.out_dir/'staged_input_manifest.json',m)
if __name__=='__main__':main()
