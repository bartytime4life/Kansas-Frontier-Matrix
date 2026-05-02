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

def test_denials(tmp_path):
    for name in ['network','publication_request','command_execution','database_write','search_api','public_catalog','task_closure','governance_closure','audit_closure','copy','transfer','export','publish','file_deletion','destruction','chmod','legal_hold_creation','archive_certification','legal_advice','auto_apply','github_action','secret_field','coordinate_leak']:
        p,_=run_manifest(name,tmp_path)
        assert p.returncode!=0
