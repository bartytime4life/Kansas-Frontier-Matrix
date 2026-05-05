#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
import argparse, json, os, sys
from pathlib import Path
from tools.ops.soil._ops_common import scan_payload_for_forbidden_terms

def main(argv=None):
 p=argparse.ArgumentParser(); p.add_argument('--access-log',required=True); a=p.parse_args(argv)
 reasons=[]; n=0
 for ln in Path(a.access_log).read_text(encoding='utf-8').splitlines():
  if not ln.strip(): continue
  n+=1
  try:e=json.loads(ln)
  except Exception: reasons.append('invalid json line'); continue
  if e.get('object_type')!='SoilPublicApiAccessLogEntry': reasons.append('bad object_type')
  if e.get('method') not in {'GET','HEAD','OPTIONS'}: reasons.append('bad method')
  if not isinstance(e.get('status'),int): reasons.append('bad status')
  if not e.get('route_template') or not e.get('release_id') or not e.get('schema_version'): reasons.append('missing fields')
  if scan_payload_for_forbidden_terms(e): reasons.append('forbidden terms found')
  t=json.dumps(e).lower()
  if any(x in t for x in ['authorization','cookie','/raw/','/work/','/quarantine/','/processed/']): reasons.append('sensitive field/path found')
 out={'access_log_valid':not reasons,'entry_count':n,'failure_reasons':sorted(set(reasons))}; print(json.dumps(out,sort_keys=True)); return 0 if out['access_log_valid'] else 1
if __name__=='__main__': raise SystemExit(main())
