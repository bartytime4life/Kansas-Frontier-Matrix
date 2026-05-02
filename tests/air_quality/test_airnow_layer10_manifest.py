import json
from kfm.air_quality.airnow.replay import run_replay_planner

def test_manifest_outputs(tmp_path):
    rec=run_replay_planner('tests/fixtures/air_quality/airnow/layer10/manifests/replay_valid_manifest.json',tmp_path,'2026-01-01T00:00:00Z')
    assert rec['workflow_outcome']=='REPLAY_PLAN_READY'
    assert (tmp_path/'replay_orchestration_manifest.resolved.json').exists()
    assert (tmp_path/'replay_receipt.json').exists()
