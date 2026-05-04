import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]

def main():
    errors=[]
    for p in (ROOT/'fixtures/domains/hydrology/source_documentation_checks').glob('*.json'):
        d=json.loads(p.read_text())
        for k in ['source_documentation_check_id','source_id','checked','no_data_fetched','finite_state']:
            if k not in d: errors.append(f'{p}: missing {k}')
        if d.get('no_data_fetched') is not True: errors.append(f'{p}: must no_data_fetched true')
    for p in (ROOT/'fixtures/domains/hydrology/source_verification_receipts').glob('*.json'):
        d=json.loads(p.read_text())
        if d.get('result')=='APPROVED': errors.append(f'{p}: approved not allowed')
    if errors: print('FAIL',errors); return 1
    print('PASS hydrology source documentation fixtures'); return 0
if __name__=='__main__': raise SystemExit(main())
