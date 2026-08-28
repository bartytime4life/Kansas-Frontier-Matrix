#!/usr/bin/env python3
"""Assess the compatibility-first TemporalAuthorityEnvelope split.

The assessment is local, deterministic, read-only, and non-authoritative. It
requires one canonical common TemporalAuthorityEnvelope, one distinctly named
EvidenceTemporalPostureAssessment, and one exact-shape legacy evidence alias.
It retains HOLD while the compatibility alias and external persisted-record
inventory gate remain active.

Exit codes: 1 FAIL_INVARIANT, 2 ERROR_VALIDATOR, 3 HOLD_COMPATIBILITY.
"""
from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from pathlib import Path, PurePosixPath
from typing import Mapping, Sequence

MODULE_ROOT = Path(__file__).resolve().parent
if str(MODULE_ROOT) not in sys.path:
    sys.path.insert(0, str(MODULE_ROOT))

from temporal_authority_split_support import (  # noqa: E402
    REPORT_VERSION,
    EXIT_FAIL,
    EXIT_ERROR,
    EXIT_HOLD,
    ADR_0014,
    ADR_0029,
    COMMON_CONTRACT,
    COMMON_SCHEMA,
    COMMON_SCHEMA_ID,
    CANONICAL_CONTRACT,
    CANONICAL_SCHEMA,
    CANONICAL_SCHEMA_ID,
    CANONICAL_VALIDATOR,
    CANONICAL_TEST,
    CANONICAL_WORKFLOW,
    CANONICAL_FIXTURES,
    LEGACY_CONTRACT,
    LEGACY_SCHEMA,
    LEGACY_SCHEMA_ID,
    LEGACY_VALIDATOR,
    LEGACY_TEST,
    LEGACY_WORKFLOW,
    LEGACY_FIXTURES,
    ADVISORY_SCHEMA,
    PROGRAM_CONTRACT,
    PROGRAM_MODEL,
    PROGRAM_LEGACY_REFERENCE,
    LEGACY_PREFIX,
    _authority,
    _finding,
    _inventory,
    _report_hash,
    _verify_state,
)


def assess(root: Path, *, revision: str = "UNKNOWN") -> tuple[int, dict[str, object]]:
    root = root.resolve()
    if not root.is_dir():
        report = {
            "report_version": REPORT_VERSION,
            "outcome": "ERROR_VALIDATOR",
            "disposition": "HOLD",
            "revision": revision,
            "scan_complete": False,
            "findings": [_finding("KFM-TAE-ROOT-001", ".", "repository_root_missing")],
            "authority": _authority(),
        }
        report["report_sha256"] = _report_hash(report)
        return EXIT_ERROR, report

    findings: list[dict[str, str]] = []
    state = _verify_state(root, findings)
    references, scan_gaps, scanned_count = _inventory(root)
    unresolved = sorted(
        str(item["path"])
        for item in references
        if "unresolved" in item["classification"]
    )
    runtime_roots = {
        "apps", "packages", "runtime", "connectors",
        "pipelines", "pipeline_specs", "release",
    }
    runtime_unresolved = sorted(
        path for path in unresolved
        if PurePosixPath(path).parts and PurePosixPath(path).parts[0] in runtime_roots
    )
    if runtime_unresolved:
        findings.append(_finding(
            "KFM-TAE-REF-003",
            runtime_unresolved[0],
            "unclassified_runtime_reference_fails_closed",
        ))

    if scan_gaps:
        code, outcome, disposition = EXIT_ERROR, "ERROR_VALIDATOR", "HOLD"
        reasons = ["KFM-TAE-SCAN-INCOMPLETE"]
    elif findings:
        code, outcome, disposition = EXIT_FAIL, "FAIL_INVARIANT", "HOLD"
        reasons = ["KFM-TAE-SPLIT-SHAPE-DRIFT"]
    else:
        code, outcome, disposition = EXIT_HOLD, "HOLD_COMPATIBILITY", "SPLIT"
        reasons = [
            "KFM-TAE-SPLIT-ACTIVE",
            "KFM-TAE-LEGACY-COMPATIBILITY-ACTIVE",
            "KFM-TAE-EXTERNAL-INVENTORY-REQUIRED-BEFORE-REMOVAL",
            "KFM-TAE-TRACKED-TEXT-INVENTORY-COMPLETE",
        ]
        if unresolved:
            reasons.append("KFM-TAE-UNRESOLVED-REFERENCES-HELD")

    counts = Counter(
        role for item in references for role in item["classification"]
    )
    report: dict[str, object] = {
        "report_version": REPORT_VERSION,
        "outcome": outcome,
        "disposition": disposition,
        "reason_codes": sorted(reasons),
        "revision": revision,
        "scan_complete": not scan_gaps,
        "scanned_text_file_count": scanned_count,
        "split_state": state,
        "reference_counts": dict(sorted(counts.items())),
        "reference_file_count": len(references),
        "unresolved_reference_paths": unresolved,
        "runtime_unresolved_reference_paths": runtime_unresolved,
        "inventory_scope": {
            "tracked_repository_text": True,
            "runtime_observation": False,
            "database_records": False,
            "external_object_storage": False,
            "generated_ci_artifacts": False,
            "downstream_repositories": False,
        },
        "reference_inventory": references,
        "findings": sorted(
            findings,
            key=lambda item: (item["path"], item["code"], item["detail"]),
        ),
        "scan_gaps": scan_gaps,
        "authority": _authority(),
        "non_effects": [
            "does_not_accept_adr_0014",
            "does_not_translate_common_and_evidence_records",
            "does_not_remove_legacy_paths_or_identifiers",
            "does_not_prove_external_persisted_record_absence",
            "does_not_create_source_evidence_policy_review_release_or_publication_authority",
        ],
    }
    report["report_sha256"] = _report_hash(report)
    return code, report


def _render_text(report: Mapping[str, object]) -> str:
    return "\n".join([
        f"outcome={report.get('outcome')}",
        f"disposition={report.get('disposition')}",
        f"revision={report.get('revision')}",
        f"scan_complete={str(report.get('scan_complete')).lower()}",
        f"reference_file_count={report.get('reference_file_count', 0)}",
        f"unresolved_reference_count={len(report.get('unresolved_reference_paths', []))}",
        f"finding_count={len(report.get('findings', []))}",
        f"scan_gap_count={len(report.get('scan_gaps', []))}",
        f"report_sha256={report.get('report_sha256')}",
        "authority_created=false",
        "legacy_removal_authorized=false",
        "",
    ])


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--root",
        type=Path,
        default=Path(__file__).resolve().parents[3],
    )
    parser.add_argument("--revision", default="UNKNOWN")
    parser.add_argument("--format", choices=("json", "text"), default="text")
    args = parser.parse_args(argv)
    try:
        code, report = assess(args.root, revision=args.revision)
    except (OSError, UnicodeError, ValueError, RecursionError) as exc:
        report = {
            "report_version": REPORT_VERSION,
            "outcome": "ERROR_VALIDATOR",
            "disposition": "HOLD",
            "revision": args.revision,
            "scan_complete": False,
            "findings": [_finding("KFM-TAE-UNEXPECTED-001", ".", type(exc).__name__)],
            "authority": _authority(),
        }
        report["report_sha256"] = _report_hash(report)
        code = EXIT_ERROR
    if args.format == "json":
        print(json.dumps(report, ensure_ascii=False, sort_keys=True, indent=2))
    else:
        sys.stdout.write(_render_text(report))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
