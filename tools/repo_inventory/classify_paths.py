#!/usr/bin/env python3
from __future__ import annotations
import argparse, subprocess, pathlib

FAMILIES = [
"app_api","app_web","app_worker","package","connector","schema_contract","api_contract","policy","test","fixture","tool_validator","pipeline","migration","data_lifecycle_raw","data_lifecycle_work","data_lifecycle_quarantine","data_lifecycle_processed","data_lifecycle_catalog","data_lifecycle_triplet","data_lifecycle_receipt","data_lifecycle_proof","data_lifecycle_published","data_registry","release","doc_adr","doc_architecture","doc_domain","doc_register","doc_runbook","doc_source","doc_tracking","style","config","infra","root_meta","generated_or_cache","unknown"
]

def classify(path:str)->str:
    p=path
    if p.startswith('apps/governed_api/'): return 'app_api'
    if p.startswith('apps/web/'): return 'app_web'
    if p.startswith('apps/ui/') or p.startswith('apps/review-console/'): return 'app_worker'
    if p.startswith('packages/'): return 'package'
    if p.startswith('connectors/'): return 'connector'
    if p.startswith('contracts/') or p.startswith('schemas/') or p.startswith('jsonschema/'): return 'schema_contract'
    if p.startswith('policy/') or p.startswith('policies/'): return 'policy'
    if p.startswith('tests/'): return 'test'
    if '/fixtures/' in p or p.startswith('fixtures/'): return 'fixture'
    if p.startswith('tools/'): return 'tool_validator'
    if p.startswith('pipelines/') or p.startswith('pipeline_specs/'): return 'pipeline'
    if p.startswith('migrations/'): return 'migration'
    if p.startswith('data/raw/'): return 'data_lifecycle_raw'
    if p.startswith('data/work/'): return 'data_lifecycle_work'
    if p.startswith('data/quarantine/'): return 'data_lifecycle_quarantine'
    if p.startswith('data/processed/'): return 'data_lifecycle_processed'
    if p.startswith('data/catalog/'): return 'data_lifecycle_catalog'
    if p.startswith('data/triplets/'): return 'data_lifecycle_triplet'
    if p.startswith('data/receipts/'): return 'data_lifecycle_receipt'
    if p.startswith('data/proofs/'): return 'data_lifecycle_proof'
    if p.startswith('data/published/'): return 'data_lifecycle_published'
    if p.startswith('data/registry/'): return 'data_registry'
    if p.startswith('release/'): return 'release'
    if p.startswith('docs/adr/'): return 'doc_adr'
    if p.startswith('docs/architecture/'): return 'doc_architecture'
    if p.startswith('docs/domains/'): return 'doc_domain'
    if p.startswith('docs/registers/'): return 'doc_register'
    if p.startswith('docs/runbooks/'): return 'doc_runbook'
    if p.startswith('docs/sources/'): return 'doc_source'
    if p.startswith('docs/tracking/'): return 'doc_tracking'
    if p.startswith('styles/'): return 'style'
    if p.startswith('configs/') or p in ('pyproject.toml','pytest.ini','.gitignore'): return 'config'
    if p.startswith('infra/'): return 'infra'
    if p in ('README.md','Makefile'): return 'root_meta'
    if p.endswith('.pyc') or '__pycache__' in p or p.startswith('apps/web/node_modules/'): return 'generated_or_cache'
    return 'unknown'

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--tsv-out')
    args=ap.parse_args()
    files=subprocess.check_output(['git','ls-files',":!:apps/web/node_modules/**",":!:.git/**"],text=True).splitlines()
    rows=[('path','family')]+[(f,classify(f)) for f in sorted(files)]
    out='\n'.join('\t'.join(r) for r in rows)+'\n'
    if args.tsv_out:
        pathlib.Path(args.tsv_out).write_text(out)
    else:
        print(out,end='')

if __name__=='__main__': main()
