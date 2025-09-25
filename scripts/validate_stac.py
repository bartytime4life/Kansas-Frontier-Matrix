#!/usr/bin/env python3
"""
scripts/validate_stac.py
========================

Validate STAC JSON (Item, Collection, or Catalog):

- Strict JSON Schema (if `jsonschema` available) using your local schema loader or common filenames.
- Fallback minimal structural checks when `jsonschema`/schema is absent.
- Optional URL reachability (HEAD->GET fallback) for http(s) assets/links.
- Optional local file checks for relative/file:// assets/links.
- Optional bbox/temporal sanity checks (appropriate to kind).
- Emits a machine-readable report for MCP/CI.

Usage
-----
# Strict validation (schema), no network:
python scripts/validate_stac.py stac/**/*.json

# Plus URL checks:
python scripts/validate_stac.py stac/**/*.json --check-urls --jobs 12 --timeout 6

# Check that relative/file:// hrefs exist on disk:
python scripts/validate_stac.py stac/**/*.json --check-files

# Extra geometry/bbox sanity:
python scripts/validate_stac.py stac/**/*.json --check-geometry --check-bbox

# Write a report for CI artifacts:
python scripts/validate_stac.py stac/**/*.json --report data/validation/validate_stac.report.json
"""

from __future__ import annotations

import argparse
import concurrent.futures as cf
import glob
import json
import sys
import time
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Dict, Iterable, Iterator, List, Mapping, Optional, Sequence, Tuple
from urllib.request import Request, urlopen

# Optional: jsonschema + local package schema loader
HAS_JSONSCHEMA = False
try:
    import jsonschema  # type: ignore
    HAS_JSONSCHEMA = True
except Exception:
    HAS_JSONSCHEMA = False

KGT_HAS_SCHEMA = False
try:
    # Optional helper in your package; we guard it and fall back gracefully
    from kansas_geo_timeline import load_json_schema  # type: ignore
    KGT_HAS_SCHEMA = True
except Exception:
    KGT_HAS_SCHEMA = False

Json = Dict[str, Any]

# ---------------------------
# IO helpers
# ---------------------------

def _iter_inputs(patterns: Iterable[str]) -> Iterator[Path]:
    for pat in patterns:
        p = Path(pat)
        if p.is_dir():
            for f in sorted(p.rglob("*.json")):
                yield f
        else:
            for m in sorted(glob.glob(pat, recursive=True)):
                yield Path(m)


def _read_json(p: Path) -> Json:
    with p.open("r", encoding="utf-8") as f:
        return json.load(f)


# ---------------------------
# Kind detection
# ---------------------------

def detect_kind(doc: Mapping[str, Any]) -> str:
    """
    Returns one of: 'item', 'collection', 'catalog', or 'unknown'
    """
    t = doc.get("type")
    if t == "Feature":
        return "item"
    if t == "Collection":
        return "collection"
    if t == "Catalog":
        return "catalog"
    # Some Catalogs may omit 'type' (non-standard); infer if 'links' exists and 'stac_version' present
    if "stac_version" in doc and "links" in doc and "assets" not in doc and "extent" not in doc:
        return "catalog"
    return "unknown"


# ---------------------------
# Minimal structural checks per kind
# ---------------------------

def _is_num(x: Any) -> bool:
    try:
        float(x)
        return True
    except Exception:
        return False


def _bbox_valid(bbox: Sequence[float]) -> bool:
    # STAC allows 2D/3D/4D/6D etc., here we minimally check 2D lon/lat order ranges
    if len(bbox) < 4:
        return False
    w, s, e, n = bbox[:4]
    if not all(_is_num(v) for v in (w, s, e, n)):
        return False
    w, s, e, n = float(w), float(s), float(e), float(n)
    return (w <= e) and (s <= n) and (-180.0 <= w <= 180.0) and (-180.0 <= e <= 180.0) and (-90.0 <= s <= 90.0) and (-90.0 <= n <= 90.0)


def _temporal_rule_errors_item(props: Mapping[str, Any]) -> List[str]:
    """
    For Items: either properties.datetime is set (string), OR both start_datetime & end_datetime are strings.
    """
    errs: List[str] = []
    dt = props.get("datetime")
    sd = props.get("start_datetime")
    ed = props.get("end_datetime")
    dt_ok = isinstance(dt, str)
    rng_ok = isinstance(sd, str) and isinstance(ed, str)
    if not (dt_ok or rng_ok):
        errs.append("temporal: require either properties.datetime OR start_datetime & end_datetime (both strings)")
    return errs


