"""Deterministic, no-network document receipt validator for water-planning.

Enforces that every admitted KWO water-planning document record carries a
properly formed, non-placeholder SHA-256 digest.  A null or all-zero digest
signals an unpinned placeholder and is rejected.

This validator operates on a bounded fixture envelope.  It does not fetch
sources, retrieve documents, construct proofs, make release decisions, or
publish.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping, Sequence


MAX_INPUT_BYTES = 1_000_000
RECORD_TYPE = "water_planning_document_receipt_check"
DIGEST_PATTERN = re.compile(r"^sha256:[0-9a-f]{64}$")
ZERO_DIGEST = "sha256:" + "0" * 64

ALLOWED_TOP_LEVEL_KEYS = frozenset(
    {
        "record_type",
        "fixture_id",
        "fixture_only",
        "network_access",
        "document_receipts",
        "blocked_behaviors",
    }
)

BLOCKED_BEHAVIOR_RULES = {
    "connector": "CONNECTOR_BEHAVIOR_FORBIDDEN",
    "proof": "PROOF_BEHAVIOR_FORBIDDEN",
    "release": "RELEASE_BEHAVIOR_FORBIDDEN",
    "publication": "PUBLICATION_BEHAVIOR_FORBIDDEN",
    "source_activation": "SOURCE_ACTIVATION_BEHAVIOR_FORBIDDEN",
}

REQUIRED_RECEIPT_KEYS = frozenset(
    {
        "document_id",
        "document_title",
        "document_digest",
        "source_ref",
    }
)

ALLOWED_RECEIPT_KEYS = frozenset(
    {
        "document_id",
        "document_title",
        "document_version",
        "document_digest",
        "source_ref",
        "pinned_at",
        "correction_ref",
    }
)


@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str


def _add(findings: list[Finding], code: str, path: str) -> None:
    finding = Finding(code=code, path=path)
    if finding not in findings:
        findings.append(finding)


def _validate_receipt(
    receipt: object,
    index: int,
    findings: list[Finding],
) -> None:
    path = f"$.document_receipts[{index}]"
    if not isinstance(receipt, Mapping):
        _add(findings, "RECEIPT_NOT_OBJECT", path)
        return

    unexpected = set(receipt.keys()) - ALLOWED_RECEIPT_KEYS
    for key in sorted(unexpected):
        _add(findings, "UNEXPECTED_RECEIPT_FIELD", f"{path}.{key}")

    for key in sorted(REQUIRED_RECEIPT_KEYS):
        if key not in receipt:
            _add(findings, "RECEIPT_FIELD_MISSING", f"{path}.{key}")

    title = receipt.get("document_title")
    digest = receipt.get("document_digest")

    if title is not None:
        # A document with a title must have a pinned digest.
        if digest is None:
            _add(
                findings,
                "DOCUMENT_DIGEST_UNPINNED",
                f"{path}.document_digest",
            )
        elif not isinstance(digest, str):
            _add(
                findings,
                "DOCUMENT_DIGEST_FORMAT_INVALID",
                f"{path}.document_digest",
            )
        elif not DIGEST_PATTERN.match(digest):
            _add(
                findings,
                "DOCUMENT_DIGEST_FORMAT_INVALID",
                f"{path}.document_digest",
            )
        elif digest == ZERO_DIGEST:
            # All-zero digest is a placeholder, not a real pinned document.
            _add(
                findings,
                "DOCUMENT_DIGEST_IS_PLACEHOLDER",
                f"{path}.document_digest",
            )

    elif digest is not None:
        # Digest without title is inconsistent.
        _add(
            findings,
            "DOCUMENT_DIGEST_WITHOUT_TITLE",
            f"{path}.document_digest",
        )


def validate_candidate(candidate: object) -> tuple[Finding, ...]:
    findings: list[Finding] = []

    if not isinstance(candidate, Mapping):
        return (Finding("DOCUMENT_NOT_OBJECT", "$"),)

    record_type = candidate.get("record_type")
    if record_type != RECORD_TYPE:
        _add(
            findings,
            "RECORD_TYPE_INVALID",
            "$.record_type",
        )

    network_access = candidate.get("network_access")
    if network_access != "forbidden":
        _add(findings, "NETWORK_ACCESS_NOT_FORBIDDEN", "$.network_access")

    unexpected = set(candidate.keys()) - ALLOWED_TOP_LEVEL_KEYS
    for key in sorted(unexpected):
        _add(findings, "UNEXPECTED_FIELD", f"$.{key}")

    receipts = candidate.get("document_receipts")
    if not isinstance(receipts, list):
        _add(findings, "RECEIPTS_NOT_ARRAY", "$.document_receipts")
    elif not receipts:
        _add(findings, "RECEIPTS_ARRAY_EMPTY", "$.document_receipts")
    else:
        for i, receipt in enumerate(receipts):
            _validate_receipt(receipt, i, findings)

    blocked = candidate.get("blocked_behaviors")
    if isinstance(blocked, Mapping):
        for behavior, code in BLOCKED_BEHAVIOR_RULES.items():
            if blocked.get(behavior) is True:
                _add(findings, code, f"$.blocked_behaviors.{behavior}")

    return tuple(findings)


def validate_file(path: Path) -> tuple[Finding, ...]:
    if not path.exists():
        return (Finding("INPUT_NOT_FOUND", "$"),)
    raw = path.read_bytes()
    if len(raw) > MAX_INPUT_BYTES:
        return (Finding("INPUT_TOO_LARGE", "$"),)
    try:
        candidate = json.loads(raw)
    except json.JSONDecodeError:
        return (Finding("INPUT_NOT_JSON", "$"),)
    return validate_candidate(candidate)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate a water-planning document receipt fixture."
    )
    parser.add_argument("files", nargs="+", type=Path)
    args = parser.parse_args(argv)

    all_findings: list[dict[str, str]] = []
    for path in args.files:
        for finding in validate_file(path):
            all_findings.append({"code": finding.code, "path": finding.path})

    total = len(args.files)
    if all_findings:
        result = {
            "files": total,
            "outcome": "VALIDATOR_FAIL",
            "findings": all_findings,
        }
        print(json.dumps(result))
        return 1

    print(json.dumps({"files": total, "outcome": "VALIDATOR_PASS"}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
