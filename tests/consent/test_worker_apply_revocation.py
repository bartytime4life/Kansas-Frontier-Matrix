import json
from pathlib import Path
from tools.consent.worker_apply_revocation import apply_revocation


def test_worker_emits_suppress_or_recompute_receipt_and_no_token_leak():
    run = json.loads(Path("tests/fixtures/consent/run_receipt.with_consent.valid.json").read_text())
    delta = json.loads(Path("tests/fixtures/consent/revoke_delta.golden.json").read_text())
    out = apply_revocation(run, delta)
    assert out["action"] == "suppress_or_recompute"
    assert out["revoke_delta_id"] == delta["revoke_delta_id"]
    assert "revocation_token" not in json.dumps(out)
