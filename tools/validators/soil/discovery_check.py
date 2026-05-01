#!/usr/bin/env python3
from __future__ import annotations
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
import argparse, json, xml.etree.ElementTree as ET
from pathlib import Path
from tools.discovery.soil._discovery_common import *

def main(argv=None):
 a=argparse.ArgumentParser();a.add_argument('--discovery-root',required=True);a.add_argument('--discovery-id');x=a.parse_args(argv)
 droot=Path(x.discovery_root)/'discovery/soil'; reasons=[]
 did=x.discovery_id or load_json(droot/'current_discovery.json')['active_discovery_id']
 rel=droot/'releases'/did
 m=load_json(rel/'discovery_manifest.json'); r=load_json(rel/'discovery_receipt.json')
 if m.get('object_type')!='SoilDiscoveryManifest' or m.get('discovery_status')!='DISCOVERABLE': reasons.append('invalid manifest')
 if r.get('receipt_type')!='DiscoveryReceipt' or r.get('from_state')!='PUBLISHED' or r.get('to_state')!='DISCOVERABLE' or r.get('decision')!='pass' or not r.get('signatures'): reasons.append('invalid receipt')
 for rp,h in r.get('generated_artifacts',{}).items():
  p=rel/rp
  if not p.exists() or sha256_file(p)!=h: reasons.append(f'hash mismatch {rp}')
 for p in ['landing.schemaorg.jsonld','dcat.dataset.jsonld','stac_collection.json','ogcapi/landing.json','ogcapi/conformance.json','ogcapi/collections.json','ogcapi/collections/soil-moisture/items.json','feeds/soil.json','search_index.json']:
  json.loads((rel/p).read_text())
 ET.fromstring((rel/'feeds/soil.atom.xml').read_text()); ET.fromstring((rel/'sitemap.xml').read_text())
 if 'Sitemap:' not in (rel/'robots.txt').read_text(): reasons.append('robots missing sitemap')
 if scan_text_for_forbidden_terms((rel/'landing.html').read_text()): reasons.append('forbidden terms in html')
 if has_private_path((rel/'landing.html').read_text()): reasons.append('private path in html')
 out={'discovery_valid':not reasons,'discovery_id':did,'release_id':m.get('release_id'),'artifact_count':len(r.get('generated_artifacts',{})),'failure_reasons':reasons}
 print(json.dumps(out,sort_keys=True)); return 0 if not reasons else 1
if __name__=='__main__': raise SystemExit(main())
