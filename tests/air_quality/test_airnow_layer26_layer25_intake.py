from pathlib import Path
import json
from kfm.air_quality.airnow.preservation_closure_finalization.run_preservation_closure_finalization import run_preservation_closure_finalization
FIX=Path('tests/fixtures/air_quality/airnow/layer26/manifests')
def test_layer25_receipt_object_type_checked(tmp_path):
 r=run_preservation_closure_finalization(str(FIX/'preservation_closure_finalization_valid_manifest.json'),str(tmp_path),'2026-01-01T00:00:00Z');assert r['validation_outcome']=='PASS'
