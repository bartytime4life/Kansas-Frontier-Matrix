from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path

import pytest

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


@pytest.mark.parametrize(
    "args",
    [
        ("--check", "--install-system"),
        ("--install-system", "--check"),
        ("--check", "--install-system", "--offline"),
        ("--install-system", "--offline", "--check"),
        ("--check", "--json", "--install-system"),
        ("--json", "--install-system", "--check"),
        ("--offline", "--json", "--install-system", "--check"),
        ("--install-system", "--check", "--offline", "--json"),
    ],
)
def test_inspection_rejects_system_install_before_host_checks(
    tmp_path: Path, args: tuple[str, ...]
) -> None:
    marker = tmp_path / "host-operations"
    mock_bin = tmp_path / "bin"
    mock_bin.mkdir()
    for name in ("apt-get", "corepack", "git", "node", "pnpm", "python3", "sudo"):
        command = mock_bin / name
        command.write_text(
            '#!/bin/sh\nprintf "%s\\n" "$0" >> "$KFM_BOOTSTRAP_TEST_MARKER"\nexit 99\n'
        )
        command.chmod(0o755)
    # Make the old path deterministic on any host and record OS probing too.
    # Mutation commands above are sentinels, never the real system installers.
    bash_env = tmp_path / "bash-env"
    bash_env.write_text(
        'source() {\n'
        '  if [[ "$1" == /etc/os-release ]]; then\n'
        '    printf "%s\\n" os-release >> "$KFM_BOOTSTRAP_TEST_MARKER"\n'
        '    ID=ubuntu\n'
        '    VERSION_ID=24.04\n'
        '  else\n'
        '    builtin source "$@"\n'
        '  fi\n'
        '}\n'
    )
    env = dict(os.environ)
    env.update(
        BASH_ENV=str(bash_env),
        KFM_BOOTSTRAP_TEST_MARKER=str(marker),
        PATH=str(mock_bin) + os.pathsep + env.get("PATH", ""),
    )
    result = subprocess.run(
        [shutil.which("bash") or "/bin/bash", str(SCRIPT), *args],
        cwd=ROOT,
        env=env,
        check=False,
        capture_output=True,
        text=True,
    )
    assert result.returncode == 2
    assert result.stderr == "bootstrap: --check is incompatible with --install-system\n"
    assert result.stdout == ""
    assert not marker.exists(), "host probing or an installation command was reached"
