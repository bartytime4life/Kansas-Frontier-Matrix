#!/usr/bin/env python3
"""Validate fixture-only PM2.5 sensor co-location manifest candidates."""

from __future__ import annotations

import argparse
import copy
import json
import math
import sys
from dataclasses import dataclass
from datetime import datetime
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[4]
HASHING_SRC = ROOT / "packages/hashing/src"
if str(HASHING_SRC) not in sys.path:
    sys.path.insert(0, str(HASHING_SRC))
from hashing import CanonicalizationFailure, compute_spec_hash

SCHEMA = ROOT / "schemas/contracts/v1/domains/atmosphere/pm25_sensor_colocation_manifest.schema.json"
CASES = ROOT / "fixtures/contracts/v1/domains/atmosphere/pm25_sensor_colocation_manifest/cases.json"
IDENTITY_PREFIX = "kfm:pm25-colocation-manifest:"
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
        value = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_unique, parse_constant=_reject_constant, parse_float=_finite_float)
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
    subject.pop("manifest_id", None)
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
    spec_hash, manifest_id = canonical_identity(candidate)
    candidate["spec_hash"] = spec_hash
    candidate["manifest_id"] = manifest_id
    _merge(candidate, case.get("patch", {}))
    if case.get("recompute_identity", True):
        spec_hash, manifest_id = canonical_identity(candidate)
        candidate["spec_hash"] = spec_hash
        candidate["manifest_id"] = manifest_id
    return candidate


def _schema_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = list(islice(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(candidate), MAX_SCHEMA_FINDINGS + 1))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding("SCHEMA_UNAVAILABLE", "/")]
    findings = [Finding("SCHEMA_INVALID", _pointer(error.absolute_path)) for error in sorted(errors[:MAX_SCHEMA_FINDINGS], key=lambda item: (_pointer(item.absolute_path), str(item.validator)))]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("SCHEMA_FINDINGS_TRUNCATED", "/"))
    return findings


def _canonical_strings(value: object) -> bool:
    return isinstance(value, list) and value == sorted(set(value))


def _datetime(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def _semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    sensor_ids = candidate["sensor_ids"]
    completeness = candidate["data_completeness"]
    seasonal = candidate["seasonal_coverage"]
    split = candidate["validation_split"]

    canonical_arrays = [sensor_ids, candidate["generalization_assumptions"], candidate["evidence_refs"], candidate["reference_site"]["evidence_refs"], seasonal["seasons"], seasonal["evidence_refs"]]
    canonical_arrays.extend(item["evidence_refs"] for item in completeness["sensors"])
    canonical_arrays.extend(item["sensor_ids"] for item in split["partitions"])
    canonical_arrays.extend(item["evidence_refs"] for item in split["partitions"])
    if any(not _canonical_strings(value) for value in canonical_arrays):
        findings.append(Finding("ARRAYS_NOT_CANONICAL", "/"))

    completeness_ids = [item["sensor_id"] for item in completeness["sensors"]]
    if completeness_ids != sensor_ids:
        findings.append(Finding("COMPLETENESS_SENSOR_SET_MISMATCH", "/data_completeness/sensors"))
    for index, item in enumerate(completeness["sensors"]):
        expected = item["expected_count"]
        observed = item["observed_count"]
        if observed > expected or not math.isclose(item["completeness_fraction"], observed / expected, rel_tol=0.0, abs_tol=1e-12):
            findings.append(Finding("COMPLETENESS_FRACTION_MISMATCH", f"/data_completeness/sensors/{index}"))

    nested_refs = set(candidate["reference_site"]["evidence_refs"]) | set(seasonal["evidence_refs"])
    for item in completeness["sensors"]:
        nested_refs.update(item["evidence_refs"])
    for item in split["partitions"]:
        nested_refs.update(item["evidence_refs"])
    if set(candidate["evidence_refs"]) != nested_refs:
        findings.append(Finding("EVIDENCE_REF_CLOSURE_MISMATCH", "/evidence_refs"))

    try:
        window_start = _datetime(candidate["window"]["started_at"])
        window_end = _datetime(candidate["window"]["ended_at"])
        if window_start >= window_end:
            findings.append(Finding("WINDOW_ORDER_INVALID", "/window"))
    except (TypeError, ValueError):
        findings.append(Finding("WINDOW_INVALID", "/window"))
        window_start = window_end = None

    if not any(item["name"] == "VALIDATION" for item in split["partitions"]):
        findings.append(Finding("VALIDATION_PARTITION_REQUIRED", "/validation_split/partitions"))
    parsed: list[tuple[int, set[str], datetime, datetime]] = []
    for index, item in enumerate(split["partitions"]):
        if not set(item["sensor_ids"]).issubset(set(sensor_ids)):
            findings.append(Finding("PARTITION_SENSOR_UNKNOWN", f"/validation_split/partitions/{index}/sensor_ids"))
        try:
            start, end = _datetime(item["started_at"]), _datetime(item["ended_at"])
            if start >= end:
                findings.append(Finding("PARTITION_TIME_ORDER_INVALID", f"/validation_split/partitions/{index}"))
            elif window_start is not None and (start < window_start or end > window_end):
                findings.append(Finding("PARTITION_OUTSIDE_WINDOW", f"/validation_split/partitions/{index}"))
            parsed.append((index, set(item["sensor_ids"]), start, end))
        except (TypeError, ValueError):
            findings.append(Finding("PARTITION_TIME_INVALID", f"/validation_split/partitions/{index}"))
    for left_index, left_sensors, left_start, left_end in parsed:
        for right_index, right_sensors, right_start, right_end in parsed:
            if right_index > left_index and left_sensors & right_sensors and max(left_start, right_start) < min(left_end, right_end):
                findings.append(Finding("PARTITION_OVERLAP", f"/validation_split/partitions/{right_index}"))

    try:
        expected_hash, expected_id = canonical_identity(candidate)
    except CanonicalizationFailure:
        findings.append(Finding("IDENTITY_CANONICALIZATION_ERROR", "/"))
    else:
        if candidate.get("spec_hash") != expected_hash:
            findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
        if candidate.get("manifest_id") != expected_id:
            findings.append(Finding("MANIFEST_ID_MISMATCH", "/manifest_id"))
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
        exit_code |= 0 if matched else 1
    return exit_code


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("record", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        return _fixture_results()
    if args.record is None:
        parser.error("record is required unless --fixtures is used")
    result = validate_record(args.record)
    print(json.dumps({"outcome": result.outcome, "findings": [item.code for item in result.findings]}, sort_keys=True))
    return 0 if result.ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
