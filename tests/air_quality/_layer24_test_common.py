import json
from pathlib import Path
import subprocess

CLI=["python","tools/air_quality/airnow_layer24_preservation_closure_readiness.py"]

def run_manifest(name,tmp_path):
 m=Path("tests/fixtures/air_quality/airnow/layer24/manifests")/name
 out=tmp_path/name.replace('.json','')
 cp=subprocess.run(CLI+["--manifest",str(m),"--out-dir",str(out),"--created-at","2026-01-01T00:00:00Z"],capture_output=True,text=True)
 return cp,out
