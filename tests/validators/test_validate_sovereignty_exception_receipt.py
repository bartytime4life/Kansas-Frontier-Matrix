from __future__ import annotations

import copy
import json
import socket
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

from tools.validators.policy import validate_sovereignty_exception_receipt as module

ROOT = Path(__file__).resolve().parents[2]
CASES = ROOT / "fixtures/contracts/v1/policy/sovereignty_exception_receipt/cases.json"
SCHEMA = ROOT / "schemas/contracts/v1/policy/sovereignty_exception_receipt.schema.json"
VALIDATOR = ROOT / "tools/validators/policy/validate_sovereignty_exception_receipt.py"
MANIFEST = json.loads(CASES.read_text(encoding="utf-8"))


def _replace(document: dict[str, Any], pointer: str, value: Any) -> None:
    target: Any = document
    parts = [part.replace("~1", "/").replace("~0", "~") for part in pointer[1:].split("/")]
    for part in parts[:-1]:
        target = target[int(part)] if isinstance(target, list) else target[part]
    final = parts[-1]
    if isinstance(target, list):
        target[int(final)] = copy.deepcopy(value)
    else:
        target[final] = copy.deepcopy(value)


def materialize(case: dict[str, Any]) -> dict[str, Any]:
    document = copy.deepcopy(MANIFEST["bases"][case["base"]])
    for mutation in case.get("mutations", []):
        _replace(document, mutation["path"], mutation["value"])
    spec_hash, receipt_id = module.canonical_identity(document)
    document["spec_hash"] = case.get("spec_hash_override", spec_hash)
    document["receipt_id"] = case.get("receipt_id_override", receipt_id)
    return document


def test_schema_is_valid_draft_2020_12() -> None:
    Draft202012Validator.check_schema(json.loads(SCHEMA.read_text(encoding="utf-8")))


def test_fixture_manifest_has_exact_polarity() -> None:
    outcomes = [case["expected_outcome"] for case in MANIFEST["cases"]]
    assert outcomes.count("PASS") == 3
    assert outcomes.count("ABSTAIN") == 1
    assert outcomes.count("DENY") == 8


def test_all_fixture_cases_match_exactly() -> None:
    for case in MANIFEST["cases"]:
        result = module.validate_payload(materialize(case))
        assert result.outcome == case["expected_outcome"], case["case_id"]
        assert [{"code": item.code, "path": item.path} for item in result.findings] == case["expected_findings"], case["case_id"]


def test_identity_is_deterministic() -> None:
    assert materialize(MANIFEST["cases"][0]) == materialize(MANIFEST["cases"][0])


def test_approved_record_is_not_authority() -> None:
    payload = materialize(MANIFEST["cases"][0])
    assert payload["decision"]["disposition"] == "RECORDED_APPROVED"
    assert all(value is False for key, value in payload["governance"].items() if key != "execution_mode")


def test_validation_is_no_network() -> None:
    original = socket.socket
    socket.socket = lambda *_a, **_k: (_ for _ in ()).throw(AssertionError("network denied"))
    try:
        for case in MANIFEST["cases"]:
            module.validate_payload(materialize(case))
    finally:
        socket.socket = original


def test_cli_is_finite_and_value_minimized() -> None:
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "receipt.json"
        path.write_text(json.dumps(materialize(MANIFEST["cases"][0])), encoding="utf-8")
        run = subprocess.run([sys.executable, str(VALIDATOR), str(path)], cwd=ROOT, text=True, capture_output=True, check=False)
    assert run.returncode == 0
    output = json.loads(run.stdout)
    assert output["outcome"] == "PASS"
    assert output["authority"] == "NONE"
    assert "synthetic-sovereignty-subject-001" not in run.stdout


def test_external_authority_families_remain_distinct() -> None:
    payload = materialize(MANIFEST["cases"][0])
    refs = {
        payload["receipt_id"],
        payload["decision"]["policy_decision_ref"],
        payload["decision"]["approver_roster_ref"],
        payload["provenance"]["activity_ref"],
        *payload["decision"]["review_record_refs"],
    }
    assert len(refs) == 6
