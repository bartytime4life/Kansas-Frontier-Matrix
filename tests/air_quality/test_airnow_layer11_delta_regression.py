import json, subprocess

MAN='tests/fixtures/air_quality/airnow/layer11/manifests/replay_results_valid_manifest.json'

def run(man,tmp_path):
    return subprocess.run(['python','tools/air_quality/airnow_layer11_replay_results.py','--manifest',man,'--out-dir',str(tmp_path),'--created-at','2026-01-01T00:00:00Z'],capture_output=True,text=True)

def test_layer11_smoke(tmp_path):
    r=run(MAN,tmp_path/'o')
    assert r.returncode==0
    obj=json.loads(r.stdout)
    assert obj['workflow_runner']=='airnow_layer11_replay_results'

def test_layer11_denied(tmp_path):
    r=run('tests/fixtures/air_quality/airnow/layer11/manifests/replay_results_publication_request_manifest.json',tmp_path/'o2')
    assert r.returncode!=0
