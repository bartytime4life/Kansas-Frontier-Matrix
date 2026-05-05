#!/usr/bin/env python3
"""Validate ecology composite claim envelopes with fail-closed checks."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from typing import Any

EXIT_OK = 0
EXIT_INVALID = 1
EXIT_MISSING_INPUT = 2
EXIT_INTERNAL_ERROR = 5

ALLOWED_DECISIONS = {"cite", "abstain", "deny"}
ALLOWED_POLICY_LABELS = {"public", "public-safe"}
REQUIRED_FIELDS = (
    "claim_id",
    "claim_type",
    "spec_hash",
    "policy_label",
    "runtime_behavior",
)


class ValidationError(Exception):
    """Raised when a fail-closed validation gate fails."""


def _load_from_stdin() -> dict[str, Any]:
    try:
        raw = sys.stdin.read()
        doc = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValidationError(f"invalid JSON from stdin: {exc.msg}") from exc
    if not isinstance(doc, dict):
        raise ValidationError("claim envelope must be a JSON object")
    return doc


def _load_from_path(path: Path) -> dict[str, Any]:
    if not path.exists():
        raise FileNotFoundError(f"missing claim file: {path}")
    with path.open("r", encoding="utf-8") as handle:
        doc = json.load(handle)
    if not isinstance(doc, dict):
        raise ValidationError("claim envelope must be a JSON object")
    return doc


def _require_non_empty(doc: dict[str, Any], key: str) -> None:
    if doc.get(key) in (None, "", []):
        raise ValidationError(f"missing required field: {key}")


def validate(doc: dict[str, Any]) -> list[str]:
    warnings: list[str] = []

    for field in REQUIRED_FIELDS:
        _require_non_empty(doc, field)

    claim_id = doc["claim_id"]
    if not isinstance(claim_id, str) or not claim_id.startswith("kfm.claim.ecology."):
        raise ValidationError("claim_id must start with kfm.claim.ecology.")

    claim_type = doc["claim_type"]
    if claim_type != "composite_ecological_claim":
        raise ValidationError("claim_type must be composite_ecological_claim")

    if doc["policy_label"] not in ALLOWED_POLICY_LABELS:
        raise ValidationError("policy_label must be public or public-safe")

    domains = doc.get("domains")
    if not isinstance(domains, list) or len(domains) < 2:
        raise ValidationError("composite claims must include at least two domains")

    runtime = doc["runtime_behavior"]
    if not isinstance(runtime, dict):
        raise ValidationError("runtime_behavior must be an object")

    decision = runtime.get("decision")
    if decision not in ALLOWED_DECISIONS:
        raise ValidationError("runtime_behavior.decision must be cite, abstain, or deny")

    if runtime.get("evidence_drawer_required") is not True:
        raise ValidationError("runtime_behavior.evidence_drawer_required must be true")

    evidence = doc.get("evidence")
    if not isinstance(evidence, dict):
        raise ValidationError("evidence must be an object")

    evidence_status = evidence.get("status")
    evidence_items = evidence.get("items")
    if not isinstance(evidence_items, list):
        raise ValidationError("evidence.items must be an array")

    if decision == "cite":
        if evidence_status != "resolved":
            raise ValidationError("cite decisions require evidence.status=resolved")
        if not evidence_items:
            raise ValidationError("cite decisions require at least one evidence item")

    for idx, item in enumerate(evidence_items):
        if not isinstance(item, dict):
            raise ValidationError(f"evidence.items[{idx}] must be an object")
        if decision == "cite" and not item.get("evidence_ref"):
            raise ValidationError(f"evidence.items[{idx}].evidence_ref is required for cite")
        if item.get("layer_ref") and item.get("evidence_ref") == item.get("layer_ref"):
            raise ValidationError(
                f"evidence.items[{idx}] layer_ref cannot be used as evidence_ref"
            )

    uncertainty = doc.get("uncertainty")
    if not isinstance(uncertainty, dict) or uncertainty.get("status") in (None, ""):
        raise ValidationError("uncertainty.status is required")

    if decision in {"abstain", "deny"} and evidence_items:
        warnings.append("negative outcome includes evidence items; ensure contradictory context is visible")

    return warnings


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", nargs="?", help="Path to claim JSON. Reads stdin when omitted.")
    parser.add_argument("--report-json", action="store_true", help="Print machine-readable validation report.")
    args = parser.parse_args()

    try:
        doc = _load_from_path(Path(args.input)) if args.input else _load_from_stdin()
    except FileNotFoundError as exc:
        print(f"DENY: {exc}", file=sys.stderr)
        raise SystemExit(EXIT_MISSING_INPUT) from exc
    except json.JSONDecodeError as exc:
        print(f"DENY: invalid JSON: {exc.msg}", file=sys.stderr)
        raise SystemExit(EXIT_INVALID) from exc
    except ValidationError as exc:
        print(f"DENY: {exc}", file=sys.stderr)
        raise SystemExit(EXIT_INVALID) from exc

    try:
        warnings = validate(doc)
    except ValidationError as exc:
        if args.report_json:
            report = {
                "validator": "ecology_composite_claim",
                "result": "fail",
                "message": str(exc),
            }
            print(json.dumps(report, indent=2))
        else:
            print(f"DENY: {exc}", file=sys.stderr)
        raise SystemExit(EXIT_INVALID) from exc
    except Exception as exc:  # pragma: no cover - defensive fail-closed catch
        print(f"DENY: internal validator error: {exc}", file=sys.stderr)
        raise SystemExit(EXIT_INTERNAL_ERROR) from exc

    if args.report_json:
        report = {
            "validator": "ecology_composite_claim",
            "result": "pass",
            "claim_id": doc.get("claim_id"),
            "warnings": warnings,
        }
        print(json.dumps(report, indent=2))
    else:
        print("ALLOW: valid ecology composite claim")


if __name__ == "__main__":
    main()
