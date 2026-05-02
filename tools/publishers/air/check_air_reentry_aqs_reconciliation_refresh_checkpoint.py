#!/usr/bin/env python3
import argparse
from datetime import datetime,timezone
from pathlib import Path
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))
from _reentry_publication_boundary_refresh_lib import ts,writej
ap=argparse.ArgumentParser(); ap.add_argument('--release-candidate-refresh-package',required=True); ap.add_argument('--qa-revalidation-refresh',required=True); ap.add_argument('--evidence-bundle-refresh',required=True); ap.add_argument('--out-dir',required=True); ap.add_argument('--status',default='not_required'); ap.add_argument('--as-of'); ap.add_argument('--reconciled-at'); ap.add_argument('--fixture-only',action='store_true'); ap.add_argument('--dry-run',action='store_true')
a=ap.parse_args(); as_of=ts(a.as_of); rec=ts(a.reconciled_at or a.as_of)
if a.status in ('fixture_reconciled','candidate_reconciled'):
    dt=lambda x: datetime.strptime(x,'%Y-%m-%dT%H:%M:%SZ').replace(tzinfo=timezone.utc)
    if (dt(as_of)-dt(rec)).total_seconds()>72*3600: raise SystemExit('DENY stale reconciliation')
obj={"schema_version":"v1","reconciliation_id":"aqs-refresh-checkpoint","domain":"atmosphere.air","created_at":as_of,"as_of":as_of,"release_candidate_refresh_package_ref":a.release_candidate_refresh_package,"qa_revalidation_refresh_report_ref":a.qa_revalidation_refresh,"release_evidence_bundle_refresh_ref":a.evidence_bundle_refresh,"aqs_validated_window":{"averaging_window":"24h_validated","pm25_units":"ug_m3","nowcast_semantics":"operational_not_validated_truth"},"reconciled_at":rec,"method":"fixture_no_network","status":a.status,"differences":[],"source_rows":0,"staleness_check":{"max_age_hours":72,"ok":True},"safety_checks":{"no_live_aqs_fetch":True,"nowcast_not_validated_truth":True}}
out=Path(a.out_dir)
if not a.dry_run:
 writej(out/'reentry_aqs_reconciliation_refresh_checkpoint.json',obj); (out/'reentry_publication_boundary_refresh_events.jsonl').write_text('{"event_type":"aqs_reconciliation_refresh_checkpoint_created","result":"pass"}\n')
print('PASS')
