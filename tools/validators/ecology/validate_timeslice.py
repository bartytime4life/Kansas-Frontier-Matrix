#!/usr/bin/env python3
"""
KFM Ecology time-slice QA validator.

Validates/generates QA metrics for governed vegetation / land-cover time slices.

Inputs:
  --qa-summary JSON with pixel counts
  --tileset-metadata JSON
  --out JSON output path

Expected qa-summary shape:
{
  "total_pixels": 1000,
  "masked_pixels": 120,
  "aerosol_flagged_pixels": 20,
  "valid_30m_pixels": 880,
  "total_30m_pixels": 1000
}
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any


PASS_MAX_MASKED_PCT = 15.0
REVIEW_MAX_MASKED_PCT = 30.0
MIN_30M_VALID_COVERAGE_PCT = 70.0
MIN_TILE_COMPLETENESS_PCT = 95.0


def load_json(path: Path) -> dict[str, Any]:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        raise SystemExit(f"ERROR: file not found: {path}")
    except json.JSONDecodeError as exc:
        raise SystemExit(f"ERROR: invalid JSON in {path}: {exc}")


def pct(numerator: float, denominator: float) -> float:
    if denominator <= 0:
        raise ValueError("percentage denominator must be > 0")
    return round((numerator / denominator) * 100.0, 4)


def decision_from_mask(masked_pct: float) -> str:
    if masked_pct <= PASS_MAX_MASKED_PCT:
        return "PASS"
    if masked_pct <= REVIEW_MAX_MASKED_PCT:
        return "REVIEW"
    return "REJECT"


def validate_timeslice(
    qa_summary: dict[str, Any],
    tileset_metadata: dict[str, Any],
) -> dict[str, Any]:
    total_pixels = float(qa_summary["total_pixels"])
    masked_pixels = float(qa_summary["masked_pixels"])
    aerosol_flagged_pixels = float(qa_summary.get("aerosol_flagged_pixels", 0))

    total_30m_pixels = float(qa_summary.get("total_30m_pixels", total_pixels))
    valid_30m_pixels = float(
        qa_summary.get("valid_30m_pixels", total_30m_pixels - masked_pixels)
    )

    expected_tile_count = float(tileset_metadata["expected_tile_count"])
    produced_tile_count = float(tileset_metadata["produced_tile_count"])

    masked_pct = pct(masked_pixels, total_pixels)
    aerosol_flag_pct = pct(aerosol_flagged_pixels, total_pixels)
    valid_coverage_pct = round(100.0 - masked_pct, 4)
    valid_30m_coverage_pct = pct(valid_30m_pixels, total_30m_pixels)

    tile_completeness_pct = (
        100.0 if expected_tile_count == 0 else pct(produced_tile_count, expected_tile_count)
    )

    decision = decision_from_mask(masked_pct)
    requires_fallback = valid_30m_coverage_pct < MIN_30M_VALID_COVERAGE_PCT
    production_incomplete = tile_completeness_pct < MIN_TILE_COMPLETENESS_PCT

    requires_steward = (
        decision == "REVIEW"
        or requires_fallback
        or production_incomplete
    )

    promotion_blocked = decision == "REJECT"

    flags: list[str] = []
    if decision == "REVIEW":
        flags.append("QA_REVIEW_REQUIRED")
    if decision == "REJECT":
        flags.append("QA_REJECTED")
    if requires_fallback:
        flags.append("VIIRS_500M_FALLBACK_REQUIRED")
    if production_incomplete:
        flags.append("PRODUCTION_INCOMPLETE")

    return {
        "object_type": "EcologyTimesliceQaDecision",
        "schema_version": "v1",
        "masked_pct": masked_pct,
        "aerosol_flag_pct": aerosol_flag_pct,
        "valid_coverage_pct": valid_coverage_pct,
        "valid_30m_coverage_pct": valid_30m_coverage_pct,
        "tile_completeness_pct": tile_completeness_pct,
        "decision": decision,
        "requires_fallback": requires_fallback,
        "requires_steward": requires_steward,
        "production_incomplete": production_incomplete,
        "promotion_blocked": promotion_blocked,
        "flags": flags,
        "thresholds": {
            "pass_max_masked_pct": PASS_MAX_MASKED_PCT,
            "review_max_masked_pct": REVIEW_MAX_MASKED_PCT,
            "min_30m_valid_coverage_pct": MIN_30M_VALID_COVERAGE_PCT,
            "min_tile_completeness_pct": MIN_TILE_COMPLETENESS_PCT,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--qa-summary", required=True, type=Path)
    parser.add_argument("--tileset-metadata", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()

    qa_summary = load_json(args.qa_summary)
    tileset_metadata = load_json(args.tileset_metadata)

    try:
        result = validate_timeslice(qa_summary, tileset_metadata)
    except KeyError as exc:
        print(f"ERROR: missing required field: {exc}", file=sys.stderr)
        return 1
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    if result["decision"] == "REJECT":
        print(json.dumps(result, indent=2, sort_keys=True))
        return 1

    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
