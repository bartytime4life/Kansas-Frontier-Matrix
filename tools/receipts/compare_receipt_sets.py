from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python -m tools.receipts.compare_receipt_sets",
        description="Compare receipt sets between two ecology receipt manifests.",
    )

    parser.add_argument("--left", required=True, help="Path to left manifest JSON.")
    parser.add_argument("--right", required=True, help="Path to right manifest JSON.")
    parser.add_argument("--out", default=None, help="Optional output path for diff JSON.")

    return parser


def _load_manifest(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("Manifest must be a JSON object.")
    return value


def _key(receipt: dict[str, Any]) -> tuple[str, str]:
    return (
        str(receipt.get("receipt_type", "")),
        str(receipt.get("receipt_ref", "")),
    )


def compare_manifests(left_manifest: dict[str, Any], right_manifest: dict[str, Any]) -> dict[str, Any]:
    left_receipts = { _key(item): item for item in left_manifest.get("receipts", []) }
    right_receipts = { _key(item): item for item in right_manifest.get("receipts", []) }

    added_keys = sorted(set(right_receipts) - set(left_receipts))
    removed_keys = sorted(set(left_receipts) - set(right_receipts))

    changed: list[dict[str, Any]] = []
    for shared_key in sorted(set(left_receipts) & set(right_receipts)):
        left_item = left_receipts[shared_key]
        right_item = right_receipts[shared_key]

        if left_item != right_item:
            changed.append(
                {
                    "receipt_type": shared_key[0],
                    "receipt_ref": shared_key[1],
                    "left": left_item,
                    "right": right_item,
                }
            )

    return {
        "left_manifest_ref": left_manifest.get("manifest_id"),
        "right_manifest_ref": right_manifest.get("manifest_id"),
        "added": [right_receipts[key] for key in added_keys],
        "removed": [left_receipts[key] for key in removed_keys],
        "changed": changed,
        "summary": {
            "added_count": len(added_keys),
            "removed_count": len(removed_keys),
            "changed_count": len(changed),
        },
    }


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    left_path = Path(args.left)
    right_path = Path(args.right)

    left_manifest = _load_manifest(left_path)
    right_manifest = _load_manifest(right_path)

    diff = compare_manifests(left_manifest, right_manifest)
    rendered = json.dumps(diff, indent=2, sort_keys=True)

    if args.out:
        out_path = Path(args.out)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(rendered + "\n", encoding="utf-8")

    print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
