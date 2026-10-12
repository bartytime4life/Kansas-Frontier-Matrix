#!/usr/bin/env python3
"""Validate proposed reversible entity reconciliation packets without network access."""

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

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/common/reversible_entity_reconciliation.schema.json"
FIXTURE_ROOT = REPO_ROOT / "fixtures/contracts/v1/common/reversible_entity_reconciliation"
MAX_FILE_BYTES = 1_048_576
MAX_SCHEMA_FINDINGS = 100
SCOPE = "reversible-entity-reconciliation-only"


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
    def error(self) -> bool:
        return any(
            item.code
            in {
                "FILE_NOT_FOUND",
                "FILE_READ_ERROR",
                "FILE_TOO_LARGE",
                "INPUT_SYMLINK_DENIED",
                "JSON_COMPLEXITY_LIMIT",
                "JSON_DUPLICATE_KEY",
                "JSON_INVALID",
                "JSON_NONFINITE_NUMBER",
                "JSON_NOT_UTF8",
                "ROOT_NOT_OBJECT",
                "SCHEMA_UNAVAILABLE",
            }
            for item in self.findings
        )


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError(key)
        value[key] = item
    return value


def _reject_nonfinite(_value: str) -> None:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
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
                parse_float=_finite_float,
            )
    except UnicodeDecodeError:
        return None, [Finding("JSON_NOT_UTF8", "/")]
    except DuplicateKeyError:
        return None, [Finding("JSON_DUPLICATE_KEY", "/")]
    except NonFiniteNumberError:
        return None, [Finding("JSON_NONFINITE_NUMBER", "/")]
    except json.JSONDecodeError:
        return None, [Finding("JSON_INVALID", "/")]
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


def _mapping(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}


