#!/usr/bin/env python3
"""Exercise bounded publication-denial paths without assembling a release.

The dry run starts from the repository's synthetic, complete promotion packet,
applies five deterministic negative mutations, and reuses the bounded promotion
gate to prove that publication remains blocked. It writes no file and creates no
candidate, decision, receipt, proof, release, or publication authority.
"""

from __future__ import annotations

import argparse
import copy
import json
import sys
from pathlib import Path
from typing import Callable, Mapping, Sequence


REPO_ROOT = Path(__file__).resolve().parents[2]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators.promotion_gate.validate_promotion_gate import (  # noqa: E402
    FIXTURES_ROOT,
    result_payload,
    validate_document,
)


BASELINE = FIXTURES_ROOT / "valid/pass__complete_candidate.json"
SCOPE = "synthetic-publication-denial-only"
DIFFERENT_DIGEST = (
    "sha256:7b9f4fa978bd68aa93050a5e1a9d4c1a42bedf32f1a7fb946467e08d9c8f77e1"
)


def _evidence_missing(candidate: dict[str, object]) -> None:
    candidate["evidence_refs"] = []


def _policy_denied(candidate: dict[str, object]) -> None:
    context = candidate["policy_context"]
    assert isinstance(context, dict)
    context["evaluation"] = "DENY"


def _integrity_mismatch(candidate: dict[str, object]) -> None:
    receipt = candidate["run_receipt"]
    assert isinstance(receipt, dict)
    receipt["output_digests"] = [DIFFERENT_DIGEST]


def _rights_or_sensitivity_unclear(candidate: dict[str, object]) -> None:
    context = candidate["policy_context"]
    assert isinstance(context, dict)
    context["labels"] = ["restricted"]


def _review_absent(candidate: dict[str, object]) -> None:
    candidate["review"] = None


CaseMutation = Callable[[dict[str, object]], None]
CASES: tuple[tuple[str, str, tuple[str, ...], CaseMutation], ...] = (
    (
        "evidence_missing",
        "ABSTAIN",
        ("PG_F_EVIDENCE_REF_MISSING",),
        _evidence_missing,
    ),
    ("policy_denied", "DENY", ("PG_E_POLICY_DENY",), _policy_denied),
    (
        "integrity_mismatch",
        "DENY",
        ("PG_B_ARTIFACT_SET_MISMATCH",),
        _integrity_mismatch,
    ),
    (
        "rights_or_sensitivity_not_public_safe",
        "DENY",
        ("PG_E_PUBLIC_SAFE_LABEL_INVALID",),
        _rights_or_sensitivity_unclear,
    ),
    (
        "review_absent",
        "DENY",
        ("PG_G_REVIEW_INVALID",),
        _review_absent,
    ),
)


def _load_baseline() -> dict[str, object]:
    value = json.loads(BASELINE.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("promotion-gate baseline must be an object")
    return value


def build_report() -> dict[str, object]:
    """Return one deterministic, value-bounded publication-denial report."""

    baseline = _load_baseline()
    case_reports: list[dict[str, object]] = []
    suite_match = True
    for case_id, expected_status, expected_codes, mutate in CASES:
        candidate = copy.deepcopy(baseline)
        mutate(candidate)
        findings = validate_document(candidate)
        gate_report = result_payload("synthetic-publication-deny-case", findings)
        observed_codes = tuple(
            sorted(
                finding["code"]
                for finding in gate_report["findings"]
                if isinstance(finding, Mapping)
                and isinstance(finding.get("code"), str)
            )
        )
        observed_status = gate_report["status"]
        case_match = (
            observed_status == expected_status
            and observed_codes == expected_codes
            and gate_report["readiness"] == "BLOCKED"
        )
        suite_match = suite_match and case_match
        case_reports.append(
            {
                "case_id": case_id,
                "expected_status": expected_status,
                "publication_outcome": "DENIED",
                "reason_codes": list(observed_codes),
                "suite_match": case_match,
                "validation_report": {
                    "findings": gate_report["findings"],
                    "gates": gate_report["gates"],
                    "readiness": gate_report["readiness"],
                    "status": observed_status,
                },
            }
        )

    return {
        "authority_created": False,
        "case_count": len(case_reports),
        "cases": case_reports,
        "decision_created": False,
        "dry_run_status": "PASS" if suite_match else "ERROR",
        "network_used": False,
        "publication_created": False,
        "release_candidate_assembled": False,
        "scope": SCOPE,
        "tool": "publication-deny-dry-run",
        "version": "v1",
    }


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pretty", action="store_true")
    args = parser.parse_args(argv)
    report = build_report()
    print(
        json.dumps(
            report,
            indent=2 if args.pretty else None,
            separators=None if args.pretty else (",", ":"),
            sort_keys=True,
        )
    )
    return 0 if report["dry_run_status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
