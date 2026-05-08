from __future__ import annotations
import argparse,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,validate,write_json

def main():
 p=argparse.ArgumentParser();p.add_argument('--archive-publication-request',type=Path,required=True);p.add_argument('--approver-id',required=True);p.add_argument('--approver-type',default='human');p.add_argument('--decision',default='approved');p.add_argument('--snapshot-date',required=True);p.add_argument('--generated-at',required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
 if a.approver_type!='human':raise SystemExit('USDA_PLANTS_ARCHIVE_NON_HUMAN_APPROVAL_REFUSED')
 out_root=a.out.parents[5]
 o={"schema_version":"1.0.0","object_type":"usda_plants_tile_archive_publication_approval","archive_publication_approval_id":f"kfm.tile_archive_publication_approval.flora.usda_plants.{a.snapshot_date}","domain":"flora","source_id":"usda_plants","snapshot_date":a.snapshot_date,"generated_at":a.generated_at,"archive_publication_request_ref":a.archive_publication_request.resolve().relative_to(out_root.resolve()).as_posix(),"approver":{"approver_id":a.approver_id,"approver_type":"human","attestation":"approved"},"decision":a.decision,"decision_reason_codes":["USDA_PLANTS_ARCHIVE_PUBLICATION_APPROVED" if a.decision=='approved' else 'USDA_PLANTS_ARCHIVE_PUBLICATION_REJECTED'],"approval_conditions":["Archive derives only from published vector tile package.","No plant occurrence coordinates.","No raw/work/quarantine refs.","No CDN deployment in this layer."],"publication_state":"approved" if a.decision=='approved' else a.decision,"status":"pass" if a.decision=='approved' else 'fail'}
 o['approval_hash']=canonical_hash(o,'approval_hash');validate(ROOT/'schemas/flora/usda_plants_tile_archive_publication_approval.schema.json',o);write_json(a.out,o)
if __name__=='__main__':main()
