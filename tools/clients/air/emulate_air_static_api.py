#!/usr/bin/env python3
import argparse,json
from pathlib import Path
BAD=("data/raw/","data/work/","data/quarantine/","data/processed/air/")
if __name__=='__main__':
 a=argparse.ArgumentParser();a.add_argument('--delivery-dir',required=True);a.add_argument('--route');a.add_argument('--record-id');a.add_argument('--publication-id');a.add_argument('--delta-cursor');a.add_argument('--include-candidates',action='store_true');a.add_argument('--show-headers',action='store_true');x=a.parse_args();
 d=Path(x.delivery_dir); rm=json.loads((d/'client_route_manifest.json').read_text())
 if not x.include_candidates and rm.get('status','').startswith('fixture'): raise SystemExit('DENY fixture routes need --include-candidates')
 m={'/air/v1/index':'responses/index.json','/air/v1/status':'responses/status.json','/air/v1/delta':'responses/deltas/delta.json','/air/v1/invalidation-notices':'responses/deltas/invalidation_notices.json'}
 if x.record_id: m[f'/air/v1/records/{x.record_id}']=f'responses/records/{x.record_id}.json'; m[f'/air/v1/provenance/{x.record_id}']=f'responses/provenance/{x.record_id}.json'
 ref=m.get(x.route)
 if not ref: raise SystemExit('DENY route unsupported')
 if any(b in ref.lower() for b in BAD): raise SystemExit('DENY unsafe ref')
 p=d/ref
 if not p.exists(): raise SystemExit('DENY response missing')
 if x.show_headers: print(json.dumps({'Content-Type':'application/json'},sort_keys=True))
 print(p.read_text())