def _array(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []


def _sorted_unique_strings(values: list[Any]) -> bool:
    return all(isinstance(item, str) for item in values) and values == sorted(set(values))


def canonical_spec_hash(candidate: Mapping[str, Any]) -> str:
    projected = dict(candidate)
    projected.pop("spec_hash", None)
    encoded = json.dumps(
        projected,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=False,
        allow_nan=False,
    ).encode("utf-8")
    return "sha256:" + hashlib.sha256(encoded).hexdigest()


def _unique_id_map(records: list[Any], key: str, duplicate_code: str, field: str, findings: list[Finding]) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for index, raw in enumerate(records):
        record = _mapping(raw)
        value = record.get(key)
        if isinstance(value, str):
            if value in result:
                findings.append(Finding(duplicate_code, f"{field}/{index}/{key}"))
            else:
                result[value] = record
    return result


def _semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []

    supplied_hash = candidate.get("spec_hash")
    if isinstance(supplied_hash, str):
        try:
            expected_hash = canonical_spec_hash(candidate)
        except (TypeError, ValueError, RecursionError):
            expected_hash = None
        if expected_hash is not None and supplied_hash != expected_hash:
            findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))

    assertions_raw = _array(candidate.get("source_assertions"))
    proposals_raw = _array(candidate.get("match_proposals"))
    decisions_raw = _array(candidate.get("reconciliation_decisions"))
    clusters_raw = _array(candidate.get("entity_clusters"))
    splits_raw = _array(candidate.get("split_decisions"))

    assertions = _unique_id_map(assertions_raw, "assertion_id", "DUPLICATE_ASSERTION_ID", "/source_assertions", findings)
    proposals = _unique_id_map(proposals_raw, "proposal_id", "DUPLICATE_PROPOSAL_ID", "/match_proposals", findings)
    decisions = _unique_id_map(decisions_raw, "decision_id", "DUPLICATE_DECISION_ID", "/reconciliation_decisions", findings)
    clusters = _unique_id_map(clusters_raw, "cluster_id", "DUPLICATE_CLUSTER_ID", "/entity_clusters", findings)
    _unique_id_map(splits_raw, "split_id", "DUPLICATE_SPLIT_ID", "/split_decisions", findings)

    for index, raw in enumerate(assertions_raw):
        assertion = _mapping(raw)
        for name in ("attribute_digests", "evidence_refs"):
            values = _array(assertion.get(name))
            if not _sorted_unique_strings(values):
                findings.append(Finding("REFS_NOT_CANONICAL", f"/source_assertions/{index}/{name}"))

    for index, raw in enumerate(proposals_raw):
        proposal = _mapping(raw)
        refs = _array(proposal.get("candidate_assertion_refs"))
        if not _sorted_unique_strings(refs):
            findings.append(Finding("REFS_NOT_CANONICAL", f"/match_proposals/{index}/candidate_assertion_refs"))
        missing = [ref for ref in refs if ref not in assertions]
        if missing:
            findings.append(Finding("PROPOSAL_ASSERTION_UNRESOLVED", f"/match_proposals/{index}/candidate_assertion_refs"))
        for name in ("blocking_keys", "evidence_refs"):
            values = _array(proposal.get(name))
            if not _sorted_unique_strings(values):
                findings.append(Finding("REFS_NOT_CANONICAL", f"/match_proposals/{index}/{name}"))
        if proposal.get("automatic_merge") is not False or proposal.get("decision_required") is not True:
            findings.append(Finding("AUTO_MERGE_DENIED", f"/match_proposals/{index}"))
        confidence = proposal.get("confidence")
        limit = proposal.get("confidence_limit")
        if isinstance(confidence, (int, float)) and isinstance(limit, (int, float)) and confidence > limit:
            findings.append(Finding("CONFIDENCE_LIMIT_EXCEEDED", f"/match_proposals/{index}/confidence"))
        features = [_mapping(item) for item in _array(proposal.get("feature_evidence"))]
        if not any(item.get("comparison") == "SAME" for item in features):
            findings.append(Finding("MATCH_SUPPORT_ABSENT", f"/match_proposals/{index}/feature_evidence"))

    for index, raw in enumerate(decisions_raw):
        decision = _mapping(raw)
        if decision.get("proposal_ref") not in proposals:
            findings.append(Finding("DECISION_PROPOSAL_UNRESOLVED", f"/reconciliation_decisions/{index}/proposal_ref"))
        for name in ("rationale_codes", "evidence_refs"):
            values = _array(decision.get(name))
            if not _sorted_unique_strings(values):
                findings.append(Finding("REFS_NOT_CANONICAL", f"/reconciliation_decisions/{index}/{name}"))
        if decision.get("reversible") is not True:
            findings.append(Finding("DECISION_NOT_REVERSIBLE", f"/reconciliation_decisions/{index}/reversible"))

    occupied: set[str] = set()
    for index, raw in enumerate(clusters_raw):
        cluster = _mapping(raw)
        members = _array(cluster.get("member_assertion_refs"))
        decision_refs = _array(cluster.get("decision_refs"))
        if not _sorted_unique_strings(members):
            findings.append(Finding("REFS_NOT_CANONICAL", f"/entity_clusters/{index}/member_assertion_refs"))
        if not _sorted_unique_strings(decision_refs):
            findings.append(Finding("REFS_NOT_CANONICAL", f"/entity_clusters/{index}/decision_refs"))
        if any(ref not in assertions for ref in members):
            findings.append(Finding("CLUSTER_ASSERTION_UNRESOLVED", f"/entity_clusters/{index}/member_assertion_refs"))
        match_decisions = [decisions.get(ref) for ref in decision_refs]
        if not match_decisions or any(item is None or item.get("outcome") != "MATCH" for item in match_decisions):
            findings.append(Finding("CLUSTER_WITHOUT_MATCH_DECISION", f"/entity_clusters/{index}/decision_refs"))
        covered: set[str] = set()
        for decision in match_decisions:
            if not decision:
                continue
            proposal = proposals.get(decision.get("proposal_ref"))
            if proposal:
                covered.update(ref for ref in _array(proposal.get("candidate_assertion_refs")) if isinstance(ref, str))
        if any(ref not in covered for ref in members):
            findings.append(Finding("CLUSTER_MEMBER_NOT_DECISION_COVERED", f"/entity_clusters/{index}/member_assertion_refs"))
        overlap = occupied.intersection(ref for ref in members if isinstance(ref, str))
        if overlap:
            findings.append(Finding("OVERLAPPING_ACTIVE_CLUSTERS", f"/entity_clusters/{index}/member_assertion_refs"))
        occupied.update(ref for ref in members if isinstance(ref, str))
        if cluster.get("source_assertions_preserved") is not True or cluster.get("transitive_closure_applied") is not False:
            findings.append(Finding("DESTRUCTIVE_OR_TRANSITIVE_CLUSTER_DENIED", f"/entity_clusters/{index}"))

    for index, raw in enumerate(splits_raw):
        split = _mapping(raw)
        cluster = clusters.get(split.get("prior_cluster_ref"))
        if cluster is None:
            findings.append(Finding("SPLIT_CLUSTER_UNRESOLVED", f"/split_decisions/{index}/prior_cluster_ref"))
            continue
        sets = _array(split.get("resulting_member_sets"))
        flattened: list[str] = []
        for member_set in sets:
            flattened.extend(item for item in _array(member_set) if isinstance(item, str))
        if len(flattened) != len(set(flattened)):
            findings.append(Finding("SPLIT_MEMBER_DUPLICATED", f"/split_decisions/{index}/resulting_member_sets"))
        prior_members = set(item for item in _array(cluster.get("member_assertion_refs")) if isinstance(item, str))
        if set(flattened) != prior_members:
            findings.append(Finding("SPLIT_PARTITION_MISMATCH", f"/split_decisions/{index}/resulting_member_sets"))
        for name in ("reason_codes", "evidence_refs"):
            values = _array(split.get(name))
            if not _sorted_unique_strings(values):
                findings.append(Finding("REFS_NOT_CANONICAL", f"/split_decisions/{index}/{name}"))
        if split.get("reversible") is not True:
            findings.append(Finding("SPLIT_NOT_REVERSIBLE", f"/split_decisions/{index}/reversible"))

    separation = _mapping(candidate.get("separation"))
    if any(
        separation.get(name) is not True
        for name in (
            "source_assertions_preserved",
            "winner_takes_all_denied",
            "destructive_merge_denied",
            "confidence_is_not_authority",
            "unresolved_is_first_class",
        )
    ):
        findings.append(Finding("DESTRUCTIVE_RECONCILIATION_DENIED", "/separation"))

    provenance = _mapping(candidate.get("provenance"))
    if not _sorted_unique_strings(_array(provenance.get("input_refs"))):
        findings.append(Finding("REFS_NOT_CANONICAL", "/provenance/input_refs"))

    governance = _mapping(candidate.get("governance"))
    flags = (
        "authority_created",
        "canonical_entity_created",
        "source_assertions_mutated",
        "evidence_closure_claimed",
        "policy_evaluated",
        "promotion_authorized",
        "release_authorized",
        "publication_authorized",
    )
    if any(governance.get(name) is not False for name in flags) or governance.get("release_ref") is not None:
        findings.append(Finding("GOVERNANCE_BOUNDARY_VIOLATION", "/governance"))

    return findings


