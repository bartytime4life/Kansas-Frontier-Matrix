import json,subprocess
from pathlib import Path
CMD=["python","tools/governance/plan_promotion_rollback.py"]

def test_deterministic_plan_id(tmp_path):
    idx={"records":[{"release_id":"rel-2026-02","public_path":"data/published/ecology/dry-run/layer_manifest.json","decision_log_ref":"data/receipts/decisions/d.json","run_receipt_ref":"data/receipts/air/run_receipt.example.json","spec_hash":"a"*64}]}
    ip=tmp_path/'idx.json'; ip.write_text(json.dumps(idx))
    req={"target_release_id":"rel-2026-02","requested_at":"2026-04-03T00:00:00Z","requested_by":"steward-1","source_promotion_registry_ref":"tests/fixtures/governance/promotion/valid/full_registry.json","receipt_index_path":str(ip)}
    rp=tmp_path/'req.json'; rp.write_text(json.dumps(req))
    a=json.loads(subprocess.run(CMD+[str(rp)],capture_output=True,text=True,check=True).stdout)
    b=json.loads(subprocess.run(CMD+[str(rp)],capture_output=True,text=True,check=True).stdout)
    assert a['rollback_plan_id']==b['rollback_plan_id']

def test_denies_candidate_target(tmp_path):
    idx={"records":[{"release_id":"rel-2026-02","public_path":"data/work/candidate/x.json","decision_log_ref":"d","run_receipt_ref":"r","spec_hash":"a"*64}]}
    ip=tmp_path/'idx.json'; ip.write_text(json.dumps(idx)); req={"target_release_id":"rel-2026-02","requested_at":"2026-04-03T00:00:00Z","requested_by":"steward-1","source_promotion_registry_ref":"x","receipt_index_path":str(ip)}
    rp=tmp_path/'req.json'; rp.write_text(json.dumps(req))
    assert subprocess.run(CMD+[str(rp)],capture_output=True,text=True).returncode!=0
