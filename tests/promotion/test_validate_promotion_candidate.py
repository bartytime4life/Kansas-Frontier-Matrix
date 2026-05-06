import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = ROOT / "tools/validators/promotion/validate_promotion_candidate.py"


def _run(path: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(["python", str(VALIDATOR), str(path)], capture_output=True, text=True)


def test_valid_candidate_approved():
    fixture = ROOT / "tests/fixtures/promotion/valid/promotion_candidate.json"
    result = _run(fixture)
    assert result.returncode == 0
    payload = json.loads(result.stdout)
    assert payload["object_type"] == "PromotionDecision"
    assert payload["decision"] == "APPROVE"
    assert payload["reasons"] == []


def test_invalid_missing_receipt_denied():
    fixture = ROOT / "tests/fixtures/promotion/invalid/missing_receipt.json"
    result = _run(fixture)
    assert result.returncode == 1
    payload = json.loads(result.stdout)
    assert payload["decision"] == "DENY"
    assert "missing_run_receipt_ref" in payload["reasons"]
    assert "missing_run_receipt_bundle_ref" in payload["reasons"]


def test_invalid_restricted_public_geometry_denied():
    fixture = ROOT / "tests/fixtures/promotion/invalid/restricted_public_geometry.json"
    result = _run(fixture)
    assert result.returncode == 1
    payload = json.loads(result.stdout)
    assert payload["decision"] == "DENY"
    assert "restricted_sensitivity_cannot_be_public" in payload["reasons"]
    assert "public_release_blocked_from_private_lifecycle_state" in payload["reasons"]
