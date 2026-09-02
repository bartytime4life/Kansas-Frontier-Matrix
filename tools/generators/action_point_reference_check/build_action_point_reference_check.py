"""Build deterministic fixture-only action-point reference checks."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, Mapping, Sequence

REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_SRC = REPO_ROOT / "packages/hashing/src"
for import_path in (REPO_ROOT, PACKAGE_SRC):
    if str(import_path) not in sys.path:
        sys.path.insert(0, str(import_path))

from hashing import compute_spec_hash  # noqa: E402

PERMISSIONS = {
    "action_allowed": False,
    "repository_write_allowed": False,
    "lifecycle_write_allowed": False,
    "release_allowed": False,
    "publication_allowed": False,
    "public_use_allowed": False,
}
NON_EFFECTS = [
    "does_not_dereference_a_live_source",
    "does_not_execute_the_action",
    "does_not_authorize_agent_or_repository_writes",
    "does_not_release_deploy_publish_or_authorize_public_use",
]


def _has_abbreviation(value: str | None) -> bool:
    return value is not None and ("..." in value or "…" in value)


def expected_report(document: Mapping[str, Any]) -> tuple[str, list[str]]:
    action = document["action"]
    source = document["authoritative_source"]
    reasons: list[str] = []
    if action["residue_status"] == "MISSING":
        return "UNCLASSIFIABLE", ["ACTION_RESIDUE_MISSING"]
    if action["literal_class"] == "OPAQUE_IDENTIFIER" and _has_abbreviation(action["literal"]):
        reasons.append("ABBREVIATED_LITERAL")
    if source["dereferenced_at"] > action["acted_at"]:
        reasons.append("DEREFERENCE_AFTER_ACTION")
    if reasons:
        return "BLOCKED", sorted(reasons)
    if action["literal"] == source["literal"]:
        return "MATCH", ["LITERAL_MATCH"]
    return "MISMATCH", ["LITERAL_MISMATCH"]


def identity_projection(document: Mapping[str, Any]) -> dict[str, Any]:
    return {key: value for key, value in document.items() if key not in {"check_id", "spec_hash"}}


def expected_identity(document: Mapping[str, Any]) -> tuple[str, str]:
    spec_hash = compute_spec_hash(identity_projection(document))
    return spec_hash, "kfm:action-point-check:" + spec_hash.removeprefix("sha256:")


def finalize(document: dict[str, Any], *, derive_report: bool = True) -> dict[str, Any]:
    if derive_report:
        outcome, reasons = expected_report(document)
        document["report"] = {"outcome": outcome, "reason_codes": reasons}
    document["spec_hash"], document["check_id"] = expected_identity(document)
    return document


def build_document(variant: str) -> dict[str, Any]:
    action_literal: str | None = "4EqwqxVz8xXf7HhT4ZQj2kYybDSq4"
    source_literal = action_literal
    acted_at = "2026-08-25T14:00:00Z"
    dereferenced_at = "2026-08-25T13:59:30Z"
    residue_status = "PRESERVED"
    if variant == "MISMATCH":
        action_literal = "4EqwqxVz8xXf7HhT4ZQj2kYybDSq5"
    elif variant == "ABBREVIATED":
        action_literal = "4EqwqxVz...ybDSq4"
    elif variant == "LATE_DEREFERENCE":
        dereferenced_at = "2026-08-25T14:00:30Z"
    elif variant == "MISSING_RESIDUE":
        action_literal = None
        residue_status = "MISSING"
    elif variant != "MATCH":
        raise ValueError("unsupported variant")
    document: dict[str, Any] = {
        "schema_version": "1.0.0",
        "profile": "kfm.validation.action-point-reference-check.v1",
        "profile_status": "PROPOSED_INACTIVE",
        "execution_mode": "FIXTURE_ONLY_NO_EXTERNAL_EFFECT",
        "authority": "NONE",
        "check_id": "kfm:action-point-check:" + "0" * 64,
        "action": {
            "kind": "TOOL_CALL",
            "literal_class": "OPAQUE_IDENTIFIER",
            "literal": action_literal,
            "acted_at": acted_at,
            "residue_status": residue_status,
        },
        "authoritative_source": {
            "source_ref": "kfm://fixture/authoritative-recipes/v1",
            "source_digest": compute_spec_hash({"fixture": "authoritative-recipes-v1"}),
            "literal": source_literal,
            "dereferenced_at": dereferenced_at,
            "method": "PINNED_BLOB",
        },
        "pointer": {"kind": "FULL_LITERAL", "locator": "recipes.md#vault-address"},
        "report": {"outcome": "MATCH", "reason_codes": ["LITERAL_MATCH"]},
        "permissions": dict(PERMISSIONS),
        "non_effects": list(NON_EFFECTS),
        "spec_hash": "sha256:" + "0" * 64,
    }
    return finalize(document)


def build_case(case: Mapping[str, Any]) -> dict[str, Any]:
    document = build_document(str(case["variant"]))
    mutation = case.get("mutation")
    if mutation is None:
        return document
    if mutation == "LINE_NUMBER_ONLY":
        document["pointer"] = {"kind": "LINE_NUMBER_ONLY", "locator": "AGENT.md:162"}
        return finalize(document)
    if mutation == "REPORT_DRIFT":
        document["report"] = {"outcome": "MATCH", "reason_codes": ["LITERAL_MATCH"]}
        return finalize(document, derive_report=False)
    if mutation == "SPEC_HASH_DRIFT":
        document["spec_hash"] = "sha256:" + "f" * 64
        document["check_id"] = "kfm:action-point-check:" + "f" * 64
        return document
    raise ValueError("unsupported mutation")


def render_case(case_id: str, manifest: Mapping[str, Any]) -> dict[str, Any]:
    for case in manifest.get("cases", []):
        if isinstance(case, dict) and case.get("case_id") == case_id:
            return build_case(case)
    raise KeyError(case_id)


def main(argv: Sequence[str] | None = None) -> int:
    import argparse

    parser = argparse.ArgumentParser(description="Render one ActionPointReferenceCheck fixture.")
    parser.add_argument("--case", required=True)
    parser.add_argument(
        "--manifest",
        type=Path,
        default=REPO_ROOT / "fixtures/contracts/v1/validation/action_point_reference_check/cases.json",
    )
    args = parser.parse_args(argv)
    manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
    print(json.dumps(render_case(args.case, manifest), sort_keys=True, separators=(",", ":")))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
