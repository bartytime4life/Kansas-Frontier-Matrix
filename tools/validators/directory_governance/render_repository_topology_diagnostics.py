#!/usr/bin/env python3
"""Render bounded failure identities for the repository-topology ratchet.

This is a diagnostic projection over validate_repository_topology.py. It does
not define topology rules, mutate the baseline, authorize migration, or expose
finding evidence members. Exit codes are preserved from the underlying ratchet.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
from typing import Mapping, Sequence

import validate_repository_topology as topology

DEFAULT_MAX_ITEMS = 20
MAX_ITEMS_LIMIT = 50
FAILURE_DISPOSITIONS = frozenset(
    {"ERROR_BASELINE_MISMATCH", "FAIL_INVARIANT", "FAIL_NEW_DRIFT"}
)

# Only stable, repository-authored messages are projected. Unknown exception
# text is never echoed because it can contain refs, paths, or other untrusted
# values. The stage fallback still makes hosted failures actionable without
# widening the validator's output surface.
ERROR_REASON_CODES = {
    "trusted baseline ref is invalid": "TRUSTED_REF_INVALID",
    "trusted baseline ref cannot be resolved": "TRUSTED_REF_UNRESOLVED",
    "trusted baseline ref did not resolve to a commit": "TRUSTED_REF_NOT_COMMIT",
    "trusted baseline is missing outside the governed bootstrap": "TRUSTED_BASELINE_MISSING",
    "baseline transition adds waiver fingerprints": "BASELINE_WAIVER_ADDED",
    "baseline transition does not strictly shrink evidence": "BASELINE_EVIDENCE_NOT_SHRUNK",
    "baseline transition mutates a waiver entry": "BASELINE_WAIVER_MUTATED",
    "baseline transition extends expiry": "BASELINE_EXPIRY_EXTENDED",
    "baseline transition mutates protected metadata": "BASELINE_METADATA_MUTATED",
    "baseline is missing or unsafe": "BASELINE_MISSING_OR_UNSAFE",
}
STAGE_REASON_CODES = {
    "scan": "SCAN_ERROR",
    "baseline": "BASELINE_LOAD_ERROR",
    "trusted-baseline": "TRUSTED_BASELINE_ERROR",
    "evaluate": "EVALUATE_ERROR",
}


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    parser.add_argument("--baseline", type=Path, default=topology.DEFAULT_BASELINE)
    parser.add_argument(
        "--trusted-baseline-ref",
        default=os.environ.get("KFM_TRUSTED_BASE_REF"),
        help="Trusted base commit/ref whose baseline may only shrink.",
    )
    parser.add_argument("--max-items", type=int, default=DEFAULT_MAX_ITEMS)
    return parser


def _bounded_max(value: int) -> int:
    if value < 1 or value > MAX_ITEMS_LIMIT:
        raise topology.TopologyError(
            f"max-items must be between 1 and {MAX_ITEMS_LIMIT}"
        )
    return value


def error_reason_code(exc: BaseException, *, stage: str) -> str:
    if isinstance(exc, topology.TopologyError):
        known = ERROR_REASON_CODES.get(str(exc))
        if known is not None:
            return known
    return STAGE_REASON_CODES.get(stage, "VALIDATOR_ERROR")


def render_diagnostics(
    report: Mapping[str, object],
    baseline: Mapping[str, Mapping[str, object]],
    *,
    max_items: int,
) -> tuple[str, ...]:
    limit = _bounded_max(max_items)
    rows: list[tuple[str, str, str, str]] = []

    raw_findings = report.get("findings", [])
    if not isinstance(raw_findings, list):
        raise topology.TopologyError("report findings are malformed")
    for raw in raw_findings:
        if not isinstance(raw, dict):
            raise topology.TopologyError("report finding is malformed")
        disposition = raw.get("disposition")
        if disposition not in FAILURE_DISPOSITIONS:
            continue
        rule_id = raw.get("rule_id")
        subject = raw.get("subject")
        fingerprint = raw.get("fingerprint")
        if not all(isinstance(value, str) and value for value in (rule_id, subject, fingerprint)):
            raise topology.TopologyError("report finding identity is malformed")
        rows.append((str(disposition), str(rule_id), str(subject), str(fingerprint)))

    raw_baseline = report.get("baseline", {})
    if not isinstance(raw_baseline, dict):
        raise topology.TopologyError("report baseline is malformed")
    stale = raw_baseline.get("stale_fingerprints", [])
    if not isinstance(stale, list) or not all(isinstance(value, str) for value in stale):
        raise topology.TopologyError("stale baseline identities are malformed")
    for fingerprint in stale:
        entry = baseline.get(fingerprint)
        if not isinstance(entry, Mapping):
            raise topology.TopologyError("stale baseline entry cannot be resolved")
        rule_id = entry.get("rule_id")
        subject = entry.get("subject")
        if not all(isinstance(value, str) and value for value in (rule_id, subject)):
            raise topology.TopologyError("stale baseline entry identity is malformed")
        rows.append(("STALE_BASELINE", str(rule_id), str(subject), fingerprint))

    ordered = sorted(set(rows))
    rendered = [
        f"{disposition} {rule_id} subject={subject} fingerprint={fingerprint}"
        for disposition, rule_id, subject, fingerprint in ordered[:limit]
    ]
    if len(ordered) > limit:
        rendered.append(f"... {len(ordered) - limit} additional failure identities omitted")
    return tuple(rendered)


def main(argv: Sequence[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    stage = "scan"
    try:
        max_items = _bounded_max(args.max_items)
        findings, tracked_count = topology.scan(args.repo_root)

        stage = "baseline"
        if args.baseline.is_symlink() or not args.baseline.is_file():
            raise topology.TopologyError("baseline is missing or unsafe")
        baseline_data, baseline = topology._load_baseline_bytes(
            args.baseline.read_bytes(), label="current"
        )

        if args.trusted_baseline_ref:
            stage = "trusted-baseline"
            topology.enforce_trusted_baseline(
                args.repo_root.resolve(),
                baseline_data,
                baseline,
                str(args.trusted_baseline_ref),
            )

        stage = "evaluate"
        code, report = topology.evaluate(
            findings,
            tracked_count,
            baseline,
            expires_on=str(baseline_data["expires_on"]),
        )
        counts = report["counts"]
        print(
            f"{report['outcome']}: {report['tracked_path_count']} tracked paths; "
            f"{counts['fail_invariant']} invariant; {counts['fail_new_drift']} new drift; "
            f"{counts['baselined_warning']} baselined warnings; "
            f"{len(report['baseline']['stale_fingerprints'])} stale baseline entries"
        )
        for line in render_diagnostics(report, baseline, max_items=max_items):
            print(line)
        return code
    except (OSError, UnicodeError, ValueError, topology.TopologyError) as exc:
        reason = error_reason_code(exc, stage=stage)
        print(f"ERROR_VALIDATOR: {type(exc).__name__} reason={reason}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
