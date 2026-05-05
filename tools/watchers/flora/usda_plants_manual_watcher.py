from __future__ import annotations
import argparse,subprocess,sys,os
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[3]
sys.path.insert(0,str(ROOT))
from tools.quality.flora.usda_common import canonical_hash,write_json

def run(c):
 return subprocess.run([sys.executable,*c],cwd=ROOT,check=True)
def main():
 a=argparse.ArgumentParser();a.add_argument('--mode',required=True);a.add_argument('--downloads-html');a.add_argument('--operator-raw-dir');a.add_argument('--source-uri');a.add_argument('--allow-network',action='store_true');a.add_argument('--operator-ack',action='store_true');a.add_argument('--allow-non-usda-source-for-tests',action='store_true');a.add_argument('--snapshot-date',required=True);a.add_argument('--generated-at',required=True);a.add_argument('--out-dir',required=True);x=a.parse_args()
 out=Path(x.out_dir);steps=[];reasons=[];status='pass';final='release_candidate_ready';outputs={k:None for k in ['raw_snapshot_manifest_ref','snapshot_lock_ref','staged_input_manifest_ref','proof_manifest_ref','catalog_ref','release_candidate_ref','snapshot_diff_ref','pr_handoff_manifest_ref']}
 try:
  raw=out/f'raw/flora/usda_plants/{x.snapshot_date}';work=out/f'work/flora/usda_plants/{x.snapshot_date}';pro=out/'processed/flora/usda_plants';rel=out/'releases/flora/usda_plants';proof=out/'proofs/flora/usda_plants'
  if x.mode in ('offline_mock','operator_snapshot'):
   run(['tools/sources/flora/usda_plants_source_discovery.py','--downloads-html',x.downloads_html,'--snapshot-date',x.snapshot_date,'--generated-at',x.generated_at,'--out',str(work/'source_discovery.json')]);steps.append({'name':'source_discovery','status':'pass','output_ref':str(work/'source_discovery.json'),'reason_codes':[]})
   run(['tools/intake/flora/usda_plants_snapshot_intake.py','--raw-dir',x.operator_raw_dir,'--snapshot-date',x.snapshot_date,'--generated-at',x.generated_at,'--out-dir',str(raw)]); outputs['raw_snapshot_manifest_ref']=f'raw/flora/usda_plants/{x.snapshot_date}/raw_snapshot_manifest.json'
  elif x.mode=='live_manual':
   c=['tools/sources/flora/usda_plants_live_fetcher.py','--source-uri',x.source_uri,'--snapshot-date',x.snapshot_date,'--generated-at',x.generated_at,'--allow-network','--operator-ack','--out-dir',str(raw)]
   if x.allow_non_usda_source_for_tests:c.append('--allow-non-usda-source-for-tests')
   run(c);outputs['raw_snapshot_manifest_ref']=f'raw/flora/usda_plants/{x.snapshot_date}/raw_snapshot_manifest.json'
  else: raise RuntimeError('USDA_PLANTS_WATCHER_MODE_INVALID')
  run(['tools/intake/flora/usda_plants_snapshot_lock_builder.py','--raw-snapshot-manifest',str(raw/'raw_snapshot_manifest.json'),'--snapshot-date',x.snapshot_date,'--generated-at',x.generated_at,'--out',str(raw/'snapshot_lock.json')]);outputs['snapshot_lock_ref']=f'raw/flora/usda_plants/{x.snapshot_date}/snapshot_lock.json'
  run(['tools/normalize/flora/usda_plants_stage_raw_snapshot.py','--raw-manifest',str(raw/'raw_snapshot_manifest.json'),'--snapshot-date',x.snapshot_date,'--generated-at',x.generated_at,'--out',str(work/'staged_input_manifest.json')]);outputs['staged_input_manifest_ref']=f'work/flora/usda_plants/{x.snapshot_date}/staged_input_manifest.json'
  run(['tools/ingest/flora/usda_plants_fixture_loader.py','--staged-input-manifest',str(work/'staged_input_manifest.json'),'--snapshot-date',x.snapshot_date,'--generated-at',x.generated_at,'--out-dir',str(pro)])
  run(['tools/proofs/flora/usda_plants_proof_manifest.py','--datasets-dir',str(pro),'--snapshot-date',x.snapshot_date,'--generated-at',x.generated_at,'--out',str(proof/'spec_hash_manifest.json')]);outputs['proof_manifest_ref']='proofs/flora/usda_plants/spec_hash_manifest.json'
  run(['tools/catalog/flora/usda_plants_catalog_builder.py','--datasets-dir',str(pro),'--proof-manifest',str(proof/'spec_hash_manifest.json'),'--snapshot-date',x.snapshot_date,'--generated-at',x.generated_at,'--out',str(out/'catalog/flora/usda_plants/catalog.json')]);outputs['catalog_ref']='catalog/flora/usda_plants/catalog.json'
  run(['tools/release/flora/usda_plants_release_candidate_builder.py','--catalog',str(out/'catalog/flora/usda_plants/catalog.json'),'--snapshot-date',x.snapshot_date,'--generated-at',x.generated_at,'--out',str(rel/f'release_candidate_{x.snapshot_date}.json')]);outputs['release_candidate_ref']=f'releases/flora/usda_plants/release_candidate_{x.snapshot_date}.json'
  run(['tools/diff/flora/usda_plants_snapshot_diff.py','--base-lock',str(raw/'snapshot_lock.json'),'--head-lock',str(raw/'snapshot_lock.json'),'--generated-at',x.generated_at,'--out',str(work/'snapshot_diff.json')]);outputs['snapshot_diff_ref']=f'work/flora/usda_plants/{x.snapshot_date}/snapshot_diff.json'
  run(['tools/release/flora/usda_plants_pr_handoff_builder.py','--release-candidate',str(rel/f'release_candidate_{x.snapshot_date}.json'),'--snapshot-diff',str(work/'snapshot_diff.json'),'--watcher-run-receipt',str(out/'receipts/flora/usda_plants/watcher_run_receipt.json'),'--snapshot-date',x.snapshot_date,'--generated-at',x.generated_at,'--out',str(rel/f'pr_handoff_{x.snapshot_date}.json')]);outputs['pr_handoff_manifest_ref']=f'releases/flora/usda_plants/pr_handoff_{x.snapshot_date}.json'
 except Exception as e:
  status='fail';final='failed';reasons+=['USDA_PLANTS_WATCHER_STEP_FAILED',str(e)]
 rec={'schema_version':'1.0.0','object_type':'usda_plants_watcher_run_receipt','watcher_run_id':f'kfm.watcher_run.flora.usda_plants.{x.snapshot_date}','domain':'flora','source_id':'usda_plants','snapshot_date':x.snapshot_date,'generated_at':x.generated_at,'mode':x.mode,'network_mode':'manual_enabled' if x.mode=='live_manual' else 'disabled','ci':os.getenv('CI','').lower()=='true','steps':steps,'outputs':outputs,'final_state':final,'published':False,'promoted':False,'status':status,'reason_codes':sorted(set(reasons))}
 rec['receipt_hash']=canonical_hash(rec,'receipt_hash');p=out/'receipts/flora/usda_plants/watcher_run_receipt.json';write_json(p,rec)
 return 0 if status=='pass' else 2
if __name__=='__main__':raise SystemExit(main())
