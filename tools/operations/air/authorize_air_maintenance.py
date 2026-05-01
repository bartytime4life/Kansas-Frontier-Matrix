#!/usr/bin/env python
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent))
from _assurance_common import j,w,ts,h,bad_text
from pathlib import Path
import argparse
p=argparse.ArgumentParser();p.add_argument('--assurance-summary',required=True);p.add_argument('--maintenance-plan',required=True);p.add_argument('--recertification-record',required=True);p.add_argument('--out-dir',required=True);p.add_argument('--finding',action='append',default=[]);p.add_argument('--decision',default='authorize_fixture_maintenance_simulation');p.add_argument('--approved-by',default='fixture-release-manager');p.add_argument('--role',default='release_manager');p.add_argument('--signature',default='fixture-signature');p.add_argument('--signature-type',default='fixture_signature');p.add_argument('--as-of');p.add_argument('--fixture-only',action='store_true');p.add_argument('--dry-run',action='store_true');a=p.parse_args();s=j(a.assurance_summary)
if s.get('result') in ('deny','blocked'): raise SystemExit('DENY')
if a.signature_type=='fixture_signature' and 'production' in a.decision: raise SystemExit('DENY')
o={"schema_version":"1.0.0","maintenance_authorization_id":"ma-001","domain":"atmosphere.air","created_at":ts(a.as_of),"as_of":ts(a.as_of),"continuous_assurance_summary_ref":a.assurance_summary,"maintenance_window_plan_ref":a.maintenance_plan,"periodic_recertification_record_ref":a.recertification_record,"assurance_finding_refs":a.finding,"authorized_scope":"fixture-only","authorization_decision":a.decision,"approver":a.approved_by,"role":a.role,"required_conditions":["non-production"],"safety_checks":["production blocked"],"signature":a.signature,"signature_type":a.signature_type,"fixture_backed":True,"status":"fixture_authorized" if 'authorize' in a.decision else "blocked"}
out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True)
if not a.dry_run:w(out/'maintenance_authorization.json',o);(out/'maintenance_events.jsonl').write_text('{"event_type":"maintenance_authorization_created"}\n')
print('PASS')
