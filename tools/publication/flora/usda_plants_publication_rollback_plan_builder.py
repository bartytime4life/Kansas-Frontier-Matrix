from __future__ import annotations
import argparse,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,validate,write_json
p=argparse.ArgumentParser();p.add_argument('--published-release-manifest',type=Path,required=True);p.add_argument('--snapshot-date',required=True);p.add_argument('--generated-at',required=True);p.add_argument('--out',type=Path,required=True);a=p.parse_args()
o={"schema_version":"1.0.0","object_type":"usda_plants_publication_rollback_plan","rollback_plan_id":f"kfm.publication_rollback_plan.flora.usda_plants.{a.snapshot_date}","domain":"flora","source_id":"usda_plants","snapshot_date":a.snapshot_date,"generated_at":a.generated_at,"published_release_manifest_ref":str(a.published_release_manifest),"rollback_strategy":"mark_superseded","rollback_actions":[{"action":"mark_publication_superseded","target_ref":str(a.published_release_manifest),"requires_human_approval":True}],"status":"ready","reason_codes":["USDA_PLANTS_PUBLICATION_ROLLBACK_PLAN_READY"]}
o['rollback_hash']=canonical_hash(o,'rollback_hash');validate(ROOT/'schemas/flora/usda_plants_publication_rollback_plan.schema.json',o);write_json(a.out,o)
