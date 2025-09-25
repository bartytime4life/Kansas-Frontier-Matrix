#!/usr/bin/env python3
"""
scripts/validate_sources.py
===========================

Validate JSON source catalogs (data/sources/*.json) **and** STAC JSON
(Items, Collections, Catalogs) for basic structure, provenance, and
(optional) URL/local-file reachability.

Goals
-----
- Pure stdlib (no hard deps). If available:
  * jsonschema : strict schema validation.
  * kansas_geo_timeline.load_json_schema : schema resolver.
- Fast, concurrent URL checks (HEAD -> GET fallback).
- Optional local file checks for relative/file:// hrefs.
- MCP traceability: emits a machine-readable report/manifest.

Usage
-----
# Validate both sources and STAC, no network
python scripts/validate_sources.py data/sources/*.json stac/**/*.json

# Also check that URLs respond (HEAD/GET)
python scripts/validate_sources.py data/sources/*.json --check-urls --jobs 8 --timeout 10

# Check relative/file:// hrefs exist on disk
python scripts/validate_sources.py stac/**/*.json --check-files

# Fail CI if any error; write report
python scripts/validate_sources.py stac/**/*.json --report data/validation/validate_sources.report.json
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

# -------------------------
# Optional schema helpers
# -------------------------
HAS_JSONSCHEMA = False
try:
    import jsonschema  # type: ignore
    HAS_JSONSCHEMA = True
except Exception:
    HAS_JSONSCHEMA = False

KGT_HAS_SCHEMA = False
try:
    from kansas_geo_timeline import load_json_schema  # type: ignore
    KGT_HAS_SCHEMA = True
except Exception:
    KGT_HAS_SCHEMA = False

Json = Dict[str, Any]

# -------------------------
# Files / IO
# -------------------------
def _iter_inputs(patterns: Iterable[str]) -> Iterator[Path]:
    for pat in patterns:
        p = Path(pat)
        if p.is_dir():
            yield from sorted(p.rglob("*.json"))
        else:
            for m in sorted(glob.glob(pat, recursive=True)):
                yield Path(m)

def _read_json(p: Path) -> Json:
    with p.open("r", encoding="utf-8") as f:
        return json.load(f)

# -------------------------
# Kind detection
# -------------------------
def detect_kind(doc: Mapping[str, Any]) -> str:
    """
    Returns one of:
      'stac_item' | 'stac_collection' | 'stac_catalog' | 'source' | 'unknown'
    """
    t = doc.get("type")
    if t == "Feature":
        return "stac_item"
    if t == "Collection":
        return "stac_collection"
    if t == "Catalog":
        return "stac_catalog"
    # treat catalog if stac_version+links present and no extent/assets typical of collection/item
    if "stac_version" in doc and "links" in doc and "assets" not in doc and "extent" not in doc:
        return "stac_catalog"
    # sources/*.json: common fields → id/title/type + endpoint(s)
    if all(k in doc for k in ("id", "title", "type")) and any(k in doc for k in ("endpoint", "endpoints", "urls")):
        return "source"
    return "unknown"

# -------------------------
# Helpers
# -------------------------
def _is_url(s: Any) -> bool:
    return isinstance(s, str) and s.startswith(("http://", "https://"))

def _is_num(x: Any) -> bool:
    try:
        float(x)
        return True
    except Exception:
        return False

def _bbox_valid(bbox: Sequence[float]) -> bool:
    if len(bbox) < 4:
        return False
    w, s, e, n = bbox[:4]
    if not all(_is_num(v) for v in (w, s, e, n)):
        return False
    w, s, e, n = float(w), float(s), float(e), float(n)
    return (w <= e) and (s <= n) and (-180 <= w <= 180) and (-180 <= e <= 180) and (-90 <= s <= 90) and (-90 <= n <= 90)

# -------------------------
# Minimal structural checks
# -------------------------
def _min_stac_item(item: Mapping[str, Any]) -> List[str]:
    req = ["stac_version", "id", "type", "geometry", "bbox", "properties", "links", "assets"]
    errs: List[str] = []
    for k in req:
        if k not in item:
            errs.append(f"missing key: {k}")
    if item.get("type") != "Feature":
        errs.append("type must be 'Feature'")
    bbox = item.get("bbox")
    if not (isinstance(bbox, (list, tuple)) and len(bbox) >= 4):
        errs.append("bbox must be [west, south, east, north, ...]")
    props = item.get("properties")
    if not isinstance(props, Mapping):
        errs.append("properties must be an object")
    assets = item.get("assets")
    if not isinstance(assets, Mapping) or not assets:
        errs.append("assets must be a non-empty object")
    # temporal: datetime OR (start_datetime & end_datetime)
    if isinstance(props, Mapping):
        dt = props.get("datetime")
        sd = props.get("start_datetime")
        ed = props.get("end_datetime")
        if not (isinstance(dt, str) or (isinstance(sd, str) and isinstance(ed, str))):
            errs.append("temporal: require properties.datetime OR start_datetime & end_datetime")
    return errs

def _min_stac_collection(coll: Mapping[str, Any]) -> List[str]:
    errs: List[str] = []
    req = ["stac_version", "id", "type", "extent", "links"]
    for k in req:
        if k not in coll:
            errs.append(f"missing key: {k}")
    if coll.get("type") != "Collection":
        errs.append("type must be 'Collection'")
    extent = coll.get("extent")
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
                errs.append("extent.spatial.bbox[0] invalid")
        if not isinstance(temporal, Mapping) or "interval" not in temporal:
            errs.append("extent.temporal.interval required")
    links = coll.get("links", [])
    if not (isinstance(links, list) and links):
        errs.append("links must be a non-empty array")
    return errs

def _min_stac_catalog(cat: Mapping[str, Any]) -> List[str]:
    errs: List[str] = []
    req = ["stac_version", "id", "type", "links"]
    for k in req:
        if k not in cat:
            errs.append(f"missing key: {k}")
    if cat.get("type") != "Catalog":
        errs.append("type must be 'Catalog'")
    if not (isinstance(cat.get("links"), list) and cat["links"]):
        errs.append("links must be a non-empty array")
    return errs

def _min_source(src: Mapping[str, Any]) -> List[str]:
    """
    Lenient but useful checks for data/sources/*.json
    Expected: id, title, type, endpoint(s)/urls, optional spatial/temporal/license/providers/outputs
    """
    errs: List[str] = []
    for k in ("id", "title", "type"):
        if k not in src:
            errs.append(f"missing key: {k}")
    # endpoints
    if "endpoint" not in src and "endpoints" not in src and "urls" not in src:
        errs.append("missing endpoint(s)/urls")
    # spatial bbox if provided
    spatial = src.get("spatial")
    if isinstance(spatial, Mapping) and "bbox" in spatial:
        bbox = spatial.get("bbox")
        if not (isinstance(bbox, (list, tuple)) and len(bbox) >= 4 and _bbox_valid(bbox)):
            errs.append("spatial.bbox invalid or out-of-range")
    # license / providers are recommended (warn level)
    if "license" not in src:
        errs.append("warn: license not declared")
    if not any(k in src for k in ("providers", "source", "citation")):
        errs.append("warn: provider/citation not declared")
    return errs

# -------------------------
# Href/URL collection
# -------------------------
def _collect_item_hrefs(doc: Mapping[str, Any]) -> Tuple[List[str], List[str]]:
    """Return (http_urls, file_like_hrefs) from STAC Item assets and links."""
    http_urls: List[str] = []
    file_like: List[str] = []
    # assets
    assets = doc.get("assets", {})
    if isinstance(assets, Mapping):
        for a in assets.values():
            if isinstance(a, Mapping):
                href = a.get("href")
                if isinstance(href, str):
                    if _is_url(href):
                        http_urls.append(href)
                    else:
                        file_like.append(href)
    # links
    links = doc.get("links", [])
    if isinstance(links, list):
        for l in links:
            if isinstance(l, Mapping):
                href = l.get("href")
                if isinstance(href, str):
                    if _is_url(href):
                        http_urls.append(href)
                    else:
                        file_like.append(href)
    return http_urls, file_like

def _collect_source_hrefs(doc: Mapping[str, Any]) -> Tuple[List[str], List[str]]:
    """
    For sources:
      - endpoint(s): {"type":"http", "urls":[...]} or {"type":"http","url": "..."} etc.
      - urls: top-level list
      - assets: [{"href": "..."}] allowance
    """
    http_urls: List[str] = []
    file_like: List[str] = []

    # endpoints / endpoint
    for key in ("endpoints", "endpoint"):
        ep = doc.get(key)
        if isinstance(ep, Mapping):
            ep = [ep]
        if isinstance(ep, list):
            for e in ep:
                if not isinstance(e, Mapping):
                    continue
                etype = e.get("type")
                # collect URLs
                # 'urls' array
                if isinstance(e.get("urls"), list):
                    for u in e["urls"]:
                        if isinstance(u, str):
                            if _is_url(u) or u.startswith("file://"):
                                http_urls.append(u) if _is_url(u) else file_like.append(u)
                # single 'url'
                u = e.get("url")
                if isinstance(u, str):
                    if _is_url(u) or u.startswith("file://"):
                        http_urls.append(u) if _is_url(u) else file_like.append(u)
                # Some sources may embed direct asset href under endpoint
                href = e.get("href")
                if isinstance(href, str):
                    if _is_url(href):
                        http_urls.append(href)
                    else:
                        file_like.append(href)

    # top-level 'urls'
    if isinstance(doc.get("urls"), list):
        for u in doc["urls"]:
            if isinstance(u, str):
                if _is_url(u):
                    http_urls.append(u)
                elif u.startswith("file://"):
                    file_like.append(u)

    # catalog-like assets array
    if isinstance(doc.get("assets"), list):
        for a in doc["assets"]:
            if isinstance(a, Mapping):
                href = a.get("href")
                if isinstance(href, str):
                    if _is_url(href):
                        http_urls.append(href)
                    else:
                        file_like.append(href)

    # de-dup stable
    def _dedup(seq: List[str]) -> List[str]:
        seen = set()
        out: List[str] = []
        for x in seq:
            if x not in seen:
                seen.add(x)
                out.append(x)
        return out

    return _dedup(http_urls), _dedup(file_like)

# -------------------------
# URL / file checks
# -------------------------
@dataclass
class UrlStatus:
    url: str
    ok: bool
    code: Optional[int]
    elapsed_s: float
    error: Optional[str] = None

def _head_or_get(url: str, timeout: float) -> UrlStatus:
    t0 = time.time()
    try:
        req = Request(url, method="HEAD", headers={"User-Agent": "kfm-validate/1.0"})
        with urlopen(req, timeout=timeout) as resp:
            code = getattr(resp, "status", 200)
            return UrlStatus(url, int(code) < 400, int(code), time.time() - t0, None)
    except Exception:
        try:
            req = Request(url, method="GET", headers={"User-Agent": "kfm-validate/1.0"})
            with urlopen(req, timeout=timeout) as resp:
                code = getattr(resp, "status", 200)
                return UrlStatus(url, int(code) < 400, int(code), time.time() - t0, None)
        except Exception as e2:
            return UrlStatus(url, False, None, time.time() - t0, f"{type(e2).__name__}: {e2}")

@dataclass
class FileHrefStatus:
    href: str
    ok: bool
    resolved: Optional[str]
    error: Optional[str] = None

def _resolve_file_href(base: Path, href: str) -> Path:
    if href.startswith("file://"):
        return Path(href[7:])
    p = Path(href)
    return p if p.is_absolute() else (base.parent / p).resolve()

def _check_local_hrefs(base: Path, hrefs: List[str]) -> List[FileHrefStatus]:
    out: List[FileHrefStatus] = []
    for href in hrefs:
        try:
            rp = _resolve_file_href(base, href)
            ok = rp.exists()
            out.append(FileHrefStatus(href, ok, str(rp) if ok else None, None if ok else "missing"))
        except Exception as e:
            out.append(FileHrefStatus(href, False, None, f"{type(e).__name__}: {e}"))
    return out

# -------------------------
# Schema resolution
# -------------------------
def _load_schema(kind: str, schema_arg: Optional[Path]) -> Optional[Mapping[str, Any]]:
    """
    kind: stac_item|stac_collection|stac_catalog
    """
    candidates = {
        "stac_item": ["item.json", "stac_item.schema.json", "item-spec/json-schema/item.json"],
        "stac_collection": ["collection.json", "stac_collection.schema.json", "collection-spec/json-schema/collection.json"],
        "stac_catalog": ["catalog.json", "stac_catalog.schema.json", "catalog-spec/json-schema/catalog.json"],
    }
    # explicit file
    if schema_arg and schema_arg.is_file():
        with schema_arg.open("r", encoding="utf-8") as f:
            return json.load(f)
    # directory of schemas
    if schema_arg and schema_arg.is_dir():
        for name in candidates.get(kind, []):
            p = schema_arg / name
            if p.exists():
                with p.open("r", encoding="utf-8") as f:
                    return json.load(f)
    # package loader
    if KGT_HAS_SCHEMA:
        for name in candidates.get(kind, []):
            try:
                sch = load_json_schema(name)  # type: ignore
                if sch:
                    return sch
            except Exception:
                continue
    return None

# -------------------------
# Reports
# -------------------------
@dataclass
class FileReport:
    path: str
    kind: str
    valid: bool
    errors: List[str]
    http_urls_checked: int
    http_urls_bad: int
    bad_url_samples: List[UrlStatus]
    file_hrefs_checked: int
    file_hrefs_bad: int
    bad_file_samples: List[FileHrefStatus]

@dataclass
class Summary:
    files_total: int
    files_valid: int
    files_invalid: int
    http_urls_checked: int
    http_urls_bad: int
    file_hrefs_checked: int
    file_hrefs_bad: int
    elapsed_s: float

# -------------------------
# Validation
# -------------------------
def validate_file(
    p: Path,
    *,
    check_urls: bool,
    check_files: bool,
    timeout: float,
    jobs: int,
    schema_path_opt: Optional[Path]
) -> FileReport:
    errors: List[str] = []
    bad_url_samples: List[UrlStatus] = []
    bad_file_samples: List[FileHrefStatus] = []
    http_urls_checked = http_urls_bad = 0
    file_hrefs_checked = file_hrefs_bad = 0

    try:
        doc = _read_json(p)
    except Exception as e:
        return FileReport(str(p), "unknown", False, [f"JSON parse failed: {e}"], 0, 0, [], 0, 0, [])

    kind = detect_kind(doc if isinstance(doc, Mapping) else {})
    if kind == "unknown":
        errors.append("could not infer kind (source/STAC); expected object with known keys")
        return FileReport(str(p), kind, False, errors, 0, 0, [], 0, 0, [])

    # Schema validation for STAC kinds (if available)
    if HAS_JSONSCHEMA and kind in ("stac_item", "stac_collection", "stac_catalog"):
        try:
            schema = _load_schema(kind, schema_path_opt)
            if schema:
                validator = jsonschema.Draft202012Validator(schema)  # type: ignore[attr-defined]
                errs = sorted(validator.iter_errors(doc), key=lambda e: e.path)
                for e in errs:
                    where = "/".join(str(x) for x in e.path)
                    errors.append(f"{where}: {e.message}")
        except Exception as e:
            errors.append(f"schema validation failed: {e}")
    else:
        # minimal structural checks
        if kind == "stac_item":
            errors.extend(_min_stac_item(doc))
        elif kind == "stac_collection":
            errors.extend(_min_stac_collection(doc))
        elif kind == "stac_catalog":
            errors.extend(_min_stac_catalog(doc))
        elif kind == "source":
            errors.extend(_min_source(doc))

    # Harvest hrefs/URLs
    http_urls: List[str] = []
    file_hrefs: List[str] = []

    if kind == "stac_item":
        u, f = _collect_item_hrefs(doc)
        http_urls.extend(u); file_hrefs.extend(f)
    elif kind in ("stac_collection", "stac_catalog"):
        # Only check links for http/file (collections rarely have assets)
        links = doc.get("links", []) if isinstance(doc, Mapping) else []
        if isinstance(links, list):
            for l in links:
                if isinstance(l, Mapping):
                    href = l.get("href")
                    if isinstance(href, str):
                        if _is_url(href):
                            http_urls.append(href)
                        else:
                            file_hrefs.append(href)
    elif kind == "source":
        u, f = _collect_source_hrefs(doc)
        http_urls.extend(u); file_hrefs.extend(f)

    # URL checks
    if check_urls and http_urls:
        with cf.ThreadPoolExecutor(max_workers=max(1, jobs)) as ex:
            futs = [ex.submit(_head_or_get, u, timeout) for u in http_urls]
            for fut in cf.as_completed(futs):
                st = fut.result()
                http_urls_checked += 1
                if not st.ok:
                    http_urls_bad += 1
                    if len(bad_url_samples) < 10:
                        bad_url_samples.append(st)

    # Local file checks
    if check_files and file_hrefs:
        results = _check_local_hrefs(p, file_hrefs)
        file_hrefs_checked = len(results)
        for r in results:
            if not r.ok:
                file_hrefs_bad += 1
                if len(bad_file_samples) < 10:
                    bad_file_samples.append(r)

    valid = (len([e for e in errors if not e.startswith("warn:")]) == 0) and http_urls_bad == 0 and file_hrefs_bad == 0
    return FileReport(
        str(p), kind, valid, errors,
        http_urls_checked, http_urls_bad, bad_url_samples,
        file_hrefs_checked, file_hrefs_bad, bad_file_samples
    )

# -------------------------
# CLI
# -------------------------
def _build_argparser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(
        prog="validate_sources.py",
        description="Validate source catalogs and STAC JSON; optional URL/local-file checks."
    )
    ap.add_argument("inputs", nargs="+", help="JSON files/dirs/globs to validate")
    ap.add_argument("--check-urls", action="store_true", help="HEAD/GET http(s) URLs")
    ap.add_argument("--check-files", action="store_true", help="Check file:// and relative hrefs exist")
    ap.add_argument("--jobs", type=int, default=8, help="Concurrency for URL checks (default: 8)")
    ap.add_argument("--timeout", type=float, default=8.0, help="HTTP timeout seconds (default: 8.0)")
    ap.add_argument("--schema", type=Path, default=None, help="Path to STAC schema (file or directory)")
    ap.add_argument("--report", type=Path, default=Path("data/validation/validate_sources.report.json"),
                    help="Write JSON report to this path")
    return ap

def main(argv: Optional[Sequence[str]] = None) -> int:
    ap = _build_argparser()
    args = ap.parse_args(argv)

    files = list(_iter_inputs(args.inputs))
    if not files:
        print("[WARN] No JSON files found.", file=sys.stderr)
        return 1

    t0 = time.time()
    reports: List[FileReport] = []
    totals = Summary(0, 0, 0, 0, 0, 0, 0, 0.0)

    for p in files:
        rep = validate_file(
            p,
            check_urls=args.check_urls,
            check_files=args.check_files,
            timeout=args.timeout,
            jobs=args.jobs,
            schema_path_opt=args.schema,
        )
        reports.append(rep)
        totals.files_total += 1
        if rep.valid:
            totals.files_valid += 1
            tag = "OK"
        else:
            totals.files_invalid += 1
            tag = "FAIL"

        totals.http_urls_checked += rep.http_urls_checked
        totals.http_urls_bad += rep.http_urls_bad
        totals.file_hrefs_checked += rep.file_hrefs_checked
        totals.file_hrefs_bad += rep.file_hrefs_bad

        print(f"[{tag}] {p}  kind={rep.kind}  http_bad={rep.http_urls_bad}/{rep.http_urls_checked}  "
              f"file_bad={rep.file_hrefs_bad}/{rep.file_hrefs_checked}")
        for e in rep.errors:
            lvl = "WARN" if e.startswith("warn:") else "ERR"
            print(f"   - {lvl}: {e}")
        for st in rep.bad_url_samples:
            print(f"   - URL BAD {st.code or '?'} {st.url} ({st.elapsed_s:.2f}s) {st.error or ''}")
        for fh in rep.bad_file_samples:
            print(f"   - FILE BAD {fh.href} -> {fh.resolved or '?'} {fh.error or ''}")

    totals.elapsed_s = time.time() - t0

    report_obj = {
        "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "inputs": [str(x) for x in args.inputs],
        "summary": asdict(totals),
        "files": [asdict(r) for r in reports],
        "environment": {
            "has_jsonschema": HAS_JSONSCHEMA,
            "kgt_has_schema": KGT_HAS_SCHEMA,
        },
    }
    args.report.parent.mkdir(parents=True, exist_ok=True)
    with args.report.open("w", encoding="utf-8") as f:
        json.dump(report_obj, f, indent=2, sort_keys=True)
        f.write("\n")

    print(f"[RESULT] {totals.files_valid}/{totals.files_total} valid; "
          f"{totals.http_urls_bad}/{totals.http_urls_checked} bad http URLs; "
          f"{totals.file_hrefs_bad}/{totals.file_hrefs_checked} bad file hrefs; "
          f"{totals.elapsed_s:.2f}s")

    return 0 if (totals.files_invalid == 0 and totals.http_urls_bad == 0 and totals.file_hrefs_bad == 0) else 2


if __name__ == "__main__":
    raise SystemExit(main())
