#!/usr/bin/env python3
"""Dry-run explainable BriefingSignal materiality and issue routing.

This command reads local validated signals, recomputes declared scores, priorities,
reason codes, and finite issue dispositions, then emits a value-minimized report.
It never calls the network or mutates GitHub, repository, lifecycle, evidence,
policy, review, proof, release, deployment, publication, or public state.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Mapping, Sequence

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators.governance.validate_briefing_signal import (  # noqa: E402
    compute_materiality_priority,
    compute_materiality_reason_codes,
    compute_materiality_score,
    compute_routing_disposition,
    load_candidate,
)

SCOPE = "briefing-materiality-routing-dry-run"


def evaluate(paths: Sequence[Path]) -> dict[str, object]:
    findings: list[dict[str, str]] = []
    signals: list[dict[str, object]] = []
    for path in sorted(paths, key=lambda item: item.as_posix()):
        candidate, candidate_findings = load_candidate(path)
        if candidate_findings:
            findings.extend(
                {
                    "code": f"INPUT_{finding.code}",
                    "path": f"{path.as_posix()}::{finding.path}",
                }
                for finding in candidate_findings
            )
            continue
        if candidate is None:
            continue
        routing_result = compute_routing_disposition(candidate)
        materiality = candidate.get("materiality")
        routing = candidate.get("routing")
        dedup = candidate.get("deduplication")
        next_action = candidate.get("next_action")
        if not all(isinstance(item, Mapping) for item in (materiality, routing, dedup, next_action)):
            findings.append({"code": "INPUT_PROFILE_INCOMPLETE", "path": path.as_posix()})
            continue
        if routing_result is None:
            findings.append({"code": "INPUT_ROUTING_UNAVAILABLE", "path": path.as_posix()})
            continue
        disposition, routing_reasons = routing_result
        override = materiality.get("mandatory_override")
        signals.append(
            {
                "signal_id": candidate.get("signal_id"),
                "event_cluster_id": candidate.get("event_cluster_id"),
                "materiality": {
                    "raw_score": compute_materiality_score(candidate),
                    "priority": compute_materiality_priority(candidate),
                    "reason_codes": list(compute_materiality_reason_codes(candidate) or ()),
                    "mandatory_override": {
                        "applied": override.get("applied") if isinstance(override, Mapping) else None,
                        "reason_code": override.get("reason_code") if isinstance(override, Mapping) else None,
                    },
                },
                "routing": {
                    "disposition": disposition,
                    "reason_codes": list(routing_reasons),
                    "idempotency_key": next_action.get("idempotency_key"),
                    "target_issue_ids": sorted(dedup.get("matched_issue_ids", []))
                    if isinstance(dedup.get("matched_issue_ids"), list)
                    else [],
                },
            }
        )
    findings.sort(key=lambda item: (item["code"], item["path"]))
    signals.sort(key=lambda item: str(item["signal_id"]))
    return {
        "authority_created": False,
        "findings": findings,
        "repository_mutation_allowed": False,
        "scope": SCOPE,
        "signals": signals,
        "status": "FAIL" if findings else "PASS",
    }


def serialize_report(report: Mapping[str, object]) -> str:
    return json.dumps(report, sort_keys=True, separators=(",", ":"))


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Dry-run explainable BriefingSignal materiality and issue routing."
    )
    parser.add_argument("files", nargs="+", type=Path)
    args = parser.parse_args(argv)
    report = evaluate(args.files)
    print(serialize_report(report))
    return 1 if report["status"] == "FAIL" else 0


if __name__ == "__main__":
    raise SystemExit(main())
