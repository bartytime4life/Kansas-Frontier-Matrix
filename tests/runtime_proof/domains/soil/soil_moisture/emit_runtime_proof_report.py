"""Emit a machine-readable review report for the fixture-only soil runtime proof.

The report contains only expected outcomes and closed outward envelopes. It never
copies source candidates, readings, station identifiers, receipts, proofs,
catalogs, promotion objects, release objects, or publication state.
"""

from __future__ import annotations

import argparse
import copy
import json
from pathlib import Path
from typing import Any

from .runtime_mapper import PROFILE_VERSION, build_soil_moisture_runtime_response

REPORT_VERSION = "soil-moisture-runtime-proof-report-v1"


def _load_object(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError(f"fixture must decode to an object: {path}")
    return value


def build_runtime_proof_report(
    repository_root: Path,
    *,
    issued_at: str,
) -> dict[str, object]:
    """Evaluate the reviewed cases and return a deterministic QA report."""

    fixture_root = repository_root / "fixtures/domains/soil/soil_moisture"
    valid = _load_object(fixture_root / "valid/station_series.json")
    missing_support = copy.deepcopy(valid)
    missing_support["evidence_refs"] = []

    cases: tuple[tuple[str, object, str, str], ...] = (
        (
            "valid_fixture_not_released",
            valid,
            "ABSTAIN",
            "SOIL_MOISTURE_FIXTURE_NOT_RELEASED",
        ),
        (
            "duplicate_reading",
            _load_object(fixture_root / "invalid/duplicate_reading.json"),
            "DENY",
            "SOIL_MOISTURE_VALIDATION_DENIED",
        ),
        (
            "missing_evidence_support",
            missing_support,
            "ABSTAIN",
            "SOIL_MOISTURE_SUPPORT_INCOMPLETE",
        ),
        (
            "non_object_input",
            [],
            "ERROR",
            "SOIL_MOISTURE_INPUT_ERROR",
        ),
    )

    results: list[dict[str, object]] = []
    for case_id, candidate, expected_outcome, expected_reason_code in cases:
        actual = build_soil_moisture_runtime_response(candidate, issued_at=issued_at)
        results.append(
            {
                "case_id": case_id,
                "expected_outcome": expected_outcome,
                "expected_reason_code": expected_reason_code,
                "actual": actual,
                "matched": actual.get("outcome") == expected_outcome
                and actual.get("reason_code") == expected_reason_code,
            }
        )

    return {
        "report_version": REPORT_VERSION,
        "profile_version": PROFILE_VERSION,
        "issued_at": issued_at,
        "cases": results,
    }


def write_runtime_proof_report(
    repository_root: Path,
    output_path: Path,
    *,
    issued_at: str,
) -> dict[str, object]:
    report = build_runtime_proof_report(repository_root, issued_at=issued_at)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        json.dumps(report, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    return report


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Emit fixture-only soil-moisture runtime-proof responses."
    )
    parser.add_argument("--repo-root", type=Path, default=Path.cwd())
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--issued-at", required=True)
    args = parser.parse_args()

    report = write_runtime_proof_report(
        args.repo_root.resolve(),
        args.output,
        issued_at=args.issued_at,
    )
    return 0 if all(case["matched"] for case in report["cases"]) else 1


if __name__ == "__main__":
    raise SystemExit(main())
