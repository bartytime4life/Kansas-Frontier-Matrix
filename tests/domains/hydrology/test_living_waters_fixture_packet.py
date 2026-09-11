"""Synthetic Living Waters semantics and the owning CI execution boundary.

The shell harness exercises the actual workflow block with a recording Python
stand-in. It proves argument wiring and failure propagation, not execution of
all Hydrology suites or runner-wide network isolation. Temporary probes never
change fixture bytes, executable bits, source admission, or release state.
"""
from __future__ import annotations

import copy
import importlib.util
import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest
import yaml
from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[3]
VALIDATOR_PATH = REPO_ROOT / "tools/validators/domains/hydrology/validate_living_waters_fixture_packet.py"
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/domains/hydrology/living_waters_fixture_packet.schema.json"
FIXTURES = REPO_ROOT / "fixtures/contracts/v1/domains/hydrology/living_waters_fixture_packet"

spec = importlib.util.spec_from_file_location("validate_living_waters_fixture_packet", VALIDATOR_PATH)
assert spec and spec.loader
validator = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = validator
spec.loader.exec_module(validator)


def _valid() -> dict[str, object]:
    return json.loads((FIXTURES / "valid/first_proof.json").read_text(encoding="utf-8"))


def test_schema_and_valid_fixture() -> None:
    Draft202012Validator.check_schema(json.loads(SCHEMA_PATH.read_text(encoding="utf-8")))
    assert validator.validate_file(FIXTURES / "valid/first_proof.json") == ()


def test_ambiguous_reach_join_must_abstain() -> None:
    findings = validator.validate_file(FIXTURES / "invalid/ambiguous_join_answered.json")
    assert validator.Finding("SCENARIO_OUTCOME_INVALID", "/scenarios/ambiguous-reach") in findings


def test_finite_states_are_complete_and_distinct() -> None:
    payload = _valid()
    scenarios = {item["id"]: item for item in payload["scenarios"]}  # type: ignore[index]
    assert {item["state"] for item in scenarios.values()} == {"AVAILABLE", "STALE", "NO_RESULTS", "UNAVAILABLE", "ABSTAIN"}
    assert scenarios["no-results"]["state"] != scenarios["unavailable"]["state"]


def test_parameter_statistic_unit_and_qualifier_are_exact() -> None:
    mutations = {"parameter_code": "00065", "statistic_code": "00003", "unit_code": "m3/s", "qualifier_code": "A"}
    for field, value in mutations.items():
        payload = copy.deepcopy(_valid())
        payload["series"][field] = value  # type: ignore[index]
        assert validator.Finding("SCHEMA_INVALID", f"/series/{field}") in validator.validate_payload(payload)


def test_governance_cannot_claim_forbidden_effects() -> None:
    for field in ("source_admitted", "source_activated", "policy_evaluated", "released", "deployed", "published"):
        payload = copy.deepcopy(_valid())
        payload["governance"][field] = True  # type: ignore[index]
        assert validator.Finding("SCHEMA_INVALID", f"/governance/{field}") in validator.validate_payload(payload)


def test_hydrograph_times_are_strictly_ordered() -> None:
    payload = copy.deepcopy(_valid())
    payload["series"]["points"].reverse()  # type: ignore[index]
    assert validator.Finding("HYDROGRAPH_TIME_ORDER_INVALID", "/series/points") in validator.validate_payload(payload)


def test_validator_has_no_network_client_import() -> None:
    source = VALIDATOR_PATH.read_text(encoding="utf-8")
    assert not any(token in source for token in ("import requests", "import httpx", "import socket", "from urllib"))


def test_cli_receipt_is_explicitly_non_authorizing() -> None:
    result = subprocess.run([sys.executable, str(VALIDATOR_PATH), str(FIXTURES / "valid/first_proof.json")], cwd=REPO_ROOT, text=True, capture_output=True, check=False)
    assert result.returncode == 0
    receipt = json.loads(result.stdout)
    assert receipt["outcome"] == "PASS"
    assert set(receipt["authority"].values()) == {False}


