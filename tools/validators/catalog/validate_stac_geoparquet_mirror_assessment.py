#!/usr/bin/env python3
"""Validate fixture-only STAC GeoParquet mirror parity assessments."""
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

SCHEMA = ROOT / "schemas/contracts/v1/data/stac_geoparquet_mirror_assessment.schema.json"
FIXTURES = ROOT / "fixtures/contracts/v1/data/stac_geoparquet_mirror_assessment/cases.json"
PREFIX = "kfm:stac-geoparquet-mirror-assessment:"
MAX_BYTES = 4 * 1024 * 1024
MAX_FINDINGS = 100
TOP_LEVEL_KEYS = {"type", "stac_extensions", "id", "geometry", "bbox", "links", "assets", "collection"}


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class Result:
    outcome: str
    findings: tuple[Finding, ...]


class DuplicateKeyError(ValueError):
    pass


class NonFiniteNumberError(ValueError):
    pass


def _unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError
        result[key] = value
    return result


def _reject(_value: str) -> None:
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
            return None, (Finding("STAC_MIRROR_INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("STAC_MIRROR_INPUT_NOT_FILE", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("STAC_MIRROR_INPUT_TOO_LARGE", "/"),)
        value = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=_unique, parse_constant=_reject, parse_float=_finite)
    except DuplicateKeyError:
        return None, (Finding("STAC_MIRROR_JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("STAC_MIRROR_JSON_NONFINITE_NUMBER", "/"),)
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError):
        return None, (Finding("STAC_MIRROR_JSON_INVALID", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("STAC_MIRROR_ROOT_NOT_OBJECT", "/"),)
    return value, ()


def canonical_identity(value: Mapping[str, Any]) -> tuple[str, str]:
    subject = {key: item for key, item in value.items() if key not in {"assessment_id", "spec_hash"}}
    digest = compute_spec_hash(subject)
    return digest, PREFIX + digest.split(":", 1)[1][:24]


def _schema_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = list(islice(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(value), MAX_FINDINGS + 1))
    except Exception:
        return (Finding("STAC_MIRROR_SCHEMA_UNAVAILABLE", "/"),)
    errors.sort(key=lambda error: (_pointer(error.absolute_path), str(error.validator)))
    findings = {Finding("STAC_MIRROR_SCHEMA_INVALID", _pointer(error.absolute_path)) for error in errors[:MAX_FINDINGS]}
    if len(errors) > MAX_FINDINGS:
        findings.add(Finding("STAC_MIRROR_SCHEMA_FINDINGS_TRUNCATED", "/"))
    return tuple(sorted(findings))


def _item_key(item: Mapping[str, Any]) -> str:
    return f'{item["collection_id"]}/{item["item_id"]}'


def _projection(item: Mapping[str, Any]) -> dict[str, Any]:
    return {key: copy.deepcopy(value) for key, value in item.items()}


def recompute_report(value: Mapping[str, Any]) -> dict[str, Any]:
    if value["assessment_state"] == "ERROR":
        return {
            "result": "ERROR", "reason_code": "ASSESSMENT_ERROR", "matched_item_keys": [],
            "missing_mirror_item_keys": [], "unexpected_mirror_item_keys": [], "divergent_item_keys": [],
            "catalog_authority_granted": False, "release_authorized": False, "publication_authorized": False,
        }
    sources = {_item_key(item): item for item in value["source_items"]}
    mirrors = {_item_key(item): item for item in value["mirror"]["rows"]}
    source_keys, mirror_keys = set(sources), set(mirrors)
    missing = sorted(source_keys - mirror_keys)
    unexpected = sorted(mirror_keys - source_keys)
    divergent = sorted(key for key in source_keys & mirror_keys if _projection(sources[key]) != _projection(mirrors[key]))
    matched = sorted(key for key in source_keys & mirror_keys if key not in divergent)
    if missing or unexpected or divergent:
        result, reason = "PARITY_CONFLICT", "MIRROR_CONTENT_CONFLICT"
    elif value["assessment_scope"] == "PARTIAL_SAMPLE":
        result, reason = "PARTIAL_SAMPLE", "PARTIAL_SAMPLE_PARITY_ONLY"
    else:
        result, reason = "PARITY_CONFIRMED", "FULL_COLLECTION_PARITY_CONFIRMED"
    return {
        "result": result, "reason_code": reason, "matched_item_keys": matched,
        "missing_mirror_item_keys": missing, "unexpected_mirror_item_keys": unexpected,
        "divergent_item_keys": divergent, "catalog_authority_granted": False,
        "release_authorized": False, "publication_authorized": False,
    }


def _canonical_list_findings(items: Sequence[Mapping[str, Any]], root: str) -> set[Finding]:
    findings: set[Finding] = set()
    for index, item in enumerate(items):
        for field in ("stac_extensions", "property_names"):
            if item[field] != sorted(set(item[field])):
                findings.add(Finding("STAC_MIRROR_LIST_NONCANONICAL", f"{root}/{index}/{field}"))
        if TOP_LEVEL_KEYS.intersection(item["property_names"]):
            findings.add(Finding("STAC_MIRROR_PROPERTY_COLLISION", f"{root}/{index}/property_names"))
        instant = item["datetime"] is not None
        interval = item["start_datetime"] is not None and item["end_datetime"] is not None
        if instant == interval or (item["start_datetime"] is None) != (item["end_datetime"] is None):
            findings.add(Finding("STAC_MIRROR_TEMPORAL_SHAPE_INVALID", f"{root}/{index}"))
    return findings


def _semantic_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    findings: set[Finding] = set()
    sources = value["source_items"]
    rows = value["mirror"]["rows"]
    source_keys = [_item_key(item) for item in sources]
    row_keys = [_item_key(item) for item in rows]
    if len(source_keys) != len(set(source_keys)):
        findings.add(Finding("STAC_MIRROR_SOURCE_ITEM_DUPLICATE", "/source_items"))
    if len(row_keys) != len(set(row_keys)):
        findings.add(Finding("STAC_MIRROR_ROW_DUPLICATE", "/mirror/rows"))
    if source_keys != sorted(source_keys):
        findings.add(Finding("STAC_MIRROR_SOURCE_ORDER_NONCANONICAL", "/source_items"))
    if row_keys != sorted(row_keys):
        findings.add(Finding("STAC_MIRROR_ROW_ORDER_NONCANONICAL", "/mirror/rows"))
    findings.update(_canonical_list_findings(sources, "/source_items"))
    findings.update(_canonical_list_findings(rows, "/mirror/rows"))

    collection = value["source_collection"]
    declared = value["mirror"]["collections"]
    if len(declared) != 1 or declared[0] != collection:
        findings.add(Finding("STAC_MIRROR_COLLECTION_METADATA_MISMATCH", "/mirror/collections"))
    if any(item["collection_id"] != collection["collection_id"] for item in [*sources, *rows]):
        findings.add(Finding("STAC_MIRROR_COLLECTION_MEMBERSHIP_MISMATCH", "/mirror/rows"))

    try:
        expected_hash, expected_id = canonical_identity(value)
    except CanonicalizationFailure:
        findings.add(Finding("STAC_MIRROR_CANONICALIZATION_ERROR", "/"))
    else:
        if value["spec_hash"] != expected_hash:
            findings.add(Finding("STAC_MIRROR_SPEC_HASH_MISMATCH", "/spec_hash"))
        if value["assessment_id"] != expected_id:
            findings.add(Finding("STAC_MIRROR_ASSESSMENT_ID_MISMATCH", "/assessment_id"))
    if not findings and value["report"] != recompute_report(value):
        findings.add(Finding("STAC_MIRROR_REPORT_MISMATCH", "/report"))
    return tuple(sorted(findings))


def validate_payload(value: Mapping[str, Any]) -> Result:
    findings = _schema_findings(value)
    if findings:
        return Result("DENY", findings)
    findings = _semantic_findings(value)
    if findings:
        return Result("DENY", findings)
    result = value["report"]["result"]
    if result == "PARITY_CONFIRMED":
        return Result("PASS", ())
    if result == "PARTIAL_SAMPLE":
        return Result("ABSTAIN", (Finding("PARTIAL_SAMPLE_PARITY_ONLY", "/report/result"),))
    if result == "PARITY_CONFLICT":
        return Result("DENY", (Finding("MIRROR_CONTENT_CONFLICT", "/report/result"),))
    return Result("ERROR", (Finding("ASSESSMENT_ERROR", "/report/result"),))


def _replace(document: Any, pointer: str, replacement: Any) -> None:
    parts = [part.replace("~1", "/").replace("~0", "~") for part in pointer[1:].split("/")]
    target = document
    for part in parts[:-1]:
        target = target[int(part)] if isinstance(target, list) else target[part]
    key = parts[-1]
    if isinstance(target, list):
        target[int(key)] = copy.deepcopy(replacement)
    else:
        target[key] = copy.deepcopy(replacement)


def load_fixtures() -> dict[str, Any]:
    return json.loads(FIXTURES.read_text(encoding="utf-8"))


def materialize_case(manifest: Mapping[str, Any], case: Mapping[str, Any]) -> dict[str, Any]:
    document = copy.deepcopy(manifest["bases"][case["base"]])
    for mutation in case.get("mutations", []):
        _replace(document, mutation["path"], mutation.get("value"))
    document["report"] = recompute_report(document)
    for mutation in case.get("report_mutations", []):
        _replace(document, mutation["path"], mutation.get("value"))
    digest, identifier = canonical_identity(document)
    document["spec_hash"] = case.get("spec_hash_override", digest)
    document["assessment_id"] = case.get("assessment_id_override", identifier)
    return document


def run_fixtures() -> int:
    manifest = load_fixtures()
    failures: list[dict[str, Any]] = []
    for case in manifest["cases"]:
        result = validate_payload(materialize_case(manifest, case))
        actual = [{"code": item.code, "path": item.path} for item in result.findings]
        if result.outcome != case["expected_outcome"] or actual != case["expected_findings"]:
            failures.append({"case_id": case["case_id"], "expected_outcome": case["expected_outcome"], "actual_outcome": result.outcome, "expected_findings": case["expected_findings"], "actual_findings": actual})
    print(json.dumps({"cases": len(manifest["cases"]), "failures": failures, "suite_match": not failures}, sort_keys=True, separators=(",", ":")))
    return 0 if not failures else 1


def serialize(path: Path | None, result: Result) -> str:
    return json.dumps({
        "authority": "NONE", "execution_mode": "FIXTURE_ONLY", "file": path.as_posix() if path else None,
        "findings": [{"code": item.code, "path": item.path} for item in result.findings],
        "non_effects": ["no_network", "no_parquet_access", "no_source_resolution", "no_catalog_mutation", "no_evidence_resolution", "no_policy_decision", "no_review_approval", "no_release", "no_publication"],
        "outcome": result.outcome,
    }, sort_keys=True, separators=(",", ":"))


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", type=Path)
    parser.add_argument("--fixtures", action="store_true")
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.input is not None:
            parser.error("--fixtures cannot be combined with input")
        return run_fixtures()
    if args.input is None:
        parser.error("input is required unless --fixtures is used")
    value, findings = _read(args.input)
    result = Result("ERROR", findings) if value is None else validate_payload(value)
    print(serialize(args.input, result))
    return {"PASS": 0, "DENY": 1, "ERROR": 2, "ABSTAIN": 3}[result.outcome]


if __name__ == "__main__":
    raise SystemExit(main())
