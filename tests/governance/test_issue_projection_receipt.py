#!/usr/bin/env python3
"""Fixture and projector tests for IssueProjectionReceipt."""
from __future__ import annotations

import copy
import hashlib
import io
import json
import socket
from contextlib import redirect_stdout
from pathlib import Path
from unittest.mock import patch

import pytest

from tools.validators.governance.project_issue_receipts import (
    ProjectionInputError,
    build_issue_projection_receipts,
    main as projector_main,
)
from tools.validators.governance.validate_issue_projection_receipt import (
    compute_receipt_digest,
    compute_receipt_id,
    validate_receipt,
)

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA = (
    REPO_ROOT
    / "schemas/contracts/v1/governance/issue_projection_receipt.schema.json"
)
FIXTURE_ROOT = (
    REPO_ROOT
    / "fixtures/contracts/v1/governance/issue_projection_receipt"
)
VALID = FIXTURE_ROOT / "valid"
INVALID = FIXTURE_ROOT / "invalid"
HEAD_SHA = "e2cbaf865f8e62dfec080db9d8933ee7590b7dc2"


def _canonical(value: object) -> str:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
        allow_nan=False,
    )


def _inventory(*, state: str = "OPEN") -> dict[str, object]:
    projection: dict[str, object] = {
        "profile": "kfm.briefing.issue-inventory.fixture.v1",
        "schema_version": "1.0.0",
        "projection_id": "kfm:issue-inventory:" + ("0" * 16),
        "repository": "bartytime4life/Kansas-Frontier-Matrix",
        "source_ref": "fixture:issue-inventory:projector-test",
        "generated_at": "2026-08-09T01:00:00Z",
        "issue_count": 1,
        "issues": [
            {
                "number": 1647,
                "state": state,
                "updated_at": "2026-08-09T00:00:00Z",
            }
        ],
        "projection_digest": "sha256:" + ("0" * 64),
        "live_state_verified": False,
        "authority_created": False,
        "repository_mutation_allowed": False,
    }
    payload = {
        key: projection[key]
        for key in sorted(projection)
        if key not in {"projection_id", "projection_digest"}
    }
    digest = hashlib.sha256(_canonical(payload).encode("utf-8")).hexdigest()
    projection["projection_digest"] = f"sha256:{digest}"
    projection["projection_id"] = f"kfm:issue-inventory:{digest[:16]}"
    return projection


def _signal_routing(
    *,
    declared: str,
    projected: str,
    inventory_status: str,
    declared_targets: list[int],
    targets: list[int],
    closed: list[int],
    missing: list[int],
    reasons: list[str],
    suffix: bytes,
) -> dict[str, object]:
    return {
        "signal_id": "kfm:briefing-signal:2026-07-30:b37a0154a1d02c3b6e4b3905",
        "event_cluster_id": (
            "kfm:event-cluster:governance_event:"
            "5c1ad27137565f1bc3fbc1f0"
        ),
        "materiality": {
            "raw_score": 20,
            "priority": "P2",
            "reason_codes": [],
            "mandatory_override": {"applied": False, "reason_code": None},
        },
        "routing": {
            "closed_issue_ids": closed,
            "declared_disposition": declared,
            "declared_target_issue_ids": declared_targets,
            "disposition": projected,
            "inventory_status": inventory_status,
            "missing_issue_ids": missing,
            "reason_codes": reasons,
            "target_issue_ids": targets,
            "idempotency_key": (
                "sha256:" + hashlib.sha256(suffix).hexdigest()
            ),
        },
    }


def _report(signal: dict[str, object]) -> dict[str, object]:
    return {
        "authority_created": False,
        "findings": [],
        "issue_inventory": None,
        "repository_mutation_allowed": False,
        "scope": "briefing-materiality-routing-dry-run",
        "signals": [signal],
        "status": "PASS",
    }


