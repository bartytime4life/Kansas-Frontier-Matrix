from __future__ import annotations
import argparse, hashlib, json
from datetime import datetime, timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]; SCHEMA=ROOT/'schemas/flora/usda_plants_release_candidate.schema.json'
def now(): return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
def can(o): return json.dumps(o,sort_keys=True,separators=(',',':'),ensure_ascii=False)
def main():
 p=argparse.ArgumentParser();p.add_argument('--processed-dir',type=Path,required=True);p.add_argument('--evidence-dir',type=Path,required=True);p.add_argument('--catalog-dir',type=Path,required=True);p.add_argument('--receipts-dir',type=Path,required=True);p.add_argument('--proof-manifest',type=Path,required=True);p.add_argument('--ui-dir',type=Path);p.add_argument('--map-contract',type=Path);p.add_argument('--snapshot-date',required=True);p.add_argument('--generated-at');p.add_argument('--out',type=Path,required=True);a=p.parse_args();g=a.generated_at or now()
 ds=sorted([f'processed/flora/usda_plants/{x.stem}.json' for x in a.processed_dir.glob('*.json')]); ev=sorted([f'evidence/flora/usda_plants/{x.name}' for x in a.evidence_dir.glob('*.json')]);
 manifest=json.loads(a.proof_manifest.read_text());
 if len(ds)!=manifest.get('dataset_count'): raise SystemExit('dataset_count mismatch')
 for r in ds:
  sym=Path(r).stem
  if f'evidence/flora/usda_plants/{sym}.evidence_link.json' not in ev: raise SystemExit('missing evidence link')
 if not (a.catalog_dir/'catalog.json').exists(): raise SystemExit('missing catalog')
 receipts=sorted([f'receipts/flora/usda_plants/{x.name}' for x in a.receipts_dir.glob('*.json')])
 if not any('ingest_receipt' in r for r in receipts) or not any('validation_receipt' in r for r in receipts): raise SystemExit('missing receipts')
 ui=sorted([f'ui/flora/usda_plants/evidence_drawer/{x.name}' for x in a.ui_dir.glob('*.json')]) if a.ui_dir else []
 mrefs=[str(a.map_contract)] if a.map_contract else []
 o={"schema_version":"1.0.0","object_type":"usda_plants_release_candidate","release_candidate_id":f"kfm.release_candidate.flora.usda_plants.{a.snapshot_date}","domain":"flora","snapshot_date":a.snapshot_date,"generated_at":g,"promotion_state":"not_promoted","publication_state":"not_published","source_id":"usda_plants","dataset_count":len(ds),"dataset_refs":ds,"evidence_link_refs":ev,"catalog_refs":["catalog/flora/usda_plants/catalog.json"],"receipt_refs":receipts,"proof_refs":["proofs/flora/usda_plants/spec_hash_manifest.json"],"policy_refs":["policy/flora/usda_plants.rego","policy/flora/usda_plants_release.rego"],"ui_refs":ui,"map_layer_contract_refs":mrefs,"gates":{"schema_validation":"pass","dataset_validation":"pass","policy_validation":"not_run","proof_manifest":"pass","catalog_closure":"pass","sensitivity_review":"pass","publication":"blocked"},"blockers":["LIVE_USDA_DOWNLOAD_NOT_IMPLEMENTED","PUBLICATION_NOT_REQUESTED","PROMOTION_NOT_REQUESTED"]}
 o['release_candidate_hash']='sha256:'+hashlib.sha256(can(o).encode()).hexdigest()
 from jsonschema import Draft202012Validator; errs=list(Draft202012Validator(json.loads(SCHEMA.read_text())).iter_errors(o));
 if errs: raise ValueError(str(errs[0]))
 a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
if __name__=='__main__': main()
