"""Tests for bounded promotion verification execution."""
from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[2]
MODULE_PATH = REPO_ROOT / "tools/validators/promotion_gate/execute_promotion_verification.py"
FIXTURE_ROOT = REPO_ROOT / "fixtures/release/promotion_verification_execution"
RESULT_SCHEMA = json.loads((REPO_ROOT / "schemas/contracts/v1/release/promotion_verification_execution_result.schema.json").read_text(encoding="utf-8"))
RESULT_VALIDATOR = Draft202012Validator(RESULT_SCHEMA, format_checker=FormatChecker())

SPEC = importlib.util.spec_from_file_location("kfm_promotion_verification_execution", MODULE_PATH)
assert SPEC and SPEC.loader
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def load(kind: str, name: str) -> dict[str, object]:
    value = json.loads((FIXTURE_ROOT / kind / name).read_text(encoding="utf-8"))
    assert isinstance(value, dict)
    return value


def tool(name: str) -> Path:
    return FIXTURE_ROOT / "bin" / name


def execute(plan: dict[str, object], *, cosign: str = "fake_cosign.py") -> dict[str, object]:
    result = MODULE.execute(
        plan,
        repo_root=REPO_ROOT,
        cosign_bin=tool(cosign),
        conftest_bin=tool("fake_conftest.py"),
        promotion_validator=tool("fake_promotion_validator.py"),
        cosign_plan_validator=tool("fake_cosign_plan_validator.py"),
    )
    assert list(RESULT_VALIDATOR.iter_errors(result)) == []
    return result


def test_complete_fixture_passes_without_authorizing_promotion() -> None:
    result = execute(load("valid", "pass.json"))
    assert result["status"] == "PASS"
    assert result["readiness"] == "APPROVE_READY"
    assert result["promotion_gate"]["status"] == "PASS"
    assert result["cosign_plan_validation"]["status"] == "PASS"
    assert result["tools"]["cosign"]["status"] == "PASS"
    assert result["tools"]["conftest"]["status"] == "PASS"
    assert {entry["kind"] for entry in result["references"]} == {
        "EVIDENCE_BUNDLE",
        "STAC",
        "DCAT",
        "PROV",
        "ROLLBACK",
    }
    assert result["authority"] == {
        "deployment_authorized": False,
        "lifecycle_write": False,
        "promotion_authorized": False,
        "publication_authorized": False,
        "release_authorized": False,
    }


def test_catalog_subject_mismatch_fails_closed() -> None:
    result = execute(load("invalid", "deny_catalog_mismatch.json"))
    assert result["status"] == "DENY"
    assert result["readiness"] == "BLOCKED"
    assert {
        finding["code"] for finding in result["findings"]
    } == {"REFERENCE_ARTIFACT_MISMATCH"}


def test_substituted_cosign_binary_is_denied_before_execution() -> None:
    result = execute(load("valid", "pass.json"), cosign="fake_conftest.py")
    assert result["status"] == "DENY"
    assert any(
        finding["code"] == "COSIGN_BINARY_DIGEST_MISMATCH"
        for finding in result["findings"]
    )
    assert result["tools"]["cosign"]["status"] == "DENY"


def test_execution_spec_hash_mismatch_is_denied() -> None:
    plan = load("valid", "pass.json")
    plan["evaluated_at"] = "2026-04-13T01:00:01Z"
    result = execute(plan)
    assert result["status"] == "DENY"
    assert result["findings"] == [
        {
            "code": "EXECUTION_SPEC_HASH_MISMATCH",
            "path": "/spec_hash",
            "status": "DENY",
        }
    ]


def test_cli_entrypoint_runs_directly_by_file_path() -> None:
    completed = subprocess.run(
        [
            sys.executable,
            str(MODULE_PATH),
            str(FIXTURE_ROOT / "valid" / "pass.json"),
            "--repo-root",
            str(REPO_ROOT),
            "--cosign-bin",
            str(tool("fake_cosign.py")),
            "--conftest-bin",
            str(tool("fake_conftest.py")),
            "--promotion-validator",
            str(tool("fake_promotion_validator.py")),
            "--cosign-plan-validator",
            str(tool("fake_cosign_plan_validator.py")),
        ],
        cwd=REPO_ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert completed.returncode == 0, completed.stderr
    result = json.loads(completed.stdout)
    assert result["status"] == "PASS"
    assert result["readiness"] == "APPROVE_READY"
    assert result["authority"]["promotion_authorized"] is False
