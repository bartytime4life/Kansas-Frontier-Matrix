from __future__ import annotations
import argparse, json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]; SCHEMA=ROOT/'schemas/flora/usda_plants_evidence_drawer_payload.schema.json'; SOURCE_URI='https://plants.sc.egov.usda.gov/downloads'
def w(p,o): p.parent.mkdir(parents=True,exist_ok=True); p.write_text(json.dumps(o,indent=2,sort_keys=True)+'\n')
def main():
 p=argparse.ArgumentParser();p.add_argument('--processed-dir',type=Path,required=True);p.add_argument('--evidence-dir',type=Path,required=True);p.add_argument('--catalog-ref',required=True);p.add_argument('--release-candidate-ref',required=True);p.add_argument('--snapshot-date',required=True);p.add_argument('--out-dir',type=Path,required=True);a=p.parse_args()
 from jsonschema import Draft202012Validator; v=Draft202012Validator(json.loads(SCHEMA.read_text()))
 for fp in sorted(a.processed_dir.glob('*.json')):
  d=json.loads(fp.read_text());sym=d['properties']['plants:symbol'];ev=f'evidence/flora/usda_plants/{sym}.evidence_link.json';states=d['distributions']['state'];counties=d['distributions']['county']
  o={"schema_version":"1.0.0","object_type":"usda_plants_evidence_drawer_payload","payload_id":f"kfm.ui.evidence_drawer.flora.usda_plants.{sym}","domain":"flora","plants_symbol":sym,"title":d['properties']['nationalCommonName'],"subtitle":d['properties']['scientificName'],"badges":["USDA PLANTS","public","county distribution"],"summary":{"family":d['properties']['family'],"nativeStatus":d['properties']['nativeStatus'],"growthHabit":d['properties']['growthHabit'],"wetlandStatus":d['properties']['wetlandStatus'],"state_count":len(states),"county_count":len(counties)},"source":{"source_name":"USDA PLANTS Database","source_uri":SOURCE_URI,"snapshot_date":a.snapshot_date},"rights":{"license":"USDA / U.S. Public Domain","rightsHolder":"United States Department of Agriculture","policy_label":"public"},"distribution_preview":{"states":states[:10],"counties":[{"fips":c['fips'],"presence":c['presence']} for c in counties[:25]]},"evidence":{"dataset_ref":f"processed/flora/usda_plants/{sym}.json","evidence_link_ref":ev,"catalog_ref":a.catalog_ref,"release_candidate_ref":a.release_candidate_ref,"spec_hash":d['spec_hash']},"actions":{"can_publish":False,"can_promote":False,"requires_review":False}}
  errs=list(v.iter_errors(o));
  if errs:
   raise ValueError(str(errs[0]))
  w(a.out_dir/f'{sym}.json',o)
if __name__=='__main__': main()
