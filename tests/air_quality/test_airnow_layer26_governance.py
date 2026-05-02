from pathlib import Path
import json
from kfm.air_quality.airnow.preservation_closure_finalization.run_preservation_closure_finalization import run_preservation_closure_finalization
FIX=Path('tests/fixtures/air_quality/airnow/layer26/manifests')
L25=Path('tests/fixtures/air_quality/airnow/layer26/input/layer25/preservation_closure_review_policy_attestation.json')

def test_denied_manifests(tmp_path):
    for n in ['network','publication_request','command_execution','execution','copy','transfer','export','publish','file_deletion','destruction','chmod','legal_hold_creation','archive_certification','legal_advice','auto_apply','task_closure','github_action','secret_field']:
        r=run_preservation_closure_finalization(str(FIX/f'preservation_closure_finalization_{n}_manifest.json'),str(tmp_path/n),'2026-01-01T00:00:00Z'); assert r['finite_outcome']=='DENY'
    orig=L25.read_text()
    try:
        L25.write_text('{"note":"12.345,-99.111"}')
        r=run_preservation_closure_finalization(str(FIX/'preservation_closure_finalization_coordinate_leak_manifest.json'),str(tmp_path/'coord'),'2026-01-01T00:00:00Z'); assert r['finite_outcome']=='DENY'
    finally:
        L25.write_text(orig)

def test_no_subprocess_or_network_imports():
    src=Path('kfm/air_quality/airnow/preservation_closure_finalization/run_preservation_closure_finalization.py').read_text();assert 'os.system' not in src and 'requests' not in src and 'subprocess' not in src
