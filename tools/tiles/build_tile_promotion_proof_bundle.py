#!/usr/bin/env python3
import argparse,hashlib,json
from pathlib import Path

def load(p): return json.loads(Path(p).read_text())
def canon(o): return json.dumps(o,sort_keys=True,separators=(',',':'))
def hbytes(b): return 'sha256:'+hashlib.sha256(b).hexdigest()
def hfile(p): return hbytes(Path(p).read_bytes())

def main():
  p=argparse.ArgumentParser()
  p.add_argument('--delta-manifest',required=True);p.add_argument('--trace',required=True);p.add_argument('--verified-tile-list',required=True)
  p.add_argument('--release-manifest',required=True);p.add_argument('--evidence-bundle',required=True);p.add_argument('--run-receipt',required=True)
  p.add_argument('--out-dir',required=True)
  a=p.parse_args(); out=Path(a.out_dir); out.mkdir(parents=True,exist_ok=True)
  refs=[a.delta_manifest,a.trace,a.verified_tile_list,a.release_manifest,a.evidence_bundle,a.run_receipt]
  inputs=[{"ref":r,"sha256":hfile(r)} for r in refs]
  t=load(a.trace)
  passed=t.get('changed_tile_verification_pct',0)>=100 and t.get('masked_pct',999)<=15
  summary={"verifier_trace_pass":passed,"changed_tiles":len(load(a.verified_tile_list).get('tiles',[]))}
  base={"schema_version":"v1","object_type":"TilePromotionProofBundle","result":"ALLOW" if passed else "DENY","inputs":inputs,
        "rollback_ref":"NEEDS_VERIFICATION:rollback","correction_ref":"NEEDS_VERIFICATION:correction","summary":summary}
  proof_id='kfm.tile_proof_bundle.'+hashlib.sha256(canon(base).encode()).hexdigest()[:16]
  proof={**base,"proof_bundle_id":proof_id}
  (out/'tile_promotion_proof_bundle.json').write_text(json.dumps(proof,indent=2)+"\n")
  rec_base={"schema_version":"v1","object_type":"TileVerificationReceipt","result":proof['result'],"proof_bundle_ref":"tile_promotion_proof_bundle.json","summary":summary}
  rid='kfm.tile_verification_receipt.'+hashlib.sha256(canon(rec_base).encode()).hexdigest()[:16]
  rec={**rec_base,"verification_receipt_id":rid}
  (out/'tile_verification_receipt.json').write_text(json.dumps(rec,indent=2)+"\n")

if __name__=='__main__': main()
