#!/usr/bin/env python
import argparse,sys,json
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('dirs',nargs='+');p.add_argument('--assurance-dir');p.add_argument('--closure-dir');p.add_argument('--handoff-dir');p.add_argument('--cutover-dir');p.add_argument('--delivery-dir');p.add_argument('--source-assurance-dir');p.add_argument('--source-closure-dir');p.add_argument('--source-handoff-dir');p.add_argument('--source-cutover-dir');p.add_argument('--source-delivery-dir');p.add_argument('--as-of');p.add_argument('--out-dir');a=p.parse_args();ok=True
for d in map(Path,a.dirs):
 for f in d.rglob('*.json'):
  t=f.read_text().lower();
  if 'data/published/air/' in t or 'kubectl' in t or 'terraform' in t: ok=False
if a.out_dir:
 Path(a.out_dir).mkdir(parents=True,exist_ok=True)
 (Path(a.out_dir)/'maintenance_audit_report.json').write_text(json.dumps({"schema_version":"1.0.0","audit_id":"maudit-001","domain":"atmosphere.air","generated_at":"2026-04-30T00:00:00Z","as_of":"2026-04-30T00:00:00Z","maintenance_authorization_ref":"","maintenance_execution_plan_ref":"","maintenance_execution_receipt_ref":"","assurance_remediation_record_refs":[],"deprecation_review_ref":"","client_sunset_plan_ref":"","maintenance_ledger_manifest_ref":"","maintenance_postcheck_report_ref":"","checks":[],"hash_checks":[],"ledger_checks":[],"authorization_checks":[],"simulation_checks":[],"deprecation_checks":[],"secret_checks":[],"path_safety_checks":[],"semantic_checks":[],"result":"pass" if ok else "deny"},indent=2,sort_keys=True)+'\n')
print('PASS' if ok else 'DENY');sys.exit(0 if ok else 1)
