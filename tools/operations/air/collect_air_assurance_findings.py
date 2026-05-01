#!/usr/bin/env python
import argparse,uuid
from pathlib import Path
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent))
from _assurance_common import j,w,ts,bad_text
p=argparse.ArgumentParser();p.add_argument('--assurance-summary',required=True);p.add_argument('--out-dir',required=True);p.add_argument('--archive-recheck');p.add_argument('--runbook-review');p.add_argument('--drift-report');p.add_argument('--recertification-record');p.add_argument('--maintenance-plan');p.add_argument('--deprecation-candidate',action='append',default=[]);p.add_argument('--as-of');p.add_argument('--allow-fixture-findings',action='store_true');p.add_argument('--dry-run',action='store_true');a=p.parse_args()
out=Path(a.out_dir);(out/'assurance_findings').mkdir(parents=True,exist_ok=True)
s=j(a.assurance_summary)
if s.get('result') in ('deny','blocked') or bad_text(s): raise SystemExit('DENY')
f={"schema_version":"1.0.0","finding_id":"finding_fixture_001","domain":"atmosphere.air","created_at":ts(a.as_of),"as_of":ts(a.as_of),"source_ref":a.assurance_summary,"source_type":"continuous_assurance_summary","severity":"info","finding_type":"needs_manual_review","description":"Fixture assurance finding evidence only.","affected_artifacts":[a.assurance_summary],"evidence_refs":[a.assurance_summary],"recommended_action":"Review in governed maintenance flow.","status":"open"}
if not a.dry_run:w(out/'assurance_findings/finding_fixture_001.json',f);(out/'maintenance_events.jsonl').write_text('{"event_type":"assurance_findings_collected"}\n')
print('PASS')
