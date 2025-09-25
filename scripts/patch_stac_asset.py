#!/usr/bin/env python3
"""
patch_stac_asset.py — Patch fields on one or more STAC Item assets.

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

# 3) Compute checksum directly (slower) and set size
python scripts/patch_stac_asset.py stac/items/dem/ks_1m_dem_2018_2020.json \
  --asset dem \
  --compute-sha256 \
  --from-file-size

# 4) Override the file used for size/hash (if asset href is remote/relative)
python scripts/patch_stac_asset.py stac/items/dem/ks_1m_dem_2018_2020.json \
  --asset dem \
  --file data/cogs/dem/ks_1m_dem_2018_2020.tif \
  --from-sha256-file --from-file-size

# 5) Patch all assets in many items (glob/dir), filter by role/type, and set item-level fields
python scripts/patch_stac_asset.py stac/items/**/*.json \
  --asset '*' --role data --type "image/tiff; application=geotiff" \
  --from-file-size --from-sha256-file \
  --item-set "properties.some_flag=true" --pretty --backup

Notes
-----
- Edits files in place by default. Use --dry-run to preview.
- Keys like "checksum:sha256" and "file:size" are treated as literal asset keys (no JSON Pointer needed).
- Sidecar checksum lookup accepts:
    "<hex>" | "<hex>  <filename>" | "SHA256 (<filename>) = <hex>"
- Local path resolution:
    --file overrides → else resolve asset href (file://, absolute, repo-root for "data/", else item-relative).
- Exit code is 0 if all successful, 2 if any hard failure occurred.
"""

from __future__ import annotations

import argparse
import glob
import hashlib
import json
import os
import sys
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple, Union
from urllib.parse import urlparse

Json = Dict[str, object]


# ---------------------------
# JSON I/O
# ---------------------------

def _read_json(p: Path) -> Json:
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        raise SystemExit(f"[ERROR] Invalid JSON in {p}:\n{e}") from e


def _write_json_atomic(p: Path, data: Json, pretty: bool, backup: bool) -> None:
    tmp = p.with_suffix(p.suffix + ".tmp")
    if pretty:
        tmp.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    else:
        tmp.write_text(json.dumps(data, separators=(",", ":"), ensure_ascii=False) + "\n", encoding="utf-8")
    if backup:
        bak = p.with_suffix(p.suffix + ".bak")
        try:
            bak.write_text(p.read_text(encoding="utf-8"), encoding="utf-8")
        except FileNotFoundError:
            pass
    tmp.replace(p)


# ---------------------------
# Value helpers
# ---------------------------

def _parse_kv(s: str) -> Tuple[str, str]:
    if "=" not in s:
        raise SystemExit(f"[ERROR] --set/--item-set expects KEY=VALUE, got: {s}")
    k, v = s.split("=", 1)
    k, v = k.strip(), v.strip()
    if not k:
        raise SystemExit("[ERROR] KEY is empty")
    return k, v


def _coerce_value(v: str):
    # ints
    try:
        return int(v)
    except ValueError:
        pass
    # floats
    try:
        return float(v)
    except ValueError:
        pass
    # booleans
    vl = v.lower()
    if vl in ("true", "false"):
        return vl == "true"
    # null
    if vl in ("null", "none"):
        return None
    return v


def _ensure_obj(d: Json, path: List[str]) -> Dict[str, object]:
    cur = d
    for key in path:
        if key not in cur or not isinstance(cur[key], dict):
            cur[key] = {}
        cur = cur[key]  # type: ignore[assignment]
    return cur  # type: ignore[return-value]


# ---------------------------
# Path resolution
# ---------------------------

def _is_remote_href(href: str) -> bool:
    # Robust scheme detection using urlparse; avoids treating "C:\..." as remote
    try:
        pr = urlparse(href)
        return bool(pr.scheme) and pr.scheme.lower() not in ("", "file")
    except Exception:
        return False


def _project_root_from(item_path: Path) -> Path:
    # Heuristic: walk up looking for repo markers
    for parent in [item_path.parent] + list(item_path.parents):
        for marker in (".git", "pyproject.toml", "README.md"):
            if (parent / marker).exists():
                return parent
    # fallback: two levels up (stac/items/<file>.json → repo root)
    return item_path.parents[2] if len(item_path.parents) >= 2 else item_path.parent


def _resolve_asset_file(item_path: Path, asset_href: str, override_file: Optional[Path]) -> Optional[Path]:
    """
    Resolve a local file path to use for size/hash operations.
      - If override_file is set, use it.
      - If href is remote (e.g., http/https), return None.
      - If href is file://, return path after stripping scheme.
      - If href is absolute, return as Path.
      - If href starts with "data/", resolve from repo root.
      - Else treat as item-relative.
    """
    if override_file:
        return override_file.resolve()

    if not isinstance(asset_href, str) or not asset_href:
        return None

    if _is_remote_href(asset_href):
        return None

    # file://
    pr = urlparse(asset_href)
    if pr.scheme.lower() == "file":
        return Path(pr.path).resolve()

    hp = Path(asset_href)
    if hp.is_absolute():
        return hp.resolve()

    # repo-root for data/ convention
    if str(hp).startswith("data/"):
        root = _project_root_from(item_path)
        return (root / hp).resolve()

    # default: relative to item
    return (item_path.parent / hp).resolve()