def _minimal_item_errors(item: Mapping[str, Any]) -> List[str]:
    errs: List[str] = []
    req_top = ["stac_version", "id", "type", "geometry", "bbox", "properties", "links", "assets"]
    for k in req_top:
        if k not in item:
            errs.append(f"missing key: {k}")
    if item.get("type") != "Feature":
        errs.append("type must be 'Feature'")
    bbox = item.get("bbox")
    if not (isinstance(bbox, (list, tuple)) and len(bbox) >= 4 and all(_is_num(v) for v in bbox[:4])):
        errs.append("bbox must be array [west, south, east, north, ...] of numbers")
    props = item.get("properties")
    if not isinstance(props, Mapping):
        errs.append("properties must be an object")
    links = item.get("links")
    if not (isinstance(links, list) and links):
        errs.append("links must be a non-empty array")
    assets = item.get("assets")
    if not (isinstance(assets, Mapping) and assets):
        errs.append("assets must be a non-empty object")
    # geometry may be null for some raster items; require presence but not enforce non-null here
    if "geometry" not in item:
        errs.append("missing key: geometry")
    return errs


def _minimal_collection_errors(coll: Mapping[str, Any]) -> List[str]:
    errs: List[str] = []
    req_top = ["stac_version", "id", "type", "extent", "links"]
    for k in req_top:
        if k not in coll:
            errs.append(f"missing key: {k}")
    if coll.get("type") != "Collection":
        errs.append("type must be 'Collection'")
    extent = coll.get("extent", {})
    if not isinstance(extent, Mapping):
        errs.append("extent must be an object")
    else:
        spatial = extent.get("spatial", {})
        temporal = extent.get("temporal", {})
        if not isinstance(spatial, Mapping) or "bbox" not in spatial:
            errs.append("extent.spatial.bbox required")
        else:
            bboxes = spatial.get("bbox", [])
            if not (isinstance(bboxes, list) and bboxes and isinstance(bboxes[0], (list, tuple)) and _bbox_valid(bboxes[0])):
                errs.append("extent.spatial.bbox[0] invalid or out-of-range")
        if not isinstance(temporal, Mapping) or "interval" not in temporal:
            errs.append("extent.temporal.interval required")
        else:
            intervals = temporal.get("interval", [])
            if not (isinstance(intervals, list) and intervals and isinstance(intervals[0], (list, tuple)) and len(intervals[0]) == 2):
                errs.append("extent.temporal.interval must be [[start, end]]")
    links = coll.get("links")
    if not (isinstance(links, list) and links):
        errs.append("links must be a non-empty array")
    return errs


def _minimal_catalog_errors(cat: Mapping[str, Any]) -> List[str]:
    errs: List[str] = []
    req_top = ["stac_version", "id", "type", "links"]
    for k in req_top:
        if k not in cat:
            errs.append(f"missing key: {k}")
    if cat.get("type") != "Catalog":
        errs.append("type must be 'Catalog'")
    links = cat.get("links")
    if not (isinstance(links, list) and links):
        errs.append("links must be a non-empty array")
    return errs


# ---------------------------
# Href collection helpers
# ---------------------------

def _collect_asset_hrefs(item: Mapping[str, Any]) -> Tuple[List[str], List[str]]:
    """Return (http_urls, file_like_hrefs)"""
    http_urls: List[str] = []
    file_like: List[str] = []
    assets = item.get("assets", {})
    if isinstance(assets, Mapping):
        for a in assets.values():
            if isinstance(a, Mapping):
                href = a.get("href")
                if not isinstance(href, str):
                    continue
                if href.startswith(("http://", "https://")):
                    http_urls.append(href)
                else:
                    file_like.append(href)
    return http_urls, file_like


def _collect_link_hrefs(doc: Mapping[str, Any]) -> Tuple[List[str], List[str]]:
    http_urls: List[str] = []
    file_like: List[str] = []
    links = doc.get("links", [])
    if isinstance(links, list):
        for link in links:
            if isinstance(link, Mapping):
                href = link.get("href")
                if not isinstance(href, str):
                    continue
                if href.startswith(("http://", "https://")):
                    http_urls.append(href)
                else:
                    file_like.append(href)
    return http_urls, file_like


