#!/usr/bin/env python3
"""Validate inactive KFM pipeline-spec declarations without network access.

A pass proves bounded declaration shape, deterministic identity, reference
existence, and fail-closed execution posture only. It does not activate a
source or pipeline, write a lifecycle target, close evidence, approve policy,
promote, release, deploy, or publish.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
import sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path, PurePosixPath
from typing import Any, Iterable, Mapping, Sequence

import yaml
from jsonschema import Draft202012Validator, FormatChecker
from yaml.constructor import ConstructorError
from yaml.resolver import BaseResolver
from yaml.tokens import AliasToken, AnchorToken

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/pipeline_spec_declaration.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/pipeline_spec_declaration"
PIPELINE_SPEC_ROOT = REPO_ROOT / "pipeline_specs"
MAX_FILE_BYTES = 1024 * 1024
MAX_NODES = 20_000
MAX_SCHEMA_FINDINGS = 50
REFERENCE_ARRAYS = (
    "source_descriptor_refs",
    "contract_refs",
    "schema_refs",
    "implementation_refs",
    "fixture_refs",
    "test_refs",
    "workflow_refs",
)
DENIED_EXECUTION_FIELDS = (
    "network_access",
    "source_activation",
    "lifecycle_write",
    "promotion",
    "release",
    "publication",
)


class UniqueKeyLoader(yaml.SafeLoader):
    """Safe YAML loader with duplicate-key denial and timestamps as strings."""


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
    path: str
    code: str
    field: str


@dataclass(frozen=True)
class ValidationResult:
    findings: tuple[Finding, ...]
    checked_count: int = 1

    @property
    def ok(self) -> bool:
        return not self.findings


def _display_path(path: Path, repo_root: Path) -> str:
    try:
        return path.resolve().relative_to(repo_root.resolve()).as_posix()
    except (OSError, ValueError):
        return path.name


def _finding(path: str, code: str, field: str = "/") -> Finding:
    return Finding(path=path, code=code, field=field)


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _walk_safe(value: Any) -> bool:
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
            if not all(isinstance(key, str) for key in current):
                return False
            pending.extend(current.values())
        elif isinstance(current, list):
            pending.extend(current)
    return True


def _read_mapping(path: Path, *, repo_root: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    label = _display_path(path, repo_root)
    try:
        if path.is_symlink():
            return None, [_finding(label, "INPUT_SYMLINK_DENIED")]
        if not path.is_file():
            return None, [_finding(label, "FILE_NOT_FOUND")]
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [_finding(label, "FILE_TOO_LARGE")]
        text = path.read_text(encoding="utf-8")
        if any(isinstance(token, (AliasToken, AnchorToken)) for token in yaml.scan(text)):
            return None, [_finding(label, "YAML_ALIAS_DENIED")]
        documents = list(yaml.load_all(text, Loader=UniqueKeyLoader))
    except UnicodeDecodeError:
        return None, [_finding(label, "YAML_NOT_UTF8")]
    except ConstructorError:
        return None, [_finding(label, "YAML_DUPLICATE_KEY")]
    except yaml.YAMLError:
        return None, [_finding(label, "YAML_INVALID")]
    except OSError:
        return None, [_finding(label, "FILE_READ_ERROR")]
    except (RecursionError, ValueError):
        return None, [_finding(label, "YAML_COMPLEXITY_LIMIT")]
    if len(documents) != 1:
        return None, [_finding(label, "YAML_MULTIDOCUMENT_DENIED")]
    value = documents[0]
    if not isinstance(value, dict):
        return None, [_finding(label, "ROOT_NOT_OBJECT")]
    if not _walk_safe(value):
        return None, [_finding(label, "YAML_NONFINITE_OR_COMPLEX")]
    return value, []


def _load_schema(path_label: str) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError, ValueError):
        return None, [_finding(path_label, "SCHEMA_UNAVAILABLE")]
    return schema, []


def _schema_findings(
    candidate: Mapping[str, Any],
    *,
    schema: Mapping[str, Any],
    path_label: str,
) -> list[Finding]:
    errors = list(
        islice(
            Draft202012Validator(
                schema,
                format_checker=FormatChecker(),
            ).iter_errors(candidate),
            MAX_SCHEMA_FINDINGS + 1,
        )
    )
    findings = [
        _finding(path_label, "SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in sorted(
            errors[:MAX_SCHEMA_FINDINGS],
            key=lambda item: (_pointer(item.absolute_path), str(item.validator)),
        )
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(_finding(path_label, "SCHEMA_FINDINGS_TRUNCATED"))
    return findings


def canonical_hash(candidate: Mapping[str, Any]) -> str:
    projected = copy.deepcopy(dict(candidate))
    projected.pop("spec_hash", None)
    encoded = json.dumps(
        projected,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def _canonical_relative_path(value: Any) -> PurePosixPath | None:
    if not isinstance(value, str) or not value or "\\" in value or value.startswith("/"):
        return None
    if "//" in value or (value.endswith("/") and value == "/"):
        return None
    normalized_value = value[:-1] if value.endswith("/") else value
    candidate = PurePosixPath(normalized_value)
    if str(candidate) != normalized_value or any(part in {"", ".", ".."} for part in candidate.parts):
        return None
    return candidate


def _check_reference(
    value: Any,
    *,
    field: str,
    path_label: str,
    repo_root: Path,
) -> list[Finding]:
    relative = _canonical_relative_path(value)
    if relative is None:
        return [_finding(path_label, "REFERENCE_PATH_INVALID", field)]
    try:
        root = repo_root.resolve(strict=True)
        unresolved = root.joinpath(*relative.parts)
        cursor = root
        for part in relative.parts:
            cursor = cursor / part
            if cursor.is_symlink():
                return [_finding(path_label, "REFERENCE_SYMLINK_DENIED", field)]
        resolved = unresolved.resolve(strict=True)
        resolved.relative_to(root)
    except (OSError, ValueError):
        return [_finding(path_label, "REFERENCE_NOT_FOUND", field)]
    if not (resolved.is_file() or resolved.is_dir()):
        return [_finding(path_label, "REFERENCE_NOT_FOUND", field)]
    return []


def _check_sorted_unique(
    value: Any,
    *,
    field: str,
    path_label: str,
) -> list[Finding]:
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        return []
    if value != sorted(set(value)):
        return [_finding(path_label, "ARRAY_NOT_CANONICAL", field)]
    return []


def validate_declaration(
    path: Path,
    *,
    repo_root: Path = REPO_ROOT,
    expected_path: str | None = None,
    check_references: bool = True,
    schema: Mapping[str, Any] | None = None,
) -> tuple[ValidationResult, dict[str, Any] | None]:
    path_label = _display_path(path, repo_root)
    candidate, findings = _read_mapping(path, repo_root=repo_root)
    if candidate is None:
        return ValidationResult(tuple(sorted(findings))), None

    if schema is None:
        schema, schema_load_findings = _load_schema(path_label)
        findings.extend(schema_load_findings)
    if schema is not None:
        findings.extend(_schema_findings(candidate, schema=schema, path_label=path_label))

    if expected_path is not None and candidate.get("path") != expected_path:
        findings.append(_finding(path_label, "DECLARED_PATH_MISMATCH", "/path"))

    declared_path = _canonical_relative_path(candidate.get("path"))
    if declared_path is not None and len(declared_path.parts) >= 3:
        declared_domain = declared_path.parts[1]
        if candidate.get("domain_id") != declared_domain:
            findings.append(_finding(path_label, "DOMAIN_PATH_MISMATCH", "/domain_id"))
        spec_id = candidate.get("spec_id")
        if isinstance(spec_id, str) and not spec_id.startswith(
            f"kfm.pipeline.{declared_domain}."
        ):
            findings.append(_finding(path_label, "SPEC_ID_DOMAIN_MISMATCH", "/spec_id"))

    try:
        expected_hash = canonical_hash(candidate)
    except (TypeError, ValueError, RecursionError):
        findings.append(_finding(path_label, "SPEC_HASH_UNCOMPUTABLE", "/spec_hash"))
    else:
        if candidate.get("spec_hash") != expected_hash:
            findings.append(_finding(path_label, "SPEC_HASH_MISMATCH", "/spec_hash"))

    canonical_arrays: list[tuple[Any, str]] = [
        (candidate.get("source_docs"), "/source_docs"),
        (candidate.get("required_gates"), "/required_gates"),
        (candidate.get("reason_codes"), "/reason_codes"),
        (candidate.get("non_effects"), "/non_effects"),
    ]
    bindings = candidate.get("bindings")
    if isinstance(bindings, dict):
        canonical_arrays.extend(
            (bindings.get(key), f"/bindings/{key}") for key in REFERENCE_ARRAYS
        )
    lifecycle = candidate.get("lifecycle")
    if isinstance(lifecycle, dict):
        canonical_arrays.extend(
            (
                (lifecycle.get("candidate_inputs"), "/lifecycle/candidate_inputs"),
                (lifecycle.get("candidate_outputs"), "/lifecycle/candidate_outputs"),
            )
        )
        if "declared_possible_targets" in lifecycle:
            canonical_arrays.append(
                (lifecycle.get("declared_possible_targets"), "/lifecycle/declared_possible_targets")
            )
    for value, field in canonical_arrays:
        findings.extend(_check_sorted_unique(value, field=field, path_label=path_label))

    if check_references:
        reference_values: list[tuple[Any, str]] = []
        source_docs = candidate.get("source_docs")
        if isinstance(source_docs, list):
            reference_values.extend(
                (value, f"/source_docs/{index}") for index, value in enumerate(source_docs)
            )
        if isinstance(bindings, dict):
            for key in REFERENCE_ARRAYS:
                values = bindings.get(key)
                if isinstance(values, list):
                    reference_values.extend(
                        (value, f"/bindings/{key}/{index}")
                        for index, value in enumerate(values)
                    )
        if "canonical_target" in candidate:
            reference_values.append((candidate.get("canonical_target"), "/canonical_target"))
        validation = candidate.get("validation")
        if isinstance(validation, dict) and "workflow" in validation:
            reference_values.append((validation.get("workflow"), "/validation/workflow"))
        for value, field in reference_values:
            findings.extend(
                _check_reference(
                    value,
                    field=field,
                    path_label=path_label,
                    repo_root=repo_root,
                )
            )

    execution = candidate.get("execution")
    lifecycle = candidate.get("lifecycle")
    if candidate.get("status") != "PROPOSED_INACTIVE":
        findings.append(_finding(path_label, "INACTIVE_POSTURE_VIOLATION", "/status"))
    if not isinstance(lifecycle, dict) or lifecycle.get("writes_targets") is not False:
        findings.append(
            _finding(path_label, "INACTIVE_POSTURE_VIOLATION", "/lifecycle/writes_targets")
        )
    if isinstance(execution, dict):
        for field in DENIED_EXECUTION_FIELDS:
            if execution.get(field) != "DENIED":
                findings.append(
                    _finding(path_label, "INACTIVE_POSTURE_VIOLATION", f"/execution/{field}")
                )
    else:
        findings.append(_finding(path_label, "INACTIVE_POSTURE_VIOLATION", "/execution"))

    return ValidationResult(tuple(sorted(set(findings)))), candidate


def _pipeline_paths(repo_root: Path) -> list[Path]:
    root = repo_root / "pipeline_specs"
    return sorted({*root.rglob("*.yaml"), *root.rglob("*.yml")}) if root.is_dir() else []


def validate_repository(repo_root: Path = REPO_ROOT) -> ValidationResult:
    paths = _pipeline_paths(repo_root)
    if not paths:
        return ValidationResult((_finding("pipeline_specs", "PIPELINE_SPEC_NOT_FOUND"),), 0)
    schema, schema_findings = _load_schema("pipeline_specs")
    if schema is None:
        return ValidationResult(tuple(schema_findings), 0)

    findings: list[Finding] = []
    candidates: dict[str, dict[str, Any]] = {}
    identities: dict[str, list[str]] = {}
    for path in paths:
        expected = path.relative_to(repo_root).as_posix()
        result, candidate = validate_declaration(
            path,
            repo_root=repo_root,
            expected_path=expected,
            check_references=True,
            schema=schema,
        )
        findings.extend(result.findings)
        if candidate is None:
            continue
        candidates[expected] = candidate
        spec_id = candidate.get("spec_id")
        if isinstance(spec_id, str):
            identities.setdefault(spec_id, []).append(expected)

    for paths_for_id in identities.values():
        if len(paths_for_id) > 1:
            findings.extend(
                _finding(path, "SPEC_ID_DUPLICATE", "/spec_id") for path in paths_for_id
            )

    for path_label, candidate in candidates.items():
        if candidate.get("profile_kind") != "COMPATIBILITY_ALIAS":
            continue
        target = candidate.get("canonical_target")
        if target == path_label:
            findings.append(_finding(path_label, "ALIAS_SELF_TARGET", "/canonical_target"))
            continue
        target_candidate = candidates.get(target) if isinstance(target, str) else None
        if target_candidate is None:
            findings.append(
                _finding(path_label, "ALIAS_TARGET_NOT_DECLARATION", "/canonical_target")
            )
        elif target_candidate.get("profile_kind") == "COMPATIBILITY_ALIAS":
            findings.append(_finding(path_label, "ALIAS_TARGET_CHAIN_DENIED", "/canonical_target"))

    return ValidationResult(tuple(sorted(set(findings))), len(paths))


def validate_fixtures(repo_root: Path = REPO_ROOT) -> ValidationResult:
    schema, schema_findings = _load_schema("fixtures")
    if schema is None:
        return ValidationResult(tuple(schema_findings), 0)
    manifest_path = FIXTURE_ROOT / "expected_findings.json"
    try:
        manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return ValidationResult((_finding("expected_findings.json", "FIXTURE_MANIFEST_INVALID"),), 0)
    if not isinstance(manifest, dict) or not isinstance(manifest.get("cases"), list):
        return ValidationResult((_finding("expected_findings.json", "FIXTURE_MANIFEST_INVALID"),), 0)

    findings: list[Finding] = []
    checked = 0
    declared_inputs: list[str] = []
    for case in manifest["cases"]:
        if not isinstance(case, dict):
            findings.append(_finding("expected_findings.json", "FIXTURE_MANIFEST_INVALID"))
            continue
        relative_input = case.get("input")
        outcome = case.get("expected_outcome")
        expected_findings = case.get("expected_findings")
        relative = _canonical_relative_path(relative_input)
        if (
            relative is None
            or relative.parts[0] not in {"valid", "invalid"}
            or outcome not in {"PASS", "DENY"}
            or not isinstance(expected_findings, list)
            or not all(
                isinstance(item, dict) and isinstance(item.get("code"), str)
                for item in expected_findings
            )
        ):
            findings.append(_finding("expected_findings.json", "FIXTURE_MANIFEST_INVALID"))
            continue
        relative_label = relative.as_posix()
        declared_inputs.append(relative_label)
        path = FIXTURE_ROOT.joinpath(*relative.parts)
        checked += 1
        result, _ = validate_declaration(
            path,
            repo_root=repo_root,
            check_references=False,
            schema=schema,
        )
        observed_codes = sorted({finding.code for finding in result.findings})
        expected_codes = sorted({item["code"] for item in expected_findings})
        expected_pass = outcome == "PASS"
        if result.ok != expected_pass or observed_codes != expected_codes:
            findings.append(_finding(relative_label, "FIXTURE_POLARITY_MISMATCH"))

    fixture_inputs = sorted(
        path.relative_to(FIXTURE_ROOT).as_posix()
        for lane in ("valid", "invalid")
        for path in (FIXTURE_ROOT / lane).glob("*.yaml")
    )
    if len(declared_inputs) != len(set(declared_inputs)):
        findings.append(_finding("expected_findings.json", "FIXTURE_MANIFEST_DUPLICATE"))
    if sorted(set(declared_inputs)) != fixture_inputs:
        findings.append(_finding("expected_findings.json", "FIXTURE_MANIFEST_COVERAGE_MISMATCH"))
    if not any(path.startswith("valid/") for path in fixture_inputs) or not any(
        path.startswith("invalid/") for path in fixture_inputs
    ):
        findings.append(_finding("fixtures", "FIXTURE_POLARITY_EMPTY"))
    return ValidationResult(tuple(sorted(set(findings))), checked)


def _report(result: ValidationResult, *, profile: str) -> dict[str, Any]:
    return {
        "schema_version": "kfm.pipeline-spec-validation-report.v1",
        "profile": profile,
        "outcome": "PASS" if result.ok else "FAIL",
        "checked_count": result.checked_count,
        "findings": [
            {"path": finding.path, "code": finding.code, "field": finding.field}
            for finding in result.findings
        ],
        "non_effects": [
            "NO_EVIDENCE_CLOSURE",
            "NO_LIFECYCLE_WRITE",
            "NO_LIVE_SOURCE_ACCESS",
            "NO_PROMOTION",
            "NO_PUBLICATION",
            "NO_RELEASE",
            "NO_SOURCE_ACTIVATION",
        ],
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path)
    parser.add_argument("--repo-root", type=Path, default=REPO_ROOT)
    parser.add_argument("--fixtures", action="store_true")
    parser.add_argument("--skip-reference-existence", action="store_true")
    args = parser.parse_args(argv)
    repo_root = args.repo_root.resolve()

    if args.fixtures and args.paths:
        parser.error("--fixtures cannot be combined with explicit paths")
    if args.fixtures:
        result = validate_fixtures(repo_root)
        profile = "fixtures"
    elif args.paths:
        schema, schema_findings = _load_schema("pipeline_specs")
        findings = list(schema_findings)
        checked = 0
        if schema is not None:
            for raw_path in args.paths:
                path = raw_path if raw_path.is_absolute() else repo_root / raw_path
                expected_path: str | None
                try:
                    expected_path = path.resolve().relative_to(repo_root).as_posix()
                except (OSError, ValueError):
                    expected_path = None
                result, _ = validate_declaration(
                    path,
                    repo_root=repo_root,
                    expected_path=expected_path,
                    check_references=not args.skip_reference_existence,
                    schema=schema,
                )
                findings.extend(result.findings)
                checked += 1
        result = ValidationResult(tuple(sorted(set(findings))), checked)
        profile = "explicit"
    else:
        result = validate_repository(repo_root)
        profile = "repository"

    print(json.dumps(_report(result, profile=profile), sort_keys=True, separators=(",", ":")))
    return 0 if result.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
