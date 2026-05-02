import json, subprocess
from pathlib import Path

def run(man):
    out=Path('/tmp')/('l9_'+Path(man).stem)
    if out.exists(): subprocess.run(['rm','-rf',str(out)],check=True)
    cmd=['python','tools/air_quality/airnow_layer9_manual_evidence.py','--manifest',man,'--out-dir',str(out),'--created-at','2026-01-01T00:00:00Z']
    p=subprocess.run(cmd,capture_output=True,text=True)
    return p,out

def test_smoke():
    p,out=run('tests/fixtures/air_quality/airnow/layer9/manifests/manual_evidence_valid_manifest.json')
    assert p.returncode==0
    r=json.loads((out/'manual_evidence_receipt.json').read_text())
    assert r['workflow_outcome'] in {'MANUAL_EVIDENCE_ACCEPTED_FOR_RERUN','MANUAL_EVIDENCE_NEEDS_MORE_INPUT'}
