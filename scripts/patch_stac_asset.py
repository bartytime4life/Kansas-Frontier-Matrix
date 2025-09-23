#!/usr/bin/env python3
"""
patch_stac_asset.py — Patch fields on a STAC Item's asset.

Examples
--------
# 1) Set checksum and size from explicit values
python scripts/patch_stac_asset.py stac/items/dem/ks_1m_dem_2018_2020.json \
  --asset dem \
  --set "checksum:sha256=abcdef1234..." \
  --set "file:size=123456789"

# 2) Derive checksum from sidecar file and size from asset on disk
python scripts/patch_stac_asset.py stac/items/dem/ks_1m_dem_2018_2020.json \
  --asset dem \
  --from-sha256-file \
  --from-file-size

# 3) Compute checksum directly from a (large) TIFF (slower) and set size
python scripts/patch_stac_asset.py stac/items/dem/ks_1m_dem_2018_2020.json \
  --asset dem \
  --compute-sha256 \
  --from-file-size

# 4) Override the file used for size/hash (if asset href is remote/relative)
python scripts/patch_stac_asset.py stac/items/dem/ks_1m_dem_2018_2020.json \
  --asset dem \
  --file data/cogs/dem/ks_1m_dem_2018_2020.tif \
  --from-sha256-file --from-file-size

Notes
-----
- This script edits the file **in place** by default. Use --dry-run to preview.
- Keys like "checksum:sha256" and "file:size" are treated as **literal** keys on the asset.
- Sidecar lookup order for checksums:
    <file>.tif.sha256  →  <file>.sha256
- Only standard library; safe for CI and local use.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
from typing import Dict, Tuple, Optional


def _read_json(p: Path) -> dict:
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise SystemExit(f"[ERROR] Invalid JSON in {p}:\n{e}") from e


def _write_json_atomic(p: Path, data: dict, pretty: bool, backup: bool):
    tmp = p.with_suffix(p.suffix + ".tmp")
    if pretty:
        tmp.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    else:
        tmp.write_text(json.dumps(data, separators=(",", ":")) + "\n", encoding="utf-8")
    if backup:
        bak = p.with_suffix(p.suffix + ".bak")
        try:
            bak.write_text(p.read_text(encoding="utf-8"), encoding="utf-8")
        except FileNotFoundError:
            pass
    tmp.replace(p)


def _parse_kv(s: str) -> Tuple[str, str]:
    if "=" not in s:
        raise SystemExit(f"[ERROR] --set expects KEY=VALUE, got: {s}")
    k, v = s.split("=", 1)
    k, v = k.strip(), v.strip()
    if not k:
        raise SystemExit("[ERROR] --set KEY is empty")
    return k, v


def _coerce_value(v: str):
    # Try int, then float, else leave as string
    try:
        return int(v)
    except ValueError:
        pass
    try:
        return float(v)
    except ValueError:
        pass
    # Booleans
    vl = v.lower()
    if vl in ("true", "false"):
        return vl == "true"
    return v


def _resolve_asset_file(
    item_path: Path, asset_href: str, override_file: Optional[Path]
) -> Optional[Path]:
    """
    Resolve a local file path to use for size/hash operations.
    - If override_file is set, use it.
    - If href looks like remote (scheme://), return None (unless override).
    - If href is relative, resolve relative to item json.
    - If href starts with "data/", resolve from repo root.
    """
    if override_file:
        return override_file.resolve()

    # Detect remote
    if isinstance(asset_href, str) and asset_href.lower().split("://", 1)[0].isalpha():
        # looks like scheme://
        return None

    hp = Path(asset_href)
    if str(hp).startswith("data/"):
        # repo-root relative
        repo = item_path.parents[2] if len(item_path.parents) >= 2 else item_path.parent
        return (repo / hp).resolve()

    return (item_path.parent / hp).resolve()


def _read_sha256_from_sidecar(file_path: Path) -> Optional[str]:
    """
    Read a sha256 hex from a sidecar file in either format:
      - <name>.tif.sha256   (sha256sum format: "<hex>  <filename>")
      - <name>.sha256       (same content format)
    Returns hex string or None if not found / invalid.
    """
    candidates = [file_path.with_suffix(file_path.suffix + ".sha256"),
                  file_path.with_suffix("").with_suffix(".sha256")]

    for sidecar in candidates:
        if not sidecar.exists():
            continue
        line = sidecar.read_text(encoding="utf-8").strip().splitlines()[0] if sidecar.read_text(encoding="utf-8").strip() else ""
        if not line:
            continue
        parts = line.split()
        if not parts:
            continue
        # First token should be the hex digest
        hexpart = parts[0].strip()
        if len(hexpart) == 64 and all(c in "0123456789abcdefABCDEF" for c in hexpart):
            return hexpart.lower()
    return None


def _compute_sha256(file_path: Path) -> str:
    h = hashlib.sha256()
    with file_path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 22), b""):  # 4 MiB chunks
            h.update(chunk)
    return h.hexdigest()


def patch_asset(
    item_path: Path,
    asset_key: str,
    sets: Dict[str, str],
    from_file_size: bool,
    from_sha256_file: bool,
    compute_sha256_flag: bool,
    override_file: Optional[Path],
    pretty: bool,
    dry_run: bool,
    backup: bool,
) -> int:
    item = _read_json(item_path)
    assets = item.setdefault("assets", {})
    asset = assets.setdefault(asset_key, {})
    if not isinstance(asset, dict):
        raise SystemExit(f"[ERROR] assets.{asset_key} is not an object in {item_path}")

    # Determine path to asset file (for size/hash ops)
    asset_href = asset.get("href", "")
    target_file = _resolve_asset_file(item_path, asset_href, override_file)

    # Apply derived fields first (size/hash), then explicit --set overrides last
    if from_file_size:
        if not target_file or not target_file.exists():
            print(f"[WARN] Cannot set file:size — asset file not found or remote: {target_file}")
        else:
            size = os.path.getsize(target_file)
            asset["file:size"] = int(size)

    if from_sha256_file:
        if not target_file or not target_file.exists():
            print(f"[WARN] Cannot read sidecar checksum — asset file not found or remote: {target_file}")
        else:
            hexsum = _read_sha256_from_sidecar(target_file)
            if hexsum:
                asset["checksum:sha256"] = hexsum
            else:
                print(f"[WARN] No valid sidecar checksum file found for {target_file}")

    if compute_sha256_flag:
        if not target_file or not target_file.exists():
            print(f"[WARN] Cannot compute sha256 — asset file not found or remote: {target_file}")
        else:
            print(f"[INFO] Computing sha256 for {target_file} (this may take a while)...")
            asset["checksum:sha256"] = _compute_sha256(target_file)

    # Apply explicit --set KEY=VALUE pairs (override anything prior)
    for k, v in sets.items():
        asset[k] = _coerce_value(v)

    # Dry run?
    if dry_run:
        print(json.dumps(item, indent=2))
        return 0

    _write_json_atomic(item_path, item, pretty=pretty, backup=backup)
    print(f"[OK] Patched {item_path} :: assets.{asset_key}")
    return 0


def main():
    ap = argparse.ArgumentParser(description="Patch fields on a STAC Item's asset.")
    ap.add_argument("item", type=Path, help="Path to STAC Item JSON")
    ap.add_argument("--asset", required=True, help="Asset key in item['assets'] (e.g., dem, hillshade)")
    ap.add_argument("--set", dest="sets", action="append", default=[],
                    help='Set a literal asset field, e.g. --set "checksum:sha256=abc" (repeatable)')
    ap.add_argument("--from-file-size", action="store_true",
                    help="Set file:size from the size of the asset file on disk")
    ap.add_argument("--from-sha256-file", action="store_true",
                    help="Set checksum:sha256 by reading a sidecar .sha256 file (prefers <file>.tif.sha256)")
    ap.add_argument("--compute-sha256", action="store_true",
                    help="Compute checksum:sha256 from the asset file contents (slower)")
    ap.add_argument("--file", type=Path, default=None,
                    help="Override path to the asset file for size/hash derivation")
    ap.add_argument("--pretty", action="store_true", help="Pretty-print JSON on write")
    ap.add_argument("--backup", action="store_true", help="Write a .bak file before overwriting")
    ap.add_argument("--dry-run", action="store_true", help="Print patched JSON to stdout without writing")

    args = ap.parse_args()

    sets = dict(_parse_kv(s) for s in args.sets)
    return SystemExit(
        patch_asset(
            item_path=args.item,
            asset_key=args.asset,
            sets=sets,
            from_file_size=args.from_file_size,
            from_sha256_file=args.from_sha256_file,
            compute_sha256_flag=args.compute_sha256,
            override_file=args.file,
            pretty=args.pretty,
            dry_run=args.dry_run,
            backup=args.backup,
        )
    )


if __name__ == "__main__":
    main()
