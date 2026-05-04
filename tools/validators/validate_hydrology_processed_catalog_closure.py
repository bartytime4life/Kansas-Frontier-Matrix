import json
from pathlib import Path

def _j(p): return json.loads(Path(p).read_text())
def main():
  e=[]
  p=_j('fixtures/domains/hydrology/processed/usgs_water_data.synthetic_streamflow.processed_observation.json')
  if p.get('lifecycle_stage')!='PROCESSED': e.append('processed lifecycle')
  if p.get('public_release_allowed') is not False: e.append('processed public flag')
  c=_j('fixtures/domains/hydrology/catalog/hydrology_synthetic_streamflow.catalog_closure_report.json')
  if c.get('finite_result')!='CATALOG_CLOSURE_PASSED_INTERNAL_ONLY': e.append('closure result')
  if e: print('FAIL',e); return 1
  print('PASS processed/catalog closure'); return 0
if __name__=='__main__': raise SystemExit(main())
