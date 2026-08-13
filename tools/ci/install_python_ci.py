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
import hashlib
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path, PurePosixPath
from typing import Any, Sequence


REPO_ROOT = Path(__file__).resolve().parents[2]
LOCK_LIMIT_BYTES = 1_048_576
MIGRATION_MANIFEST = "tools/ci/python-dependency-lock-migration.json"
MIGRATION_SCHEMA = "kfm.python-dependency-lock-migration.v1"
MIGRATION_ID = "scorecard-pinned-dependencies-20260812"
MIGRATION_ENTRY_COUNT = 387
HASH_LINE = re.compile(r"^\s+--hash=sha256:[0-9a-f]{64}(?: \\)?$")
FULL_SHA256 = re.compile(r"^sha256:[0-9a-f]{64}$")
RECEIPT_SHA256 = re.compile(r"^sha256:[0-9a-f]{32,64}$")
COMMIT_SHA = re.compile(r"^[0-9a-f]{40}$")
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


class DuplicateKeyError(ValueError):
    """Raised when a migration manifest repeats an object member."""


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError(key)
        value[key] = item
    return value


def _sha256_bytes(raw: bytes) -> str:
    return "sha256:" + hashlib.sha256(raw).hexdigest()


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


def load_workflow_migration_manifest(
    repo_root: Path = REPO_ROOT,
) -> tuple[dict[str, Any], dict[str, dict[str, Any]]]:
    """Load and strictly validate the one-time workflow migration ledger."""

    path = repo_root / MIGRATION_MANIFEST
    if path.is_symlink() or not path.is_file():
        raise InstallConfigurationError("MIGRATION_MANIFEST_UNSAFE")
    try:
        if not 0 < path.stat().st_size <= LOCK_LIMIT_BYTES:
            raise InstallConfigurationError("MIGRATION_MANIFEST_SIZE_INVALID")
        value = json.loads(
            path.read_text(encoding="utf-8"), object_pairs_hook=_unique_object
        )
    except InstallConfigurationError:
        raise
    except (OSError, UnicodeError, ValueError, DuplicateKeyError) as exc:
        raise InstallConfigurationError("MIGRATION_MANIFEST_INVALID") from exc
    if not isinstance(value, dict) or set(value) != {
        "schema_version",
        "migration_id",
        "base_commit",
        "entries",
    }:
        raise InstallConfigurationError("MIGRATION_MANIFEST_SHAPE_INVALID")
    if value["schema_version"] != MIGRATION_SCHEMA:
        raise InstallConfigurationError("MIGRATION_SCHEMA_INVALID")
    if value["migration_id"] != MIGRATION_ID:
        raise InstallConfigurationError("MIGRATION_ID_INVALID")
    if not isinstance(value["base_commit"], str) or not COMMIT_SHA.fullmatch(
        value["base_commit"]
    ):
        raise InstallConfigurationError("MIGRATION_BASE_INVALID")
    entries = value["entries"]
    if not isinstance(entries, list) or len(entries) != MIGRATION_ENTRY_COUNT:
        raise InstallConfigurationError("MIGRATION_ENTRY_COUNT_INVALID")

    by_path: dict[str, dict[str, Any]] = {}
    prior_path = ""
    for entry in entries:
        if not isinstance(entry, dict) or set(entry) != {
            "path",
            "base_sha256",
            "current_sha256",
            "profiles",
            "superseded_receipt_sha256s",
        }:
            raise InstallConfigurationError("MIGRATION_ENTRY_SHAPE_INVALID")
        workflow_path = entry["path"]
        parsed = PurePosixPath(workflow_path) if isinstance(workflow_path, str) else None
        if (
            parsed is None
            or parsed.is_absolute()
            or parsed.as_posix() != workflow_path
            or len(parsed.parts) != 3
            or parsed.parts[:2] != (".github", "workflows")
            or parsed.suffix not in {".yml", ".yaml"}
            or workflow_path <= prior_path
        ):
            raise InstallConfigurationError("MIGRATION_PATH_INVALID")
        prior_path = workflow_path
        if not isinstance(entry["base_sha256"], str) or not FULL_SHA256.fullmatch(
            entry["base_sha256"]
        ):
            raise InstallConfigurationError("MIGRATION_BASE_HASH_INVALID")
        if not isinstance(entry["current_sha256"], str) or not FULL_SHA256.fullmatch(
            entry["current_sha256"]
        ):
            raise InstallConfigurationError("MIGRATION_CURRENT_HASH_INVALID")
        profiles = entry["profiles"]
        if (
            not isinstance(profiles, list)
            or not profiles
            or profiles != sorted(set(profiles))
            or any(profile not in PROFILES for profile in profiles)
        ):
            raise InstallConfigurationError("MIGRATION_PROFILES_INVALID")
        superseded = entry["superseded_receipt_sha256s"]
        if (
            not isinstance(superseded, list)
            or superseded != sorted(set(superseded))
            or any(
                not isinstance(item, str) or not RECEIPT_SHA256.fullmatch(item)
                for item in superseded
            )
        ):
            raise InstallConfigurationError("MIGRATION_RECEIPT_HASHES_INVALID")
        by_path[workflow_path] = entry
    return value, by_path


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

    manifest, entries = load_workflow_migration_manifest()
    base_commit = manifest["base_commit"]
    migration_head = os.environ.get("KFM_MIGRATION_HEAD", "")
    if not COMMIT_SHA.fullmatch(migration_head):
        raise InstallConfigurationError("MIGRATION_HEAD_INVALID")
    subprocess.run(
        ("git", "merge-base", "--is-ancestor", base_commit, migration_head),
        check=True,
        cwd=REPO_ROOT,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    for workflow_path, entry in entries.items():
        workflow = REPO_ROOT / workflow_path
        profile_names = profiles_for_workflow(workflow)
        if profile_names != frozenset(entry["profiles"]):
            raise InstallConfigurationError("MIGRATION_PROFILE_MISMATCH")
        prior_bytes = subprocess.run(
            (
                "git",
                "show",
                f"{base_commit}:{workflow_path}",
            ),
            check=True,
            cwd=REPO_ROOT,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
        ).stdout
        if _sha256_bytes(prior_bytes) != entry["base_sha256"]:
            raise InstallConfigurationError("MIGRATION_BASE_HASH_MISMATCH")
        old_prefix = b"python -m pip install"
        if old_prefix not in prior_bytes:
            raise InstallConfigurationError("PRIOR_WORKFLOW_INSTALL_MISSING")
        current_bytes = workflow.read_bytes()
        if _sha256_bytes(current_bytes) != entry["current_sha256"]:
            raise InstallConfigurationError("MIGRATION_CURRENT_HASH_MISMATCH")
        if old_prefix in current_bytes:
            raise InstallConfigurationError("MIGRATION_INSTALL_UNCHANGED")
        for profile_name in profile_names:
            profile = PROFILES[profile_name]
            validate_lockfile(_lock_path(profile))
            _validate_local_specs(profile)


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
