import json
from pathlib import Path
import pytest
from tools.consent.revoke_consent import revoke_consent

FIX = Path("tests/fixtures/consent")


def test_revoke_delta_deterministic_and_golden():
    req = json.loads((FIX / "revoke_request.valid.json").read_text())
    got = revoke_consent(req)
    exp = json.loads((FIX / "revoke_delta.golden.json").read_text())
    assert got == exp
    assert revoke_consent(req)["revoke_delta_id"] == got["revoke_delta_id"]


def test_revoke_delta_changes_with_inputs():
    req = json.loads((FIX / "revoke_request.valid.json").read_text())
    a = revoke_consent(req)["revoke_delta_id"]
    req2 = dict(req); req2["revocation_token"] = "different-token"
    b = revoke_consent(req2)["revoke_delta_id"]
    req3 = dict(req); req3["prior_spec_hash"] = "f"*64
    c = revoke_consent(req3)["revoke_delta_id"]
    assert a != b
    assert a != c


def test_revoke_requires_token_or_jwt():
    req = {"consent_vc_id":"x","prior_spec_hash":"a"*64,"delta_timestamp":"2026-05-01T00:00:00Z"}
    with pytest.raises(ValueError):
        revoke_consent(req)
