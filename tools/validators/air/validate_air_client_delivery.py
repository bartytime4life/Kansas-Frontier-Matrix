#!/usr/bin/env python3
import argparse,json,hashlib
from pathlib import Path
BAD=("data/raw/","data/work/","data/quarantine/","data/processed/air/")
def J(p): return json.loads(Path(p).read_text())
def deny(m): print('DENY',m); return 1
def etag(s): return f'"sha256:{s}"'
def check(d):
 files=['client_delivery_manifest.json','client_delivery_contract.json','client_route_manifest.json','static_response_bundle.json','client_cache_manifest.json','client_compatibility_report.json']
 for f in files:
  if not (d/f).exists(): return deny(f'missing {f}')
 bundle=J(d/'static_response_bundle.json'); cache=J(d/'client_cache_manifest.json'); cidx={e['artifact_ref']:e for e in cache.get('entries',[])}
 for r in bundle.get('responses',[]):
  p=d/r['response_ref']
  if not p.exists(): return deny('missing response ref')
  s=hashlib.sha256(p.read_bytes()).hexdigest()
  if r.get('sha256')!=s: return deny('sha mismatch')
  ce=cidx.get(r['response_ref'])
  if not ce or ce.get('etag')!=etag(s): return deny('bad etag')
 txt=(d/'client_delivery_manifest.json').read_text().lower()
 if any(x in txt for x in BAD): return deny('unsafe path in manifest')
 if 'published_delivery' in txt and 'fixture' in txt: return deny('fixture published')
 if 'validated aqs truth' in (d/'client_delivery_contract.json').read_text().lower(): return deny('nowcast truth violation')
 print('PASS',d)
 return 0
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('dirs',nargs='+');a.add_argument('--as-of');x=a.parse_args();
 rc=0
 for dd in x.dirs: rc=max(rc,check(Path(dd)))
 raise SystemExit(rc)
