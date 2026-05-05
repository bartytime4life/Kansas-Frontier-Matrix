#!/usr/bin/env python
import argparse,sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent))
from _rollforward_common import *
p=argparse.ArgumentParser();p.add_argument('--maintenance-closure',required=True);p.add_argument('--maintenance-dir',action='append',default=[]);p.add_argument('--delivery-dir',required=True);p.add_argument('--out-dir',required=True);p.add_argument('--assurance-dir');p.add_argument('--as-of');p.add_argument('--allow-fixture-rollforward',action='store_true');p.add_argument('--dry-run',action='store_true');a=p.parse_args();c=j(a.maintenance_closure)
if not c.get('signature'): deny('unsigned maintenance closure')
if c.get('signature_type')=='fixture_signature' and not a.allow_fixture_rollforward: deny('fixture rollforward not allowed')
plan={"schema_version":"1.0.0","rollforward_plan_id":"rfp-001","domain":"atmosphere.air","created_at":ts(a.as_of),"as_of":ts(a.as_of),"maintenance_closure_record_ref":a.maintenance_closure,"maintenance_ledger_manifest_ref":c['maintenance_ledger_manifest_ref'],"assurance_remediation_record_refs":c['assurance_remediation_record_refs'],"deprecation_review_ref":c['deprecation_review_ref'],"client_sunset_plan_ref":c['client_sunset_plan_ref'],"source_candidate_refs":[a.delivery_dir],"planned_changes":[{"change_id":"chg-001","change_type":"metadata_correction_candidate","subject_ref":"candidate/public_status.json","before_ref":"delivery/public_status.json","after_candidate_ref":"candidate/public_status.refresh.json","reason":"rollforward candidate metadata refresh","evidence_refs":[a.maintenance_closure],"destructive":False}],"non_mutation_guarantees":["no_source_mutation","no_published_writes"],"safety_checks":["nowcast_operational_not_validated_truth"],"status":"fixture_rollforward_plan"}
if any(ch.get('destructive') for ch in plan['planned_changes']): deny('destructive change')
if not ensure_safe_text(plan): deny('unsafe content')
out=Path(a.out_dir)
if not a.dry_run:
 w(out/'remediation_rollforward_plan.json',plan)
 (out/'maintenance_rollforward_events.jsonl').write_text('{\"event_type\":\"rollforward_plan_created\",\"result\":\"pass\"}\n')
print('PASS')
