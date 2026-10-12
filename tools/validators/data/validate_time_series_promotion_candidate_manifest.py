#!/usr/bin/env python3
"""Validate fixture-only TimeSeriesPromotionCandidateManifest records.

A PASS result proves bounded shape, semantic consistency, and deterministic
identity only. It does not fetch or admit station observations, resolve evidence,
evaluate policy, authenticate review, promote, release, deploy, publish, or
authorize public use.
"""

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
HASHING_SRC = ROOT / "packages/hashing/src"
if str(HASHING_SRC) not in sys.path:
    sys.path.insert(0, str(HASHING_SRC))
from hashing import CanonicalizationFailure, compute_spec_hash

SCHEMA = ROOT / "schemas/contracts/v1/data/time_series_promotion_candidate_manifest.schema.json"
CASES = ROOT / "fixtures/contracts/v1/data/time_series_promotion_candidate_manifest/cases.json"
IDENTITY_PREFIX = "kfm:time-series-promotion-candidate:"
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
    subject.pop("manifest_id", None)
    subject.pop("spec_hash", None)
    return subject


def canonical_identity(value: Mapping[str, Any]) -> tuple[str, str]:
    spec_hash = compute_spec_hash(identity_subject(value))
    manifest_id = IDENTITY_PREFIX + spec_hash.split(":", 1)[1][:24]
    return spec_hash, manifest_id


def _merge(target: dict[str, Any], patch: Mapping[str, Any]) -> None:
    for key, value in patch.items():
        if isinstance(value, dict) and isinstance(target.get(key), dict):
            _merge(target[key], value)
        else:
            target[key] = copy.deepcopy(value)


def materialize_case(corpus: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    candidate = copy.deepcopy(corpus["base"])
    base_hash, base_id = canonical_identity(candidate)
    candidate["spec_hash"] = base_hash
    candidate["manifest_id"] = base_id
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


def _parse_time(value: object) -> datetime | None:
    if not isinstance(value, str):
        return None
    normalized = value[:-1] + "+00:00" if value.endswith(("Z", "z")) else value
    try:
        parsed = datetime.fromisoformat(normalized)
    except ValueError:
        return None
    return parsed if parsed.tzinfo is not None and parsed.utcoffset() is not None else None


def _canonical_strings(value: object) -> bool:
    return isinstance(value, list) and value == sorted(set(value))


def _semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    batch = candidate.get("batch")
    if not isinstance(batch, dict):
        return [Finding("BATCH_INVALID", "/batch")]

    if not _canonical_strings(batch.get("station_ids")):
        findings.append(Finding("STATION_IDS_NOT_CANONICAL", "/batch/station_ids"))
    if not _canonical_strings(batch.get("variable_ids")):
        findings.append(Finding("VARIABLE_IDS_NOT_CANONICAL", "/batch/variable_ids"))

    temporal = batch.get("temporal_extent")
    if isinstance(temporal, dict):
        start = _parse_time(temporal.get("start"))
        end = _parse_time(temporal.get("end"))
        if start is None or end is None or start > end:
            findings.append(Finding("TEMPORAL_EXTENT_INVALID", "/batch/temporal_extent"))

    spatial = batch.get("spatial_scope")
    if isinstance(spatial, dict):
        bbox = spatial.get("bbox")
        if (
            not isinstance(bbox, list)
            or len(bbox) != 4
            or not all(isinstance(item, (int, float)) and not isinstance(item, bool) for item in bbox)
            or bbox[0] >= bbox[2]
            or bbox[1] >= bbox[3]
        ):
            findings.append(Finding("FOOTPRINT_BBOX_INVALID", "/batch/spatial_scope/bbox"))

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
    schema_findings = _schema_findings(candidate)
    if schema_findings:
        return Result("DENY", tuple(sorted(set(schema_findings))))
    findings = _semantic_findings(candidate)
    return Result("PASS" if not findings else "DENY", tuple(sorted(set(findings))))


def validate_record(path: Path) -> Result:
    candidate, findings = _read(path)
    if candidate is None:
        return Result("ERROR", tuple(sorted(set(findings))))
    return validate_candidate(candidate)


def _serialize(label: str, result: Result) -> str:
    return json.dumps(
        {
            "fixture": label,
            "findings": [item.code for item in result.findings],
            "outcome": result.outcome,
            "scope": "fixture-only-time-series-candidate-manifest",
        },
        sort_keys=True,
        separators=(",", ":"),
    )


def run_fixture_profile() -> int:
    corpus, findings = _read(CASES)
    if corpus is None:
        print(_serialize("cases.json", Result("ERROR", findings)))
        return 1
    passed = True
    cases = corpus.get("cases")
    if not isinstance(cases, list):
        print(_serialize("cases.json", Result("ERROR", (Finding("CASE_CORPUS_INVALID", "/cases"),))))
        return 1
    for case in sorted(cases, key=lambda item: item.get("id", "") if isinstance(item, dict) else ""):
        if not isinstance(case, dict):
            passed = False
            continue
        candidate = materialize_case(corpus, case)
        result = validate_candidate(candidate)
        expected = case.get("expected", {})
        actual_codes = sorted({item.code for item in result.findings})
        if result.outcome != expected.get("outcome") or actual_codes != expected.get("findings"):
            passed = False
        print(_serialize(str(case.get("id", "invalid-case")), result))
    return 0 if passed else 1


def run(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("files", nargs="*")
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.files:
            parser.error("--fixtures does not accept file arguments")
        return run_fixture_profile()
    if not args.files:
        parser.print_usage(sys.stderr)
        return 2
    passed = True
    for raw in sorted(args.files):
        result = validate_record(Path(raw))
        print(_serialize(Path(raw).name, result))
        passed = result.ok and passed
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(run())

