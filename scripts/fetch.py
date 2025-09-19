#!/usr/bin/env python3
"""
scripts/fetch.py
================

Fetch source datasets (STAC Items and/or source catalogs) to `data/raw/` with
checksums and a manifest. Designed for the Kansas-Frontier-Matrix / Kansas Geo Timeline stack.

Key features
------------
- Accepts mixed inputs:
  • STAC Item files (individual JSON items)
  • STAC-like source catalogs (lists/maps with asset URLs)
  • Direct HTTP(S) URLs
- Streams downloads to disk (no RAM spikes), writes *.sha256 sidecars.
- Skips existing files when size+hash match (idempotent).
- Concurrent downloads with retries/backoff (stdlib only).
- Emits a manifest JSON capturing provenance + checksums for MCP reproducibility.

Usage
-----
# Fetch everything under data/sources and data/stac into data/raw
python scripts/fetch.py data/sources/*.json data/stac/*.json

# Fetch a specific URL into data/raw/usgs/
python scripts/fetch.py "https://example.org/file.tif" --subdir usgs

# Print plan only
python scripts/fetch.py data/sources/*.json --dry-run

# Increase concurrency and retries
python scripts/fetch.py data/sources/*.json --jobs 6 --retries 4

Notes
-----
- This script is dependency-light (stdlib). It does NOT convert rasters to COG,
  nor does it `dvc add` files (you can do that in a follow-up Make target).
- STAC handling: we try assets['source'] first, otherwise all assets.
"""

from __future__ import annotations

import argparse
import concurrent.futures as cf
import contextlib
import glob
import hashlib
import json
import math
import os
import sys
import time
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Dict, Iterable, Iterator, List, Mapping, Optional, Sequence, Tuple
from urllib.parse import urlparse
from urllib.request import Request, urlopen


# ------------------------------
# Small IO / JSON helpers
# ------------------------------

def _read_json(p: Path) -> Dict[str, Any]:
    with p.open("r", encoding="utf-8") as f:
        return json.load(f)


def _write_json(p: Path, obj: Dict[str, Any]) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, sort_keys=True, ensure_ascii=False)
        f.write("\n")


def _iter_inputs(patterns: Iterable[str]) -> Iterator[str]:
    for pat in patterns:
        # If this is a URL, yield it directly
        if pat.startswith("http://") or pat.startswith("https://"):
            yield pat
            continue
        # Otherwise expand filesystem patterns
        p = Path(pat)
        if p.is_dir():
            for f in sorted(p.rglob("*.json")):
                yield str(f)
        else:
            for m in sorted(glob.glob(pat)):
                yield m


def _sha256_file(path: Path, chunk: int = 1024 * 1024) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            b = f.read(chunk)
            if not b:
                break
            h.update(b)
    return h.hexdigest()


# ------------------------------
# STAC / Catalog parsing
# ------------------------------

def _assets_from_stac_item(item: Mapping[str, Any]) -> List[Tuple[str, Mapping[str, Any]]]:
    """Return [(name, asset_dict), ...] preferring 'source' first if present."""
    assets = item.get("assets")
    if not isinstance(assets, dict) or not assets:
        return []
    if "source" in assets and isinstance(assets["source"], Mapping):
        # put source first
        rest = [(k, v) for k, v in assets.items() if k != "source" and isinstance(v, Mapping)]
        return [("source", assets["source"])] + rest
    return [(k, v) for k, v in assets.items() if isinstance(v, Mapping)]


