import subprocess, json
from pathlib import Path
CLI=["python","tools/air_quality/airnow_layer25_preservation_closure_review.py"]
FIX=Path("tests/fixtures/air_quality/airnow/layer25/manifests")
def run_manifest(name,tmp_path):
 out=tmp_path/name.replace('.json','')
 cp=subprocess.run(CLI+["--manifest",str(FIX/name),"--out-dir",str(out),"--created-at","2026-01-01T00:00:00Z"],capture_output=True,text=True)
 return cp,out
