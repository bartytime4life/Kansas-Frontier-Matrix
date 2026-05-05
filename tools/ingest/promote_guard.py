from __future__ import annotations

import argparse
import json
from pathlib import Path


def guard_tree(root: Path, require_signatures: bool = True) -> list[str]:
    errors: list[str] = []
    receipts = list(root.rglob("run_receipt.json"))
    if not receipts:
        return [f"{root}: no run_receipt.json files found"]
    for receipt_path in receipts:
        with receipt_path.open("r", encoding="utf-8") as fh:
            receipt = json.load(fh)
        if receipt.get("result") != "PENDING_PROMOTION":
            errors.append(f"{receipt_path}: result is {receipt.get('result')}, not PENDING_PROMOTION")
        if require_signatures:
            for name in ["evidence_bundle.json", "decision_log.json", "run_receipt.json"]:
                artifact = receipt_path.parent / name
                bundle = Path(str(artifact) + ".sigstore.json")
                if not artifact.exists():
                    errors.append(f"{receipt_path}: missing {artifact.name}")
                if not bundle.exists():
                    errors.append(f"{receipt_path}: missing signature bundle {bundle.name}")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Fail-closed promotion guard for KFM POC receipts")
    parser.add_argument("root", help="Receipt tree root")
    parser.add_argument("--require-signatures", action="store_true", help="Require .sigstore.json bundles")
    args = parser.parse_args(argv)
    errors = guard_tree(Path(args.root), require_signatures=args.require_signatures)
    if errors:
        for error in errors:
            print(error)
        return 1
    print(f"promotion preconditions satisfied for {args.root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
