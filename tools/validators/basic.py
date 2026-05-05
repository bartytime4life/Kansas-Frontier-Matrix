from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from tools.ingest.utils import sha256_file


REQUIRED_BUNDLE_FIELDS = {
    "schema_version",
    "object_type",
    "bundle_id",
    "domain",
    "policy_label",
    "rights_status",
    "spec_hash",
    "source_refs",
    "evidence_refs",
    "validators",
}

REQUIRED_RECEIPT_FIELDS = {
    "schema_version",
    "object_type",
    "bundle_id",
    "source_id",
    "fingerprint",
    "spec_hash",
    "policy_label",
    "rights_status",
    "validators",
    "runner_version",
    "result",
    "artifacts",
    "signing",
}


def _load(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def validate_bundle(path: Path) -> list[str]:
    errors: list[str] = []
    data = _load(path)
    missing = sorted(REQUIRED_BUNDLE_FIELDS - set(data))
    if missing:
        errors.append(f"{path}: missing fields {missing}")
    if data.get("object_type") != "EvidenceBundle":
        errors.append(f"{path}: object_type must be EvidenceBundle")
    if not isinstance(data.get("source_refs"), list) or not data.get("source_refs"):
        errors.append(f"{path}: source_refs must be a non-empty list")
    if not isinstance(data.get("evidence_refs"), list) or not data.get("evidence_refs"):
        errors.append(f"{path}: evidence_refs must be a non-empty list")
    if data.get("rights_status") in {None, "", "unresolved"}:
        errors.append(f"{path}: rights_status is unresolved")
    if data.get("policy_label") in {None, "", "unresolved"}:
        errors.append(f"{path}: policy_label is unresolved")
    return errors


def validate_receipt(path: Path) -> list[str]:
    errors: list[str] = []
    data = _load(path)
    missing = sorted(REQUIRED_RECEIPT_FIELDS - set(data))
    if missing:
        errors.append(f"{path}: missing fields {missing}")
    if data.get("object_type") != "RunReceipt":
        errors.append(f"{path}: object_type must be RunReceipt")
    bundle_path = Path(data.get("artifacts", {}).get("evidence_bundle_path", ""))
    if not bundle_path.exists():
        # Receipts may be moved as a packet; fall back to sibling path.
        bundle_path = path.parent / "evidence_bundle.json"
    if not bundle_path.exists():
        errors.append(f"{path}: evidence_bundle_path does not exist")
    else:
        actual = sha256_file(bundle_path)
        if actual != data.get("fingerprint"):
            errors.append(f"{path}: fingerprint mismatch expected {data.get('fingerprint')} got {actual}")
    if data.get("result") not in {"PENDING_SIGNATURE", "PENDING_PROMOTION"}:
        errors.append(f"{path}: invalid result {data.get('result')}")
    return errors


def validate_tree(root: Path) -> list[str]:
    errors: list[str] = []
    for bundle in root.rglob("evidence_bundle.json"):
        errors.extend(validate_bundle(bundle))
    for receipt in root.rglob("run_receipt.json"):
        errors.extend(validate_receipt(receipt))
    if not list(root.rglob("run_receipt.json")):
        errors.append(f"{root}: no run_receipt.json files found")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Basic KFM EvidenceBundle/receipt validator")
    parser.add_argument("root", help="Receipt tree root")
    args = parser.parse_args(argv)
    errors = validate_tree(Path(args.root))
    if errors:
        for error in errors:
            print(error)
        return 1
    print(f"validated {args.root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
