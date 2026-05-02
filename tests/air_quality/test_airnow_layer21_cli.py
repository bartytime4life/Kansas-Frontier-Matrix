import subprocess

def test_cli_valid(tmp_path):
 p=subprocess.run(["python","tools/air_quality/airnow_layer21_snapshot_preservation_review.py","--manifest","tests/fixtures/air_quality/airnow/layer21/manifests/snapshot_preservation_review_valid_manifest.json","--out-dir",str(tmp_path),"--created-at","2026-01-01T00:00:00Z"],check=False)
 assert p.returncode==0
