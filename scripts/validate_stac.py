#!/usr/bin/env python3
"""
scripts/validate_stac.py
========================

Validate STAC **Item** JSON files with:
- Strict JSON Schema (if `jsonschema` available) using your local schema.
- Fallback minimal structural checks when `jsonschema` is absent.
- Optional URL reachability (HEAD/GET) for asset/links.
- Optional bbox/geometry sanity checks and temporal rules.
- Emits a machine-readable report for MCP/CI.

Usage
-----
# Strict validation (schema), no network:
python scripts/validate_stac.py data/stac/*.json

# Plus URL checks:
python scripts/validate_stac.py data/stac/*.json --check-urls --jobs 12 --timeout 6

# Extra geometry/bbox sanity:
python scripts/validate_stac.py data/stac/*.json --check-geometry --check-bbox

# Write a report for CI artifacts:
python scripts/validate_stac.py data/stac/*.json --report data/validation/validate_stac.report.json
"""

from __future__ import annotations

import argparse
import concurrent.futures as cf
import glob
import json
import math
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
    from kansas_geo_timeline import load_json_schema, schema_path  # type: ignore
    KGT_HAS_SCHEMA = True
except Exception:
    KGT_HAS_SCHEMA = False


Json = Dict[str, Any]
REQ_TOP = ["stac_version", "id", "type", "geometry", "bbox", "properties", "links", "assets"]


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
            for m in sorted(glob.glob(pat)):
                yield Path(m)


def _read_json(p: Path) -> Json:
    with p.open("r", encoding="utf-8") as f:
        return json.load(f)


# ---------------------------
# Minimal structural checks
# ---------------------------

def _minimal_item_errors(item: Mapping[str, Any]) -> List[str]:
    errs: List[str] = []
    for k in REQ_TOP:
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
    return errs


def _is_num(x: Any) -> bool:
    try:
        float(x)
        return True
    except Exception:
        return False


def _collect_asset_urls(item: Mapping[str, Any]) -> List[str]:
    urls: List[str] = []
    assets = item.get("assets", {})
    if isinstance(assets, Mapping):
        for a in assets.values():
            if isinstance(a, Mapping):
                href = a.get("href")
                if isinstance(href, str) and href.startswith(("http://", "https://")):
                    urls.append(href)
    return urls


def _collect_link_urls(item: Mapping[str, Any]) -> List[str]:
    out: List[str] = []
    links = item.get("links", [])
    if isinstance(links, list):
        for link in links:
            if isinstance(link, Mapping):
                href = link.get("href")
                if isinstance(href, str) and href.startswith(("http://", "https://")):
                    out.append(href)
    return out


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
# Geometry / bbox sanity (optional)
# ---------------------------

def _bbox_valid(bbox: Sequence[float]) -> bool:
    if len(bbox) < 4:
        return False
    w, s, e, n = bbox[:4]
    if not all(_is_num(v) for v in (w, s, e, n)):
        return False
    w, s, e, n = float(w), float(s), float(e), float(n)
    return (w <= e) and (s <= n) and (-180.0 <= w <= 180.0) and (-180.0 <= e <= 180.0) and (-90.0 <= s <= 90.0) and (-90.0 <= n <= 90.0)


