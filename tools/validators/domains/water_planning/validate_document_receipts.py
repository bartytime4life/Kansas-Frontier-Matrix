"""Deterministic, no-network receipt-fixture validator for water planning.

This validator checks a bounded synthetic fixture envelope. Positive digest
examples must be bound to embedded synthetic bytes and ``fixture:`` source
references. A fixture must never assign a digest to an official ``kwo:``
source reference; official document identities require separately captured
source bytes and repository-owned ingest receipts.

The validator does not fetch sources, retrieve documents, construct proofs,
make release decisions, activate connectors, or publish.
"""

from __future__ import annotations

import argparse
import hashlib
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
        "fixture_payload_utf8",
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
    *,
    fixture_only: bool,
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
    source_ref = receipt.get("source_ref")
    payload = receipt.get("fixture_payload_utf8")
    digest_shape_valid = False

    if title is not None:
        if digest is None:
            _add(
                findings,
                "DOCUMENT_DIGEST_UNPINNED",
                f"{path}.document_digest",
            )
        elif not isinstance(digest, str) or not DIGEST_PATTERN.match(digest):
            _add(
                findings,
                "DOCUMENT_DIGEST_FORMAT_INVALID",
                f"{path}.document_digest",
            )
        elif digest == ZERO_DIGEST:
            _add(
                findings,
                "DOCUMENT_DIGEST_IS_PLACEHOLDER",
                f"{path}.document_digest",
            )
        else:
            digest_shape_valid = True
    elif digest is not None:
        _add(
            findings,
            "DOCUMENT_DIGEST_WITHOUT_TITLE",
            f"{path}.document_digest",
        )

    if isinstance(source_ref, str) and source_ref.startswith("fixture:"):
        if not fixture_only:
            _add(findings, "FIXTURE_SOURCE_OUTSIDE_FIXTURE", f"{path}.source_ref")
        if not isinstance(payload, str):
            _add(findings, "FIXTURE_PAYLOAD_MISSING", f"{path}.fixture_payload_utf8")
        elif digest_shape_valid:
            expected = "sha256:" + hashlib.sha256(payload.encode("utf-8")).hexdigest()
            if digest != expected:
                _add(
                    findings,
                    "FIXTURE_DIGEST_MISMATCH",
                    f"{path}.document_digest",
                )
    elif payload is not None:
        _add(
            findings,
            "FIXTURE_PAYLOAD_SCOPE_INVALID",
            f"{path}.fixture_payload_utf8",
        )

    if (
        fixture_only
        and isinstance(source_ref, str)
        and source_ref.startswith("kwo:")
        and digest is not None
    ):
        _add(
            findings,
            "OFFICIAL_SOURCE_DIGEST_FORBIDDEN_IN_FIXTURE",
            f"{path}.document_digest",
        )


def validate_candidate(candidate: object) -> tuple[Finding, ...]:
    findings: list[Finding] = []

    if not isinstance(candidate, Mapping):
        return (Finding("DOCUMENT_NOT_OBJECT", "$"),)

    record_type = candidate.get("record_type")
    if record_type != RECORD_TYPE:
        _add(findings, "RECORD_TYPE_INVALID", "$.record_type")

    fixture_only = candidate.get("fixture_only")
    if fixture_only is not True:
        _add(findings, "FIXTURE_ONLY_REQUIRED", "$.fixture_only")

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
            _validate_receipt(
                receipt,
                i,
                findings,
                fixture_only=fixture_only is True,
            )

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
