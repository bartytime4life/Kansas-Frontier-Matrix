#!/usr/bin/env python3
"""Install fixed, hash-locked Python dependency profiles for KFM CI.

The profile names, lockfiles, and local package paths are repository constants.
Callers cannot supply a package name, index, URL, requirement path, or shell
fragment. Third-party dependencies are installed with pip hash enforcement;
approved local packages are installed without dependency resolution or build
isolation after their locked build backend is present.

This helper bootstraps CI dependencies only. It does not validate repository
content, decide policy, create evidence, approve release, or publish anything.
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Sequence


REPO_ROOT = Path(__file__).resolve().parents[2]
LOCK_LIMIT_BYTES = 1_048_576
HASH_LINE = re.compile(r"^\s+--hash=sha256:[0-9a-f]{64}(?: \\)?$")
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


class InstallConfigurationError(ValueError):
    """Raised when a committed install profile or lockfile is unsafe."""


@dataclass(frozen=True)
class InstallProfile:
    lockfile: str
    local_specs: tuple[str, ...] = ()
    editable: bool = True


PROFILES = {
    "all-local-test": InstallProfile(
        "tools/ci/python-test.lock",
        (
            ".[test]",
            "./packages/connectors-core[test]",
            "./packages/hashing[test]",
            "./packages/schema-registry[test]",
        ),
    ),
    "audit-tool": InstallProfile("tools/ci/python-audit.lock"),
    "connectors-core": InstallProfile(
        "tools/ci/python-test.lock", ("./packages/connectors-core",)
    ),
    "project-runtime": InstallProfile("tools/ci/python-test.lock", (".",)),
    "project-test": InstallProfile("tools/ci/python-test.lock", (".[test]",)),
    "project-test-hashing": InstallProfile(
        "tools/ci/python-test.lock", (".[test]", "./packages/hashing")
    ),
    "project-test-hashing-test": InstallProfile(
        "tools/ci/python-test.lock", (".[test]", "./packages/hashing[test]")
    ),
    "project-test-schema-registry-test": InstallProfile(
        "tools/ci/python-test.lock",
        (".[test]", "./packages/schema-registry[test]"),
    ),
    "project-test-wheel": InstallProfile(
        "tools/ci/python-test.lock", (".[test]",), editable=False
    ),
    "test-dependencies": InstallProfile("tools/ci/python-test.lock"),
}


def profiles_for_workflow(workflow_path: Path) -> frozenset[str]:
    """Return the fixed profiles invoked by one repository workflow."""

    if workflow_path.is_symlink() or not workflow_path.is_file():
        raise InstallConfigurationError("WORKFLOW_UNSAFE")
    try:
        workflow_path.resolve().relative_to(REPO_ROOT / ".github/workflows")
        text = workflow_path.read_text(encoding="utf-8")
    except (OSError, UnicodeError, ValueError) as exc:
        raise InstallConfigurationError("WORKFLOW_UNREADABLE") from exc
    marker = "python tools/ci/install_python_ci.py "
    profiles: set[str] = set()
    for line in text.splitlines():
        if marker not in line:
            continue
        profile_name = line.split(marker, 1)[1].strip()
        if profile_name == "verify-workflows":
            continue
        profiles.add(profile_name)
    if not profiles:
        return frozenset()
    if any(profile_name not in PROFILES for profile_name in profiles):
        raise InstallConfigurationError("PROFILE_UNKNOWN")
    return frozenset(profiles)


def verify_workflow_receipts() -> None:
    """Verify changed workflows through their immutable receipts plus new locks."""

    workflow_root = REPO_ROOT / ".github/workflows"
    workflows = sorted(workflow_root.glob("*.yml")) + sorted(
        workflow_root.glob("*.yaml")
    )
    locked_count = 0
    for workflow in workflows:
        profile_names = profiles_for_workflow(workflow)
        if not profile_names or workflow.name == "python-dependency-lock.yml":
            continue
        locked_count += 1
        prior_bytes = subprocess.run(
            (
                "git",
                "show",
                f"HEAD^:{workflow.relative_to(REPO_ROOT).as_posix()}",
            ),
            check=True,
            cwd=REPO_ROOT,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
        ).stdout
        old_prefix = b"python -m pip install"
        if old_prefix not in prior_bytes:
            raise InstallConfigurationError("PRIOR_WORKFLOW_INSTALL_MISSING")
        for profile_name in profile_names:
            profile = PROFILES[profile_name]
            validate_lockfile(_lock_path(profile))
            _validate_local_specs(profile)
    if locked_count < 1:
        raise InstallConfigurationError("WORKFLOW_MIGRATION_EMPTY")


def _lock_path(profile: InstallProfile) -> Path:
    path = REPO_ROOT / profile.lockfile
    if path.is_symlink() or not path.is_file():
        raise InstallConfigurationError("LOCKFILE_UNSAFE")
    try:
        size = path.stat().st_size
    except OSError as exc:
        raise InstallConfigurationError("LOCKFILE_UNREADABLE") from exc
    if size <= 0 or size > LOCK_LIMIT_BYTES:
        raise InstallConfigurationError("LOCKFILE_SIZE_INVALID")
    return path


def validate_lockfile(path: Path) -> None:
    """Fail closed unless every requirement is exact and SHA-256 hashed."""

    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as exc:
        raise InstallConfigurationError("LOCKFILE_UNREADABLE") from exc
    lowered = text.lower()
    if any(token in lowered for token in FORBIDDEN_LOCK_TEXT):
        raise InstallConfigurationError("LOCKFILE_SOURCE_UNSAFE")

    requirements = [
        line
        for line in text.splitlines()
        if line and not line[0].isspace() and not line.startswith("#")
    ]
    hashes = [line for line in text.splitlines() if "--hash=" in line]
    if not requirements or len(hashes) < len(requirements):
        raise InstallConfigurationError("LOCKFILE_HASH_COVERAGE_INVALID")
    for requirement in requirements:
        if "==" not in requirement or not requirement.rstrip().endswith("\\"):
            raise InstallConfigurationError("LOCKFILE_REQUIREMENT_UNPINNED")
    if any(not HASH_LINE.fullmatch(line) for line in hashes):
        raise InstallConfigurationError("LOCKFILE_HASH_INVALID")


def _validate_local_specs(profile: InstallProfile) -> None:
    for spec in profile.local_specs:
        path_text = spec.split("[", 1)[0]
        path = REPO_ROOT / path_text
        if path.is_symlink() or not path.is_dir():
            raise InstallConfigurationError("LOCAL_PACKAGE_UNSAFE")
        try:
            path.resolve().relative_to(REPO_ROOT)
        except (OSError, ValueError) as exc:
            raise InstallConfigurationError("LOCAL_PACKAGE_OUTSIDE_REPOSITORY") from exc
        if not (path / "pyproject.toml").is_file():
            raise InstallConfigurationError("LOCAL_PACKAGE_METADATA_MISSING")


def build_commands(
    profile_name: str, *, executable: str | None = None
) -> tuple[tuple[str, ...], ...]:
    """Return the finite pip command sequence for one named profile."""

    try:
        profile = PROFILES[profile_name]
    except KeyError as exc:
        raise InstallConfigurationError("PROFILE_UNKNOWN") from exc
    lockfile = _lock_path(profile)
    validate_lockfile(lockfile)
    _validate_local_specs(profile)
    python = executable or sys.executable
    commands: list[tuple[str, ...]] = [
        (
            python,
            "-m",
            "pip",
            "install",
            "--disable-pip-version-check",
            "--no-input",
            "--require-hashes",
            "--requirement",
            str(lockfile),
        )
    ]
    if profile.local_specs:
        local = [
            python,
            "-m",
            "pip",
            "install",
            "--disable-pip-version-check",
            "--no-input",
            "--no-deps",
            "--no-build-isolation",
        ]
        if profile.editable:
            for spec in profile.local_specs:
                local.extend(("--editable", spec))
        else:
            local.extend(profile.local_specs)
        commands.append(tuple(local))
    return tuple(commands)


def install(profile_name: str) -> None:
    environment = os.environ.copy()
    environment["PIP_DISABLE_PIP_VERSION_CHECK"] = "1"
    environment["PIP_NO_INPUT"] = "1"
    for command in build_commands(profile_name):
        subprocess.run(
            command,
            check=True,
            cwd=REPO_ROOT,
            env=environment,
            shell=False,
        )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("profile", choices=[*sorted(PROFILES), "verify-workflows"])
    args = parser.parse_args(argv)
    if args.profile == "verify-workflows":
        verify_workflow_receipts()
    else:
        install(args.profile)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
