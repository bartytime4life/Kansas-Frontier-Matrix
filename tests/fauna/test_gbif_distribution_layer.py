import json,subprocess,sys,tempfile
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
V=ROOT/'tests/fixtures/fauna/gbif/valid/distribution'

def run(cmd): subprocess.check_call(cmd,cwd=ROOT)

def test_end_to_end_and_hash_stability():
 with tempfile.TemporaryDirectory() as td:
  td=Path(td)
  b=td/'b.json';se=td/'se.json';sr=td/'sr.json';ap=td/'ap.json';ec=td/'ec.json';gr=td/'gr.json';cr=td/'cr.json';tr=td/'tr.json';tcr=td/'tcr.json'
  run([sys.executable,'tools/distribution/fauna/kfm_gbif_distribution_bundle.py','--release-registry',V/'release_registry_entry.json','--manifest',V/'public_release_manifest.json','--review-decision',V/'review_decision_receipt.json','--package',V/'publication_package.json','--output',b])
  run([sys.executable,'tools/distribution/fauna/kfm_gbif_static_export.py','--distribution-bundle',b,'--runtime-answer',V/'runtime_answer.json','--ui-cards',V/'ui_cards.json','--map-layers',V/'map_layers.json','--output',se])
  run([sys.executable,'tools/search/fauna/kfm_gbif_search_index.py','--distribution-bundle',b,'--ui-cards',V/'ui_cards.json','--output',sr])
  run([sys.executable,'tools/api/fauna/kfm_gbif_public_api_dto.py','--distribution-bundle',b,'--runtime-answer',V/'runtime_answer.json','--output',ap])
  run([sys.executable,'tools/monitoring/fauna/kfm_gbif_public_endpoint_check.py','--distribution-bundle',b,'--static-exports',se,'--api-responses',ap,'--search-records',sr,'--output',ec])
  run([sys.executable,'tools/ci/fauna/kfm_gbif_distribution_gate.py','--distribution-bundle',b,'--static-exports',se,'--search-records',sr,'--api-responses',ap,'--endpoint-checks',ec,'--output',gr])
  run([sys.executable,'tools/cache/fauna/kfm_gbif_cache_invalidation.py','--distribution-bundle',b,'--reason','new_public_release','--output',cr])
  run([sys.executable,'tools/takedown/fauna/kfm_gbif_takedown_enforce.py','--distribution-bundle',b,'--withdrawal-receipt',V/'withdrawal_receipt.json','--reason','withdrawal_applied','--output',tr,'--cache-receipt-output',tcr])
  bd=json.loads(b.read_text()); assert bd['distribution_state']=='ready'
  old=bd['kfm:spec_hash']; bd['created_at']='2099-01-01T00:00:00Z'; from tools.distribution.fauna._gbif_distribution_common import stable_hash; assert old==stable_hash(bd,exclude=('created_at','distribution_bundle_id'))
  assert json.loads(gr.read_text())['gate_posture']=='passed'
