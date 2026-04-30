from __future__ import annotations
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,validate,write_json,sha256_file

def rel(out_root:Path,p:Path)->str:return p.resolve().relative_to(out_root.resolve()).as_posix()
def main():
 p=argparse.ArgumentParser();p.add_argument('--vector-tile-package-manifest',type=Path,required=True);p.add_argument('--vector-tile-publication-receipt',type=Path,required=True);p.add_argument('--vector-tile-publication-audit-ledger',type=Path,required=True);p.add_argument('--snapshot-date',required=True);p.add_argument('--generated-at',required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
 out_root=a.out.parents[5]
 o={"schema_version":"1.0.0","object_type":"usda_plants_tile_archive_source","archive_source_id":f"kfm.tile_archive_source.flora.usda_plants.{a.snapshot_date}","domain":"flora","source_id":"usda_plants","snapshot_date":a.snapshot_date,"generated_at":a.generated_at,"vector_tile_package_manifest_ref":rel(out_root,a.vector_tile_package_manifest),"vector_tile_publication_receipt_ref":rel(out_root,a.vector_tile_publication_receipt),"vector_tile_publication_audit_ledger_ref":rel(out_root,a.vector_tile_publication_audit_ledger),"source_tile_root":f"published/flora/usda_plants/{a.snapshot_date}/tiles","source_layer":"county_presence","tile_format":"mvt","tile_scheme":"xyz","minzoom":0,"maxzoom":8,"source_tile_package_hash":sha256_file(a.vector_tile_package_manifest),"archive_targets":["pmtiles","mbtiles_optional"],"public_safety":{"derived_from_published_vector_tiles":True,"contains_occurrence_coordinates":False,"contains_point_occurrences":False,"contains_raw_refs":False,"contains_work_refs":False,"contains_quarantine_refs":False,"deploys_to_cdn":False},"status":"registered","reason_codes":["USDA_PLANTS_ARCHIVE_SOURCE_REGISTERED"]}
 o['source_hash']=canonical_hash(o,'source_hash');validate(ROOT/'schemas/flora/usda_plants_tile_archive_source.schema.json',o);write_json(a.out,o)
if __name__=='__main__':main()
