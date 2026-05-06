import json
from pathlib import Path
from tools.consent.issue_consent import issue_consent

FIX = Path("tests/fixtures/consent")


def test_issue_consent_golden():
    req = json.loads((FIX / "issue_request.valid.json").read_text())
    got = issue_consent(req)
    exp = json.loads((FIX / "issue_response.golden.json").read_text())
    assert got == exp
    assert "revocation_token" not in json.dumps(got)
