from __future__ import annotations

import importlib.util
import json
import socket
import subprocess
import sys
import tempfile
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = ROOT / "tools/validators/validate_catalog_matrix_claim_closure.py"
SCHEMA = ROOT / "schemas/contracts/v1/data/catalog_matrix_claim_closure_profile.schema.json"
FIXTURES = ROOT / "fixtures/data/catalog_matrix/claim_closure"
MANIFEST = FIXTURES / "expected_findings_manifest.json"

sys.path.insert(0, str(ROOT))
from tools.validators._common.local_resolver import build_registry

SPEC = importlib.util.spec_from_file_location(
    "validate_catalog_matrix_claim_closure", VALIDATOR
)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def cases() -> list[dict[str, object]]:
    return json.loads(MANIFEST.read_text(encoding="utf-8"))["cases"]


def test_schema_is_closed_and_composes_existing_authorities_offline() -> None:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    assert schema["additionalProperties"] is False
    assert schema["properties"]["claim_envelope"]["$ref"].endswith(
        "/evidence/claim_envelope.schema.json"
    )
    assert schema["properties"]["catalog_matrix_closure"]["$ref"].endswith(
        "/data/catalog_matrix_closure_profile.schema.json"
    )
    assert (
        schema["x-kfm"]["validator"]
        == "tools/validators/validate_catalog_matrix_claim_closure.py"
    )
    validator = Draft202012Validator(
        schema,
        registry=build_registry(ROOT),
        format_checker=FormatChecker(),
    )
    assert not list(
        validator.iter_errors(
            json.loads((FIXTURES / "valid/valid_ready_published.json").read_text())
        )
    )


def test_manifest_has_exact_polarity() -> None:
    assert len(cases()) == 16
    assert {case["case_kind"] for case in cases()} == {
        "VALID",
        "SCHEMA_NEGATIVE",
        "SEMANTIC_NEGATIVE",
    }


def test_exact_manifest_results() -> None:
    for case in cases():
        result = MODULE.validate(FIXTURES / case["path"])
        assert result.outcome == case["expected_outcome"], case["case_id"]
        assert sorted({finding.code for finding in result.findings}) == sorted(
            case["expected_findings"]
        ), case["case_id"]


def test_schema_and_semantic_negative_separation() -> None:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    validator = Draft202012Validator(
        schema,
        registry=build_registry(ROOT),
        format_checker=FormatChecker(),
    )
    for case in cases():
        value = json.loads((FIXTURES / case["path"]).read_text(encoding="utf-8"))
        errors = list(validator.iter_errors(value))
        if case["case_kind"] == "SCHEMA_NEGATIVE":
            assert errors, case["case_id"]
        elif case["case_kind"] == "SEMANTIC_NEGATIVE":
            assert not errors, case["case_id"]


def test_valid_packets_remain_valid_under_both_existing_validators() -> None:
    for case in cases():
        if case["case_kind"] != "VALID":
            continue
        value = json.loads((FIXTURES / case["path"]).read_text(encoding="utf-8"))
        assert MODULE.CLAIM_VALIDATOR.validate_value(value["claim_envelope"]).ok
        assert MODULE.CATALOG_VALIDATOR.validate_value(
            value["catalog_matrix_closure"]
        ).ok


def test_no_network_deterministic_replay_and_cli() -> None:
    with mock.patch.object(
        socket, "create_connection", side_effect=AssertionError("network")
    ), mock.patch.object(socket, "socket", side_effect=AssertionError("network")):
        first = [MODULE.validate(FIXTURES / case["path"]) for case in cases()]
        second = [MODULE.validate(FIXTURES / case["path"]) for case in cases()]
    assert first == second
    run = subprocess.run(
        [sys.executable, str(VALIDATOR), "--fixtures"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert run.returncode == 0, run.stdout + run.stderr
    assert "CATALOG_MATRIX_CLAIM_CLOSURE_FIXTURES_VALID cases=16" in run.stdout


def test_duplicate_nonfinite_and_symlink_fail_closed() -> None:
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        duplicate = root / "duplicate.json"
        nonfinite = root / "nonfinite.json"
        duplicate.write_text('{"id":"a","id":"b"}', encoding="utf-8")
        nonfinite.write_text('{"value":NaN}', encoding="utf-8")
        assert {finding.code for finding in MODULE.validate(duplicate).findings} == {
            "JSON_DUPLICATE_KEY"
        }
        assert {finding.code for finding in MODULE.validate(nonfinite).findings} == {
            "JSON_NONFINITE_NUMBER"
        }
        target = root / "target.json"
        link = root / "link.json"
        target.write_text("{}", encoding="utf-8")
        try:
            link.symlink_to(target)
        except (OSError, NotImplementedError):
            return
        assert {finding.code for finding in MODULE.validate(link).findings} == {
            "INPUT_SYMLINK_DENIED"
        }


def test_overstatement_findings_do_not_echo_references() -> None:
    path = FIXTURES / "semantic_invalid/semantic_evidence_overstatement.json"
    result = MODULE.validate(path)
    rendered = json.dumps([finding.__dict__ for finding in result.findings])
    assert "CATALOG_EVIDENCE_REFS_OVERSTATE_CLAIM" in rendered
    assert "hydrology:999" not in rendered


def test_cli_exit_codes_are_finite() -> None:
    for path, expected in [
        (FIXTURES / "valid/valid_ready_published.json", 0),
        (FIXTURES / "semantic_invalid/semantic_publication_overstatement.json", 1),
        (ROOT / "missing.json", 2),
    ]:
        run = subprocess.run(
            [sys.executable, str(VALIDATOR), str(path)],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        assert run.returncode == expected, run.stdout + run.stderr
