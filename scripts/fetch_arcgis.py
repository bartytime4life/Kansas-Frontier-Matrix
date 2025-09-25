#!/usr/bin/env python3
# scripts/fetch_arcgis.py
# -*- coding: utf-8 -*-
"""
Fetch ArcGIS ImageService / FeatureService layers to local files (robust, idempotent).

Improvements vs. prior:
- HTTP hardening: retries/backoff, optional POST, default timeout, ETag caching (If-None-Match)
- Imagery: chooses pixelSize or size automatically; tiles big requests; optional COG-translate via GDAL
- Features: resilient paging (dedup by objectIdField, resultOffset loop), optional bbox filter, outSR
- Safer outputs: atomic writes, SHA sidecars, JSON manifest; optional meta+COG validation hooks
- CLI ergonomics: --only, --post, --cog, --gdal-threads, --skip-existing, per-type defaults

Usage
-----
# Fetch every JSON descriptor in data/sources into data/raw
python scripts/fetch_arcgis.py --sources data/sources --out data/raw

# Fetch a single id from a folder
python scripts/fetch_arcgis.py --sources data/sources --out data/raw --only ks_hillshade

# Force POST, create COG from imagery via GDAL, add token and UA
python scripts/fetch_arcgis.py --sources data/sources --out data/raw \
  --post --cog --token "$TOKEN" --user-agent "kfm/1.1 (+github.com/..)"

JSON descriptors (examples)
---------------------------
Imagery (ImageServer):
{
  "id": "ks_hillshade",
  "type": "arcgis-imagery",
  "url": "https://.../ArcGIS/rest/services/KS/Hillshade/ImageServer",
  "format": "geotiff",                   # geotiff|tiff|png|jpg
  "bbox": [-102.05, 36.99, -94.59, 40.00],
  "pixel_size": 30,                      # meters
  "crs": "EPSG:4326"
}

Feature (FeatureServer/MapServer layer):
{
  "id": "rr_lines_1887",
  "type": "arcgis-feature",
  "url": "https://.../ArcGIS/rest/services/KS/railroads/FeatureServer/0",
  "where": "1=1",
  "bbox": [-102.05, 36.99, -94.59, 40.00],   # optional
  "crs": "EPSG:4326",
  "out_fields": "*"
}
"""
from __future__ import annotations

import argparse, hashlib, json, math, os, sys, time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Dict, Iterable, List, Mapping, Optional, Sequence, Tuple, Union

import requests
from requests.adapters import HTTPAdapter, Retry

# ---------- Types ----------
Json = Dict[str, Any]
PathLike = Union[str, os.PathLike[str]]

# ---------- Optional GDAL presence for COG translate ----------
import shutil, subprocess
GDAL_TRANSLATE = shutil.which("gdal_translate")
GDALINFO       = shutil.which("gdalinfo")

# ---------- HTTP session ----------
def _with_timeout(request_fn, timeout: float):
    def _wrapped(method, url, **kwargs):
        kwargs.setdefault("timeout", timeout)
        return request_fn(method, url, **kwargs)
    return _wrapped

def build_session(
    *,
    user_agent: Optional[str],
    retries: int,
    backoff: float,
    timeout: float,
) -> requests.Session:
    sess = requests.Session()
    retry = Retry(
        total=retries, read=retries, connect=retries,
        backoff_factor=backoff,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=frozenset({"GET","POST"}),
        raise_on_status=False,
    )
    adapter = HTTPAdapter(max_retries=retry, pool_connections=16, pool_maxsize=32)
    sess.mount("http://", adapter); sess.mount("https://", adapter)
    sess.headers.update({
        "Accept": "*/*",
        "User-Agent": user_agent or "kfm-fetch-arcgis/1.1",
    })
    sess.request = _with_timeout(sess.request, timeout)
    return sess

# ---------- IO / SHA / atomic ----------
def read_json(p: PathLike) -> Json:
    return json.loads(Path(p).read_text(encoding="utf-8"))

def write_bytes_atomic(p: PathLike, data: bytes) -> None:
    p = Path(p); p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(p.suffix + ".tmp")
    tmp.write_bytes(data); os.replace(tmp, p)