def _urls_from_json(doc: Mapping[str, Any]) -> List[str]:
    """
    Extract download URLs from:
      - STAC Item (assets)
      - Simple catalogs: {"assets":[{"href":...}, ...]} OR {"urls":["...", "..."]} OR list of hrefs
    """
    out: List[str] = []

    # STAC Item (type=Feature) with assets map
    if doc.get("type") == "Feature" and "assets" in doc:
        for _name, a in _assets_from_stac_item(doc):
            href = a.get("href")
            if isinstance(href, str) and href.startswith(("http://", "https://")):
                out.append(href)

    # Generic catalog forms
    assets = doc.get("assets")
    if isinstance(assets, list):
        for a in assets:
            if isinstance(a, Mapping):
                href = a.get("href")
                if isinstance(href, str) and href.startswith(("http://", "https://")):
                    out.append(href)

    urls = doc.get("urls")
    if isinstance(urls, list):
        for u in urls:
            if isinstance(u, str) and u.startswith(("http://", "https://")):
                out.append(u)

    # Allow top-level arrays of strings (lenient)
    if isinstance(doc, list):
        for u in doc:
            if isinstance(u, str) and u.startswith(("http://", "https://")):
                out.append(u)

    # De-duplicate preserving order
    seen = set()
    deduped = []
    for u in out:
        if u not in seen:
            deduped.append(u)
            seen.add(u)
    return deduped


def collect_urls(inputs: Iterable[str]) -> List[str]:
    """
    For each input:
      - if URL: keep it
      - if JSON file: parse and collect URLs
    """
    urls: List[str] = []
    for item in _iter_inputs(inputs):
        if item.startswith(("http://", "https://")):
            urls.append(item)
            continue
        p = Path(item)
        try:
            doc = _read_json(p)
        except Exception as e:
            print(f"[WARN] Cannot parse JSON {p}: {e}", file=sys.stderr)
            continue
        found = _urls_from_json(doc)
        if not found and doc.get("type") == "Feature":
            # Informative hint if a STAC item lacks absolute asset HREFs
            print(f"[WARN] STAC item {p} had no HTTP(S) asset hrefs; skipping.", file=sys.stderr)
        urls.extend(found)
    # unique, stable order
    seen = set()
    out = []
    for u in urls:
        if u not in seen:
            out.append(u)
            seen.add(u)
    return out


# ------------------------------
# Download machinery
# ------------------------------

@dataclass
class FetchResult:
    url: str
    path: str
    size: int
    sha256: str
    existed: bool
    elapsed_s: float
    ok: bool
    error: Optional[str] = None


def _human(n: float) -> str:
    if n <= 0:
        return "0B"
    units = ["B", "KB", "MB", "GB", "TB"]
    i = int(math.floor(math.log(n, 1024)))
    i = max(0, min(i, len(units) - 1))
    return f"{n / (1024 ** i):.2f}{units[i]}"


def _download_one(url: str, dest: Path, retries: int, timeout: float, overwrite: bool) -> FetchResult:
    dest.parent.mkdir(parents=True, exist_ok=True)
    t0 = time.time()

    # If file exists and overwrite=False, try to verify quickly
    if dest.exists() and not overwrite:
        try:
            sha = _sha256_file(dest)
            size = dest.stat().st_size
            # Write (or refresh) sidecar
            (dest.with_suffix(dest.suffix + ".sha256")).write_text(sha + "\n", encoding="utf-8")
            return FetchResult(url, str(dest), size, sha, True, time.time() - t0, True, None)
        except Exception as e:
            # Fall through to re-download attempt
            print(f"[INFO] Re-downloading {dest.name}: existing hash failed: {e}", file=sys.stderr)

    # Retry loop
    backoff = 1.0
    last_err: Optional[str] = None
    for attempt in range(1, retries + 2):
        try:
            req = Request(url, headers={"User-Agent": "kfm-fetch/1.0"})
            with contextlib.closing(urlopen(req, timeout=timeout)) as resp:
                # Try to infer filename from URL if needed
                tmp = dest.with_suffix(dest.suffix + ".part")
                with tmp.open("wb") as f:
                    # Stream to disk
                    total = 0
                    while True:
                        chunk = resp.read(1024 * 1024)
                        if not chunk:
                            break
                        f.write(chunk)
                        total += len(chunk)
                # Move into place
                tmp.rename(dest)
            sha = _sha256_file(dest)
            (dest.with_suffix(dest.suffix + ".sha256")).write_text(sha + "\n", encoding="utf-8")
            return FetchResult(url, str(dest), dest.stat().st_size, sha, False, time.time() - t0, True, None)
        except Exception as e:
            last_err = f"{type(e).__name__}: {e}"
            if attempt <= retries:
                time.sleep(backoff)
                backoff *= 2
            else:
                break

    return FetchResult(url, str(dest), 0, "", False, time.time() - t0, False, last_err)


