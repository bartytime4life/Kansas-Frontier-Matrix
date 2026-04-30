from __future__ import annotations
import argparse,json,sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]; sys.path.insert(0, str(ROOT))
from tools.quality.flora.usda_common import canonical_hash, write_json, validate

def main():
  p=argparse.ArgumentParser();p.add_argument('--release-candidate',type=Path,required=True);p.add_argument('--snapshot-date',required=True);p.add_argument('--generated-at',required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
  if not a.release_candidate.exists(): raise SystemExit('USDA_PLANTS_RIGHTS_SOURCE_URI_MISSING')
  rc=json.loads(a.release_candidate.read_text())
  reasons=[]; status='pass'
  if rc.get('source_id')!='usda_plants': reasons.append('USDA_PLANTS_RIGHTS_SOURCE_URI_MISSING'); status='fail'
  rights={"license":"USDA / U.S. Public Domain","rightsHolder":"United States Department of Agriculture","policy_label":"public","citation_required":True,"citation_text":f"USDA PLANTS Database, snapshot {a.snapshot_date}."}
  if not rights['citation_text']: reasons.append('USDA_PLANTS_RIGHTS_CITATION_MISSING'); status='fail'
  if status=='pass': reasons.append('USDA_PLANTS_RIGHTS_PUBLIC_CONFIRMED')
  o={"schema_version":"1.0.0","object_type":"usda_plants_rights_attestation","rights_attestation_id":f"kfm.rights_attestation.flora.usda_plants.{a.snapshot_date}","domain":"flora","source_id":"usda_plants","source_uri":"https://plants.sc.egov.usda.gov/downloads","snapshot_date":a.snapshot_date,"generated_at":a.generated_at,"rights":rights,"attested_refs":[str(a.release_candidate)],"status":status,"reason_codes":reasons}
  o['attestation_hash']=canonical_hash(o,'attestation_hash'); validate(ROOT/'schemas/flora/usda_plants_rights_attestation.schema.json',o); write_json(a.out,o)
if __name__=='__main__':main()
