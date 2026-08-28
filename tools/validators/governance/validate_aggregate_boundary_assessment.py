"""Validate fixture-only aggregate boundary assessment candidates.

The validator checks one declared aggregate root, members, invariants, reference
edges, repository/factory posture, and consistency boundary. It does not create
or mutate objects, execute persistence or transactions, resolve references or
evidence, change schemas or registers, decide policy or review, or grant
promotion, release, deployment, publication, or public-use authority.
"""

from __future__ import annotations

import argparse
import copy
import hashlib
import json
import math
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/governance/aggregate_boundary_assessment.schema.json"
FIXTURE_PATH = REPO_ROOT / "fixtures/contracts/v1/governance/aggregate_boundary_assessment/cases.json"
MAX_FILE_BYTES = 1_048_576
IDENTITY_PREFIX = "kfm:aggregate-boundary:"
ABSTAIN_CODES = {
    "AGGREGATE_BOUNDARY_UNRESOLVED",
    "FACTORY_PROFILE_UNRESOLVED",
    "IDENTITY_ASSESSMENT_UNRESOLVED",
    "INVARIANT_COVERAGE_INCOMPLETE",
    "INVARIANT_COVERAGE_UNKNOWN",
    "OBJECT_FAMILY_BINDING_UNRESOLVED",
    "OBJECT_FAMILY_NOT_REGISTERED",
    "REPOSITORY_PROFILE_UNRESOLVED",
    "REVIEW_PENDING",
    "REVIEW_UNKNOWN",
}
DIRECT_STORE_MARKERS = (
    "postgres://",
    "neo4j://",
    "s3://",
    "file://",
    "data/raw",
    "data/work",
    "data/quarantine",
    "raw/",
    "work/",
    "quarantine/",
)
QUERY_MARKERS = ("match (", "select *", "sparql ", "graph_query", "cypher:")


class DuplicateKeyError(ValueError):
    """Raised when a JSON object repeats a member name."""


class NonFiniteNumberError(ValueError):
    """Raised when JSON contains a non-standard non-finite number."""


class UnpairedSurrogateError(ValueError):
    """Raised when text cannot be represented as Unicode scalar values."""


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str


@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]

    @property
    def codes(self) -> list[str]:
        return sorted({finding.code for finding in self.findings})


def _pairs(items: list[tuple[str, object]]) -> dict[str, object]:
    value: dict[str, object] = {}
    for key, item in items:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _nonfinite(_value: str) -> object:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _contains_surrogate(value: object) -> bool:
    if isinstance(value, str):
        return any(0xD800 <= ord(char) <= 0xDFFF for char in value)
    if isinstance(value, Mapping):
        return any(_contains_surrogate(key) or _contains_surrogate(item) for key, item in value.items())
    if isinstance(value, list):
        return any(_contains_surrogate(item) for item in value)
    return False


def load_json_object(path: Path) -> tuple[dict[str, object] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return None, [Finding("INPUT_SYMLINK_DENIED", "/")]
        if not path.is_file():
            return None, [Finding("FILE_NOT_FOUND", "/")]
        if path.stat().st_size > MAX_FILE_BYTES:
            return None, [Finding("FILE_TOO_LARGE", "/")]
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_pairs,
            parse_constant=_nonfinite,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError, ValueError):
        return None, [Finding("JSON_INVALID", "/")]
    if not isinstance(value, dict):
        return None, [Finding("ROOT_NOT_OBJECT", "/")]
    if _contains_surrogate(value):
        return None, [Finding("JSON_UNPAIRED_SURROGATE", "/")]
    return value, []


