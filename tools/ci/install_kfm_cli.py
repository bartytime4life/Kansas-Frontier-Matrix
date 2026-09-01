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
from pathlib import Path
from typing import Sequence


REPO_ROOT = Path(__file__).resolve().parents[2]
LOCKFILE = REPO_ROOT / "tools/ci/python-cli.lock"
LOCAL_PACKAGE = REPO_ROOT / "packages/kfm-cli"
LOCAL_SPEC = "./packages/kfm-cli"
LOCK_LIMIT_BYTES = 262_144
HASH_LINE = re.compile(r"^\s+--hash=sha256:[0-9a-f]{64}(?: \\)?$")
REQUIREMENT_LINE = re.compile(
    r"^[A-Za-z0-9][A-Za-z0-9._-]*==[A-Za-z0-9][A-Za-z0-9.!+_-]* \\$"
)
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
PIP_SOURCE_ENV_KEYS = (
    "PIP_EXTRA_INDEX_URL",
    "PIP_FIND_LINKS",
    "PIP_INDEX_URL",
    "PIP_TRUSTED_HOST",
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

    lines = text.splitlines()
    requirements = [
        line
        for line in lines
        if line and not line[0].isspace() and not line.startswith("#")
    ]
    hashes = [line for line in lines if "--hash=" in line]
    if not requirements:
        raise CliInstallConfigurationError("CLI_LOCKFILE_HASH_COVERAGE_INVALID")
    seen_requirement_names: set[str] = set()
    for requirement in requirements:
        if "==" not in requirement or not requirement.rstrip().endswith("\\"):
            raise CliInstallConfigurationError("CLI_LOCKFILE_REQUIREMENT_UNPINNED")
        if not REQUIREMENT_LINE.fullmatch(requirement):
            raise CliInstallConfigurationError("CLI_LOCKFILE_REQUIREMENT_UNSAFE")
        name = requirement.split("==", 1)[0]
        normalized_name = re.sub(r"[-_.]+", "-", name).lower()
        if normalized_name in seen_requirement_names:
            raise CliInstallConfigurationError("CLI_LOCKFILE_REQUIREMENT_DUPLICATE")
        seen_requirement_names.add(normalized_name)
    if any(not HASH_LINE.fullmatch(line) for line in hashes):
        raise CliInstallConfigurationError("CLI_LOCKFILE_HASH_INVALID")

    continuations = [
        line
        for line in lines
        if line
        and line[0].isspace()
        and line.strip()
        and not line.lstrip().startswith("#")
    ]
    if any(not HASH_LINE.fullmatch(line) for line in continuations):
        raise CliInstallConfigurationError("CLI_LOCKFILE_CONTINUATION_UNSAFE")

    in_requirement = False
    current_has_hash = False
    for line in lines:
        if not line or line.startswith("#"):
            continue
        if not line[0].isspace():
            if in_requirement and not current_has_hash:
                raise CliInstallConfigurationError(
                    "CLI_LOCKFILE_HASH_COVERAGE_INVALID"
                )
            in_requirement = True
            current_has_hash = False
            continue
        if "--hash=" in line:
            if not in_requirement:
                raise CliInstallConfigurationError(
                    "CLI_LOCKFILE_HASH_COVERAGE_INVALID"
                )
            current_has_hash = True
    if in_requirement and not current_has_hash:
        raise CliInstallConfigurationError("CLI_LOCKFILE_HASH_COVERAGE_INVALID")


def validate_local_package(path: Path = LOCAL_PACKAGE) -> None:
    """Fail closed unless the fixed local package path is repository-owned."""

    if path.is_symlink() or not path.is_dir():
        raise CliInstallConfigurationError("CLI_LOCAL_PACKAGE_UNSAFE")
    try:
        path.resolve().relative_to(REPO_ROOT)
    except (OSError, ValueError) as exc:
        raise CliInstallConfigurationError("CLI_LOCAL_PACKAGE_OUTSIDE_REPOSITORY") from exc
    metadata = path / "pyproject.toml"
    if metadata.is_symlink():
        raise CliInstallConfigurationError("CLI_LOCAL_PACKAGE_METADATA_UNSAFE")
    if not metadata.is_file():
        raise CliInstallConfigurationError("CLI_LOCAL_PACKAGE_METADATA_MISSING")


def build_commands(executable: str | None = None) -> tuple[tuple[str, ...], ...]:
    """Return the finite pip command sequence for the committed CLI package."""

    validate_lockfile()
    validate_local_package()
    python = executable or sys.executable
    return (
        (
            python,
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

    environment = os.environ.copy()
    for key in PIP_SOURCE_ENV_KEYS:
        environment.pop(key, None)
    environment["PIP_CONFIG_FILE"] = os.devnull
    environment["PIP_DISABLE_PIP_VERSION_CHECK"] = "1"
    environment["PIP_NO_INPUT"] = "1"
    for command in build_commands():
        subprocess.run(
            command,
            check=True,
            cwd=REPO_ROOT,
            env=environment,
            shell=False,
        )


def main(argv: Sequence[str] | None = None) -> int:
    if argv:
        raise CliInstallConfigurationError("CLI_INSTALLER_TAKES_NO_ARGUMENTS")
    install()
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