def _build(
    report: dict[str, object],
    *,
    inventory: dict[str, object] | None,
    recorded_at: str,
) -> list[dict[str, object]]:
    return build_issue_projection_receipts(
        report,
        repository="bartytime4life/Kansas-Frontier-Matrix",
        default_branch="main",
        default_branch_head_sha=HEAD_SHA,
        recorded_at=recorded_at,
        inventory_projection=inventory,
        schema_path=SCHEMA,
    )


def test_valid_fixtures_pass_and_identity_replays() -> None:
    paths = sorted(VALID.glob("*.json"))
    assert {path.name for path in paths} == {
        "held-closed-target.json",
        "no-action.json",
        "proposed-update.json",
    }
    for path in paths:
        result = validate_receipt(path, schema_path=SCHEMA)
        assert result.ok, (path, result.findings)
        assert result.payload is not None
        assert result.payload["receipt_digest"] == compute_receipt_digest(
            result.payload
        )
        assert result.payload["receipt_id"] == compute_receipt_id(result.payload)
        assert result.payload["operation_attempted"] is False
        assert result.payload["repository_mutation_allowed"] is False
        assert result.payload["receipt_authoritative"] is False


@pytest.mark.parametrize(
    ("name", "expected"),
    [
        ("digest-mismatch.json", "RECEIPT_DIGEST_MISMATCH"),
        ("inventory-reference-missing.json", "SCHEMA_INVALID"),
        ("missing-open-reason.json", "UPDATE_OPEN_TARGET_REASON_REQUIRED"),
        ("mutation-attempted.json", "SCHEMA_INVALID"),
        ("reason-order.json", "REASON_CODES_NOT_SORTED_UNIQUE"),
        ("target-mismatch.json", "TARGET_NOT_DECLARED"),
    ],
)
def test_invalid_fixtures_fail_closed(name: str, expected: str) -> None:
    result = validate_receipt(INVALID / name, schema_path=SCHEMA)
    assert not result.ok
    assert expected in {finding.code for finding in result.findings}


def test_builder_emits_bound_update_without_network() -> None:
    report = _report(
        _signal_routing(
            declared="UPDATE_EXISTING_ISSUE",
            projected="UPDATE_EXISTING_ISSUE",
            inventory_status="BOUND_OPEN_TARGET",
            declared_targets=[1647],
            targets=[1647],
            closed=[],
            missing=[],
            reasons=[
                "EXISTING_ISSUE_MATCH",
                "ISSUE_INVENTORY_OPEN_TARGET",
            ],
            suffix=b"update",
        )
    )
    inventory = _inventory()
    with (
        patch.object(
            socket.socket,
            "connect",
            side_effect=AssertionError("unexpected network"),
        ),
        patch.object(
            socket.socket,
            "connect_ex",
            side_effect=AssertionError("unexpected network"),
        ),
        patch.object(
            socket,
            "create_connection",
            side_effect=AssertionError("unexpected network"),
        ),
        patch.object(
            socket,
            "getaddrinfo",
            side_effect=AssertionError("unexpected network"),
        ),
    ):
        first = _build(
            report,
            inventory=inventory,
            recorded_at="2026-08-09T01:30:00Z",
        )
        second = _build(
            report,
            inventory=inventory,
            recorded_at="2026-08-09T01:30:00Z",
        )

    assert first == second
    assert len(first) == 1
    receipt = first[0]
    assert receipt["projection"]["outcome"] == "PROPOSED"
    assert receipt["projection"]["target_issue_ids"] == [1647]
    assert receipt["inventory"]["kind"] == "FIXTURE_PROJECTION"
    assert receipt["inventory"]["live_state_verified"] is False


def test_builder_preserves_closed_target_hold() -> None:
    report = _report(
        _signal_routing(
            declared="UPDATE_EXISTING_ISSUE",
            projected="HOLD_FOR_DEPENDENCY",
            inventory_status="TARGET_CLOSED",
            declared_targets=[1647],
            targets=[],
            closed=[1647],
            missing=[],
            reasons=[
                "EXISTING_ISSUE_MATCH",
                "ISSUE_INVENTORY_TARGET_CLOSED",
            ],
            suffix=b"hold",
        )
    )
    receipt = _build(
        report,
        inventory=_inventory(state="CLOSED"),
        recorded_at="2026-08-09T01:31:00Z",
    )[0]

    assert receipt["projection"]["outcome"] == "HELD"
    assert receipt["projection"]["target_issue_ids"] == []
    assert receipt["projection"]["closed_issue_ids"] == [1647]
    assert receipt["operation_attempted"] is False


