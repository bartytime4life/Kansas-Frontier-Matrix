#!/usr/bin/env python
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent))
from _assurance_common import j,w,ts,h,bad_text
from pathlib import Path
import argparse
p=argparse.ArgumentParser();p.add_argument('--maintenance-authorization',required=True);p.add_argument('--maintenance-plan',required=True);p.add_argument('--out-dir',required=True);p.add_argument('--finding',action='append',default=[]);p.add_argument('--as-of');p.add_argument('--fixture-only',action='store_true');p.add_argument('--dry-run',action='store_true');a=p.parse_args()
auth=j(a.maintenance_authorization)
if auth.get('status') not in ('fixture_authorized','candidate_authorized'): raise SystemExit('DENY')
steps=["Review findings and candidate remediations.","Run local fixture simulation only.","Record additive evidence."]
o={"schema_version":"1.0.0","maintenance_execution_plan_id":"mep-001","domain":"atmosphere.air","created_at":ts(a.as_of),"as_of":ts(a.as_of),"maintenance_authorization_ref":a.maintenance_authorization,"maintenance_window_plan_ref":a.maintenance_plan,"assurance_finding_refs":a.finding,"planned_steps":steps,"preconditions":["authorization present"],"hold_points":["block if unsafe"],"rollback_preconditions":["no source mutation"],"expected_artifacts":["maintenance_fixture_simulation.json"],"forbidden_actions":["no live ops"],"safety_checks":["no network"],"status":"fixture_execution_plan"}
out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True)
if not a.dry_run:w(out/'maintenance_execution_plan.json',o);(out/'maintenance_events.jsonl').write_text('{"event_type":"maintenance_execution_plan_created"}\n')
print('PASS')
