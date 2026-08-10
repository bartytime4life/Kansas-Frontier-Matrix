#!/usr/bin/env python3
"""Validate fixture-only TypedReceiptAggregationCandidate records."""

from __future__ import annotations

import argparse
import copy
import json
import math
import sys
from collections import Counter
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

SCHEMA = ROOT / "schemas/contracts/v1/data/typed_receipt_aggregation.schema.json"
CASES = ROOT / "fixtures/contracts/v1/data/typed_receipt_aggregation/cases.json"
IDENTITY_PREFIX = "kfm:typed-receipt-aggregation:"
MATERIALITY = ("NON_EVENT", "PROMOTION_CANDIDATE", "HOLD", "ERROR")
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
    subject.pop("aggregation_id", None)
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
    spec_hash, aggregation_id = canonical_identity(candidate)
    candidate["spec_hash"] = spec_hash
    candidate["aggregation_id"] = aggregation_id
    _merge(candidate, case.get("patch", {}))
    if case.get("recompute_identity", True):
        spec_hash, aggregation_id = canonical_identity(candidate)
        candidate["spec_hash"] = spec_hash
        candidate["aggregation_id"] = aggregation_id
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


def _canonical_strings(values: object) -> bool:
    return isinstance(values, list) and values == sorted(set(values))


def _semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    entries: Sequence[Mapping[str, Any]] = candidate["entries"]
    summary = candidate["summary"]

    entry_keys = [(entry["receipt_type"], entry["receipt_ref"]) for entry in entries]
    if entry_keys != sorted(entry_keys):
        findings.append(Finding("ENTRY_ORDER_INVALID", "/entries"))
    receipt_refs = [entry["receipt_ref"] for entry in entries]
    if len(receipt_refs) != len(set(receipt_refs)):
        findings.append(Finding("RECEIPT_REF_DUPLICATE", "/entries"))

    artifact_paths: list[str] = []
    for index, entry in enumerate(entries):
        paths = [item["path"] for item in entry["produced_artifacts"]]
        if paths != sorted(set(paths)):
            findings.append(Finding("ARTIFACT_ORDER_INVALID", f"/entries/{index}/produced_artifacts"))
        artifact_paths.extend(paths)
        if entry["publish_candidate"] and entry["materiality_delta"] != "PROMOTION_CANDIDATE":
            findings.append(Finding("PUBLISH_MATERIALITY_INCOHERENT", f"/entries/{index}/publish_candidate"))
    if len(artifact_paths) != len(set(artifact_paths)):
        findings.append(Finding("ARTIFACT_PATH_DUPLICATE", "/entries"))

    if summary["entry_count"] != len(entries):
        findings.append(Finding("ENTRY_COUNT_MISMATCH", "/summary/entry_count"))
    if summary["artifact_count"] != len(artifact_paths):
        findings.append(Finding("ARTIFACT_COUNT_MISMATCH", "/summary/artifact_count"))

    counts = Counter(entry["materiality_delta"] for entry in entries)
    expected_counts = {name: counts[name] for name in MATERIALITY}
    if summary["materiality_counts"] != expected_counts:
        findings.append(Finding("MATERIALITY_COUNTS_MISMATCH", "/summary/materiality_counts"))

    expected_inputs = sorted({entry["input_sha256"] for entry in entries})
    if not _canonical_strings(summary["input_sha256s"]):
        findings.append(Finding("SUMMARY_NOT_CANONICAL", "/summary/input_sha256s"))
    elif summary["input_sha256s"] != expected_inputs:
        findings.append(Finding("INPUT_DIGESTS_MISMATCH", "/summary/input_sha256s"))

    expected_publish = sorted(entry["receipt_ref"] for entry in entries if entry["publish_candidate"])
    if not _canonical_strings(summary["publish_candidate_receipt_refs"]):
        findings.append(Finding("SUMMARY_NOT_CANONICAL", "/summary/publish_candidate_receipt_refs"))
    elif summary["publish_candidate_receipt_refs"] != expected_publish:
        findings.append(Finding("PUBLISH_REFS_MISMATCH", "/summary/publish_candidate_receipt_refs"))

    expected_unsigned = sorted(entry["receipt_ref"] for entry in entries if entry["rekor_entry_id"] is None)
    if not _canonical_strings(summary["unsigned_receipt_refs"]):
        findings.append(Finding("SUMMARY_NOT_CANONICAL", "/summary/unsigned_receipt_refs"))
    elif summary["unsigned_receipt_refs"] != expected_unsigned:
        findings.append(Finding("UNSIGNED_REFS_MISMATCH", "/summary/unsigned_receipt_refs"))

    try:
        expected_hash, expected_id = canonical_identity(candidate)
    except CanonicalizationFailure:
        findings.append(Finding("IDENTITY_CANONICALIZATION_ERROR", "/"))
    else:
        if candidate.get("spec_hash") != expected_hash:
            findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
        if candidate.get("aggregation_id") != expected_id:
            findings.append(Finding("AGGREGATION_ID_MISMATCH", "/aggregation_id"))
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
