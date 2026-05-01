import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[3]
BUILD=ROOT/'tools/publishers/air/build_air_public_read_model.py'
AUD=ROOT/'tools/auditors/air/audit_air_public_read_model.py'
CLIENT=ROOT/'tools/clients/air/query_air_public_read_model.py'
FIX=ROOT/'tests/fixtures/air/public_read_model'

def run(args): return subprocess.run(args,capture_output=True,text=True)

def test_pass_fixture_candidate(tmp_path):
    out=tmp_path/'out'
    r=run(['python',str(BUILD),'--publication-dir',str(FIX/'pass_fixture_candidate'),'--out-dir',str(out),'--allow-fixture-candidate-index'])
    assert r.returncode==0
    assert (out/'public_index.json').exists()
    assert (out/'public_status.json').exists()
    assert list(out.glob('public_api_record.*.json'))
    assert list(out.glob('public_provenance_trace.*.json'))

def test_deny_cases(tmp_path):
    for c in ['deny_raw_path_leak','deny_processed_path_exposure','deny_missing_sha256','deny_nowcast_labelled_validated_truth','deny_missing_publication_manifest']:
        out=tmp_path/c
        r=run(['python',str(BUILD),'--publication-dir',str(FIX/c),'--out-dir',str(out),'--allow-fixture-candidate-index'])
        assert r.returncode!=0
        assert (out/'public_index.blocked.json').exists()

def test_auditor_and_client(tmp_path):
    out=tmp_path/'out'
    run(['python',str(BUILD),'--publication-dir',str(FIX/'pass_fixture_candidate'),'--out-dir',str(out),'--allow-fixture-candidate-index'])
    assert run(['python',str(AUD),str(out)]).returncode==0
    assert run(['python',str(CLIENT),'--index',str(out/'public_index.json'),'--include-candidates']).returncode==0
