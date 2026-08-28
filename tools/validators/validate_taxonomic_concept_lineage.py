#!/usr/bin/env python3
"""Validate proposed taxonomic concept and name-usage lineage packets."""

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
SCHEMA_PATH = REPO_ROOT / "schemas/contracts/v1/crosswalks/taxonomy/taxonomic_concept_lineage.schema.json"
MAX_FILE_BYTES = 1_048_576
MAX_SCHEMA_FINDINGS = 100
SCOPE = "taxonomic-concept-and-name-usage-lineage-only"


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
        return any(item.code in {
            "FILE_NOT_FOUND", "FILE_READ_ERROR", "FILE_TOO_LARGE",
            "INPUT_SYMLINK_DENIED", "JSON_COMPLEXITY_LIMIT",
            "JSON_DUPLICATE_KEY", "JSON_INVALID", "JSON_NONFINITE_NUMBER",
            "JSON_NOT_UTF8", "ROOT_NOT_OBJECT", "SCHEMA_UNAVAILABLE",
        } for item in self.findings)


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

    usages = {
        item.get("usage_id"): item
        for item in (_mapping(raw) for raw in _array(candidate.get("name_usages")))
        if isinstance(item.get("usage_id"), str)
    }
    concepts = {
        item.get("concept_id"): item
        for item in (_mapping(raw) for raw in _array(candidate.get("taxon_concepts")))
        if isinstance(item.get("concept_id"), str)
    }

    for index, raw in enumerate(_array(candidate.get("concept_relations"))):
        relation = _mapping(raw)
        source = relation.get("from_concept_ref")
        target = relation.get("to_concept_ref")
        if source not in concepts or target not in concepts:
            findings.append(Finding("RELATION_CONCEPT_UNRESOLVED", f"/concept_relations/{index}"))
        if source == target:
            findings.append(Finding("RELATION_SELF_LOOP_DENIED", f"/concept_relations/{index}"))

    for index, raw in enumerate(_array(candidate.get("taxon_concepts"))):
        concept = _mapping(raw)
        if concept.get("accepted_usage_ref") not in usages:
            findings.append(Finding("CONCEPT_USAGE_UNRESOLVED", f"/taxon_concepts/{index}/accepted_usage_ref"))

    unresolved_statuses = {"MISAPPLIED", "HOMONYM", "UNRESOLVED"}
    for index, raw in enumerate(_array(candidate.get("reconciliation_decisions"))):
        decision = _mapping(raw)
        usage_refs = [ref for ref in _array(decision.get("usage_refs")) if isinstance(ref, str)]
        concept_refs = [ref for ref in _array(decision.get("concept_refs")) if isinstance(ref, str)]
        if any(ref not in usages for ref in usage_refs):
            findings.append(Finding("DECISION_USAGE_UNRESOLVED", f"/reconciliation_decisions/{index}/usage_refs"))
        if any(ref not in concepts for ref in concept_refs):
            findings.append(Finding("DECISION_CONCEPT_UNRESOLVED", f"/reconciliation_decisions/{index}/concept_refs"))
        if decision.get("outcome") in {"ACCEPT", "PROVISIONAL"} and not concept_refs:
            findings.append(Finding("DECISION_CONCEPT_REQUIRED", f"/reconciliation_decisions/{index}/concept_refs"))
        statuses = {usages[ref].get("usage_status") for ref in usage_refs if ref in usages}
        if decision.get("outcome") == "ACCEPT" and statuses.intersection(unresolved_statuses):
            findings.append(Finding("UNRESOLVED_USAGE_ACCEPTED", f"/reconciliation_decisions/{index}/outcome"))
        if decision.get("automatic_resolution") is not False:
            findings.append(Finding("AUTOMATIC_TAXONOMY_RESOLUTION_DENIED", f"/reconciliation_decisions/{index}/automatic_resolution"))
        if decision.get("reversible") is not True:
            findings.append(Finding("DECISION_NOT_REVERSIBLE", f"/reconciliation_decisions/{index}/reversible"))

    separation = _mapping(candidate.get("separation"))
    if separation.get("name_string_is_not_identity") is not True:
        findings.append(Finding("NAME_STRING_IDENTITY_COLLAPSE", "/separation/name_string_is_not_identity"))
    for name in (
        "source_native_ids_preserved",
        "concept_circumscription_versioned",
        "unresolved_conflict_preserved",
        "taxonomy_is_not_occurrence_evidence",
    ):
        if separation.get(name) is not True:
            findings.append(Finding("TAXONOMY_SEPARATION_VIOLATION", f"/separation/{name}"))

    governance = _mapping(candidate.get("governance"))
    flags = (
        "taxonomic_authority_created",
        "occurrence_evidence_claimed",
        "distribution_claimed",
        "source_admitted",
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


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("paths", nargs="+", type=Path)
    args = parser.parse_args(argv)
    exit_code = 0
    for path in args.paths:
        result = validate_packet(path)
        print(_serialize(path, result))
        if not result.ok:
            exit_code = max(exit_code, 2 if result.error else 1)
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
