from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


def run_cli(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, "tools/evaluators/evaluate_fixture.py", *args],
        check=False,
        text=True,
        capture_output=True,
    )


def test_evaluator_fixture_allow(tmp_path: Path) -> None:
    output_path = tmp_path / "allow-report.json"

    result = run_cli(
        "--config",
        "tools/evaluators/examples/runtime_response.config.json",
        "--fixture",
        "tools/evaluators/fixtures/runtime_response/valid_response.json",
        "--output",
        str(output_path),
    )

    assert result.returncode == 0
    report = json.loads(output_path.read_text(encoding="utf-8"))
    assert report["outcome"] == "ALLOW"
    assert report["failure_flags"] == []


def test_evaluator_fixture_deny(tmp_path: Path) -> None:
    output_path = tmp_path / "deny-report.json"

    result = run_cli(
        "--config",
        "tools/evaluators/examples/runtime_response.config.json",
        "--fixture",
        "tools/evaluators/fixtures/citation_quality/missing_citation.json",
        "--output",
        str(output_path),
    )

    assert result.returncode == 0
    report = json.loads(output_path.read_text(encoding="utf-8"))
    assert report["outcome"] == "DENY"
    assert report["failure_flags"] == ["MISSING_CITATION"]


def test_evaluator_fixture_invalid_fixture_fails(tmp_path: Path) -> None:
    fixture_path = tmp_path / "bad-fixture.json"
    fixture_path.write_text(
        json.dumps(
            {
                "fixture_type": "kfm.evaluator_fixture.v1",
                "fixture_id": "broken",
                "fixture_category": "negative"
            }
        ),
        encoding="utf-8",
    )

    result = run_cli(
        "--config",
        "tools/evaluators/examples/runtime_response.config.json",
        "--fixture",
        str(fixture_path),
        "--output",
        str(tmp_path / "broken-report.json"),
    )

    assert result.returncode == 1
    assert "fixture failed schema validation" in result.stderr
