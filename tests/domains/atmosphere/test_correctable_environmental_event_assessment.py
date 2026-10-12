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

from tools.validators.domains.atmosphere import validate_correctable_environmental_event_assessment as module

ROOT = Path(__file__).resolve().parents[3]
CASES = ROOT / "fixtures/contracts/v1/domains/atmosphere/correctable_environmental_event_assessment/cases.json"
SCHEMA = ROOT / "schemas/contracts/v1/domains/atmosphere/correctable_environmental_event_assessment.schema.json"
VALIDATOR = ROOT / "tools/validators/domains/atmosphere/validate_correctable_environmental_event_assessment.py"
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
    document["assessment"] = copy.deepcopy(case.get("assessment_override", module.expected_assessment(document)))
    spec_hash, assessment_id = module.canonical_identity(document)
    document["spec_hash"] = case.get("spec_hash_override", spec_hash)
    document["assessment_id"] = case.get("assessment_id_override", assessment_id)
    return document


def _case(case_id: str) -> dict[str, Any]:
    return next(case for case in MANIFEST["cases"] if case["case_id"] == case_id)


def test_schema_is_valid_draft_2020_12() -> None:
    Draft202012Validator.check_schema(json.loads(SCHEMA.read_text(encoding="utf-8")))


def test_fixture_manifest_has_exact_polarity() -> None:
    outcomes = [case["expected_outcome"] for case in MANIFEST["cases"]]
    assert outcomes.count("PASS") == 2
    assert outcomes.count("ABSTAIN") == 2
    assert outcomes.count("ERROR") == 1
    assert outcomes.count("DENY") == 11


def test_all_fixture_cases_match_exactly() -> None:
    for case in MANIFEST["cases"]:
        result = module.validate_payload(materialize(case))
        assert result.outcome == case["expected_outcome"], case["case_id"]
        assert [{"code": item.code, "path": item.path} for item in result.findings] == case["expected_findings"], case["case_id"]


def test_correction_lineage_keeps_distinct_identities() -> None:
    subject = materialize(_case("corrected-pass"))["subject"]
    assert subject["correction_of_event_ref"] == subject["event_ref"]
    assert subject["replacement_event_ref"] != subject["event_ref"]
    assert subject["candidate_ref"] != subject["observation_ref"]
    assert subject["review_disposition_ref"] not in {subject["candidate_ref"], subject["event_ref"]}


def test_candidate_never_inherits_event_outcome() -> None:
    payload = materialize(_case("candidate-only-hold"))
    assert payload["assessment"] == {"outcome": "HOLD", "reason_code": "CANDIDATE_REMAINS_PROVISIONAL"}
    assert payload["subject"]["event_ref"] is None
    assert module.validate_payload(payload).outcome == "ABSTAIN"


def test_source_roles_are_distinct_and_explicit() -> None:
    roles = materialize(_case("corrected-pass"))["subject"]["source_roles"]
    assert [entry["role"] for entry in roles] == ["BASELINE_SOURCE", "CORROBORATION_SOURCE", "OBSERVATION_SOURCE"]
    assert len({entry["source_ref"] for entry in roles}) == 3


def test_identity_is_deterministic() -> None:
    case = _case("corrected-pass")
    assert materialize(case) == materialize(case)


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
        path = Path(directory) / "assessment.json"
        path.write_text(json.dumps(materialize(_case("corrected-pass"))), encoding="utf-8")
        run = subprocess.run([sys.executable, str(VALIDATOR), str(path)], cwd=ROOT, text=True, capture_output=True, check=False)
    assert run.returncode == 0
    output = json.loads(run.stdout)
    assert output["outcome"] == "PASS"
    assert output["authority"] == "NONE"
    assert "synthetic-air-001" not in run.stdout


def test_raw_measurements_and_authority_are_excluded() -> None:
    schema_text = SCHEMA.read_text(encoding="utf-8")
    for forbidden in ("pm25_value", "threshold_value", "aqi_value", "latitude", "longitude"):
        assert forbidden not in schema_text
    governance = materialize(_case("corrected-pass"))["governance"]
    assert all(value is False for key, value in governance.items() if key != "execution_mode")
