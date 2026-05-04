import json
from pathlib import Path
P=Path('fixtures/domains/hydrology/manual_review/hydrology_source_review_packet.pr004.json')

def main():
    d=json.loads(P.read_text())
    errs=[]
    if d.get('approval_for_data_fetch') is not False: errs.append('approval_for_data_fetch must be false')
    if d.get('approval_for_connector_enablement') is not False: errs.append('approval_for_connector_enablement must be false')
    if d.get('approval_for_public_release') is not False: errs.append('approval_for_public_release must be false')
    if d.get('finite_state') not in {'READY_FOR_MANUAL_REVIEW','BLOCKED','NEEDS_VERIFICATION'}: errs.append('invalid finite_state')
    if errs: print('FAIL',errs); return 1
    print('PASS manual review packet guarded'); return 0
if __name__=='__main__': raise SystemExit(main())
