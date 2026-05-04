import json
from pathlib import Path

def main():
    d=json.loads(Path('fixtures/domains/hydrology/lifecycle/hydrology_synthetic_ingest_transition_matrix.pr006.json').read_text())
    denied=' '.join(d.get('denied',[]))
    errs=[]
    for req in ['RAW->PUBLISHED','WORK->PUBLISHED','QUARANTINE->PUBLISHED']:
        if req not in denied: errs.append(f'missing denied transition {req}')
    if errs: print('FAIL',errs); return 1
    print('PASS lifecycle transition boundaries'); return 0
if __name__=='__main__': raise SystemExit(main())
