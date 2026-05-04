import json
from pathlib import Path

def main():
    errs=[]
    for p in Path('fixtures/domains/hydrology/ingest_plans').glob('*.json'):
        d=json.loads(p.read_text())
        if 'malformed' in p.name: continue
        if d.get('synthetic') is not True or d.get('no_network') is not True: errs.append(f'{p}: must be synthetic/no_network')
        if d.get('public_release_allowed') is not False: errs.append(f'{p}: public release must be false')
    prom=json.loads(Path('fixtures/domains/hydrology/promotion_dry_runs/hydrology_synthetic_ingest_drill.denied.json').read_text())
    if prom.get('finite_result') not in {'DENY','ABSTAIN'}: errs.append('promotion must deny/abstain')
    if errs: print('FAIL',errs); return 1
    print('PASS synthetic ingest drill guarded'); return 0
if __name__=='__main__': raise SystemExit(main())
