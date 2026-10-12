#!/usr/bin/env python3
"""Validate fixture-only local STAC link-closure assessments."""
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

from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[3]
HASH_SRC = ROOT / "packages/hashing/src"
if str(HASH_SRC) not in sys.path:
    sys.path.insert(0, str(HASH_SRC))
from hashing import CanonicalizationFailure, compute_spec_hash

SCHEMA = ROOT / "schemas/contracts/v1/data/stac_link_closure_assessment.schema.json"
MAX_BYTES = 512 * 1024
MAX_SCHEMA_FINDINGS = 50
IDENTITY_PREFIX = "kfm:stac-link-closure:"
RECIPROCAL = {"child": "parent", "parent": "child", "item": "collection", "collection": "item"}


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
        return self.outcome == "PASS"


def _unique(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    out: dict[str, Any] = {}
    for key, value in pairs:
        if key in out:
            raise DuplicateKeyError
        out[key] = value
    return out


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
            return None, (Finding("STAC_LINK_INPUT_SYMLINK_DENIED", "/"),)
        if not path.is_file():
            return None, (Finding("STAC_LINK_FILE_NOT_FOUND", "/"),)
        if path.stat().st_size > MAX_BYTES:
            return None, (Finding("STAC_LINK_FILE_TOO_LARGE", "/"),)
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_unique,
            parse_constant=_reject_constant,
            parse_float=_finite,
        )
    except DuplicateKeyError:
        return None, (Finding("STAC_LINK_JSON_DUPLICATE_KEY", "/"),)
    except NonFiniteNumberError:
        return None, (Finding("STAC_LINK_JSON_NONFINITE_NUMBER", "/"),)
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError, ValueError):
        return None, (Finding("STAC_LINK_JSON_INVALID", "/"),)
    if not isinstance(value, dict):
        return None, (Finding("STAC_LINK_ROOT_NOT_OBJECT", "/"),)
    return value, ()


def _schema_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    try:
        schema = json.loads(SCHEMA.read_text(encoding="utf-8"))
        Draft202012Validator.check_schema(schema)
        errors = list(islice(Draft202012Validator(schema).iter_errors(value), MAX_SCHEMA_FINDINGS))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return (Finding("STAC_LINK_SCHEMA_UNAVAILABLE", "/"),)
    return tuple(sorted(Finding("STAC_LINK_SCHEMA_INVALID", _pointer(error.absolute_path)) for error in errors))


def _identity_subject(value: Mapping[str, Any]) -> dict[str, Any]:
    subject = copy.deepcopy(dict(value))
    subject.pop("assessment_id", None)
    subject.pop("spec_hash", None)
    return subject


def canonical_identity(value: Mapping[str, Any]) -> tuple[str, str]:
    spec_hash = compute_spec_hash(_identity_subject(value))
    return spec_hash, IDENTITY_PREFIX + spec_hash.removeprefix("sha256:")[:24]


def _edge_key(source: str, link: Mapping[str, Any]) -> str:
    return f"{source}|{link['rel']}|{link['target_record_id']}"


def _link_key(link: Mapping[str, Any]) -> tuple[str, str, str]:
    return str(link["rel"]), str(link["target_record_id"]), str(link["target_record_type"])


def expected_assessment(value: Mapping[str, Any]) -> dict[str, Any]:
    if value["assessment_state"] == "ERROR":
        return {
            "outcome": "ERROR",
            "reason_code": "UPSTREAM_ERROR",
            "reachable_record_ids": [],
            "missing_target_record_ids": [],
            "nonreciprocal_edges": [],
            "type_mismatch_edges": [],
            "orphan_record_ids": [],
        }

    records = value["records"]
    by_id = {record["record_id"]: record for record in records}
    missing: set[str] = set()
    nonreciprocal: set[str] = set()
    mismatched: set[str] = set()

    for record in records:
        source_id = record["record_id"]
        source_type = record["record_type"]
        for link in record["links"]:
            target_id = link["target_record_id"]
            target = by_id.get(target_id)
            edge = _edge_key(source_id, link)
            if target is None:
                missing.add(target_id)
                continue
            if target["record_type"] != link["target_record_type"]:
                mismatched.add(edge)
            rel = link["rel"]
            type_invalid = (
                (rel == "root" and (target_id != value["root_record_id"] or target["record_type"] != "CATALOG"))
                or (rel == "item" and (source_type != "COLLECTION" or target["record_type"] != "ITEM"))
                or (rel == "collection" and (source_type != "ITEM" or target["record_type"] != "COLLECTION"))
                or (rel in {"child", "parent"} and target["record_type"] not in {"CATALOG", "COLLECTION"})
            )
            if type_invalid:
                mismatched.add(edge)
            reciprocal = RECIPROCAL.get(rel)
            if reciprocal and not any(
                candidate["rel"] == reciprocal
                and candidate["target_record_id"] == source_id
                and candidate["target_record_type"] == source_type
                for candidate in target["links"]
            ):
                nonreciprocal.add(edge)

    reachable: set[str] = set()
    pending = [value["root_record_id"]] if value["root_record_id"] in by_id else []
    while pending:
        record_id = pending.pop()
        if record_id in reachable:
            continue
        reachable.add(record_id)
        for link in by_id[record_id]["links"]:
            if link["rel"] in {"child", "item"} and link["target_record_id"] in by_id:
                pending.append(link["target_record_id"])
    orphan = set(by_id) - reachable

    common = {
        "reachable_record_ids": sorted(reachable),
        "missing_target_record_ids": sorted(missing),
        "nonreciprocal_edges": sorted(nonreciprocal),
        "type_mismatch_edges": sorted(mismatched),
        "orphan_record_ids": sorted(orphan),
    }
    if missing or nonreciprocal or mismatched or orphan:
        return {"outcome": "LINK_GRAPH_OPEN", "reason_code": "LOCAL_LINK_CONFLICT", **common}
    if value["graph_scope"] == "PARTIAL_DECLARED_GRAPH":
        return {"outcome": "PARTIAL_GRAPH", "reason_code": "PARTIAL_GRAPH_ONLY", **common}
    return {"outcome": "LINK_GRAPH_CLOSED", "reason_code": "FULL_LOCAL_CLOSURE_CONFIRMED", **common}


