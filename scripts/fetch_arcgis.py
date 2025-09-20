#!/usr/bin/env python3
# scripts/fetch_arcgis.py
"""
Fetch ArcGIS ImageService / FeatureService layers to local files (robust).

Source JSON (examples)
----------------------
Imagery:
{
  "id": "ks_hillshade",
  "title": "Kansas Elevation Hillshade",
  "type": "arcgis-imagery",
  "url": "https://example.com/ArcGIS/rest/services/KS/Hillshade/ImageServer",
  "format": "geotiff",                   # geotiff|png|jpg
  "bbox": [-102.05, 36.99, -94.59, 40.00],
  "pixel_size": 30,
  "crs": "EPSG:4326"
}

Feature:
{
  "id": "rr_lines_1887",
  "title": "Railroads (1887)",
  "type": "arcgis-feature",
  "url": "https://example.com/ArcGIS/rest/services/KS/railroads/FeatureServer/0",
  "where": "1=1",
  "bbox": [-102.05, 36.99, -94.59, 40.00],   # optional spatial filter
  "crs": "EPSG:4326",
  "out_fields": "*"
}

Usage
-----
# Fetch every JSON descriptor in data/sources into data/raw
python scripts/fetch_arcgis.py --sources data/sources --out data/raw

# Fetch specific file(s)
python scripts/fetch_arcgis.py --sources data/sources/ks_hillshade.json --out data/raw

# Only fetch a specific id from a folder of JSON files
python scripts/fetch_arcgis.py --sources data/sources --out data/raw --id ks_hillshade

# Add token/user-agent and check sizes aggressively
python scripts/fetch_arcgis.py --sources data/sources --out data/raw --token "$TOKEN" --user-agent "kfm/1.0"
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import sys
import time
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple, Union
from urllib.parse import urlencode

import requests
from requests.adapters import HTTPAdapter, Retry

Json = Dict[str, Any]
PathLike = Union[str, os.PathLike[str]]

# ------------------------------
# HTTP session (retries/backoff)
# ------------------------------

def build_session(
    *,
    user_agent: Optional[str] = None,
    retries: int = 4,
    backoff: float = 0.5,
    timeout: float = 60.0,
) -> requests.Session:
    sess = requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=frozenset(["GET", "POST"]),
        raise_on_status=False,
    )
    adapter = HTTPAdapter(max_retries=retry, pool_connections=16, pool_maxsize=32)
    sess.mount("http://", adapter)
    sess.mount("https://", adapter)
    sess.headers.update({
        "Accept": "*/*",
        "User-Agent": user_agent or "kfm-fetch-arcgis/1.0",
    })
    # store default timeout on session
    sess.request = _with_timeout(sess.request, timeout)
    return sess


def _with_timeout(request_fn, timeout: float):
    def _wrapped(method, url, **kwargs):
        if "timeout" not in kwargs:
            kwargs["timeout"] = timeout
        return request_fn(method, url, **kwargs)
    return _wrapped


# ------------------------------
# IO helpers / SHA
# ------------------------------

def read_json(p: PathLike) -> Json:
    return json.loads(Path(p).read_text(encoding="utf-8"))


def write_bytes(p: PathLike, data: bytes) -> None:
    p = Path(p)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("wb") as f:
        f.write(data)


def write_json(p: PathLike, obj: Mapping[str, Any]) -> None:
    p = Path(p)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8") as f:
        json.dump(obj, f, indent=2, sort_keys=True, ensure_ascii=False)
        f.write("\n")


def sha256_bytes(b: bytes) -> str:
    h = hashlib.sha256()
    h.update(b)
    return h.hexdigest()


def sha256_file(p: PathLike, chunk: int = 1024 * 1024) -> str:
    h = hashlib.sha256()
    with Path(p).open("rb") as f:
        while True:
            buf = f.read(chunk)
            if not buf:
                break
            h.update(buf)
    return h.hexdigest()


def sidecar_sha(path: PathLike, sha: str) -> None:
    Path(f"{path}.sha256").write_text(sha + "\n", encoding="utf-8")


# ------------------------------
# Utilities
# ------------------------------

def is_epsg(code: Optional[str]) -> Optional[int]:
    """
    Parse 'EPSG:xxxx' -> 4326 (int). Returns None if unknown.
    """
    try:
        if not code:
            return None
        code = code.strip().upper()
        if code.startswith("EPSG:"):
            return int(code.split(":", 1)[1])
        return int(code)  # allow '4326'
    except Exception:
        return None


def estimate_pixels(bbox: Sequence[float], pixel_size_m: float) -> Tuple[int, int]:
    """
    Rough geodesic estimate (spherical), 111 km/deg, scale lon by cos(mean lat).
    """
    minx, miny, maxx, maxy = bbox
    lat_m = (maxy - miny) * 111_000.0
    midlat = 0.5 * (miny + maxy)
    lon_m = (maxx - minx) * 111_000.0 * math.cos(math.radians(midlat))
    nx = max(1, int(round(lon_m / pixel_size_m)))
    ny = max(1, int(round(lat_m / pixel_size_m)))
    return nx, ny


def split_bbox(bbox: Sequence[float], nx: int, ny: int) -> List[List[float]]:
    """
    Split bbox into nx * ny tiles, row-major.
    """
    minx, miny, maxx, maxy = bbox
    dx = (maxx - minx) / nx
    dy = (maxy - miny) / ny
    tiles = []
    for j in range(ny):
        y0 = miny + j * dy
        y1 = y0 + dy
        for i in range(nx):
            x0 = minx + i * dx
            x1 = x0 + dx
            tiles.append([x0, y0, x1, y1])
    return tiles


def safe_name(s: str) -> str:
    return "".join(ch if ch.isalnum() or ch in ("-", "_", ".") else "_" for ch in s)


# ------------------------------
# Imagery (exportImage)
# ------------------------------

@dataclass
class ImageryRequest:
    url: str
    bbox: List[float]
    bbox_epsg: int
    image_epsg: int
    pixel_size: float
    fmt: str  # tiff|png|jpg
    token: Optional[str] = None


def export_imagery(
    sess: requests.Session,
    req: ImageryRequest,
    out_path: Path,
    *,
    max_dim: int = 4096,
    overwrite: bool = False,
) -> Dict[str, Any]:
    """
    Exports imagery. If estimated pixels exceed max_dim, tiles the bbox into smaller chunks
    and fetches each tile individually, then writes them as chunk files alongside main file.
    (Local mosaic is intentionally not attempted; consumers can ingest per-tile COGs or re-tile.)
    """
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fmt = req.fmt.lower()
    if fmt == "geotiff":
        img_format = "tiff"
        ext = "tif"
    elif fmt in ("tiff", "tif"):
        img_format = "tiff"
        ext = "tif"
    elif fmt in ("png", "jpg", "jpeg"):
        img_format = fmt
        ext = fmt if fmt != "jpeg" else "jpg"
    else:
        raise ValueError(f"Unsupported imagery format: {req.fmt}")

    # Idempotency
    if out_path.exists() and not overwrite:
        sha = sha256_file(out_path)
        sidecar_sha(out_path, sha)
        return {"path": str(out_path), "size": Path(out_path).stat().st_size, "sha256": sha, "tiled": False}

    # Estimate pixel dims
    est_w, est_h = estimate_pixels(req.bbox, req.pixel_size)
    tiles: List[List[float]]
    if max(est_w, est_h) <= max_dim:
        tiles = [req.bbox]
    else:
        nx = math.ceil(est_w / max_dim)
        ny = math.ceil(est_h / max_dim)
        tiles = split_bbox(req.bbox, nx, ny)

    # Fetch tiles
    chunk_paths: List[Path] = []
    total_size = 0
    for idx, b in enumerate(tiles):
        params = {
            "bbox": ",".join(map(str, b)),
            "bboxSR": req.bbox_epsg,
            "imageSR": req.image_epsg,
            "format": img_format,
            "f": "image",
        }

        # Compute tile pixel size (approx)
        tw, th = estimate_pixels(b, req.pixel_size)
        # ArcGIS expects 'size' as width,height; some servers also support 'pixelSize'
        params["size"] = f"{min(tw, max_dim)},{min(th, max_dim)}"

        if req.token:
            params["token"] = req.token

        url = req.url.rstrip("/") + "/exportImage"
        r = sess.get(url, params=params)
        # If server returned JSON error (content-type), try to parse it
        if r.headers.get("Content-Type", "").startswith("application/json"):
            try:
                err = r.json()
                raise RuntimeError(f"exportImage error: {err}")
            except Exception:
                r.raise_for_status()
        r.raise_for_status()
        data = r.content

        # If single tile → write directly to out_path; else write chunk
        if len(tiles) == 1:
            write_bytes(out_path, data)
            total_size = len(data)
        else:
            chunk = out_path.with_name(out_path.stem + f".chunk{idx:03d}." + ext)
            write_bytes(chunk, data)
            chunk_paths.append(chunk)
            total_size += len(data)

    # SHA(s)
    if len(tiles) == 1:
        sha = sha256_file(out_path)
        sidecar_sha(out_path, sha)
    else:
        # for tiled export, write a small index json and SHA each chunk
        index = {
            "base": str(out_path.name),
            "format": ext,
            "tiles": [p.name for p in chunk_paths],
        }
        index_path = out_path.with_suffix(out_path.suffix + ".tiles.json")
        write_json(index_path, index)
        for p in chunk_paths:
            sidecar_sha(p, sha256_file(p))
        sha = sha256_file(index_path)
        sidecar_sha(index_path, sha)

    return {
        "path": str(out_path),
        "size": total_size,
        "sha256": sha,
        "tiled": len(tiles) > 1,
        "tiles": [str(p) for p in chunk_paths] if len(tiles) > 1 else [],
    }


# ------------------------------
# Features (paged query)
# ------------------------------

@dataclass
class FeatureRequest:
    url: str                  # .../FeatureServer/{layer} OR .../MapServer/{layer}
    where: str = "1=1"
    out_fields: str = "*"
    bbox: Optional[List[float]] = None
    out_epsg: Optional[int] = None
    token: Optional[str] = None


def export_features(
    sess: requests.Session,
    req: FeatureRequest,
    out_path: Path,
    *,
    page_size: int = 5000,
    overwrite: bool = False,
) -> Dict[str, Any]:
    """
    Paged ArcGIS REST query to GeoJSON, with optional spatial filter (bbox).
    De-dupes OIDs, concatenates features in memory, then writes one GeoJSON.
    """
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if out_path.exists() and not overwrite:
        sha = sha256_file(out_path)
        sidecar_sha(out_path, sha)
        return {"path": str(out_path), "size": out_path.stat().st_size, "sha256": sha, "pages": 0}

    # Get objectIdField (or fallback)
    meta = sess.get(req.url + "?f=json" + (f"&token={req.token}" if req.token else "")).json()
    oid_field = meta.get("objectIdField", "OBJECTID")

    features: List[Json] = []
    seen_ids = set()
    offset = 0
    pages = 0

    while True:
        params = {
            "where": req.where or "1=1",
            "outFields": req.out_fields or "*",
            "returnGeometry": "true",
            "f": "geojson",
            "resultOffset": offset,
            "resultRecordCount": page_size,
        }
        if req.bbox:
            params["geometry"] = ",".join(map(str, req.bbox))
            params["geometryType"] = "esriGeometryEnvelope"
            params["inSR"] = 4326  # assuming WGS84 bbox
            params["spatialRel"] = "esriSpatialRelIntersects"
        if req.out_epsg:
            params["outSR"] = req.out_epsg
        if req.token:
            params["token"] = req.token

        r = sess.get(req.url.rstrip("/") + "/query", params=params)
        # Some servers return 200 with error JSON; check 'error'
        try:
            obj = r.json()
            if isinstance(obj, dict) and obj.get("error"):
                raise RuntimeError(obj["error"])
        except Exception:
            r.raise_for_status()
            obj = r.json()

        if "features" not in obj:
            # Some servers return GeoJSON FeatureCollection at top-level
            feats = obj.get("features", []) if isinstance(obj, dict) else []
        else:
            feats = obj["features"]

        if not feats:
            break

        # Dedup by OID when possible
        for f in feats:
            oid = None
            if isinstance(f, dict):
                props = f.get("properties") or f.get("attributes") or {}
                oid = props.get(oid_field) if isinstance(props, dict) else None
            if oid is None or oid not in seen_ids:
                features.append(f)
                if oid is not None:
                    seen_ids.add(oid)

        pages += 1
        offset += page_size

    # Write GeoJSON FeatureCollection
    fc = {"type": "FeatureCollection", "features": features}
    write_json(out_path, fc)
    sha = sha256_file(out_path)
    sidecar_sha(out_path, sha)
    return {"path": str(out_path), "size": out_path.stat().st_size, "sha256": sha, "pages": pages}


# ------------------------------
# Source discovery
# ------------------------------

def list_sources(sources: Sequence[str]) -> List[Path]:
    out: List[Path] = []
    for s in sources:
        p = Path(s)
        if p.is_dir():
            out.extend(sorted(p.glob("*.json")))
        elif p.is_file():
            out.append(p)
    return out


# ------------------------------
# CLI & Orchestration
# ------------------------------

@dataclass
class Source:
    id: str
    type: str
    url: str
    title: Optional[str] = None
    format: Optional[str] = None
    bbox: Optional[List[float]] = None
    pixel_size: Optional[float] = None
    crs: Optional[str] = None
    where: Optional[str] = None
    out_fields: Optional[str] = None


def parse_source(p: Path) -> Source:
    s = read_json(p)
    required = ["id", "type", "url"]
    miss = [k for k in required if k not in s]
    if miss:
        raise ValueError(f"{p}: missing required keys: {miss}")
    return Source(
        id=s["id"],
        type=s["type"],
        url=s["url"],
        title=s.get("title"),
        format=s.get("format"),
        bbox=s.get("bbox"),
        pixel_size=s.get("pixel_size"),
        crs=s.get("crs"),
        where=s.get("where"),
        out_fields=s.get("out_fields"),
    )


def main(argv: Optional[Sequence[str]] = None) -> int:
    ap = argparse.ArgumentParser(
        prog="fetch_arcgis.py",
        description="Fetch ArcGIS ImageService/FeatureService layers to local files."
    )
    ap.add_argument("--sources", nargs="+", required=True, help="Folder(s) and/or JSON file(s)")
    ap.add_argument("--out", required=True, help="Output directory")
    ap.add_argument("--id", default=None, help="Only fetch a single 'id' from provided sources")
    ap.add_argument("--token", default=os.getenv("ARCGIS_TOKEN"), help="ArcGIS token (env ARCGIS_TOKEN by default)")
    ap.add_argument("--user-agent", default=None, help="Custom User-Agent")
    ap.add_argument("--max-dim", type=int, default=4096, help="Max tile dimension for imagery (default 4096)")
    ap.add_argument("--page-size", type=int, default=5000, help="Feature page size (default 5000)")
    ap.add_argument("--retries", type=int, default=4, help="HTTP retries (default 4)")
    ap.add_argument("--timeout", type=float, default=60.0, help="HTTP timeout seconds (default 60)")
    ap.add_argument("--overwrite", action="store_true", help="Overwrite existing files")
    ap.add_argument("--manifest", default="data/raw/manifest.arcgis.json", help="Manifest path")
    args = ap.parse_args(argv)

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    # Build HTTP session
    sess = build_session(
        user_agent=args.user_agent,
        retries=args.retries,
        timeout=args.timeout,
    )

    src_files = list_sources(args.sources)
    if not src_files:
        print("[WARN] no source JSON files found", file=sys.stderr)
        return 1

    manifest_entries: List[Json] = []
    failures = 0
    t0 = time.time()

    for jf in src_files:
        try:
            s = parse_source(jf)
            if args.id and s.id != args.id:
                continue

            if s.type == "arcgis-imagery":
                if not s.bbox or not s.pixel_size:
                    raise ValueError(f"{jf}: imagery source requires 'bbox' and 'pixel_size'")
                epsg = is_epsg(s.crs) or 4326
                fmt = (s.format or "geotiff").lower()
                out_ext = "tif" if fmt in ("geotiff", "tiff") else fmt
                out_path = out_dir / f"{safe_name(s.id)}.{out_ext}"
                info = export_imagery(
                    sess,
                    ImageryRequest(
                        url=s.url,
                        bbox=s.bbox,
                        bbox_epsg=4326,       # we assume bbox in WGS84
                        image_epsg=epsg,
                        pixel_size=float(s.pixel_size),
                        fmt=fmt,
                        token=args.token,
                    ),
                    out_path,
                    max_dim=int(args.max_dim),
                    overwrite=bool(args.overwrite),
                )
                entry = {
                    "id": s.id, "type": s.type, "title": s.title, "url": s.url,
                    "out": info, "source_file": str(jf)
                }
                print(f"[OK] imagery {s.id} -> {info['path']}  size={info['size']}  tiled={info['tiled']}")
                manifest_entries.append(entry)

            elif s.type == "arcgis-feature":
                out_path = out_dir / f"{safe_name(s.id)}.geojson"
                info = export_features(
                    sess,
                    FeatureRequest(
                        url=s.url,
                        where=s.where or "1=1",
                        out_fields=s.out_fields or "*",
                        bbox=s.bbox,
                        out_epsg=is_epsg(s.crs),
                        token=args.token,
                    ),
                    out_path,
                    page_size=int(args.page_size),
                    overwrite=bool(args.overwrite),
                )
                entry = {
                    "id": s.id, "type": s.type, "title": s.title, "url": s.url,
                    "out": info, "source_file": str(jf)
                }
                print(f"[OK] feature {s.id} -> {info['path']}  size={info['size']}  pages={info['pages']}")
                manifest_entries.append(entry)

            else:
                print(f"[SKIP] unknown type: {s.type} in {jf}", file=sys.stderr)

        except Exception as e:
            failures += 1
            print(f"[FAIL] {jf}: {type(e).__name__}: {e}", file=sys.stderr)

    # Manifest
    manifest = {
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "elapsed_s": time.time() - t0,
        "out_dir": str(out_dir),
        "entries": manifest_entries,
    }
    write_json(args.manifest, manifest)
    print(f"[RESULT] ok={len(manifest_entries)}  fail={failures}  wrote manifest={args.manifest}")

    return 0 if failures == 0 else 2


if __name__ == "__main__":
    raise SystemExit(main())