WORKFLOW_PATH = REPO_ROOT / ".github/workflows/domain-hydrology.yml"
LIVING_WATERS_TEST = "tests/domains/hydrology/test_living_waters_fixture_packet.py"
LIVING_WATERS_MARKER = "WORKFLOW_CHECK_EXECUTED: hydrology-living-waters-fixture-packet"


def _workflow_steps() -> tuple[dict, dict]:
    workflow = yaml.safe_load(WORKFLOW_PATH.read_text(encoding="utf-8"))
    steps = workflow["jobs"]["validate-hydrology"]["steps"]
    bounded = [step for step in steps if step.get("name") == "Run bounded Hydrology schema validation"]
    summary = [step for step in steps if step.get("name") == "Record Hydrology validation result and broader hold"]
    assert len(bounded) == len(summary) == 1
    return bounded[0], summary[0]


def _bash() -> str:
    executable = shutil.which("bash")
    if executable is None:
        pytest.skip("Bash is required for the Linux workflow execution contract")
    return executable


def _run_bounded_shell(
    tmp_path: Path, script: str, *, pytest_status: int = 0,
    guard_status: int = 0, accept_invalid: bool = False,
) -> tuple[subprocess.CompletedProcess[str], list[list[str]]]:
    # Reproduce the real 100644 input: it is a pytest argument, not a program.
    probe = tmp_path / LIVING_WATERS_TEST
    probe.parent.mkdir(parents=True, exist_ok=True)
    probe.write_text("# synthetic non-executable argument probe\n", encoding="utf-8")
    probe.chmod(0o644)
    trace = tmp_path / "python-argv.bin"
    trace.write_bytes(b"")
    environment = {
        "PATH": "/usr/bin:/bin", "HOME": str(tmp_path), "LC_ALL": "C",
        "KFM_TEST_TRACE": str(trace), "KFM_TEST_PYTEST_STATUS": str(pytest_status),
        "KFM_TEST_GUARD_STATUS": str(guard_status),
        "KFM_TEST_ACCEPT_INVALID": "1" if accept_invalid else "0",
    }
    # Functions take precedence over PATH. No real Python or domain validator
    # runs in this subprocess; the owning suites execute separately in pytest.
    recorder = r"""
python() {
  printf '\036' >> "$KFM_TEST_TRACE"
  printf '%s\0' "$@" >> "$KFM_TEST_TRACE"
  if [[ "${1:-}" == "-c" ]]; then
    return "$KFM_TEST_GUARD_STATUS"
  fi
  if [[ "${1:-}" == "-m" && "${2:-}" == "pytest" ]]; then
    return "$KFM_TEST_PYTEST_STATUS"
  fi
  case " $* " in
    *"/invalid/"*)
      if [[ "$KFM_TEST_ACCEPT_INVALID" == "1" ]]; then return 0; fi
      return 1 ;;
  esac
  return 0
}
"""
    result = subprocess.run(
        [_bash(), "--noprofile", "--norc", "-c", recorder + script],
        cwd=tmp_path, env=environment, text=True, capture_output=True,
        timeout=10, check=False,
    )
    calls = [
        chunk.decode("utf-8").rstrip("\0").split("\0")
        for chunk in trace.read_bytes().split(b"\x1e") if chunk
    ]
    return result, calls


