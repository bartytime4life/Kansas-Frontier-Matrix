#!/usr/bin/env python
import argparse
from _assurance_common import *
p=argparse.ArgumentParser();[p.add_argument(x,required=True) for x in ('--assurance-plan','--recertification-record','--archive-recheck','--runbook-review','--drift-report','--maintenance-plan','--out-dir')];p.add_argument('--deprecation-candidate',action='append',default=[]);p.add_argument('--as-of');p.add_argument('--allow-fixture-summary',action='store_true');a=p.parse_args();ar,dr=j(a.archive_recheck),j(a.drift_report)
blocked=ar.get('result')=='deny' or dr.get('result')=='deny'
out={"schema_version":"1.0.0","summary_id":"sum-"+h(a.assurance_plan)[:12],"domain":"atmosphere.air","generated_at":ts(a.as_of),"as_of":ts(a.as_of),"continuous_assurance_plan_ref":a.assurance_plan,"recertification_record_ref":a.recertification_record,"archive_integrity_recheck_ref":a.archive_recheck,"runbook_review_record_ref":a.runbook_review,"drift_observation_report_ref":a.drift_report,"maintenance_window_plan_ref":a.maintenance_plan,"deprecation_candidate_refs":a.deprecation_candidate,"open_findings":[],"blocked_items":[],"recommended_next_actions":[],"safety_checks":[],"status":"blocked" if blocked else "fixture_assurance_passed"}
w(Path(a.out_dir)/'continuous_assurance_summary.json',out);print('PASS' if not blocked else 'DENY')
