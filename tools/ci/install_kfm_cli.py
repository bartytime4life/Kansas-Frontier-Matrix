#!/usr/bin/env python3
"""Install the fixed, hash-locked KFM developer CLI package for CI.

Callers cannot supply a package, URL, index, requirement path, local path, or
shell fragment. The dependency overlay is installed with hash enforcement; the
fixed local package is then installed without dependency resolution or build
isolation after the normal project-test profile has provided the build backend.
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
import time
from pathlib import Path
from typing import Sequence


REPO_ROOT = Path(__file__).resolve().parents[2]
LOCKFILE = REPO_ROOT / "tools/ci/python-cli.lock"
LOCAL_PACKAGE = REPO_ROOT / "packages/kfm-cli"
LOCAL_SPEC = "./packages/kfm-cli"
LOCK_LIMIT_BYTES = 262_144
MAX_HASHES_PER_REQUIREMENT = 32
INSTALL_TIMEOUT_SECONDS = 300
UNSAFE_PYTHON_ENVIRONMENT = {"PYTHONHOME", "PYTHONPATH", "PYTHONUSERBASE"}
HASH_LINE = re.compile(r"^\s+--hash=sha256:[0-9a-f]{64}(?: \\)?$")
REQUIREMENT_LINE = re.compile(
    r"^[A-Za-z0-9]+(?:[._-][A-Za-z0-9]+)*"
    r"==[A-Za-z0-9]+(?:[._+!-][A-Za-z0-9]+)* \\?$"
)
DISTRIBUTION_SEPARATOR = re.compile(r"[-_.]+")
FORBIDDEN_LOCK_TEXT = (
    "--extra-index-url",
    "--index-url",
    "--trusted-host",
    "--editable",
    "-e ",
    " @ ",
    "git+",
    "http://",
    "https://",
)


class CliInstallConfigurationError(ValueError):
    """Raised when the committed CLI install inputs are unsafe."""


def validate_lockfile(path: Path = LOCKFILE) -> None:
    """Fail closed unless every CLI requirement is exact and SHA-256 hashed."""

    if path.is_symlink() or not path.is_file():
        raise CliInstallConfigurationError("CLI_LOCKFILE_UNSAFE")
    try:
        size = path.stat().st_size
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise CliInstallConfigurationError("CLI_LOCKFILE_UNREADABLE") from exc
    if size <= 0 or size > LOCK_LIMIT_BYTES:
        raise CliInstallConfigurationError("CLI_LOCKFILE_SIZE_INVALID")

    lowered = text.lower()
    if any(token in lowered for token in FORBIDDEN_LOCK_TEXT):
        raise CliInstallConfigurationError("CLI_LOCKFILE_SOURCE_UNSAFE")

    physical_lines = text.splitlines()
    if any(
        previous.rstrip().endswith("\\")
        and not previous.lstrip().startswith("#")
        and (not current.strip() or current.lstrip().startswith("#"))
        for previous, current in zip(physical_lines, physical_lines[1:])
    ):
        raise CliInstallConfigurationError(
            "CLI_LOCKFILE_CONTINUATION_INTERRUPTED"
        )

    lock_lines = [
        line
        for line in physical_lines
        if line.strip() and not line.lstrip().startswith("#")
    ]
    if any(
        (line[0].isspace() and "--hash=" not in line) or line.startswith("-")
        for line in lock_lines
    ):
        raise CliInstallConfigurationError("CLI_LOCKFILE_DIRECTIVE_UNSAFE")
    requirements = [line for line in lock_lines if not line[0].isspace()]
    hashes = [line for line in lock_lines if "--hash=" in line]
    hash_coverage: list[int] = []
    hash_groups: list[list[str]] = []
    for line in lock_lines:
        if not line[0].isspace():
            hash_coverage.append(0)
            hash_groups.append([])
        elif "--hash=" in line:
            if not hash_coverage:
                raise CliInstallConfigurationError(
                    "CLI_LOCKFILE_HASH_COVERAGE_INVALID"
                )
            hash_coverage[-1] += 1
            hash_groups[-1].append(line)
            if hash_coverage[-1] > MAX_HASHES_PER_REQUIREMENT:
                raise CliInstallConfigurationError(
                    "CLI_LOCKFILE_HASH_LIMIT_EXCEEDED"
                )
    if not hash_coverage or any(count == 0 for count in hash_coverage):
        raise CliInstallConfigurationError("CLI_LOCKFILE_HASH_COVERAGE_INVALID")
    if any(
        any(not line.rstrip().endswith("\\") for line in group[:-1])
        or group[-1].rstrip().endswith("\\")
        for group in hash_groups
    ):
        raise CliInstallConfigurationError("CLI_LOCKFILE_CONTINUATION_INVALID")
    seen_distributions: set[str] = set()
    for requirement in requirements:
        if "==" not in requirement or not requirement.rstrip().endswith("\\"):
            raise CliInstallConfigurationError("CLI_LOCKFILE_REQUIREMENT_UNPINNED")
        if not REQUIREMENT_LINE.fullmatch(requirement):
            raise CliInstallConfigurationError("CLI_LOCKFILE_REQUIREMENT_UNSAFE")
        distribution = DISTRIBUTION_SEPARATOR.sub(
            "-", requirement.split("==", 1)[0].lower()
        )
        if distribution in seen_distributions:
            raise CliInstallConfigurationError("CLI_LOCKFILE_REQUIREMENT_DUPLICATE")
        seen_distributions.add(distribution)
    if any(not HASH_LINE.fullmatch(line) for line in hashes):
        raise CliInstallConfigurationError("CLI_LOCKFILE_HASH_INVALID")
    for group in hash_groups:
        digests = [line.split("sha256:", 1)[1].split()[0] for line in group]
        if len(digests) != len(set(digests)):
            raise CliInstallConfigurationError("CLI_LOCKFILE_HASH_DUPLICATE")


def validate_local_package(path: Path = LOCAL_PACKAGE) -> None:
    """Fail closed unless the fixed local package path is repository-owned."""

    if path.is_symlink() or not path.is_dir():
        raise CliInstallConfigurationError("CLI_LOCAL_PACKAGE_UNSAFE")
    try:
        path.resolve().relative_to(REPO_ROOT)
    except (OSError, ValueError) as exc:
        raise CliInstallConfigurationError("CLI_LOCAL_PACKAGE_OUTSIDE_REPOSITORY") from exc
    if not (path / "pyproject.toml").is_file():
        raise CliInstallConfigurationError("CLI_LOCAL_PACKAGE_METADATA_MISSING")


def build_commands(executable: str | None = None) -> tuple[tuple[str, ...], ...]:
    """Return the finite pip command sequence for the committed CLI package."""

    validate_lockfile()
    validate_local_package()
    python = executable or sys.executable
    return (
        (
            python,
            "-I",
            "-m",
            "pip",
            "install",
            "--disable-pip-version-check",
            "--no-input",
            "--require-hashes",
            "--requirement",
            str(LOCKFILE),
        ),
        (
            python,
            "-I",
            "-m",
            "pip",
            "install",
            "--disable-pip-version-check",
            "--no-input",
            "--no-deps",
            "--no-build-isolation",
            "--editable",
            LOCAL_SPEC,
        ),
    )


def install() -> None:
    """Install the committed CLI dependency overlay and local package."""

    environment = {
        key: value
        for key, value in os.environ.items()
        if not key.upper().startswith("PIP_")
        and key.upper() not in UNSAFE_PYTHON_ENVIRONMENT
    }
    environment["PIP_CONFIG_FILE"] = os.devnull
    environment["PIP_DISABLE_PIP_VERSION_CHECK"] = "1"
    environment["PIP_NO_INPUT"] = "1"
    environment["PYTHONNOUSERSITE"] = "1"
    deadline = time.monotonic() + INSTALL_TIMEOUT_SECONDS
    for command in build_commands():
        remaining_seconds = deadline - time.monotonic()
        if remaining_seconds <= 0:
            raise CliInstallConfigurationError("CLI_INSTALL_TIMEOUT")
        try:
            subprocess.run(
                command,
                check=True,
                cwd=REPO_ROOT,
                env=environment,
                shell=False,
                stdin=subprocess.DEVNULL,
                timeout=remaining_seconds,
            )
        except subprocess.TimeoutExpired as exc:
            raise CliInstallConfigurationError("CLI_INSTALL_TIMEOUT") from exc
        except subprocess.CalledProcessError as exc:
            raise CliInstallConfigurationError("CLI_INSTALL_COMMAND_FAILED") from exc
        except OSError as exc:
            raise CliInstallConfigurationError("CLI_INSTALL_EXECUTION_FAILED") from exc


def main(argv: Sequence[str] | None = None) -> int:
    if argv:
        raise CliInstallConfigurationError("CLI_INSTALLER_TAKES_NO_ARGUMENTS")
    install()
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
