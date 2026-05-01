#!/usr/bin/env python3
import argparse,json,hashlib
from pathlib import Path
from datetime import datetime,timezone
now=lambda: datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')

def main():
 p=argparse.ArgumentParser();p.add_argument('--materialization-dir',action='append',default=[]);p.add_argument('--out-dir',required=True);p.add_argument('--previous-ledger');p.add_argument('--as-of');p.add_argument('--allow-fixture-ledger',action='store_true');p.add_argument('--dry-run',action='store_true');a=p.parse_args();asof=a.as_of or now();
 out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True); entries=[]; prev=None
 for i,d in enumerate(a.materialization_dir,1):
  c={'schema_version':'v1','ledger_entry_id':f'e-{i}','domain':'atmosphere.air','created_at':now(),'as_of':asof,'entry_type':'materialization_plan_created','actor':'fixture-non-production','subject_refs':[d],'evidence_refs':[],'artifact_hashes':{},'previous_entry_ref':prev,'result':'pass','details':{}}
  h=hashlib.sha256(json.dumps(c,sort_keys=True,separators=(',',':')).encode()).hexdigest();c['entry_hash']=h;prev=f'e-{i}';entries.append(c)
 chain=hashlib.sha256(''.join(e['entry_hash'] for e in entries).encode()).hexdigest();man={'schema_version':'v1','ledger_id':'ml-1','domain':'atmosphere.air','generated_at':now(),'as_of':asof,'entry_refs':[f"reentry_publication_materialization_ledger_entries.jsonl#{e['ledger_entry_id']}" for e in entries],'head_entry_ref':entries[-1]['ledger_entry_id'] if entries else None,'chain_hash':chain,'source_refs':a.materialization_dir,'safety_checks':{'append_only':True},'status':'fixture_publication_materialization_ledger'}
 if not a.dry_run:(out/'reentry_publication_materialization_ledger_entries.jsonl').write_text(''.join(json.dumps(e,sort_keys=True)+'\n' for e in entries));(out/'reentry_publication_materialization_ledger_manifest.json').write_text(json.dumps(man,indent=2,sort_keys=True)+'\n')
 print('PASS')
if __name__=='__main__': main()
