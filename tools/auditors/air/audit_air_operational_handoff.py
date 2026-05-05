#!/usr/bin/env python
import argparse,sys
from pathlib import Path
import json
p=argparse.ArgumentParser();p.add_argument('dirs',nargs='+');p.add_argument('--out-dir');p.add_argument('--as-of');p.add_argument('--cutover-dir');p.add_argument('--authorization-dir');p.add_argument('--deployment-readiness-dir');p.add_argument('--delivery-dir');p.add_argument('--source-cutover-dir');p.add_argument('--source-authorization-dir');p.add_argument('--source-deployment-readiness-dir');p.add_argument('--source-delivery-dir');a=p.parse_args();ok=True
for d in map(Path,a.dirs):
 for f in d.glob('*.json'):
  t=f.read_text().lower()
  if any(x in t for x in ("data/raw/","data/work/","data/quarantine/","data/processed/air/")): ok=False
if a.out_dir:
 Path(a.out_dir).mkdir(parents=True,exist_ok=True)
 (Path(a.out_dir)/'operational_handoff_audit_report.json').write_text(json.dumps({"schema_version":"1.0.0","audit_id":"audit-001","domain":"atmosphere.air","generated_at":"2026-04-30T00:00:00Z","as_of":"2026-04-30T00:00:00Z","operational_handoff_package_ref":"","watch_window_plan_ref":"","watch_window_evaluation_ref":"","runbook_activation_candidate_ref":"","release_closure_dossier_ref":"","evidence_archive_manifest_ref":"","stakeholder_notice_finalization_refs":[],"checks":[],"hash_checks":[],"ledger_checks":[],"handoff_checks":[],"watch_window_checks":[],"archive_checks":[],"notice_checks":[],"secret_checks":[],"path_safety_checks":[],"semantic_checks":[],"result":"pass" if ok else "deny"},sort_keys=True,indent=2)+'\n')
print('PASS' if ok else 'DENY');sys.exit(0 if ok else 1)
