#!/usr/bin/env python3
"""Validate fixture-only time-bucket playback manifests without playback."""
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

ROOT = Path(__file__).resolve().parents[3]
HASH_SRC = ROOT / "packages/hashing/src"
if str(HASH_SRC) not in sys.path:
    sys.path.insert(0, str(HASH_SRC))
from hashing import CanonicalizationFailure, compute_spec_hash

SCHEMA = ROOT / "schemas/contracts/v1/ui/time_bucket_playback_manifest.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/ui/time_bucket_playback_manifest/cases.json"
MAX_BYTES = 1024 * 1024
MAX_SCHEMA_FINDINGS = 50
MANIFEST_PREFIX = "kfm:time-bucket-playback:"
BUCKET_PREFIX = "kfm:time-bucket:"
TIME_FIELDS = {
    "VALID_TIME": "valid_time",
    "OBSERVED_TIME": "observed_time",
    "SOURCE_TIME": "source_time",
    "RETRIEVAL_TIME": "retrieval_time",
    "RELEASE_TIME": "release_time",
    "CORRECTION_TIME": "correction_time",
}


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
    state: str | None
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return self.outcome == "PASS"


def _unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value


def _reject_constant(_value: str) -> None:
    raise NonFiniteNumberError


def _finite(value: str) -> float:
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
            return None, (Finding("TIME_BUCKET_INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("TIME_BUCKET_INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("TIME_BUCKET_INPUT_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject_constant,
            parse_float=_finite,
        )
    except DuplicateKeyError:
        return None, (Finding("TIME_BUCKET_JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("TIME_BUCKET_JSON_NONFINITE_NUMBER", "/"),)
    except (UnicodeError, json.JSONDecodeError):
        return None, (Finding("TIME_BUCKET_JSON_INVALID", "/"),)
    except OSError:
        return None, (Finding("TIME_BUCKET_INPUT_READ_ERROR", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("TIME_BUCKET_ROOT_NOT_OBJECT", "/"),)
    return value, ()


def _dt(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00"))


def bucket_identity(bucket: Mapping[str, Any]) -> tuple[str, str]:
    subject = {
        key: item
        for key, item in bucket.items()
        if key not in {"bucket_id", "bucket_hash"}
    }
    digest = compute_spec_hash(subject)
    return digest, BUCKET_PREFIX + digest.split(":", 1)[1][:24]


def manifest_identity(value: Mapping[str, Any]) -> tuple[str, str]:
    subject = {
        key: item
        for key, item in value.items()
        if key not in {"manifest_id", "spec_hash"}
    }
    digest = compute_spec_hash(subject)
    return digest, MANIFEST_PREFIX + digest.split(":", 1)[1][:24]


def _schema_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        errors = list(islice(validator.iter_errors(value), MAX_SCHEMA_FINDINGS + 1))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return (Finding("TIME_BUCKET_SCHEMA_UNAVAILABLE", "/"),)
    errors.sort(key=lambda error: (_pointer(error.absolute_path), str(error.validator)))
    findings = [
        Finding("TIME_BUCKET_SCHEMA_INVALID", _pointer(error.absolute_path))
        for error in errors[:MAX_SCHEMA_FINDINGS]
    ]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding("TIME_BUCKET_SCHEMA_FINDINGS_TRUNCATED", "/"))
    return tuple(sorted(set(findings)))


def expected_selection_mode(buckets: Sequence[Mapping[str, Any]]) -> str:
    hints = {bucket["transport_hint"] for bucket in buckets}
    if hints == {"SAME_SOURCE_FILTER"}:
        return "FILTER"
    if hints == {"SOURCE_SWAP"}:
        return "SWAP"
    return "HYBRID"


def _semantic_findings(value: Mapping[str, Any]) -> set[Finding]:
    findings: set[Finding] = set()
    semantics = value["time_semantics"]
    buckets = value["buckets"]
    window_start = _dt(semantics["window_start"])
    window_end = _dt(semantics["window_end"])

    expected_field = TIME_FIELDS[semantics["filter_time_kind"]]
    if semantics["filter_field"] != expected_field:
        findings.add(Finding("TIME_BUCKET_FILTER_TIME_KIND_MISMATCH", "/time_semantics/filter_field"))
    if window_start >= window_end:
        findings.add(Finding("TIME_BUCKET_WINDOW_INVALID", "/time_semantics"))
    if _dt(semantics["correction_cutoff"]) < window_end:
        findings.add(Finding("TIME_BUCKET_CORRECTION_CUTOFF_INVALID", "/time_semantics/correction_cutoff"))

    if _dt(buckets[0]["interval"]["start_inclusive"]) != window_start:
        findings.add(Finding("TIME_BUCKET_WINDOW_START_MISMATCH", "/time_semantics/window_start"))
    if _dt(buckets[-1]["interval"]["end_exclusive"]) != window_end:
        findings.add(Finding("TIME_BUCKET_WINDOW_END_MISMATCH", "/time_semantics/window_end"))

    bucket_ids: list[str] = []
    artifact_refs: list[str] = []
    prior_end: datetime | None = None
    prior_index: int | None = None
    for index, bucket in enumerate(buckets):
        bucket_ids.append(bucket["bucket_id"])
        artifact_refs.append(bucket["artifact_ref"])
        if bucket["ordinal"] != index:
            findings.add(Finding("TIME_BUCKET_ORDINAL_MISMATCH", f"/buckets/{index}/ordinal"))
        if bucket["time_field"] != semantics["filter_field"]:
            findings.add(Finding("TIME_BUCKET_FIELD_MIXED", f"/buckets/{index}/time_field"))
        start = _dt(bucket["interval"]["start_inclusive"])
        end = _dt(bucket["interval"]["end_exclusive"])
        if start >= end:
            findings.add(Finding("TIME_BUCKET_INTERVAL_INVALID", f"/buckets/{index}/interval"))
        if prior_end is not None and prior_index is not None:
            if start < prior_end:
                findings.add(Finding("TIME_BUCKET_INTERVAL_OVERLAP", f"/buckets/{index}/interval/start_inclusive"))
            elif start > prior_end:
                if not buckets[prior_index]["gap_after"]:
                    findings.add(Finding("TIME_BUCKET_GAP_UNDECLARED", f"/buckets/{prior_index}/gap_after"))
            elif buckets[prior_index]["gap_after"]:
                findings.add(Finding("TIME_BUCKET_GAP_FLAG_INVALID", f"/buckets/{prior_index}/gap_after"))
        prior_end = end
        prior_index = index

        evidence_refs = bucket["evidence_refs"]
        if evidence_refs != sorted(evidence_refs):
            findings.add(Finding("TIME_BUCKET_EVIDENCE_ORDER_INVALID", f"/buckets/{index}/evidence_refs"))
        try:
            expected_hash, expected_id = bucket_identity(bucket)
        except CanonicalizationFailure:
            findings.add(Finding("TIME_BUCKET_BUCKET_CANONICALIZATION_ERROR", f"/buckets/{index}"))
        else:
            if bucket["bucket_hash"] != expected_hash:
                findings.add(Finding("TIME_BUCKET_BUCKET_HASH_MISMATCH", f"/buckets/{index}/bucket_hash"))
            if bucket["bucket_id"] != expected_id:
                findings.add(Finding("TIME_BUCKET_BUCKET_ID_MISMATCH", f"/buckets/{index}/bucket_id"))

    if buckets[-1]["gap_after"]:
        findings.add(Finding("TIME_BUCKET_TRAILING_GAP_INVALID", f"/buckets/{len(buckets) - 1}/gap_after"))
    if len(bucket_ids) != len(set(bucket_ids)):
        findings.add(Finding("TIME_BUCKET_BUCKET_ID_DUPLICATE", "/buckets"))
    if len(artifact_refs) != len(set(artifact_refs)):
        findings.add(Finding("TIME_BUCKET_ARTIFACT_REF_DUPLICATE", "/buckets"))
    expected_mode = expected_selection_mode(buckets)
    if value["transition"]["selection_mode"] != expected_mode:
        findings.add(Finding("TIME_BUCKET_SELECTION_MODE_MISMATCH", "/transition/selection_mode"))
    return findings


def validate_payload(value: Mapping[str, Any]) -> Result:
    schema_findings = _schema_findings(value)
    if schema_findings:
        return Result("DENY", None, schema_findings)
    try:
        findings = _semantic_findings(value)
        expected_hash, expected_id = manifest_identity(value)
    except (CanonicalizationFailure, ValueError, TypeError, OverflowError):
        return Result(
            "DENY",
            None,
            (Finding("TIME_BUCKET_CANONICALIZATION_OR_TIME_ERROR", "/"),),
        )
    if value["spec_hash"] != expected_hash:
        findings.add(Finding("TIME_BUCKET_SPEC_HASH_MISMATCH", "/spec_hash"))
    if value["manifest_id"] != expected_id:
        findings.add(Finding("TIME_BUCKET_MANIFEST_ID_MISMATCH", "/manifest_id"))
    if findings:
        return Result("DENY", None, tuple(sorted(findings)))
    return Result("PASS", "REVIEW_REQUIRED", ())


def validate_file(path: Path) -> Result:
    value, findings = _read(path)
    if value is None:
        return Result("ERROR", None, findings)
    return validate_payload(value)


def _set_pointer(document: dict[str, Any], pointer: str, replacement: Any) -> None:
    parts = [
        part.replace("~1", "/").replace("~0", "~")
        for part in pointer.removeprefix("/").split("/")
    ]
    cursor: Any = document
    for part in parts[:-1]:
        cursor = cursor[int(part)] if isinstance(cursor, list) else cursor[part]
    last = parts[-1]
    if isinstance(cursor, list):
        cursor[int(last)] = replacement
    else:
        cursor[last] = replacement


def materialize_case(manifest: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    document = copy.deepcopy(manifest["base"])
    for mutation in case.get("mutations", []):
        _set_pointer(document, mutation["path"], mutation["value"])
    for bucket in document["buckets"]:
        bucket["bucket_hash"], bucket["bucket_id"] = bucket_identity(bucket)
    document["spec_hash"], document["manifest_id"] = manifest_identity(document)
    for override, pointer in (
        ("bucket_0_hash_override", "/buckets/0/bucket_hash"),
        ("bucket_0_id_override", "/buckets/0/bucket_id"),
        ("spec_hash_override", "/spec_hash"),
        ("manifest_id_override", "/manifest_id"),
    ):
        if override in case:
            _set_pointer(document, pointer, case[override])
    return document


def load_fixtures() -> dict[str, Any]:
    value = json.loads(FIXTURES.read_text(encoding="utf-8"), object_pairs_hook=_unique)
    if not isinstance(value, dict):
        raise ValueError("fixture root must be an object")
    return value


def _run_fixtures() -> int:
    manifest = load_fixtures()
    failures: list[dict[str, Any]] = []
    for case in manifest["cases"]:
        result = validate_payload(materialize_case(manifest, case))
        actual = [{"code": item.code, "path": item.path} for item in result.findings]
        if (
            result.outcome != case["expected_outcome"]
            or result.state != case["expected_state"]
            or actual != case["expected_findings"]
        ):
            failures.append(
                {
                    "case_id": case["case_id"],
                    "expected_outcome": case["expected_outcome"],
                    "actual_outcome": result.outcome,
                    "expected_state": case["expected_state"],
                    "actual_state": result.state,
                    "expected_findings": case["expected_findings"],
                    "actual_findings": actual,
                }
            )
    print(json.dumps({"cases": len(manifest["cases"]), "failures": failures, "suite_match": not failures}, sort_keys=True, separators=(",", ":")))
    return 0 if not failures else 1


def _serialize(path: Path, result: Result) -> str:
    return json.dumps(
        {
            "authority": {
                "executes_playback": False,
                "executes_worker": False,
                "fetches_artifacts": False,
                "verifies_integrity": False,
                "resolves_evidence": False,
                "evaluates_policy": False,
                "authorizes_release": False,
                "deploys": False,
                "publishes": False,
            },
            "execution_mode": "FIXTURE_ONLY",
            "file": path.as_posix(),
            "findings": [{"code": item.code, "path": item.path} for item in result.findings],
            "outcome": result.outcome,
            "state": result.state,
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        return _run_fixtures()
    if args.input is None:
        raise SystemExit("input is required unless --fixtures is used")
    result = validate_file(args.input)
    print(_serialize(args.input, result))
    return {"PASS": 0, "DENY": 1, "ERROR": 2}[result.outcome]


if __name__ == "__main__":
    raise SystemExit(main())
