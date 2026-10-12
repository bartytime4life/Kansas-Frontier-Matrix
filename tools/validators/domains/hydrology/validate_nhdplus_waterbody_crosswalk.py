#!/usr/bin/env python3
"""Validate the bounded synthetic NHDPlus waterbody crosswalk profile."""

from __future__ import annotations

import hashlib
import json
import sys
from collections import Counter
from pathlib import Path
from typing import Sequence

sys.path.insert(0, str(Path(__file__).resolve().parents[4]))

from tools.validators._common.jsonschema_runner import load_validator
from tools.validators._common.public_safe_fixture import (
    Finding,
    add_finding,
    run_cli,
    serialize_result,
    validate_fixture_file,
)


REPO_ROOT = Path(__file__).resolve().parents[4]
SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/domains/hydrology/nhdplus_waterbody_crosswalk.schema.json"
)
FIXTURES_ROOT = (
    REPO_ROOT / "fixtures/domains/hydrology/nhdplus_waterbody_crosswalk"
)
SCOPE = "hydrology.nhdplus_waterbody_crosswalk"
_SCHEMA_VALIDATOR = load_validator(SCHEMA_PATH)


def canonical_spec_hash(document: dict[str, object]) -> str:
    """Return the canonical hash of every profile field except spec_hash."""

    identity_document = {
        key: value for key, value in document.items() if key != "spec_hash"
    }
    canonical = json.dumps(
        identity_document,
        ensure_ascii=True,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return f"sha256:{hashlib.sha256(canonical).hexdigest()}"


def _json_path(error_path: Sequence[object]) -> str:
    result = "$"
    for part in error_path:
        result += f"[{part}]" if isinstance(part, int) else f".{part}"
    return result


def _expected_relationship(
    source_count: int,
    target_count: int,
) -> tuple[str, str]:
    if source_count == 1 and target_count == 1:
        return "exact", "ANSWER"
    if source_count > 1 and target_count == 1:
        return "split", "ABSTAIN"
    if source_count == 1 and target_count > 1:
        return "merge", "ABSTAIN"
    return "complex", "ABSTAIN"


def validate_document(candidate: object) -> list[Finding]:
    """Validate closed shape, deterministic identity, and mapping cardinality."""

    findings: set[Finding] = set()
    schema_errors = sorted(
        _SCHEMA_VALIDATOR.iter_errors(candidate),
        key=lambda error: tuple(str(part) for part in error.absolute_path),
    )
    for error in schema_errors:
        add_finding(
            findings,
            "NHDPLUS_WATERBODY_CROSSWALK_SCHEMA_INVALID",
            _json_path(tuple(error.absolute_path)),
        )
    if schema_errors or not isinstance(candidate, dict):
        return sorted(findings)

    declared_hash = candidate["spec_hash"]
    if declared_hash != canonical_spec_hash(candidate):
        add_finding(findings, "NHDPLUS_WATERBODY_CROSSWALK_HASH_MISMATCH", "$.spec_hash")

    records = candidate["records"]
    assert isinstance(records, list)
    ordered_keys = [
        (
            record["nhdplus_hr_permanent_identifier"],
            record["nhdplus_v2_comid"],
        )
        for record in records
    ]
    if ordered_keys != sorted(ordered_keys):
        add_finding(findings, "NHDPLUS_WATERBODY_CROSSWALK_ORDER_INVALID", "$.records")

    source_counts = Counter(source_id for source_id, _target_id in ordered_keys)
    target_counts = Counter(target_id for _source_id, target_id in ordered_keys)
    duplicate_keys = {key for key, count in Counter(ordered_keys).items() if count > 1}

    for index, record in enumerate(records):
        source_id, target_id = ordered_keys[index]
        record_path = f"$.records[{index}]"
        if (source_id, target_id) in duplicate_keys:
            add_finding(
                findings,
                "NHDPLUS_WATERBODY_CROSSWALK_DUPLICATE_PAIR",
                record_path,
            )

        expected_relationship, expected_outcome = _expected_relationship(
            source_counts[source_id], target_counts[target_id]
        )
        if record["relationship_type"] != expected_relationship:
            add_finding(
                findings,
                "NHDPLUS_WATERBODY_CROSSWALK_CARDINALITY_MISMATCH",
                f"{record_path}.relationship_type",
            )
        if record["outcome"] != expected_outcome:
            add_finding(
                findings,
                "NHDPLUS_WATERBODY_CROSSWALK_AMBIGUITY_COLLAPSED",
                f"{record_path}.outcome",
            )

        shared_area = record["shared_area_m2"]
        if (
            shared_area > record["nhdplus_hr_area_m2"]
            or shared_area > record["nhdplus_v2_area_m2"]
        ):
            add_finding(
                findings,
                "NHDPLUS_WATERBODY_CROSSWALK_OVERLAP_AREA_INVALID",
                f"{record_path}.shared_area_m2",
            )

    return sorted(findings)


def validate_crosswalk_file(path: Path | str) -> list[Finding]:
    return validate_fixture_file(path, validate_document)


def _run_fixture_suite() -> int:
    ok = True
    for expected_valid, directory in (
        (True, FIXTURES_ROOT / "valid"),
        (False, FIXTURES_ROOT / "invalid"),
    ):
        files = sorted(directory.glob("*.json"))
        if not files:
            print(f"FAIL {directory}: no JSON fixtures found")
            ok = False
            continue
        for path in files:
            findings = validate_crosswalk_file(path)
            accepted = not findings
            if accepted == expected_valid:
                label = "OK" if expected_valid else "EXPECTED_FAIL"
                print(f"{label} {path}")
            else:
                print(serialize_result(SCOPE, path, findings))
                ok = False
    return 0 if ok else 1


def main(argv: Sequence[str] | None = None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    if args == ["--fixtures"]:
        return _run_fixture_suite()
    if "--fixtures" in args:
        print("--fixtures cannot be combined with file arguments", file=sys.stderr)
        return 2
    return run_cli(
        argv=args,
        description="Validate synthetic NHDPlus waterbody crosswalk fixtures.",
        scope=SCOPE,
        validator=validate_crosswalk_file,
    )


if __name__ == "__main__":
    raise SystemExit(main())
