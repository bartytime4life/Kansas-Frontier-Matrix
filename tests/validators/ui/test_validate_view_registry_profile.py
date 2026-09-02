from __future__ import annotations

import copy
import importlib.util
import json
import socket
import subprocess
import sys
from pathlib import Path

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = ROOT / "tools/validators/ui/validate_view_registry_profile.py"
SCHEMA_PATH = ROOT / "schemas/contracts/v1/ui/view_registry_profile.schema.json"
CASES_PATH = ROOT / "fixtures/ui/view_registry_profile/cases.json"

SPEC = importlib.util.spec_from_file_location("view_registry_validator", VALIDATOR_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)

MANIFEST = json.loads(CASES_PATH.read_text(encoding="utf-8"))


def _set_pointer(value: dict[str, object], pointer: str, replacement: object) -> None:
    parts = [part.replace("~1", "/").replace("~0", "~") for part in pointer.split("/")[1:]]
    target: object = value
    for part in parts[:-1]:
        target = target[int(part)] if isinstance(target, list) else target[part]  # type: ignore[index]
    if isinstance(target, list):
        target[int(parts[-1])] = replacement
    else:
        target[parts[-1]] = replacement  # type: ignore[index]


def materialize(case: dict[str, object]) -> dict[str, object]:
    value = copy.deepcopy(MANIFEST["bases"][case["base"]])
    for mutation in case.get("mutations", []):
        _set_pointer(value, mutation["path"], mutation["value"])
    spec_hash, registry_id = MODULE.canonical_identity(value)
    value["spec_hash"] = case.get("spec_hash_override", spec_hash)
    value["registry_id"] = case.get("registry_id_override", registry_id)
    return value


def _findings(result: object) -> list[dict[str, str]]:
    return [{"code": item.code, "path": item.path} for item in result.findings]


def test_schema_is_valid_draft_2020_12() -> None:
    Draft202012Validator.check_schema(json.loads(SCHEMA_PATH.read_text(encoding="utf-8")))


def test_fixture_manifest_has_exact_polarity() -> None:
    for case in MANIFEST["cases"]:
        result = MODULE.validate_payload(materialize(case))
        assert result.outcome == case["expected_outcome"], case["case_id"]
        assert _findings(result) == case["expected_findings"], case["case_id"]


def test_finite_outcome_coverage() -> None:
    outcomes = {MODULE.validate_payload(materialize(case)).outcome for case in MANIFEST["cases"]}
    assert outcomes == {"PASS", "ABSTAIN", "DENY"}


def test_identity_is_deterministic() -> None:
    candidate = materialize(MANIFEST["cases"][0])
    assert MODULE.canonical_identity(candidate) == MODULE.canonical_identity(copy.deepcopy(candidate))


def test_valid_candidate_remains_inactive_and_non_authoritative() -> None:
    candidate = materialize(MANIFEST["cases"][0])
    assert candidate["governance"] == {
        "execution_mode": "FIXTURE_ONLY",
        "network_attempted": False,
        "registry_activated": False,
        "policy_evaluated": False,
        "review_approved": False,
        "release_authorized": False,
        "deployment_authorized": False,
        "publication_authorized": False,
    }
    assert all(entry["activation_state"] == "PROPOSED_INACTIVE" for entry in candidate["entries"])
    assert all(not any(entry["authority"].values()) for entry in candidate["entries"])


def test_validation_is_no_network() -> None:
    original = socket.socket
    socket.socket = lambda *_a, **_k: (_ for _ in ()).throw(AssertionError("network denied"))  # type: ignore[assignment]
    try:
        assert MODULE.validate_payload(materialize(MANIFEST["cases"][0])).outcome == "PASS"
    finally:
        socket.socket = original


def test_malformed_input_is_bounded_error(tmp_path: Path) -> None:
    candidate = tmp_path / "malformed.json"
    candidate.write_text('{"secret":"do-not-echo"', encoding="utf-8")
    result = MODULE.validate_file(candidate)
    assert result.outcome == "ERROR"
    assert _findings(result) == [{"code": "VIEW_REGISTRY_JSON_INVALID", "path": "/"}]


def test_cli_emits_machine_safe_summary(tmp_path: Path) -> None:
    candidate = tmp_path / "candidate.json"
    candidate.write_text(json.dumps(materialize(MANIFEST["cases"][0])), encoding="utf-8")
    run = subprocess.run(
        [sys.executable, str(VALIDATOR_PATH), str(candidate)],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
        timeout=10,
    )
    summary = json.loads(run.stdout)
    assert run.returncode == 0
    assert summary["outcome"] == "PASS"
    assert summary["authority"] == "NONE"
    assert "kfm:view:hydrology.streamflow" not in run.stdout
