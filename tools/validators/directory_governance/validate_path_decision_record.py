#!/usr/bin/env python3
"""Validate KFM PathDecisionRecord instances against the pinned root registry.

A PASS proves internal consistency of the recorded placement evaluation only.
It does not authorize a path, accept an ADR, create authority, move bytes, grant
write access, or approve release, deployment, promotion, or publication.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path, PurePosixPath
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(REPO_ROOT))

from tools.validators.directory_governance.validate_root_registry import (
    ADOPTED_DOCTRINE_SHA256,
    REGISTER_PATH,
    resolve_registry,
    validate_register,
)

SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/governance/path_decision_record.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/governance/path_decision_record"
MAX_FILE_BYTES = 2 * 1024 * 1024
MAX_SCHEMA_FINDINGS = 100
SCOPE = "path-decision-record-consistency-only"

ROLE_ROOT = {
    "deployable": "apps/",
    "reusable_library": "packages/",
    "source_connector": "connectors/",
    "transformation_pipeline": "pipelines/",
    "declarative_spec": "pipeline_specs/",
    "repository_tool": "tools/",
    "thin_script": "scripts/",
    "runtime_adapter": "runtime/",
    "infrastructure": "infra/",
}
TRUST_BEARING_KINDS = {
    "data_instance",
    "governance_projection",
    "policy_rule",
    "release_decision",
    "schema",
    "semantic_contract",
}
INTERNAL_LIFECYCLE_PREFIXES = ("data/raw/", "data/work/", "data/quarantine/")


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

    @property
    def outcome(self) -> str:
        if not self.findings:
            return "PASS"
        if any(
            finding.code.startswith(("INPUT_", "JSON_", "SCHEMA_UNAVAILABLE", "REGISTRY_UNAVAILABLE"))
            for finding in self.findings
        ):
            return "ERROR_VALIDATOR"
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


def _canonical_repo_path(value: Any) -> PurePosixPath | None:
    if not isinstance(value, str) or not value or value.startswith("/") or "\\" in value:
        return None
    path = PurePosixPath(value)
    if str(path) != value.rstrip("/") or any(part in {"", ".", ".."} for part in path.parts):
        return None
    if any(
        not part
        or part.endswith((".", " "))
        or any(char.isspace() for char in part)
        or not all(char.isascii() and (char.isalnum() or char in "._-") for char in part)
        for part in path.parts
    ):
        return None
    return path


def _root_path(value: str) -> str:
    first = PurePosixPath(value.rstrip("/")).parts[0]
    return f"{first}/"


def _load_registry() -> tuple[dict[str, Any] | None, list[Finding]]:
    result = validate_register(
        REGISTER_PATH,
        check_repo_roots=False,
        enforce_doctrine_parity=True,
    )
    if not result.ok:
        return None, [Finding("REGISTRY_UNAVAILABLE", "/registry")]
    try:
        registry = resolve_registry(json.loads(REGISTER_PATH.read_text(encoding="utf-8")))
    except (OSError, UnicodeError, json.JSONDecodeError):
        return None, [Finding("REGISTRY_UNAVAILABLE", "/registry")]
    return registry, []


def _canonical_arrays(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    for field in ("evidence", "rules", "reason_codes", "candidate_roots", "consumer_refs", "split_targets"):
        values = _array(candidate.get(field))
        if values != sorted(set(values)):
            findings.append(Finding("ARRAY_NOT_CANONICAL", f"/{field}"))
    return findings


def _semantic_findings(candidate: Mapping[str, Any], registry: Mapping[str, Any]) -> list[Finding]:
    findings = _canonical_arrays(candidate)
    actual_registry_digest = "sha256:" + hashlib.sha256(REGISTER_PATH.read_bytes()).hexdigest()
    binding = candidate["registry"]
    doctrine = candidate["doctrine"]
    if binding["digest"] != actual_registry_digest:
        findings.append(Finding("REGISTRY_DIGEST_MISMATCH", "/registry/digest"))
    if binding["base_ref"] != registry["base_ref"]:
        findings.append(Finding("REGISTRY_BASE_REF_MISMATCH", "/registry/base_ref"))
    expected_doctrine = f"sha256:{ADOPTED_DOCTRINE_SHA256}"
    if doctrine["digest"] != expected_doctrine:
        findings.append(Finding("DOCTRINE_DIGEST_MISMATCH", "/doctrine/digest"))

    artifact = candidate["artifact"]
    proposed = artifact["proposed_path"]
    current = artifact["current_path"]
    proposed_path = _canonical_repo_path(proposed)
    if proposed_path is None:
        findings.append(Finding("PROPOSED_PATH_INVALID", "/artifact/proposed_path"))
        return findings
    if current is not None and _canonical_repo_path(current) is None:
        findings.append(Finding("CURRENT_PATH_INVALID", "/artifact/current_path"))

    proposed_root = _root_path(proposed)
    roots = {entry["path"]: entry for entry in registry["roots"]}
    root = roots.get(proposed_root)
    if root is None:
        findings.append(Finding("ROOT_UNREGISTERED", "/artifact/proposed_path"))
    if proposed_root not in candidate["candidate_roots"]:
        findings.append(Finding("PROPOSED_ROOT_NOT_CANDIDATE", "/candidate_roots"))

    outcome = candidate["outcome"]
    kind = artifact["artifact_kind"]
    role = artifact["execution_role"]
    exposure = artifact["exposure"]

    if exposure == "public" and proposed.startswith(INTERNAL_LIFECYCLE_PREFIXES):
        if outcome not in {"HOLD", "DENY"}:
            findings.append(Finding("PUBLIC_INTERNAL_LIFECYCLE_DENIED", "/outcome"))

    if proposed_root == "artifacts/" and kind in TRUST_BEARING_KINDS:
        if outcome not in {"HOLD", "DENY", "MIGRATE"}:
            findings.append(Finding("ARTIFACTS_TRUST_AUTHORITY_DENIED", "/outcome"))

    if root is not None and outcome in {"PLACE", "MIGRATE"}:
        if root["class"] not in {"canonical", "platform"} or root["status"] != "ACTIVE":
            findings.append(Finding("TARGET_ROOT_NOT_WRITABLE_CANONICAL", "/outcome"))
        if kind not in root["allowed_artifact_kinds"]:
            findings.append(Finding("ARTIFACT_KIND_NOT_ALLOWED", "/artifact/artifact_kind"))
        if kind in root["prohibited_artifact_kinds"]:
            findings.append(Finding("ARTIFACT_KIND_PROHIBITED", "/artifact/artifact_kind"))
        expected_root = ROLE_ROOT.get(role)
        if expected_root is not None and proposed_root != expected_root:
            findings.append(Finding("EXECUTION_ROLE_ROOT_MISMATCH", "/artifact/execution_role"))

    if outcome == "PLACE":
        if current is not None and current != proposed:
            findings.append(Finding("PLACE_CURRENT_PATH_CONFLICT", "/artifact/current_path"))
        if candidate["canonical_source"] is not None or candidate["consumer_refs"] or candidate["split_targets"]:
            findings.append(Finding("PLACE_COMPANION_FIELDS_FORBIDDEN", "/outcome"))

    elif outcome == "MIGRATE":
        if current is None or current == proposed:
            findings.append(Finding("MIGRATION_SOURCE_REQUIRED", "/artifact/current_path"))
        if "DIR-MIGRATE-001" not in candidate["rules"]:
            findings.append(Finding("MIGRATION_RULE_REQUIRED", "/rules"))

    elif outcome == "MIRROR":
        if root is None or root["class"] != "compatibility":
            findings.append(Finding("MIRROR_TARGET_NOT_COMPATIBILITY", "/artifact/proposed_path"))
        if candidate["canonical_source"] is None:
            findings.append(Finding("MIRROR_CANONICAL_SOURCE_REQUIRED", "/canonical_source"))
        if not candidate["consumer_refs"]:
            findings.append(Finding("MIRROR_CONSUMER_REQUIRED", "/consumer_refs"))
        if "exit_condition_recorded" not in candidate["reason_codes"]:
            findings.append(Finding("MIRROR_EXIT_CONDITION_REQUIRED", "/reason_codes"))

    elif outcome == "SPLIT":
        if len(candidate["split_targets"]) < 2:
            findings.append(Finding("SPLIT_TARGETS_REQUIRED", "/split_targets"))
        if candidate["canonical_source"] is not None or candidate["consumer_refs"]:
            findings.append(Finding("SPLIT_COMPANION_FIELDS_FORBIDDEN", "/outcome"))

    elif outcome in {"HOLD", "DENY"}:
        if not candidate["reason_codes"]:
            findings.append(Finding("FAIL_CLOSED_REASON_REQUIRED", "/reason_codes"))

    return findings


def validate_record(path: Path) -> ValidationResult:
    candidate, findings = _read_object(path)
    if candidate is None:
        return ValidationResult(tuple(sorted(set(findings))))
    findings.extend(_schema_findings(candidate))
    if findings:
        return ValidationResult(tuple(sorted(set(findings))))
    registry, registry_findings = _load_registry()
    findings.extend(registry_findings)
    if registry is not None:
        findings.extend(_semantic_findings(candidate, registry))
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
                "authorizes_path": False,
                "accepts_adr": False,
                "moves_bytes": False,
                "grants_writes": False,
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
        result = validate_record(path)
        print(_serialize(path, result))
        passed = result.ok and passed
    for path in invalid:
        result = validate_record(path)
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
    parser = argparse.ArgumentParser(description="Validate one KFM PathDecisionRecord.")
    parser.add_argument("path", nargs="?")
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        return run_fixture_profile()
    if not args.path:
        parser.error("path is required unless --fixtures is used")
    path = Path(args.path)
    result = validate_record(path)
    print(_serialize(path, result))
    if result.outcome == "PASS":
        return 0
    if result.outcome == "ERROR_VALIDATOR":
        return 2
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
