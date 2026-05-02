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

def test_valid_manifest(tmp_path):
    p,out=run_manifest('valid',tmp_path); assert p.returncode==0
    assert (out/'closure_archive_index_review_receipt.json').exists()

def test_no_packet_manifest(tmp_path):
    p,out=run_manifest('valid_no_packet',tmp_path); assert p.returncode==0
    assert not (out/'closure_archive_index_review_packet.tar.gz').exists()

def test_missing_layer28_receipt_nonzero(tmp_path):
    p,_=run_manifest('missing_layer28_receipt',tmp_path); assert p.returncode!=0
