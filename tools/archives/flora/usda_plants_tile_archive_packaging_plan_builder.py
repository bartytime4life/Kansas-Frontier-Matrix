from __future__ import annotations
import argparse,shutil,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,validate,write_json

def rel(r,p):return p.resolve().relative_to(r.resolve()).as_posix()
def main():
 p=argparse.ArgumentParser();p.add_argument('--archive-source',type=Path,required=True);p.add_argument('--archive-publication-approval',type=Path,required=True);p.add_argument('--input-tile-package-manifest',type=Path,required=True);p.add_argument('--input-tilejson',type=Path,required=True);p.add_argument('--archive-engine',required=True);p.add_argument('--snapshot-date',required=True);p.add_argument('--generated-at',required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
 if a.archive_engine not in {'fixture_pmtiles','pmtiles_cli','mbtiles_fixture'}: raise SystemExit('USDA_PLANTS_ARCHIVE_PLAN_UNSUPPORTED_ENGINE')
 if a.archive_engine=='pmtiles_cli' and shutil.which('pmtiles') is None: raise SystemExit('USDA_PLANTS_ARCHIVE_PLAN_PMTILES_CLI_UNAVAILABLE')
 r=a.out.parents[5]
 o={"schema_version":"1.0.0","object_type":"usda_plants_tile_archive_packaging_plan","packaging_plan_id":f"kfm.tile_archive_packaging_plan.flora.usda_plants.{a.snapshot_date}","domain":"flora","source_id":"usda_plants","snapshot_date":a.snapshot_date,"generated_at":a.generated_at,"archive_source_ref":rel(r,a.archive_source),"archive_publication_approval_ref":rel(r,a.archive_publication_approval),"input_tile_package_manifest_ref":rel(r,a.input_tile_package_manifest),"input_tilejson_ref":rel(r,a.input_tilejson),"output_root":f"published/flora/usda_plants/{a.snapshot_date}/archives","archive_engine":a.archive_engine,"archive_targets":[{"target_type":"pmtiles","target_ref":f"published/flora/usda_plants/{a.snapshot_date}/archives/county_presence.pmtiles","required":True}],"optional_archive_targets":[{"target_type":"mbtiles","target_ref":f"published/flora/usda_plants/{a.snapshot_date}/archives/county_presence.mbtiles","required":False}],"guards":{"requires_human_approval":True,"requires_published_vector_tiles":True,"allows_occurrence_coordinates":False,"allows_raw_refs":False,"allows_work_refs":False,"allows_quarantine_refs":False,"allows_live_downloads":False,"allows_cdn_deploy":False,"allows_cloud_upload":False},"status":"pass","reason_codes":["USDA_PLANTS_ARCHIVE_PLAN_PASS"]}
 o['plan_hash']=canonical_hash(o,'plan_hash');validate(ROOT/'schemas/flora/usda_plants_tile_archive_packaging_plan.schema.json',o);write_json(a.out,o)
if __name__=='__main__':main()
