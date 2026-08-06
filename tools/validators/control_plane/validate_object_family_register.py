#!/usr/bin/env python3
"""Validate the KFM machine-readable object-family register without network access.

The `.yaml` register intentionally uses the JSON-compatible subset of YAML so the
validator can parse it deterministically with the Python standard library. A PASS
proves bounded shape, canonical ordering, declared-path placement, path existence,
and structural maturity classification only. It does not establish object-family
meaning, policy, evidence, review, release, deployment, or publication authority.
"""

from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path, PurePosixPath
from typing import Any, Iterable, Mapping

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
REGISTER_PATH = REPO_ROOT / "control_plane/object_family_register.yaml"
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/governance/object_family_register.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/governance/object_family_register"
MAX_FILE_BYTES = 2 * 1024 * 1024
MAX_SCHEMA_FINDINGS = 100
SCOPE = "object-family-register-navigation-and-structural-coverage-only"
PATH_ROLES = {
    "contract_paths": ("contracts/",),
    "schema_paths": ("schemas/contracts/v1/",),
    "policy_paths": ("policy/",),
    "fixture_paths": ("fixtures/",),
    "validator_paths": ("tools/validators/",),
    "test_paths": ("tests/",),
    "workflow_paths": (".github/workflows/",),
    "emitter_paths": ("apps/", "data/", "packages/", "pipelines/", "runtime/", "tools/"),
}


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


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


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError
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
            return None, [Finding("FILE_NOT_FOUND", "/")]
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        with path.open("r", encoding="utf-8") as stream:
            value = json.load(
                stream,
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
        return None, [Finding("FILE_READ_ERROR", "/")]
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
    truncated = len(errors) > MAX_SCHEMA_FINDINGS
    findings = [
        Finding("SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in sorted(errors[:MAX_SCHEMA_FINDINGS], key=lambda item: (_pointer(item.absolute_path), str(item.validator)))
    ]
    if truncated:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def _array(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _canonical_path(value: Any) -> PurePosixPath | None:
    if not isinstance(value, str) or not value or "\\" in value or value.startswith("/"):
        return None
    path = PurePosixPath(value)
    if str(path) != value or any(part in {"", ".", ".."} for part in path.parts):
        return None
    return path


def _expected_maturity(entry: Mapping[str, Any]) -> str:
    contracts = bool(_array(entry.get("contract_paths")))
    schemas = bool(_array(entry.get("schema_paths")))
    fixtures = bool(_array(entry.get("fixture_paths")))
    validators = bool(_array(entry.get("validator_paths")))
    tests = bool(_array(entry.get("test_paths")))
    workflows = bool(_array(entry.get("workflow_paths")))
    if contracts and schemas and fixtures and validators and tests and workflows:
        return "hardened"
    if contracts and schemas and fixtures and validators and tests:
        return "covered"
    if contracts and schemas and any((fixtures, validators, tests, workflows)):
        return "partial"
    return "seed"


def _semantic_findings(candidate: Mapping[str, Any], *, repo_root: Path, check_paths: bool) -> list[Finding]:
    findings: list[Finding] = []
    entries = _array(candidate.get("entries"))
    ids = [entry.get("family_id") for entry in entries if isinstance(entry, dict)]
    if ids != sorted(ids):
        findings.append(Finding("ENTRIES_NOT_CANONICAL", "/entries"))
    if len(ids) != len(set(ids)):
        findings.append(Finding("FAMILY_ID_DUPLICATE", "/entries"))

    try:
        resolved_root = repo_root.resolve(strict=True)
    except OSError:
        resolved_root = repo_root.resolve()
        if check_paths:
            findings.append(Finding("REPO_ROOT_INVALID", "/repo_root"))

    for index, raw_entry in enumerate(entries):
        if not isinstance(raw_entry, dict):
            continue
        field_base = f"/entries/{index}"
        if raw_entry.get("maturity") != _expected_maturity(raw_entry):
            findings.append(Finding("MATURITY_MISMATCH", f"{field_base}/maturity"))
        for role, prefixes in PATH_ROLES.items():
            values = _array(raw_entry.get(role))
            if values != sorted(set(values)):
                findings.append(Finding("PATHS_NOT_CANONICAL", f"{field_base}/{role}"))
            for item_index, value in enumerate(values):
                field = f"{field_base}/{role}/{item_index}"
                relative = _canonical_path(value)
                if relative is None:
                    findings.append(Finding("PATH_INVALID", field))
                    continue
                if not any(value.startswith(prefix) for prefix in prefixes):
                    findings.append(Finding("PATH_ROOT_MISMATCH", field))
                    continue
                if check_paths:
                    candidate_path = resolved_root.joinpath(*relative.parts)
                    try:
                        candidate_path.resolve(strict=True).relative_to(resolved_root)
                    except (OSError, ValueError):
                        findings.append(Finding("PATH_NOT_FOUND", field))
    return findings


def validate_register(path: Path, *, repo_root: Path = REPO_ROOT, check_paths: bool = True) -> ValidationResult:
    candidate, findings = _read_object(path)
    if candidate is None:
        return ValidationResult(tuple(sorted(set(findings))))
    findings.extend(_schema_findings(candidate))
    findings.extend(_semantic_findings(candidate, repo_root=repo_root, check_paths=check_paths))
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
            "outcome": "PASS" if result.ok else "FAIL",
            "scope": SCOPE,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def run_fixture_profile() -> int:
    try:
        manifest = json.loads((FIXTURE_ROOT / "expected_findings_manifest.json").read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return 1
    valid = sorted((FIXTURE_ROOT / "valid").glob("*.yaml"))
    invalid = sorted((FIXTURE_ROOT / "invalid").glob("*.yaml"))
    if not valid or not invalid or not isinstance(manifest, dict):
        return 1
    passed = True
    for path in valid:
        result = validate_register(path, check_paths=False)
        print(_serialize(path, result))
        passed = result.ok and passed
    for path in invalid:
        result = validate_register(path, check_paths=False)
        print(_serialize(path, result))
        expected = sorted(manifest.get(path.name, []))
        actual = sorted({finding.code for finding in result.findings})
        if result.ok or not expected or actual != expected:
            passed = False
            print(json.dumps({"file":path.name,"expected_codes":expected,"actual_codes":actual,"outcome":"FIXTURE_EXPECTATION_MISMATCH"}, sort_keys=True, separators=(",", ":")), file=sys.stderr)
    return 0 if passed else 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", nargs="?", default=str(REGISTER_PATH))
    parser.add_argument("--repo-root", default=str(REPO_ROOT))
    parser.add_argument("--skip-path-existence", action="store_true")
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        return run_fixture_profile()
    result = validate_register(Path(args.path), repo_root=Path(args.repo_root), check_paths=not args.skip_path_existence)
    print(_serialize(Path(args.path), result))
    return 0 if result.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
