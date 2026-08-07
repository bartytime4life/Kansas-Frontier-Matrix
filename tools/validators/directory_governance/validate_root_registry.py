#!/usr/bin/env python3
"""Validate the KFM root-registry projection without network access.

The register is JSON-compatible YAML so parsing stays deterministic with the
standard library. A PASS proves projection shape, adopted-doctrine binding,
root-class invariants, canonical ordering, and (when enabled) top-level root
coverage. It does not create or activate roots, authorize writes, migrate data,
or grant evidence, policy, review, release, deployment, or publication status.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
REGISTER_PATH = REPO_ROOT / "control_plane/root_registry.yaml"
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/governance/root_registry.schema.json"
DOCTRINE_PATH = REPO_ROOT / "docs/doctrine/directory-rules.md"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/governance/root_registry"

ADOPTED_DOCTRINE_SHA256 = "44f7e94344cb42b630008eb0bc03a13fcb97dbdfba6f3e56579693a272571e6e"
ADOPTED_DECISION = "ADR-0029"
MAX_FILE_BYTES = 4 * 1024 * 1024
MAX_SCHEMA_FINDINGS = 100
SCOPE = "root-registry-projection-only"

CANONICAL_ROOTS = (
    ".github/",
    "apps/",
    "configs/",
    "connectors/",
    "contracts/",
    "control_plane/",
    "data/",
    "docs/",
    "examples/",
    "fixtures/",
    "infra/",
    "migrations/",
    "packages/",
    "pipeline_specs/",
    "pipelines/",
    "policy/",
    "release/",
    "runtime/",
    "schemas/",
    "scripts/",
    "tests/",
    "tools/",
)
IGNORED_TOP_LEVEL_DIRS = {".git", ".pytest_cache", ".mypy_cache", ".ruff_cache", "__pycache__", ".venv", "venv"}


class DuplicateKeyError(ValueError):
    """Raised for duplicate JSON object members."""


class NonFiniteNumberError(ValueError):
    """Raised for JSON NaN or infinity."""


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

    @property
    def outcome(self) -> str:
        codes = {finding.code for finding in self.findings}
        if not codes:
            return "PASS"
        if any(code.startswith(("INPUT_", "JSON_", "SCHEMA_UNAVAILABLE", "REPO_ROOT_")) for code in codes):
            return "ERROR_VALIDATOR"
        if any(code in {"AUTHORITY_EVIDENCE_MISSING", "DECISION_EVIDENCE_MISSING"} for code in codes):
            return "HOLD_UNRESOLVED"
        if any(code in {"UNREGISTERED_ROOT", "REGISTERED_ACTIVE_ROOT_MISSING"} for code in codes):
            return "FAIL_NEW_DRIFT"
        return "FAIL_INVARIANT"


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def _reject_nonfinite(_value: str) -> None:
    raise NonFiniteNumberError


def _parse_finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _read_object(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("INPUT_NOT_FILE", "/")]
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [Finding("INPUT_TOO_LARGE", "/")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique_object,
            parse_constant=_reject_nonfinite,
            parse_float=_parse_finite_float,
        )
    except UnicodeDecodeError:
        return None, [Finding("JSON_NOT_UTF8", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_COMPATIBLE_YAML_REQUIRED", "/")]
    except OSError:
        return None, [Finding("INPUT_READ_ERROR", "/")]
    except (RecursionError, ValueError):
        return None, [Finding("JSON_COMPLEXITY_LIMIT", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
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
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    findings = [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in sorted(
            errors[:MAX_SCHEMA_FINDINGS],
            key=lambda item: (_pointer(item.absolute_path), str(item.validator)),
        )
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def _array(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def resolve_registry(candidate: Mapping[str, Any]) -> dict[str, Any]:
    """Expand normalized shared/class defaults into complete root entries."""
    entry_defaults = candidate.get("entry_defaults")
    class_defaults = candidate.get("class_defaults")
    if not isinstance(entry_defaults, Mapping) or not isinstance(class_defaults, Mapping):
        return dict(candidate)
    resolved_roots: list[Any] = []
    for raw in _array(candidate.get("roots")):
        if not isinstance(raw, Mapping):
            resolved_roots.append(raw)
            continue
        class_profile = class_defaults.get(raw.get("class"), {})
        merged: dict[str, Any] = dict(entry_defaults)
        if isinstance(class_profile, Mapping):
            merged.update(class_profile)
        merged.update(raw)
        resolved_roots.append(merged)
    resolved = dict(candidate)
    resolved["roots"] = resolved_roots
    return resolved


def _semantic_findings(
    candidate: Mapping[str, Any],
    *,
    enforce_doctrine_parity: bool,
) -> list[Finding]:
    findings: list[Finding] = []
    doctrine = candidate.get("doctrine")
    expected_digest = f"sha256:{ADOPTED_DOCTRINE_SHA256}"
    if not isinstance(doctrine, Mapping):
        return findings
    if doctrine.get("sha256") != expected_digest:
        findings.append(Finding("DOCTRINE_DIGEST_MISMATCH", "/doctrine/sha256"))
    if doctrine.get("decision_ref") != ADOPTED_DECISION:
        findings.append(Finding("DECISION_EVIDENCE_MISSING", "/doctrine/decision_ref"))

    roots = _array(candidate.get("roots"))
    root_ids = [entry.get("root_id") for entry in roots if isinstance(entry, Mapping)]
    paths = [entry.get("path") for entry in roots if isinstance(entry, Mapping)]
    if paths != sorted(paths):
        findings.append(Finding("ROOTS_NOT_CANONICAL", "/roots"))
    if len(root_ids) != len(set(root_ids)):
        findings.append(Finding("ROOT_ID_DUPLICATE", "/roots"))
    if len(paths) != len(set(paths)):
        findings.append(Finding("ROOT_PATH_DUPLICATE", "/roots"))

    by_path: dict[str, Mapping[str, Any]] = {}
    for index, raw in enumerate(roots):
        if not isinstance(raw, Mapping):
            continue
        path = raw.get("path")
        if isinstance(path, str):
            by_path[path] = raw
        base = f"/roots/{index}"
        allowed = _array(raw.get("allowed_artifact_kinds"))
        prohibited = _array(raw.get("prohibited_artifact_kinds"))
        if allowed != sorted(set(allowed)):
            findings.append(Finding("ALLOWED_KINDS_NOT_CANONICAL", f"{base}/allowed_artifact_kinds"))
        if prohibited != sorted(set(prohibited)):
            findings.append(Finding("PROHIBITED_KINDS_NOT_CANONICAL", f"{base}/prohibited_artifact_kinds"))
        if set(allowed) & set(prohibited):
            findings.append(Finding("ARTIFACT_KIND_CONFLICT", base))

        cls = raw.get("class")
        status = raw.get("status")
        target = raw.get("canonical_target")
        activation = _array(raw.get("activation_conditions"))
        exits = _array(raw.get("exit_conditions"))
        profiles = set(_array(raw.get("validation_profiles")))

        if raw.get("source_digest") != expected_digest:
            findings.append(Finding("ENTRY_SOURCE_DIGEST_MISMATCH", f"{base}/source_digest"))
        if ADOPTED_DECISION not in _array(raw.get("governing_decisions")):
            findings.append(Finding("DECISION_EVIDENCE_MISSING", f"{base}/governing_decisions"))

        if cls in {"canonical", "platform"}:
            if status != "ACTIVE":
                findings.append(Finding("ACTIVE_ROOT_STATUS_INVALID", f"{base}/status"))
            if target is not None:
                findings.append(Finding("CANONICAL_TARGET_FORBIDDEN", f"{base}/canonical_target"))
        elif cls == "conditional":
            if status not in {"PROPOSED", "ACCEPTED", "ACTIVE"}:
                findings.append(Finding("CONDITIONAL_STATUS_INVALID", f"{base}/status"))
            if not activation:
                findings.append(Finding("ACTIVATION_CONDITION_REQUIRED", f"{base}/activation_conditions"))
            if not exits:
                findings.append(Finding("EXIT_CONDITION_REQUIRED", f"{base}/exit_conditions"))
        elif cls == "compatibility":
            if target is None:
                findings.append(Finding("CANONICAL_TARGET_REQUIRED", f"{base}/canonical_target"))
            if not exits:
                findings.append(Finding("EXIT_CONDITION_REQUIRED", f"{base}/exit_conditions"))
            if "no_independent_writes" not in profiles:
                findings.append(Finding("SINGLE_WRITE_PROFILE_REQUIRED", f"{base}/validation_profiles"))
        elif cls == "deprecated":
            if status != "DEPRECATED":
                findings.append(Finding("DEPRECATED_STATUS_REQUIRED", f"{base}/status"))
            if target is None:
                findings.append(Finding("CANONICAL_TARGET_REQUIRED", f"{base}/canonical_target"))
            if not exits:
                findings.append(Finding("EXIT_CONDITION_REQUIRED", f"{base}/exit_conditions"))
            if "frozen_no_writes" not in profiles:
                findings.append(Finding("FROZEN_WRITE_PROFILE_REQUIRED", f"{base}/validation_profiles"))
        elif cls == "retired" and status != "RETIRED":
            findings.append(Finding("RETIRED_STATUS_REQUIRED", f"{base}/status"))

    if enforce_doctrine_parity:
        for expected in CANONICAL_ROOTS:
            entry = by_path.get(expected)
            field = f"/roots/{expected.replace('/', '~1')}"
            if entry is None:
                findings.append(Finding("CANONICAL_ROOT_MISSING", field))
                continue
            expected_class = "platform" if expected == ".github/" else "canonical"
            if entry.get("class") != expected_class:
                findings.append(Finding("CANONICAL_ROOT_CLASS_MISMATCH", field))
    return findings


def _repo_root_findings(candidate: Mapping[str, Any], repo_root: Path) -> list[Finding]:
    findings: list[Finding] = []
    try:
        resolved = repo_root.resolve(strict=True)
        observed = {
            f"{path.name}/"
            for path in resolved.iterdir()
            if path.is_dir() and path.name not in IGNORED_TOP_LEVEL_DIRS
        }
    except OSError:
        return [Finding("REPO_ROOT_UNAVAILABLE", "/repo_root")]

    roots = {
        entry.get("path"): entry
        for entry in _array(candidate.get("roots"))
        if isinstance(entry, Mapping) and isinstance(entry.get("path"), str)
    }
    registered_present = {
        path
        for path, entry in roots.items()
        if entry.get("status") != "RETIRED"
    }
    for path in sorted(observed - set(roots)):
        findings.append(Finding("UNREGISTERED_ROOT", f"/repo_roots/{path.rstrip('/')}"))
    for path in sorted(registered_present - observed):
        entry = roots[path]
        if entry.get("status") in {"ACTIVE", "DEPRECATED"}:
            findings.append(Finding("REGISTERED_ACTIVE_ROOT_MISSING", f"/repo_roots/{path.rstrip('/')}"))
    return findings


def validate_register(
    path: Path,
    *,
    repo_root: Path = REPO_ROOT,
    check_repo_roots: bool = True,
    enforce_doctrine_parity: bool = True,
) -> ValidationResult:
    candidate, findings = _read_object(path)
    if candidate is None:
        return ValidationResult(tuple(sorted(set(findings))))
    findings.extend(_schema_findings(candidate))
    if not findings:
        resolved = resolve_registry(candidate)
        findings.extend(_semantic_findings(resolved, enforce_doctrine_parity=enforce_doctrine_parity))
        if check_repo_roots:
            findings.extend(_repo_root_findings(resolved, repo_root))
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
            "findings": [{"code": item.code, "field": item.field} for item in result.findings],
            "outcome": result.outcome,
            "scope": SCOPE,
            "authority": {
                "creates_root": False,
                "activates_root": False,
                "authorizes_writes": False,
                "migrates_paths": False,
                "releases": False,
                "publishes": False,
            },
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def run_fixture_profile() -> int:
    try:
        manifest = json.loads((FIXTURE_ROOT / "expected_findings_manifest.json").read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return 2
    valid = sorted((FIXTURE_ROOT / "valid").glob("*.yaml"))
    invalid = sorted((FIXTURE_ROOT / "invalid").glob("*.yaml"))
    if not valid or not invalid or not isinstance(manifest, dict):
        return 2
    passed = True
    for path in valid:
        result = validate_register(
            path,
            check_repo_roots=False,
            enforce_doctrine_parity=False,
        )
        print(_serialize(path, result))
        passed = result.ok and passed
    for path in invalid:
        result = validate_register(
            path,
            check_repo_roots=False,
            enforce_doctrine_parity=False,
        )
        print(_serialize(path, result))
        expected = sorted(manifest.get(path.name, []))
        actual = sorted({finding.code for finding in result.findings})
        if result.ok or not expected or actual != expected:
            passed = False
            print(
                json.dumps(
                    {
                        "file": path.name,
                        "expected_codes": expected,
                        "actual_codes": actual,
                        "outcome": "FIXTURE_EXPECTATION_MISMATCH",
                    },
                    sort_keys=True,
                    separators=(",", ":"),
                ),
                file=sys.stderr,
            )
    return 0 if passed else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate the KFM root-registry projection.")
    parser.add_argument("path", nargs="?", default=str(REGISTER_PATH))
    parser.add_argument("--repo-root", default=str(REPO_ROOT))
    parser.add_argument("--skip-repo-roots", action="store_true")
    parser.add_argument("--skip-doctrine-parity", action="store_true")
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)

    if args.fixtures:
        return run_fixture_profile()

    result = validate_register(
        Path(args.path),
        repo_root=Path(args.repo_root),
        check_repo_roots=not args.skip_repo_roots,
        enforce_doctrine_parity=not args.skip_doctrine_parity,
    )
    print(_serialize(Path(args.path), result))
    if result.outcome == "PASS":
        return 0
    if result.outcome == "ERROR_VALIDATOR":
        return 2
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
