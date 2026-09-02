#!/usr/bin/env python3
"""Validate the synthetic USDA PLANTS Kansas distribution snapshot profile."""

from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path
from typing import Sequence

from jsonschema import Draft202012Validator

REPO_ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(REPO_ROOT))

from tools.validators._common.public_safe_fixture import (  # noqa: E402
    Finding,
    add_finding,
    run_cli,
    serialize_result,
    validate_fixture_file,
)

SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/domains/flora/"
    "usda_plants_distribution_snapshot.schema.json"
)
FIXTURES_ROOT = (
    REPO_ROOT
    / "fixtures/domains/flora/usda_plants_distribution_snapshot"
)
SCOPE = "flora.usda_plants_distribution_snapshot"
SOURCE_URI = "https://plants.sc.egov.usda.gov/downloads"
FORBIDDEN_GEOMETRY_KEYS = frozenset(
    {
        "coordinate",
        "coordinates",
        "decimallatitude",
        "decimallongitude",
        "geometry",
        "geom",
        "latitude",
        "longitude",
        "wkt",
    }
)
INTERNAL_LIFECYCLE_MARKERS = (
    "/data/raw/",
    "/data/work/",
    "/data/quarantine/",
    "data/raw/",
    "data/work/",
    "data/quarantine/",
)

_SCHEMA = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
_SCHEMA_VALIDATOR = Draft202012Validator(_SCHEMA)


