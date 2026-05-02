import json, subprocess, tempfile
from pathlib import Path

MANIFEST='tests/fixtures/air_quality/airnow/layer6/manifests/bundle_valid_manifest.json'

def run_cmd(manifest=MANIFEST):
    td=tempfile.mkdtemp(prefix='l6_')
    cp=subprocess.run(['python','tools/air_quality/airnow_layer6_bundle.py','--manifest',manifest,'--out-dir',td,'--created-at','2026-01-01T00:00:00Z'],capture_output=True,text=True)
    return cp, Path(td)

def test_runs():
    cp,td=run_cmd(); assert cp.returncode==0
    assert (td/'bundle_receipt.json').exists()
