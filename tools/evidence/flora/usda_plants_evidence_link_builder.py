from __future__ import annotations
import argparse, json, sys
from datetime import datetime, timezone
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
if str(ROOT) not in sys.path: sys.path.insert(0,str(ROOT))
from tools.validators.flora.usda_plants_dataset_validator import validate_dataset
SOURCE_URI="https://plants.sc.egov.usda.gov/downloads"
SCHEMA=ROOT/"schemas/flora/usda_plants_evidence_link.schema.json"
def now(): return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00','Z')
def w(p,o): p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(o,indent=2,sort_keys=True)+"\n",encoding='utf-8')
def jv(payload,schema):
 from jsonschema import Draft202012Validator
 errs=list(Draft202012Validator(json.loads(schema.read_text())).iter_errors(payload));
 if errs: raise ValueError(str(errs[0]))
def main():
 ap=argparse.ArgumentParser(); ap.add_argument('--processed-dir',type=Path,required=True); ap.add_argument('--receipts-dir',type=Path,required=True); ap.add_argument('--proof-manifest',type=Path,required=True); ap.add_argument('--snapshot-date',required=True); ap.add_argument('--generated-at'); ap.add_argument('--out-dir',type=Path,required=True); a=ap.parse_args()
 generated=a.generated_at or now(); receipt_refs=sorted([f"receipts/flora/usda_plants/{p.name}" for p in a.receipts_dir.glob('*.json')])
 for p in sorted(a.processed_dir.glob('*.json')):
  d=json.loads(p.read_text()); sym=d['properties']['plants:symbol']; res=validate_dataset(d); decision='cite' if res['result']=='pass' else 'review_required'
  o={"schema_version":"1.0.0","object_type":"usda_plants_evidence_link","evidence_link_id":f"kfm.evidence_link.flora.usda_plants.{sym}","domain":"flora","candidate_id":d['id'],"plants_symbol":sym,"scientificName":d['properties']['scientificName'],"spec_hash":d['spec_hash'],"source":{"source_id":"usda_plants","source_type":"usda_plants_bulk","source_name":"USDA PLANTS Database","source_uri":SOURCE_URI,"source_descriptor_ref":"data/registry/flora/sources.yaml#usda_plants"},"rights":{"license":"USDA / U.S. Public Domain","rightsHolder":"United States Department of Agriculture","policy_label":"public"},"lineage":{"dataset_ref":f"processed/flora/usda_plants/{sym}.json","raw_refs":sorted([f"tests/fixtures/flora/usda_plants/raw/{Path(r).name}" for r in d.get('provenance',{}).get('raw_refs',[])]),"receipt_refs":receipt_refs,"proof_refs":["proofs/flora/usda_plants/spec_hash_manifest.json"],"catalog_refs":[],"release_candidate_refs":[]},"decision":decision,"status":"generated","generated_at":generated,"validation":{"result":res['result'],"reason_codes":res['reason_codes']}}
  jv(o,SCHEMA); w(a.out_dir/f"{sym}.evidence_link.json",o)
if __name__=='__main__': main()
