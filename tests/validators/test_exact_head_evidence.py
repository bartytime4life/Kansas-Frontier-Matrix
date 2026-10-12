from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
VALIDATOR = (
    ROOT
    / "tools"
    / "validators"
    / "evidence"
    / "validate_exact_head_evidence.py"
)
FIXTURE = ROOT / "fixtures" / "governance" / "exact_head_evidence" / "valid.json"
CURRENT_HEAD = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(VALIDATOR), str(FIXTURE), *args],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )


def test_valid_current_exact_head() -> None:
    result = run("--current-head", CURRENT_HEAD)
    assert result.returncode == 0, result.stdout + result.stderr
    assert "EXACT_HEAD_EVIDENCE_VALID" in result.stdout


def test_current_manifest_rejects_stale_head() -> None:
    result = run(
        "--current-head", "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
    )
    assert result.returncode == 2
    assert "STALE_HEAD" in result.stdout


def test_schema_fixes_release_authority_false() -> None:
    schema = json.loads(
        (
            ROOT
            / "schemas"
            / "contracts"
            / "v1"
            / "evidence"
            / "exact_head_evidence_manifest.schema.json"
        ).read_text(encoding="utf-8")
    )
    assert (
        schema["properties"]["disposition"]["properties"]["release_authority"][
            "const"
        ]
        is False
    )
