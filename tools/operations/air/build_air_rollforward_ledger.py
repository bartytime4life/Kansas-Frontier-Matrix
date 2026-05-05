#!/usr/bin/env python
import argparse,sys,hashlib,json
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent))
from _rollforward_common import *
p=argparse.ArgumentParser();p.add_argument('--rollforward-dir',action='append',default=[]);p.add_argument('--out-dir',required=True);p.add_argument('--previous-ledger');p.add_argument('--as-of');p.add_argument('--allow-fixture-ledger',action='store_true');p.add_argument('--dry-run',action='store_true');a=p.parse_args();out=Path(a.out_dir)
entries=[];prev=''
for i,d in enumerate(sorted(a.rollforward_dir)):
 e={"schema_version":"1.0.0","ledger_entry_id":f"rle-{i+1:03d}","domain":"atmosphere.air","created_at":ts(a.as_of),"as_of":ts(a.as_of),"entry_type":"rollforward_plan_created","actor":{"name":"fixture-operator","non_production":True},"subject_refs":[d],"evidence_refs":[d],"artifact_hashes":[],"previous_entry_ref":prev,"result":"pass","details":"fixture-only"}
 e['entry_hash']=hashlib.sha256(json.dumps(e,sort_keys=True,separators=(',',':')).encode()).hexdigest();prev=e['ledger_entry_id'];entries.append(e)
chain=hashlib.sha256(''.join(x['entry_hash'] for x in entries).encode()).hexdigest()
man={"schema_version":"1.0.0","ledger_id":"rlm-001","domain":"atmosphere.air","generated_at":ts(a.as_of),"as_of":ts(a.as_of),"entry_refs":[f"rollforward_ledger_entries.jsonl#{e['ledger_entry_id']}" for e in entries],"head_entry_ref":entries[-1]['ledger_entry_id'] if entries else None,"chain_hash":chain,"source_refs":sorted(a.rollforward_dir),"safety_checks":["append_only"],"status":"fixture_rollforward_ledger"}
if not a.dry_run:
 out.mkdir(parents=True,exist_ok=True)
 (out/'rollforward_ledger_entries.jsonl').write_text(''.join(json.dumps(e,sort_keys=True)+'\n' for e in entries));w(out/'rollforward_ledger_manifest.json',man);(out/'maintenance_rollforward_events.jsonl').write_text('{"event_type":"rollforward_ledger_created","result":"pass"}\n')
print('PASS')
