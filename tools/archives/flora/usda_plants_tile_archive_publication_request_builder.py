from __future__ import annotations
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,validate,write_json,sha256_file

def rel(out_root:Path,p:Path)->str:return p.resolve().relative_to(out_root.resolve()).as_posix()
def main():
 p=argparse.ArgumentParser();p.add_argument('--archive-source',type=Path,required=True);p.add_argument('--vector-tile-package-manifest',type=Path,required=True);p.add_argument('--requester-id',required=True);p.add_argument('--requester-type',default='human');p.add_argument('--snapshot-date',required=True);p.add_argument('--generated-at',required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
 if a.requester_type!='human':raise SystemExit('USDA_PLANTS_ARCHIVE_REQUEST_NON_HUMAN_REFUSED')
 out_root=a.out.parents[5];o={"schema_version":"1.0.0","object_type":"usda_plants_tile_archive_publication_request","archive_publication_request_id":f"kfm.tile_archive_publication_request.flora.usda_plants.{a.snapshot_date}","domain":"flora","source_id":"usda_plants","snapshot_date":a.snapshot_date,"generated_at":a.generated_at,"requested_by":{"requester_id":a.requester_id,"requester_type":"human"},"scope":{"archive_source_ref":rel(out_root,a.archive_source),"vector_tile_package_manifest_ref":rel(out_root,a.vector_tile_package_manifest)},"intent":"publish_portable_tile_archive","publication_state":"requested","allowed_outputs":["pmtiles_archive","pmtiles_manifest","static_host_handoff","cache_integrity_manifest","pmtiles_map_style"],"optional_outputs":["mbtiles_archive","mbtiles_manifest"],"blocked_outputs":["occurrence_coordinates","point_occurrences","raw_files","work_files","quarantine_files","live_downloads","cdn_deploy","cloud_upload"],"status":"requested","reason_codes":["USDA_PLANTS_ARCHIVE_PUBLICATION_REQUESTED"]}
 o['request_hash']=canonical_hash(o,'request_hash');validate(ROOT/'schemas/flora/usda_plants_tile_archive_publication_request.schema.json',o);write_json(a.out,o)
if __name__=='__main__':main()
