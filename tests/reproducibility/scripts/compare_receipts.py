#!/usr/bin/env python3
"""Compare two receipt JSON files with case-defined required fields and allowed drift."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


DEFAULT_MUST_MATCH = [
    "object_type",
    "spec_hash",
    "decision",
    "artifact_digests",
    "policy_refs",
]


def _load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def _get_case_config(case_path: Path | None) -> tuple[list[str], set[str]]:
    if case_path is None:
        return DEFAULT_MUST_MATCH, set()

    case = _load_json(case_path)
    must_match = case.get("must_match_fields") or DEFAULT_MUST_MATCH
    allowed_drift = set(case.get("allowed_drift_fields") or [])
    return list(must_match), allowed_drift


def compare_receipts(
    receipt_a: dict[str, Any],
    receipt_b: dict[str, Any],
    must_match_fields: list[str],
    allowed_drift_fields: set[str],
) -> dict[str, Any]:
    diffs: list[dict[str, Any]] = []

    keys = sorted(set(receipt_a.keys()) | set(receipt_b.keys()))
    for key in keys:
        a_value = receipt_a.get(key)
        b_value = receipt_b.get(key)

        if a_value == b_value:
            continue

        status = "allowed_drift" if key in allowed_drift_fields else "mismatch"
        diffs.append(
            {
                "field": key,
                "status": status,
                "left": a_value,
                "right": b_value,
            }
        )

    required_mismatches = [
        diff
        for diff in diffs
        if diff["field"] in must_match_fields and diff["status"] != "allowed_drift"
    ]

    decision = "PASS" if not required_mismatches else "FAIL_CLOSED"

    return {
        "decision": decision,
        "required_fields": must_match_fields,
        "allowed_drift_fields": sorted(allowed_drift_fields),
        "first_differing_field": diffs[0]["field"] if diffs else None,
        "differences": diffs,
        "required_mismatch_count": len(required_mismatches),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("receipt_a", type=Path)
    parser.add_argument("receipt_b", type=Path)
    parser.add_argument("--case", dest="case_path", type=Path, default=None)
    parser.add_argument("--report-out", dest="report_out", type=Path, default=None)
    args = parser.parse_args()

    receipt_a = _load_json(args.receipt_a)
    receipt_b = _load_json(args.receipt_b)
    must_match_fields, allowed_drift_fields = _get_case_config(args.case_path)

    report = compare_receipts(receipt_a, receipt_b, must_match_fields, allowed_drift_fields)

    rendered = json.dumps(report, indent=2, sort_keys=True)
    print(rendered)

    if args.report_out:
        args.report_out.parent.mkdir(parents=True, exist_ok=True)
        args.report_out.write_text(rendered + "\n", encoding="utf-8")

    return 0 if report["decision"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
