#!/usr/bin/env python3
"""Validate fixture-only GraphInvariantArtifactCandidate records."""

from __future__ import annotations

import argparse
import copy
import json
import math
import sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
HASHING_SRC = ROOT / "packages/hashing/src"
if str(HASHING_SRC) not in sys.path:
    sys.path.insert(0, str(HASHING_SRC))
from hashing import CanonicalizationFailure, compute_spec_hash

SCHEMA = ROOT / "schemas/contracts/v1/evidence/graph_invariant_artifact.schema.json"
CASES = ROOT / "fixtures/contracts/v1/evidence/graph_invariant_artifact/cases.json"
IDENTITY_PREFIX = "kfm:graph-invariant-artifact:"
MAX_BYTES = 2 * 1024 * 1024
MAX_SCHEMA_FINDINGS = 50


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class Result:
    outcome: str
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return self.outcome == "PASS" and not self.findings


def _unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _reject_constant(_value: str) -> None:
    raise NonFiniteNumberError


def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed


def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace("~", "~0").replace("/", "~1") for part in parts]
    return "/" + "/".join(encoded) if encoded else "/"


def _read(path: Path) -> tuple[dict[str, Any] | None, tuple[Finding, ...]]:
    try:
        if path.is_symlink():
            return None, (Finding("INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("INPUT_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject_constant,
            parse_float=_finite_float,
        )
    except DuplicateKeyError:
        return None, (Finding("JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("JSON_NONFINITE_NUMBER", "/"),)
    except (UnicodeError, json.JSONDecodeError):
        return None, (Finding("JSON_INVALID", "/"),)
    except OSError:
        return None, (Finding("INPUT_READ_ERROR", "/"),)
    except (RecursionError, ValueError):
        return None, (Finding("JSON_COMPLEXITY_LIMIT", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("ROOT_NOT_OBJECT", "/"),)
    return value, ()


def identity_subject(value: Mapping[str, Any]) -> dict[str, Any]:
    subject = copy.deepcopy(dict(value))
    subject.pop("artifact_id", None)
    subject.pop("spec_hash", None)
    return subject


def canonical_identity(value: Mapping[str, Any]) -> tuple[str, str]:
    spec_hash = compute_spec_hash(identity_subject(value))
    return spec_hash, IDENTITY_PREFIX + spec_hash.split(":", 1)[1][:24]


def _merge(target: dict[str, Any], patch: Mapping[str, Any]) -> None:
    for key, value in patch.items():
        if isinstance(value, dict) and isinstance(target.get(key), dict):
            _merge(target[key], value)
        else:
            target[key] = copy.deepcopy(value)


def materialize_case(corpus: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    candidate = copy.deepcopy(corpus["base"])
    spec_hash, artifact_id = canonical_identity(candidate)
    candidate["spec_hash"] = spec_hash
    candidate["artifact_id"] = artifact_id
    _merge(candidate, case.get("patch", {}))
    if case.get("recompute_identity", True):
        spec_hash, artifact_id = canonical_identity(candidate)
        candidate["spec_hash"] = spec_hash
        candidate["artifact_id"] = artifact_id
    return candidate


def _schema_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = list(
            islice(
                Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(candidate),
                MAX_SCHEMA_FINDINGS + 1,
            )
        )
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


def _canonical_records(items: Sequence[Mapping[str, Any]], key: str) -> bool:
    names = [item[key] for item in items]
    return names == sorted(set(names))


def _record_map(items: Sequence[Mapping[str, Any]], key: str) -> dict[str, Mapping[str, Any]]:
    return {item[key]: item for item in items}


def _semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    before = candidate["before"]
    after = candidate["after"]
    comparison = candidate["comparison"]

    fields = (
        ("node_counts", "name"),
        ("relationship_counts", "name"),
        ("constraints", "name"),
        ("representative_queries", "query_id"),
        ("gds_procedures", "procedure_id"),
    )
    for side_name, snapshot in (("before", before), ("after", after)):
        for field, key in fields:
            if not _canonical_records(snapshot[field], key):
                findings.append(Finding("SNAPSHOT_NOT_CANONICAL", f"/{side_name}/{field}"))

    comparison_fields = (
        ("node_count_deltas", "name"),
        ("relationship_count_deltas", "name"),
    )
    comparison_canonical: dict[str, bool] = {}
    for field, key in comparison_fields:
        comparison_canonical[field] = _canonical_records(comparison[field], key)
        if not comparison_canonical[field]:
            findings.append(Finding("COMPARISON_NOT_CANONICAL", f"/comparison/{field}"))
    for field in ("constraint_regressions", "changed_queries", "changed_gds_procedures"):
        values = comparison[field]
        if values != sorted(set(values)):
            findings.append(Finding("COMPARISON_NOT_CANONICAL", f"/comparison/{field}"))

    before_maps = {field: _record_map(before[field], key) for field, key in fields}
    after_maps = {field: _record_map(after[field], key) for field, key in fields}
    comparable = True
    for field, _key in fields:
        if set(before_maps[field]) != set(after_maps[field]):
            comparable = False
            findings.append(Finding("SNAPSHOT_KEYSET_MISMATCH", f"/{field}"))

    if comparable:
        expected_nodes = [
            {"name": name, "delta": after_maps["node_counts"][name]["count"] - before_maps["node_counts"][name]["count"]}
            for name in sorted(before_maps["node_counts"])
        ]
        expected_relationships = [
            {"name": name, "delta": after_maps["relationship_counts"][name]["count"] - before_maps["relationship_counts"][name]["count"]}
            for name in sorted(before_maps["relationship_counts"])
        ]
        expected_regressions = sorted(
            name
            for name in before_maps["constraints"]
            if before_maps["constraints"][name]["status"] == "SATISFIED"
            and after_maps["constraints"][name]["status"] != "SATISFIED"
        )
        expected_queries = sorted(
            name
            for name in before_maps["representative_queries"]
            if before_maps["representative_queries"][name] != after_maps["representative_queries"][name]
        )
        expected_gds = sorted(
            name
            for name in before_maps["gds_procedures"]
            if before_maps["gds_procedures"][name] != after_maps["gds_procedures"][name]
        )
        if comparison_canonical["node_count_deltas"] and comparison["node_count_deltas"] != expected_nodes:
            findings.append(Finding("NODE_DELTA_MISMATCH", "/comparison/node_count_deltas"))
        if comparison_canonical["relationship_count_deltas"] and comparison["relationship_count_deltas"] != expected_relationships:
            findings.append(Finding("RELATIONSHIP_DELTA_MISMATCH", "/comparison/relationship_count_deltas"))
        if comparison["constraint_regressions"] != expected_regressions:
            findings.append(Finding("CONSTRAINT_REGRESSION_MISMATCH", "/comparison/constraint_regressions"))
        if comparison["changed_queries"] != expected_queries:
            findings.append(Finding("QUERY_CHANGE_MISMATCH", "/comparison/changed_queries"))
        if comparison["changed_gds_procedures"] != expected_gds:
            findings.append(Finding("GDS_CHANGE_MISMATCH", "/comparison/changed_gds_procedures"))

    declared_change = (
        any(item["delta"] != 0 for item in comparison["node_count_deltas"])
        or any(item["delta"] != 0 for item in comparison["relationship_count_deltas"])
        or bool(comparison["constraint_regressions"])
        or bool(comparison["changed_queries"])
        or bool(comparison["changed_gds_procedures"])
    )
    expected_classification = "REVIEW_REQUIRED" if declared_change else "NO_DRIFT"
    if comparison["classification"] != expected_classification:
        findings.append(Finding("CLASSIFICATION_MISMATCH", "/comparison/classification"))

    try:
        expected_hash, expected_id = canonical_identity(candidate)
    except CanonicalizationFailure:
        findings.append(Finding("IDENTITY_CANONICALIZATION_ERROR", "/"))
    else:
        if candidate.get("spec_hash") != expected_hash:
            findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
        if candidate.get("artifact_id") != expected_id:
            findings.append(Finding("ARTIFACT_ID_MISMATCH", "/artifact_id"))
    return findings


def validate_candidate(candidate: Mapping[str, Any]) -> Result:
    findings = _schema_findings(candidate)
    if not findings:
        findings = _semantic_findings(candidate)
    unique = tuple(sorted(set(findings)))
    return Result("PASS" if not unique else "FAIL", unique)


def validate_record(path: Path) -> Result:
    value, findings = _read(path)
    if findings or value is None:
        return Result("FAIL", findings)
    return validate_candidate(value)


def _fixture_results() -> int:
    corpus, findings = _read(CASES)
    if findings or corpus is None:
        print(json.dumps({"outcome": "FAIL", "findings": [item.code for item in findings]}, sort_keys=True))
        return 1
    exit_code = 0
    for case in corpus["cases"]:
        result = validate_candidate(materialize_case(corpus, case))
        actual = sorted({item.code for item in result.findings})
        expected = case["expected"]
        matched = result.outcome == expected["outcome"] and actual == expected["findings"]
        print(json.dumps({"id": case["id"], "outcome": result.outcome, "findings": actual, "matched": matched}, sort_keys=True))
        if not matched:
            exit_code = 1
    return exit_code


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--fixtures", action="store_true")
    group.add_argument("record", nargs="?", type=Path)
    args = parser.parse_args()
    if args.fixtures:
        return _fixture_results()
    result = validate_record(args.record)
    print(json.dumps({"outcome": result.outcome, "findings": [{"code": item.code, "path": item.path} for item in result.findings]}, sort_keys=True))
    return 0 if result.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
