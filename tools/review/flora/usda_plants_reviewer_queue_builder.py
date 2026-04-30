from __future__ import annotations
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3];sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,write_json,validate
M={'none':'none','info':'low','warning':'medium','critical':'high'}
a=argparse.ArgumentParser();a.add_argument('--alert',type=Path,required=True);a.add_argument('--observation',type=Path,required=True);a.add_argument('--generated-at',required=True);a.add_argument('--out',type=Path,required=True);x=a.parse_args();al=json.loads(x.alert.read_text());pr=M[al['severity']]
cmds=[]
if pr in ('medium','high'):cmds=["python tools/watchers/flora/usda_plants_manual_watcher.py --mode operator_snapshot --operator-raw-dir <raw_dir> --downloads-html tests/fixtures/flora/usda_plants/source_discovery/downloads_page_fixture.html --snapshot-date <YYYY-MM-DD> --generated-at <ISO8601> --out-dir <out_dir>"]
q={'schema_version':'1.0.0','object_type':'usda_plants_reviewer_queue','queue_id':f"kfm.reviewer_queue.flora.usda_plants.{x.generated_at.replace(':','').replace('-','')}",'domain':'flora','source_id':'usda_plants','generated_at':x.generated_at,'priority':pr,'review_status':'not_started','reviewer_hint':'flora-data-steward','alert_ref':str(x.alert),'observation_ref':str(x.observation),'suggested_next_commands':cmds,'required_review_gates':['source_check','rights_check','drift_check','quarantine_check','manual_snapshot_intake','release_candidate_review'],'blocked_actions':['publish','promote','auto_pr','auto_merge']}
q['queue_hash']=canonical_hash(q,'queue_hash');validate(ROOT/'schemas/flora/usda_plants_reviewer_queue.schema.json',q);write_json(x.out,q)
