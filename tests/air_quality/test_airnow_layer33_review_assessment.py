import json, subprocess
from pathlib import Path
CLI=["python","tools/air_quality/airnow_layer33_closure_archive_index_preservation_review.py"]
FIX=Path("tests/fixtures/air_quality/airnow/layer33/manifests")

def run_manifest(name,tmp_path):
 out=tmp_path/name
 cp=subprocess.run(CLI+["--manifest",str(FIX/name),"--out-dir",str(out),"--created-at","2026-01-01T00:00:00Z"],capture_output=True,text=True)
 return cp,out

def test_smoke(tmp_path):
 cp,out=run_manifest("closure_archive_index_preservation_review_valid_manifest.json",tmp_path)
 assert cp.returncode==0
 assert (out/"closure_archive_index_preservation_review_receipt.json").exists()
