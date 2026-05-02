import json, subprocess

def run(man,out):
    return subprocess.run(['python','tools/air_quality/airnow_layer10_replay_plan.py','--manifest',man,'--out-dir',str(out),'--created-at','2026-01-01T00:00:00Z'],capture_output=True,text=True)

def test_valid(tmp_path):
    r=run('tests/fixtures/air_quality/airnow/layer10/manifests/replay_valid_manifest.json',tmp_path/'o')
    assert r.returncode==0
    assert json.loads(r.stdout)['workflow_outcome']=='REPLAY_PLAN_READY'

def test_publication_denied(tmp_path):
    r=run('tests/fixtures/air_quality/airnow/layer10/manifests/replay_publication_request_manifest.json',tmp_path/'o2')
    assert r.returncode!=0
    assert json.loads(r.stdout)['finite_outcome']=='DENY'
