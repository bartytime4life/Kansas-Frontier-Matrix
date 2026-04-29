#!/usr/bin/env python3
"""
Build a minimal KFM Ecology EvidenceBundle from time-slice pipeline artifacts.

This is a no-network bundle builder. It records artifact paths, sha256 digests,
artifact roles, and lightweight validation context for CI / dry-run evidence.

Example:
  python tools/validators/ecology/build_evidence_bundle.py \
    --bundle-id kfm://evidence/ecology/example-pass-timeslice \
    --artifact ingest_manifest=tests/fixtures/ecology/timeslice/pass/ingest_manifest.json \
    --artifact qa_decision=/tmp/ecology_timeslice_qa_decision.json \
    --artifact tileset_metadata=tests/fixtures/ecology/timeslice/pass/tileset_metadata.json \
    --artifact promotion_decision=/tmp/promotion_decision.json \
    --out /tmp/evidence_bundle.json
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
    return (
        datetime.now(timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z")
    )


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()

    try:
        with path.open("rb") as handle:
            for chunk in iter(lambda: handle.read(1024 * 1024), b""):
                digest.update(chunk)
    except FileNotFoundError:
        raise SystemExit(f"ERROR: artifact not found: {path}")

    return "sha256:" + digest.hexdigest()


def parse_artifact(value: str) -> tuple[str, Path]:
    if "=" not in value:
        raise argparse.ArgumentTypeError(
            "artifact must use role=path form, "
            f"got: {value}"
        )

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
    created_at: str | None = None,
    source: str | None = None,
    notes: list[str] | None = None,
) -> dict[str, Any]:
    if not bundle_id.startswith("kfm://evidence/ecology/"):
        raise ValueError("bundle_id must start with kfm://evidence/ecology/")

    artifact_records = [
        build_artifact_record(role, path)
        for role, path in artifacts
    ]

    return {
        "schema_version": "v1",
        "object_type": "EvidenceBundle",
        "bundle_id": bundle_id,
        "domain": "ecology",
        "policy_label": policy_label,
        "created_at": created_at or utc_now(),
        "source": source or "no-network-fixture",
        "artifacts": artifact_records,
        "artifact_count": len(artifact_records),
        "notes": notes or [],
    }


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build a minimal KFM Ecology EvidenceBundle."
    )
    parser.add_argument("--bundle-id", required=True)
    parser.add_argument(
        "--artifact",
        action="append",
        type=parse_artifact,
        default=[],
        help="Artifact in role=path form. May be provided multiple times.",
    )
    parser.add_argument("--policy-label", default="public")
    parser.add_argument("--source")
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
            created_at=args.created_at,
            source=args.source,
            notes=args.note,
        )
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(
        json.dumps(bundle, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    print(json.dumps(bundle, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