def test_workflow_runs_living_waters_with_pytest_and_reaches_later_checks(tmp_path: Path) -> None:
    bounded, _ = _workflow_steps()
    result, calls = _run_bounded_shell(tmp_path, bounded["run"])
    assert result.returncode == 0, result.stderr
    pytest_calls = [call for call in calls if call[:2] == ["-m", "pytest"]]
    assert len(pytest_calls) == 1
    expected_modules = [
        "test_no_network_proof.py", "test_hydrology_smoke.py",
        "test_aquifer_observation.py", "test_aquifer_context_link.py",
        "test_nhdplus_hr_ambiguity.py", "test_adaptive_threshold_proposal.py",
        "test_hydro_identity_bridge.py", "test_streamflow_qc_context_assessment.py",
        "test_living_waters_fixture_packet.py",
    ]
    assert pytest_calls[0] == ["-m", "pytest", "-q", "-p", "no:cacheprovider"] + [
        f"tests/domains/hydrology/{name}" for name in expected_modules
    ]
    assert ["tests/domains/hydrology/test_public_safe_flow_fixture.py", "--verbose"] in calls
    assert ["tests/domains/hydrology/test_public_safe_water_level_fixture.py", "--verbose"] in calls
    assert ["tests/cross_domain/test_environmental_observation_boundaries.py", "--verbose"] in calls
    for group, name in (("valid", "first_proof"), ("invalid", "ambiguous_join_answered")):
        assert [
            "tools/validators/domains/hydrology/validate_living_waters_fixture_packet.py",
            f"fixtures/contracts/v1/domains/hydrology/living_waters_fixture_packet/{group}/{name}.json",
        ] in calls
    assert calls[-1] == [
        "tools/validators/domains/hydrology/validate_nhdplus_waterbody_crosswalk.py", "--fixtures",
    ]
    assert LIVING_WATERS_MARKER in result.stdout
    assert "WORKFLOW_HOLD:" in result.stdout


def test_missing_continuation_control_detects_unexecuted_living_waters(tmp_path: Path) -> None:
    bounded, _ = _workflow_steps()
    line = "tests/domains/hydrology/test_streamflow_qc_context_assessment.py"
    script = bounded["run"]
    assert line + " \\\n" in script
    broken = script.replace(line + " \\\n", line + "\n", 1)
    result, calls = _run_bounded_shell(tmp_path, broken)
    assert result.returncode == 126
    assert "Permission denied" in result.stderr
    pytest_call = next(call for call in calls if call[:2] == ["-m", "pytest"])
    assert LIVING_WATERS_TEST not in pytest_call
    assert len(calls) == 2  # startup assertion and incomplete pytest invocation
    assert "WORKFLOW_CHECK_EXECUTED:" not in result.stdout


@pytest.mark.parametrize("exit_code", [1, 2, 5])
def test_workflow_propagates_pytest_failure_before_later_checks(tmp_path: Path, exit_code: int) -> None:
    bounded, _ = _workflow_steps()
    result, calls = _run_bounded_shell(tmp_path, bounded["run"], pytest_status=exit_code)
    assert result.returncode == exit_code
    assert len(calls) == 2
    assert "WORKFLOW_CHECK_EXECUTED:" not in result.stdout


def test_workflow_stops_when_startup_guard_is_unavailable(tmp_path: Path) -> None:
    bounded, _ = _workflow_steps()
    result, calls = _run_bounded_shell(tmp_path, bounded["run"], guard_status=1)
    assert result.returncode == 1
    assert len(calls) == 1
    assert "WORKFLOW_CHECK_EXECUTED:" not in result.stdout


def test_workflow_rejects_an_accepted_negative_control(tmp_path: Path) -> None:
    bounded, _ = _workflow_steps()
    result, _ = _run_bounded_shell(tmp_path, bounded["run"], accept_invalid=True)
    assert result.returncode == 1
    assert "known-invalid Hydrology EvidenceBundle fixture was accepted" in result.stdout
    assert "WORKFLOW_CHECK_EXECUTED:" not in result.stdout


def test_summary_uses_raw_bounded_step_outcome_and_preserves_guards() -> None:
    bounded, summary = _workflow_steps()
    assert bounded["id"] == "bounded_validation"
    assert bounded.get("continue-on-error", False) is False
    assert bounded["env"]["KFM_NO_NETWORK"] == "1"
    assert bounded["env"]["PYTHONDONTWRITEBYTECODE"] == "1"
    assert bounded["env"]["PYTHONPATH"] == "${{ github.workspace }}/tools/ci/kfm_no_network:${{ github.workspace }}"
    assert summary["if"] == "always()"
    assert summary["env"]["KFM_HYDROLOGY_VALIDATION_OUTCOME"] == "${{ steps.bounded_validation.outcome }}"


