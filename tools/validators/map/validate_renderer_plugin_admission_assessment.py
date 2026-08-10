#!/usr/bin/env python3
"""Validate inactive, fixture-only RendererPluginAdmissionAssessment candidates.

PASS means ready for human review only. This validator never queries a registry,
downloads or imports a package, installs a plugin, evaluates policy, or boots a
renderer.
"""
from __future__ import annotations

import argparse
import copy
import json
import math
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
HASH_SRC = ROOT / "packages/hashing/src"
if str(HASH_SRC) not in sys.path:
    sys.path.insert(0, str(HASH_SRC))
try:
    from hashing import compute_spec_hash
except ImportError as exc:
    compute_spec_hash = None  # type: ignore[assignment]
    HASH_ERROR: Exception | None = exc
else:
    HASH_ERROR = None

SCHEMA = ROOT / "schemas/contracts/v1/map/renderer_plugin_admission_assessment.schema.json"
CASES = ROOT / "fixtures/contracts/v1/map/renderer_plugin_admission_assessment/cases.json"
MAX_BYTES = 1_048_576
SCOPE = "renderer-plugin-admission-assessment-fixture-only-v1"
FALSE_EFFECTS = {
    key: False
    for key in (
        "registry_queried", "package_downloaded", "plugin_installed",
        "plugin_imported", "renderer_booted", "network_probed",
        "lockfile_mutated", "policy_decided", "human_review_approved",
        "release_authorized", "deployed", "published",
    )
}
ERROR_CODES = {
    "FILE_NOT_FOUND", "FILE_READ_ERROR", "FILE_TOO_LARGE",
    "INPUT_SYMLINK_DENIED", "JSON_INVALID", "JSON_DUPLICATE_KEY",
    "JSON_NONFINITE_NUMBER", "ROOT_NOT_OBJECT", "SCHEMA_UNAVAILABLE",
    "HASHING_UNAVAILABLE", "SPEC_HASH_MISMATCH",
    "RENDERER_PLUGIN_ASSESSMENT_ID_MISMATCH", "FIXTURE_MANIFEST_INVALID",
}
ABSTAIN_CODES = {
    "DEPENDENCY_ORIGIN_UNRESOLVED", "ATTESTATION_UNRESOLVED",
    "SBOM_UNRESOLVED", "LICENSE_UNRESOLVED", "VULNERABILITY_UNRESOLVED",
    "ADAPTER_BOUNDARY_UNRESOLVED", "NETWORK_BEHAVIOR_UNRESOLVED",
    "REMOVAL_TEST_UNRESOLVED", "ROLLBACK_UNRESOLVED",
}


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return self.outcome == "PASS"


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


