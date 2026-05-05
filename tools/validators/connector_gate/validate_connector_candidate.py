#!/usr/bin/env python3
"""Fail-closed validator for connector admission candidates.

This script validates a connector candidate JSON document and exits non-zero
when the candidate is incomplete or unsafe to admit into downstream work lanes.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import sys
from pathlib import Path
from typing import Any

REQUIRED_FIELDS = (
    "candidate_id",
    "connector_id",
    "source_id",
    "source_role",
    "rights_status",
    "policy_label",
    "candidate_ref",
    "validation_plan",
    "handoff_targets",
)

ALLOWED_RIGHTS = {"approved", "public", "licensed"}
ALLOWED_POLICY_LABEL = {"public", "public-safe"}
ALLOWED_STATUS = {"candidate", "reviewed"}
ALLOWED_VALIDATION_PLAN = {"schema", "source_role", "rights", "crs", "time"}
REQUIRED_HANDOFF_KEYS = {"allow", "deny", "receipt"}


def fail(message: str) -> None:
    print(f"DENY: {message}", file=sys.stderr)
    raise SystemExit(1)


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as handle:
        loaded = json.load(handle)
    if not isinstance(loaded, dict):
        fail("candidate payload must be a JSON object")
    return loaded


def is_non_empty_text(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def validate_handoffs(handoffs: Any) -> None:
    if not isinstance(handoffs, dict):
        fail("handoff_targets must be an object")

    missing = sorted(REQUIRED_HANDOFF_KEYS - set(handoffs.keys()))
    if missing:
        fail(f"handoff_targets missing keys: {', '.join(missing)}")

    for key in REQUIRED_HANDOFF_KEYS:
        value = handoffs.get(key)
        if not is_non_empty_text(value):
            fail(f"handoff_targets.{key} must be a non-empty string")


def validate_validation_plan(plan: Any) -> None:
    if not isinstance(plan, list) or not plan:
        fail("validation_plan must be a non-empty list")

    invalid = [item for item in plan if item not in ALLOWED_VALIDATION_PLAN]
    if invalid:
        fail(
            "validation_plan contains unsupported values: "
            + ", ".join(sorted({str(item) for item in invalid}))
        )


def compute_spec_hash(path: Path) -> str:
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    return f"sha256:{digest}"


def validate_candidate(doc: dict[str, Any], *, candidate_path: Path, enforce_spec_hash: bool) -> None:
    for key in REQUIRED_FIELDS:
        if not is_non_empty_text(doc.get(key)) and key not in {"validation_plan", "handoff_targets"}:
            fail(f"missing required field: {key}")

    if doc["rights_status"] not in ALLOWED_RIGHTS:
        fail("rights_status must be one of approved/public/licensed")

    if doc["policy_label"] not in ALLOWED_POLICY_LABEL:
        fail("policy_label must be public or public-safe")

    status = doc.get("status")
    if status is not None and status not in ALLOWED_STATUS:
        fail("status must be candidate/reviewed when provided")

    validate_validation_plan(doc["validation_plan"])
    validate_handoffs(doc["handoff_targets"])

    spec_hash = doc.get("spec_hash")
    if spec_hash is not None and not is_non_empty_text(spec_hash):
        fail("spec_hash must be a non-empty string when provided")

    if enforce_spec_hash:
        if spec_hash is None:
            fail("spec_hash is required when --enforce-spec-hash is enabled")

        expected = compute_spec_hash(candidate_path)
        if spec_hash != expected:
            fail("spec_hash does not match candidate file content")


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate a connector admission candidate in fail-closed mode."
    )
    parser.add_argument("candidate", type=Path, help="Path to candidate JSON document")
    parser.add_argument(
        "--enforce-spec-hash",
        action="store_true",
        help="Require spec_hash to equal sha256 hash of the candidate file",
    )
    return parser.parse_args(argv)


def main() -> None:
    args = parse_args(sys.argv[1:])
    path = args.candidate

    if not path.exists():
        fail(f"missing candidate file: {path}")

    doc = load_json(path)
    validate_candidate(doc, candidate_path=path, enforce_spec_hash=args.enforce_spec_hash)
    print(f"ALLOW: valid connector candidate: {path}")


if __name__ == "__main__":
    main()
