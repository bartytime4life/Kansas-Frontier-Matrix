from __future__ import annotations

import json
from pathlib import Path

import pytest

from tools.validators import validate_ai_receipt as validator

ROOT = Path(__file__).resolve().parents[2]
VALID = ROOT / "fixtures/contracts/v1/runtime/ai_receipt/valid/valid_1.json"
REGISTRY = ROOT / "tools/validators/validator_registry.json"


def _candidate() -> dict[str, object]:
    return json.loads(VALID.read_text(encoding="utf-8"))


def _write(path: Path, candidate: dict[str, object]) -> Path:
    path.write_text(json.dumps(candidate, sort_keys=True), encoding="utf-8")
    return path


def _codes(result: validator.ValidationResult) -> set[str]:
    return {finding.code for finding in result.findings}


def test_fixture_profile_preserves_polarity(capsys: pytest.CaptureFixture[str]) -> None:
    assert validator.run_fixture_profile() == 0
    output = capsys.readouterr().out
    assert '"outcome":"PASS"' in output
    assert '"outcome":"FAIL"' in output
    assert "policy_decision_ref" not in output


def test_zero_digest_placeholder_fails(tmp_path: Path) -> None:
    candidate = _candidate()
    candidate["inputs_digest"] = "sha256:" + ("0" * 64)
    result = validator.validate_ai_receipt(_write(tmp_path / "candidate.json", candidate))
    assert result.outcome == "FAIL"
    assert "DIGEST_PLACEHOLDER" in _codes(result)


def test_blank_reference_fails(tmp_path: Path) -> None:
    candidate = _candidate()
    candidate["citation_validation_ref"] = "   "
    result = validator.validate_ai_receipt(_write(tmp_path / "candidate.json", candidate))
    assert result.outcome == "FAIL"
    assert "FIELD_EMPTY" in _codes(result)


def test_duplicate_key_fails_without_echoing_value(tmp_path: Path) -> None:
    path = tmp_path / "duplicate.json"
    path.write_text('{"id":"ai1","id":"secret-value"}', encoding="utf-8")
    result = validator.validate_ai_receipt(path)
    assert result.outcome == "ERROR"
    assert _codes(result) == {"JSON_DUPLICATE_KEY"}
    serialized = validator.serialize_result(path, result)
    assert "secret-value" not in serialized


def test_nonfinite_number_fails_before_schema(tmp_path: Path) -> None:
    path = tmp_path / "nonfinite.json"
    path.write_text('{"value":NaN}', encoding="utf-8")
    result = validator.validate_ai_receipt(path)
    assert result.outcome == "ERROR"
    assert _codes(result) == {"JSON_NONFINITE_NUMBER"}


def test_symlink_input_is_denied(tmp_path: Path) -> None:
    target = _write(tmp_path / "target.json", _candidate())
    link = tmp_path / "link.json"
    try:
        link.symlink_to(target)
    except (OSError, NotImplementedError):
        pytest.skip("symlinks are unavailable on this platform")
    result = validator.validate_ai_receipt(link)
    assert result.outcome == "ERROR"
    assert _codes(result) == {"INPUT_SYMLINK_DENIED"}


def test_registry_wires_ai_receipt_into_focused_and_full_profiles() -> None:
    registry = json.loads(REGISTRY.read_text(encoding="utf-8"))
    entry = next(item for item in registry["validators"] if item["id"] == "ai-receipt")
    assert entry["script"] == "tools/validators/validate_ai_receipt.py"
    assert entry["args"] == ["--fixtures"]
    assert "ai-receipt" in registry["profiles"]["focused"]
    assert "ai-receipt" in registry["profiles"]["full"]
    assert "ai-receipt" not in registry["profiles"]["release-dry-run"]
