#!/usr/bin/env python
import argparse, json, sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from pathlib import Path
from kfm.air_quality.airnow.file_products.manifest import validate_manifest
from kfm.air_quality.airnow.file_products.parse_common import parse_manifest_file
from kfm.air_quality.airnow.file_products.receipts import build_receipt

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--manifest',required=True); ap.add_argument('--out-dir',required=True); ap.add_argument('--created-at',required=True)
    a=ap.parse_args()
    try: m=json.loads(Path(a.manifest).read_text())
    except Exception:
        return 2
    errs=validate_manifest(m)
    if errs:
        r=build_receipt(m,a.created_at,0,[],[],errors=errs,validation_outcome='FAIL',finite_outcome='DENY' if any(e in errs for e in ['NETWORK_FORBIDDEN','SECRET_FIELD_DENIED','BULK_LOOP_DENIED']) else 'ERROR')
        print(json.dumps(r,sort_keys=True)); return 1
    p=Path(m['input_file'])
    if not p.exists():
        r=build_receipt(m,a.created_at,0,[],[],errors=['INPUT_FILE_MISSING'],validation_outcome='FAIL',finite_outcome='ERROR'); print(json.dumps(r,sort_keys=True)); return 1
    parsed,quar=parse_manifest_file(m,p,a.created_at)
    parsed=sorted(parsed,key=lambda x:x['staging_id']); quar=sorted(quar,key=lambda x:x['quarantine_id'])
    out=Path(a.out_dir); out.mkdir(parents=True,exist_ok=True)
    (out/'parsed_records.jsonl').write_text('\n'.join(json.dumps(x,sort_keys=True,separators=(',',':')) for x in parsed)+'\n' if parsed else '')
    (out/'quarantine.jsonl').write_text('\n'.join(json.dumps(x,sort_keys=True,separators=(',',':')) for x in quar)+'\n' if quar else '')
    fo='ANSWER' if parsed else 'ABSTAIN'
    rec=build_receipt(m,a.created_at,len(parsed)+len(quar),[json.dumps(x,sort_keys=True,separators=(',',':')) for x in parsed],[json.dumps(x,sort_keys=True,separators=(',',':')) for x in quar],finite_outcome=fo)
    (out/'parse_receipt.json').write_text(json.dumps(rec,sort_keys=True,indent=2)+'\n')
    print(json.dumps(rec,sort_keys=True))
    return 0
if __name__=='__main__':
    raise SystemExit(main())
