from __future__ import annotations
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,validate,write_json

def rel(out_root:Path,p:Path)->str:return p.resolve().relative_to(out_root.resolve()).as_posix()

def main():
 p=argparse.ArgumentParser();p.add_argument('--promoted-package',type=Path,required=True);p.add_argument('--promotion-receipt',type=Path,required=True);p.add_argument('--promotion-audit-ledger',type=Path,required=True);p.add_argument('--requester-id',required=True);p.add_argument('--requester-type',default='human');p.add_argument('--snapshot-date',required=True);p.add_argument('--generated-at',required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
 if a.requester_type!='human':raise SystemExit('USDA_PLANTS_PUBLICATION_REQUEST_NON_HUMAN_REFUSED')
 pkg=json.loads(a.promoted_package.read_text())
 if not pkg.get('sealed',False):raise SystemExit('USDA_PLANTS_PUBLICATION_REQUEST_PROMOTED_PACKAGE_NOT_SEALED')
 out_root=a.out.parents[5]
 o={"schema_version":"1.0.0","object_type":"usda_plants_publication_request","publication_request_id":f"kfm.publication_request.flora.usda_plants.{a.snapshot_date}","domain":"flora","source_id":"usda_plants","snapshot_date":a.snapshot_date,"generated_at":a.generated_at,"requested_by":{"requester_id":a.requester_id,"requester_type":"human"},"scope":{"promoted_package_ref":rel(out_root,a.promoted_package),"promotion_receipt_ref":rel(out_root,a.promotion_receipt),"promotion_audit_ledger_ref":rel(out_root,a.promotion_audit_ledger)},"intent":"publish_public_safe_flora_dataset","target_stage":"published","publication_state":"requested","allowed_public_outputs":["published_release_manifest","published_dataset_index","published_evidence_drawer_index","published_county_presence","published_map_descriptor"],"blocked_outputs":["precise_coordinates","county_geometry","vector_tiles","raw_files","work_files","quarantine_files"],"conditions":["Publish only from sealed promoted package.","No precise coordinates.","No county geometry.","No vector tile generation.","Human publication approval required."],"status":"requested","reason_codes":["USDA_PLANTS_PUBLICATION_REQUESTED"]}
 o['request_hash']=canonical_hash(o,'request_hash');validate(ROOT/'schemas/flora/usda_plants_publication_request.schema.json',o);write_json(a.out,o)
if __name__=='__main__':main()
