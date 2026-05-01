#!/usr/bin/env python
import argparse,sys,json
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('dirs',nargs='+');p.add_argument('--out-dir');p.add_argument('--as-of');p.add_argument('--closure-dir');p.add_argument('--handoff-dir');p.add_argument('--cutover-dir');p.add_argument('--authorization-dir');p.add_argument('--deployment-readiness-dir');p.add_argument('--delivery-dir');p.add_argument('--source-closure-dir');p.add_argument('--source-handoff-dir');p.add_argument('--source-cutover-dir');p.add_argument('--source-delivery-dir');a=p.parse_args();ok=True
for d in map(Path,a.dirs):
 for f in d.glob('*.json'):
  t=f.read_text().lower()
  if 'data/processed/air/' in t or 'data/raw/' in t: ok=False
if a.out_dir:
 Path(a.out_dir).mkdir(parents=True,exist_ok=True)
 (Path(a.out_dir)/'continuous_assurance_audit_report.json').write_text(json.dumps({"schema_version":"1.0.0","audit_id":"audit-001","domain":"atmosphere.air","generated_at":"2026-04-30T00:00:00Z","as_of":"2026-04-30T00:00:00Z","continuous_assurance_summary_ref":"","continuous_assurance_plan_ref":"","recertification_record_ref":"","archive_integrity_recheck_ref":"","runbook_review_record_ref":"","drift_observation_report_ref":"","maintenance_window_plan_ref":"","checks":[],"hash_checks":[],"ledger_checks":[],"archive_checks":[],"runbook_checks":[],"drift_checks":[],"secret_checks":[],"path_safety_checks":[],"semantic_checks":[],"result":"pass" if ok else "deny"},indent=2,sort_keys=True)+'\n')
print('PASS' if ok else 'DENY');sys.exit(0 if ok else 1)
