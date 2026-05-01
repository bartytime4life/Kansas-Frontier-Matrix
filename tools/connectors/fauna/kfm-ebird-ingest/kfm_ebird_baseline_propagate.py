#!/usr/bin/env python3
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path
VERSION='0.36.0'
def canonical(o): return json.dumps(o,sort_keys=True,separators=(',',':'))
def parse(argv=None):
 p=argparse.ArgumentParser(prog='kfm-ebird-baseline-propagate')
 p.add_argument('--mode',default='plan',choices=['plan','apply-local','validate','diff','report'])
 p.add_argument('--aggregate',default='both',choices=['huc12','county','both'])
 p.add_argument('--out-dir'); p.add_argument('--public-out-dir'); p.add_argument('--apply',action='store_true'); p.add_argument('--force',action='store_true'); p.add_argument('--version',action='store_true')
 return p.parse_args(argv)
def main(argv=None):
 a=parse(argv)
 if a.version:
  print(json.dumps({'adapter':'kfm-ebird','tool':'baseline-propagate','version':VERSION})); return 0
 if a.mode=='apply-local' and (not a.apply or not a.force): raise SystemExit('apply-local requires --apply and --force')
 bid=hashlib.sha256(canonical({'aggregate_targets':a.aggregate,'adapter_version':VERSION}).encode()).hexdigest()[:16]
 out=Path(a.out_dir or f'data/catalog/fauna/ebird/baseline-propagation/{bid}'); pub=Path(a.public_out_dir or f'data/published/fauna/ebird/baseline-propagation/{bid}')
 if out.exists() and any(out.iterdir()) and not a.force: raise SystemExit('refusing overwrite without --force')
 out.mkdir(parents=True,exist_ok=True); pub.mkdir(parents=True,exist_ok=True)
 (out/'baseline_propagation_plan.json').write_text(json.dumps({'schema_version':'v1','object_type':'KfmEbirdBaselinePropagationPlan','baseline_propagation_id':bid},indent=2)+'\n')
 print(json.dumps({'baseline_propagation_id':bid,'out_dir':str(out),'public_out_dir':str(pub)})); return 0
if __name__=='__main__': raise SystemExit(main())
