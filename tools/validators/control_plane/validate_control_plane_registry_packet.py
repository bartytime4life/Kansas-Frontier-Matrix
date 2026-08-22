#!/usr/bin/env python3
"""Validate the normalized KFM control-plane registry packet without network.

A PASS proves bounded projection shape, packet membership, canonical ordering,
reference existence, and referenced-byte integrity only. It does not create
authority, activate sources, approve policy or review, resolve contradictions,
complete verification, change lifecycle/release state, or publish.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import subprocess
import sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path, PurePosixPath
from typing import Any, Iterable, Mapping, Sequence

import yaml
from jsonschema import Draft202012Validator, FormatChecker
from yaml.constructor import ConstructorError
from yaml.resolver import BaseResolver

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/governance/control_plane_registry.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/governance/control_plane_registry"
REGISTRY_PATHS = {
    "contradiction_register": REPO_ROOT / "control_plane/contradiction_register.yaml",
    "deprecation_register": REPO_ROOT / "control_plane/deprecation_register.yaml",
    "document_registry": REPO_ROOT / "control_plane/document_registry.yaml",
    "policy_gate_register": REPO_ROOT / "control_plane/policy_gate_register.yaml",
    "release_state_register": REPO_ROOT / "control_plane/release_state_register.yaml",
    "source_authority_register": REPO_ROOT / "control_plane/source_authority_register.yaml",
    "verification_backlog": REPO_ROOT / "control_plane/verification_backlog.yaml",
}
MAX_FILE_BYTES = 4 * 1024 * 1024
MAX_REFERENCED_FILE_BYTES = 64 * 1024 * 1024
MAX_SCHEMA_FINDINGS = 100
MAX_NODES = 100_000
GIT_TIMEOUT_SECONDS = 5
SCOPE = "seven-registry-projection-shape-reference-and-integrity-only"
REQUIRED_NON_EFFECTS = frozenset(
    {
        "does_not_activate_sources",
        "does_not_approve_policy",
        "does_not_create_authority",
        "does_not_release_deploy_or_publish",
        "does_not_replace_owning_objects",
    }
)


class UniqueKeyLoader(yaml.SafeLoader):
    """Safe loader with duplicate-key rejection and string date handling."""


def _construct_unique_mapping(
    loader: UniqueKeyLoader,
    node: yaml.nodes.MappingNode,
    deep: bool = False,
) -> dict[Any, Any]:
    mapping: dict[Any, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                "duplicate key",
                key_node.start_mark,
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueKeyLoader.add_constructor(
    BaseResolver.DEFAULT_MAPPING_TAG,
    _construct_unique_mapping,
)
for first_character, resolvers in list(UniqueKeyLoader.yaml_implicit_resolvers.items()):
    UniqueKeyLoader.yaml_implicit_resolvers[first_character] = [
        resolver
        for resolver in resolvers
        if resolver[0] != "tag:yaml.org,2002:timestamp"
    ]


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class ValidationResult:
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return not self.findings


def _walk_finite(value: Any) -> bool:
    pending = [value]
    visited = 0
    while pending:
        current = pending.pop()
        visited += 1
        if visited > MAX_NODES:
            return False
        if isinstance(current, float) and not math.isfinite(current):
            return False
        if isinstance(current, dict):
            pending.extend(current.keys())
            pending.extend(current.values())
        elif isinstance(current, list):
            pending.extend(current)
    return True


def _read_mapping(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("FILE_NOT_FOUND", "/")]
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        with path.open("r", encoding="utf-8") as stream:
            value = yaml.load(stream, Loader=UniqueKeyLoader)
    except UnicodeDecodeError:
        return None, [Finding("YAML_NOT_UTF8", "/")]
    except ConstructorError:
        return None, [Finding("YAML_DUPLICATE_KEY", "/")]
    except yaml.YAMLError:
        return None, [Finding("YAML_INVALID", "/")]
    except OSError:
        return None, [Finding("FILE_READ_ERROR", "/")]
    except (RecursionError, ValueError):
        return None, [Finding("YAML_COMPLEXITY_LIMIT", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    if not _walk_finite(value):
        return None, [Finding("YAML_NONFINITE_OR_COMPLEX", "/")]
    if not all(isinstance(key, str) for key in value):
        return None, [Finding("ROOT_KEY_NOT_STRING", "/")]
    return value, []


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        errors = list(islice(validator.iter_errors(candidate), MAX_SCHEMA_FINDINGS + 1))
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError, ValueError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    truncated = len(errors) > MAX_SCHEMA_FINDINGS
    findings = [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in sorted(
            errors[:MAX_SCHEMA_FINDINGS],
            key=lambda item: (_pointer(item.absolute_path), str(item.validator)),
        )
    ]
    if truncated:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def _array(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _mapping(value: Any) -> Mapping[str, Any]:
    return value if isinstance(value, dict) else {}


def _check_sorted_unique(
    values: Sequence[Any],
    *,
    field: str,
    findings: list[Finding],
    prefix: str,
) -> None:
    try:
        sorted_values = sorted(values)
        unique_count = len(set(values))
    except TypeError:
        return
    if len(values) != unique_count:
        findings.append(Finding(f"{prefix}_DUPLICATE", field))
    if list(values) != sorted_values:
        findings.append(Finding(f"{prefix}_NOT_CANONICAL", field))


def _canonical_path(value: Any) -> PurePosixPath | None:
    if not isinstance(value, str) or not value or "\\" in value or value.startswith("/"):
        return None
    path = PurePosixPath(value)
    if str(path) != value or any(part in {"", ".", ".."} for part in path.parts):
        return None
    return path


def _resolve_path(
    value: Any,
    *,
    repo_root: Path,
    field: str,
    findings: list[Finding],
) -> Path | None:
    relative = _canonical_path(value)
    if relative is None:
        findings.append(Finding("PATH_INVALID", field))
        return None
    try:
        resolved_root = repo_root.resolve(strict=True)
        unresolved = resolved_root.joinpath(*relative.parts)
        if unresolved.is_symlink():
            findings.append(Finding("PATH_SYMLINK_DENIED", field))
            return None
        resolved = unresolved.resolve(strict=True)
        resolved.relative_to(resolved_root)
    except (OSError, ValueError):
        findings.append(Finding("PATH_NOT_FOUND", field))
        return None
    if not resolved.is_file():
        findings.append(Finding("PATH_NOT_FILE", field))
        return None
    return resolved


def _git_commit_status(repo_root: Path, base_ref: str) -> bool | None:
    try:
        completed = subprocess.run(
            ["git", "cat-file", "-e", f"{base_ref}^{{commit}}"],
            cwd=repo_root,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            timeout=GIT_TIMEOUT_SECONDS,
            check=False,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    return completed.returncode == 0


def _pinned_ref(
    candidate: Mapping[str, Any],
    *,
    repo_root: Path,
    check_git: bool,
    findings: list[Finding],
) -> str | None:
    if not check_git:
        return None
    base_ref = candidate.get("base_ref")
    if not isinstance(base_ref, str):
        return ""
    status = _git_commit_status(repo_root, base_ref)
    if status is None:
        findings.append(Finding("GIT_CHECK_UNAVAILABLE", "/base_ref"))
        return ""
    if not status:
        findings.append(Finding("BASE_COMMIT_NOT_FOUND", "/base_ref"))
        return ""
    return base_ref


def _read_pinned_blob(
    value: Any,
    *,
    base_ref: str,
    repo_root: Path,
    field: str,
    findings: list[Finding],
) -> bytes | None:
    relative = _canonical_path(value)
    if relative is None:
        findings.append(Finding("PATH_INVALID", field))
        return None
    object_name = f"{base_ref}:{relative.as_posix()}"
    try:
        tree_result = subprocess.run(
            ["git", "ls-tree", "-z", base_ref, "--", relative.as_posix()],
            cwd=repo_root,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            timeout=GIT_TIMEOUT_SECONDS,
            check=False,
        )
    except (OSError, subprocess.SubprocessError):
        findings.append(Finding("GIT_CHECK_UNAVAILABLE", field))
        return None
    records = [record for record in tree_result.stdout.split(b"\0") if record]
    if tree_result.returncode != 0 or not records:
        findings.append(Finding("PINNED_PATH_NOT_FOUND", field))
        return None
    try:
        metadata, returned_path = records[0].split(b"\t", 1)
        mode, object_type, _object_id = metadata.split(b" ", 2)
        returned = returned_path.decode("utf-8")
    except (UnicodeError, ValueError, IndexError):
        findings.append(Finding("PINNED_PATH_READ_ERROR", field))
        return None
    if len(records) != 1 or returned != relative.as_posix():
        findings.append(Finding("PINNED_PATH_READ_ERROR", field))
        return None
    if object_type != b"blob":
        findings.append(Finding("PATH_NOT_FILE", field))
        return None
    if mode not in {b"100644", b"100755"}:
        findings.append(Finding("PATH_SYMLINK_DENIED", field))
        return None
    try:
        size_result = subprocess.run(
            ["git", "cat-file", "-s", object_name],
            cwd=repo_root,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            timeout=GIT_TIMEOUT_SECONDS,
            check=False,
        )
    except (OSError, subprocess.SubprocessError):
        findings.append(Finding("GIT_CHECK_UNAVAILABLE", field))
        return None
    if size_result.returncode != 0:
        findings.append(Finding("PINNED_PATH_NOT_FOUND", field))
        return None
    try:
        size = int(size_result.stdout.decode("ascii").strip())
    except (UnicodeError, ValueError):
        findings.append(Finding("PINNED_PATH_READ_ERROR", field))
        return None
    if size < 0 or size > MAX_REFERENCED_FILE_BYTES:
        findings.append(Finding("REFERENCED_FILE_TOO_LARGE", field))
        return None
    try:
        blob_result = subprocess.run(
            ["git", "cat-file", "blob", object_name],
            cwd=repo_root,
            stdin=subprocess.DEVNULL,
            stdout=subprocess.PIPE,
            stderr=subprocess.DEVNULL,
            timeout=GIT_TIMEOUT_SECONDS,
            check=False,
        )
    except (OSError, subprocess.SubprocessError):
        findings.append(Finding("GIT_CHECK_UNAVAILABLE", field))
        return None
    if blob_result.returncode != 0 or len(blob_result.stdout) != size:
        findings.append(Finding("PINNED_PATH_READ_ERROR", field))
        return None
    return blob_result.stdout


def _check_reference(
    value: Any,
    *,
    repo_root: Path,
    pinned_ref: str | None,
    field: str,
    findings: list[Finding],
) -> None:
    if pinned_ref is not None:
        if pinned_ref:
            _read_pinned_blob(
                value,
                base_ref=pinned_ref,
                repo_root=repo_root,
                field=field,
                findings=findings,
            )
        return
    _resolve_path(value, repo_root=repo_root, field=field, findings=findings)


def _check_digest(
    value: Any,
    expected: Any,
    *,
    repo_root: Path,
    pinned_ref: str | None,
    field: str,
    findings: list[Finding],
) -> None:
    if not isinstance(expected, str) or not expected.startswith("sha256:"):
        return
    if pinned_ref is not None:
        if not pinned_ref:
            return
        content = _read_pinned_blob(
            value,
            base_ref=pinned_ref,
            repo_root=repo_root,
            field=field.removesuffix("_sha256"),
            findings=findings,
        )
        if content is None:
            return
    else:
        path = _resolve_path(
            value,
            repo_root=repo_root,
            field=field.removesuffix("_sha256"),
            findings=findings,
        )
        if path is None:
            return
        try:
            if path.stat().st_size > MAX_REFERENCED_FILE_BYTES:
                findings.append(Finding("REFERENCED_FILE_TOO_LARGE", field))
                return
            content = path.read_bytes()
        except OSError:
            findings.append(Finding("PATH_READ_ERROR", field))
            return
    actual = "sha256:" + hashlib.sha256(content).hexdigest()
    if actual != expected:
        findings.append(Finding("DIGEST_MISMATCH", field))


def _semantic_findings(
    candidate: Mapping[str, Any],
    *,
    expected_registry_id: str | None,
    repo_root: Path,
    check_paths: bool,
    check_git: bool,
) -> list[Finding]:
    findings: list[Finding] = []
    pinned_ref = _pinned_ref(
        candidate,
        repo_root=repo_root,
        check_git=check_git,
        findings=findings,
    )
    registry_id = candidate.get("registry_id")
    if expected_registry_id is not None and registry_id != expected_registry_id:
        findings.append(Finding("REGISTRY_FILE_ID_MISMATCH", "/registry_id"))

    meta = _mapping(candidate.get("meta"))
    if meta.get("owner") != candidate.get("owner_role"):
        findings.append(Finding("OWNER_PROJECTION_MISMATCH", "/owner_role"))

    non_effects = _array(candidate.get("non_effects"))
    _check_sorted_unique(
        non_effects,
        field="/non_effects",
        findings=findings,
        prefix="NON_EFFECTS",
    )
    if not REQUIRED_NON_EFFECTS.issubset(set(non_effects)):
        findings.append(Finding("REQUIRED_NON_EFFECT_MISSING", "/non_effects"))

    entries = _array(candidate.get("entries"))
    entry_ids = [entry.get("entry_id") for entry in entries if isinstance(entry, dict)]
    _check_sorted_unique(
        entry_ids,
        field="/entries",
        findings=findings,
        prefix="ENTRY_ID",
    )

    doctrine_refs = _array(meta.get("related_doctrine"))
    _check_sorted_unique(
        doctrine_refs,
        field="/meta/related_doctrine",
        findings=findings,
        prefix="DOCTRINE_REFS",
    )

    for index, raw_entry in enumerate(entries):
        if not isinstance(raw_entry, dict):
            continue
        field = f"/entries/{index}"
        governing_refs = _array(raw_entry.get("governing_refs"))
        source_digests = _array(raw_entry.get("source_digests"))
        reason_codes = _array(raw_entry.get("reason_codes"))
        _check_sorted_unique(
            governing_refs,
            field=f"{field}/governing_refs",
            findings=findings,
            prefix="GOVERNING_REFS",
        )
        _check_sorted_unique(
            source_digests,
            field=f"{field}/source_digests",
            findings=findings,
            prefix="SOURCE_DIGESTS",
        )
        _check_sorted_unique(
            reason_codes,
            field=f"{field}/reason_codes",
            findings=findings,
            prefix="REASON_CODES",
        )
        if raw_entry.get("authority_status") in {"CONFIRMED", "CONFLICTED"}:
            if not governing_refs or not source_digests:
                findings.append(
                    Finding(
                        "MATERIAL_AUTHORITY_EVIDENCE_MISSING",
                        field,
                    )
                )
        if check_paths:
            _check_digest(
                raw_entry.get("path"),
                raw_entry.get("path_sha256"),
                repo_root=repo_root,
                pinned_ref=pinned_ref,
                field=f"{field}/path_sha256",
                findings=findings,
            )
            for ref_index, value in enumerate(governing_refs):
                _check_reference(
                    value,
                    repo_root=repo_root,
                    pinned_ref=pinned_ref,
                    field=f"{field}/governing_refs/{ref_index}",
                    findings=findings,
                )

    if check_paths:
        for index, value in enumerate(doctrine_refs):
            _check_reference(
                value,
                repo_root=repo_root,
                pinned_ref=pinned_ref,
                field=f"/meta/related_doctrine/{index}",
                findings=findings,
            )
    return findings


def validate_registry(
    path: Path,
    *,
    expected_registry_id: str | None = None,
    repo_root: Path = REPO_ROOT,
    check_paths: bool = True,
    check_git: bool = True,
) -> ValidationResult:
    candidate, findings = _read_mapping(path)
    if candidate is None:
        return ValidationResult(tuple(sorted(set(findings))))
    findings.extend(_schema_findings(candidate))
    findings.extend(
        _semantic_findings(
            candidate,
            expected_registry_id=expected_registry_id,
            repo_root=repo_root,
            check_paths=check_paths,
            check_git=check_git,
        )
    )
    return ValidationResult(tuple(sorted(set(findings))))


def _display(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()
    except (OSError, ValueError):
        return path.name


def _serialize(path: Path, result: ValidationResult) -> str:
    return json.dumps(
        {
            "file": _display(path),
            "findings": [
                {"code": finding.code, "field": finding.field}
                for finding in result.findings
            ],
            "outcome": "PASS" if result.ok else "FAIL",
            "scope": SCOPE,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def validate_packet() -> int:
    passed = True
    for registry_id, path in sorted(REGISTRY_PATHS.items()):
        result = validate_registry(path, expected_registry_id=registry_id)
        print(_serialize(path, result))
        passed = result.ok and passed
    return 0 if passed else 1


def run_fixture_profile() -> int:
    try:
        manifest = json.loads(
            (FIXTURE_ROOT / "expected_findings_manifest.json").read_text(encoding="utf-8")
        )
    except (OSError, UnicodeError, json.JSONDecodeError):
        return 1
    valid = sorted((FIXTURE_ROOT / "valid").glob("*.yaml"))
    invalid = sorted((FIXTURE_ROOT / "invalid").glob("*.yaml"))
    if not valid or not invalid or not isinstance(manifest, dict):
        return 1
    passed = True
    for path in valid:
        result = validate_registry(path, check_paths=True, check_git=False)
        print(_serialize(path, result))
        passed = result.ok and passed
    for path in invalid:
        result = validate_registry(path, check_paths=True, check_git=False)
        print(_serialize(path, result))
        expected = sorted(manifest.get(path.name, []))
        actual = sorted({finding.code for finding in result.findings})
        if result.ok or not expected or actual != expected:
            passed = False
            print(
                json.dumps(
                    {
                        "actual_codes": actual,
                        "expected_codes": expected,
                        "file": path.name,
                        "outcome": "FIXTURE_EXPECTATION_MISMATCH",
                    },
                    sort_keys=True,
                    separators=(",", ":"),
                ),
                file=sys.stderr,
            )
    return 0 if passed else 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*")
    parser.add_argument("--repo-root", default=str(REPO_ROOT))
    parser.add_argument("--skip-path-existence", action="store_true")
    parser.add_argument("--skip-git-commit", action="store_true")
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        return run_fixture_profile()
    if not args.paths:
        return validate_packet()
    passed = True
    for raw_path in args.paths:
        path = Path(raw_path)
        result = validate_registry(
            path,
            repo_root=Path(args.repo_root),
            check_paths=not args.skip_path_existence,
            check_git=not args.skip_git_commit,
        )
        print(_serialize(path, result))
        passed = result.ok and passed
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
