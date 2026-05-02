from pathlib import Path
from kfm.air_quality.airnow.snapshot_preservation_finalization.run_snapshot_preservation_finalization import run_snapshot_preservation_finalization
FIX=Path('tests/fixtures/air_quality/airnow/layer22/manifests')
def test_valid_manifest(tmp_path):
 r=run_snapshot_preservation_finalization(str(FIX/'snapshot_preservation_finalization_valid_manifest.json'),str(tmp_path),'2026-01-01T00:00:00Z');assert r['finite_outcome']=='ANSWER'
def test_missing_receipt_denied(tmp_path):
 r=run_snapshot_preservation_finalization(str(FIX/'snapshot_preservation_finalization_missing_layer21_receipt_manifest.json'),str(tmp_path),'2026-01-01T00:00:00Z');assert r['finite_outcome']=='DENY'