def test_builder_preserves_no_action_without_inventory() -> None:
    report = _report(
        _signal_routing(
            declared="NO_ACTION",
            projected="NO_ACTION",
            inventory_status="NOT_REQUIRED",
            declared_targets=[],
            targets=[],
            closed=[],
            missing=[],
            reasons=["LOW_PRIORITY_NO_ACTION"],
            suffix=b"no-action",
        )
    )
    receipt = _build(
        report,
        inventory=None,
        recorded_at="2026-08-09T01:32:00Z",
    )[0]

    assert receipt["projection"]["outcome"] == "NO_ACTION"
    assert receipt["inventory"] == {
        "kind": "NOT_APPLICABLE",
        "reference": None,
        "digest": None,
        "status": "NOT_REQUIRED",
        "live_state_verified": False,
    }


def test_builder_rejects_router_authority_or_mutation_overclaim() -> None:
    report = _report(
        _signal_routing(
            declared="NO_ACTION",
            projected="NO_ACTION",
            inventory_status="NOT_REQUIRED",
            declared_targets=[],
            targets=[],
            closed=[],
            missing=[],
            reasons=["LOW_PRIORITY_NO_ACTION"],
            suffix=b"boundary",
        )
    )

    authority = copy.deepcopy(report)
    authority["authority_created"] = True
    with pytest.raises(
        ProjectionInputError,
        match="ROUTER_AUTHORITY_BOUNDARY_INVALID",
    ):
        _build(
            authority,
            inventory=None,
            recorded_at="2026-08-09T01:33:00Z",
        )

    mutation = copy.deepcopy(report)
    mutation["repository_mutation_allowed"] = True
    with pytest.raises(
        ProjectionInputError,
        match="ROUTER_MUTATION_BOUNDARY_INVALID",
    ):
        _build(
            mutation,
            inventory=None,
            recorded_at="2026-08-09T01:33:00Z",
        )


def test_cli_outputs_valid_receipt_array(tmp_path: Path) -> None:
    report = _report(
        _signal_routing(
            declared="UPDATE_EXISTING_ISSUE",
            projected="UPDATE_EXISTING_ISSUE",
            inventory_status="BOUND_OPEN_TARGET",
            declared_targets=[1647],
            targets=[1647],
            closed=[],
            missing=[],
            reasons=[
                "EXISTING_ISSUE_MATCH",
                "ISSUE_INVENTORY_OPEN_TARGET",
            ],
            suffix=b"cli",
        )
    )
    report_path = tmp_path / "router-report.json"
    inventory_path = tmp_path / "inventory.json"
    report_path.write_text(json.dumps(report), encoding="utf-8")
    inventory_path.write_text(json.dumps(_inventory()), encoding="utf-8")

    output = io.StringIO()
    with redirect_stdout(output):
        code = projector_main(
            [
                "--router-report",
                str(report_path),
                "--inventory-projection",
                str(inventory_path),
                "--repository",
                "bartytime4life/Kansas-Frontier-Matrix",
                "--default-branch",
                "main",
                "--default-branch-head-sha",
                HEAD_SHA,
                "--recorded-at",
                "2026-08-09T01:34:00Z",
                "--schema",
                str(SCHEMA),
            ]
        )

    assert code == 0
    payload = json.loads(output.getvalue())
    assert len(payload) == 1
    assert payload[0]["projection"]["projected_operation"] == (
        "UPDATE_EXISTING_ISSUE"
    )
    candidate = tmp_path / "candidate.json"
    candidate.write_text(json.dumps(payload[0]), encoding="utf-8")
    assert validate_receipt(candidate, schema_path=SCHEMA).ok
