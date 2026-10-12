#!/usr/bin/env python3
"""Validate fixture-only STAC search behavior profile candidates."""

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

SCHEMA = ROOT / "schemas/contracts/v1/data/stac_search_behavior_fixture_profile.schema.json"
CASES = ROOT / "fixtures/contracts/v1/data/stac_search_behavior_fixture_profile/cases.json"
IDENTITY_PREFIX = "kfm:stac-search-behavior:"
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
    subject.pop("profile_id", None)
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
    spec_hash, profile_id = canonical_identity(candidate)
    candidate["spec_hash"] = spec_hash
    candidate["profile_id"] = profile_id
    _merge(candidate, case.get("patch", {}))
    if case.get("recompute_identity", True):
        spec_hash, profile_id = canonical_identity(candidate)
        candidate["spec_hash"] = spec_hash
        candidate["profile_id"] = profile_id
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


def _strictly_ordered(left: Sequence[str], right: Sequence[str], sortby: Sequence[Mapping[str, Any]]) -> bool:
    for index, rule in enumerate(sortby):
        if left[index] == right[index]:
            continue
        return left[index] < right[index] if rule["direction"] == "ASC" else left[index] > right[index]
    return False


def _semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    request = candidate["request"]
    pages = candidate["pages"]
    fields = request["fields"]
    sortby = request["sortby"]

    if not _canonical_strings(fields["include"]) or not _canonical_strings(fields["exclude"]) or any(not _canonical_strings(page["returned_field_paths"]) for page in pages):
        findings.append(Finding("FIELDS_NOT_CANONICAL", "/"))
    if set(fields["include"]) & set(fields["exclude"]):
        findings.append(Finding("FIELD_INCLUDE_EXCLUDE_OVERLAP", "/request/fields"))

    bbox = request["bbox"]
    if bbox[0] >= bbox[2] or bbox[1] >= bbox[3]:
        findings.append(Finding("BBOX_ORDER_INVALID", "/request/bbox"))
    try:
        started_at, ended_at = request["datetime"].split("/", 1)
        if _datetime(started_at) >= _datetime(ended_at):
            findings.append(Finding("DATETIME_INTERVAL_INVALID", "/request/datetime"))
    except (TypeError, ValueError):
        findings.append(Finding("DATETIME_INTERVAL_INVALID", "/request/datetime"))

    sort_fields = [item["field"] for item in sortby]
    if len(sort_fields) != len(set(sort_fields)):
        findings.append(Finding("SORT_FIELD_DUPLICATE", "/request/sortby"))
    if sort_fields[-1] != "id":
        findings.append(Finding("ID_TIEBREAKER_REQUIRED", "/request/sortby"))

    if pages[0]["request_token"] is not None or pages[-1]["response_next_token"] is not None:
        findings.append(Finding("PAGE_TOKEN_CHAIN_INVALID", "/pages"))
    for index in range(1, len(pages)):
        if pages[index]["request_token"] != pages[index - 1]["response_next_token"]:
            findings.append(Finding("PAGE_TOKEN_CHAIN_INVALID", f"/pages/{index}/request_token"))

    all_items: list[Mapping[str, Any]] = []
    for page_index, page in enumerate(pages):
        returned = set(page["returned_field_paths"])
        if not set(fields["include"]).issubset(returned):
            findings.append(Finding("REQUIRED_FIELD_MISSING", f"/pages/{page_index}/returned_field_paths"))
        if set(fields["exclude"]) & returned:
            findings.append(Finding("EXCLUDED_FIELD_RETURNED", f"/pages/{page_index}/returned_field_paths"))
        for item_index, item in enumerate(page["items"]):
            if len(item["sort_values"]) != len(sortby):
                findings.append(Finding("SORT_VALUE_ARITY_MISMATCH", f"/pages/{page_index}/items/{item_index}/sort_values"))
            all_items.append(item)

    ids = [item["id"] for item in all_items]
    if len(ids) != len(set(ids)):
        findings.append(Finding("ITEM_ID_DUPLICATE", "/pages"))
    if all(len(item["sort_values"]) == len(sortby) for item in all_items):
        for left, right in zip(all_items, all_items[1:]):
            if not _strictly_ordered(left["sort_values"], right["sort_values"], sortby):
                findings.append(Finding("STABLE_SORT_ORDER_INVALID", "/pages"))
                break

    try:
        expected_hash, expected_id = canonical_identity(candidate)
    except CanonicalizationFailure:
        findings.append(Finding("IDENTITY_CANONICALIZATION_ERROR", "/"))
    else:
        if candidate.get("spec_hash") != expected_hash:
            findings.append(Finding("SPEC_HASH_MISMATCH", "/spec_hash"))
        if candidate.get("profile_id") != expected_id:
            findings.append(Finding("PROFILE_ID_MISMATCH", "/profile_id"))
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
