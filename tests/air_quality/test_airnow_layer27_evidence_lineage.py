from kfm.air_quality.airnow.preservation_closure_audit.run_preservation_closure_audit import run_preservation_closure_audit
from pathlib import Path

def test_smoke(tmp_path):
    r=run_preservation_closure_audit('tests/fixtures/air_quality/airnow/layer27/manifests/preservation_closure_audit_valid_manifest.json',str(tmp_path),'2026-01-01T00:00:00Z')
    assert r['public_release_allowed'] is False
    assert r['commands_executed'] is False
    assert (tmp_path/'preservation_closure_audit_receipt.json').exists()
