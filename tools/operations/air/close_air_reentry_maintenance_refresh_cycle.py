#!/usr/bin/env python
import argparse, json, sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent))
from _rollforward_common import *
p=argparse.ArgumentParser();p.add_argument('--maintenance-refresh-dir',action='append',default=[]);p.add_argument('--maintenance-refresh-ledger',required=True);p.add_argument('--maintenance-refresh-postcheck',required=True);p.add_argument('--maintenance-refresh-audit',required=True);p.add_argument('--out-dir',required=True);p.add_argument('--signature',default='fixture-signature');p.add_argument('--signature-type',default='fixture_signature');p.add_argument('--closed-by',default='fixture-release-manager');p.add_argument('--role',default='release_manager');p.add_argument('--as-of');p.add_argument('--fixture-only',action='store_true');p.add_argument('--dry-run',action='store_true');a=p.parse_args();
post=j(a.maintenance_refresh_postcheck);aud=j(a.maintenance_refresh_audit);led=j(a.maintenance_refresh_ledger)
if post.get('result') in ('deny','blocked'): deny('maintenance refresh postcheck failed')
if aud.get('result') in ('deny','blocked'): deny('maintenance refresh audit failed')
if led.get('chain_hash_status')=='invalid': deny('invalid maintenance refresh ledger chain')
if a.signature_type=='fixture_signature' and not a.fixture_only: deny('fixture signatures are non-production only')
out={"schema_version":"1.0.0","closure_id":"rmrc-001","domain":"atmosphere.air","created_at":ts(a.as_of),"as_of":ts(a.as_of),"maintenance_refresh_authorization_ref":"maintenance_refresh/authorization.json","maintenance_refresh_execution_plan_ref":"maintenance_refresh/execution_plan.json","maintenance_refresh_execution_receipt_ref":"maintenance_refresh/execution_receipt.json","maintenance_refresh_fixture_simulation_ref":"maintenance_refresh/fixture_simulation.json","maintenance_refresh_postcheck_report_ref":a.maintenance_refresh_postcheck,"maintenance_refresh_audit_report_ref":a.maintenance_refresh_audit,"maintenance_refresh_ledger_manifest_ref":a.maintenance_refresh_ledger,"maintenance_refresh_manifest_ref":"maintenance_refresh/manifest.json","maintenance_refresh_decision_ref":"maintenance_refresh/decision.json","assurance_refresh_remediation_record_refs":["maintenance_refresh/remediation.json"],"deprecation_refresh_review_ref":"maintenance_refresh/deprecation_refresh_review_record.json","client_sunset_refresh_plan_ref":"maintenance_refresh/reentry_client_sunset_refresh_plan.json","closure_decision":"close_fixture_maintenance_refresh","remaining_findings":[],"required_followups":[],"evidence_refs":[a.maintenance_refresh_postcheck,a.maintenance_refresh_audit,a.maintenance_refresh_ledger],"signature":a.signature,"signature_type":a.signature_type,"fixture_backed":True,"status":"fixture_closed"}
if not ensure_safe_text(out): deny('unsafe content')
if not a.dry_run:
 w(Path(a.out_dir)/'reentry_maintenance_refresh_closure_record.json',out);(Path(a.out_dir)/'reentry_maintenance_rollforward_refresh_events.jsonl').write_text('{"event_type":"maintenance_refresh_closure_created","result":"pass"}\n')
print('PASS')
