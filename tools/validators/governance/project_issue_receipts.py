#!/usr/bin/env python3
"""Project no-network BriefingSignal routing reports into process-memory receipts."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import sys
from pathlib import Path
from typing import Mapping, Sequence

REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators.governance.validate_issue_inventory_projection import (  # noqa: E402
    compute_projection_digest,
    compute_projection_id,
    validate_projection as validate_inventory_projection,
)
from tools.validators.governance.validate_issue_projection_receipt import (  # noqa: E402
    canonical_json,
    compute_receipt_digest,
    compute_receipt_id,
    validate_payload,
)

MAX_JSON_BYTES = 2 * 1024 * 1024
OUTCOME_BY_OPERATION = {
    "UPDATE_EXISTING_ISSUE": "PROPOSED",
    "OPEN_SOURCE_DISCOVERY_ISSUE": "PROPOSED",
    "OPEN_OBJECT_MODEL_ISSUE": "PROPOSED",
    "OPEN_CORRECTIVE_ISSUE": "PROPOSED",
    "HOLD_FOR_DEPENDENCY": "HELD",
    "REJECT_UNSAFE": "REJECTED",
    "NO_ACTION": "NO_ACTION",
    "ERROR": "ERROR",
}

class ProjectionInputError(ValueError):
    """Raised when local router input cannot support a bounded receipt."""

class DuplicateKeyError(ValueError):
    pass

class NonFiniteNumberError(ValueError):
    pass

def _reject_duplicate_keys(pairs: list[tuple[str, object]]) -> dict[str, object]:
    value: dict[str, object] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError
        value[key] = item
    return value

def _reject_nonfinite(_value: str) -> object:
    raise NonFiniteNumberError

def _parse_finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed

def load_json_object(path: Path) -> dict[str, object]:
    try:
        if path.is_symlink() or not path.is_file():
            raise ProjectionInputError("INPUT_NOT_REGULAR_FILE")
        if path.stat().st_size > MAX_JSON_BYTES:
            raise ProjectionInputError("INPUT_TOO_LARGE")
        value = json.loads(
            path.read_text(encoding="utf-8"),
            object_pairs_hook=_reject_duplicate_keys,
            parse_constant=_reject_nonfinite,
            parse_float=_parse_finite_float,
        )
    except ProjectionInputError:
        raise
    except DuplicateKeyError as exc:
        raise ProjectionInputError("JSON_DUPLICATE_KEY") from exc
    except NonFiniteNumberError as exc:
        raise ProjectionInputError("JSON_NONFINITE_NUMBER") from exc
    except json.JSONDecodeError as exc:
        raise ProjectionInputError("JSON_INVALID") from exc
    except (OSError, UnicodeError, RecursionError, ValueError) as exc:
        raise ProjectionInputError("INPUT_UNREADABLE") from exc
    if not isinstance(value, dict):
        raise ProjectionInputError("JSON_ROOT_INVALID")
    return value

def compute_router_report_digest(report: Mapping[str, object]) -> str:
    return "sha256:" + hashlib.sha256(
        canonical_json(report).encode("utf-8")
    ).hexdigest()

def _issue_ids(value: object) -> list[int]:
    if not isinstance(value, list):
        raise ProjectionInputError("ROUTING_ISSUE_IDS_INVALID")
    ids: list[int] = []
    for item in value:
        if not isinstance(item, int) or isinstance(item, bool) or item < 1:
            raise ProjectionInputError("ROUTING_ISSUE_IDS_INVALID")
        ids.append(item)
    if ids != sorted(set(ids)):
        raise ProjectionInputError("ROUTING_ISSUE_IDS_NOT_CANONICAL")
    return ids

def _reason_codes(value: object) -> list[str]:
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise ProjectionInputError("ROUTING_REASON_CODES_INVALID")
    codes = sorted(set(value) | {"ISSUE_PROJECTION_DRY_RUN"})
    return codes

def _inventory_record(
    *,
    inventory_status: str,
    inventory_projection: Mapping[str, object] | None,
    repository: str,
) -> dict[str, object]:
    if inventory_status == "NOT_REQUIRED":
        return {
            "kind": "NOT_APPLICABLE",
            "reference": None,
            "digest": None,
            "status": "NOT_REQUIRED",
            "live_state_verified": False,
        }
    if inventory_status == "REQUIRED":
        if inventory_projection is not None:
            raise ProjectionInputError("INVENTORY_UNEXPECTED_FOR_REQUIRED_STATUS")
        return {
            "kind": "MISSING",
            "reference": None,
            "digest": None,
            "status": "REQUIRED",
            "live_state_verified": False,
        }
    if inventory_projection is None:
        raise ProjectionInputError("INVENTORY_PROJECTION_REQUIRED")
    projection_id = inventory_projection.get("projection_id")
    projection_digest = inventory_projection.get("projection_digest")
    if (
        inventory_projection.get("profile")
        != "kfm.briefing.issue-inventory.fixture.v1"
        or inventory_projection.get("repository") != repository
        or inventory_projection.get("live_state_verified") is not False
        or inventory_projection.get("authority_created") is not False
        or inventory_projection.get("repository_mutation_allowed") is not False
        or not isinstance(projection_id, str)
        or not isinstance(projection_digest, str)
        or projection_digest != compute_projection_digest(inventory_projection)
        or projection_id != compute_projection_id(inventory_projection)
    ):
        raise ProjectionInputError("INVENTORY_PROJECTION_IDENTITY_INVALID")
    return {
        "kind": "FIXTURE_PROJECTION",
        "reference": projection_id,
        "digest": projection_digest,
        "status": inventory_status,
        "live_state_verified": False,
    }

def build_issue_projection_receipts(
    report: Mapping[str, object],
    *,
    repository: str,
    default_branch: str,
    default_branch_head_sha: str,
    recorded_at: str,
    inventory_projection: Mapping[str, object] | None = None,
    schema_path: Path,
) -> list[dict[str, object]]:
    """Build deterministic dry-run receipts from one validated router report.

    The builder performs no network or repository mutation. It accepts only a
    PASS report whose authority and mutation flags are false.
    """

    if report.get("status") != "PASS":
        raise ProjectionInputError("ROUTER_REPORT_NOT_PASS")
    if report.get("findings") not in ([], None):
        raise ProjectionInputError("ROUTER_REPORT_HAS_FINDINGS")
    if report.get("authority_created") is not False:
        raise ProjectionInputError("ROUTER_AUTHORITY_BOUNDARY_INVALID")
    if report.get("repository_mutation_allowed") is not False:
        raise ProjectionInputError("ROUTER_MUTATION_BOUNDARY_INVALID")
    signals = report.get("signals")
    if not isinstance(signals, list):
        raise ProjectionInputError("ROUTER_SIGNALS_INVALID")

    routing_report_digest = compute_router_report_digest(report)
    receipts: list[dict[str, object]] = []
    signal_ids: list[str] = []
    for signal in signals:
        if not isinstance(signal, Mapping):
            raise ProjectionInputError("ROUTER_SIGNAL_INVALID")
        signal_id = signal.get("signal_id")
        event_cluster_id = signal.get("event_cluster_id")
        routing = signal.get("routing")
        if (
            not isinstance(signal_id, str)
            or not isinstance(event_cluster_id, str)
            or not isinstance(routing, Mapping)
        ):
            raise ProjectionInputError("ROUTER_SIGNAL_PROFILE_INCOMPLETE")
        signal_ids.append(signal_id)
        declared = routing.get("declared_disposition")
        projected = routing.get("disposition")
        idempotency_key = routing.get("idempotency_key")
        inventory_status = routing.get("inventory_status")
        if (
            not isinstance(declared, str)
            or not isinstance(projected, str)
            or projected not in OUTCOME_BY_OPERATION
            or not isinstance(idempotency_key, str)
            or not isinstance(inventory_status, str)
        ):
            raise ProjectionInputError("ROUTING_PROFILE_INCOMPLETE")

        receipt: dict[str, object] = {
            "profile": "kfm.briefing.issue-projection-receipt.v1",
            "schema_version": "1.0.0",
            "receipt_id": "kfm:issue-projection-receipt:" + ("0" * 24),
            "recorded_at": recorded_at,
            "repository": repository,
            "repository_context": {
                "default_branch": default_branch,
                "default_branch_head_sha": default_branch_head_sha,
            },
            "signal": {
                "signal_id": signal_id,
                "event_cluster_id": event_cluster_id,
                "routing_profile": "kfm-briefing-routing-v1",
                "routing_report_digest": routing_report_digest,
                "idempotency_key": idempotency_key,
            },
            "inventory": _inventory_record(
                inventory_status=inventory_status,
                inventory_projection=inventory_projection,
                repository=repository,
            ),
            "projection": {
                "declared_operation": declared,
                "projected_operation": projected,
                "outcome": OUTCOME_BY_OPERATION[projected],
                "declared_target_issue_ids": _issue_ids(
                    routing.get("declared_target_issue_ids")
                ),
                "target_issue_ids": _issue_ids(routing.get("target_issue_ids")),
                "closed_issue_ids": _issue_ids(routing.get("closed_issue_ids")),
                "missing_issue_ids": _issue_ids(routing.get("missing_issue_ids")),
                "reason_codes": _reason_codes(routing.get("reason_codes")),
            },
            "execution_mode": "DRY_RUN",
            "operation_attempted": False,
            "receipt_digest": "sha256:" + ("0" * 64),
            "authority_created": False,
            "evidence_created": False,
            "receipt_authoritative": False,
            "repository_mutation_allowed": False,
            "release_authorized": False,
            "publication_authorized": False,
            "public_use_allowed": False,
        }
        receipt["receipt_digest"] = compute_receipt_digest(receipt)
        receipt["receipt_id"] = compute_receipt_id(receipt)
        validation = validate_payload(receipt, schema_path=schema_path)
        if not validation.ok:
            codes = ",".join(finding.code for finding in validation.findings)
            raise ProjectionInputError(f"BUILT_RECEIPT_INVALID:{codes}")
        receipts.append(receipt)

    if signal_ids != sorted(set(signal_ids)):
        raise ProjectionInputError("ROUTER_SIGNALS_NOT_SORTED_UNIQUE")
    return receipts

def main(argv: Sequence[str] | None = None) -> int:
    default_schema = (
        REPO_ROOT
        / "schemas/contracts/v1/governance/issue_projection_receipt.schema.json"
    )
    parser = argparse.ArgumentParser(
        description="Project a local BriefingSignal router report into dry-run receipts."
    )
    parser.add_argument("--router-report", type=Path, required=True)
    parser.add_argument("--inventory-projection", type=Path, default=None)
    parser.add_argument("--repository", required=True)
    parser.add_argument("--default-branch", required=True)
    parser.add_argument("--default-branch-head-sha", required=True)
    parser.add_argument("--recorded-at", required=True)
    parser.add_argument("--schema", type=Path, default=default_schema)
    args = parser.parse_args(argv)
    try:
        report = load_json_object(args.router_report)
        inventory: Mapping[str, object] | None = None
        if args.inventory_projection is not None:
            inventory_result = validate_inventory_projection(
                args.inventory_projection
            )
            if not inventory_result.ok or inventory_result.payload is None:
                raise ProjectionInputError("INVENTORY_PROJECTION_INVALID")
            inventory = inventory_result.payload
        receipts = build_issue_projection_receipts(
            report,
            repository=args.repository,
            default_branch=args.default_branch,
            default_branch_head_sha=args.default_branch_head_sha,
            recorded_at=args.recorded_at,
            inventory_projection=inventory,
            schema_path=args.schema,
        )
    except ProjectionInputError as exc:
        print(
            canonical_json(
                {
                    "authority_created": False,
                    "code": str(exc).split(":", 1)[0],
                    "repository_mutation_allowed": False,
                    "status": "FAIL",
                }
            )
        )
        return 1
    print(canonical_json(receipts))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