# ---------------------------
# Sidecar & checksum
# ---------------------------

def _read_first_line(p: Path) -> Optional[str]:
    try:
        text = p.read_text(encoding="utf-8").strip()
        if not text:
            return None
        return text.splitlines()[0]
    except FileNotFoundError:
        return None


def _parse_sidecar_line(line: str) -> Optional[str]:
    """
    Accept formats:
      - "<hex>"
      - "<hex>  <filename>"
      - "SHA256 (<filename>) = <hex>"
    Return hex string or None.
    """
    s = line.strip()
    # SHA256 (file) = hex
    if s.lower().startswith("sha256"):
        parts = s.split("=", 1)
        if len(parts) == 2:
            hexpart = parts[1].strip()
            if len(hexpart) == 64 and all(c in "0123456789abcdefABCDEF" for c in hexpart):
                return hexpart.lower()
        return None
    # hex [filename]
    token = s.split()[0]
    if len(token) == 64 and all(c in "0123456789abcdefABCDEF" for c in token):
        return token.lower()
    return None


def _read_sha256_from_sidecar(file_path: Path) -> Optional[str]:
    """
    Look for:
      - <name>.<ext>.sha256
      - <name>.sha256
      Parse first line with _parse_sidecar_line.
    """
    cands = [
        file_path.with_suffix(file_path.suffix + ".sha256"),
        file_path.with_suffix("").with_suffix(".sha256"),
    ]
    for sidecar in cands:
        line = _read_first_line(sidecar)
        if not line:
            continue
        hexsum = _parse_sidecar_line(line)
        if hexsum:
            return hexsum
    return None


def _compute_sha256(file_path: Path, chunk: int = 1 << 22) -> str:
    h = hashlib.sha256()
    with file_path.open("rb") as f:
        for b in iter(lambda: f.read(chunk), b""):
            h.update(b)
    return h.hexdigest()


# ---------------------------
# Core patching
# ---------------------------

def _patch_single_item(
    item_path: Path,
    asset_key: str,
    sets: Dict[str, str],
    item_sets: Dict[str, str],
    from_file_size: bool,
    from_sha256_file: bool,
    compute_sha256_flag: bool,
    override_file: Optional[Path],
    pretty: bool,
    dry_run: bool,
    backup: bool,
    role_filter: Optional[str],
    type_filter: Optional[str],
) -> int:
    """
    Return 0 on success, 2 on hard failure.
    """
    item = _read_json(item_path)

    # Optional: patch item-level keys
    if item_sets:
        for raw_k, v in item_sets.items():
            # support dotted path for simple nested fields (e.g., "properties.some_flag")
            path = raw_k.split(".")
            if len(path) == 1:
                item[path[0]] = _coerce_value(v)
            else:
                parent = _ensure_obj(item, path[:-1])
                parent[path[-1]] = _coerce_value(v)

    assets = item.setdefault("assets", {})  # type: ignore[assignment]
    if not isinstance(assets, dict):
        print(f"[ERROR] {item_path}: assets is not an object", file=sys.stderr)
        return 2

    # Determine which asset keys to patch
    if asset_key == "*":
        keys = list(assets.keys())
    else:
        if asset_key not in assets:
            print(f"[ERROR] {item_path}: assets.{asset_key} not found", file=sys.stderr)
            return 2
        keys = [asset_key]

    # Apply role/type filtering if requested
    def _match_filters(a: Dict[str, object]) -> bool:
        if role_filter:
            roles = a.get("roles")
            if isinstance(roles, list):
                if role_filter not in roles:
                    return False
            else:
                return False
        if type_filter:
            if str(a.get("type") or "") != type_filter:
                return False
        return True

    patched_any = False
    for k in keys:
        a = assets.get(k)
        if not isinstance(a, dict):
            print(f"[WARN] {item_path}: assets.{k} is not an object; skipping", file=sys.stderr)
            continue
        if (role_filter or type_filter) and not _match_filters(a):
            continue

        # Derive file path for size/hash
        asset_href = str(a.get("href") or "")
        target_file = _resolve_asset_file(item_path, asset_href, override_file)

        # Derived fields first
        if from_file_size:
            if not target_file or not target_file.exists():
                print(f"[WARN] {item_path}: cannot set file:size — file not found or remote: {target_file}", file=sys.stderr)
            else:
                a["file:size"] = int(os.path.getsize(target_file))
                patched_any = True

        if from_sha256_file:
            if not target_file or not target_file.exists():
                print(f"[WARN] {item_path}: cannot read sidecar checksum — file not found or remote: {target_file}", file=sys.stderr)
            else:
                hexsum = _read_sha256_from_sidecar(target_file)
                if hexsum:
                    a["checksum:sha256"] = hexsum
                    patched_any = True
                else:
                    print(f"[WARN] {item_path}: no valid sidecar checksum file for {target_file}", file=sys.stderr)

        if compute_sha256_flag:
            if not target_file or not target_file.exists():
                print(f"[WARN] {item_path}: cannot compute sha256 — file not found or remote: {target_file}", file=sys.stderr)
            else:
                print(f"[INFO] {item_path}: computing sha256 for {target_file} (this may take a while)...", file=sys.stderr)
                a["checksum:sha256"] = _compute_sha256(target_file)
                patched_any = True

        # Explicit sets override anything prior
        for sk, sv in sets.items():
            a[sk] = _coerce_value(sv)
            patched_any = True

    # Dry run?
    if dry_run:
        print(json.dumps(item, indent=2, ensure_ascii=False))
        return 0

    if patched_any or item_sets:
        _write_json_atomic(item_path, item, pretty=pretty, backup=backup)
        print(f"[OK] Patched {item_path}")
    else:
        print(f"[OK] No changes for {item_path}")

    return 0


