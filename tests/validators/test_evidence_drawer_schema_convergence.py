from __future__ import annotations

import json
from pathlib import Path

from tools.validators.validate_evidence_drawer_schema_convergence import audit


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
