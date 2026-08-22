#!/usr/bin/env python3
"""Validate the KFM machine-readable object-family register without network access.

The `.yaml` register intentionally uses the JSON-compatible subset of YAML so the
validator can parse it deterministically with the Python standard library. A PASS
proves bounded shape, milestone-family membership, canonical ordering, relationship
closure, declared-path placement and existence, and structural classification only.
It does not establish object-family meaning, select conflicting candidates, or
grant policy, evidence, review, release, deployment, or publication authority.
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
SCOPE = "trust-object-catalog-navigation-relationships-and-structural-coverage-only"
PATH_ROLES = {
    "contract_paths": ("contracts/",),
    "schema_paths": ("schemas/contracts/v1/",),
    "policy_paths": ("policy/",),
    "fixture_paths": ("fixtures/",),
    "validator_paths": ("tools/proof_pack/", "tools/validators/"),
    "test_paths": ("tests/",),
    "workflow_paths": (".github/workflows/",),
    "emitter_paths": ("apps/", "data/", "packages/", "pipelines/", "runtime/", "tools/"),
}
SURFACE_BY_PATH_ROLE = {
    "contract_paths": "contracts",
    "schema_paths": "schemas",
    "policy_paths": "policy",
    "fixture_paths": "fixtures",
    "validator_paths": "validators",
    "test_paths": "tests",
    "workflow_paths": "workflows",
    "emitter_paths": "emitters",
}
RELATIONSHIP_ROLES = (
    "dependency_family_ids",
    "evidence_family_ids",
    "release_family_ids",
    "correction_family_ids",
    "rollback_family_ids",
)
STRUCTURAL_ROLES = (
    "contract_paths",
    "schema_paths",
    "fixture_paths",
    "validator_paths",
    "test_paths",
    "workflow_paths",
)
REQUIRED_FAMILIES = {
    "ai_receipt": "AIReceipt",
    "correction_notice": "CorrectionNotice",
    "evidence_bundle": "EvidenceBundle",
    "evidence_ref": "EvidenceRef",
    "layer_manifest": "LayerManifest",
    "policy_decision": "PolicyDecision",
    "promotion_receipt": "PromotionReceipt",
    "proof_pack": "ProofPack",
    "release_manifest": "ReleaseManifest",
    "rollback_card": "RollbackCard",
    "run_receipt": "RunReceipt",
    "runtime_response_envelope": "RuntimeResponseEnvelope",
    "source_activation_decision": "SourceActivationDecision",
    "source_descriptor": "SourceDescriptor",
    "validation_report": "ValidationReport",
    "withdrawal_notice": "WithdrawalNotice",
}
REQUIRED_NON_EFFECTS = frozenset(
    {
        "does_not_activate_sources",
        "does_not_add_rename_or_remove_object_family_authority",
        "does_not_create_evidence_release_or_publication_authority",
        "does_not_define_contract_meaning",
        "does_not_define_schema_shape",
        "does_not_evaluate_policy",
        "does_not_prove_runtime_or_release_maturity",
        "does_not_select_conflicting_candidates",
    }
)
ABSENT_SURFACE_STATES = frozenset({"ABSENT", "NOT_INSPECTED"})


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


def _mapping(value: Any) -> Mapping[str, Any]:
    return value if isinstance(value, dict) else {}


def _check_sorted_unique(
    values: list[Any],
    *,
    field: str,
    findings: list[Finding],
    prefix: str,
) -> None:
    try:
        canonical = sorted(values)
        unique_count = len(set(values))
    except TypeError:
        return
    if len(values) != unique_count:
        findings.append(Finding(f"{prefix}_DUPLICATE", field))
    if values != canonical:
        findings.append(Finding(f"{prefix}_NOT_CANONICAL", field))


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


def _expected_implementation_status(entry: Mapping[str, Any]) -> str:
    surfaces = _mapping(entry.get("surface_status"))
    compatibility = _mapping(entry.get("compatibility"))
    if compatibility.get("posture") == "multiple_candidates_unresolved" or any(
        value == "CONFLICTED" for value in surfaces.values()
    ):
        return "CONFLICTED"
    contracts = bool(_array(entry.get("contract_paths")))
    schemas = bool(_array(entry.get("schema_paths")))
    if not contracts and not schemas:
        return "ABSENT"
    if all(
        _array(entry.get(role))
        and surfaces.get(SURFACE_BY_PATH_ROLE[role]) == "IMPLEMENTED"
        for role in STRUCTURAL_ROLES
    ):
        return "IMPLEMENTED"
    return "PARTIAL"


def _path_has_symlink_component(root: Path, relative: PurePosixPath) -> bool:
    candidate = root
    for part in relative.parts:
        candidate = candidate / part
        if candidate.is_symlink():
            return True
    return False


def _check_declared_path(
    value: Any,
    *,
    prefixes: tuple[str, ...],
    field: str,
    resolved_root: Path,
    check_paths: bool,
    findings: list[Finding],
) -> None:
    relative = _canonical_path(value)
    if relative is None:
        findings.append(Finding("PATH_INVALID", field))
        return
    if not any(str(relative).startswith(prefix) for prefix in prefixes):
        findings.append(Finding("PATH_ROOT_MISMATCH", field))
        return
    if not check_paths:
        return
    try:
        if _path_has_symlink_component(resolved_root, relative):
            findings.append(Finding("PATH_SYMLINK_DENIED", field))
            return
        candidate_path = resolved_root.joinpath(*relative.parts)
        resolved = candidate_path.resolve(strict=True)
        resolved.relative_to(resolved_root)
        if not (resolved.is_file() or resolved.is_dir()):
            findings.append(Finding("PATH_NOT_REGULAR", field))
    except (OSError, ValueError):
        findings.append(Finding("PATH_NOT_FOUND", field))


def _semantic_findings(
    candidate: Mapping[str, Any],
    *,
    repo_root: Path,
    check_paths: bool,
) -> list[Finding]:
    findings: list[Finding] = []
    entries = _array(candidate.get("entries"))
    ids = [entry.get("family_id") for entry in entries if isinstance(entry, dict)]
    _check_sorted_unique(
        ids,
        field="/entries",
        findings=findings,
        prefix="FAMILY_ID",
    )

    unresolved = _array(candidate.get("unresolved_items"))
    non_effects = _array(candidate.get("non_effects"))
    _check_sorted_unique(
        unresolved,
        field="/unresolved_items",
        findings=findings,
        prefix="UNRESOLVED_ITEMS",
    )
    _check_sorted_unique(
        non_effects,
        field="/non_effects",
        findings=findings,
        prefix="NON_EFFECTS",
    )
    if not REQUIRED_NON_EFFECTS.issubset(set(non_effects)):
        findings.append(Finding("REQUIRED_NON_EFFECT_MISSING", "/non_effects"))
    if candidate.get("authority") != "navigational_index_only":
        findings.append(Finding("SELF_AUTHORITY_CLAIM", "/authority"))

    entry_by_id = {
        entry.get("family_id"): entry
        for entry in entries
        if isinstance(entry, dict) and isinstance(entry.get("family_id"), str)
    }
    required_entries = [
        entry
        for entry in entries
        if isinstance(entry, dict) and entry.get("required_by_milestone") is True
    ]
    required_ids = {
        entry.get("family_id")
        for entry in required_entries
        if isinstance(entry.get("family_id"), str)
    }
    if candidate.get("coverage_scope") == "milestone_trust_spine_v1":
        if required_ids != set(REQUIRED_FAMILIES):
            findings.append(Finding("REQUIRED_FAMILY_SET_MISMATCH", "/entries"))
        for family_id, display_name in sorted(REQUIRED_FAMILIES.items()):
            entry = entry_by_id.get(family_id)
            if isinstance(entry, dict) and entry.get("display_name") != display_name:
                findings.append(
                    Finding("REQUIRED_DISPLAY_NAME_MISMATCH", f"/entries/{family_id}")
                )

    required_count = len(required_entries)
    other_count = len(entries) - required_count
    conflicted_required_count = sum(
        1
        for entry in required_entries
        if entry.get("implementation_status") == "CONFLICTED"
    )
    for field, expected in (
        ("required_family_count", len(REQUIRED_FAMILIES)),
        ("required_registered_count", required_count),
        ("other_registered_count", other_count),
        ("conflicted_required_count", conflicted_required_count),
    ):
        if candidate.get(field) != expected:
            findings.append(Finding("CATALOG_COUNT_MISMATCH", f"/{field}"))
    if candidate.get("completeness") == "complete" and (
        unresolved or conflicted_required_count
    ):
        findings.append(Finding("IMPOSSIBLE_COMPLETENESS", "/completeness"))

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
        if raw_entry.get("implementation_status") != _expected_implementation_status(
            raw_entry
        ):
            findings.append(
                Finding(
                    "IMPLEMENTATION_STATUS_MISMATCH",
                    f"{field_base}/implementation_status",
                )
            )

        surfaces = _mapping(raw_entry.get("surface_status"))
        declared_paths: set[Any] = set()
        for role, prefixes in PATH_ROLES.items():
            values = _array(raw_entry.get(role))
            declared_paths.update(values)
            _check_sorted_unique(
                values,
                field=f"{field_base}/{role}",
                findings=findings,
                prefix="PATHS",
            )
            surface = SURFACE_BY_PATH_ROLE[role]
            surface_status = surfaces.get(surface)
            if values and surface_status in ABSENT_SURFACE_STATES:
                findings.append(
                    Finding("SURFACE_STATUS_MISMATCH", f"{field_base}/surface_status/{surface}")
                )
            if not values and surface_status not in ABSENT_SURFACE_STATES:
                findings.append(
                    Finding("SURFACE_STATUS_MISMATCH", f"{field_base}/surface_status/{surface}")
                )
            for item_index, value in enumerate(values):
                _check_declared_path(
                    value,
                    prefixes=prefixes,
                    field=f"{field_base}/{role}/{item_index}",
                    resolved_root=resolved_root,
                    check_paths=check_paths,
                    findings=findings,
                )

        identity = _mapping(raw_entry.get("identity"))
        identity_refs = _array(identity.get("rule_refs"))
        _check_sorted_unique(
            identity_refs,
            field=f"{field_base}/identity/rule_refs",
            findings=findings,
            prefix="IDENTITY_REFS",
        )
        for ref_index, value in enumerate(identity_refs):
            if value not in declared_paths:
                findings.append(
                    Finding(
                        "IDENTITY_REF_UNDECLARED",
                        f"{field_base}/identity/rule_refs/{ref_index}",
                    )
                )
            _check_declared_path(
                value,
                prefixes=("contracts/", "schemas/contracts/v1/"),
                field=f"{field_base}/identity/rule_refs/{ref_index}",
                resolved_root=resolved_root,
                check_paths=check_paths,
                findings=findings,
            )

        compatibility = _mapping(raw_entry.get("compatibility"))
        candidates = _array(compatibility.get("candidate_paths"))
        _check_sorted_unique(
            candidates,
            field=f"{field_base}/compatibility/candidate_paths",
            findings=findings,
            prefix="COMPATIBILITY_CANDIDATES",
        )
        for candidate_index, value in enumerate(candidates):
            if value not in declared_paths:
                findings.append(
                    Finding(
                        "COMPATIBILITY_CANDIDATE_UNDECLARED",
                        f"{field_base}/compatibility/candidate_paths/{candidate_index}",
                    )
                )
        reasons = _array(compatibility.get("reason_codes"))
        _check_sorted_unique(
            reasons,
            field=f"{field_base}/compatibility/reason_codes",
            findings=findings,
            prefix="COMPATIBILITY_REASONS",
        )
        if compatibility.get("posture") == "multiple_candidates_unresolved":
            if raw_entry.get("implementation_status") != "CONFLICTED":
                findings.append(
                    Finding(
                        "UNRESOLVED_COMPATIBILITY_NOT_CONFLICTED",
                        f"{field_base}/implementation_status",
                    )
                )

        for role in RELATIONSHIP_ROLES:
            values = _array(raw_entry.get(role))
            _check_sorted_unique(
                values,
                field=f"{field_base}/{role}",
                findings=findings,
                prefix="RELATIONSHIPS",
            )
            for relationship_index, value in enumerate(values):
                field = f"{field_base}/{role}/{relationship_index}"
                if value == raw_entry.get("family_id"):
                    findings.append(Finding("SELF_RELATIONSHIP", field))
                elif value not in entry_by_id:
                    findings.append(Finding("RELATIONSHIP_TARGET_MISSING", field))

        for role in ("producer_classes", "consumer_classes"):
            _check_sorted_unique(
                _array(raw_entry.get(role)),
                field=f"{field_base}/{role}",
                findings=findings,
                prefix="ROLE_CLASSES",
            )
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
