#!/usr/bin/env python
import argparse,sys
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('dirs',nargs='+');p.add_argument('--maintenance-dir');p.add_argument('--assurance-dir');p.add_argument('--closure-dir');p.add_argument('--delivery-dir');p.add_argument('--as-of');a=p.parse_args();ok=True
need=['maintenance_closure_record.json','remediation_rollforward_plan.json','candidate_artifact_refresh_manifest.json','candidate_read_model_refresh.json','client_delivery_refresh_manifest.json','sunset_delta_candidate.json','client_sunset_notice_candidate.json','assurance_baseline_rotation.json','rollforward_ledger_manifest.json','rollforward_postcheck_report.json']
alltxt=''
for d in map(Path,a.dirs):
 for f in d.rglob('*.json'): alltxt += f.read_text().lower()
for x in ('data/raw/','data/work/','data/quarantine/','data/processed/air/','secret','token','bearer ','https://'):
 if x in alltxt: ok=False
present={f.name for d in map(Path,a.dirs) for f in d.rglob('*.json')}
if not any('maintenance_closure_record.json'==x for x in present): ok=False
print('PASS' if ok else 'DENY');sys.exit(0 if ok else 1)
