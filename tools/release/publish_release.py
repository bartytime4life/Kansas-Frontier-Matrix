#!/usr/bin/env python3
"""
Publish a KFM release only after ReleaseManifest closure resolves.

Pipeline:
- run ReleaseManifest closure resolver
- require finite status = PUBLISHABLE
- in --dry-run mode, print the publish plan and exit
- in publish mode, emit a local publish receipt

This command is intentionally conservative. It does not copy, upload, deploy,
or mutate public state yet. That behavior should be added only after the
repository has a confirmed release storage contract.
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


RESOLVER_PATH = Path("tools/resolvers/release/resolve_release_manifest.py")
DEFAULT_RECEIPT_DIR = Path("data/receipts/release")


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def fail(message: str) -> None:
    print(f"DENY: {message}", file=sys.stderr)
    sys.exit(1)


def run_resolver(manifest_path: Path) -> dict[str, Any]:
    if not RESOLVER_PATH.exists():
        fail(f"missing release resolver: {RESOLVER_PATH}")

    completed = subprocess.run(
        [sys.executable, str(RESOLVER_PATH), str(manifest_path)],
        text=True,
        capture_output=True,
        check=False,
    )

    output = completed.stdout.strip()

    if not output:
        detail = completed.stderr.strip() or f"resolver exited {completed.returncode}"
        fail(f"resolver produced no JSON output: {detail}")

    try:
        result = json.loads(output)
    except json.JSONDecodeError as exc:
        fail(f"resolver output was not valid JSON: {exc}")

    if completed.returncode != 0 and result.get("status") == "PUBLISHABLE":
        fail("resolver returned non-zero exit with PUBLISHABLE status")

    return result


def build_publish_plan(manifest_path: Path, manifest: dict[str, Any], closure: dict[str, Any]) -> dict[str, Any]:
    return {
        "release_id": manifest.get("release_id"),
        "manifest_id": manifest.get("manifest_id"),
        "manifest_path": str(manifest_path),
        "policy_label": manifest.get("policy_label"),
        "review_state": manifest.get("review_state"),
        "spec_hash": manifest.get("spec_hash"),
        "artifact_count": len(manifest.get("artifacts", [])),
        "closure_status": closure.get("status"),
        "artifacts": [
            {
                "artifact_ref": artifact.get("artifact_ref"),
                "evidence_ref": artifact.get("evidence_ref"),
                "provenance_ref": artifact.get("provenance_ref"),
                "stac_ref": artifact.get("stac_ref"),
                "dcat_ref": artifact.get("dcat_ref"),
                "attestation_ref": artifact.get("attestation_ref"),
                "run_receipt_ref": artifact.get("run_receipt_ref"),
            }
            for artifact in manifest.get("artifacts", [])
        ],
    }


def write_publish_receipt(plan: dict[str, Any], receipt_dir: Path) -> Path:
    receipt_dir.mkdir(parents=True, exist_ok=True)

    release_id = str(plan.get("release_id") or "unknown-release")
    safe_release_id = (
        release_id.replace("kfm://", "")
        .replace("/", "_")
        .replace(":", "_")
        .replace(" ", "_")
    )

    timestamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    receipt_path = receipt_dir / f"{safe_release_id}.{timestamp}.publish-receipt.json"

    receipt = {
        "receipt_type": "kfm:PublishReceipt",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "status": "PUBLISHED",
        "mode": "local-receipt-only",
        "plan": plan,
    }

    with receipt_path.open("w", encoding="utf-8") as f:
        json.dump(receipt, f, indent=2, sort_keys=True)
        f.write("\n")

    return receipt_path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Publish a KFM release after closure resolves as PUBLISHABLE.",
    )
    parser.add_argument(
        "manifest",
        help="Path to ReleaseManifest JSON file.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Validate closure and print publish plan without writing a receipt.",
    )
    parser.add_argument(
        "--receipt-dir",
        default=str(DEFAULT_RECEIPT_DIR),
        help="Directory for publish receipts when not using --dry-run.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    manifest_path = Path(args.manifest)

    if not manifest_path.exists():
        fail(f"missing ReleaseManifest: {manifest_path}")

    manifest = load_json(manifest_path)
    closure = run_resolver(manifest_path)

    status = closure.get("status")

    if status != "PUBLISHABLE":
        print(
            json.dumps(
                {
                    "status": "DENY",
                    "reason": "release closure did not resolve as PUBLISHABLE",
                    "closure": closure,
                },
                indent=2,
                sort_keys=True,
            )
        )
        sys.exit(1)

    plan = build_publish_plan(manifest_path, manifest, closure)

    if args.dry_run:
        print(
            json.dumps(
                {
                    "status": "PUBLISHABLE",
                    "mode": "dry-run",
                    "publish_plan": plan,
                },
                indent=2,
                sort_keys=True,
            )
        )
        sys.exit(0)

    receipt_path = write_publish_receipt(plan, Path(args.receipt_dir))

    print(
        json.dumps(
            {
                "status": "PUBLISHED",
                "mode": "local-receipt-only",
                "publish_receipt": str(receipt_path),
                "publish_plan": plan,
            },
            indent=2,
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
