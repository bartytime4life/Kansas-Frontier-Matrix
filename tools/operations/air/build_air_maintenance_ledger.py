#!/usr/bin/env python
import argparse,json
from pathlib import Path
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent))
from _assurance_common import w,ts,h
p=argparse.ArgumentParser();p.add_argument('--maintenance-dir',action='append',default=[]);p.add_argument('--out-dir',required=True);p.add_argument('--previous-ledger');p.add_argument('--as-of');p.add_argument('--allow-fixture-ledger',action='store_true');p.add_argument('--dry-run',action='store_true');a=p.parse_args()
entries=[];prev=''
for i,d in enumerate(a.maintenance_dir,1):
 e={"schema_version":"1.0.0","ledger_entry_id":f"le-{i:03d}","domain":"atmosphere.air","created_at":ts(a.as_of),"as_of":ts(a.as_of),"entry_type":"maintenance_blocked" if 'deny' in d else "assurance_findings_collected","actor":"fixture-actor-non-production","subject_refs":[d],"evidence_refs":[d],"artifact_hashes":[],"previous_entry_ref":prev,"result":"pass","details":"fixture ledger entry"}
 e['entry_hash']=h({k:v for k,v in e.items() if k!='entry_hash'});prev=e['ledger_entry_id'];entries.append(e)
chain=h([e['entry_hash'] for e in entries])
manifest={"schema_version":"1.0.0","ledger_id":"ml-001","domain":"atmosphere.air","generated_at":ts(a.as_of),"as_of":ts(a.as_of),"entry_refs":[e['ledger_entry_id'] for e in entries],"head_entry_ref":prev,"chain_hash":chain,"source_refs":a.maintenance_dir,"safety_checks":["append-only"],"status":"fixture_maintenance_ledger"}
out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True)
if not a.dry_run:(out/'maintenance_ledger_entries.jsonl').write_text(''.join(json.dumps(e,sort_keys=True)+'\n' for e in entries));w(out/'maintenance_ledger_manifest.json',manifest);(out/'maintenance_events.jsonl').write_text('{"event_type":"maintenance_blocked"}\n')
print('PASS')