# ---------------------------
# URL checks (HEAD -> GET fallback)
# ---------------------------

@dataclass
class UrlStatus:
    url: str
    ok: bool
    code: Optional[int]
    elapsed_s: float
    error: Optional[str] = None


def _check_url(url: str, timeout: float) -> UrlStatus:
    t0 = time.time()
    try:
        req = Request(url, method="HEAD", headers={"User-Agent": "kgt-validate/1.0"})
        with urlopen(req, timeout=timeout) as resp:
            code = getattr(resp, "status", 200)
            return UrlStatus(url, int(code) < 400, int(code), time.time() - t0, None)
    except Exception as e:
        try:
            req = Request(url, method="GET", headers={"User-Agent": "kgt-validate/1.0"})
            with urlopen(req, timeout=timeout) as resp:
                code = getattr(resp, "status", 200)
                return UrlStatus(url, int(code) < 400, int(code), time.time() - t0, None)
        except Exception as e2:
            return UrlStatus(url, False, None, time.time() - t0, f"{type(e2).__name__}: {e2}")


# ---------------------------
# Local file checks
# ---------------------------

@dataclass
class FileHrefStatus:
    href: str
    ok: bool
    resolved: Optional[str]
    error: Optional[str] = None


def _resolve_file_href(base: Path, href: str) -> Path:
    if href.startswith("file://"):
        return Path(href[7:])
    href_p = Path(href)
    if href_p.is_absolute():
        return href_p
    return (base.parent / href_p).resolve()


def _check_local_hrefs(base: Path, hrefs: List[str]) -> List[FileHrefStatus]:
    out: List[FileHrefStatus] = []
    for href in hrefs:
        try:
            rp = _resolve_file_href(base, href)
            ok = rp.exists()
            out.append(FileHrefStatus(href=href, ok=ok, resolved=str(rp) if ok else None, error=None if ok else "missing"))
        except Exception as e:
            out.append(FileHrefStatus(href=href, ok=False, resolved=None, error=f"{type(e).__name__}: {e}"))
    return out


# ---------------------------
# Schema loading
# ---------------------------

def _load_schema_for_kind(kind: str, schema_arg: Optional[Path]) -> Optional[Mapping[str, Any]]:
    """
    Determine and load an appropriate schema:
      - If --schema is a file, load that file.
      - If --schema is a directory, try item.json / collection.json / catalog.json inside it.
      - Else, if kansas_geo_timeline.load_json_schema is available, try conventional names.
      - Else, return None (fallback to minimal checks).
    """
    candidates_files = {
        "item": ["item.json", "stac_item.schema.json", "item-spec/json-schema/item.json"],
        "collection": ["collection.json", "stac_collection.schema.json", "collection-spec/json-schema/collection.json"],
        "catalog": ["catalog.json", "stac_catalog.schema.json", "catalog-spec/json-schema/catalog.json"],
    }
    # Explicit file
    if schema_arg and schema_arg.is_file():
        with schema_arg.open("r", encoding="utf-8") as f:
            return json.load(f)
    # Directory of schemas
    if schema_arg and schema_arg.is_dir():
        for cand in candidates_files.get(kind, []):
            p = schema_arg / cand
            if p.exists():
                with p.open("r", encoding="utf-8") as f:
                    return json.load(f)
    # Package loader
    if KGT_HAS_SCHEMA:
        # Try a few conventional names per kind
        for cand in candidates_files.get(kind, []):
            try:
                sch = load_json_schema(cand)  # type: ignore
                if sch:
                    return sch
            except Exception:
                continue
    return None


# ---------------------------
# Validation per file
# ---------------------------

@dataclass
class FileReport:
    path: str
    kind: str
    valid: bool
    errors: List[str]
    warnings: List[str]
    assets_count: int
    links_count: int
    urls_checked: int
    urls_bad: int
    bad_url_samples: List[UrlStatus]
    file_hrefs_checked: int
    file_hrefs_bad: int
    bad_file_samples: List[FileHrefStatus]


