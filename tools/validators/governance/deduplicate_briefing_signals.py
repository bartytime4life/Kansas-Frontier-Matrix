#!/usr/bin/env python3
"""Dry-run deterministic BriefingSignal clustering and issue-routing checks.

The command reads validated signal files, groups them by declared event cluster,
and reports replay, collision, duplicate-classification, and issue-routing findings.
It performs no network access and writes no repository, issue, lifecycle, evidence,
release, deployment, or publication state.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators.governance.validate_briefing_signal import (  # noqa: E402
    Finding,
    load_candidate,
)

SCOPE = "briefing-signal-dedup-dry-run"


@dataclass(frozen=True)
class LoadedSignal:
    path: Path
    candidate: Mapping[str, Any]

    @property
    def signal_id(self) -> str:
        return str(self.candidate.get("signal_id", ""))

    @property
    def signal_digest(self) -> str:
        identity = self.candidate.get("identity")
        return str(identity.get("signal_digest", "")) if isinstance(identity, Mapping) else ""

    @property
    def event_cluster_id(self) -> str:
        return str(self.candidate.get("event_cluster_id", ""))

    @property
    def briefing_date(self) -> str:
        return str(self.candidate.get("briefing_date", ""))


def _finding(code: str, path: str) -> Finding:
    return Finding(code=code, path=path)


def _dedup_status(signal: LoadedSignal) -> str:
    value = signal.candidate.get("deduplication")
    return str(value.get("status", "")) if isinstance(value, Mapping) else ""


def _matched_signal_ids(signal: LoadedSignal) -> set[str]:
    value = signal.candidate.get("deduplication")
    if not isinstance(value, Mapping) or not isinstance(value.get("matched_signal_ids"), list):
        return set()
    return {str(item) for item in value["matched_signal_ids"]}


def _disposition(signal: LoadedSignal) -> str:
    value = signal.candidate.get("next_action")
    return str(value.get("disposition", "")) if isinstance(value, Mapping) else ""


def evaluate(paths: Sequence[Path]) -> dict[str, object]:
    findings: set[Finding] = set()
    loaded: list[LoadedSignal] = []

    for path in sorted(paths, key=lambda item: item.as_posix()):
        candidate, candidate_findings = load_candidate(path)
        for candidate_finding in candidate_findings:
            findings.add(
                _finding(
                    f"INPUT_{candidate_finding.code}",
                    f"{path.as_posix()}::{candidate_finding.path}",
                )
            )
        if candidate is not None and not candidate_findings:
            loaded.append(LoadedSignal(path=path, candidate=candidate))

    by_signal_id: dict[str, list[LoadedSignal]] = defaultdict(list)
    for signal in loaded:
        by_signal_id[signal.signal_id].append(signal)
    replay_counts: dict[str, int] = {}
    for signal_id, members in by_signal_id.items():
        digests = {member.signal_digest for member in members}
        if len(digests) > 1:
            findings.add(_finding("SIGNAL_ID_COLLISION", f"signal:{signal_id}"))
        replay_counts[signal_id] = len(members)

    by_cluster: dict[str, list[LoadedSignal]] = defaultdict(list)
    unique_signals: dict[tuple[str, str], LoadedSignal] = {}
    for signal in loaded:
        unique_signals.setdefault((signal.signal_id, signal.signal_digest), signal)
    for signal in unique_signals.values():
        by_cluster[signal.event_cluster_id].append(signal)

    clusters: list[dict[str, object]] = []
    operations: list[dict[str, object]] = []
    for event_cluster_id in sorted(by_cluster):
        members = sorted(
            by_cluster[event_cluster_id],
            key=lambda item: (item.briefing_date, item.signal_id, item.path.as_posix()),
        )
        primary = members[0]
        if len(members) > 1:
            for member in members[1:]:
                if _dedup_status(member) != "DUPLICATE":
                    findings.add(
                        _finding(
                            "DUPLICATE_CLASSIFICATION_REQUIRED",
                            f"signal:{member.signal_id}",
                        )
                    )
                if primary.signal_id not in _matched_signal_ids(member):
                    findings.add(
                        _finding(
                            "PRIMARY_SIGNAL_REFERENCE_REQUIRED",
                            f"signal:{member.signal_id}",
                        )
                    )
                if _disposition(member).startswith("OPEN_"):
                    findings.add(
                        _finding(
                            "DUPLICATE_ISSUE_CREATE_FORBIDDEN",
                            f"signal:{member.signal_id}",
                        )
                    )
        clusters.append(
            {
                "event_cluster_id": event_cluster_id,
                "primary_signal_id": primary.signal_id,
                "signal_ids": [member.signal_id for member in members],
                "distinct_signal_count": len(members),
                "replay_count": sum(replay_counts.get(member.signal_id, 1) for member in members),
            }
        )
        for member in members:
            next_action = member.candidate.get("next_action")
            dedup = member.candidate.get("deduplication")
            operations.append(
                {
                    "signal_id": member.signal_id,
                    "event_cluster_id": event_cluster_id,
                    "deduplication_status": _dedup_status(member),
                    "disposition": _disposition(member),
                    "idempotency_key": next_action.get("idempotency_key")
                    if isinstance(next_action, Mapping)
                    else None,
                    "target_issue_ids": sorted(dedup.get("matched_issue_ids", []))
                    if isinstance(dedup, Mapping)
                    and isinstance(dedup.get("matched_issue_ids"), list)
                    else [],
                }
            )

    return {
        "authority_created": False,
        "clusters": clusters,
        "findings": [
            {"code": finding.code, "path": finding.path}
            for finding in sorted(findings)
        ],
        "operations": sorted(operations, key=lambda item: str(item["signal_id"])),
        "repository_mutation_allowed": False,
        "scope": SCOPE,
        "status": "FAIL" if findings else "PASS",
    }


def serialize_report(report: Mapping[str, object]) -> str:
    return json.dumps(report, sort_keys=True, separators=(",", ":"))


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Dry-run deterministic BriefingSignal event clustering and issue routing."
    )
    parser.add_argument("files", nargs="+", type=Path)
    args = parser.parse_args(argv)
    report = evaluate(args.files)
    print(serialize_report(report))
    return 1 if report["status"] == "FAIL" else 0


if __name__ == "__main__":
    raise SystemExit(main())
