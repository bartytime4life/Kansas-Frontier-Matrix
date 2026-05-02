import json, tempfile, subprocess
from pathlib import Path

def test_evidence_contains_required_checks():
    td=tempfile.mkdtemp(prefix='l7_')
    subprocess.run(['python','tools/air_quality/airnow_layer7_release_gate.py','--manifest','tests/fixtures/air_quality/airnow/layer7/manifests/gate_valid_internal_review_manifest.json','--out-dir',td,'--created-at','2026-01-01T00:00:00Z'],check=True)
    em=json.loads((Path(td)/'release_gate_evidence_matrix.json').read_text())
    checks={r['gate_check'] for r in em['records']}
    assert 'BUNDLE_RECEIPT_PASS' in checks
    assert 'DISCLAIMER_AUDIT_PASS' in checks