def canonical_hash(value: object) -> str:
    if _contains_surrogate(value):
        raise UnpairedSurrogateError
    payload = json.dumps(
        value,
        ensure_ascii=False,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(payload).hexdigest()


def compute_profile_hash(candidate: Mapping[str, object]) -> str:
    subject = copy.deepcopy(dict(candidate))
    subject.pop("assessment_id", None)
    subject.pop("profile_spec_hash", None)
    return canonical_hash(subject)


def compute_assessment_id(candidate: Mapping[str, object]) -> str:
    return IDENTITY_PREFIX + compute_profile_hash(candidate).split(":", 1)[1][:24]


def _schema_findings(candidate: object) -> list[Finding]:
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(
        validator.iter_errors(candidate),
        key=lambda error: (list(error.absolute_path), str(error.validator)),
    )
    return [
        Finding("SCHEMA_INVALID", "/" + "/".join(str(part) for part in error.absolute_path))
        for error in errors[:100]
    ]


def _is_utc(value: object) -> bool:
    if not isinstance(value, str) or not value.endswith("Z"):
        return False
    try:
        datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return False
    return True


def _canonical_strings(value: object) -> bool:
    return (
        isinstance(value, list)
        and all(isinstance(item, str) for item in value)
        and value == sorted(set(value))
    )


def _walk_strings(value: object, path: str = "") -> Iterable[tuple[str, str]]:
    if isinstance(value, str):
        yield path or "/", value
    elif isinstance(value, list):
        for index, item in enumerate(value):
            yield from _walk_strings(item, f"{path}/{index}")
    elif isinstance(value, Mapping):
        for key in sorted(value):
            escaped = str(key).replace("~", "~0").replace("/", "~1")
            yield from _walk_strings(value[key], f"{path}/{escaped}")


def _binding_findings(bindings: Mapping[str, object]) -> set[Finding]:
    findings: set[Finding] = set()
    register = bindings["object_family_register"]
    identity = bindings["identity_kind_assessment"]
    assert isinstance(register, Mapping) and isinstance(identity, Mapping)

    register_state = register.get("state")
    if register_state == "RESOLVED":
        if register.get("ref") is None or register.get("digest") is None:
            findings.add(Finding("OBJECT_FAMILY_BINDING_REQUIRED", "/bindings/object_family_register"))
    else:
        if register.get("ref") is not None or register.get("digest") is not None:
            findings.add(Finding("OBJECT_FAMILY_BINDING_PROHIBITED", "/bindings/object_family_register"))
        if register_state == "UNRESOLVED":
            findings.add(Finding("OBJECT_FAMILY_BINDING_UNRESOLVED", "/bindings/object_family_register/state"))
        elif register_state == "NOT_REGISTERED":
            findings.add(Finding("OBJECT_FAMILY_NOT_REGISTERED", "/bindings/object_family_register/state"))

    identity_state = identity.get("state")
    if identity_state == "RESOLVED":
        if identity.get("ref") is None:
            findings.add(Finding("IDENTITY_ASSESSMENT_BINDING_REQUIRED", "/bindings/identity_kind_assessment/ref"))
        if identity.get("root_identity_kind") != "ENTITY":
            findings.add(Finding("AGGREGATE_ROOT_IDENTITY_INCOHERENT", "/bindings/identity_kind_assessment/root_identity_kind"))
    else:
        if identity.get("ref") is not None or identity.get("root_identity_kind") != "UNRESOLVED":
            findings.add(Finding("IDENTITY_ASSESSMENT_BINDING_PROHIBITED", "/bindings/identity_kind_assessment"))
        findings.add(Finding("IDENTITY_ASSESSMENT_UNRESOLVED", "/bindings/identity_kind_assessment/state"))
    return findings


def _member_findings(candidate: Mapping[str, object], declaration: Mapping[str, object]) -> set[Finding]:
    findings: set[Finding] = set()
    members = declaration["members"]
    assert isinstance(members, list)
    member_refs = [item["member_ref"] for item in members]
    if member_refs != sorted(member_refs):
        findings.add(Finding("MEMBERS_NOT_CANONICAL", "/declaration/members"))
    if len(member_refs) != len(set(member_refs)):
        findings.add(Finding("MEMBER_REFERENCE_DUPLICATE", "/declaration/members"))

    root_refs = [item["member_ref"] for item in members if item["role"] == "ROOT"]
    if len(root_refs) != 1:
        findings.add(Finding("AGGREGATE_ROOT_CARDINALITY", "/declaration/members"))
    elif root_refs[0] != declaration.get("aggregate_root_ref"):
        findings.add(Finding("AGGREGATE_ROOT_DECLARATION_MISMATCH", "/declaration/aggregate_root_ref"))
    if declaration.get("aggregate_root_ref") != candidate.get("aggregate_family_ref"):
        findings.add(Finding("AGGREGATE_FAMILY_ROOT_MISMATCH", "/aggregate_family_ref"))
    return findings


def _reference_findings(declaration: Mapping[str, object]) -> set[Finding]:
    findings: set[Finding] = set()
    if declaration.get("external_reference_policy") != "ROOT_ONLY":
        findings.add(Finding("EXTERNAL_REFERENCE_POLICY_INCOHERENT", "/declaration/external_reference_policy"))

    members = declaration["members"]
    edges = declaration["reference_edges"]
    assert isinstance(members, list) and isinstance(edges, list)
    member_refs = {item["member_ref"] for item in members}
    root_ref = declaration.get("aggregate_root_ref")
    observed_order = [
        (edge["scope"], edge["source_ref"], edge["target_member_ref"])
        for edge in edges
    ]
    if observed_order != sorted(set(observed_order)):
        findings.add(Finding("REFERENCE_EDGES_NOT_CANONICAL", "/declaration/reference_edges"))
    for edge in edges:
        if edge["scope"] == "EXTERNAL":
            if edge["source_ref"] in member_refs or edge["target_member_ref"] != root_ref:
                findings.add(Finding("EXTERNAL_REFERENCE_BOUNDARY_VIOLATION", "/declaration/reference_edges"))
        elif edge["source_ref"] not in member_refs or edge["target_member_ref"] not in member_refs:
            findings.add(Finding("INTERNAL_REFERENCE_SCOPE_INCOHERENT", "/declaration/reference_edges"))
    return findings


def _repository_findings(repository: Mapping[str, object], root_ref: object) -> set[Finding]:
    findings: set[Finding] = set()
    state = repository.get("state")
    observed = (
        repository.get("repository_ref"),
        repository.get("exposed_root_ref"),
        repository.get("return_scope"),
        repository.get("direct_internal_member_access"),
    )
    if state == "DECLARED":
        if (
            observed[0] is None
            or observed[1] != root_ref
            or observed[2] != "WHOLE_AGGREGATE_OR_PROXY"
            or observed[3] is not False
        ):
            findings.add(Finding("REPOSITORY_AGGREGATE_SCOPE_INCOHERENT", "/declaration/repository"))
    elif observed != (None, None, None, False):
        findings.add(Finding("REPOSITORY_PROFILE_PROHIBITED", "/declaration/repository"))
    if state == "UNRESOLVED":
        findings.add(Finding("REPOSITORY_PROFILE_UNRESOLVED", "/declaration/repository/state"))
    return findings


def _factory_findings(factory: Mapping[str, object]) -> set[Finding]:
    findings: set[Finding] = set()
    state = factory.get("state")
    observed = (
        factory.get("factory_ref"),
        factory.get("creation_scope"),
        factory.get("enforces_invariants"),
    )
    if state == "DECLARED":
        if observed[0] is None or observed[1] != "WHOLE_AGGREGATE" or observed[2] is not True:
            findings.add(Finding("FACTORY_AGGREGATE_SCOPE_INCOHERENT", "/declaration/factory"))
    elif observed != (None, None, False):
        findings.add(Finding("FACTORY_PROFILE_PROHIBITED", "/declaration/factory"))
    if state == "UNRESOLVED":
        findings.add(Finding("FACTORY_PROFILE_UNRESOLVED", "/declaration/factory/state"))
    return findings


def _declaration_findings(candidate: Mapping[str, object], declaration: Mapping[str, object]) -> set[Finding]:
    findings = _member_findings(candidate, declaration)
    findings.update(_reference_findings(declaration))

    if declaration.get("boundary_state") == "UNRESOLVED":
        findings.add(Finding("AGGREGATE_BOUNDARY_UNRESOLVED", "/declaration/boundary_state"))

    for field in ("invariant_refs", "review_record_refs"):
        if not _canonical_strings(declaration.get(field)):
            findings.add(Finding("ARRAY_NOT_CANONICAL", f"/declaration/{field}"))

    coverage = declaration.get("invariant_coverage")
    if coverage == "INCOMPLETE":
        findings.add(Finding("INVARIANT_COVERAGE_INCOMPLETE", "/declaration/invariant_coverage"))
    elif coverage == "UNKNOWN":
        findings.add(Finding("INVARIANT_COVERAGE_UNKNOWN", "/declaration/invariant_coverage"))

    review_state = declaration.get("review_state")
    review_refs = declaration.get("review_record_refs")
    assert isinstance(review_refs, list)
    if review_state == "PENDING":
        findings.add(Finding("REVIEW_PENDING", "/declaration/review_state"))
    elif review_state == "UNKNOWN":
        findings.add(Finding("REVIEW_UNKNOWN", "/declaration/review_state"))
    elif not review_refs:
        findings.add(Finding("REVIEW_RECORD_REQUIRED", "/declaration/review_record_refs"))
    if review_state == "COMPLETE_FOR_DECLARED_SCOPE" and declaration.get("rationale_summary") is None:
        findings.add(Finding("RATIONALE_SUMMARY_REQUIRED", "/declaration/rationale_summary"))

    repository = declaration["repository"]
    factory = declaration["factory"]
    consistency = declaration["consistency"]
    external_evidence = declaration["external_evidence"]
    assert all(isinstance(item, Mapping) for item in (repository, factory, consistency, external_evidence))
    findings.update(_repository_findings(repository, declaration.get("aggregate_root_ref")))
    findings.update(_factory_findings(factory))

    if consistency != {
        "transaction_unit": "AGGREGATE",
        "within_boundary": "SYNCHRONOUS",
        "cross_boundary": "ASYNCHRONOUS_OR_EXPLICIT_PROCESS",
    }:
        findings.add(Finding("CONSISTENCY_BOUNDARY_INCOHERENT", "/declaration/consistency"))

    evidence_refs = external_evidence.get("evidence_bundle_refs")
    if not _canonical_strings(evidence_refs):
        findings.add(Finding("ARRAY_NOT_CANONICAL", "/declaration/external_evidence/evidence_bundle_refs"))
    if (
        external_evidence.get("relationship") != "REFERENCE_ONLY"
        or external_evidence.get("consistency_scope") != "OUTSIDE_AGGREGATE"
        or external_evidence.get("resolution_authority") is not False
    ):
        findings.add(Finding("EVIDENCE_REFERENCE_BOUNDARY_INCOHERENT", "/declaration/external_evidence"))
    return findings


def _semantic_findings(candidate: Mapping[str, object]) -> list[Finding]:
    findings: set[Finding] = set()
    if candidate.get("profile_spec_hash") != compute_profile_hash(candidate):
        findings.add(Finding("PROFILE_SPEC_HASH_MISMATCH", "/profile_spec_hash"))
    if candidate.get("assessment_id") != compute_assessment_id(candidate):
        findings.add(Finding("ASSESSMENT_ID_MISMATCH", "/assessment_id"))
    if not _is_utc(candidate.get("observed_at")):
        findings.add(Finding("OBSERVED_AT_NOT_UTC", "/observed_at"))

    bindings = candidate["bindings"]
    declaration = candidate["declaration"]
    assert isinstance(bindings, Mapping) and isinstance(declaration, Mapping)
    findings.update(_binding_findings(bindings))
    findings.update(_declaration_findings(candidate, declaration))

    for path, text in _walk_strings(candidate):
        lowered = text.casefold()
        if any(marker in lowered for marker in DIRECT_STORE_MARKERS):
            findings.add(Finding("DIRECT_STORE_REFERENCE_DENIED", path))
        if any(marker in lowered for marker in QUERY_MARKERS):
            findings.add(Finding("EMBEDDED_QUERY_DENIED", path))
    return sorted(findings)


def validate_candidate(candidate: object) -> ValidationResult:
    if _contains_surrogate(candidate):
        return ValidationResult("ERROR", (Finding("JSON_UNPAIRED_SURROGATE", "/"),))
    schema_findings = _schema_findings(candidate)
    if schema_findings:
        return ValidationResult("ERROR", tuple(schema_findings))
    assert isinstance(candidate, dict)
    findings = _semantic_findings(candidate)
    codes = {finding.code for finding in findings}
    if not codes:
        outcome = "PASS"
    elif codes <= ABSTAIN_CODES:
        outcome = "ABSTAIN"
    else:
        outcome = "DENY"
    return ValidationResult(outcome, tuple(findings))


def _merge_patch(base: object, patch: object) -> object:
    if isinstance(base, list) and isinstance(patch, Mapping) and all(
        isinstance(key, str) and key.isdigit() for key in patch
    ):
        target = copy.deepcopy(base)
        for key in sorted(patch, key=int):
            index = int(key)
            if index >= len(target):
                raise ValueError("fixture list patch index out of range")
            target[index] = _merge_patch(target[index], patch[key])
        return target
    if not isinstance(patch, Mapping):
        return copy.deepcopy(patch)
    target = copy.deepcopy(base) if isinstance(base, Mapping) else {}
    assert isinstance(target, dict)
    for key, value in patch.items():
        target[key] = None if value is None else _merge_patch(target.get(key), value)
    return target


def materialize_fixture_case(
    manifest: Mapping[str, object], entry: Mapping[str, object]
) -> dict[str, object]:
    candidate = _merge_patch(manifest["base_candidate"], entry.get("patch", {}))
    if not isinstance(candidate, dict):
        raise ValueError("materialized fixture must be an object")
    candidate["profile_spec_hash"] = compute_profile_hash(candidate)
    candidate["assessment_id"] = compute_assessment_id(candidate)
    if entry.get("tamper") == "profile_hash":
        candidate["profile_spec_hash"] = "sha256:" + "f" * 64
    elif entry.get("tamper") == "assessment_id":
        candidate["assessment_id"] = IDENTITY_PREFIX + "f" * 24
    return candidate


def validate_fixture_manifest(path: Path = FIXTURE_PATH) -> list[dict[str, object]]:
    manifest, load_findings = load_json_object(path)
    if manifest is None:
        return [{
            "name": "fixture_manifest",
            "ok": False,
            "observed": {
                "outcome": "ERROR",
                "codes": sorted({item.code for item in load_findings}),
            },
        }]
    results: list[dict[str, object]] = []
    for entry in manifest["cases"]:
        candidate = materialize_fixture_case(manifest, entry)
        result = validate_candidate(candidate)
        observed = {"outcome": result.outcome, "codes": result.codes}
        expected = entry["expected"]
        results.append({
            "name": entry["name"],
            "ok": observed == expected,
            "expected": expected,
            "observed": observed,
        })
    return results


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate fixture-only aggregate boundary assessments."
    )
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--fixtures", action="store_true")
    group.add_argument("--input", type=Path)
    args = parser.parse_args(argv)
    if args.fixtures:
        results = validate_fixture_manifest()
        print(json.dumps(results, indent=2, sort_keys=True))
        return 0 if all(item["ok"] for item in results) else 1
    candidate, findings = load_json_object(args.input)
    result = (
        ValidationResult("ERROR", tuple(sorted(findings)))
        if candidate is None
        else validate_candidate(candidate)
    )
    print(json.dumps({"outcome": result.outcome, "codes": result.codes}, indent=2, sort_keys=True))
    return 0 if result.outcome == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
