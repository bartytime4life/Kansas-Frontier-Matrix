#!/usr/bin/env python
import argparse
from pathlib import Path
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent))
from _assurance_common import j,w,ts,bad_text
p=argparse.ArgumentParser();p.add_argument('--deprecation-candidate',required=True);p.add_argument('--assurance-summary',required=True);p.add_argument('--delivery-dir',required=True);p.add_argument('--out-dir',required=True);p.add_argument('--decision',default='approve_fixture_sunset_planning');p.add_argument('--as-of');p.add_argument('--fixture-only',action='store_true');p.add_argument('--dry-run',action='store_true');a=p.parse_args()
c=j(a.deprecation_candidate)
if bad_text(c) or 'delete' in str(c).lower(): raise SystemExit('DENY')
man=list(Path(a.delivery_dir).glob('*manifest*.json'))
o={"schema_version":"1.0.0","deprecation_review_id":"dr-001","domain":"atmosphere.air","created_at":ts(a.as_of),"as_of":ts(a.as_of),"deprecation_candidate_ref":a.deprecation_candidate,"continuous_assurance_summary_ref":a.assurance_summary,"client_delivery_manifest_ref":str(man[0]) if man else "","affected_routes":c.get('affected_routes',[]),"affected_artifacts":c.get('affected_artifacts',[]),"replacement_refs":c.get('replacement_refs',[]),"risk_assessment":["review only"],"review_decision":a.decision,"evidence_refs":[a.deprecation_candidate,a.assurance_summary],"status":"fixture_reviewed"}
out=Path(a.out_dir);out.mkdir(parents=True,exist_ok=True)
if not a.dry_run:w(out/'deprecation_review_record.json',o);(out/'maintenance_events.jsonl').write_text('{"event_type":"deprecation_review_created"}\n')
print('PASS')
