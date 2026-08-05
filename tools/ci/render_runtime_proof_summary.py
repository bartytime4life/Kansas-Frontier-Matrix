#!/usr/bin/env python3
"""Render a deterministic reviewer summary from a runtime-proof QA report.

This helper is presentation only. It does not validate source candidates,
decide policy, resolve evidence, create proof, approve release, or publish.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


class SummaryRenderError(ValueError):
    """Safe failure for malformed or contradictory report input."""


def _require_string(value: object, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise SummaryRenderError(f"invalid field: {field}")
    return value


def _load_cases(report_path: Path) -> tuple[dict[str, Any], list[dict[str, Any]]]:
    try:
        report = json.loads(report_path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise SummaryRenderError("runtime-proof report is unreadable") from exc
    if not isinstance(report, dict):
        raise SummaryRenderError("runtime-proof report must be an object")
    _require_string(report.get("report_version"), "report_version")
    _require_string(report.get("profile_version"), "profile_version")
    _require_string(report.get("issued_at"), "issued_at")
    cases = report.get("cases")
    if not isinstance(cases, list) or not cases:
        raise SummaryRenderError("cases must be a nonempty array")
    if not all(isinstance(case, dict) for case in cases):
        raise SummaryRenderError("each case must be an object")
    return report, cases


def render_runtime_proof_summary(
    report_path: Path,
    *,
    output_path: Path | None = None,
    title: str = "Runtime Proof Summary — Soil Moisture",
) -> str:
    """Render expected-vs-actual outcomes and visibly surface mismatches."""

    report, cases = _load_cases(report_path)
    rows: list[tuple[str, str, str, bool, str, str, str, int]] = []
    for index, case in enumerate(cases):
        case_id = _require_string(case.get("case_id"), f"cases[{index}].case_id")
        expected = _require_string(
            case.get("expected_outcome"), f"cases[{index}].expected_outcome"
        )
        expected_reason = _require_string(
            case.get("expected_reason_code"),
            f"cases[{index}].expected_reason_code",
        )
        actual = case.get("actual")
        if not isinstance(actual, dict):
            raise SummaryRenderError(f"invalid field: cases[{index}].actual")
        actual_outcome = _require_string(
            actual.get("outcome"), f"cases[{index}].actual.outcome"
        )
        reason_code = _require_string(
            actual.get("reason_code"), f"cases[{index}].actual.reason_code"
        )
        policy_state = _require_string(
            actual.get("policy_state"), f"cases[{index}].actual.policy_state"
        )
        freshness = _require_string(
            actual.get("freshness"), f"cases[{index}].actual.freshness"
        )
        evidence_refs = actual.get("evidence_refs")
        if not isinstance(evidence_refs, list):
            raise SummaryRenderError(
                f"invalid field: cases[{index}].actual.evidence_refs"
            )
        matched = actual_outcome == expected and reason_code == expected_reason
        if case.get("matched") is not matched:
            raise SummaryRenderError(f"contradictory match flag: cases[{index}]")
        rows.append(
            (
                case_id,
                expected,
                actual_outcome,
                matched,
                reason_code,
                policy_state,
                freshness,
                len(evidence_refs),
            )
        )

    matched_count = sum(1 for row in rows if row[3])
    lines = [
        f"# {title}",
        "",
        f"- **Profile:** `{report['profile_version']}`",
        f"- **Issued at:** `{report['issued_at']}`",
        f"- **Cases:** `{len(rows)}`",
        f"- **Matched:** `{matched_count}`",
        f"- **Mismatched:** `{len(rows) - matched_count}`",
        "",
        "| Case | Expected | Actual | Match | Reason | Policy state | Freshness | Evidence refs |",
        "|---|---|---|:---:|---|---|---|---:|",
    ]
    for row in rows:
        case_id, expected, actual, matched, reason, policy, freshness, refs = row
        lines.append(
            f"| `{case_id}` | `{expected}` | `{actual}` | "
            f"{'✅' if matched else '❌'} | `{reason}` | `{policy}` | "
            f"`{freshness}` | `{refs}` |"
        )
    lines.extend(
        [
            "",
            "## Boundary",
            "",
            "This is a temporary QA summary over machine-readable outward envelopes. "
            "It is not evidence, policy, proof, review approval, promotion, release, "
            "publication, or public-use authority.",
            "",
        ]
    )
    markdown = "\n".join(lines)
    if output_path is not None:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(markdown, encoding="utf-8")
    return markdown


def main() -> int:
    parser = argparse.ArgumentParser(description="Render a runtime-proof review summary.")
    parser.add_argument("--report", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--title", default="Runtime Proof Summary — Soil Moisture")
    args = parser.parse_args()
    summary = render_runtime_proof_summary(
        args.report,
        output_path=args.output,
        title=args.title,
    )
    return 1 if "- **Mismatched:** `0`" not in summary else 0


if __name__ == "__main__":
    raise SystemExit(main())