def validate_doc(
    p: Path,
    *,
    schema_opt: Optional[Path],
    strict: bool,
    check_urls: bool,
    check_files: bool,
    check_geometry: bool,  # reserved
    check_bbox: bool,
    timeout: float,
    jobs: int
) -> FileReport:
    errors: List[str] = []
    warnings: List[str] = []

    try:
        doc = _read_json(p)
    except Exception as e:
        return FileReport(str(p), "unknown", False, [f"JSON parse failed: {e}"], [], 0, 0, 0, 0, [], 0, 0, [])

    kind = detect_kind(doc if isinstance(doc, Mapping) else {})
    if kind == "unknown":
        warnings.append("could not infer STAC kind; applying minimal Item checks as a fallback")
        kind = "item"

    # Strict-first schema validation
    if HAS_JSONSCHEMA and strict:
        try:
            schema = _load_schema_for_kind(kind, schema_opt)
            if schema is not None:
                validator = jsonschema.Draft202012Validator(schema)  # type: ignore[attr-defined]
                errs = sorted(validator.iter_errors(doc), key=lambda e: e.path)
                for e in errs:
                    where = "/".join(str(x) for x in e.path)
                    errors.append(f"{where}: {e.message}")
            else:
                warnings.append("schema: no STAC schema available; falling back to minimal checks")
        except Exception as e:
            errors.append(f"schema validation failed: {e}")
    else:
        if strict and not HAS_JSONSCHEMA:
            warnings.append("jsonschema not installed; minimal checks only")

    # Minimal checks (always run to catch useful issues even if schema passed)
    if isinstance(doc, Mapping):
        if kind == "item":
            errors.extend(_minimal_item_errors(doc))
            props = doc.get("properties", {}) or {}
            if isinstance(props, Mapping):
                errors.extend(_temporal_rule_errors_item(props))
            if check_bbox:
                bbox = doc.get("bbox", [])
                if not _bbox_valid(bbox if isinstance(bbox, (list, tuple)) else []):
                    errors.append("bbox: invalid or out-of-range")
        elif kind == "collection":
            errors.extend(_minimal_collection_errors(doc))
        elif kind == "catalog":
            errors.extend(_minimal_catalog_errors(doc))

    # Collect hrefs
    http_asset_urls, file_asset_hrefs = _collect_asset_hrefs(doc if isinstance(doc, Mapping) else {})
    http_link_urls, file_link_hrefs = _collect_link_hrefs(doc if isinstance(doc, Mapping) else {})
    urls = http_asset_urls + http_link_urls
    file_hrefs = file_asset_hrefs + file_link_hrefs

    # URL reachability
    bad_urls = 0
    bad_url_samples: List[UrlStatus] = []
    if check_urls and urls:
        with cf.ThreadPoolExecutor(max_workers=max(1, jobs)) as ex:
            futs = [ex.submit(_check_url, u, timeout) for u in urls]
            for fut in cf.as_completed(futs):
                st = fut.result()
                if not st.ok:
                    bad_urls += 1
                    if len(bad_url_samples) < 10:
                        bad_url_samples.append(st)

    # Local file existence checks
    file_bad = 0
    bad_file_samples: List[FileHrefStatus] = []
    file_checks: List[FileHrefStatus] = []
    if check_files and file_hrefs:
        res = _check_local_hrefs(p, file_hrefs)
        file_checks = res
        for r in res:
            if not r.ok:
                file_bad += 1
                if len(bad_file_samples) < 10:
                    bad_file_samples.append(r)

    valid = (len(errors) == 0) and (bad_urls == 0) and (file_bad == 0)
    return FileReport(
        path=str(p),
        kind=kind,
        valid=valid,
        errors=errors,
        warnings=warnings,
        assets_count=len(doc.get("assets", {})) if isinstance(doc, Mapping) and "assets" in doc else 0,
        links_count=len(doc.get("links", [])) if isinstance(doc, Mapping) and "links" in doc else 0,
        urls_checked=len(urls) if check_urls else 0,
        urls_bad=bad_urls,
        bad_url_samples=bad_url_samples,
        file_hrefs_checked=len(file_hrefs) if check_files else 0,
        file_hrefs_bad=file_bad,
        bad_file_samples=bad_file_samples,
    )


# ---------------------------
# CLI
# ---------------------------

@dataclass
class Summary:
    files_total: int
    files_valid: int
    files_invalid: int
    urls_checked: int
    urls_bad: int
    file_hrefs_checked: int
    file_hrefs_bad: int
    elapsed_s: float


