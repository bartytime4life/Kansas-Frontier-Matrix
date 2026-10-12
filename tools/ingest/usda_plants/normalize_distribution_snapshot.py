#!/usr/bin/env python3
"""Build a deterministic synthetic USDA PLANTS Kansas distribution snapshot.

This tool is intentionally fixture-first and no-network. It accepts a small,
explicit CSV profile rather than claiming compatibility with current USDA
download headers. Live source activation, source terms, and exact file layouts
remain separate governed work.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import stat
import sys
from datetime import date
from pathlib import Path
from typing import Iterable, Sequence

MAX_INPUT_BYTES = 1_000_000
SYMBOL_RE = re.compile(r"^[A-Z][A-Z0-9]{1,9}$")
KANSAS_FIPS_RE = re.compile(r"^20[0-9]{3}$")
SHA256_RE = re.compile(r"^sha256:[a-f0-9]{64}$")
EVIDENCE_REF_RE = re.compile(
    r"^kfm://evidence/flora/usda-plants/[^@\s]+@sha256:[a-f0-9]{64}$"
)
SOURCE_URI = "https://plants.sc.egov.usda.gov/downloads"
PROFILE = "kfm.flora.usda-plants-distribution-snapshot.v1"
NORMALIZER = "kfm-usda-plants-distribution-normalizer@1.0.0"
INPUT_PROFILE = "kfm.synthetic.usda-plants-distribution-csv.v1"
EXPECTED_HEADERS = {
    "taxa": ("plants_symbol", "scientific_name", "family"),
    "counties": ("fips", "name"),
    "distribution": ("plants_symbol", "county_fips", "presence"),
}


class NormalizationError(ValueError):
    """A stable, user-safe normalization failure."""

    def __init__(self, code: str) -> None:
        super().__init__(code)
        self.code = code


def _read_regular_file(path: Path) -> bytes:
    flags = os.O_RDONLY
    for flag_name in ("O_BINARY", "O_CLOEXEC", "O_NONBLOCK", "O_NOFOLLOW"):
        flags |= getattr(os, flag_name, 0)

    try:
        descriptor = os.open(path, flags)
    except OSError as exc:
        raise NormalizationError("INPUT_UNREADABLE") from exc

    try:
        if not stat.S_ISREG(os.fstat(descriptor).st_mode):
            raise NormalizationError("INPUT_NOT_REGULAR_FILE")
        with os.fdopen(descriptor, "rb") as stream:
            descriptor = -1
            payload = stream.read(MAX_INPUT_BYTES + 1)
    finally:
        if descriptor >= 0:
            os.close(descriptor)

    if len(payload) > MAX_INPUT_BYTES:
        raise NormalizationError("INPUT_TOO_LARGE")
    return payload


def _decode_csv(path: Path, profile: str) -> tuple[list[dict[str, str]], str]:
    payload = _read_regular_file(path)
    try:
        text = payload.decode("utf-8")
    except UnicodeError as exc:
        raise NormalizationError("INPUT_NOT_UTF8") from exc

    reader = csv.DictReader(text.splitlines())
    expected = EXPECTED_HEADERS[profile]
    if reader.fieldnames is None or tuple(reader.fieldnames) != expected:
        raise NormalizationError(f"{profile.upper()}_HEADER_INVALID")
    if len(set(reader.fieldnames)) != len(reader.fieldnames):
        raise NormalizationError(f"{profile.upper()}_HEADER_DUPLICATE")

    rows: list[dict[str, str]] = []
    try:
        for raw in reader:
            if raw is None or None in raw:
                raise NormalizationError(f"{profile.upper()}_ROW_INVALID")
            normalized = {
                key: (value or "").strip()
                for key, value in raw.items()
            }
            if not all(normalized.values()):
                raise NormalizationError(f"{profile.upper()}_FIELD_EMPTY")
            rows.append(normalized)
    except csv.Error as exc:
        raise NormalizationError(f"{profile.upper()}_CSV_INVALID") from exc

    digest = f"sha256:{hashlib.sha256(payload).hexdigest()}"
    return rows, digest


def canonical_spec_hash(document: dict[str, object]) -> str:
    """Hash canonical JSON after removing the top-level spec_hash member."""

    identity = {key: value for key, value in document.items() if key != "spec_hash"}
    canonical = json.dumps(
        identity,
        ensure_ascii=True,
        allow_nan=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")
    return f"sha256:{hashlib.sha256(canonical).hexdigest()}"


def _validate_snapshot_date(value: str) -> str:
    try:
        parsed = date.fromisoformat(value)
    except ValueError as exc:
        raise NormalizationError("SNAPSHOT_DATE_INVALID") from exc
    if parsed.isoformat() != value:
        raise NormalizationError("SNAPSHOT_DATE_INVALID")
    return value


def _normalize_taxa(rows: Iterable[dict[str, str]]) -> list[dict[str, str]]:
    taxa: dict[str, dict[str, str]] = {}
    for row in rows:
        symbol = row["plants_symbol"].upper()
        if not SYMBOL_RE.fullmatch(symbol):
            raise NormalizationError("PLANTS_SYMBOL_INVALID")
        if symbol in taxa:
            raise NormalizationError("PLANTS_SYMBOL_DUPLICATE")
        scientific_name = " ".join(row["scientific_name"].split())
        family = " ".join(row["family"].split())
        if len(scientific_name.split()) < 3:
            raise NormalizationError("SCIENTIFIC_AUTHORSHIP_MISSING")
        taxa[symbol] = {
            "plants_symbol": symbol,
            "scientific_name": scientific_name,
            "family": family,
        }
    if not taxa:
        raise NormalizationError("TAXA_EMPTY")
    return [taxa[symbol] for symbol in sorted(taxa)]


def _normalize_counties(rows: Iterable[dict[str, str]]) -> list[dict[str, str]]:
    counties: dict[str, dict[str, str]] = {}
    for row in rows:
        fips = row["fips"]
        if not KANSAS_FIPS_RE.fullmatch(fips):
            raise NormalizationError("COUNTY_FIPS_INVALID")
        if fips in counties:
            raise NormalizationError("COUNTY_FIPS_DUPLICATE")
        counties[fips] = {
            "fips": fips,
            "name": " ".join(row["name"].split()),
        }
    if not counties:
        raise NormalizationError("COUNTIES_EMPTY")
    return [counties[fips] for fips in sorted(counties)]


def _normalize_source_rows(
    rows: Iterable[dict[str, str]],
    taxa: list[dict[str, str]],
    counties: list[dict[str, str]],
) -> list[dict[str, str]]:
    known_taxa = {item["plants_symbol"] for item in taxa}
    known_counties = {item["fips"] for item in counties}
    source_rows: dict[tuple[str, str], dict[str, str]] = {}

    for row in rows:
        symbol = row["plants_symbol"].upper()
        fips = row["county_fips"]
        presence = row["presence"].lower()
        if symbol not in known_taxa:
            raise NormalizationError("DISTRIBUTION_TAXON_UNKNOWN")
        if fips not in known_counties:
            raise NormalizationError("DISTRIBUTION_COUNTY_UNKNOWN")
        if presence not in {"present", "absent"}:
            raise NormalizationError("DISTRIBUTION_PRESENCE_INVALID")
        key = (symbol, fips)
        if key in source_rows:
            raise NormalizationError("DISTRIBUTION_PAIR_DUPLICATE")
        source_rows[key] = {
            "plants_symbol": symbol,
            "county_fips": fips,
            "normalized_presence": presence,
        }

    return [source_rows[key] for key in sorted(source_rows)]


def build_snapshot(
    *,
    taxa_path: Path,
    counties_path: Path,
    distribution_path: Path,
    snapshot_date: str,
    evidence_ref: str,
    source_uri: str = SOURCE_URI,
) -> dict[str, object]:
    """Normalize a bounded synthetic CSV bundle into one snapshot candidate."""

    normalized_date = _validate_snapshot_date(snapshot_date)
    if source_uri != SOURCE_URI:
        raise NormalizationError("SOURCE_URI_UNSUPPORTED")
    if not EVIDENCE_REF_RE.fullmatch(evidence_ref):
        raise NormalizationError("EVIDENCE_REF_INVALID")

    taxa_rows, taxa_digest = _decode_csv(taxa_path, "taxa")
    county_rows, counties_digest = _decode_csv(counties_path, "counties")
    distribution_rows, distribution_digest = _decode_csv(
        distribution_path, "distribution"
    )

    taxa = _normalize_taxa(taxa_rows)
    counties = _normalize_counties(county_rows)
    source_rows = _normalize_source_rows(distribution_rows, taxa, counties)
    source_lookup = {
        (row["plants_symbol"], row["county_fips"]): row["normalized_presence"]
        for row in source_rows
    }

    states: list[dict[str, object]] = []
    for taxon in taxa:
        symbol = taxon["plants_symbol"]
        for county in counties:
            fips = county["fips"]
            presence = source_lookup.get((symbol, fips))
            if presence == "present":
                state = "reported_present"
                interpretation = "administrative_presence_claim"
                row_present = True
            elif presence == "absent":
                state = "reported_absent"
                interpretation = "administrative_absence_claim"
                row_present = True
            else:
                state = "not_reported"
                interpretation = "no_claim"
                row_present = False
            states.append(
                {
                    "plants_symbol": symbol,
                    "county_fips": fips,
                    "state": state,
                    "source_row_present": row_present,
                    "interpretation": interpretation,
                    "first_observed": None,
                }
            )

    counts = {
        state: sum(1 for item in states if item["state"] == state)
        for state in (
            "reported_present",
            "reported_absent",
            "not_reported",
            "not_evaluated",
        )
    }

    candidate: dict[str, object] = {
        "schema_version": PROFILE,
        "object_type": "USDAPlantsDistributionSnapshotCandidate",
        "fixture_only": True,
        "snapshot_id": (
            f"kfm://candidate/flora/usda-plants/distribution/ks/{normalized_date}"
        ),
        "domain": "flora",
        "source_role": "administrative",
        "source_ref": f"kfm://source/flora/usda-plants@{normalized_date}",
        "source_uri": source_uri,
        "snapshot_date": normalized_date,
        "scope": {"state": "KS", "counties": counties},
        "taxa": taxa,
        "source_rows": source_rows,
        "distribution_states": states,
        "summary": {
            "taxon_count": len(taxa),
            "county_count": len(counties),
            "cell_count": len(states),
            "source_row_count": len(source_rows),
            **counts,
        },
        "missing_row_policy": "NO_SOURCE_ROW_IS_NO_CLAIM_NOT_ABSENCE",
        "provenance": {
            "input_profile": INPUT_PROFILE,
            "normalizer": NORMALIZER,
            "input_digests": {
                "taxa": taxa_digest,
                "counties": counties_digest,
                "distribution": distribution_digest,
            },
        },
        "review": {
            "rights": "NEEDS_VERIFICATION",
            "sensitivity": "NEEDS_VERIFICATION",
            "release": "HOLD",
            "holds": [
                "SOURCE_RIGHTS_CURRENTNESS_UNVERIFIED",
                "RARE_PLANT_SENSITIVITY_UNASSESSED",
            ],
        },
        "evidence_refs": [evidence_ref],
    }
    candidate["spec_hash"] = canonical_spec_hash(candidate)
    return candidate


def write_snapshot(candidate: dict[str, object], output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(candidate, ensure_ascii=True, allow_nan=False, indent=2, sort_keys=True)
        + "\n",
        encoding="utf-8",
    )


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Normalize the synthetic USDA PLANTS Kansas distribution CSV profile."
        )
    )
    parser.add_argument("--taxa", type=Path, required=True)
    parser.add_argument("--counties", type=Path, required=True)
    parser.add_argument("--distribution", type=Path, required=True)
    parser.add_argument("--snapshot-date", required=True)
    parser.add_argument("--evidence-ref", required=True)
    parser.add_argument("--source-uri", default=SOURCE_URI)
    parser.add_argument("--out", type=Path, required=True)
    args = parser.parse_args(argv)

    try:
        candidate = build_snapshot(
            taxa_path=args.taxa,
            counties_path=args.counties,
            distribution_path=args.distribution,
            snapshot_date=args.snapshot_date,
            evidence_ref=args.evidence_ref,
            source_uri=args.source_uri,
        )
        write_snapshot(candidate, args.out)
    except NormalizationError as exc:
        print(f"DENY {exc.code}", file=sys.stderr)
        return 1
    except OSError:
        print("ERROR OUTPUT_UNWRITABLE", file=sys.stderr)
        return 2

    print(
        json.dumps(
            {
                "object_type": candidate["object_type"],
                "output": str(args.out),
                "snapshot_id": candidate["snapshot_id"],
                "spec_hash": candidate["spec_hash"],
                "status": "STRUCTURAL_CANDIDATE_WRITTEN",
            },
            sort_keys=True,
            separators=(",", ":"),
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
