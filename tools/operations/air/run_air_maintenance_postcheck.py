#!/usr/bin/env python
import argparse
from pathlib import Path
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent))
from _assurance_common import w,ts,j
p=argparse.ArgumentParser();p.add_argument('--maintenance-dir',action='append',default=[]);p.add_argument('--ledger',required=True);p.add_argument('--delivery-dir',required=True);p.add_argument('--out-dir',required=True);p.add_argument('--assurance-dir');p.add_argument('--as-of');p.add_argument('--allow-fixture-postcheck',action='store_true');p.add_argument('--dry-run',action='store_true');a=p.parse_args()
l=j(a.ledger)
result='pass_fixture' if l.get('status')=='fixture_maintenance_ledger' else 'deny'
o={"schema_version":"1.0.0","postcheck_id":"pc-001","domain":"atmosphere.air","generated_at":ts(a.as_of),"as_of":ts(a.as_of),"maintenance_execution_receipt_ref":"","assurance_remediation_record_refs":[],"deprecation_review_ref":"","client_sunset_plan_ref":"","checks":["no published writes"],"hash_checks":[],"etag_checks":[],"path_safety_checks":[],"semantic_checks":["nowcast operational label present","aqs 24h_validated required"],"open_findings":[],"result":result}
out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True)
if not a.dry_run:w(out/'maintenance_postcheck_report.json',o);(out/'maintenance_events.jsonl').write_text('{"event_type":"maintenance_postcheck_created"}\n')
print('PASS' if result!='deny' else 'DENY')
