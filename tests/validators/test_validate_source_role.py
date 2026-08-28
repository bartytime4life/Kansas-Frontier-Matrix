from __future__ import annotations

import copy
import json
import os
import socket
import subprocess
import sys
import tempfile
from pathlib import Path
from unittest import mock

import pytest
from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[2]
HASHING_SRC = REPO_ROOT / "packages/hashing/src"
for path in (REPO_ROOT, HASHING_SRC):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))

from tools.validators.source_role.source_role_core import (  # noqa: E402
    BASE_PATH,
    CASES_PATH,
    DESCRIPTOR_SCHEMA_PATH,
    REQUEST_SCHEMA_PATH,
    descriptor_validator,
    expected_request_id,
    load_json,
    request_validator,
)
from tools.validators.source_role.source_role_rules import evaluate_document, evaluate_path  # noqa: E402
from tools.validators.source_role.validate_source_role import load_fixture_cases, run_fixture_suite  # noqa: E402


def test_schemas_self_check() -> None:
    Draft202012Validator.check_schema(json.loads(REQUEST_SCHEMA_PATH.read_text(encoding="utf-8")))
    Draft202012Validator.check_schema(json.loads(DESCRIPTOR_SCHEMA_PATH.read_text(encoding="utf-8")))


def test_base_validates_against_both_schemas() -> None:
    packet = load_json(BASE_PATH)
    assert list(request_validator().iter_errors(packet)) == []
    assert list(descriptor_validator().iter_errors(packet["descriptor"])) == []
    assert packet["use"]["request_id"] == expected_request_id(packet)


def test_fixture_suite_has_exact_polarity() -> None:
    ok, payload = run_fixture_suite()
    assert ok, payload
    assert payload == {
        "profile": "kfm.source-role-use.fixtures.v1",
        "outcome": "PASS",
        "cases": 14,
        "mismatches": [],
        "authority_created": False,
    }


@pytest.mark.parametrize(
    ("name", "outcome"),
    [
        ("pass_public_map", "PASS"),
        ("restrict_steward_sensitive", "RESTRICT"),
        ("abstain_context_only", "ABSTAIN"),
        ("hold_role_change_with_lineage", "HOLD"),
        ("deny_ai_inferred", "DENY"),
        ("error_request_id_drift", "ERROR"),
    ],
)
def test_representative_outcomes(name: str, outcome: str) -> None:
    case = next(item for item in load_fixture_cases() if item["name"] == name)
    evaluation = evaluate_document(case["packet"])
    assert evaluation.outcome == outcome
    assert evaluation.report["authority_created"] is False
    assert evaluation.report["descriptor_mutated"] is False
    assert evaluation.report["publication_created"] is False


def test_role_change_never_mutates_descriptor() -> None:
    case = next(item for item in load_fixture_cases() if item["name"] == "hold_role_change_with_lineage")
    before = copy.deepcopy(case["packet"]["descriptor"])
    evaluation = evaluate_document(case["packet"])
    assert evaluation.outcome == "HOLD"
    assert case["packet"]["descriptor"] == before


def test_identity_changes_when_support_changes() -> None:
    packet = load_json(BASE_PATH)
    original = expected_request_id(packet)
    packet["use"]["support_refs"]["evidence_refs"] = ["kfm:evidence-bundle:changed"]
    assert expected_request_id(packet) != original


def test_duplicate_json_keys_are_error() -> None:
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "duplicate.json"
        path.write_text('{"profile":"a","profile":"b"}', encoding="utf-8")
        evaluation = evaluate_path(path)
    assert evaluation.outcome == "ERROR"
    assert [item.code for item in evaluation.findings] == ["INPUT_JSON_INVALID"]


def test_fixture_execution_does_not_use_network() -> None:
    with mock.patch.object(socket, "socket", side_effect=AssertionError("network denied")):
        ok, payload = run_fixture_suite()
    assert ok, payload


def test_cli_and_compatibility_shim_are_deterministic() -> None:
    env = dict(os.environ)
    env["KFM_NO_NETWORK"] = "1"
    canonical = [sys.executable, str(REPO_ROOT / "tools/validators/source_role/validate_source_role.py"), "--fixtures"]
    compatibility = [sys.executable, str(REPO_ROOT / "tools/validators/sources/validate_source_role.py"), "--fixtures"]
    first = subprocess.run(canonical, cwd=REPO_ROOT, env=env, check=False, capture_output=True, text=True)
    second = subprocess.run(canonical, cwd=REPO_ROOT, env=env, check=False, capture_output=True, text=True)
    shim = subprocess.run(compatibility, cwd=REPO_ROOT, env=env, check=False, capture_output=True, text=True)
    assert first.returncode == second.returncode == shim.returncode == 0
    assert first.stdout == second.stdout == shim.stdout
    assert json.loads(first.stdout)["cases"] == 14


def test_direct_cli_exit_code_for_deny() -> None:
    case = next(item for item in load_fixture_cases() if item["name"] == "deny_ai_inferred")
    with tempfile.TemporaryDirectory() as directory:
        path = Path(directory) / "deny.json"
        path.write_text(json.dumps(case["packet"]), encoding="utf-8")
        completed = subprocess.run(
            [sys.executable, str(REPO_ROOT / "tools/validators/source_role/validate_source_role.py"), str(path)],
            cwd=REPO_ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
    assert completed.returncode == 6
    assert json.loads(completed.stdout)["outcome"] == "DENY"


def test_fixture_manifest_is_bounded_and_named() -> None:
    manifest = load_json(CASES_PATH)
    names = [item["name"] for item in manifest["cases"]]
    assert names == sorted(names, key=names.index)
    assert len(names) == len(set(names)) == 14