@pytest.mark.parametrize("outcome", ["success", "failure", "cancelled", "skipped", "", "PRIVATE-SENTINEL"])
def test_summary_claims_completion_only_after_success(tmp_path: Path, outcome: str) -> None:
    _, summary = _workflow_steps()
    output = tmp_path / "summary.md"
    result = subprocess.run(
        [_bash(), "--noprofile", "--norc", "-c", summary["run"]],
        cwd=tmp_path,
        env={
            "PATH": "/usr/bin:/bin", "HOME": str(tmp_path), "LC_ALL": "C",
            "GITHUB_STEP_SUMMARY": str(output),
            "KFM_HYDROLOGY_VALIDATION_OUTCOME": outcome,
        },
        text=True, capture_output=True, timeout=10, check=False,
    )
    assert result.returncode == 0, result.stderr
    text = output.read_text(encoding="utf-8")
    assert "WORKFLOW_HOLD:" in text
    assert "PRIVATE-SENTINEL" not in text
    if outcome == "success":
        assert LIVING_WATERS_MARKER in text
        assert "eleven bounded domain modules" in text
        assert "WORKFLOW_CHECK_NOT_COMPLETED:" not in text
    else:
        assert "WORKFLOW_CHECK_EXECUTED:" not in text
        assert "WORKFLOW_CHECK_NOT_COMPLETED: hydrology-bounded-validation" in text
        safe_outcome = outcome if outcome in {"failure", "cancelled", "skipped"} else "unknown"
        assert f"Bounded validation outcome: {safe_outcome}." in text


# Timestamp spelling is not chronology. These cases keep the existing UTC-Z
# schema and compare observation instants without rewriting source strings.
@pytest.mark.parametrize("timestamps", [
    ("2026-09-10T12:00:00Z", "2026-09-10T12:00:00.1Z", "2026-09-10T12:00:01Z"),
    ("2026-09-10T12:00:00.1Z", "2026-09-10T12:00:00.11Z", "2026-09-10T12:00:00.2Z"),
    ("2026-09-10T12:00:00.09Z", "2026-09-10T12:00:00.1Z", "2026-09-10T12:00:00.1001Z"),
    ("2026-09-10T12:00:00Z", "2026-09-10T12:00:00.0000001Z", "2026-09-10T12:00:00.0000002Z"),
    ("2026-09-10T12:00:00.1234567890123456789012345678901Z", "2026-09-10T12:00:00.1234567890123456789012345678902Z", "2026-09-10T12:00:01Z"),
    ("2026-12-31T23:59:59.999Z", "2027-01-01T00:00:00Z", "2027-01-01T00:00:00.001Z"),
    ("2026-09-10t12:00:00Z", "2026-09-10T12:15:00Z", "2026-09-10t12:30:00Z"),
])
def test_chronology_accepts_exact_increasing_instants_without_mutation(timestamps: tuple[str, ...]) -> None:
    payload = _valid()
    for point, timestamp in zip(payload["series"]["points"], timestamps):
        point["observed_at"] = timestamp
    before = copy.deepcopy(payload)
    assert validator.validate_payload(payload) == ()
    assert payload == before


