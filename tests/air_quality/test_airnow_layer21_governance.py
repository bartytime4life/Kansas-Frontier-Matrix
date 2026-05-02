
from pathlib import Path
from kfm.air_quality.airnow.snapshot_preservation_review.run_snapshot_preservation_review import run_snapshot_preservation_review
FIX=Path("tests/fixtures/air_quality/airnow/layer21")

def run_manifest(name,tmp_path,created_at="2026-01-01T00:00:00Z"):
    return run_snapshot_preservation_review(str(FIX/f"manifests/{name}"), str(tmp_path), created_at)

def test_network_manifest_denied(tmp_path):
 r=run_manifest('snapshot_preservation_review_network_manifest.json',tmp_path)
 assert r['finite_outcome']=='DENY'

def test_no_packet_manifest_has_null_hash(tmp_path):
 r=run_manifest('snapshot_preservation_review_valid_no_packet_manifest.json',tmp_path)
 assert r['output_hashes']['snapshot_preservation_review_packet_hash'] is None
