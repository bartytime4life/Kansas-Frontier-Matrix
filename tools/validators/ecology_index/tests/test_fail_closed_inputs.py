from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

from tools.validators.ecology_index.validator import validate_file


SCHEMA_REF = "schemas/ecology/kfm_eco_index.schema.json"
FIXTURE_ROOT = Path("tools/validators/ecology_index/fixtures")


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "tools.validators.ecology_index", *args],
        check=False,
        text=True,
        capture_output=True,
    )


def test_validate_file_rejects_malformed_json(tmp_path: Path) -> None:
    input_path = tmp_path / "malformed.json"
    input_path.write_text("{ this is not valid json", encoding="utf-8")

    with pytest.raises(ValueError):
        validate_file(input_path=input_path, schema_ref=SCHEMA_REF)


def test_validate_file_rejects_non_object_json(tmp_path: Path) -> None:
    input_path = tmp_path / "array.json"
    input_path.write_text("[]\n", encoding="utf-8")

    with pytest.raises(ValueError, match="Eco index input must be a JSON object"):
        validate_file(input_path=input_path, schema_ref=SCHEMA_REF)


def test_cli_malformed_json_returns_validation_failure(tmp_path: Path) -> None:
    input_path = tmp_path / "malformed.json"
    input_path.write_text("{ this is not valid json", encoding="utf-8")

    result = run_cli(
        "--input",
        str(input_path),
        "--schema",
        SCHEMA_REF,
    )

    assert result.returncode == 1
    assert "invalid json:" in result.stderr


def test_cli_non_object_json_returns_validation_failure(tmp_path: Path) -> None:
    input_path = tmp_path / "array.json"
    input_path.write_text("[]\n", encoding="utf-8")

    result = run_cli(
        "--input",
        str(input_path),
        "--schema",
        SCHEMA_REF,
    )

    assert result.returncode == 1
    assert "invalid input:" in result.stderr
    assert "Eco index input must be a JSON object" in result.stderr


def test_cli_missing_input_fails_closed() -> None:
    result = run_cli(
        "--input",
        "tools/validators/ecology_index/fixtures/does_not_exist.json",
        "--schema",
        SCHEMA_REF,
    )

    assert result.returncode == 2
    assert "missing input:" in result.stderr


def test_cli_missing_schema_fails_closed() -> None:
    result = run_cli(
        "--input",
        str(FIXTURE_ROOT / "valid" / "huc12_vegetation_soil_hydrology.json"),
        "--schema",
        "schemas/ecology/does_not_exist.schema.json",
    )

    assert result.returncode == 3
    assert "missing schema:" in result.stderr
