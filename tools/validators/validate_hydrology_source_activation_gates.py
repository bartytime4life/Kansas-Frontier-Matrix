import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]

def main()->int:
    errors=[]
    for p in sorted((ROOT/'fixtures/domains/hydrology').glob('source_activation_gate.*.json')):
        d=json.loads(p.read_text())
        if d.get('finite_result') not in {'BLOCKED','READY_FOR_MANUAL_REVIEW'}: errors.append(f'{p}: invalid finite_result')
        if d.get('connector_enabled') is not False: errors.append(f'{p}: connector enabled')
        if d.get('data_fetch_allowed') is not False: errors.append(f'{p}: data fetch enabled')
    if errors: print('FAIL',errors); return 1
    print('PASS source activation gates blocked'); return 0
if __name__=='__main__': raise SystemExit(main())
