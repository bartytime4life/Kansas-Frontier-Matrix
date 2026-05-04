from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]

def main()->int:
    errors=[]
    for p in sorted((ROOT/'connectors/hydrology').glob('*_connector_stub.py')):
        t=p.read_text().lower()
        for bad in ['requests.','urllib','httpx','socket','apikey','api_key']:
            if bad in t: errors.append(f'{p}: forbidden token {bad}')
        if 'connector_enabled = false' not in t: errors.append(f'{p}: missing disabled constant')
    if errors: print('FAIL',errors); return 1
    print('PASS no live hydrology connectors'); return 0
if __name__=='__main__': raise SystemExit(main())
