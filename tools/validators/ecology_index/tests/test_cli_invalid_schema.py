from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


FIXTURE_ROOT = Path("tools/validators/ecology_index/fixtures")


def write_json(path: Path, value: object) -> None:
    path.write_text(json.dumps(value, indent=2) + "\n", encoding="utf-8")


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "-m", "tools.validators.ecology_index", *args],
        check=False,
        text=True,
        capture_output=True,
    )


def test_cli_invalid_schema_exits_three(tmp_path: Path) -> None:
    schema_path = tmp_path / "invalid_schema.json"

    write_json(
        schema_path,
        {
            "$schema": "https://json-schema.org/draft/2020-12/schema",
            "type": 123
        },
    )

    result = run_cli(
        "--input",
        str(FIXTURE_ROOT / "valid" / "air_station_vegetation.json"),
        "--schema",
        str(schema_path),
    )

    assert result.returncode == 3
    assert "invalid schema:" in result.stderr
    assert "internal validator error:" not in result.stderr
