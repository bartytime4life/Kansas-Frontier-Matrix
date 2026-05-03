import json, subprocess
from pathlib import Path
CLI=["python","tools/air_quality/airnow_layer33_closure_archive_index_preservation_review.py"]
FIX=Path("tests/fixtures/air_quality/airnow/layer33/manifests")

def run_manifest(name,tmp_path):
 out=tmp_path/name
 cp=subprocess.run(CLI+["--manifest",str(FIX/name),"--out-dir",str(out),"--created-at","2026-01-01T00:00:00Z"],capture_output=True,text=True)
 return cp,out

def test_governance_manifests_denied(tmp_path):
 names=["closure_archive_index_preservation_review_publication_request_manifest.json","closure_archive_index_preservation_review_command_execution_manifest.json","closure_archive_index_preservation_review_database_write_manifest.json","closure_archive_index_preservation_review_search_api_manifest.json","closure_archive_index_preservation_review_public_catalog_manifest.json"]
 for n in names:
  cp,_=run_manifest(n,tmp_path)
  assert cp.returncode!=0
