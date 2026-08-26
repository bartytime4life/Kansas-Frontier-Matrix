from __future__ import annotations

import json
import subprocess
from pathlib import Path

import pytest

from tools.validators.validate_evidence_drawer_schema_convergence import (
    ConvergenceError,
    audit,
    validate_baseline_transition,
)


DRAFT = "https://json-schema.org/draft/2020-12/schema"


def _write_schema(
    root: Path,
    relative: str,
    schema_id: str,
    *,
    properties: dict | None = None,
    additional_properties: bool = True,
    contract_doc: str | None = None,
) -> None:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(
            {
                "$schema": DRAFT,
                "$id": schema_id,
                "type": "object",
                "properties": properties or {},
                "additionalProperties": additional_properties,
                "x-kfm": {
                    "status": "PROPOSED",
                    "contract_doc": contract_doc,
                },
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


def _write_required_anchors(root: Path) -> None:
    _write_schema(
        root,
        "schemas/contracts/v1/evidence/evidence_drawer_payload.schema.json",
        "kfm://evidence-drawer/evidence",
    )
    _write_schema(
        root,
        "schemas/contracts/v1/runtime/evidence_drawer_payload.schema.json",
        "kfm://evidence-drawer/runtime",
    )
    _write_schema(
        root,
        "schemas/contracts/v1/ui/evidence_drawer_payload.schema.json",
        "kfm://evidence-drawer/ui",
        properties={"outcome": {"type": "string"}},
        additional_properties=False,
        contract_doc="contracts/ui/evidence_drawer_payload.md",
    )


def _write_reference_schema(
    root: Path,
    relative: str,
    schema_id: str,
    ref: str,
) -> None:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        json.dumps(
            {
                "$schema": DRAFT,
                "$id": schema_id,
                "$ref": ref,
                "x-kfm": {
                    "status": "PROPOSED",
                    "contract_doc": "contracts/ui/evidence_drawer_payload.md",
                },
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )


def _write_baseline(root: Path, result: dict) -> Path:
    path = root / "evidence_drawer_schema_family_baseline.json"
    path.write_text(
        json.dumps(
            {
                "schema_version": "kfm.evidence-drawer-schema-family-baseline.v1",
                "authority": "implementation_inventory_only",
                "generated_from_ref": (
                    "main@0000000000000000000000000000000000000000"
                ),
                "closure_ref": (
                    "https://github.com/bartytime4life/"
                    "Kansas-Frontier-Matrix/issues/3368"
                ),
                "entries": [
                    {
                        "path": entry["path"],
                        "shape_class": entry["shape_class"],
                        "document_fingerprint": entry["document_fingerprint"],
                    }
                    for entry in result["schemas"]
                ],
                "non_effects": [
                    "does_not_select_canonical_authority",
                    "does_not_accept_adr_0037",
                    "does_not_waive_new_removed_or_changed_family_members",
                    (
                        "does_not_authorize_migration_review_release_deployment_"
                        "promotion_or_publication"
                    ),
                ],
            },
            indent=2,
            sort_keys=True,
        )
        + "\n",
        encoding="utf-8",
    )
    return path


def test_audit_classifies_anchors_and_domain_profiles(tmp_path: Path) -> None:
    _write_required_anchors(tmp_path)
    _write_schema(
        tmp_path,
        "schemas/contracts/v1/domains/hydrology/evidence_drawer_payload.schema.json",
        "kfm://evidence-drawer/hydrology",
        properties={"id": {"type": "string"}},
        contract_doc="contracts/domains/hydrology/evidence_drawer_payload.md",
    )

    result = audit(tmp_path)

    assert result["outcome"] == "PASS"
    assert result["placement_state"] == "NEEDS_REVIEW"
    assert result["schema_count"] == 4
    assert result["shape_state"] == "MULTIPLE_LOCAL_SHAPE_WRITERS"
    assert result["classification_counts"] == {
        "closed-ui-profile-candidate": 1,
        "domain-local-shape-scaffold": 1,
        "permissive-empty-scaffold": 2,
    }
    assert result["baseline_state"] == "NOT_EVALUATED"
    roles = {entry["path"]: entry["role"] for entry in result["schemas"]}
    assert roles["schemas/contracts/v1/evidence/evidence_drawer_payload.schema.json"] == (
        "evidence-family-placement-candidate"
    )
    assert roles["schemas/contracts/v1/ui/evidence_drawer_payload.schema.json"] == (
        "ui-public-safe-profile"
    )
    assert roles[
        "schemas/contracts/v1/domains/hydrology/evidence_drawer_payload.schema.json"
    ] == "domain-profile-or-scaffold"


def test_audit_identifies_reference_only_profile_without_selecting_authority(
    tmp_path: Path,
) -> None:
    _write_required_anchors(tmp_path)
    relative = "schemas/contracts/v1/domains/atmosphere/evidence_drawer_payload.schema.json"
    _write_reference_schema(
        tmp_path,
        relative,
        "kfm://evidence-drawer/atmosphere",
        "../../ui/evidence_drawer_payload.schema.json",
    )

    result = audit(tmp_path)

    entry = next(item for item in result["schemas"] if item["path"] == relative)
    assert entry["shape_class"] == "reference-only-profile"
    assert entry["reference_target"] == "../../ui/evidence_drawer_payload.schema.json"
    assert result["placement_state"] == "NEEDS_REVIEW"
    assert "does not select a canonical schema" in result["boundary"]


def test_audit_denies_duplicate_schema_ids(tmp_path: Path) -> None:
    _write_required_anchors(tmp_path)
    duplicate = "kfm://evidence-drawer/ui"
    _write_schema(
        tmp_path,
        "schemas/contracts/v1/domains/soil/evidence_drawer_payload.schema.json",
        duplicate,
    )

    result = audit(tmp_path)

    assert result["outcome"] == "ERROR"
    assert "DUPLICATE_SCHEMA_ID" in result["reason_codes"]
    assert result["duplicate_ids"] == [duplicate]


def test_audit_denies_missing_anchor(tmp_path: Path) -> None:
    _write_schema(
        tmp_path,
        "schemas/contracts/v1/evidence/evidence_drawer_payload.schema.json",
        "kfm://evidence-drawer/evidence",
    )

    result = audit(tmp_path)

    assert result["outcome"] == "ERROR"
    assert "MISSING_PLACEMENT_ANCHOR" in result["reason_codes"]
    assert result["missing_anchors"] == ["runtime", "ui"]


def test_audit_denies_wrong_json_schema_draft(tmp_path: Path) -> None:
    _write_required_anchors(tmp_path)
    path = tmp_path / "schemas/contracts/v1/runtime/evidence_drawer_payload.schema.json"
    payload = json.loads(path.read_text(encoding="utf-8"))
    payload["$schema"] = "http://json-schema.org/draft-07/schema#"
    path.write_text(json.dumps(payload) + "\n", encoding="utf-8")

    result = audit(tmp_path)

    assert result["outcome"] == "ERROR"
    assert "UNEXPECTED_JSON_SCHEMA_DRAFT" in result["reason_codes"]


def test_audit_denies_malformed_schema_json(tmp_path: Path) -> None:
    _write_required_anchors(tmp_path)
    path = tmp_path / "schemas/contracts/v1/domains/fauna/evidence_drawer_payload.schema.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("{not-json}\n", encoding="utf-8")

    result = audit(tmp_path)

    assert result["outcome"] == "ERROR"
    assert "SCHEMA_PARSE_ERROR" in result["reason_codes"]
    assert result["parse_errors"] == [
        "schemas/contracts/v1/domains/fauna/evidence_drawer_payload.schema.json"
    ]


def test_family_baseline_accepts_exact_inventory(tmp_path: Path) -> None:
    _write_required_anchors(tmp_path)
    snapshot = audit(tmp_path)
    baseline = _write_baseline(tmp_path, snapshot)

    result = audit(tmp_path, baseline_path=baseline)

    assert result["outcome"] == "PASS"
    assert result["baseline_state"] == "PASS"
    assert result["baseline_entry_count"] == 3
    assert result["unbaselined_schema_paths"] == []
    assert result["stale_baseline_paths"] == []
    assert result["changed_baseline_paths"] == []


def test_family_baseline_denies_new_member(tmp_path: Path) -> None:
    _write_required_anchors(tmp_path)
    baseline = _write_baseline(tmp_path, audit(tmp_path))
    relative = "schemas/contracts/v1/domains/soil/evidence_drawer_payload.schema.json"
    _write_reference_schema(
        tmp_path,
        relative,
        "kfm://evidence-drawer/soil",
        "../../ui/evidence_drawer_payload.schema.json",
    )

    result = audit(tmp_path, baseline_path=baseline)

    assert result["outcome"] == "ERROR"
    assert "UNBASELINED_SCHEMA_FAMILY_MEMBER" in result["reason_codes"]
    assert result["unbaselined_schema_paths"] == [relative]


def test_family_baseline_denies_changed_member(tmp_path: Path) -> None:
    _write_required_anchors(tmp_path)
    baseline = _write_baseline(tmp_path, audit(tmp_path))
    relative = "schemas/contracts/v1/ui/evidence_drawer_payload.schema.json"
    path = tmp_path / relative
    payload = json.loads(path.read_text(encoding="utf-8"))
    payload["properties"]["id"] = {"type": "string"}
    path.write_text(json.dumps(payload) + "\n", encoding="utf-8")

    result = audit(tmp_path, baseline_path=baseline)

    assert result["outcome"] == "ERROR"
    assert "SCHEMA_FAMILY_FINGERPRINT_CHANGED" in result["reason_codes"]
    assert result["changed_baseline_paths"] == [relative]


def test_family_baseline_denies_stale_member(tmp_path: Path) -> None:
    _write_required_anchors(tmp_path)
    baseline = _write_baseline(tmp_path, audit(tmp_path))
    relative = "schemas/contracts/v1/runtime/evidence_drawer_payload.schema.json"
    (tmp_path / relative).unlink()

    result = audit(tmp_path, baseline_path=baseline)

    assert result["outcome"] == "ERROR"
    assert "STALE_SCHEMA_FAMILY_BASELINE" in result["reason_codes"]
    assert result["stale_baseline_paths"] == [relative]


def test_family_baseline_denies_authority_metadata_change(tmp_path: Path) -> None:
    _write_required_anchors(tmp_path)
    baseline = _write_baseline(tmp_path, audit(tmp_path))
    payload = json.loads(baseline.read_text(encoding="utf-8"))
    payload["authority"] = "canonical_schema_authority"
    baseline.write_text(json.dumps(payload) + "\n", encoding="utf-8")

    result = audit(tmp_path, baseline_path=baseline)

    assert result["outcome"] == "ERROR"
    assert result["baseline_state"] == "ERROR"
    assert result["baseline_errors"] == ["baseline authority is invalid"]
    assert "SCHEMA_FAMILY_BASELINE_ERROR" in result["reason_codes"]


def test_trusted_family_baseline_accepts_exact_inventory(tmp_path: Path) -> None:
    _write_required_anchors(tmp_path)
    baseline = _write_baseline(tmp_path, audit(tmp_path))
    trusted_data = json.loads(baseline.read_text(encoding="utf-8"))
    trusted_entries = {entry["path"]: entry for entry in trusted_data["entries"]}

    validate_baseline_transition(
        trusted_data,
        trusted_entries,
        trusted_data,
        trusted_entries,
    )


def test_trusted_family_baseline_denies_membership_change(tmp_path: Path) -> None:
    _write_required_anchors(tmp_path)
    baseline = _write_baseline(tmp_path, audit(tmp_path))
    trusted_data = json.loads(baseline.read_text(encoding="utf-8"))
    trusted_entries = {entry["path"]: entry for entry in trusted_data["entries"]}
    added = dict(trusted_entries)
    added["schemas/contracts/v1/domains/soil/evidence_drawer_payload.schema.json"] = {
        "path": "schemas/contracts/v1/domains/soil/evidence_drawer_payload.schema.json",
        "shape_class": "reference-only-profile",
        "document_fingerprint": "sha256:" + ("a" * 64),
    }

    with pytest.raises(ConvergenceError, match="adds schema members"):
        validate_baseline_transition(
            trusted_data,
            added,
            trusted_data,
            trusted_entries,
        )

    removed = dict(trusted_entries)
    removed.pop(next(iter(removed)))
    with pytest.raises(ConvergenceError, match="removes schema members"):
        validate_baseline_transition(
            trusted_data,
            removed,
            trusted_data,
            trusted_entries,
        )


def test_trusted_family_baseline_denies_member_rewrite(tmp_path: Path) -> None:
    _write_required_anchors(tmp_path)
    baseline = _write_baseline(tmp_path, audit(tmp_path))
    trusted_data = json.loads(baseline.read_text(encoding="utf-8"))
    trusted_entries = {entry["path"]: entry for entry in trusted_data["entries"]}
    changed = {path: dict(entry) for path, entry in trusted_entries.items()}
    first_path = next(iter(changed))
    changed[first_path]["document_fingerprint"] = "sha256:" + ("b" * 64)

    with pytest.raises(ConvergenceError, match="changes schema members"):
        validate_baseline_transition(
            trusted_data,
            changed,
            trusted_data,
            trusted_entries,
        )


def test_trusted_family_baseline_denies_protected_metadata_change(
    tmp_path: Path,
) -> None:
    _write_required_anchors(tmp_path)
    baseline = _write_baseline(tmp_path, audit(tmp_path))
    trusted_data = json.loads(baseline.read_text(encoding="utf-8"))
    trusted_entries = {entry["path"]: entry for entry in trusted_data["entries"]}
    changed_data = dict(trusted_data)
    changed_data["closure_ref"] = (
        "https://github.com/bartytime4life/Kansas-Frontier-Matrix/issues/1"
    )

    with pytest.raises(ConvergenceError, match="changes protected metadata"):
        validate_baseline_transition(
            changed_data,
            trusted_entries,
            trusted_data,
            trusted_entries,
        )


def test_trusted_bootstrap_binds_exact_schema_inventory(tmp_path: Path) -> None:
    _write_required_anchors(tmp_path)
    subprocess.run(["git", "init", "-q", str(tmp_path)], check=True)
    subprocess.run(
        ["git", "-C", str(tmp_path), "config", "user.name", "KFM Test"],
        check=True,
    )
    subprocess.run(
        ["git", "-C", str(tmp_path), "config", "user.email", "kfm@example.invalid"],
        check=True,
    )
    subprocess.run(["git", "-C", str(tmp_path), "add", "schemas"], check=True)
    subprocess.run(
        ["git", "-C", str(tmp_path), "commit", "-q", "-m", "trusted base"],
        check=True,
    )
    trusted_sha = subprocess.run(
        ["git", "-C", str(tmp_path), "rev-parse", "HEAD"],
        check=True,
        capture_output=True,
        text=True,
    ).stdout.strip()

    exact_baseline = _write_baseline(tmp_path, audit(tmp_path))
    exact_payload = json.loads(exact_baseline.read_text(encoding="utf-8"))
    exact_payload["generated_from_ref"] = f"main@{trusted_sha}"
    exact_baseline.write_text(
        json.dumps(exact_payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    exact_result = audit(
        tmp_path,
        baseline_path=exact_baseline,
        trusted_baseline_ref=trusted_sha,
    )
    assert exact_result["outcome"] == "PASS"
    assert exact_result["trusted_baseline_state"] == "PASS"

    ui_schema = (
        tmp_path / "schemas/contracts/v1/ui/evidence_drawer_payload.schema.json"
    )
    changed_schema = json.loads(ui_schema.read_text(encoding="utf-8"))
    changed_schema["properties"]["id"] = {"type": "string"}
    ui_schema.write_text(json.dumps(changed_schema) + "\n", encoding="utf-8")
    changed_baseline = _write_baseline(tmp_path, audit(tmp_path))
    changed_payload = json.loads(changed_baseline.read_text(encoding="utf-8"))
    changed_payload["generated_from_ref"] = f"main@{trusted_sha}"
    changed_baseline.write_text(
        json.dumps(changed_payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    changed_result = audit(
        tmp_path,
        baseline_path=changed_baseline,
        trusted_baseline_ref=trusted_sha,
    )
    assert changed_result["outcome"] == "ERROR"
    assert changed_result["trusted_baseline_state"] == "ERROR"
    assert changed_result["trusted_baseline_errors"] == [
        "bootstrap family baseline does not match trusted schema inventory"
    ]