def validate_packet(path: Path) -> ValidationResult:
    candidate, findings = _read_object(path)
    if candidate is None:
        return ValidationResult(tuple(sorted(set(findings))))
    findings.extend(_schema_findings(candidate))
    findings.extend(_semantic_findings(candidate))
    return ValidationResult(tuple(sorted(set(findings))))


def _display_path(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()
    except (OSError, ValueError):
        return path.name


def _serialize(path: Path, result: ValidationResult) -> str:
    return json.dumps(
        {
            "file": _display_path(path),
            "findings": [{"code": item.code, "field": item.field} for item in result.findings],
            "outcome": "PASS" if result.ok else ("ERROR" if result.error else "FAIL"),
            "scope": SCOPE,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def _expected_manifest() -> dict[str, list[str]]:
    path = FIXTURE_ROOT / "invalid/expected_findings_manifest.json"
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("expected findings manifest must be an object")
    return {
        str(name): sorted(str(code) for code in codes)
        for name, codes in value.items()
        if isinstance(codes, list)
    }


def validate_fixtures() -> int:
    expected = _expected_manifest()
    failures: list[str] = []
    valid_files = sorted((FIXTURE_ROOT / "valid").glob("*.json"))
    invalid_files = sorted(
        path
        for path in (FIXTURE_ROOT / "invalid").glob("*.json")
        if path.name != "expected_findings_manifest.json"
    )
    if not valid_files or not invalid_files:
        print("fixture inventory is incomplete", file=sys.stderr)
        return 2
    for path in valid_files:
        result = validate_packet(path)
        if not result.ok:
            failures.append(f"{path.name}: expected PASS, got {[item.code for item in result.findings]}")
    for path in invalid_files:
        result = validate_packet(path)
        actual = sorted(set(item.code for item in result.findings))
        wanted = expected.get(path.name)
        if wanted is None:
            failures.append(f"{path.name}: missing expected findings")
        elif actual != wanted:
            failures.append(f"{path.name}: expected {wanted}, got {actual}")
    extra = sorted(set(expected) - {path.name for path in invalid_files})
    if extra:
        failures.append(f"manifest references absent fixtures: {extra}")
    if failures:
        for failure in failures:
            print(failure, file=sys.stderr)
        return 1
    print(f"CONFIRMED: {len(valid_files)} valid and {len(invalid_files)} invalid reconciliation fixtures passed exact polarity.")
    return 0


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="*", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        return validate_fixtures()
    if not args.paths:
        parser.error("provide at least one JSON path or --fixtures")
    exit_code = 0
    for path in args.paths:
        result = validate_packet(path)
        print(_serialize(path, result))
        if not result.ok:
            exit_code = max(exit_code, 2 if result.error else 1)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
