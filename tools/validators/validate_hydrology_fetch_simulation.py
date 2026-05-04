import json
from pathlib import Path

def main():
    errs=[]
    for p in Path('fixtures/domains/hydrology/fetch_plans').glob('*.json'):
        d=json.loads(p.read_text())
        if 'malformed' in p.name: continue
        if d.get('transport')!='offline_mock': errs.append(f'{p}: non-offline transport')
        if d.get('credentials_required') or d.get('credentials_present'): errs.append(f'{p}: credentials not allowed')
    if errs: print('FAIL',errs); return 1
    print('PASS fetch simulation fixtures guarded'); return 0
if __name__=='__main__': raise SystemExit(main())
