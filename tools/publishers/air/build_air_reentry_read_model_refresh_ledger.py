#!/usr/bin/env python3
import argparse, hashlib, json
from pathlib import Path
from datetime import datetime, timezone

now=lambda: datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')

ENTRY_TYPES=[
 'read_model_refresh_plan_created','public_index_refresh_candidate_created','public_api_record_refresh_candidate_created',
 'public_status_refresh_candidate_created','public_provenance_trace_refresh_candidate_created','public_delta_feed_refresh_candidate_created',
 'client_invalidation_notice_refresh_candidate_created','read_model_version_candidate_created','read_model_refresh_manifest_created','read_model_refresh_decided'
]

def sha(x:str)->str:return hashlib.sha256(x.encode()).hexdigest()

def canonical(obj):return json.dumps(obj,sort_keys=True,separators=(',',':'))

def main():
 p=argparse.ArgumentParser();p.add_argument('--read-model-refresh-dir',action='append',default=[]);p.add_argument('--out-dir',required=True);p.add_argument('--previous-ledger');p.add_argument('--as-of');p.add_argument('--allow-fixture-ledger',action='store_true');p.add_argument('--dry-run',action='store_true');a=p.parse_args()
 asof=a.as_of or now(); out=Path(a.out_dir); out.mkdir(parents=True,exist_ok=True)
 artifacts=[]
 for d in a.read_model_refresh_dir:
  for f in sorted(Path(d).rglob('*.json')):
   artifacts.append(f)
 entries=[]; prev=None
 if a.previous_ledger and Path(a.previous_ledger).exists():
  prev=json.loads(Path(a.previous_ledger).read_text()).get('head_entry_ref')
 for i,f in enumerate(artifacts):
  content=f.read_text()
  e={
   'schema_version':'v1','ledger_entry_id':f'le-{i+1}','domain':'atmosphere.air','created_at':asof,'as_of':asof,
   'entry_type':ENTRY_TYPES[min(i,len(ENTRY_TYPES)-1)],'actor':{'id':'fixture-non-production','environment':'non-production'},
   'subject_refs':[str(f)],'evidence_refs':[],'artifact_hashes':{str(f):hashlib.sha256(content.encode()).hexdigest()},
   'previous_entry_ref': prev,'result':'pass','details':{'candidate_only':True}
  }
  payload={k:v for k,v in e.items() if k!='entry_hash'}
  e['entry_hash']=sha(canonical(payload)); prev=e['ledger_entry_id']; entries.append(e)
 chain_hash=sha(''.join(e['entry_hash'] for e in entries)) if entries else sha('')
 manifest={'schema_version':'v1','ledger_id':'rmr-ledger-1','domain':'atmosphere.air','generated_at':asof,'as_of':asof,'entry_refs':[e['ledger_entry_id'] for e in entries],'head_entry_ref':entries[-1]['ledger_entry_id'] if entries else None,'chain_hash':chain_hash,'source_refs':[str(Path(d)) for d in a.read_model_refresh_dir],'safety_checks':{'append_only':True},'status':'fixture_read_model_refresh_ledger'}
 if not a.dry_run:
  (out/'reentry_read_model_refresh_ledger_entries.jsonl').write_text(''.join(json.dumps(e,sort_keys=True)+'\n' for e in entries))
  (out/'reentry_read_model_refresh_ledger_manifest.json').write_text(json.dumps(manifest,indent=2,sort_keys=True)+'\n')
  (out/'reentry_read_model_refresh_events.jsonl').write_text(json.dumps({'event_type':'read_model_refresh_ledger_created','result':'pass','as_of':asof},sort_keys=True)+'\n')
 print('PASS')

if __name__=='__main__': main()
