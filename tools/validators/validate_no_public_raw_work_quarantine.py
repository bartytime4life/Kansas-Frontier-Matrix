from pathlib import Path

def main():
    t=Path('fixtures/ui/evidence_drawer_payload.valid.json').read_text().lower()
    bad=['data/raw/','data/work/','data/quarantine/','raw-1','work-1','qr-1']
    errs=[b for b in bad if b in t]
    if errs: print('FAIL',errs); return 1
    print('PASS no public raw/work/quarantine references'); return 0
if __name__=='__main__': raise SystemExit(main())
