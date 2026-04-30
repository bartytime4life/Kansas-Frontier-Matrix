from __future__ import annotations
import argparse,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,validate,write_json

def main():
 p=argparse.ArgumentParser();p.add_argument('--pmtiles-package-manifest',type=Path,required=True);p.add_argument('--static-host-handoff',type=Path,required=True);p.add_argument('--snapshot-date',required=True);p.add_argument('--generated-at',required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
 s=a.snapshot_date
 o={"schema_version":"1.0.0","object_type":"usda_plants_tile_archive_rollback_plan","rollback_plan_id":f"kfm.tile_archive_rollback_plan.flora.usda_plants.{s}","domain":"flora","source_id":"usda_plants","snapshot_date":s,"generated_at":a.generated_at,"pmtiles_package_manifest_ref":f"published/flora/usda_plants/{s}/archives/pmtiles_package_manifest.json","static_host_handoff_ref":f"published/flora/usda_plants/{s}/hosting/static_host_handoff.json","rollback_strategy":"mark_superseded","rollback_actions":[{"action":"mark_pmtiles_archive_superseded","target_ref":f"published/flora/usda_plants/{s}/archives/county_presence.pmtiles","requires_human_approval":True}],"status":"ready","reason_codes":[]}
 o['rollback_hash']=canonical_hash(o,'rollback_hash');validate(ROOT/'schemas/flora/usda_plants_tile_archive_rollback_plan.schema.json',o);write_json(a.out,o)
if __name__=='__main__':main()