# ---------------------------
# CLI / batch
# ---------------------------

def _expand_inputs(inputs: List[str]) -> List[Path]:
    files: List[Path] = []
    for pat in inputs:
        p = Path(pat)
        if p.is_dir():
            files.extend(sorted(p.rglob("*.json")))
        else:
            matches = [Path(m) for m in glob.glob(pat, recursive=True)]
            files.extend(sorted(matches if matches else [p] if p.exists() else []))
    # unique, stable
    out: List[Path] = []
    seen = set()
    for f in files:
        if f.exists() and str(f) not in seen:
            out.append(f)
            seen.add(str(f))
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description="Patch fields on STAC Item assets.")
    ap.add_argument("items", nargs="+", help="One or more STAC Item JSON paths (files/dirs/globs)")
    ap.add_argument("--asset", required=True, help="Asset key (e.g., dem) or '*' to patch all assets")
    ap.add_argument("--set", dest="sets", action="append", default=[],
                    help='Set a literal asset field, e.g. --set "checksum:sha256=abc" (repeatable)')
    ap.add_argument("--item-set", dest="item_sets", action="append", default=[],
                    help='Set item-level field, supports dotted path (e.g., --item-set "properties.flag=true")')
    ap.add_argument("--from-file-size", action="store_true",
                    help="Set file:size from the size of the asset file on disk")
    ap.add_argument("--from-sha256-file", action="store_true",
                    help="Set checksum:sha256 by reading a sidecar .sha256 file")
    ap.add_argument("--compute-sha256", action="store_true",
                    help="Compute checksum:sha256 from the asset file contents (slower)")
    ap.add_argument("--file", type=Path, default=None,
                    help="Override path to the asset file for size/hash derivation")
    ap.add_argument("--role", type=str, default=None,
                    help="Only patch assets that include this role (e.g., data, source)")
    ap.add_argument("--type", dest="type_filter", type=str, default=None,
                    help='Only patch assets with this exact media type (e.g., "image/tiff; application=geotiff")')
    ap.add_argument("--pretty", action="store_true", help="Pretty-print JSON on write")
    ap.add_argument("--backup", action="store_true", help="Write a .bak file before overwriting")
    ap.add_argument("--dry-run", action="store_true", help="Print patched JSON to stdout without writing")

    args = ap.parse_args()

    sets = dict(_parse_kv(s) for s in args.sets)
    item_sets = dict(_parse_kv(s) for s in args.item_sets)

    files = _expand_inputs(args.items)
    if not files:
        print("[WARN] No JSON files found for inputs.", file=sys.stderr)
        return 1

    rc = 0
    for item_path in files:
        try:
            code = _patch_single_item(
                item_path=item_path,
                asset_key=args.asset,
                sets=sets,
                item_sets=item_sets,
                from_file_size=args.from_file_size,
                from_sha256_file=args.from_sha256_file,
                compute_sha256_flag=args.compute_sha256,
                override_file=args.file,
                pretty=args.pretty,
                dry_run=args.dry_run,
                backup=args.backup,
                role_filter=args.role,
                type_filter=args.type_filter,
            )
            if code != 0:
                rc = 2
        except SystemExit as se:
            # bubbled JSON parse / schema errors
            print(str(se), file=sys.stderr)
            rc = 2
        except Exception as e:
            print(f"[ERROR] {item_path}: {e}", file=sys.stderr)
            rc = 2

    return rc


if __name__ == "__main__":
    raise SystemExit(main())
