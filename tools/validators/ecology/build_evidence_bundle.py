#!/usr/bin/env python3
"""
Build a minimal KFM Ecology EvidenceBundle from time-slice pipeline artifacts.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import mimetypes
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    try:
        with path.open("rb") as handle:
            for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                digest.update(chunk)
    except FileNotFoundError:
        raise SystemExit(f"ERROR: artifact not found: {path}")

    return "sha256:" + digest.hexdigest()


def sha256_json(value: Any) -> str:
    payload = json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return "sha256:" + hashlib.sha256(payload.encode("utf-8")).hexdigest()


def parse_artifact(value: str) -> tuple[str, Path]:
    if "=" not in value:
        raise argparse.ArgumentTypeError(f"artifact must use role=path form, got: {value}")

    role, raw_path = value.split("=", 1)
    role = role.strip()
    raw_path = raw_path.strip()

    if not role:
        raise argparse.ArgumentTypeError("artifact role cannot be empty")
    if not raw_path:
        raise argparse.ArgumentTypeError("artifact path cannot be empty")

    return role, Path(raw_path)


def media_type_for(path: Path) -> str:
    guessed, _ = mimetypes.guess_type(str(path))
    return guessed or "application/octet-stream"


def build_artifact_record(role: str, path: Path) -> dict[str, Any]:
    return {
        "role": role,
        "uri": str(path),
        "media_type": media_type_for(path),
        "digest": sha256_file(path),
    }


def build_bundle(
    *,
    bundle_id: str,
    artifacts: list[tuple[str, Path]],
    policy_label: str,
    rights_status: str,
    sensitivity: str,
    source_refs: list[str],
    dataset_refs: list[str],
    evidence_refs: list[str],
    object_refs: list[str],
    resolved: bool,
    evidence_bundle_resolved: bool,
    created_at: str | None = None,
    title: str | None = None,
    source: str | None = None,
    policy_id: str | None = None,
    surface: str | None = None,
    publication_state: str | None = None,
    source_role: str | None = None,
    claim_status: str | None = None,
    catalog_closure: bool | None = None,
    exact_geometry_present: bool | None = None,
    public_geometry_policy: str | None = None,
    public_visibility: str | None = None,
    limitations: list[str] | None = None,
    notes: list[str] | None = None,
) -> dict[str, Any]:
    if not bundle_id.startswith("kfm://evidence/ecology/"):
        raise ValueError("bundle_id must start with kfm://evidence/ecology/")

    artifact_records = [build_artifact_record(role, path) for role, path in artifacts]

    bundle: dict[str, Any] = {
        "schema_version": "v1",
        "object_type": "EvidenceBundle",
        "bundle_id": bundle_id,
        "domain": "ecology",
        "created_at": created_at or utc_now(),
        "source": source or "no-network-fixture",
        "source_refs": source_refs,
        "dataset_refs": dataset_refs,
        "evidence_refs": evidence_refs,
        "object_refs": object_refs,
        "resolved": resolved,
        "evidence_bundle_resolved": evidence_bundle_resolved,
        "policy_label": policy_label,
        "rights_status": rights_status,
        "sensitivity": sensitivity,
        "artifacts": artifact_records,
        "artifact_count": len(artifact_records),
        "limitations": limitations or [],
        "notes": notes or [],
    }

    optional_fields = {
        "title": title,
        "policy_id": policy_id,
        "surface": surface,
        "publication_state": publication_state,
        "source_role": source_role,
        "claim_status": claim_status,
        "catalog_closure": catalog_closure,
        "exact_geometry_present": exact_geometry_present,
        "public_geometry_policy": public_geometry_policy,
        "public_visibility": public_visibility,
    }

    for key, value in optional_fields.items():
        if value is not None:
            bundle[key] = value

    bundle["spec_hash"] = sha256_json(
        {
            "bundle_id": bundle_id,
            "source_refs": source_refs,
            "dataset_refs": dataset_refs,
            "evidence_refs": evidence_refs,
            "object_refs": object_refs,
            "artifact_digests": [
                {"role": item["role"], "digest": item["digest"]}
                for item in artifact_records
            ],
            "policy_label": policy_label,
            "rights_status": rights_status,
            "sensitivity": sensitivity,
        }
    )

    return bundle


def main() -> int:
    parser = argparse.ArgumentParser(description="Build a minimal KFM Ecology EvidenceBundle.")
    parser.add_argument("--bundle-id", required=True)
    parser.add_argument("--artifact", action="append", type=parse_artifact, default=[])
    parser.add_argument("--source-ref", action="append", default=["kfm://source/ecology/no-network-fixture"])
    parser.add_argument("--dataset-ref", action="append", default=["kfm://dataset/ecology/no-network-fixture"])
    parser.add_argument("--evidence-ref", action="append", default=["kfm://evidence/ref/ecology/no-network-fixture"])
    parser.add_argument("--object-ref", action="append", default=[])
    parser.add_argument("--policy-label", default="public")
    parser.add_argument("--rights-status", default="open")
    parser.add_argument("--sensitivity", default="public")
    parser.add_argument("--resolved", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--evidence-bundle-resolved", action=argparse.BooleanOptionalAction, default=True)
    parser.add_argument("--title")
    parser.add_argument("--source")
    parser.add_argument("--policy-id")
    parser.add_argument("--surface", choices=["public", "internal", "restricted"])
    parser.add_argument("--publication-state", choices=["candidate", "held", "quarantined", "published", "released", "ready"])
    parser.add_argument("--source-role")
    parser.add_argument("--claim-status", choices=["CONFIRMED", "PROPOSED", "UNKNOWN", "NEEDS_VERIFICATION", "CONFLICTED", "SUPERSEDED"])
    parser.add_argument("--catalog-closure", action=argparse.BooleanOptionalAction)
    parser.add_argument("--exact-geometry-present", action=argparse.BooleanOptionalAction)
    parser.add_argument("--public-geometry-policy")
    parser.add_argument("--public-visibility", choices=["public", "generalized", "internal_only", "restricted"])
    parser.add_argument("--limitation", action="append", default=[])
    parser.add_argument("--note", action="append", default=[])
    parser.add_argument("--created-at")
    parser.add_argument("--out", required=True, type=Path)

    args = parser.parse_args()

    if not args.artifact:
        print("ERROR: at least one --artifact role=path is required", file=sys.stderr)
        return 1

    try:
        bundle = build_bundle(
            bundle_id=args.bundle_id,
            artifacts=args.artifact,
            policy_label=args.policy_label,
            rights_status=args.rights_status,
            sensitivity=args.sensitivity,
            source_refs=args.source_ref,
            dataset_refs=args.dataset_ref,
            evidence_refs=args.evidence_ref,
            object_refs=args.object_ref,
            resolved=args.resolved,
            evidence_bundle_resolved=args.evidence_bundle_resolved,
            created_at=args.created_at,
            title=args.title,
            source=args.source,
            policy_id=args.policy_id,
            surface=args.surface,
            publication_state=args.publication_state,
            source_role=args.source_role,
            claim_status=args.claim_status,
            catalog_closure=args.catalog_closure,
            exact_geometry_present=args.exact_geometry_present,
            public_geometry_policy=args.public_geometry_policy,
            public_visibility=args.public_visibility,
            limitations=args.limitation,
            notes=args.note,
        )
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(bundle, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(bundle, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
