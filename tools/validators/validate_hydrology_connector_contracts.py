import json
from pathlib import Path

def main():
    errs=[]
    for p in Path('fixtures/domains/hydrology/connector_contracts').glob('*.json'):
        d=json.loads(p.read_text())
        if d.get('connector_enabled') is not False: errs.append(f'{p}: connector enabled')
        if d.get('data_fetch_allowed') is not False: errs.append(f'{p}: data fetch allowed')
        if d.get('public_release_allowed') is not False: errs.append(f'{p}: public release allowed')
        if d.get('allowed_transports')!=['offline_mock']: errs.append(f'{p}: allowed transport must offline_mock')
    if errs: print('FAIL',errs); return 1
    print('PASS connector contracts guarded'); return 0
if __name__=='__main__': raise SystemExit(main())
