from __future__ import annotations

import subprocess
import sys
from pathlib import Path


SCHEMA_REF = "schemas/ecology/kfm_eco_index.schema.json"
FIXTURE_ROOT = Path("tools/validators/ecology_index/fixtures")


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "tools.validators.ecology_index", *args],
        check=False,
        text=True,
        capture_output=True,
    )


def test_cli_valid_fixture_exits_zero() -> None:
    result = run_cli(
        "--input",
        str(FIXTURE_ROOT / "valid" / "huc12_vegetation_soil_hydrology.json"),
        "--schema",
        SCHEMA_REF,
    )

    assert result.returncode == 0
    assert "valid:" in result.stdout
    assert result.stderr == ""


def test_cli_invalid_fixture_exits_one() -> None:
    result = run_cli(
        "--input",
        str(FIXTURE_ROOT / "invalid" / "huc12_missing_watershed_id.json"),
        "--schema",
        SCHEMA_REF,
    )

    assert result.returncode == 1
    assert result.stdout == ""
    assert "ECO_INDEX_HUC12_WATERSHED_REQUIRED" in result.stderr


def test_cli_missing_input_exits_two() -> None:
    result = run_cli(
        "--input",
        "tools/validators/ecology_index/fixtures/missing.json",
        "--schema",
        SCHEMA_REF,
    )

    assert result.returncode == 2
    assert "missing input:" in result.stderr


def test_cli_missing_schema_exits_three() -> None:
    result = run_cli(
        "--input",
        str(FIXTURE_ROOT / "valid" / "air_station_vegetation.json"),
        "--schema",
        "schemas/ecology/missing.schema.json",
    )

    assert result.returncode == 3
    assert "missing schema:" in result.stderr


def test_cli_writes_receipt(tmp_path: Path) -> None:
    receipt_out = tmp_path / "cli_receipt.json"

    result = run_cli(
        "--input",
        str(FIXTURE_ROOT / "valid" / "air_station_vegetation.json"),
        "--schema",
        SCHEMA_REF,
        "--receipt-out",
        str(receipt_out),
    )

    assert result.returncode == 0
    assert receipt_out.exists()
