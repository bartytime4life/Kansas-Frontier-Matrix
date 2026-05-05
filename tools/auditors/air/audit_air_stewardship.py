#!/usr/bin/env python3
import json,sys
from pathlib import Path
errs=[]
for d in sys.argv[1:]:
 p=Path(d); rem=json.loads((p/'retraction_execution_manifest.json').read_text()) if (p/'retraction_execution_manifest.json').exists() else {}
 if rem.get('status')=='executed_fixture_only':
  for f in ['tombstone.json','read_model_invalidation_notice.json']: 
   if not (p/f).exists(): errs.append(f'missing {f}')
 if 'data/published/air/' in json.dumps(rem): errs.append('writes_to_published_air')
 if any(x in json.dumps(rem).lower() for x in ['data/raw','data/work','data/quarantine','data/processed/air']): errs.append('unsafe_path')
print('DENY' if errs else 'PASS')
if errs: print('\n'.join(errs)); raise SystemExit(1)
