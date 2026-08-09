from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path


SCHEMA_NAME = "evidence_drawer_payload.schema.json"
DRAFT_2020_12 = "https://json-schema.org/draft/2020-12/schema"
ANCHORS = {
    "evidence": Path("schemas/contracts/v1/evidence") / SCHEMA_NAME,
    "runtime": Path("schemas/contracts/v1/runtime") / SCHEMA_NAME,
    "ui": Path("schemas/contracts/v1/ui") / SCHEMA_NAME,
}


def _load_json(path: Path) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"schema must be a JSON object: {path.as_posix()}")
    return data


def audit(repo_root: Path) -> dict:
    schema_root = repo_root / "schemas/contracts/v1"
    paths = sorted(schema_root.rglob(SCHEMA_NAME))
    findings: list[dict] = []

    if not paths:
        return {
            "outcome": "ERROR",
            "placement_state": "NEEDS_REVIEW",
            "reason_codes": ["NO_EVIDENCE_DRAWER_SCHEMAS"],
            "schemas": [],
        }

    relative_paths = [path.relative_to(repo_root) for path in paths]
    missing_anchors = [
        role for role, relative in ANCHORS.items() if relative not in relative_paths
    ]

    documents: list[tuple[Path, dict]] = []
    parse_errors: list[str] = []
    for relative, path in zip(relative_paths, paths):
        try:
            documents.append((relative, _load_json(path)))
        except (OSError, UnicodeError, json.JSONDecodeError, ValueError):
            parse_errors.append(relative.as_posix())

    schema_ids = [
        document.get("$id")
        for _, document in documents
        if isinstance(document.get("$id"), str) and document.get("$id")
    ]
    duplicate_ids = sorted(
        schema_id for schema_id, count in Counter(schema_ids).items() if count > 1
    )

    invalid_drafts = sorted(
        relative.as_posix()
        for relative, document in documents
        if document.get("$schema") != DRAFT_2020_12
    )
    missing_ids = sorted(
        relative.as_posix()
        for relative, document in documents
        if not isinstance(document.get("$id"), str) or not document.get("$id")
    )

    for relative, document in documents:
        metadata = document.get("x-kfm")
        metadata = metadata if isinstance(metadata, dict) else {}
        properties = document.get("properties")
        property_count = len(properties) if isinstance(properties, dict) else None
        path_text = relative.as_posix()
        if relative == ANCHORS["evidence"]:
            role = "evidence-family-placement-candidate"
        elif relative == ANCHORS["runtime"]:
            role = "runtime-compatibility-or-placement-candidate"
        elif relative == ANCHORS["ui"]:
            role = "ui-public-safe-profile"
        elif path_text.startswith("schemas/contracts/v1/domains/"):
            role = "domain-profile-or-scaffold"
        else:
            role = "other-profile"

        findings.append(
            {
                "path": path_text,
                "role": role,
                "schema_id": document.get("$id"),
                "status": metadata.get("status"),
                "contract_doc": metadata.get("contract_doc"),
                "additional_properties": document.get("additionalProperties"),
                "property_count": property_count,
            }
        )

    reason_codes: list[str] = []
    if missing_anchors:
        reason_codes.append("MISSING_PLACEMENT_ANCHOR")
    if parse_errors:
        reason_codes.append("SCHEMA_PARSE_ERROR")
    if missing_ids:
        reason_codes.append("MISSING_SCHEMA_ID")
    if duplicate_ids:
        reason_codes.append("DUPLICATE_SCHEMA_ID")
    if invalid_drafts:
        reason_codes.append("UNEXPECTED_JSON_SCHEMA_DRAFT")

    return {
        "outcome": "PASS" if not reason_codes else "ERROR",
        "placement_state": "NEEDS_REVIEW",
        "reason_codes": reason_codes,
        "anchor_paths": {role: path.as_posix() for role, path in ANCHORS.items()},
        "schema_count": len(paths),
        "parse_errors": parse_errors,
        "missing_anchors": missing_anchors,
        "missing_ids": missing_ids,
        "duplicate_ids": duplicate_ids,
        "invalid_drafts": invalid_drafts,
        "schemas": findings,
        "boundary": (
            "Inventory and identity audit only; it does not select a canonical schema, "
            "migrate consumers, change contract meaning, or grant release/publication authority."
        ),
    }


def main(argv: list[str]) -> int:
    repo_root = Path(argv[0]).resolve() if argv else Path.cwd().resolve()
    result = audit(repo_root)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["outcome"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
