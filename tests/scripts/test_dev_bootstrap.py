from __future__ import annotations

import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCRIPT = ROOT / "scripts" / "dev" / "bootstrap.sh"


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["bash", str(SCRIPT), *args],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )


def test_bootstrap_has_valid_bash_syntax() -> None:
    result = subprocess.run(
        ["bash", "-n", str(SCRIPT)],
        cwd=ROOT,
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0, result.stderr


def test_bootstrap_help_is_read_only_and_documents_guardrails() -> None:
    result = run("--help")
    assert result.returncode == 0
    assert "--check" in result.stdout
    assert "--offline" in result.stdout
    assert "--install-system" in result.stdout
    assert "never invokes sudo" in result.stdout


def test_bootstrap_rejects_unknown_arguments() -> None:
    result = run("--definitely-not-supported")
    assert result.returncode == 2
    assert "unknown argument" in result.stderr