def _build_argparser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(
        prog="validate_stac.py",
        description="Validate STAC JSON (Item, Collection, or Catalog)."
    )
    ap.add_argument("inputs", nargs="+", help="STAC files/dirs/globs to validate")
    ap.add_argument("--schema", type=Path, default=None,
                    help="Path to STAC schema (file or directory). If directory, tries item.json/collection.json/catalog.json.")
    ap.add_argument("--no-strict", action="store_true", help="Disable jsonschema strict validation (use minimal checks)")
    ap.add_argument("--check-urls", action="store_true", help="HEAD/GET http(s) asset & link URLs")
    ap.add_argument("--check-files", action="store_true", help="Check local/relative/file:// hrefs exist")
    ap.add_argument("--jobs", type=int, default=8, help="Concurrency for URL checks (default 8)")
    ap.add_argument("--timeout", type=float, default=8.0, help="HTTP timeout seconds (default 8.0)")
    ap.add_argument("--check-geometry", action="store_true", help="(Reserved) Geometry internal checks")
    ap.add_argument("--check-bbox", action="store_true", help="Validate bbox ranges (lon/lat order & limits)")
    ap.add_argument("--report", type=Path, default=Path("data/validation/validate_stac.report.json"),
                    help="Write JSON report")
    return ap


def main(argv: Optional[Sequence[str]] = None) -> int:
    ap = _build_argparser()
    args = ap.parse_args(argv)

    files = [p for p in _iter_inputs(args.inputs)]
    if not files:
        print("[WARN] No STAC files found.", file=sys.stderr)
        return 1

    t0 = time.time()
    reports: List[FileReport] = []
    totals = Summary(0, 0, 0, 0, 0, 0, 0, 0.0)

    for p in files:
        rep = validate_doc(
            p,
            schema_opt=args.schema,
            strict=not args.no_strict,
            check_urls=args.check_urls,
            check_files=args.check_files,
            check_geometry=args.check_geometry,
            check_bbox=args.check_bbox,
            timeout=args.timeout,
            jobs=args.jobs,
        )
        reports.append(rep)
        totals.files_total += 1
        if rep.valid:
            totals.files_valid += 1
            tag = "OK"
        else:
            totals.files_invalid += 1
            tag = "FAIL"

        totals.urls_checked += rep.urls_checked
        totals.urls_bad += rep.urls_bad
        totals.file_hrefs_checked += rep.file_hrefs_checked
        totals.file_hrefs_bad += rep.file_hrefs_bad

        print(f"[{tag}] {p}  kind={rep.kind}  assets={rep.assets_count}  links={rep.links_count}  "
              f"url_bad={rep.urls_bad}/{rep.urls_checked}  file_bad={rep.file_hrefs_bad}/{rep.file_hrefs_checked}")
        for e in rep.errors:
            print(f"   - ERR: {e}")
        for w in rep.warnings:
            print(f"   - WARN: {w}")
        for st in rep.bad_url_samples:
            print(f"   - URL BAD {st.code or '?'} {st.url} ({st.elapsed_s:.2f}s) {st.error or ''}")
        for fh in rep.bad_file_samples:
            print(f"   - FILE BAD {fh.href} -> {fh.resolved or '?'} {fh.error or ''}")

    totals.elapsed_s = time.time() - t0

    # Report
    rep_obj = {
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "inputs": [str(x) for x in args.inputs],
        "summary": asdict(totals),
        "files": [asdict(r) for r in reports],
        "environment": {
            "jsonschema": HAS_JSONSCHEMA,
            "kgt_schema_loader": KGT_HAS_SCHEMA,
        },
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    with args.report.open("w", encoding="utf-8") as f:
        json.dump(rep_obj, f, indent=2, sort_keys=True)
        f.write("\n")

    print(f"[RESULT] {totals.files_valid}/{totals.files_total} valid; "
          f"{totals.urls_bad}/{totals.urls_checked} bad URLs; "
          f"{totals.file_hrefs_bad}/{totals.file_hrefs_checked} bad file hrefs; "
          f"{totals.elapsed_s:.2f}s")

    # Exit non-zero if any invalid files or bad URLs/files
    return 0 if (totals.files_invalid == 0 and totals.urls_bad == 0 and totals.file_hrefs_bad == 0) else 2


if __name__ == "__main__":
    raise SystemExit(main())