def canonical_spec_hash(document: dict[str, object]) -> str:
    """Hash canonical JSON after removing the top-level spec_hash field."""

    identity = {key: value for key, value in document.items() if key != "spec_hash"}
    canonical = json.dumps(
        identity,
        ensure_ascii=True,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return f"sha256:{hashlib.sha256(canonical).hexdigest()}"


def _json_path(parts: Sequence[object]) -> str:
    result = "$"
    for part in parts:
        result += f"[{part}]" if isinstance(part, int) else f".{part}"
    return result


def _scan_payload(value: object) -> list[Finding]:
    findings: set[Finding] = set()
    pending: list[tuple[object, str]] = [(value, "$")]
    while pending:
        current, path = pending.pop()
        if isinstance(current, dict):
            for key, item in current.items():
                child_path = f"{path}.{key}"
                if key.lower() in FORBIDDEN_GEOMETRY_KEYS:
                    add_finding(
                        findings,
                        "USDA_PLANTS_EXACT_GEOMETRY_FIELD_DENIED",
                        child_path,
                    )
                pending.append((item, child_path))
        elif isinstance(current, list):
            pending.extend(
                (item, f"{path}[{index}]")
                for index, item in enumerate(current)
            )
        elif isinstance(current, str):
            normalized = current.lower()
            if any(marker in normalized for marker in INTERNAL_LIFECYCLE_MARKERS):
                add_finding(
                    findings,
                    "USDA_PLANTS_INTERNAL_LIFECYCLE_REF_DENIED",
                    path,
                )
    return sorted(findings)


def _has_authorship(scientific_name: object) -> bool:
    if not isinstance(scientific_name, str):
        return False
    tokens = scientific_name.split()
    return len(tokens) >= 3 and any(character.isalpha() for character in tokens[-1])


def validate_document(candidate: object) -> list[Finding]:
    """Validate schema, deterministic identity, completeness, and no-row semantics."""

    findings: set[Finding] = set(_scan_payload(candidate))

    schema_errors = sorted(
        _SCHEMA_VALIDATOR.iter_errors(candidate),
        key=lambda error: tuple(str(part) for part in error.absolute_path),
    )
    for error in schema_errors:
        add_finding(
            findings,
            "USDA_PLANTS_DISTRIBUTION_SCHEMA_INVALID",
            _json_path(tuple(error.absolute_path)),
        )
    if schema_errors or not isinstance(candidate, dict):
        return sorted(findings)

    snapshot_date = candidate["snapshot_date"]
    assert isinstance(snapshot_date, str)
    try:
        parsed_date = date.fromisoformat(snapshot_date)
    except ValueError:
        add_finding(
            findings,
            "USDA_PLANTS_SNAPSHOT_DATE_INVALID",
            "$.snapshot_date",
        )
    else:
        if parsed_date.isoformat() != snapshot_date:
            add_finding(
                findings,
                "USDA_PLANTS_SNAPSHOT_DATE_INVALID",
                "$.snapshot_date",
            )

    expected_snapshot_id = (
        f"kfm://candidate/flora/usda-plants/distribution/ks/{snapshot_date}"
    )
    if candidate["snapshot_id"] != expected_snapshot_id:
        add_finding(
            findings,
            "USDA_PLANTS_SNAPSHOT_ID_MISMATCH",
            "$.snapshot_id",
        )
    if candidate["source_ref"] != f"kfm://source/flora/usda-plants@{snapshot_date}":
        add_finding(
            findings,
            "USDA_PLANTS_SOURCE_REF_MISMATCH",
            "$.source_ref",
        )
    if candidate["source_uri"] != SOURCE_URI:
        add_finding(
            findings,
            "USDA_PLANTS_SOURCE_URI_MISMATCH",
            "$.source_uri",
        )
    if candidate["spec_hash"] != canonical_spec_hash(candidate):
        add_finding(
            findings,
            "USDA_PLANTS_SPEC_HASH_MISMATCH",
            "$.spec_hash",
        )

    scope = candidate["scope"]
    taxa = candidate["taxa"]
    source_rows = candidate["source_rows"]
    states = candidate["distribution_states"]
    summary = candidate["summary"]
    assert isinstance(scope, dict)
    assert isinstance(taxa, list)
    assert isinstance(source_rows, list)
    assert isinstance(states, list)
    assert isinstance(summary, dict)

    counties = scope["counties"]
    assert isinstance(counties, list)
    county_fips = [county["fips"] for county in counties]
    if county_fips != sorted(county_fips):
        add_finding(
            findings,
            "USDA_PLANTS_COUNTY_ORDER_INVALID",
            "$.scope.counties",
        )
    if len(set(county_fips)) != len(county_fips):
        add_finding(
            findings,
            "USDA_PLANTS_COUNTY_DUPLICATE",
            "$.scope.counties",
        )

    taxon_symbols = [taxon["plants_symbol"] for taxon in taxa]
    if taxon_symbols != sorted(taxon_symbols):
        add_finding(
            findings,
            "USDA_PLANTS_TAXON_ORDER_INVALID",
            "$.taxa",
        )
    if len(set(taxon_symbols)) != len(taxon_symbols):
        add_finding(
            findings,
            "USDA_PLANTS_TAXON_DUPLICATE",
            "$.taxa",
        )
    for index, taxon in enumerate(taxa):
        if not _has_authorship(taxon["scientific_name"]):
            add_finding(
                findings,
                "USDA_PLANTS_SCIENTIFIC_AUTHORSHIP_MISSING",
                f"$.taxa[{index}].scientific_name",
            )

    known_taxa = set(taxon_symbols)
    known_counties = set(county_fips)
    expected_pairs = {
        (symbol, fips)
        for symbol in taxon_symbols
        for fips in county_fips
    }

    source_pairs: list[tuple[str, str]] = []
    source_presence: dict[tuple[str, str], str] = {}
    for index, row in enumerate(source_rows):
        key = (row["plants_symbol"], row["county_fips"])
        source_pairs.append(key)
        if row["plants_symbol"] not in known_taxa:
            add_finding(
                findings,
                "USDA_PLANTS_SOURCE_ROW_TAXON_UNKNOWN",
                f"$.source_rows[{index}].plants_symbol",
            )
        if row["county_fips"] not in known_counties:
            add_finding(
                findings,
                "USDA_PLANTS_SOURCE_ROW_COUNTY_UNKNOWN",
                f"$.source_rows[{index}].county_fips",
            )
        if key in source_presence:
            add_finding(
                findings,
                "USDA_PLANTS_SOURCE_ROW_DUPLICATE",
                f"$.source_rows[{index}]",
            )
        source_presence[key] = row["normalized_presence"]

    if source_pairs != sorted(source_pairs):
        add_finding(
            findings,
            "USDA_PLANTS_SOURCE_ROW_ORDER_INVALID",
            "$.source_rows",
        )

    state_pairs: list[tuple[str, str]] = []
    state_by_pair: dict[tuple[str, str], dict[str, object]] = {}
    for index, item in enumerate(states):
        key = (item["plants_symbol"], item["county_fips"])
        state_pairs.append(key)
        if item["plants_symbol"] not in known_taxa:
            add_finding(
                findings,
                "USDA_PLANTS_STATE_TAXON_UNKNOWN",
                f"$.distribution_states[{index}].plants_symbol",
            )
        if item["county_fips"] not in known_counties:
            add_finding(
                findings,
                "USDA_PLANTS_STATE_COUNTY_UNKNOWN",
                f"$.distribution_states[{index}].county_fips",
            )
        if key in state_by_pair:
            add_finding(
                findings,
                "USDA_PLANTS_DISTRIBUTION_PAIR_DUPLICATE",
                f"$.distribution_states[{index}]",
            )
        state_by_pair[key] = item

        source_value = source_presence.get(key)
        declared_state = item["state"]
        if source_value == "present":
            expected_state = "reported_present"
            expected_interpretation = "administrative_presence_claim"
            expected_row_present = True
        elif source_value == "absent":
            expected_state = "reported_absent"
            expected_interpretation = "administrative_absence_claim"
            expected_row_present = True
        else:
            expected_state = "not_reported"
            expected_interpretation = "no_claim"
            expected_row_present = False

        if declared_state != expected_state:
            add_finding(
                findings,
                "USDA_PLANTS_DISTRIBUTION_STATE_SOURCE_MISMATCH",
                f"$.distribution_states[{index}].state",
            )
        if item["interpretation"] != expected_interpretation:
            add_finding(
                findings,
                "USDA_PLANTS_DISTRIBUTION_INTERPRETATION_MISMATCH",
                f"$.distribution_states[{index}].interpretation",
            )
        if item["source_row_present"] is not expected_row_present:
            add_finding(
                findings,
                "USDA_PLANTS_SOURCE_ROW_PRESENCE_MISMATCH",
                f"$.distribution_states[{index}].source_row_present",
            )
        if (
            declared_state == "reported_absent"
            and source_value != "absent"
        ):
            add_finding(
                findings,
                "USDA_PLANTS_EXPLICIT_ABSENCE_ROW_REQUIRED",
                f"$.distribution_states[{index}].state",
            )

    if state_pairs != sorted(state_pairs):
        add_finding(
            findings,
            "USDA_PLANTS_DISTRIBUTION_ORDER_INVALID",
            "$.distribution_states",
        )

    observed_pairs = set(state_by_pair)
    if observed_pairs != expected_pairs:
        add_finding(
            findings,
            "USDA_PLANTS_DISTRIBUTION_COVERAGE_INCOMPLETE",
            "$.distribution_states",
        )

    state_counts = Counter(
        item["state"]
        for item in states
        if isinstance(item.get("state"), str)
    )
    expected_summary = {
        "taxon_count": len(taxa),
        "county_count": len(counties),
        "cell_count": len(states),
        "source_row_count": len(source_rows),
        "reported_present": state_counts["reported_present"],
        "reported_absent": state_counts["reported_absent"],
        "not_reported": state_counts["not_reported"],
        "not_evaluated": state_counts["not_evaluated"],
    }
    for key, value in expected_summary.items():
        if summary[key] != value:
            add_finding(
                findings,
                "USDA_PLANTS_SUMMARY_MISMATCH",
                f"$.summary.{key}",
            )

    review = candidate["review"]
    assert isinstance(review, dict)
    if (
        review["rights"] != "NEEDS_VERIFICATION"
        or review["sensitivity"] != "NEEDS_VERIFICATION"
        or review["release"] != "HOLD"
    ):
        add_finding(
            findings,
            "USDA_PLANTS_REVIEW_HOLD_REQUIRED",
            "$.review",
        )

    return sorted(findings)


def validate_snapshot_file(path: Path | str) -> list[Finding]:
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
            findings = validate_snapshot_file(path)
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
        description="Validate synthetic USDA PLANTS distribution snapshots.",
        scope=SCOPE,
        validator=validate_snapshot_file,
    )


if __name__ == "__main__":
    raise SystemExit(main())
