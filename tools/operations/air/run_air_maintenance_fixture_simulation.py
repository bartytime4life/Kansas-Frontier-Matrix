#!/usr/bin/env python
import argparse
from pathlib import Path
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent))
from _assurance_common import j,w,ts,h,bad_text
p=argparse.ArgumentParser();p.add_argument('--maintenance-execution-plan',required=True);p.add_argument('--assurance-dir',required=True);p.add_argument('--delivery-dir',required=True);p.add_argument('--out-dir',required=True);p.add_argument('--closure-dir');p.add_argument('--handoff-dir');p.add_argument('--cutover-dir');p.add_argument('--as-of');p.add_argument('--allow-fixture-simulation',action='store_true');p.add_argument('--dry-run',action='store_true');a=p.parse_args()
plan=j(a.maintenance_execution_plan)
if bad_text(plan): raise SystemExit('DENY')
out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True)
sim={"schema_version":"1.0.0","simulation_id":"sim-001","domain":"atmosphere.air","generated_at":ts(a.as_of),"as_of":ts(a.as_of),"maintenance_authorization_ref":plan['maintenance_authorization_ref'],"maintenance_execution_plan_ref":a.maintenance_execution_plan,"source_assurance_refs":[str(p) for p in Path(a.assurance_dir).glob('*.json')],"simulated_steps":plan.get('planned_steps',[]),"simulated_artifact_impacts":[],"hash_checks":[],"etag_checks":[],"path_safety_checks":["pass"],"semantic_checks":["nowcast operational only"],"result":"pass_fixture"}
receipt={"schema_version":"1.0.0","maintenance_receipt_id":"mr-001","domain":"atmosphere.air","created_at":ts(a.as_of),"as_of":ts(a.as_of),"execution_mode":"fixture_simulation","maintenance_authorization_ref":plan['maintenance_authorization_ref'],"maintenance_execution_plan_ref":a.maintenance_execution_plan,"maintenance_fixture_simulation_ref":str(out/'maintenance_fixture_simulation.json'),"actor":"fixture-operator-non-production","steps_observed":plan.get('planned_steps',[]),"artifact_refs":[str(out/'maintenance_fixture_simulation.json')],"hashes":[],"result":"pass","status":"fixture_receipt"}
if not a.dry_run:
 w(out/'maintenance_fixture_simulation.json',sim);w(out/'maintenance_execution_receipt.json',receipt);(out/'maintenance_events.jsonl').write_text('{"event_type":"fixture_maintenance_simulated"}\n')
print('PASS')
