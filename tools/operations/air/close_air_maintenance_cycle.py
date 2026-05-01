#!/usr/bin/env python
import argparse,sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent))
from _rollforward_common import *
p=argparse.ArgumentParser();p.add_argument('--maintenance-dir',action='append',default=[]);p.add_argument('--maintenance-ledger',required=True);p.add_argument('--maintenance-postcheck',required=True);p.add_argument('--maintenance-audit',required=True);p.add_argument('--out-dir',required=True);p.add_argument('--signature',default='fixture-signature');p.add_argument('--signature-type',default='fixture_signature');p.add_argument('--closed-by',default='fixture-release-manager');p.add_argument('--role',default='release_manager');p.add_argument('--as-of');p.add_argument('--fixture-only',action='store_true');p.add_argument('--dry-run',action='store_true');a=p.parse_args()
post=j(a.maintenance_postcheck);aud=j(a.maintenance_audit);led=j(a.maintenance_ledger)
if post.get('result') in ('deny','blocked'): deny('maintenance postcheck failed')
if aud.get('result') in ('deny','blocked'): deny('maintenance audit failed')
if led.get('chain_hash_status')=='invalid': deny('invalid maintenance ledger chain')
if a.signature_type=='fixture_signature' and not a.fixture_only: deny('fixture signatures are non-production only')
out=Path(a.out_dir)
o={"schema_version":"1.0.0","closure_id":"mcr-001","domain":"atmosphere.air","created_at":ts(a.as_of),"as_of":ts(a.as_of),"maintenance_authorization_ref":"maintenance/maintenance_authorization.json","maintenance_execution_plan_ref":"maintenance/maintenance_execution_plan.json","maintenance_execution_receipt_ref":"maintenance/maintenance_execution_receipt.json","maintenance_fixture_simulation_ref":"maintenance/maintenance_fixture_simulation.json","maintenance_postcheck_report_ref":a.maintenance_postcheck,"maintenance_audit_report_ref":a.maintenance_audit,"maintenance_ledger_manifest_ref":a.maintenance_ledger,"assurance_remediation_record_refs":["maintenance/remediation_001.json"],"deprecation_review_ref":"maintenance/deprecation_review_record.json","client_sunset_plan_ref":"maintenance/client_sunset_plan.json","closure_decision":"close_fixture_maintenance","remaining_findings":[],"required_followups":[],"evidence_refs":[a.maintenance_postcheck,a.maintenance_audit,a.maintenance_ledger],"signature":a.signature,"signature_type":a.signature_type,"fixture_backed":True,"status":"fixture_closed","actor":{"name":a.closed_by,"role":a.role,"non_production":True}}
if not ensure_safe_text(o): deny('unsafe content')
if not a.dry_run:
 w(out/'maintenance_closure_record.json',o)
 (out/'maintenance_rollforward_events.jsonl').write_text('{\"event_type\":\"maintenance_closure_created\",\"result\":\"pass\"}\n')
print('PASS')
