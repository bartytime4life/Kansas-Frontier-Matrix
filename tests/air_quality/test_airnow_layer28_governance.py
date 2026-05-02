
from pathlib import Path
import json, subprocess, sys
CLI=[sys.executable,'tools/air_quality/airnow_layer28_closure_archive_index.py']
MAN='tests/fixtures/air_quality/airnow/layer28/manifests'

def run(name,tmp_path):
 out=tmp_path/name
 m=f"{MAN}/{name}.json"
 p=subprocess.run(CLI+['--manifest',m,'--out-dir',str(out),'--created-at','2026-01-01T00:00:00Z'],capture_output=True,text=True)
 return p,out


def test_smoke(tmp_path):
 p,out=run('closure_archive_index_valid_manifest',tmp_path)
 assert p.returncode==0
 assert (out/'closure_archive_index_receipt.json').exists()

def test_denied(tmp_path):
 p,_=run('closure_archive_index_network_manifest',tmp_path)
 assert p.returncode!=0
