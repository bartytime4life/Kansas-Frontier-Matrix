import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
DESC_DIR=ROOT/'data/registry/sources/hydrology'
REQ=['source_id','source_role','rights_status','public_release_allowed','connector_enabled','data_fetch_allowed','activation_status','documentation_check_receipt_id']
ALLOWED={'blocked_needs_verification','blocked_rights_unknown','blocked_policy','descriptor_only','ready_for_manual_review'}

def main()->int:
    errors=[]
    for p in sorted(DESC_DIR.glob('*.json')):
        d=json.loads(p.read_text())
        for k in REQ:
            if k not in d: errors.append(f'{p}: missing {k}')
        if d.get('activation_status') not in ALLOWED: errors.append(f'{p}: activation not blocked state')
        if d.get('connector_enabled') is not False: errors.append(f'{p}: connector_enabled must be false')
        if d.get('data_fetch_allowed') is not False: errors.append(f'{p}: data_fetch_allowed must be false')
        if d.get('public_release_allowed') is not False: errors.append(f'{p}: public_release_allowed must be false')
    if errors:
        print('FAIL',errors); return 1
    print('PASS hydrology source descriptors blocked')
    return 0
if __name__=='__main__': raise SystemExit(main())
