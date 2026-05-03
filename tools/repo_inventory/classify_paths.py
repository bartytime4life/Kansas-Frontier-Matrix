#!/usr/bin/env python3
import argparse, subprocess, re
RULES=[('app_web',r'^apps/(web|ui|review-console)/'),('app_api',r'^apps/governed_api/'),('package',r'^packages/'),('connector',r'^connectors/'),('schema_contract',r'^(schemas|contracts|jsonschema)/'),('policy',r'^(policy|policies)/'),('test',r'^tests/'),('doc_adr',r'^docs/adr/'),('doc_architecture',r'^docs/architecture/'),('doc_domain',r'^docs/domains/'),('doc_register',r'^docs/registers/'),('doc_runbook',r'^docs/runbooks/'),('data_lifecycle_raw',r'^data/raw/'),('data_lifecycle_work',r'^data/work/'),('data_lifecycle_quarantine',r'^data/quarantine/'),('data_lifecycle_processed',r'^data/processed/'),('data_lifecycle_catalog',r'^data/catalog/'),('data_lifecycle_triplet',r'^data/triplets/'),('data_lifecycle_receipt',r'^data/receipts/'),('data_lifecycle_proof',r'^data/proofs/'),('data_lifecycle_published',r'^data/published/'),('data_registry',r'^data/registry/'),('tool_validator',r'^tools/'),('config',r'^(configs/|.*(pytest.ini|pyproject.toml|package.json|\.gitignore)$)'),('infra',r'^infra/'),('root_meta',r'^(README.md|Makefile|conftest.py)$')]
def classify(p):
    for n,pat in RULES:
        if re.search(pat,p): return n
    return 'unknown'
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--out',default='docs/registers/reorg/path_inventory.tsv');a=ap.parse_args()
    paths=subprocess.check_output(['git','ls-files',':!:apps/web/node_modules/**',':!:.git/**'],text=True).splitlines()
    with open(a.out,'w') as f:
        f.write('path\tfamily\n')
        for p in sorted(paths): f.write(f'{p}\t{classify(p)}\n')
    print(f'wrote {len(paths)} paths to {a.out}')
