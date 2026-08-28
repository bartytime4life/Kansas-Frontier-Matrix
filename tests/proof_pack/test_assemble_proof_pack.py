from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

from tools.proof_pack.assemble_proof_pack import assemble_candidate, render_manifest
from tools.proof_pack.proof_pack_check import validate_payload

ROOT = Path(__file__).resolve().parents[2]
FIXTURES = ROOT / "fixtures/contracts/v1/evidence/proof_pack"
CANDIDATE = FIXTURES / "candidates/release_support_candidate.json"
EXPECTED = FIXTURES / "valid/valid_release_support.json"
ASSEMBLER = ROOT / "tools/proof_pack/assemble_proof_pack.py"


def test_assembler_matches_golden_manifest() -> None:
    payload = assemble_candidate(CANDIDATE)
    assert render_manifest(payload) == EXPECTED.read_text(encoding="utf-8")
    assert validate_payload(payload) == ()


def test_assembler_is_deterministic() -> None:
    first = render_manifest(assemble_candidate(CANDIDATE))
    second = render_manifest(assemble_candidate(CANDIDATE))
    assert first == second


def test_cli_builds_explicit_output(tmp_path: Path) -> None:
    output = tmp_path / "proof_pack.json"
    result = subprocess.run(
        [
            sys.executable,
            str(ASSEMBLER),
            "--candidate",
            str(CANDIDATE),
            "--repo-root",
            str(ROOT),
            "--output",
            str(output),
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stdout + result.stderr
    assert output.read_text(encoding="utf-8") == EXPECTED.read_text(encoding="utf-8")
    assert "release_authority=false" in result.stdout


def test_cli_refuses_implicit_overwrite(tmp_path: Path) -> None:
    output = tmp_path / "proof_pack.json"
    output.write_text("occupied\n", encoding="utf-8")
    result = subprocess.run(
        [
            sys.executable,
            str(ASSEMBLER),
            "--candidate",
            str(CANDIDATE),
            "--repo-root",
            str(ROOT),
            "--output",
            str(output),
        ],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode != 0
    assert output.read_text(encoding="utf-8") == "occupied\n"
