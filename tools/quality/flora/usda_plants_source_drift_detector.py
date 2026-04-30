from __future__ import annotations
import argparse,csv,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,write_json,validate
REQ=['checklist','state_distribution','county_distribution']
def main():
 a=argparse.ArgumentParser();a.add_argument('--raw-dir',type=Path,required=True);a.add_argument('--column-contract',type=Path,required=True);a.add_argument('--snapshot-date',required=True);a.add_argument('--generated-at',required=True);a.add_argument('--out',type=Path,required=True);x=a.parse_args()
 c=json.loads(x.column_contract.read_text());t=c['tables'];res=[];reasons=[];q=False
 for f in sorted(x.raw_dir.glob('*.csv')):
  table=f.stem if f.stem in REQ else 'unknown';status='pass';rr=[];missing=[];unexp=[]
  with f.open() as h:
   hdr=h.readline().strip('\n\r')
  if not hdr: status='fail'; rr.append('USDA_PLANTS_DRIFT_EMPTY_TABLE')
  cols=hdr.split(',') if hdr else []
  if len(cols)!=len(set(cols)): status='fail'; rr.append('USDA_PLANTS_DRIFT_DUPLICATE_COLUMN')
  if table=='unknown': status='quarantined'; rr.append('USDA_PLANTS_DRIFT_UNKNOWN_TABLE'); q=True
  else:
   req=t[table]['required_columns']; missing=[c for c in req if c not in cols]
   if missing: status='fail'; rr.append('USDA_PLANTS_DRIFT_MISSING_REQUIRED_COLUMN'); q=True
   unexp=[c for c in cols if c not in req+t[table]['optional_columns']]
   if unexp and status=='pass': status='warn'; rr.append('USDA_PLANTS_DRIFT_UNEXPECTED_COLUMN')
  res.append({'table':table,'path':f'raw/flora/usda_plants/{x.snapshot_date}/{f.name}','required_columns_present':len(missing)==0,'missing_required_columns':missing,'unexpected_columns':unexp,'status':status,'reason_codes':rr})
  reasons.extend(rr)
 st='fail' if any(r['status']=='fail' for r in res) else ('warn' if any(r['status']=='warn' for r in res) else 'pass')
 o={'schema_version':'1.0.0','object_type':'usda_plants_source_drift_report','drift_report_id':f'kfm.source_drift.flora.usda_plants.{x.snapshot_date}','domain':'flora','source_id':'usda_plants','snapshot_date':x.snapshot_date,'generated_at':x.generated_at,'contract_ref':'schemas/flora/usda_plants_column_contract.schema.json','table_results':res,'status':st,'reason_codes':sorted(set(reasons)),'quarantine_required':q}
 o['drift_hash']=canonical_hash(o,'drift_hash');validate(ROOT/'schemas/flora/usda_plants_source_drift_report.schema.json',o);write_json(x.out,o)
if __name__=='__main__':main()
