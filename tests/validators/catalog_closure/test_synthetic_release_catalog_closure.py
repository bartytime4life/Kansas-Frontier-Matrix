from __future__ import annotations

import importlib.util
import json
import socket
import subprocess
import sys
import tempfile
from pathlib import Path
from unittest import mock

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[3]
VALIDATOR = ROOT / "tools/validators/catalog_closure/validate_synthetic_release_catalog_closure.py"
SCHEMA = ROOT / "schemas/contracts/v1/data/synthetic_release_catalog_closure_profile.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/data/synthetic_release_catalog_closure_profile"
CASES = FIXTURES / "cases.json"

SPEC = importlib.util.spec_from_file_location(
    "validate_synthetic_release_catalog_closure",
    VALIDATOR,
)
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = MODULE
SPEC.loader.exec_module(MODULE)


def manifest() -> dict:
    return MODULE.load_cases()


def test_schema_is_closed_and_points_to_current_validator() -> None:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(schema)
    assert schema["additionalProperties"] is False
    assert (
        schema["x-kfm"]["validator"]
        == "tools/validators/catalog_closure/validate_synthetic_release_catalog_closure.py"
    )


def test_exact_fixture_matrix_and_finite_reason_codes() -> None:
    cases = manifest()["cases"]
    assert len(cases) == 17
    assert sum(case["expected_outcome"] == "PASS" for case in cases) == 2
    for case in cases:
        result = MODULE.validate_candidate(MODULE.materialize_case(manifest(), case))
        assert result.outcome == case["expected_outcome"], case["case_id"]
        assert sorted({item.code for item in result.findings}) == sorted(
            case["expected_reason_codes"]
        ), case["case_id"]


def test_generated_packets_are_schema_valid_and_byte_stable() -> None:
    schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema)
    for case in manifest()["cases"]:
        if not case.get("expected_packet_spec_hash"):
            continue
        candidate = MODULE.materialize_case(manifest(), case)
        first = MODULE.validate_candidate(candidate)
        second = MODULE.validate_candidate(candidate)
        assert first == second
        assert first.packet is not None
        assert not list(validator.iter_errors(first.packet))
        assert first.packet["spec_hash"] == case["expected_packet_spec_hash"]
        assert MODULE.canonical_bytes(first.packet) == MODULE.canonical_bytes(second.packet)


def test_cross_profile_dimensions_agree() -> None:
    current = manifest()["cases"][0]
    packet = MODULE.validate_candidate(
        MODULE.materialize_case(manifest(), current)
    ).packet
    assert packet is not None
    records = list(packet["projections"].values())
    shared_fields = (
        "release_id",
        "artifact_id",
        "digest",
        "bbox",
        "interval",
        "source_role",
        "license",
        "sensitivity",
        "public_safe",
        "review_state",
        "release_state",
        "catalog_state",
        "correction_ref",
        "rollback_ref",
        "authored_at",
        "public_url",
    )
    for field in shared_fields:
        assert len({json.dumps(record[field], sort_keys=True) for record in records}) == 1
    assert {record["profile"] for record in records} == {"STAC", "DCAT", "PROV"}
    assert len({record["record_id"] for record in records}) == 7


def test_withdrawal_preserves_history_and_updates_all_profiles() -> None:
    current_case, withdrawn_case = manifest()["cases"][:2]
    current = MODULE.validate_candidate(
        MODULE.materialize_case(manifest(), current_case)
    ).packet
    withdrawn = MODULE.validate_candidate(
        MODULE.materialize_case(manifest(), withdrawn_case)
    ).packet
    assert current is not None and withdrawn is not None
    assert current["packet_id"] != withdrawn["packet_id"]
    assert withdrawn["transition"]["predecessor_packet_ref"]
    assert withdrawn["transition"]["correction_notice_ref"]
    assert withdrawn["closure_report"]["history_preserved"] is True
    assert {
        record["catalog_state"] for record in withdrawn["projections"].values()
    } == {"WITHDRAWN"}
    assert {
        record["public_safe"] for record in withdrawn["projections"].values()
    } == {False}


def test_no_network_and_cli_fixture_command() -> None:
    with mock.patch.object(
        socket, "create_connection", side_effect=AssertionError("network")
    ), mock.patch.object(socket, "socket", side_effect=AssertionError("network")):
        assert MODULE.run_fixtures() == 0
    run = subprocess.run(
        [sys.executable, str(VALIDATOR), "--fixtures"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert run.returncode == 0, run.stdout + run.stderr
    assert "SYNTHETIC_RELEASE_CATALOG_CLOSURE_FIXTURES_VALID cases=17" in run.stdout


def test_output_is_explicit_and_never_written_to_lifecycle_roots() -> None:
    candidate = MODULE.materialize_case(manifest(), manifest()["cases"][0])
    with tempfile.TemporaryDirectory() as directory:
        input_path = Path(directory) / "candidate.json"
        output_path = Path(directory) / "packet.json"
        input_path.write_text(json.dumps(candidate), encoding="utf-8")
        run = subprocess.run(
            [
                sys.executable,
                str(VALIDATOR),
                str(input_path),
                "--write-packet",
                str(output_path),
            ],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )
        assert run.returncode == 0, run.stdout + run.stderr
        written = json.loads(output_path.read_text(encoding="utf-8"))
        assert written["spec_hash"] == manifest()["cases"][0]["expected_packet_spec_hash"]
        assert output_path.read_bytes() == MODULE.canonical_bytes(written)


def test_duplicate_nonfinite_and_symlink_inputs_fail_closed() -> None:
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        duplicate = root / "duplicate.json"
        nonfinite = root / "nonfinite.json"
        duplicate.write_text('{"id":"a","id":"b"}', encoding="utf-8")
        nonfinite.write_text('{"value":NaN}', encoding="utf-8")
        assert {item.code for item in MODULE.validate_file(duplicate).findings} == {
            "JSON_DUPLICATE_KEY"
        }
        assert {item.code for item in MODULE.validate_file(nonfinite).findings} == {
            "JSON_NONFINITE_NUMBER"
        }
        target = root / "target.json"
        link = root / "link.json"
        target.write_text("{}", encoding="utf-8")
        try:
            link.symlink_to(target)
        except (OSError, NotImplementedError):
            return
        assert {item.code for item in MODULE.validate_file(link).findings} == {
            "INPUT_SYMLINK_DENIED"
        }


def test_cli_exit_codes_are_finite() -> None:
    valid = MODULE.materialize_case(manifest(), manifest()["cases"][0])
    invalid = MODULE.materialize_case(manifest(), manifest()["cases"][2])
    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        valid_path = root / "valid.json"
        invalid_path = root / "invalid.json"
        valid_path.write_text(json.dumps(valid), encoding="utf-8")
        invalid_path.write_text(json.dumps(invalid), encoding="utf-8")
        for path, expected in (
            (valid_path, 0),
            (invalid_path, 1),
            (root / "missing.json", 2),
        ):
            run = subprocess.run(
                [sys.executable, str(VALIDATOR), str(path)],
                cwd=ROOT,
                text=True,
                capture_output=True,
                check=False,
            )
            assert run.returncode == expected, run.stdout + run.stderr