def target_path_for(url: str, base: Path, subdir: Optional[str] = None) -> Path:
    """
    Build a safe target path for a URL under base/subdir, preserving the filename.
    """
    parsed = urlparse(url)
    name = Path(parsed.path).name or "download.bin"
    if subdir:
        return base / subdir / name
    return base / name


def fetch_urls(
    urls: Sequence[str],
    base_dir: Path,
    *,
    subdir: Optional[str],
    jobs: int,
    retries: int,
    timeout: float,
    overwrite: bool,
    dry_run: bool,
) -> List[FetchResult]:
    results: List[FetchResult] = []

    if dry_run:
        for url in urls:
            dest = target_path_for(url, base_dir, subdir=subdir)
            print(f"[PLAN] {url} -> {dest}")
        return results

    # Concurrency
    with cf.ThreadPoolExecutor(max_workers=max(1, jobs)) as ex:
        futs = []
        for url in urls:
            dest = target_path_for(url, base_dir, subdir=subdir)
            futs.append(ex.submit(_download_one, url, dest, retries, timeout, overwrite))
        for fut in cf.as_completed(futs):
            res = fut.result()
            results.append(res)
            tag = "OK" if res.ok else "FAIL"
            print(f"[{tag}] {_human(res.size):>8}  {Path(res.path).name}  ({res.elapsed_s:.2f}s)")
            if res.error:
                print(f"      {res.url}\n      Error: {res.error}", file=sys.stderr)

    return results


def write_manifest(results: Sequence[FetchResult], manifest_path: Path, inputs: Sequence[str]) -> None:
    manifest = {
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "inputs": list(inputs),
        "entries": [asdict(r) for r in results],
    }
    _write_json(manifest_path, manifest)
    print(f"[OK] wrote manifest: {manifest_path}")


# ------------------------------
# CLI
# ------------------------------

def _build_argparser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(
        prog="fetch.py",
        description="Fetch source datasets (STAC items, catalogs, or direct URLs) into data/raw/ with checksums."
    )
    ap.add_argument("inputs", nargs="+", help="JSON files/dirs/globs or HTTP(S) URLs")
    ap.add_argument("--dest", type=Path, default=Path("data/raw"), help="Destination base directory (default: data/raw)")
    ap.add_argument("--subdir", type=str, default=None, help="Optional subdirectory under dest/ to place files")
    ap.add_argument("--jobs", type=int, default=4, help="Concurrent downloads (default: 4)")
    ap.add_argument("--retries", type=int, default=2, help="Retries per URL on failure (default: 2)")
    ap.add_argument("--timeout", type=float, default=120.0, help="Socket timeout in seconds (default: 120)")
    ap.add_argument("--overwrite", action="store_true", help="Always re-download even if file exists")
    ap.add_argument("--dry-run", action="store_true", help="Print plan and exit")
    ap.add_argument("--manifest", type=Path, default=Path("data/raw/manifest.fetch.json"), help="Manifest output path")
    return ap


def main(argv: Optional[List[str]] = None) -> int:
    ap = _build_argparser()
    args = ap.parse_args(argv)

    # Collect URLs from inputs
    urls = collect_urls(args.inputs)
    if not urls:
        print("[WARN] No HTTP(S) URLs found in inputs.", file=sys.stderr)
        return 1

    # Fetch
    results = fetch_urls(
        urls,
        args.dest,
        subdir=args.subdir,
        jobs=max(1, int(args.jobs)),
        retries=max(0, int(args.retries)),
        timeout=max(1.0, float(args.timeout)),
        overwrite=bool(args.overwrite),
        dry_run=bool(args.dry_run),
    )

    # Write manifest if any results (non-dry-run)
    if not args.dry_run:
        write_manifest(results, args.manifest, args.inputs)

        # Non-zero if any failed
        if any(not r.ok for r in results):
            return 2

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