def _semantic_findings(value: Mapping[str, Any]) -> tuple[Finding, ...]:
    out: set[Finding] = set()
    records = value["records"]
    record_ids = [record["record_id"] for record in records]
    if record_ids != sorted(record_ids) or len(record_ids) != len(set(record_ids)):
        out.add(Finding("STAC_LINK_RECORD_ORDER_INVALID", "/records"))
    for index, record in enumerate(records):
        keys = [_link_key(link) for link in record["links"]]
        if keys != sorted(keys) or len(keys) != len(set(keys)):
            out.add(Finding("STAC_LINK_LINK_ORDER_INVALID", f"/records/{index}/links"))
    roots = [record for record in records if record["record_id"] == value["root_record_id"]]
    if len(roots) != 1 or roots[0]["record_type"] != "CATALOG":
        out.add(Finding("STAC_LINK_ROOT_INVALID", "/root_record_id"))
    if not out and value["assessment"] != expected_assessment(value):
        out.add(Finding("STAC_LINK_ASSESSMENT_MISMATCH", "/assessment"))
    try:
        expected_hash, expected_id = canonical_identity(value)
    except CanonicalizationFailure:
        out.add(Finding("STAC_LINK_CANONICALIZATION_FAILED", "/spec_hash"))
    else:
        if value["spec_hash"] != expected_hash:
            out.add(Finding("STAC_LINK_SPEC_HASH_MISMATCH", "/spec_hash"))
        if value["assessment_id"] != expected_id:
            out.add(Finding("STAC_LINK_ASSESSMENT_ID_MISMATCH", "/assessment_id"))
    return tuple(sorted(out))


def validate_payload(value: Mapping[str, Any]) -> Result:
    schema = _schema_findings(value)
    if schema:
        return Result("DENY", schema)
    semantic = _semantic_findings(value)
    if semantic:
        return Result("DENY", semantic)
    outcome = value["assessment"]["outcome"]
    if outcome == "PARTIAL_GRAPH":
        return Result("ABSTAIN", (Finding("STAC_LINK_PARTIAL_GRAPH", "/assessment/outcome"),))
    if outcome == "LINK_GRAPH_OPEN":
        return Result("DENY", (Finding("STAC_LINK_GRAPH_OPEN", "/assessment/outcome"),))
    if outcome == "ERROR":
        return Result("ERROR", (Finding("STAC_LINK_UPSTREAM_ERROR", "/assessment/outcome"),))
    return Result("PASS", ())


def validate_file(path: Path) -> Result:
    value, findings = _read(path)
    return Result("ERROR", findings) if value is None else validate_payload(value)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    args = parser.parse_args(argv)
    result = validate_file(args.input)
    print(json.dumps({
        "authority": "NONE",
        "execution_mode": "FIXTURE_ONLY",
        "file": args.input.as_posix(),
        "findings": [{"code": item.code, "path": item.path} for item in result.findings],
        "non_effects": ["no_network_or_remote_resolution", "no_record_or_api_validation", "no_availability_claim", "no_catalog_policy_release_or_publication"],
        "outcome": result.outcome,
    }, sort_keys=True, separators=(",", ":")))
    return {"PASS": 0, "DENY": 1, "ERROR": 2, "ABSTAIN": 3}[result.outcome]


if __name__ == "__main__":
    raise SystemExit(main())
