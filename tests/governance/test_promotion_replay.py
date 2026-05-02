import json,subprocess,tempfile
from pathlib import Path

CMD=["python","tools/governance/replay_promotion.py"]

def replay(req): return subprocess.run(CMD+[str(req)],capture_output=True,text=True)

def test_replay_verified_for_valid_registry():
    r=replay('tests/fixtures/governance/promotion/valid/replay_request_minimal.json')
    assert json.loads(r.stdout)['outcome']=='VERIFIED'

def test_replay_deny_for_deny_decision(tmp_path):
    req={"schema_version":"PromotionReplayRequest.v1","registry_path":"tests/fixtures/governance/promotion/invalid/deny_decision.json","receipt_index_path":"tests/fixtures/governance/promotion/valid/receipt_index.json"}
    p=tmp_path/'req.json'; p.write_text(json.dumps(req))
    r=replay(p); assert json.loads(r.stdout)['outcome']=='DENY'

def test_replay_abstain_for_incomplete_evidence(tmp_path):
    req={"schema_version":"PromotionReplayRequest.v1","registry_path":"tests/fixtures/governance/promotion/invalid/missing_steward_attestation.json","receipt_index_path":"tests/fixtures/governance/promotion/valid/receipt_index.json"}
    p=tmp_path/'req.json'; p.write_text(json.dumps(req))
    r=replay(p); assert json.loads(r.stdout)['outcome']=='ABSTAIN'

def test_replay_error_for_malformed_or_unreadable(tmp_path):
    bad=tmp_path/'bad.json'; bad.write_text('{bad')
    r=replay(bad); assert json.loads(r.stdout)['outcome']=='ERROR'
