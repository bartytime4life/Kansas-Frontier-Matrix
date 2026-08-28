#!/usr/bin/env python3
"""Compare two synthetic SDA micro-snapshots without source access.

The helper canonicalizes a bounded subset of SSURGO/SDA-like component rows,
checks map-unit identity, component percentage closure, and field ranges, then
emits a deterministic human-review report.  It separates a content spec hash
from a retrieval hash so a new retrieval timestamp alone does not create false
material change.  It performs no network access, source activation, lifecycle
write, operational receipt signing, policy approval, promotion, release, or
publication.
"""

from __future__ import annotations

import argparse
import copy
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
import hashlib
import json
import math
import re
import sys
from typing import Any, Mapping, Sequence

PROFILE_ID = "kfm.ssurgo-sda-micro-snapshot.synthetic.v1"
OBJECT_TYPE = "SyntheticSdaMicroSnapshotDiffReport"
SCHEMA_VERSION = "1.0.0"
SOURCE_DESCRIPTOR_REF = "fixture://source/nrcs-sda"
MAX_ROWS = 5_000
OUTCOMES = frozenset(
    {"NO_MATERIAL_CHANGE", "PROPOSED_WORK_RECORD", "VALIDATION_HOLD", "ERROR"}
)

_MUKEY = re.compile(r"SYN-MU-[A-Z0-9][A-Z0-9_-]{0,63}\Z")
_COKEY = re.compile(r"SYN-CO-[A-Z0-9][A-Z0-9_-]{0,63}\Z")
_PRODUCT_VERSION = re.compile(r"SYNTHETIC-[A-Z0-9][A-Z0-9_.-]{0,95}\Z")
_DRAINAGE = re.compile(r"[a-z][a-z0-9_]{0,63}\Z")


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


@dataclass(frozen=True)
class ComparisonResult:
    outcome: str
    reason_codes: tuple[str, ...]
    report: dict[str, Any] | None
    findings: tuple[Finding, ...]

    @property
    def ok(self) -> bool:
        return self.outcome == "NO_MATERIAL_CHANGE" and self.report is not None


class DuplicateKeyError(ValueError):
    pass


def _reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result


def _reject_nonfinite(raw: str) -> object:
    raise ValueError(f"non-finite JSON value denied: {raw}")