def write_text_atomic(p: PathLike, text: str) -> None:
    p = Path(p); p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(p.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8"); os.replace(tmp, p)

def write_json(p: PathLike, obj: Mapping[str, Any]) -> None:
    write_text_atomic(p, json.dumps(obj, indent=2, sort_keys=True, ensure_ascii=False) + "\n")

def sha256_file(p: PathLike, chunk: int = 1<<20) -> str:
    h = hashlib.sha256()
    with Path(p).open("rb") as f:
        for buf in iter(lambda: f.read(chunk), b""):
            h.update(buf)
    return h.hexdigest()

def sidecar_sha(path: PathLike, sha: str) -> None:
    Path(f"{path}.sha256").write_text(sha + "\n", encoding="utf-8")

# ---------- utils ----------
def is_epsg(code: Optional[str]) -> Optional[int]:
    try:
        if not code: return None
        code = code.strip().upper()
        if code.startswith("EPSG:"): return int(code.split(":",1)[1])
        return int(code)
    except Exception:
        return None

def estimate_pixels(bbox: Sequence[float], pixel_size_m: float) -> Tuple[int,int]:
    minx, miny, maxx, maxy = bbox
    lat_m = (maxy-miny)*111_000.0
    midlat = 0.5*(miny+maxy)
    lon_m = (maxx-minx)*111_000.0*math.cos(math.radians(midlat))
    return max(1, round(lon_m/pixel_size_m)), max(1, round(lat_m/pixel_size_m))

def split_bbox(bbox: Sequence[float], nx: int, ny: int) -> List[List[float]]:
    minx, miny, maxx, maxy = bbox
    dx = (maxx-minx)/nx; dy = (maxy-miny)/ny
    tiles=[]
    for j in range(ny):
        y0=miny+j*dy; y1=y0+dy
        for i in range(nx):
            x0=minx+i*dx; x1=x0+dx
            tiles.append([x0,y0,x1,y1])
    return tiles

def safe_name(s: str) -> str:
    return "".join(ch if ch.isalnum() or ch in "-_." else "_" for ch in s)

# ---------- models ----------
@dataclass
class ImageryRequest:
    url: str
    bbox: List[float]
    bbox_epsg: int
    image_epsg: int
    pixel_size: float
    fmt: str             # tiff|png|jpg
    token: Optional[str] = None
    use_post: bool = False

@dataclass
class FeatureRequest:
    url: str
    where: str = "1=1"
    out_fields: str = "*"
    bbox: Optional[List[float]] = None
    out_epsg: Optional[int] = None
    token: Optional[str] = None
    use_post: bool = False

# ---------- imagery ----------
def export_imagery(
    sess: requests.Session,
    req: ImageryRequest,
    out_path: Path,
    *,
    max_dim: int,
    overwrite: bool,
    etag_cache: bool,
    build_cog: bool,
    gdal_threads: str,
) -> Dict[str, Any]:
    out_path.parent.mkdir(parents=True, exist_ok=True)

    fmt = req.fmt.lower()
    if fmt in ("geotiff","tiff","tif"): img_format, ext = "tiff", "tif"
    elif fmt in ("png","jpg","jpeg"):   img_format, ext = (fmt, "jpg" if fmt=="jpeg" else fmt)
    else: raise ValueError(f"Unsupported imagery format: {req.fmt}")

    # Idempotency + ETag cache
    headers = {}
    etag_file = out_path.with_suffix(out_path.suffix + ".etag")
    if etag_cache and etag_file.exists():
        headers["If-None-Match"] = etag_file.read_text(encoding="utf-8").strip()

    # Short-circuit existing
    if out_path.exists() and not overwrite and not etag_cache:
        sha = sha256_file(out_path); sidecar_sha(out_path, sha)
        return {"path": str(out_path), "size": out_path.stat().st_size, "sha256": sha, "tiled": False}

    est_w, est_h = estimate_pixels(req.bbox, req.pixel_size)
    if max(est_w, est_h) <= max_dim:
        tiles = [req.bbox]
    else:
        nx = math.ceil(est_w / max_dim); ny = math.ceil(est_h / max_dim)
        tiles = split_bbox(req.bbox, nx, ny)

    total_size = 0
    chunk_paths: List[Path] = []

    def do_request(bbox: List[float], w: int, h: int) -> bytes:
        params = {
            "bbox": ",".join(map(str, bbox)),
            "bboxSR": req.bbox_epsg,
            "imageSR": req.image_epsg,
            "format": img_format,
            "f": "image",
        }
        # Prefer pixelSize when available; keep size fallback for servers that require it.
        # Note: some servers reject pixelSize with tiff+georeference; size is safer.
        params["size"] = f"{min(w, max_dim)},{min(h, max_dim)}"
        # Using pixelSizeMeters could be possible for some deployments:
        # params["pixelSize"] = req.pixel_size

        if req.token: params["token"] = req.token
        url = req.url.rstrip("/") + "/exportImage"

        if req.use_post:
            r = sess.post(url, data=params, headers=headers)
        else:
            r = sess.get(url, params=params, headers=headers)

        if r.status_code == 304:  # Not modified (ETag hit)
            return b"__ETAG_NOT_MODIFIED__"

        ctype = r.headers.get("Content-Type","").lower()
        if "application/json" in ctype or "text/json" in ctype:
            try:
                err = r.json()
                raise RuntimeError(f"exportImage error: {err}")
            except Exception:
                r.raise_for_status()
        r.raise_for_status()
        # persist ETag for next runs
        if etag_cache and (etag := r.headers.get("ETag")):
            etag_file.write_text(etag.strip(), encoding="utf-8")
        return r.content

    for idx, b in enumerate(tiles):
        tw, th = estimate_pixels(b, req.pixel_size)
        blob = do_request(b, tw, th)
        if blob == b"__ETAG_NOT_MODIFIED__":
            # nothing to write; keep the existing file(s)
            continue

        if len(tiles) == 1:
            write_bytes_atomic(out_path, blob)
            total_size = len(blob)
        else:
            chunk = out_path.with_name(out_path.stem + f".chunk{idx:03d}." + ext)
            write_bytes_atomic(chunk, blob)
            chunk_paths.append(chunk)
            total_size += len(blob)

    # sidecars / index
    if len(tiles) == 1:
        sha = sha256_file(out_path); sidecar_sha(out_path, sha)
        result = {"path": str(out_path), "size": total_size, "sha256": sha, "tiled": False, "tiles": []}
    else:
        index = {"base": out_path.name, "format": ext, "tiles": [p.name for p in chunk_paths]}
        index_path = out_path.with_suffix(out_path.suffix + ".tiles.json")
        write_json(index_path, index)
        for p in chunk_paths: sidecar_sha(p, sha256_file(p))
        sha = sha256_file(index_path); sidecar_sha(index_path, sha)
        result = {"path": str(out_path), "size": total_size, "sha256": sha, "tiled": True, "tiles": [str(p) for p in chunk_paths]}

    # Optional: COG translate single-tile imagers to COG (in-place path selection)
    if build_cog and GDAL_TRANSLATE and len(tiles) == 1 and out_path.suffix.lower() in {".tif",".tiff"}:
        cog_out = out_path.with_suffix(".cog.tif")
        cmd = [
            GDAL_TRANSLATE, str(out_path), str(cog_out),
            "-of", "COG",
            "-co", "COMPRESS=DEFLATE", "-co", "PREDICTOR=2", "-co", "ZLEVEL=6",
            "-co", "BLOCKSIZE=512", "-co", f"NUM_THREADS={gdal_threads}",
            "-co", "OVERVIEWS=AUTO", "-co", "OVERVIEW_RESAMPLING=AVERAGE", "-co", "BIGTIFF=IF_SAFER",
        ]
        subprocess.run(cmd, check=True, text=True)
        if GDALINFO:
            try: subprocess.check_output([GDALINFO, "-stats", str(cog_out)], text=True)
            except Exception: pass
        sha2 = sha256_file(cog_out); sidecar_sha(cog_out, sha2)
        result["cog_path"] = str(cog_out); result["cog_sha256"] = sha2

    return result

# ---------- features ----------
def export_features(
    sess: requests.Session,
    req: FeatureRequest,
    out_path: Path,
    *,
    page_size: int,
    overwrite: bool,
) -> Dict[str, Any]:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    if out_path.exists() and not overwrite:
        sha = sha256_file(out_path); sidecar_sha(out_path, sha)
        return {"path": str(out_path), "size": out_path.stat().st_size, "sha256": sha, "pages": 0}

    # layer metadata
    meta_url = req.url if req.url.endswith("?f=json") else (req.url + ("&" if "?" in req.url else "?") + "f=json")
    if req.token: meta_url += f"&token={req.token}"
    meta = requests.get(meta_url, timeout=30).json()
    oid_field = meta.get("objectIdField", meta.get("objectIdFieldName", "OBJECTID"))

    features: List[Json] = []
    seen_oids = set()
    offset = 0; pages = 0

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
            params.update({
                "geometry": ",".join(map(str, req.bbox)),
                "geometryType": "esriGeometryEnvelope",
                "inSR": 4326,  # bbox always assumed WGS84 in our descriptors
                "spatialRel": "esriSpatialRelIntersects",
            })
        if req.out_epsg: params["outSR"] = req.out_epsg
        if req.token:    params["token"] = req.token

        url = req.url.rstrip("/") + "/query"
        r = sess.post(url, data=params) if req.use_post else sess.get(url, params=params)

        # Some servers reply 200 with error JSON
        try:
            obj = r.json()
            if isinstance(obj, dict) and obj.get("error"):
                raise RuntimeError(obj["error"])
        except ValueError:
            r.raise_for_status()
            obj = r.json()

        feats = obj.get("features", [])
        if not feats: break

        for f in feats:
            props = f.get("properties") or f.get("attributes") or {}
            oid = None
            if isinstance(props, dict):
                oid = props.get(oid_field)
            if oid is None or oid not in seen_oids:
                features.append(f)
                if oid is not None: seen_oids.add(oid)

        pages += 1; offset += page_size

    fc = {"type": "FeatureCollection", "features": features}
    write_json(out_path, fc)
    sha = sha256_file(out_path); sidecar_sha(out_path, sha)
    return {"path": str(out_path), "size": out_path.stat().st_size, "sha256": sha, "pages": pages}

# ---------- source discovery ----------
def list_sources(sources: Sequence[str]) -> List[Path]:
    out: List[Path] = []
    for s in sources:
        p = Path(s)
        if p.is_dir():  out.extend(sorted(p.glob("*.json")))
        elif p.is_file(): out.append(p)
    return out

# ---------- CLI ----------
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
    miss = [k for k in ("id","type","url") if k not in s]
    if miss: raise ValueError(f"{p}: missing required keys: {miss}")
    return Source(
        id=s["id"], type=s["type"], url=s["url"],
        title=s.get("title"), format=s.get("format"),
        bbox=s.get("bbox"), pixel_size=s.get("pixel_size"),
        crs=s.get("crs"), where=s.get("where"), out_fields=s.get("out_fields"),
    )

def try_meta_sidecar(path: Path, inputs: List[str], **extra):
    wm = Path(__file__).with_name("write_meta.py")
    if wm.exists():
        try:
            extras = sum(([f"{k}={v}"] for k,v in extra.items()), [])
            subprocess.run([sys.executable, str(wm), str(path), "--inputs", *inputs, "--extra", *extras],
                           check=True, text=True)
        except Exception as e:
            print(f"[WARN] meta sidecar skipped: {e}")

def try_validate_cog(path: Path):
    val = Path(__file__).with_name("validate_cogs.py")
    if val.exists() and path.suffix.lower() in {".tif",".tiff"}:
        try:
            subprocess.run([sys.executable, str(val), str(path.parent), "--pattern", path.name, "--quiet"],
                           check=False, text=True)
        except Exception as e:
            print(f"[WARN] COG validate skipped: {e}")

def main(argv: Optional[Sequence[str]] = None) -> int:
    ap = argparse.ArgumentParser(description="Fetch ArcGIS ImageService/FeatureService layers to local files.")
    ap.add_argument("--sources", nargs="+", required=True, help="Folder(s) and/or JSON file(s)")
    ap.add_argument("--out", required=True, help="Output directory")
    ap.add_argument("--only", default=None, help="Only fetch a single 'id' (matches JSON 'id')")
    ap.add_argument("--token", default=os.getenv("ARCGIS_TOKEN"), help="ArcGIS token (env ARCGIS_TOKEN default)")
    ap.add_argument("--user-agent", default=None, help="Custom User-Agent")
    ap.add_argument("--post", action="store_true", help="Use POST for requests (some servers prefer)")
    ap.add_argument("--max-dim", type=int, default=4096, help="Max tile dimension for imagery")
    ap.add_argument("--page-size", type=int, default=5000, help="Feature page size")
    ap.add_argument("--retries", type=int, default=4, help="HTTP retries")
    ap.add_argument("--backoff", type=float, default=0.5, help="HTTP backoff factor")
    ap.add_argument("--timeout", type=float, default=60.0, help="HTTP timeout seconds")
    ap.add_argument("--overwrite", action="store_true", help="Overwrite existing files")
    ap.add_argument("--skip-existing", action="store_true", help="Skip if output file exists (overrides ETag check)")
    ap.add_argument("--etag-cache", action="store_true", help="Cache and honor ETag for idempotent re-runs")
    ap.add_argument("--cog", action="store_true", help="If single-tile GeoTIFF, also write a COG via gdal_translate")
    ap.add_argument("--gdal-threads", default="ALL_CPUS", help="NUM_THREADS for GDAL translate")
    ap.add_argument("--manifest", default="data/raw/manifest.arcgis.json", help="Manifest output path")
    args = ap.parse_args(argv)

    out_dir = Path(args.out); out_dir.mkdir(parents=True, exist_ok=True)
    sess = build_session(user_agent=args.user_agent, retries=args.retries, backoff=args.backoff, timeout=args.timeout)

    src_files = list_sources(args.sources)
    if not src_files:
        print("[WARN] no source JSON files found", file=sys.stderr); return 1

    entries: List[Json] = []; failures = 0; t0 = time.time()

    for jf in src_files:
        try:
            s = parse_source(jf)
            if args.only and s.id != args.only: continue

            if s.type == "arcgis-imagery":
                if not s.bbox or not s.pixel_size:
                    raise ValueError(f"{jf}: imagery requires 'bbox' and 'pixel_size'")
                epsg = is_epsg(s.crs) or 4326
                fmt  = (s.format or "geotiff").lower()
                out_ext = "tif" if fmt in ("geotiff","tiff") else (fmt if fmt!="jpeg" else "jpg")
                out_path = out_dir / f"{safe_name(s.id)}.{out_ext}"

                if args.skip_existing and out_path.exists() and not args.overwrite:
                    sha = sha256_file(out_path); sidecar_sha(out_path, sha)
                    entries.append({"id": s.id, "type": s.type, "title": s.title, "url": s.url,
                                    "out": {"path": str(out_path), "size": out_path.stat().st_size, "sha256": sha,
                                            "tiled": False}, "source_file": str(jf)})
                    print(f"[SKIP] imagery {s.id} (exists)")
                    continue

                info = export_imagery(
                    sess,
                    ImageryRequest(
                        url=s.url, bbox=s.bbox, bbox_epsg=4326, image_epsg=epsg,
                        pixel_size=float(s.pixel_size), fmt=fmt, token=args.token, use_post=args.post,
                    ),
                    out_path,
                    max_dim=int(args.max_dim), overwrite=bool(args.overwrite),
                    etag_cache=bool(args.etag_cache), build_cog=bool(args.cog),
                    gdal_threads=args.gdal_threads,
                )
                entries.append({"id": s.id, "type": s.type, "title": s.title, "url": s.url,
                                "out": info, "source_file": str(jf)})
                print(f"[OK] imagery {s.id} -> {info['path']} size={info['size']} tiled={info['tiled']}")
                if "cog_path" in info:
                    print(f"     COG -> {info['cog_path']}")

                # provenance + validate (best-effort)
                try_meta_sidecar(Path(info["path"]), [jf])
                if "cog_path" in info: try_validate_cog(Path(info["cog_path"]))

            elif s.type == "arcgis-feature":
                out_path = out_dir / f"{safe_name(s.id)}.geojson"
                if args.skip_existing and out_path.exists() and not args.overwrite:
                    sha = sha256_file(out_path); sidecar_sha(out_path, sha)
                    entries.append({"id": s.id, "type": s.type, "title": s.title, "url": s.url,
                                    "out": {"path": str(out_path), "size": out_path.stat().st_size, "sha256": sha,
                                            "pages": 0}, "source_file": str(jf)})
                    print(f"[SKIP] feature {s.id} (exists)")
                    continue

                info = export_features(
                    sess,
                    FeatureRequest(
                        url=s.url, where=s.where or "1=1", out_fields=s.out_fields or "*",
                        bbox=s.bbox, out_epsg=is_epsg(s.crs), token=args.token, use_post=args.post
                    ),
                    out_path,
                    page_size=int(args.page_size), overwrite=bool(args.overwrite),
                )
                entries.append({"id": s.id, "type": s.type, "title": s.title, "url": s.url,
                                "out": info, "source_file": str(jf)})
                print(f"[OK] feature {s.id} -> {info['path']} size={info['size']} pages={info['pages']}")
                try_meta_sidecar(Path(info["path"]), [jf])

            else:
                print(f"[SKIP] unknown type: {s.type} in {jf}", file=sys.stderr)

        except Exception as e:
            failures += 1
            print(f"[FAIL] {jf}: {type(e).__name__}: {e}", file=sys.stderr)

    manifest = {
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "elapsed_s": round(time.time()-t0, 3),
        "out_dir": str(out_dir),
        "entries": entries,
        "failures": failures,
    }
    write_json(args.manifest, manifest)
    print(f"[RESULT] ok={len(entries)} fail={failures} manifest={args.manifest}")
    return 0 if failures == 0 else 2

if __name__ == "__main__":
    raise SystemExit(main())
