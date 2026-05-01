#!/usr/bin/env python
import argparse
from pathlib import Path
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent))
from _assurance_common import j,w,ts
p=argparse.ArgumentParser();p.add_argument('--maintenance-execution-receipt',required=True);p.add_argument('--out-dir',required=True);p.add_argument('--finding',action='append',default=[]);p.add_argument('--remediation-type',default='no_op');p.add_argument('--as-of');p.add_argument('--fixture-only',action='store_true');p.add_argument('--dry-run',action='store_true');a=p.parse_args()
r=j(a.maintenance_execution_receipt)
if r.get('result') in ('deny','blocked'): raise SystemExit('DENY')
out=Path(a.out_dir);d=out/'assurance_remediation_records';d.mkdir(parents=True,exist_ok=True)
o={"schema_version":"1.0.0","remediation_record_id":"arr-001","domain":"atmosphere.air","created_at":ts(a.as_of),"as_of":ts(a.as_of),"assurance_finding_refs":a.finding,"maintenance_authorization_ref":r['maintenance_authorization_ref'],"maintenance_execution_receipt_ref":a.maintenance_execution_receipt,"remediation_type":a.remediation_type,"before_refs":a.finding,"after_refs":a.finding,"evidence_refs":[a.maintenance_execution_receipt],"remaining_risks":[],"status":"fixture_remediation_recorded"}
if not a.dry_run:w(d/'remediation_fixture_001.json',o);(out/'maintenance_events.jsonl').write_text('{"event_type":"assurance_remediation_recorded"}\n')
print('PASS')
