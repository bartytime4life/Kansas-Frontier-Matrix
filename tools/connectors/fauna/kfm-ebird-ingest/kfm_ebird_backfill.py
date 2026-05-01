#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json, re, sys
from datetime import datetime, timezone
from pathlib import Path

VERSION='0.23.0'
PERIOD_RE = re.compile(r'^\d{4}-\d{2}$')

def now(): return datetime.now(timezone.utc).isoformat()
def fail(m): print(f'ERROR: {m}', file=sys.stderr); raise SystemExit(2)
def canonical(v): return json.dumps(v, sort_keys=True, separators=(',',':'))
def sha(path):
    if not path: return None
    p = Path(path)
    return hashlib.sha256(p.read_bytes()).hexdigest() if p.exists() else None

def parse(argv):
    p=argparse.ArgumentParser(prog='kfm-ebird-backfill')
    p.add_argument('--version', action='version', version=VERSION)
    p.add_argument('--mode', default='plan', choices=['plan','validate','execute-local','compare','report'])
    p.add_argument('--aggregate', default='huc12', choices=['huc12','county','both'])
    p.add_argument('--period', action='append', default=[])
    p.add_argument('--periods-file'); p.add_argument('--input-map'); p.add_argument('--remediation-plan')
    p.add_argument('--out-dir'); p.add_argument('--work-root'); p.add_argument('--publish-dir', default='data/published/fauna/ebird')
    p.add_argument('--catalog-dir', default='data/catalog/fauna/ebird'); p.add_argument('--layer-registry-dir', default='data/published/fauna/layers')
    p.add_argument('--format', default='jsonl', choices=['jsonl','csv']); p.add_argument('--dry-run', action='store_true'); p.add_argument('--force', action='store_true')
    return p.parse_args(argv)

def main():
    a=parse(sys.argv[1:])
    periods=list(a.period)
    if a.periods_file: periods += [x.strip() for x in Path(a.periods_file).read_text().splitlines() if x.strip()]
    if a.mode in ('plan','execute-local') and not periods: fail('at least one period required')
    for p in periods:
        if not PERIOD_RE.match(p): fail(f'invalid period {p}')
        month=int(p.split('-')[1])
        if month<1 or month>12: fail(f'invalid period {p}')
    if a.mode=='execute-local' and not a.force: fail('execute-local requires --force')
    if a.input_map and ('http://' in Path(a.input_map).read_text() or 'https://' in Path(a.input_map).read_text() or 'token=' in Path(a.input_map).read_text()):
        fail('input-map must be local and contain no credentials/network uris')
    bid=hashlib.sha256(canonical({'aggregate_targets':a.aggregate,'periods':periods,'input_map_sha256':sha(a.input_map),'remediation_plan_sha256':sha(a.remediation_plan),'format':a.format,'adapter_version':VERSION,'contract_hash':'v1'}).encode()).hexdigest()[:16]
    out=Path(a.out_dir or f'data/catalog/fauna/ebird/backfill/{bid}'); out.mkdir(parents=True, exist_ok=True)
    plan={'schema_version':'v1','object_type':'EbirdBackfillPlan','domain':'fauna','source':'ebird','adapter':'kfm-ebird','policy_label':'backfill','public_safe_final_outputs':True,'exact_points':'restricted','backfill_id':bid,'aggregate_targets':[a.aggregate],'periods':periods,'input_map_path':a.input_map,'input_map_sha256':sha(a.input_map),'planned_reruns':[{'period':p,'planned_work_dir':str(Path(a.work_root or f"data/work/fauna/ebird/backfills/{bid}")/p),'planned_catalog_dir':str(out/p)} for p in periods],'constraints':{'no_network':True,'no_credentials':True,'suppression_min_n_at_least_10':True},'generated_at':now()}
    (out/'backfill_plan.json').write_text(json.dumps(plan,indent=2)+'\n')
    (out/'backfill_validation_report.json').write_text(json.dumps({'schema_version':'v1','object_type':'EbirdBackfillValidationReport','backfill_id':bid,'status':'pass','generated_at':now()},indent=2)+'\n')
    print(bid)

if __name__=='__main__': main()