def _pairs(items: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in items:
        if key in result:
            raise DuplicateKeyError
        result[key] = value
    return result


def _bad_number(_value: str) -> object:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _read(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("FILE_NOT_FOUND", "/")]
        if path.stat().st_size > MAX_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_pairs,
            parse_constant=_bad_number,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
    except (OSError, UnicodeError):
        return None, [Finding("FILE_READ_ERROR", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    return value, []


def _pointer(parts: Iterable[object]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _schema_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = sorted(
            Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(candidate),
            key=lambda error: (_pointer(error.absolute_path), str(error.validator)),
        )
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    return [Finding("SCHEMA_INVALID", _pointer(error.absolute_path)) for error in errors[:100]]


def identity_subject(candidate: Mapping[str, Any]) -> dict[str, Any]:
    subject = copy.deepcopy(dict(candidate))
    subject.pop("assessment_id", None)
    subject.pop("spec_hash", None)
    return subject


def canonical_spec_hash(candidate: Mapping[str, Any]) -> str:
    if HASH_ERROR is not None or compute_spec_hash is None:
        raise RuntimeError("hashing unavailable") from HASH_ERROR
    return compute_spec_hash(identity_subject(candidate))


def expected_assessment_id(candidate: Mapping[str, Any]) -> str:
    digest = canonical_spec_hash(candidate).removeprefix("sha256:")
    return "renderer-plugin-assessment:" + digest[:24]


def assign_identity(candidate: Mapping[str, Any]) -> dict[str, Any]:
    result = copy.deepcopy(dict(candidate))
    result["spec_hash"] = canonical_spec_hash(result)
    result["assessment_id"] = expected_assessment_id(result)
    return result


def _canonical(values: Any) -> bool:
    return isinstance(values, list) and values == sorted(set(values))


def _status_finding(
    checks: Mapping[str, Any],
    status_key: str,
    good: str,
    unresolved: str,
    bad: str,
    unresolved_code: str,
    bad_code: str,
) -> Finding | None:
    status = checks.get(status_key)
    path = f"/checks/{status_key}"
    if status == unresolved:
        return Finding(unresolved_code, path)
    if status == bad:
        return Finding(bad_code, path)
    if status != good:
        return Finding(bad_code, path)
    return None


def _semantic(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    scope = candidate.get("assessment_scope")
    if isinstance(scope, Mapping) and not _canonical(scope.get("admitted_for")):
        findings.append(Finding("NONCANONICAL_ADMITTED_FOR", "/assessment_scope/admitted_for"))
    for key in ("evidence_refs", "limitations"):
        if not _canonical(candidate.get(key)):
            findings.append(Finding("NONCANONICAL_ARRAY", f"/{key}"))

    checks = candidate.get("checks")
    if isinstance(checks, Mapping):
        if checks.get("version_pinned") is not True:
            findings.append(Finding("VERSION_NOT_PINNED", "/checks/version_pinned"))
        if checks.get("integrity_verified") is not True:
            findings.append(Finding("INTEGRITY_NOT_VERIFIED", "/checks/integrity_verified"))
        if checks.get("lockfile_bound") is not True:
            findings.append(Finding("LOCKFILE_NOT_BOUND", "/checks/lockfile_bound"))

        origin = checks.get("origin_status")
        if origin == "ABSTAIN":
            findings.append(Finding("DEPENDENCY_ORIGIN_UNRESOLVED", "/checks/origin_status"))
        elif origin == "DENY":
            findings.append(Finding("DEPENDENCY_ORIGIN_DENIED", "/checks/origin_status"))

        status_specs = (
            ("attestation_status", "VERIFIED", "UNKNOWN", "INVALID", "ATTESTATION_UNRESOLVED", "ATTESTATION_INVALID"),
            ("sbom_status", "VERIFIED", "UNKNOWN", "INVALID", "SBOM_UNRESOLVED", "SBOM_INVALID"),
            ("license_status", "VERIFIED", "UNKNOWN", "DENIED", "LICENSE_UNRESOLVED", "LICENSE_DENIED"),
            ("vulnerability_status", "CLEAR", "UNKNOWN", "AFFECTED", "VULNERABILITY_UNRESOLVED", "VULNERABILITY_AFFECTED"),
            ("adapter_boundary_status", "VERIFIED", "UNKNOWN", "VIOLATED", "ADAPTER_BOUNDARY_UNRESOLVED", "ADAPTER_BOUNDARY_VIOLATED"),
            ("network_behavior_status", "DECLARED", "UNKNOWN", "VIOLATED", "NETWORK_BEHAVIOR_UNRESOLVED", "NETWORK_BEHAVIOR_VIOLATED"),
            ("removal_status", "VERIFIED", "UNKNOWN", "FAILED", "REMOVAL_TEST_UNRESOLVED", "REMOVAL_TEST_FAILED"),
            ("rollback_status", "VERIFIED", "UNKNOWN", "FAILED", "ROLLBACK_UNRESOLVED", "ROLLBACK_FAILED"),
        )
        for spec in status_specs:
            finding = _status_finding(checks, *spec)
            if finding is not None:
                findings.append(finding)

        verified_refs = (
            ("lockfile_bound", True, "lockfile_ref"),
            ("origin_status", "PASS", "dependency_origin_policy_ref"),
            ("attestation_status", "VERIFIED", "attestation_ref"),
            ("sbom_status", "VERIFIED", "sbom_ref"),
            ("license_status", "VERIFIED", "license_evidence_ref"),
            ("vulnerability_status", "CLEAR", "vulnerability_evidence_ref"),
            ("adapter_boundary_status", "VERIFIED", "adapter_evidence_ref"),
            ("network_behavior_status", "DECLARED", "network_behavior_ref"),
            ("removal_status", "VERIFIED", "removal_test_ref"),
            ("rollback_status", "VERIFIED", "rollback_ref"),
        )
        evidence = candidate.get("evidence_refs")
        evidence_set = set(evidence) if isinstance(evidence, list) else set()
        for status_key, good, ref_key in verified_refs:
            if checks.get(status_key) == good:
                ref = checks.get(ref_key)
                if not isinstance(ref, str):
                    findings.append(Finding("VERIFIED_EVIDENCE_REFERENCE_MISSING", f"/checks/{ref_key}"))
                elif ref not in evidence_set:
                    findings.append(Finding("VERIFIED_EVIDENCE_REFERENCE_UNBOUND", f"/checks/{ref_key}"))

    if candidate.get("review_state") != "HOLD":
        findings.append(Finding("REVIEW_STATE_OVERCLAIM", "/review_state"))
    if candidate.get("effects") != FALSE_EFFECTS:
        findings.append(Finding("AUTHORITY_EFFECT_OVERCLAIM", "/effects"))

    current = set(findings)
    expected_recommendation = (
        "DENY" if any(item.code not in ABSTAIN_CODES for item in current)
        else "HOLD" if current
        else "READY_FOR_REVIEW"
    )
    if candidate.get("recommendation") != expected_recommendation:
        findings.append(Finding("RECOMMENDATION_MISMATCH", "/recommendation"))

    try:
        expected_hash = canonical_spec_hash(candidate)
        expected_id = expected_assessment_id(candidate)
    except RuntimeError:
        findings.append(Finding("HASHING_UNAVAILABLE", "/spec_hash"))
    else:
        if candidate.get("spec_hash") != expected_hash:
            findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
        if candidate.get("assessment_id") != expected_id:
            findings.append(Finding("RENDERER_PLUGIN_ASSESSMENT_ID_MISMATCH", "/assessment_id"))
    return findings


def validate_payload(candidate: Mapping[str, Any]) -> ValidationResult:
    findings = _schema_findings(candidate)
    if not findings:
        findings.extend(_semantic(candidate))
    ordered = tuple(sorted(set(findings)))
    if not ordered:
        return ValidationResult("PASS", ordered)
    if any(item.code in ERROR_CODES or item.code == "SCHEMA_INVALID" for item in ordered):
        return ValidationResult("ERROR", ordered)
    if all(item.code in ABSTAIN_CODES for item in ordered):
        return ValidationResult("ABSTAIN", ordered)
    return ValidationResult("DENY", ordered)


def validate_file(path: Path) -> ValidationResult:
    candidate, findings = _read(path)
    if candidate is None:
        return ValidationResult("ERROR", tuple(sorted(set(findings))))
    return validate_payload(candidate)


def _set(candidate: dict[str, Any], pointer: str, value: Any) -> None:
    parts = [part.replace("~1", "/").replace("~0", "~") for part in pointer.lstrip("/").split("/") if part]
    current: Any = candidate
    for part in parts[:-1]:
        current = current[int(part)] if isinstance(current, list) else current[part]
    last = parts[-1]
    if isinstance(current, list):
        current[int(last)] = copy.deepcopy(value)
    else:
        current[last] = copy.deepcopy(value)


def _fixture_document() -> dict[str, Any]:
    document, findings = _read(CASES)
    if (
        document is None
        or findings
        or document.get("profile") != "kfm.map.renderer-plugin-admission-assessment-fixtures.v1"
        or not isinstance(document.get("base"), dict)
        or not isinstance(document.get("cases"), list)
    ):
        raise ValueError("invalid fixture manifest")
    return document


def materialize_case(document: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    candidate = copy.deepcopy(document["base"])
    for mutation in case.get("mutations", []):
        _set(candidate, mutation["path"], mutation["value"])
    candidate = assign_identity(candidate)
    mode = case.get("identity_mode", "RECOMPUTE")
    if mode == "MISMATCH_SPEC_HASH":
        candidate["spec_hash"] = "sha256:" + "0" * 64
    elif mode == "MISMATCH_ID":
        candidate["assessment_id"] = "renderer-plugin-assessment:" + "0" * 24
    elif mode != "RECOMPUTE":
        raise ValueError("unknown identity mode")
    return candidate


def load_fixture_cases() -> list[tuple[dict[str, Any], dict[str, Any]]]:
    document = _fixture_document()
    output: list[tuple[dict[str, Any], dict[str, Any]]] = []
    names: set[str] = set()
    for raw in document["cases"]:
        if not isinstance(raw, dict) or not isinstance(raw.get("name"), str) or raw["name"] in names:
            raise ValueError("invalid fixture case")
        names.add(raw["name"])
        output.append((raw, materialize_case(document, raw)))
    return output


def _serialize(result: ValidationResult, *, path: Path | None = None, case: str | None = None) -> str:
    payload: dict[str, Any] = {
        "outcome": result.outcome,
        "findings": [{"code": item.code, "path": item.path} for item in result.findings],
        "scope": SCOPE,
        "authority": {
            key: False
            for key in (
                "registry_query", "download", "install", "import", "renderer_boot",
                "network_probe", "lockfile_mutation", "policy", "human_review",
                "release", "deployment", "publication",
            )
        },
    }
    if path is not None:
        try:
            payload["file"] = path.resolve().relative_to(ROOT.resolve()).as_posix()
        except (OSError, ValueError):
            payload["file"] = path.name
    if case is not None:
        payload["case"] = case
    return json.dumps(payload, sort_keys=True, separators=(",", ":"))


def replay_fixtures() -> int:
    try:
        cases = load_fixture_cases()
    except (OSError, UnicodeError, ValueError, RecursionError):
        result = ValidationResult("ERROR", (Finding("FIXTURE_MANIFEST_INVALID", "/"),))
        print(_serialize(result, path=CASES))
        return 1
    ok = True
    for definition, candidate in cases:
        result = validate_payload(candidate)
        expected = tuple(
            Finding(item["code"], item["path"])
            for item in definition.get("expected_findings", [])
        )
        matches = result.outcome == definition.get("expected_outcome") and result.findings == expected
        print(json.dumps({
            "case": definition["name"],
            "outcome": result.outcome,
            "findings": [{"code": item.code, "path": item.path} for item in result.findings],
            "matches_expected": matches,
            "scope": SCOPE,
        }, sort_keys=True, separators=(",", ":")))
        ok &= matches
    return 0 if ok else 1


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Validate an inactive RendererPluginAdmissionAssessment candidate.")
    parser.add_argument("file", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(list(sys.argv[1:] if argv is None else argv))
    if args.fixtures and args.file is not None:
        print("--fixtures cannot be combined with a file", file=sys.stderr)
        return 2
    if args.fixtures:
        return replay_fixtures()
    if args.file is None:
        print("a fixture file or --fixtures is required", file=sys.stderr)
        return 2
    result = validate_file(args.file)
    print(_serialize(result, path=args.file))
    return 0 if result.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
