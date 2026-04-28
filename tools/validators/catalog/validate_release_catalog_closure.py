#!/usr/bin/env python3
"""Validate release-to-catalog closure across manifest and catalog artifacts."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

FORBIDDEN_PUBLIC_REFS = (
    "/raw/",
    "/work/",
    "/quarantine/",
    "data/raw/",
    "data/work/",
    "data/quarantine/",
)

BLOCKED_PUBLIC_VALUES = {
    "TODO",
    "todo",
    "UNKNOWN",
    "unknown",
    "NEEDS-VERIFICATION",
    "restricted",
    "deny",
    "",
}


def fail(message: str) -> None:
    print(f"DENY: {message}", file=sys.stderr)
    sys.exit(1)


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def assert_present(mapping: dict[str, Any], key: str, label: str) -> Any:
    value = mapping.get(key)
    if value in (None, ""):
        fail(f"{label} missing {key}")
    return value


def assert_not_blocked(value: Any, label: str) -> None:
    if isinstance(value, str) and value in BLOCKED_PUBLIC_VALUES:
        fail(f"{label} cannot be {value}")


def contains_forbidden_ref(value: Any) -> bool:
    if isinstance(value, str):
        lowered = value.lower()
        return any(token in lowered for token in FORBIDDEN_PUBLIC_REFS)
    if isinstance(value, dict):
        return any(contains_forbidden_ref(v) for v in value.values())
    if isinstance(value, list):
        return any(contains_forbidden_ref(v) for v in value)
    return False


def check_manifest(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    if manifest.get("policy_label") != "public":
        fail("ReleaseManifest requires policy_label=public")

    if manifest.get("review_state") not in {"reviewed", "published"}:
        fail("ReleaseManifest requires review_state reviewed or published")

    artifacts = manifest.get("artifacts", [])
    if not isinstance(artifacts, list) or not artifacts:
        fail("ReleaseManifest missing artifacts")

    for idx, artifact in enumerate(artifacts):
        if not isinstance(artifact, dict):
            fail(f"artifacts[{idx}] must be an object")

        label = f"artifacts[{idx}]"
        for key in (
            "artifact_ref",
            "evidence_ref",
            "provenance_ref",
            "stac_ref",
            "dcat_ref",
            "release_ref",
            "publish_receipt_ref",
            "spec_hash",
        ):
            value = assert_present(artifact, key, label)
            assert_not_blocked(value, f"{label}.{key}")

    return artifacts


def check_catalog(matrix: dict[str, Any]) -> list[dict[str, Any]]:
    if matrix.get("status") != "closed":
        fail("CatalogMatrix requires status=closed")

    artifacts = matrix.get("artifacts", [])
    if not isinstance(artifacts, list) or not artifacts:
        fail("CatalogMatrix missing artifacts")

    return artifacts


def main() -> None:
    if len(sys.argv) != 3:
        fail(
            "usage: validate_release_catalog_closure.py "
            "<release-manifest.json> <catalog-matrix.json>"
        )

    manifest_path = Path(sys.argv[1])
    matrix_path = Path(sys.argv[2])

    if not manifest_path.exists():
        fail(f"missing ReleaseManifest: {manifest_path}")

    if not matrix_path.exists():
        fail(f"missing CatalogMatrix: {matrix_path}")

    manifest = load_json(manifest_path)
    matrix = load_json(matrix_path)

    manifest_artifacts = check_manifest(manifest)
    matrix_artifacts = check_catalog(matrix)

    manifest_by_artifact_ref = {
        item["artifact_ref"]: item
        for item in manifest_artifacts
        if isinstance(item.get("artifact_ref"), str)
    }

    matrix_by_artifact_ref = {
        item["artifact_ref"]: item
        for item in matrix_artifacts
        if isinstance(item.get("artifact_ref"), str)
    }

    missing_in_matrix = sorted(set(manifest_by_artifact_ref) - set(matrix_by_artifact_ref))
    if missing_in_matrix:
        fail(f"CatalogMatrix missing artifacts present in ReleaseManifest: {missing_in_matrix}")

    for artifact_ref, manifest_artifact in manifest_by_artifact_ref.items():
        matrix_artifact = matrix_by_artifact_ref[artifact_ref]

        for key in (
            "evidence_ref",
            "provenance_ref",
            "stac_ref",
            "dcat_ref",
            "release_ref",
            "publish_receipt_ref",
            "spec_hash",
        ):
            if manifest_artifact.get(key) != matrix_artifact.get(key):
                fail(
                    f"artifact {artifact_ref} mismatch for {key}: "
                    f"manifest={manifest_artifact.get(key)} matrix={matrix_artifact.get(key)}"
                )

    if contains_forbidden_ref(manifest) or contains_forbidden_ref(matrix):
        fail("closure references RAW / WORK / QUARANTINE material")

    print(
        "ALLOW: valid release-catalog closure: "
        f"manifest={manifest_path} matrix={matrix_path}"
    )


if __name__ == "__main__":
    main()
