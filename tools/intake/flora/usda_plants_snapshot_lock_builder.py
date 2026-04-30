from __future__ import annotations
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,write_json
REQ=['checklist','state_distribution','county_distribution']
def main():
 a=argparse.ArgumentParser();a.add_argument('--raw-snapshot-manifest',required=True);a.add_argument('--live-fetch-receipt');a.add_argument('--operator-intake-receipt');a.add_argument('--snapshot-date',required=True);a.add_argument('--generated-at',required=True);a.add_argument('--out',required=True);x=a.parse_args()
 m=json.loads(Path(x.raw_snapshot_manifest).read_text()); reasons=[];state='locked'
 if m.get('status')=='quarantined': state='quarantined';reasons.append('USDA_PLANTS_LOCK_QUARANTINE_PRESENT')
 if m.get('status')!='pass': state='failed';reasons.append('USDA_PLANTS_LOCK_RAW_MANIFEST_NOT_PASS')
 raw={r['role']:r for r in m.get('raw_files',[])};locked=[]
 for r in REQ:
  if r not in raw: reasons.append('USDA_PLANTS_LOCK_MISSING_REQUIRED_ROLE'); state='failed';continue
  if not raw[r].get('sha256'): reasons.append('USDA_PLANTS_LOCK_MISSING_CHECKSUM');state='failed';continue
  locked.append({'role':r,'path':raw[r]['path'],'sha256':raw[r]['sha256'],'size_bytes':raw[r].get('size_bytes',0)})
 o={'schema_version':'1.0.0','object_type':'usda_plants_snapshot_lock','lock_id':f'kfm.snapshot_lock.flora.usda_plants.{x.snapshot_date}','domain':'flora','source_id':'usda_plants','snapshot_date':x.snapshot_date,'generated_at':x.generated_at,'raw_snapshot_manifest_ref':m.get('manifest_ref',f'raw/flora/usda_plants/{x.snapshot_date}/raw_snapshot_manifest.json'),'live_fetch_receipt_ref':x.live_fetch_receipt or x.operator_intake_receipt or '','locked_files':locked,'lock_state':state,'eligible_for_processing':state=='locked' and not reasons,'reason_codes':sorted(set(reasons))}
 o['lock_hash']=canonical_hash(o,'lock_hash');write_json(Path(x.out),o)
 return 0 if state=='locked' else 2
if __name__=='__main__':raise SystemExit(main())
