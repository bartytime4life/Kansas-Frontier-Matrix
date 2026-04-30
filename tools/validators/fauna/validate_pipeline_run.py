#!/usr/bin/env python3
from __future__ import annotations
import json,sys,hashlib
from pathlib import Path

def sha256_file(p:Path)->str:
 d=hashlib.sha256();
 with p.open('rb') as f:
  for c in iter(lambda:f.read(65536),b''): d.update(c)
 return f'sha256:{d.hexdigest()}'

def fail(m): print(f'ERROR: {m}',file=sys.stderr); raise SystemExit(2)

if __name__=='__main__':
 if len(sys.argv)!=2: fail('usage: validate_pipeline_run.py <work_dir>')
 w=Path(sys.argv[1]);
 plan=json.loads((w/'pipeline_plan.json').read_text()); man=json.loads((w/'pipeline_manifest.json').read_text()); rep=json.loads((w/'validation_report.json').read_text())
 if plan['suppression_min_n']<10: fail('suppression_min_n <10')
 for k,h in [('pipeline_plan_path','pipeline_plan_sha256'),('validation_report_path','validation_report_sha256'),('evidencebundle_path','evidencebundle_sha256')]:
  if man.get(h)!=sha256_file(Path(man[k])): fail(f'hash mismatch {h}')
 if rep.get('status')!='pass': fail('validation report fail')
 print('OK')
