#!/usr/bin/env python3
import argparse, hashlib, json, sys
from pathlib import Path
from datetime import datetime, timezone
now=lambda: datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
BAD=['data/raw/','data/work/','data/quarantine/','data/processed/air/','data/published/air/','data/published/air/read_model/','secret','token','bearer ','http://','https://','kubectl','terraform']

def main():
 p=argparse.ArgumentParser();p.add_argument('--read-model-refresh-dir',action='append',default=[]);p.add_argument('--read-model-refresh-ledger',required=True);p.add_argument('--out-dir',required=True);p.add_argument('--materialization-dir');p.add_argument('--source-read-model-dir');p.add_argument('--as-of');p.add_argument('--allow-fixture-postcheck',action='store_true');p.add_argument('--dry-run',action='store_true');a=p.parse_args()
 asof=a.as_of or now(); out=Path(a.out_dir); out.mkdir(parents=True,exist_ok=True)
 findings=[]
 ledger=json.loads(Path(a.read_model_refresh_ledger).read_text())
 if not ledger.get('chain_hash'): findings.append('invalid ledger chain hash')
 all_json=[]
 for d in a.read_model_refresh_dir:
  all_json += list(Path(d).rglob('*.json'))
 hashes={str(f):hashlib.sha256(f.read_bytes()).hexdigest() for f in all_json}
 for f in all_json:
  t=f.read_text(errors='ignore').lower()
  for b in BAD:
   if b in t: findings.append(f'unsafe marker {b} in {f}')
  if 'nowcast_is_validated_aqs_truth": true' in t: findings.append('nowcast treated as aqs truth')
 result='pass_fixture' if not findings else 'deny'
 rep={'schema_version':'v1','postcheck_id':'rmr-post-1','domain':'atmosphere.air','generated_at':asof,'as_of':asof,'refresh_plan_ref':'local','read_model_refresh_manifest_ref':'local','read_model_refresh_decision_ref':'local','checks':[],'hash_checks':[{'path':k,'sha256':v} for k,v in sorted(hashes.items())],'delta_checks':[],'invalidation_checks':[],'version_checks':[],'lineage_checks':[],'path_safety_checks':[],'semantic_checks':[],'non_mutation_checks':[],'open_findings':findings,'result':result}
 if not a.dry_run:
  (out/'reentry_read_model_refresh_postcheck_report.json').write_text(json.dumps(rep,indent=2,sort_keys=True)+'\n')
  (out/'reentry_read_model_refresh_events.jsonl').write_text(json.dumps({'event_type':'read_model_refresh_postcheck_created','result':'pass' if result.startswith('pass') else 'deny','as_of':asof},sort_keys=True)+'\n')
 print('PASS' if result.startswith('pass') else 'DENY')
 sys.exit(0 if result.startswith('pass') else 1)
if __name__=='__main__': main()
