#!/usr/bin/env python
import argparse
from pathlib import Path
from tools.operations.air._assurance_common import j,w,ts
p=argparse.ArgumentParser();p.add_argument('--deprecation-review',required=True);p.add_argument('--delivery-dir',required=True);p.add_argument('--out-dir',required=True);p.add_argument('--as-of');p.add_argument('--fixture-only',action='store_true');p.add_argument('--dry-run',action='store_true');a=p.parse_args()
d=j(a.deprecation_review)
o={"schema_version":"1.0.0","sunset_plan_id":"sp-001","domain":"atmosphere.air","created_at":ts(a.as_of),"as_of":ts(a.as_of),"deprecation_review_ref":a.deprecation_review,"client_delivery_manifest_ref":d.get('client_delivery_manifest_ref',''),"affected_routes":d.get('affected_routes',[]),"affected_records":d.get('affected_artifacts',[]),"replacement_refs":d.get('replacement_refs',[]),"client_impact_summary":"review-only fixture sunset planning","notice_requirements":["not sent in this PR"],"planned_visibility_changes":[],"forbidden_actions":["no route removal","no notices"],"safety_checks":["no external targets"],"status":"fixture_sunset_plan"}
out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True)
if not a.dry_run:w(out/'client_sunset_plan.json',o);(out/'maintenance_events.jsonl').write_text('{"event_type":"client_sunset_plan_created"}\n')
print('PASS')