@pytest.mark.parametrize("timestamps", [
    ("2026-09-10T12:00:00.1Z", "2026-09-10T12:00:00Z", "2026-09-10T12:00:01Z"),
    ("2026-09-10T12:00:00.000Z", "2026-09-10T12:00:00Z", "2026-09-10T12:00:01Z"),
    ("2026-09-10T12:00:00.10Z", "2026-09-10T12:00:00.1Z", "2026-09-10T12:00:01Z"),
    ("2026-09-10T12:00:00Z", "2026-09-10t12:00:00Z", "2026-09-10t12:00:01Z"),
    ("2026-09-10T12:00:00Z", "2026-09-10T12:00:00Z", "2026-09-10T12:00:01Z"),
    ("2026-09-10T12:00:00.11Z", "2026-09-10T12:00:00.1Z", "2026-09-10T12:00:00.2Z"),
    ("2026-09-10T12:00:00.1234567890123456789012345678902Z", "2026-09-10T12:00:00.1234567890123456789012345678901Z", "2026-09-10T12:00:01Z"),
])
def test_chronology_rejects_reversed_or_equivalent_instants(timestamps: tuple[str, ...]) -> None:
    payload = _valid()
    for point, timestamp in zip(payload["series"]["points"], timestamps):
        point["observed_at"] = timestamp
    expected = (validator.Finding("HYDROGRAPH_TIME_ORDER_INVALID", "/series/points"),)
    assert validator.validate_payload(payload) == expected
    assert validator.validate_payload(payload) == expected


@pytest.mark.parametrize("timestamp", [
    "2026-09-10T12:00:00+00:00", "2026-09-10T12:00:00-00:00",
    "2026-02-30T12:00:00Z", "2026-09-10T12:00:00.Z",
])
def test_chronology_keeps_schema_rejection_before_comparison(timestamp: str) -> None:
    payload = _valid()
    payload["series"]["points"][0]["observed_at"] = timestamp
    findings = validator.validate_payload(payload)
    assert validator.Finding("SCHEMA_INVALID", "/series/points/0/observed_at") in findings
    assert all(item.code == "SCHEMA_INVALID" for item in findings)


def test_chronology_matches_an_exact_fraction_oracle() -> None:
    from fractions import Fraction
    from itertools import product

    fractions = ("", "0", "000", "001", "09", "090", "1", "10", "11", "1234567890123456789012345678901")
    for left, right in product(fractions, repeat=2):
        payload = _valid()
        points = payload["series"]["points"]
        points[0]["observed_at"] = "2026-09-10T12:00:00" + ("." + left if left else "") + "Z"
        points[1]["observed_at"] = "2026-09-10T12:00:00" + ("." + right if right else "") + "Z"
        # The third point stays in a later minute, so only the first pair decides.
        expected_ok = Fraction("0." + (left or "0")) < Fraction("0." + (right or "0"))
        findings = validator.validate_payload(payload)
        assert (findings == ()) is expected_ok, (left, right, findings)


@pytest.mark.parametrize("first,second,expected_exit", [
    ("2026-09-10T12:00:00Z", "2026-09-10T12:00:00.1Z", 0),
    ("2026-09-10T12:00:00.1Z", "2026-09-10T12:00:00Z", 1),
    ("2026-09-10T12:00:00.000Z", "2026-09-10T12:00:00Z", 1),
])
def test_chronology_cli_returns_bounded_report_without_rewriting_input(
    tmp_path: Path, first: str, second: str, expected_exit: int,
) -> None:
    payload = _valid()
    payload["series"]["points"][0]["observed_at"] = first
    payload["series"]["points"][1]["observed_at"] = second
    candidate = tmp_path / "chronology.json"
    before = json.dumps(payload, sort_keys=True).encode("utf-8")
    candidate.write_bytes(before)
    result = subprocess.run(
        [sys.executable, str(VALIDATOR_PATH), str(candidate)], cwd=REPO_ROOT,
        text=True, capture_output=True, timeout=10, check=False,
    )
    assert result.returncode == expected_exit
    assert result.stderr == ""
    report = json.loads(result.stdout)
    assert report["outcome"] == ("PASS" if expected_exit == 0 else "FAIL")
    assert report["findings"] == ([] if expected_exit == 0 else [
        {"code": "HYDROGRAPH_TIME_ORDER_INVALID", "field": "/series/points"},
    ])
    assert set(report["authority"].values()) == {False}
    assert candidate.read_bytes() == before
