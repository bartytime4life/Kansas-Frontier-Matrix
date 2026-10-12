#!/usr/bin/env python3
"""Dry-run explainable BriefingSignal materiality and issue routing.

This command reads local validated signals, recomputes declared scores, priorities,
reason codes, and finite issue dispositions, then optionally binds an existing-issue
route to either the deterministic fixture IssueInventoryProjection or a separately
captured and validated GitHubIssueInventoryRead receipt. It never calls the network
or mutates GitHub, repository, lifecycle, evidence, policy, review, proof, release,
deployment, publication, or public state.
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
from tools.validators.governance.validate_issue_inventory_projection import (  # noqa: E402
    bind_issue_inventory,
    projection_summary,
    validate_projection,
)
from tools.validators.governance.validate_github_issue_inventory_read import (  # noqa: E402
    summary as live_summary,
    validate_record as validate_live_record,
)

SCOPE = "briefing-materiality-routing-dry-run"


def _inventory_input(
    fixture_path: Path | None,
    live_read_path: Path | None,
    *,
    as_of: str | None,
) -> tuple[Mapping[str, object] | None, list[dict[str, str]], dict[str, object] | None]:
    if fixture_path is not None and live_read_path is not None:
        return None, [{"code": "ISSUE_INVENTORY_INPUT_AMBIGUOUS", "path": "/"}], None

    if live_read_path is not None:
        if as_of is None:
            return None, [{"code": "LIVE_ISSUE_INVENTORY_AS_OF_REQUIRED", "path": "/"}], None
        result = validate_live_record(live_read_path, as_of=as_of)
        if not result.ok or result.payload is None:
            findings = [
                {
                    "code": f"LIVE_ISSUE_INVENTORY_{finding.code}",
                    "path": f"{live_read_path.as_posix()}::{finding.path}",
                }
                for finding in result.findings
            ]
            return None, findings, None
        return result.payload, [], live_summary(result.payload)

    if fixture_path is None:
        return None, [], None

    result = validate_projection(fixture_path)
    if not result.ok or result.payload is None:
        findings = [
            {
                "code": f"ISSUE_INVENTORY_{finding.code}",
                "path": f"{fixture_path.as_posix()}::{finding.path}",
            }
            for finding in result.findings
        ]
        return None, findings, None
    return result.payload, [], projection_summary(result.payload)


def evaluate(
    paths: Sequence[Path],
    issue_inventory_path: Path | None = None,
    live_issue_inventory_path: Path | None = None,
    *,
    as_of: str | None = None,
) -> dict[str, object]:
    projection, inventory_findings, inventory_summary = _inventory_input(
        issue_inventory_path,
        live_issue_inventory_path,
        as_of=as_of,
    )
    if inventory_findings:
        inventory_findings.sort(key=lambda item: (item["code"], item["path"]))
        return {
            "authority_created": False,
            "findings": inventory_findings,
            "issue_inventory": None,
            "repository_mutation_allowed": False,
            "scope": SCOPE,
            "signals": [],
            "status": "FAIL",
        }

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
        matched_issue_ids = (
            dedup.get("matched_issue_ids", [])
            if isinstance(dedup.get("matched_issue_ids"), list)
            else []
        )
        binding = bind_issue_inventory(
            declared_disposition=disposition,
            declared_reason_codes=routing_reasons,
            matched_issue_ids=matched_issue_ids,
            projection=projection,
        )
        if live_issue_inventory_path is not None and binding.get("inventory_status") == "BOUND_OPEN_TARGET":
            binding["inventory_status"] = "BOUND_OPEN_TARGET_LIVE_READ"
            reasons = list(binding.get("reason_codes", []))
            reasons.append("ISSUE_INVENTORY_LIVE_READ_FRESH")
            binding["reason_codes"] = reasons

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
                    **binding,
                    "idempotency_key": next_action.get("idempotency_key"),
                },
            }
        )

    findings.sort(key=lambda item: (item["code"], item["path"]))
    signals.sort(key=lambda item: str(item["signal_id"]))
    return {
        "authority_created": False,
        "findings": findings,
        "issue_inventory": inventory_summary,
        "repository_mutation_allowed": False,
        "scope": SCOPE,
        "signals": signals,
        "status": "FAIL" if findings else "PASS",
    }


def serialize_report(report: Mapping[str, object]) -> str:
    return json.dumps(report, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Dry-run explainable BriefingSignal materiality and issue routing "
            "with optional read-only issue-inventory binding."
        )
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--issue-inventory",
        type=Path,
        default=None,
        help="Validated local fixture IssueInventoryProjection. No live GitHub read is performed.",
    )
    group.add_argument(
        "--github-issue-inventory-read",
        type=Path,
        default=None,
        help="Previously captured GitHubIssueInventoryRead receipt. The router itself performs no network access.",
    )
    parser.add_argument(
        "--as-of",
        default=None,
        help="Explicit ISO-8601 time used to prove live-read freshness. Required with --github-issue-inventory-read.",
    )
    parser.add_argument("files", nargs="+", type=Path)
    args = parser.parse_args(argv)
    report = evaluate(
        args.files,
        args.issue_inventory,
        args.github_issue_inventory_read,
        as_of=args.as_of,
    )
    print(serialize_report(report))
    return 1 if report["status"] == "FAIL" else 0


if __name__ == "__main__":
    raise SystemExit(main())
