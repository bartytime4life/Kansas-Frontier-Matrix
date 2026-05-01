#!/usr/bin/env python
import argparse,sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent))
from _rollforward_common import *
p=argparse.ArgumentParser();p.add_argument('--client-sunset-plan',required=True);p.add_argument('--deprecation-review',required=True);p.add_argument('--delivery-dir',required=True);p.add_argument('--out-dir',required=True);p.add_argument('--as-of');p.add_argument('--fixture-only',action='store_true');p.add_argument('--dry-run',action='store_true');a=p.parse_args();out=Path(a.out_dir)
d={"schema_version":"1.0.0","sunset_delta_id":"sdc-001","domain":"atmosphere.air","created_at":ts(a.as_of),"as_of":ts(a.as_of),"client_sunset_plan_ref":a.client_sunset_plan,"deprecation_review_ref":a.deprecation_review,"source_client_delivery_manifest_ref":"delivery/client_delivery_manifest.json","affected_routes":[],"affected_records":[],"replacement_refs":[],"planned_visibility_changes":[],"client_delta_refs":[],"notice_candidate_refs":[str(out/'client_sunset_notice_candidate.json')],"forbidden_actions":["no_route_removal","no_artifact_deletion","no_notice_send"],"safety_checks":["candidate_only"],"status":"fixture_sunset_delta"}
n={"schema_version":"1.0.0","notice_candidate_id":"csn-001","domain":"atmosphere.air","created_at":ts(a.as_of),"as_of":ts(a.as_of),"sunset_delta_candidate_ref":str(out/'sunset_delta_candidate.json'),"client_sunset_plan_ref":a.client_sunset_plan,"notice_type":"fixture_sunset_planning","message_summary":"Candidate-only sunset planning notice; do not send.","public_safe_links":[],"redactions":[],"forbidden_actions":["no_external_targets","no_sending"],"approval_state":"draft_only","status":"fixture_notice_candidate"}
if not a.dry_run:
 w(out/'sunset_delta_candidate.json',d);w(out/'client_sunset_notice_candidate.json',n);(out/'maintenance_rollforward_events.jsonl').write_text('{"event_type":"sunset_delta_created","result":"pass"}\n')
print('PASS')
