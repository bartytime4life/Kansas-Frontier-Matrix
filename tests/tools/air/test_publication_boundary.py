import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
PUB=ROOT/'tools/publishers/air/publish_air_release.py'
AUD=ROOT/'tools/auditors/air/audit_air_public_boundary.py'
FIX=ROOT/'tests/fixtures/air/publication_boundary'

def run(args):
    return subprocess.run(args,capture_output=True,text=True)

def test_pass_fixture_candidate(tmp_path):
    out=tmp_path/'out'
    r=run(['python',str(PUB),'--release-candidate-dir',str(FIX/'pass_fixture_candidate'),'--out-dir',str(out),'--allow-fixture-publication-candidate','--requested-status','publication_candidate'])
    assert r.returncode==0
    assert (out/'data/catalog/air/publication_candidate/example/publication_manifest.json').exists()

def test_deny_cases(tmp_path):
    for name in ['deny_missing_attestation','deny_pending_aqs_reconciliation','deny_old_aqs_reconciliation','deny_raw_path_reference','deny_fixture_real_publish']:
        out=tmp_path/name
        r=run(['python',str(PUB),'--release-candidate-dir',str(FIX/name),'--out-dir',str(out)])
        assert r.returncode!=0
        assert (out/'publication_manifest.json').exists()
    # schema-invalid evidence also fails closed
    bad=run(['python',str(PUB),'--release-candidate-dir',str(FIX/'deny_nowcast_labelled_validated_truth'),'--out-dir',str(tmp_path/'bad')])
    assert bad.returncode!=0

def test_auditor_detects_violation(tmp_path):
    out=tmp_path/'out'
    run(['python',str(PUB),'--release-candidate-dir',str(FIX/'pass_fixture_candidate'),'--out-dir',str(out),'--allow-fixture-publication-candidate','--requested-status','publication_candidate'])
    good=out/'data/catalog/air/publication_candidate/example'
    assert run(['python',str(AUD),str(good)]).returncode==0
    assert run(['python',str(AUD),str(FIX/'deny_raw_path_reference')]).returncode!=0
