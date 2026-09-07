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
GIT_OPERATION_TIMEOUT_SECONDS = 30
GIT_REPOSITORY_CONTEXT_VARIABLES = (
    "GIT_ALTERNATE_OBJECT_DIRECTORIES",
    "GIT_CEILING_DIRECTORIES",
    "GIT_COMMON_DIR",
    "GIT_DIR",
    "GIT_DISCOVERY_ACROSS_FILESYSTEM",
    "GIT_INDEX_FILE",
    "GIT_OBJECT_DIRECTORY",
    "GIT_REPLACE_REF_BASE",
    "GIT_WORK_TREE",
)
HASH_LINE = re.compile(r"^\s+--hash=sha256:[0-9a-f]{64}(?: \\)?$")
FULL_SHA256 = re.compile(r"^sha256:[0-9a-f]{64}$")
RECEIPT_SHA256 = re.compile(r"^sha256:[0-9a-f]{32,64}$")
COMMIT_SHA = re.compile(r"^[0-9a-f]{40}$")
WORKFLOW_PROFILE_INVOCATION = re.compile(
    r"(?P<profile>[a-z0-9][a-z0-9-]*)"
    r'(?:\s+2>&1\s+\|\s+tee\s+"\$RUNNER_TEMP/'
    r'(?P<log_path>[A-Za-z0-9._/-]+)")?'
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


def _repository_git_environment() -> dict[str, str]:
    environment = {
        key: value for key, value in os.environ.items() if not key.startswith("GIT_")
    }
    environment["GIT_NO_REPLACE_OBJECTS"] = "1"
    return environment


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
    "geoparquet-pyarrow-25": InstallProfile(
        "tools/ci/geoparquet-pyarrow-25.lock"
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
        raw = workflow_path.read_bytes()
    except (OSError, UnicodeError, ValueError) as exc:
        raise InstallConfigurationError("WORKFLOW_UNREADABLE") from exc
    return _profiles_for_workflow_bytes(raw)


def _profiles_for_workflow_bytes(raw: bytes) -> frozenset[str]:
    try:
        text = raw.decode("utf-8")
    except UnicodeError as exc:
        raise InstallConfigurationError("WORKFLOW_UNREADABLE") from exc
    marker = "python tools/ci/install_python_ci.py "
    profiles: set[str] = set()
    for line in text.splitlines():
        if marker not in line:
            continue
        prefix, invocation = line.split(marker, 1)
        stripped_prefix = prefix.strip()
        if stripped_prefix.startswith("#"):
            continue
        if stripped_prefix not in {"", "run:", "- run:"}:
            raise InstallConfigurationError("WORKFLOW_PROFILE_INVOCATION_INVALID")
        invocation = invocation.lstrip()
        match = WORKFLOW_PROFILE_INVOCATION.fullmatch(invocation)
        if match is not None and match.group("log_path") is not None:
            if any(
                part in {"", ".", ".."}
                for part in match.group("log_path").split("/")
            ):
                match = None
        profile_name = match.group("profile") if match is not None else ""
        if profile_name == "verify-workflows":
            continue
        profiles.add(profile_name)
    if not profiles:
        return frozenset()
    if any(profile_name not in PROFILES for profile_name in profiles):
        raise InstallConfigurationError("PROFILE_UNKNOWN")
    return frozenset(profiles)


def _read_commit_workflows(
    commit_sha: str, workflow_paths: Sequence[str]
) -> dict[str, bytes]:
    """Read workflow blobs from one exact commit in a single Git process."""

    specs = [f"{commit_sha}:{path}" for path in workflow_paths]
    try:
        result = subprocess.run(
            ("git", "cat-file", "--batch"),
            check=True,
            cwd=REPO_ROOT,
            input=("\n".join(specs) + "\n").encode("ascii"),
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            env=_repository_git_environment(),
            timeout=GIT_OPERATION_TIMEOUT_SECONDS,
        )
    except (OSError, subprocess.CalledProcessError, subprocess.TimeoutExpired) as exc:
        raise InstallConfigurationError("MIGRATION_GIT_READ_FAILED") from exc

    raw = result.stdout
    offset = 0
    workflows: dict[str, bytes] = {}
    for workflow_path in workflow_paths:
        header_end = raw.find(b"\n", offset)
        if header_end < 0:
            raise InstallConfigurationError("MIGRATION_GIT_OUTPUT_INVALID")
        header = raw[offset:header_end].split()
        if (
            len(header) != 3
            or header[1] != b"blob"
            or not header[2].isdigit()
        ):
            raise InstallConfigurationError("MIGRATION_GIT_OUTPUT_INVALID")
        size = int(header[2])
        start = header_end + 1
        end = start + size
        if end >= len(raw) or raw[end : end + 1] != b"\n":
            raise InstallConfigurationError("MIGRATION_GIT_OUTPUT_INVALID")
        workflows[workflow_path] = raw[start:end]
        offset = end + 1
    if offset != len(raw):
        raise InstallConfigurationError("MIGRATION_GIT_OUTPUT_INVALID")
    return workflows


def _require_migration_ancestry(base_commit: str, migration_head: str) -> None:
    try:
        subprocess.run(
            ("git", "merge-base", "--is-ancestor", base_commit, migration_head),
            check=True,
            cwd=REPO_ROOT,
            env=_repository_git_environment(),
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=GIT_OPERATION_TIMEOUT_SECONDS,
        )
    except subprocess.CalledProcessError as exc:
        raise InstallConfigurationError("MIGRATION_ANCESTRY_INVALID") from exc
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise InstallConfigurationError("MIGRATION_GIT_READ_FAILED") from exc


def verify_workflow_receipts() -> None:
    """Verify changed workflows through their immutable receipts plus new locks."""

    manifest, entries = load_workflow_migration_manifest()
    base_commit = manifest["base_commit"]
    migration_head = os.environ.get("KFM_MIGRATION_HEAD", "")
    if not COMMIT_SHA.fullmatch(migration_head):
        raise InstallConfigurationError("MIGRATION_HEAD_INVALID")
    _require_migration_ancestry(base_commit, migration_head)
    workflow_paths = tuple(entries)
    base_workflows = _read_commit_workflows(base_commit, workflow_paths)
    head_workflows = _read_commit_workflows(migration_head, workflow_paths)
    current_hash_mismatches: list[str] = []
    validated_profiles: set[str] = set()
    for workflow_path, entry in entries.items():
        current_bytes = head_workflows[workflow_path]
        profile_names = _profiles_for_workflow_bytes(current_bytes)
        if profile_names != frozenset(entry["profiles"]):
            raise InstallConfigurationError("MIGRATION_PROFILE_MISMATCH")
        prior_bytes = base_workflows[workflow_path]
        if _sha256_bytes(prior_bytes) != entry["base_sha256"]:
            raise InstallConfigurationError("MIGRATION_BASE_HASH_MISMATCH")
        old_prefix = b"python -m pip install"
        if old_prefix not in prior_bytes:
            raise InstallConfigurationError("PRIOR_WORKFLOW_INSTALL_MISSING")
        if _sha256_bytes(current_bytes) != entry["current_sha256"]:
            current_hash_mismatches.append(workflow_path)
        if old_prefix in current_bytes:
            raise InstallConfigurationError("MIGRATION_INSTALL_UNCHANGED")
        for profile_name in sorted(profile_names - validated_profiles):
            profile = PROFILES[profile_name]
            validate_lockfile(_lock_path(profile))
            _validate_local_specs(profile)
            validated_profiles.add(profile_name)
    if current_hash_mismatches:
        raise InstallConfigurationError(
            "MIGRATION_CURRENT_HASH_MISMATCH:"
            + ",".join(current_hash_mismatches)
        )


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
