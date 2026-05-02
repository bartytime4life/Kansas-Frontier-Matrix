from pathlib import Path
from kfm.air_quality.airnow.preservation_closure_finalization.run_preservation_closure_finalization import run_preservation_closure_finalization
FIX=Path('tests/fixtures/air_quality/airnow/layer26/manifests')
def test_valid_manifest(tmp_path):
 r=run_preservation_closure_finalization(str(FIX/'preservation_closure_finalization_valid_manifest.json'),str(tmp_path),'2026-01-01T00:00:00Z');assert r['finite_outcome']=='ANSWER'
def test_missing_receipt_denied(tmp_path):
 r=run_preservation_closure_finalization(str(FIX/'preservation_closure_finalization_missing_layer25_receipt_manifest.json'),str(tmp_path),'2026-01-01T00:00:00Z');assert r['finite_outcome']=='DENY'