def canonical_bytes(value: object) -> bytes:
    return json.dumps(
        value,
        ensure_ascii=True,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")


def _sha256(value: object) -> str:
    return "sha256:" + hashlib.sha256(canonical_bytes(value)).hexdigest()


def _finite_number(value: object) -> bool:
    return (
        isinstance(value, (int, float))
        and not isinstance(value, bool)
        and math.isfinite(float(value))
    )


def _nonempty_string(value: object) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _parse_utc(value: object) -> datetime | None:
    if not isinstance(value, str) or not value.endswith("Z") or "T" not in value:
        return None
    try:
        parsed = datetime.fromisoformat(value[:-1] + "+00:00")
    except ValueError:
        return None
    if parsed.tzinfo is None or parsed.utcoffset() != timedelta(0):
        return None
    return parsed.astimezone(timezone.utc)


def _canonical_strings(value: object, *, nonempty: bool = False) -> bool:
    return (
        isinstance(value, list)
        and (bool(value) or not nonempty)
        and all(_nonempty_string(item) for item in value)
        and value == sorted(set(value))
    )


def _add(findings: set[Finding], code: str, path: str) -> None:
    findings.add(Finding(code=code, path=path))


def _unknown_fields(value: Mapping[object, object], allowed: set[str]) -> list[object]:
    return sorted(
        (field for field in value if field not in allowed),
        key=lambda field: (type(field).__name__, repr(field)),
    )


def canonical_rows(rows: Sequence[Mapping[str, object]]) -> list[dict[str, object]]:
    """Normalize numeric types and return stable row/key ordering."""

    normalized: list[dict[str, object]] = []
    for row in rows:
        normalized.append(
            {
                "cokey": row["cokey"],
                "component_pct": float(row["component_pct"]),
                "drainage_class": row["drainage_class"],
                "mukey": row["mukey"],
                "slope_r": float(row["slope_r"]),
            }
        )
    return sorted(normalized, key=lambda row: (str(row["mukey"]), str(row["cokey"])))


def compute_content_spec_hash(snapshot: Mapping[str, object]) -> str:
    rows = snapshot.get("rows")
    canonical = canonical_rows(rows) if isinstance(rows, list) else []
    payload = {
        "profile_id": snapshot.get("profile_id"),
        "fixture_only": snapshot.get("fixture_only"),
        "source_descriptor_ref": snapshot.get("source_descriptor_ref"),
        "product_version": snapshot.get("product_version"),
        "source_etag": snapshot.get("source_etag"),
        "rows": canonical,
    }
    return _sha256(payload)


def compute_retrieval_hash(snapshot: Mapping[str, object]) -> str:
    payload = {
        "content_spec_hash": compute_content_spec_hash(snapshot),
        "retrieval_timestamp": snapshot.get("retrieval_timestamp"),
        "evidence_refs": snapshot.get("evidence_refs"),
    }
    return _sha256(payload)


def compute_row_set_hash(snapshot: Mapping[str, object]) -> str:
    rows = snapshot.get("rows")
    canonical = canonical_rows(rows) if isinstance(rows, list) else []
    return _sha256(canonical)


def _validate_row(findings: set[Finding], row: object, index: int) -> tuple[str, str] | None:
    path = f"/rows/{index}"
    if not isinstance(row, dict):
        _add(findings, "ROW_INVALID", path)
        return None
    allowed = {"mukey", "cokey", "component_pct", "slope_r", "drainage_class"}
    for field in _unknown_fields(row, allowed):
        _add(findings, "ROW_FIELD_UNKNOWN", f"{path}/{field}")
    if set(row) != allowed:
        _add(findings, "ROW_FIELDS_INVALID", path)

    mukey = row.get("mukey")
    cokey = row.get("cokey")
    if not isinstance(mukey, str) or _MUKEY.fullmatch(mukey) is None:
        _add(findings, "MUKEY_NOT_SYNTHETIC", f"{path}/mukey")
    if not isinstance(cokey, str) or _COKEY.fullmatch(cokey) is None:
        _add(findings, "COKEY_NOT_SYNTHETIC", f"{path}/cokey")

    component_pct = row.get("component_pct")
    if not _finite_number(component_pct) or not 0.0 <= float(component_pct) <= 100.0:
        _add(findings, "COMPONENT_PCT_OUT_OF_RANGE", f"{path}/component_pct")
    slope = row.get("slope_r")
    if not _finite_number(slope) or not 0.0 <= float(slope) <= 100.0:
        _add(findings, "SLOPE_R_OUT_OF_RANGE", f"{path}/slope_r")
    drainage = row.get("drainage_class")
    if not isinstance(drainage, str) or _DRAINAGE.fullmatch(drainage) is None:
        _add(findings, "DRAINAGE_CLASS_INVALID", f"{path}/drainage_class")

    if isinstance(mukey, str) and isinstance(cokey, str):
        return mukey, cokey
    return None


def validate_snapshot(candidate: object) -> tuple[Finding, ...]:
    findings: set[Finding] = set()
    if not isinstance(candidate, dict):
        return (Finding("SNAPSHOT_NOT_OBJECT", "/"),)

    allowed = {
        "profile_id",
        "fixture_only",
        "source_descriptor_ref",
        "product_version",
        "source_etag",
        "retrieval_timestamp",
        "evidence_refs",
        "rows",
    }
    for field in _unknown_fields(candidate, allowed):
        _add(findings, "TOP_LEVEL_FIELD_UNKNOWN", f"/{field}")
    if set(candidate) != allowed:
        _add(findings, "TOP_LEVEL_FIELDS_INVALID", "/")
    if candidate.get("profile_id") != PROFILE_ID:
        _add(findings, "PROFILE_ID_INVALID", "/profile_id")
    if candidate.get("fixture_only") is not True:
        _add(findings, "FIXTURE_ONLY_REQUIRED", "/fixture_only")
    if candidate.get("source_descriptor_ref") != SOURCE_DESCRIPTOR_REF:
        _add(findings, "SOURCE_DESCRIPTOR_REF_INVALID", "/source_descriptor_ref")

    version = candidate.get("product_version")
    if not isinstance(version, str) or _PRODUCT_VERSION.fullmatch(version) is None:
        _add(findings, "PRODUCT_VERSION_NOT_SYNTHETIC", "/product_version")
    if not _nonempty_string(candidate.get("source_etag")):
        _add(findings, "SOURCE_ETAG_MISSING", "/source_etag")
    if _parse_utc(candidate.get("retrieval_timestamp")) is None:
        _add(findings, "RETRIEVAL_TIMESTAMP_INVALID", "/retrieval_timestamp")
    if not _canonical_strings(candidate.get("evidence_refs"), nonempty=True):
        _add(findings, "EVIDENCE_REFS_NOT_CANONICAL", "/evidence_refs")

    rows = candidate.get("rows")
    identities: set[tuple[str, str]] = set()
    cokeys: set[str] = set()
    component_sums: dict[str, float] = {}
    if not isinstance(rows, list) or not rows:
        _add(findings, "ROWS_EMPTY", "/rows")
    elif len(rows) > MAX_ROWS:
        _add(findings, "ROW_COUNT_EXCEEDED", "/rows")
    else:
        for index, row in enumerate(rows):
            identity = _validate_row(findings, row, index)
            if identity is None:
                continue
            mukey, cokey = identity
            if identity in identities:
                _add(findings, "ROW_IDENTITY_DUPLICATE", f"/rows/{index}")
            identities.add(identity)
            if cokey in cokeys:
                _add(findings, "COKEY_DUPLICATE", f"/rows/{index}/cokey")
            cokeys.add(cokey)
            component_pct = row.get("component_pct") if isinstance(row, dict) else None
            if _finite_number(component_pct):
                component_sums[mukey] = component_sums.get(mukey, 0.0) + float(component_pct)

        for mukey, component_sum in sorted(component_sums.items()):
            if abs(component_sum - 100.0) > 1.0:
                _add(findings, "COMPONENT_PCT_SUM_OUTSIDE_TOLERANCE", f"/rows@mukey={mukey}")

    return tuple(sorted(findings))


def _snapshot_summary(snapshot: Mapping[str, object]) -> dict[str, object]:
    rows = snapshot["rows"]
    assert isinstance(rows, list)
    return {
        "content_spec_hash": compute_content_spec_hash(snapshot),
        "retrieval_hash": compute_retrieval_hash(snapshot),
        "row_set_hash": compute_row_set_hash(snapshot),
        "product_version": snapshot["product_version"],
        "source_etag": snapshot["source_etag"],
        "retrieval_timestamp": snapshot["retrieval_timestamp"],
        "row_count": len(rows),
    }


def compare_snapshots(prior: object, current: object) -> ComparisonResult:
    """Validate and compare two synthetic snapshots without mutating either input."""

    prior_copy = copy.deepcopy(prior)
    current_copy = copy.deepcopy(current)
    prior_findings = validate_snapshot(prior_copy)
    current_findings = validate_snapshot(current_copy)
    findings = tuple(
        sorted(
            [Finding(finding.code, f"/prior{finding.path}") for finding in prior_findings]
            + [Finding(finding.code, f"/current{finding.path}") for finding in current_findings]
        )
    )
    if findings:
        return ComparisonResult(
            outcome="VALIDATION_HOLD",
            reason_codes=("SDA_MICRO_SNAPSHOT_VALIDATION_FAILED",),
            report=None,
            findings=findings,
        )

    assert isinstance(prior_copy, dict) and isinstance(current_copy, dict)
    prior_rows = {
        (str(row["mukey"]), str(row["cokey"])): row
        for row in canonical_rows(prior_copy["rows"])  # type: ignore[arg-type]
    }
    current_rows = {
        (str(row["mukey"]), str(row["cokey"])): row
        for row in canonical_rows(current_copy["rows"])  # type: ignore[arg-type]
    }

    prior_keys = set(prior_rows)
    current_keys = set(current_rows)
    added_keys = sorted(current_keys - prior_keys)
    removed_keys = sorted(prior_keys - current_keys)
    field_changes: list[dict[str, object]] = []
    for key in sorted(prior_keys & current_keys):
        prior_row = prior_rows[key]
        current_row = current_rows[key]
        for field in ("component_pct", "drainage_class", "slope_r"):
            if prior_row[field] != current_row[field]:
                field_changes.append(
                    {
                        "mukey": key[0],
                        "cokey": key[1],
                        "field": field,
                        "prior": prior_row[field],
                        "current": current_row[field],
                    }
                )

    metadata_fields = [
        field
        for field in ("product_version", "source_etag")
        if prior_copy[field] != current_copy[field]
    ]
    material = bool(added_keys or removed_keys or field_changes or metadata_fields)
    outcome = "PROPOSED_WORK_RECORD" if material else "NO_MATERIAL_CHANGE"

    reason_codes: list[str] = []
    if metadata_fields:
        reason_codes.append("SOURCE_METADATA_CHANGED")
    if added_keys:
        reason_codes.append("SDA_ROWS_ADDED")
    if removed_keys:
        reason_codes.append("SDA_ROWS_REMOVED")
    if field_changes:
        reason_codes.append("SDA_FIELDS_CHANGED")
    reason_codes.sort()

    prior_summary = _snapshot_summary(prior_copy)
    current_summary = _snapshot_summary(current_copy)
    comparison_id = _sha256(
        {
            "profile_id": PROFILE_ID,
            "prior_content_spec_hash": prior_summary["content_spec_hash"],
            "current_content_spec_hash": current_summary["content_spec_hash"],
            "outcome": outcome,
        }
    )
    evidence_refs = sorted(
        set(prior_copy["evidence_refs"]) | set(current_copy["evidence_refs"])  # type: ignore[arg-type]
    )

    report = {
        "object_type": OBJECT_TYPE,
        "schema_version": SCHEMA_VERSION,
        "profile_id": PROFILE_ID,
        "fixture_only": True,
        "comparison_id": comparison_id,
        "prior": prior_summary,
        "current": current_summary,
        "validation": {
            "status": "pass",
            "checks": [
                "component_pct_sum_within_one_percentage_point",
                "identity_uniqueness",
                "mukey_presence",
                "slope_r_range_0_100",
                "synthetic_fixture_boundary",
            ],
        },
        "diff_summary": {
            "metadata_changed_fields": metadata_fields,
            "rows_added": len(added_keys),
            "rows_removed": len(removed_keys),
            "fields_changed": len(field_changes),
        },
        "added_rows": [
            {"mukey": mukey, "cokey": cokey} for mukey, cokey in added_keys
        ],
        "removed_rows": [
            {"mukey": mukey, "cokey": cokey} for mukey, cokey in removed_keys
        ],
        "field_changes": field_changes,
        "outcome": outcome,
        "reason_codes": reason_codes,
        "evidence_refs": evidence_refs,
        "governance": {
            "promotion_allowed": False,
            "publication_allowed": False,
            "release_state": "not_released",
            "review_state": "fixture_only",
            "steward_review_required": outcome != "NO_MATERIAL_CHANGE",
        },
    }
    return ComparisonResult(
        outcome=outcome,
        reason_codes=tuple(reason_codes),
        report=report,
        findings=(),
    )


def load_snapshot(path: str) -> object:
    with open(path, "r", encoding="utf-8") as stream:
        return json.load(
            stream,
            object_pairs_hook=_reject_duplicate_keys,
            parse_constant=_reject_nonfinite,
        )


def _main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Compare synthetic SDA micro-snapshots")
    parser.add_argument("--prior", required=True)
    parser.add_argument("--current", required=True)
    args = parser.parse_args(argv)
    try:
        prior = load_snapshot(args.prior)
        current = load_snapshot(args.current)
    except (OSError, UnicodeError, json.JSONDecodeError, DuplicateKeyError, ValueError):
        result = ComparisonResult(
            outcome="ERROR",
            reason_codes=("SDA_MICRO_SNAPSHOT_INPUT_ERROR",),
            report=None,
            findings=(Finding("INPUT_UNREADABLE_OR_INVALID", "/"),),
        )
    else:
        result = compare_snapshots(prior, current)

    print(
        json.dumps(
            {
                "outcome": result.outcome,
                "reason_codes": list(result.reason_codes),
                "findings": [finding.__dict__ for finding in result.findings],
                "report": result.report,
            },
            sort_keys=True,
            indent=2,
        )
    )
    if result.outcome == "NO_MATERIAL_CHANGE":
        return 0
    if result.outcome in {"PROPOSED_WORK_RECORD", "VALIDATION_HOLD"}:
        return 1
    return 2


if __name__ == "__main__":
    sys.exit(_main())
