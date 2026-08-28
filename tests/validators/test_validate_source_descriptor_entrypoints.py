"""Direct tests for SourceDescriptor schema and validator-path convergence."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import pytest

from tools.validators._common.jsonschema_runner import load_validator


ROOT = Path(__file__).resolve().parents[2]
IMPLEMENTATION_SCHEMA = (
    ROOT / "schemas/contracts/v1/source/source_descriptor.schema.json"
)
DECLARED_SCHEMA = (
    ROOT / "schemas/contracts/v1/sources/source_descriptor.schema.json"
)
FIXTURE_ROOT = ROOT / "fixtures/contracts/v1/source/source_descriptor"
ENTRYPOINTS = (
    ROOT / "tools/validators/validate_source_descriptor.py",
    ROOT / "tools/validators/sources/validate_source_descriptor.py",
)


def _fixtures(kind: str) -> list[Path]:
    return sorted((FIXTURE_ROOT / kind).glob("*.json"))


def _run(entrypoint: Path, *arguments: object, cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(entrypoint), *(str(value) for value in arguments)],
        cwd=cwd,
        check=False,
        capture_output=True,
        text=True,
        timeout=30,
    )


def test_declared_schema_is_a_bounded_alias() -> None:
    schema = json.loads(DECLARED_SCHEMA.read_text(encoding="utf-8"))

    assert schema["$schema"] == "https://json-schema.org/draft/2020-12/schema"
    assert schema["$id"] == (
        "kfm://schemas/contracts/v1/sources/source_descriptor.schema.json"
    )
    assert schema["$ref"] == (
        "https://schemas.kfm.local/contracts/v1/source/"
        "source_descriptor.schema.json"
    )
    assert "properties" not in schema
    assert "additionalProperties" not in schema
    assert schema["x-kfm"]["canonical_implementation_schema"] == (
        "schemas/contracts/v1/source/source_descriptor.schema.json"
    )
    assert schema["x-kfm"]["fixtures_root"] == (
        "fixtures/contracts/v1/source/source_descriptor/"
    )
    assert schema["x-kfm"]["validator"] == (
        "tools/validators/sources/validate_source_descriptor.py"
    )


def test_declared_and_implementation_schemas_have_identical_fixture_polarity() -> None:
    valid = _fixtures("valid")
    invalid = _fixtures("invalid")
    assert valid
    assert invalid

    implementation = load_validator(IMPLEMENTATION_SCHEMA)
    declared = load_validator(DECLARED_SCHEMA)

    for fixture in valid:
        candidate = json.loads(fixture.read_text(encoding="utf-8"))
        assert not list(implementation.iter_errors(candidate)), fixture
        assert not list(declared.iter_errors(candidate)), fixture

    for fixture in invalid:
        candidate = json.loads(fixture.read_text(encoding="utf-8"))
        assert list(implementation.iter_errors(candidate)), fixture
        assert list(declared.iter_errors(candidate)), fixture


@pytest.mark.parametrize("entrypoint", ENTRYPOINTS, ids=lambda path: path.parent.name)
def test_fixture_mode_is_cwd_independent(
    entrypoint: Path,
    tmp_path: Path,
) -> None:
    result = _run(entrypoint, "--fixtures", cwd=tmp_path)

    assert result.returncode == 0, result.stdout + result.stderr
    assert "OK " in result.stdout
    assert "EXPECTED_FAIL " in result.stdout
    assert not any(line.startswith("FAIL ") for line in result.stdout.splitlines())


@pytest.mark.parametrize("entrypoint", ENTRYPOINTS, ids=lambda path: path.parent.name)
def test_entrypoints_require_an_explicit_input(
    entrypoint: Path,
    tmp_path: Path,
) -> None:
    result = _run(entrypoint, cwd=tmp_path)

    assert result.returncode == 2
    assert result.stdout == ""
    assert "No files provided" in result.stderr


@pytest.mark.parametrize("entrypoint", ENTRYPOINTS, ids=lambda path: path.parent.name)
def test_entrypoints_match_explicit_file_polarity(
    entrypoint: Path,
    tmp_path: Path,
) -> None:
    valid = _fixtures("valid")[0]
    invalid = _fixtures("invalid")[0]

    valid_result = _run(entrypoint, valid, cwd=tmp_path)
    invalid_result = _run(entrypoint, invalid, cwd=tmp_path)

    assert valid_result.returncode == 0, valid_result.stdout + valid_result.stderr
    assert valid_result.stdout.startswith("OK ")
    assert invalid_result.returncode == 1
    assert invalid_result.stdout.startswith("FAIL ")
