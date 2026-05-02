
from pathlib import Path
from kfm.air_quality.airnow.snapshot_preservation_review.run_snapshot_preservation_review import run_snapshot_preservation_review
FIX=Path("tests/fixtures/air_quality/airnow/layer21")

def run_manifest(name,tmp_path,created_at="2026-01-01T00:00:00Z"):
    return run_snapshot_preservation_review(str(FIX/f"manifests/{name}"), str(tmp_path), created_at)

def test_item_satisfaction_written(tmp_path):
 run_manifest('snapshot_preservation_review_valid_manifest.json',tmp_path)
 assert (tmp_path/'snapshot_preservation_item_satisfaction_matrix.json').exists()
