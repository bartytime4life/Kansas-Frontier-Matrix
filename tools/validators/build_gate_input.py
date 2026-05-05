#!/usr/bin/env python3
"""Build a Conftest input document for one promotion gate."""
from __future__ import annotations

import argparse
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

MAX_TEXT_BYTES = 1_000_000

def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()

def read_text_limited(path: Path) -> tuple[str, bool]:
    data = path.read_bytes()
    truncated = len(data) > MAX_TEXT_BYTES
    if truncated:
        data = data[:MAX_TEXT_BYTES]
    return data.decode("utf-8", errors="replace"), truncated

def describe_path(path_str: str) -> dict[str, Any]:
    path = Path(path_str)
    info: dict[str, Any] = {"path": path_str, "exists": path.exists()}
    if not path.exists():
        info["kind"] = "directory" if path_str.endswith("/") else "missing"
        return info
    if path.is_dir():
        children = [p for p in path.iterdir() if p.name not in {".gitkeep"}]
        info.update({"kind": "directory", "child_count": len(children), "children": sorted(str(p) for p in children[:200])})
        return info
    if not path.is_file():
        info["kind"] = "other"
        return info

    stat = path.stat()
    info.update({"kind": "file", "size_bytes": stat.st_size, "sha256": sha256_file(path)})
    try:
        text, truncated = read_text_limited(path)
        info["text"] = text
        info["text_stripped"] = text.strip()
        info["text_truncated"] = truncated
    except OSError as exc:
        info["read_error"] = str(exc)
        return info
    if path.suffix.lower() == ".json":
        try:
            info["json"] = json.loads(info["text"])
        except json.JSONDecodeError as exc:
            info["parse_error"] = f"{exc.msg} at line {exc.lineno}, column {exc.colno}"
    return info

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--gate", required=True, choices=list("ABCDEFG"))
    parser.add_argument("--contract", default="promotion-contract.json")
    parser.add_argument("--out", required=True)
    args = parser.parse_args()

    contract_path = Path(args.contract)
    try:
        contract = json.loads(contract_path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"failed to read contract {contract_path}: {exc}", file=sys.stderr)
        return 2

    gate = contract.get("gates", {}).get(args.gate)
    if not gate:
        print(f"gate {args.gate!r} not found in {contract_path}", file=sys.stderr)
        return 2

    required = list(gate.get("requires", []))
    optional = list(gate.get("optional", []))
    all_paths = []
    for path in required + optional:
        if path not in all_paths:
            all_paths.append(path)

    gate_input = {
        "gate": args.gate,
        "gate_name": gate.get("name"),
        "policy": gate.get("policy"),
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "required": required,
        "optional": optional,
        "files": {path: describe_path(path) for path in all_paths},
    }

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(gate_input, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {out}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
