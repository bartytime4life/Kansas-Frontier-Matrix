#!/usr/bin/env python3
from __future__ import annotations
import sys, argparse, json
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.distribution.fauna._gbif_distribution_common import stable_hash, scan_forbidden

L=lambda p: json.loads(Path(p).read_text())

def main():
    a=argparse.ArgumentParser()
    a.add_argument('--distribution-bundle',required=True);a.add_argument('--runtime-answer',required=True);a.add_argument('--ui-cards',required=True);a.add_argument('--map-layers',required=True);a.add_argument('--output',required=True)
    x=a.parse_args(); b,_,cards,maps=[L(i) for i in [x.distribution_bundle,x.runtime_answer,x.ui_cards,x.map_layers]]
    out=[]
    for c in cards:
        r={"static_export_record_id":"gbif_static_TEST_001","domain":"fauna","source_system":"GBIF","export_type":"ui_card_json","distribution_bundle_id":b['distribution_bundle_id'],"artifact_id":c['card_id'],"artifact_type":"ui_card","public_url_path":c['public_url_path'],"relative_output_path":f"fauna/gbif/cards/{c['card_id']}.json","content_hash":"sha256:card","citation_refs":b['citation_index'],"public_safe":True,"created_at":datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')}
        r['kfm:spec_hash']=stable_hash(r,exclude=('created_at','static_export_record_id')); out.append(r)
    for m in maps:
        if m.get('geometry_kind')!='generalized_public_area': raise SystemExit('point layer export fails')
    errs=scan_forbidden(out)
    if errs: raise SystemExit('\n'.join(errs))
    Path(x.output).write_text(json.dumps(out,indent=2)+'\n'); print('ok')

if __name__=='__main__': main()
