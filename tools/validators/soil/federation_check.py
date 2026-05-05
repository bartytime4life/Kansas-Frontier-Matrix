#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
import argparse, json, xml.etree.ElementTree as ET
from pathlib import Path
from tools.federation.soil._federation_common import *
def main(argv=None):
 a=argparse.ArgumentParser();a.add_argument('--federation-root',required=True);a.add_argument('--federation-id');x=a.parse_args(argv)
 root=Path(x.federation_root)/'federation/soil';fid=x.federation_id or load_json(root/'current_federation.json')['active_federation_id'];rel=root/'releases'/fid;rs=[]
 m=load_json(rel/'federation_manifest.json'); rc=load_json(rel/'federation_receipt.json'); mm=load_json(rel/'mirror/mirror_manifest.json')
 if m.get('object_type')!='SoilFederationManifest' or m.get('federation_status')!='FEDERATION_READY': rs.append('invalid manifest')
 if rc.get('receipt_type')!='FederationReceipt' or rc.get('decision')!='pass' or not rc.get('signatures') or rc.get('live_submission_performed') is not False: rs.append('invalid receipt')
 for rp,h in rc.get('generated_artifacts',{}).items():
  p=rel/rp
  if not p.exists() or sha256_file(p)!=h: rs.append(f'hash mismatch {rp}')
 for p in rel.rglob('*'):
  if p.is_file() and p.suffix in {'.json','.jsonld'}: json.loads(p.read_text())
 if (rel/'notifications/feed_delta.atom.xml').exists(): ET.fromstring((rel/'notifications/feed_delta.atom.xml').read_text())
 if mm.get('object_type')!='SoilMirrorManifest' or mm.get('mirror_status')!='MIRROR_READY': rs.append('invalid mirror manifest')
 out={'federation_valid':not rs,'federation_id':fid,'discovery_id':m.get('discovery_id'),'release_id':m.get('release_id'),'target_count':m.get('target_count',0),'failure_reasons':rs}
 print(json.dumps(out,sort_keys=True)); return 0 if not rs else 1
if __name__=='__main__': raise SystemExit(main())
