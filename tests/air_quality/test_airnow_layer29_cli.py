from pathlib import Path
import json
import subprocess

CLI=["python","tools/air_quality/airnow_layer29_closure_archive_index_review.py"]
CREATED="2026-01-01T00:00:00Z"

def run_manifest(name,tmp_path):
    out=tmp_path/name
    m=f"tests/fixtures/air_quality/airnow/layer29/manifests/closure_archive_index_review_{name}_manifest.json"
    p=subprocess.run(CLI+["--manifest",m,"--out-dir",str(out),"--created-at",CREATED],capture_output=True,text=True)
    return p,out

def test_stable_hashes(tmp_path):
    p1,o1=run_manifest('valid',tmp_path); p2,o2=run_manifest('valid',tmp_path)
    assert p1.returncode==0 and p2.returncode==0
    r1=json.loads((o1/'closure_archive_index_review_receipt.json').read_text())
    r2=json.loads((o2/'closure_archive_index_review_receipt.json').read_text())
    assert r1['output_hashes']['closure_archive_index_review_packet_hash']==r2['output_hashes']['closure_archive_index_review_packet_hash']