def _temporal_rule_errors(props: Mapping[str, Any]) -> List[str]:
    """
    STAC temporal rule: either datetime is set (non-null) OR both start/end set (non-null).
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


# ---------------------------
# Validation per file
# ---------------------------

@dataclass
class FileReport:
    path: str
    valid: bool
    errors: List[str]
    warnings: List[str]
    assets_total: int
    links_total: int
    bad_urls: int
    bad_url_samples: List[UrlStatus]


def validate_item(
    p: Path,
    *,
    schema_opt: Optional[Path],
    strict: bool,
    check_urls: bool,
    check_geometry: bool,
    check_bbox: bool,
    timeout: float,
    jobs: int
) -> FileReport:
    errors: List[str] = []
    warnings: List[str] = []

    try:
        doc = _read_json(p)
    except Exception as e:
        return FileReport(str(p), False, [f"JSON parse failed: {e}"], [], 0, 0, 0, [])

    # Strict-first schema validation
    if HAS_JSONSCHEMA and strict:
        try:
            if schema_opt is not None:
                with schema_opt.open("r", encoding="utf-8") as f:
                    schema = json.load(f)
            elif KGT_HAS_SCHEMA:
                schema = load_json_schema("stac_item.schema.json")
            else:
                schema = None

            if schema is not None:
                validator = jsonschema.Draft202012Validator(schema)  # type: ignore[attr-defined]
                errs = sorted(validator.iter_errors(doc), key=lambda e: e.path)
                for e in errs:
                    where = "/".join(str(x) for x in e.path)
                    errors.append(f"{where}: {e.message}")
            else:
                warnings.append("schema: no STAC schema available; falling back to minimal checks")
                errors.extend(_minimal_item_errors(doc))
        except Exception as e:
            errors.append(f"schema validation failed: {e}")
    else:
        # Minimal structure if strict off or jsonschema missing
        errors.extend(_minimal_item_errors(doc))
        if strict and not HAS_JSONSCHEMA:
            warnings.append("jsonschema not installed; minimal checks only")

    # Optional temporal/bbox/geometry sanity
    if isinstance(doc, Mapping):
        props = doc.get("properties", {}) or {}
        if isinstance(props, Mapping):
            errors.extend(_temporal_rule_errors(props))

        if check_bbox:
            bbox = doc.get("bbox", [])
            if not _bbox_valid(bbox if isinstance(bbox, (list, tuple)) else []):
                errors.append("bbox: invalid or out-of-range")

    # Collect URLs
    asset_urls = _collect_asset_urls(doc if isinstance(doc, Mapping) else {})
    link_urls = _collect_link_urls(doc if isinstance(doc, Mapping) else {})

    # URL reachability
    bad_urls = 0
    bad_samples: List[UrlStatus] = []
    if check_urls:
        urls = asset_urls + link_urls
        with cf.ThreadPoolExecutor(max_workers=max(1, jobs)) as ex:
            futs = [ex.submit(_check_url, u, timeout) for u in urls]
            for fut in cf.as_completed(futs):
                st = fut.result()
                if not st.ok:
                    bad_urls += 1
                    if len(bad_samples) < 10:
                        bad_samples.append(st)

    valid = (len(errors) == 0) and (bad_urls == 0)
    return FileReport(
        path=str(p),
        valid=valid,
        errors=errors,
        warnings=warnings,
        assets_total=len(asset_urls),
        links_total=len(link_urls),
        bad_urls=bad_urls,
        bad_url_samples=bad_samples,
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
    elapsed_s: float


def _build_argparser() -> argparse.ArgumentParser:
    ap = argparse.ArgumentParser(
        prog="validate_stac.py",
        description="Validate STAC Item JSON files (schema + optional URL/geometry checks)."
    )
    ap.add_argument("inputs", nargs="+", help="STAC Item files/dirs/globs to validate")
    ap.add_argument("--schema", type=Path, default=None, help="Path to STAC Item schema (optional)")
    ap.add_argument("--no-strict", action="store_true", help="Disable jsonschema strict validation (use minimal checks)")
    ap.add_argument("--check-urls", action="store_true", help="HEAD/GET asset & link URLs")
    ap.add_argument("--jobs", type=int, default=8, help="Concurrency for URL checks (default 8)")
    ap.add_argument("--timeout", type=float, default=8.0, help="HTTP timeout seconds (default 8.0)")
    ap.add_argument("--check-geometry", action="store_true", help="(Reserved) Geometry internal checks")
    ap.add_argument("--check-bbox", action="store_true", help="Validate bbox ranges (lon/lat order & limits)")
    ap.add_argument("--report", type=Path, default=Path("data/validation/validate_stac.report.json"), help="Write JSON report")
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
    totals = Summary(0, 0, 0, 0, 0, 0.0)

    for p in files:
        rep = validate_item(
            p,
            schema_opt=args.schema,
            strict=not args.no_strict,
            check_urls=args.check_urls,
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
        totals.urls_checked += (rep.assets_total + rep.links_total if args.check_urls else 0)
        totals.urls_bad += rep.bad_urls

        print(f"[{tag}] {p}  assets={rep.assets_total}  links={rep.links_total}  bad_urls={rep.bad_urls}")
        for e in rep.errors:
            print(f"   - ERR: {e}")
        for w in rep.warnings:
            print(f"   - WARN: {w}")
        for st in rep.bad_url_samples:
            print(f"   - URL BAD {st.code or '?'} {st.url} ({st.elapsed_s:.2f}s) {st.error or ''}")

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
          f"{totals.elapsed_s:.2f}s")

    return 0 if (totals.files_invalid == 0 and totals.urls_bad == 0) else 2


if __name__ == "__main__":
    raise SystemExit(main())

