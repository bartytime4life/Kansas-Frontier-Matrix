from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def _utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def _canonical_json_bytes(obj: Any) -> bytes:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")


def generate_manifest(processed_dir: Path, out: Path) -> dict[str, Any]:
    datasets = []
    for path in sorted(processed_dir.glob("*.json")):
        payload = json.loads(path.read_text(encoding="utf-8"))
        datasets.append(
            {
                "id": payload.get("id"),
                "plants_symbol": payload.get("properties", {}).get("plants:symbol"),
                "path": path.name,
                "spec_hash": payload.get("spec_hash"),
            }
        )

    manifest: dict[str, Any] = {
        "schema_version": "1.0.0",
        "object_type": "usda_plants_spec_hash_manifest",
        "generated_at": _utc_now_iso(),
        "algorithm": "sha256",
        "canonicalization": "json_sorted_keys_compact_separators_excluding_self_hash_fields",
        "dataset_count": len(datasets),
        "datasets": datasets,
    }
    manifest_hash = hashlib.sha256(_canonical_json_bytes(manifest)).hexdigest()
    manifest["manifest_hash"] = f"sha256:{manifest_hash}"

    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate USDA PLANTS deterministic spec_hash proof manifest")
    parser.add_argument("--processed-dir", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()
    generate_manifest(args.processed_dir, args.out)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
