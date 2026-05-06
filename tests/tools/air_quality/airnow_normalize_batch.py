#!/usr/bin/env python3
import argparse, json, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path: sys.path.insert(0, str(ROOT))
from kfm.air_quality.airnow import normalize_record, build_receipt
from kfm.air_quality.airnow.ids import source_record_hash

def fail(msg):
    print(msg, file=sys.stderr); return 1

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--manifest',required=True)
    ap.add_argument('--input',required=True)
    ap.add_argument('--out-dir',required=True)
    ap.add_argument('--created-at',required=True)
    a=ap.parse_args()
    manifest=json.loads(Path(a.manifest).read_text())
    if manifest.get('no_network') is not True:
        return fail('NETWORK_FORBIDDEN: manifest no_network must be true')
    if manifest.get('bulk_loop_prohibited') is not True or any(x in str(manifest.get('intake_mode','')).lower() for x in ('bulk','zip')):
        return fail('BULK_LOOP_DENIED: bulk loop intent detected')
    mid=manifest.get('manifest_id')
    if not mid: return fail('invalid manifest_id')
    out=Path(a.out_dir); out.mkdir(parents=True,exist_ok=True)
    obs=[]; fc=[]; quar=[]; count=0
    for ln,line in enumerate(Path(a.input).read_text().splitlines(),start=1):
        if not line.strip():
            continue
        count +=1
        try:r=json.loads(line)
        except Exception:return fail(f'malformed jsonl line {ln}')
        n,q = normalize_record(r, mid, a.created_at)
        if q: quar.append(q)
        elif n['object_type']=='CanonicalAirQualityObservation': obs.append(n)
        else: fc.append(n)
    obs=sorted(obs,key=lambda x:x['canonical_id']); fc=sorted(fc,key=lambda x:x['canonical_id']); quar=sorted(quar,key=lambda x:x['quarantine_id'])
    p_obs=out/'normalized_observations.jsonl'; p_fc=out/'normalized_forecasts.jsonl'; p_q=out/'quarantine.jsonl'; p_r=out/'normalization_receipt.json'
    for p,data in ((p_obs,obs),(p_fc,fc),(p_q,quar)):
        p.write_text(''.join(json.dumps(x,sort_keys=True,separators=(',',':'))+'\n' for x in data))
    outpaths={'observations_jsonl':str(p_obs),'forecasts_jsonl':str(p_fc),'quarantine_jsonl':str(p_q)}
    receipt=build_receipt(mid,a.created_at,count,obs,fc,quar,source_record_hash(manifest),outpaths)
    p_r.write_text(json.dumps(receipt,indent=2,sort_keys=True)+'\n')
    print(json.dumps(receipt,indent=2,sort_keys=True))
    return 0
if __name__=='__main__':
    raise SystemExit(main())
