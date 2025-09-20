#!/usr/bin/env python3
"""
scripts/validate_sources.py
===========================

Validate JSON source catalogs (data/sources/*.json) and/or STAC Items (data/stac/*.json)
for basic structure, provenance, and (optionally) URL reachability.

Goals
-----
- Pure stdlib (no hard dependencies). If available:
  * jsonschema : strict STAC Item validation against local schema.
  * kansas_geo_timeline : load schema path if the package is installed.
- Fast, concurrent URL checks with HEAD (fallback to GET) when requested.
- MCP traceability: emits a machine-readable report/manifest.

Usage
-----
# Validate both sources and STAC, no network
python scripts/validate_sources.py data/sources/*.json data/stac/*.json

# Also check that asset URLs respond (HEAD/GET)
python scripts/validate_sources.py data/sources/*.json --check-urls --jobs 8 --timeout 10

# Fail CI if any error (non-zero exit)
python scripts/validate_sources.py data/stac/*.json --report data/validation/validate_sources.report.json

Notes
-----
- This tool is intentionally tolerant for sources/*.json (lenient catalogs). For strict STAC Items,
  jsonschema is used when available, else a minimal structural check runs.
"""

from __future__ import annotations

import argparse
import concurrent.futures as cf
import glob
import json
import os
import sys
import time
from dataclasses import dataclass, asdict
from pathlib import Path
from typing import Any, Dict, Iterable, Iterator, List, Mapping, Optional, Sequence, Tuple
from urllib.parse import urlparse
from urllib.request import Request, urlopen

# ---------------------------------------------------------------------
# Optional helpers (jsonschema, kansas_geo_timeline for schema loading)
# ---------------------------------------------------------------------
HAS_JSONSCHEMA = False
try:
    import jsonschema  # type: ignore
    HAS_JSONSCHEMA = True
except Exception:
    HAS_JSONSCHEMA = False

KGT_HAS_SCHEMA = False
try:
    # Prefer local package's schema loader if available
    from kansas_geo_timeline import load_json_schema, schema_path  # type: ignore
    KGT_HAS_SCHEMA = True
except Exception:
    KGT_HAS_SCHEMA = False


Json = Dict[str, Any]


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


def _is_url(s: Any) -> bool:
    return isinstance(s, str) and s.startswith(("http://", "https://"))


def _collect_urls_from_doc(doc: Any) -> List[str]:
    """
    Focus on typical shapes we use:
      - STAC item: {type:'Feature', assets:{key:{href: URL}}}
      - Catalog-ish: {"assets":[{"href":URL}, ...]} or {"urls":[URL,...]} or top-level [URL,...]
    """
    urls: List[str] = []
    if isinstance(doc, Mapping):
        # STAC Feature assets
        if doc.get("type") == "Feature" and isinstance(doc.get("assets"), Mapping):
            for a in doc["assets"].values():
                if isinstance(a, Mapping) and _is_url(a.get("href")):
                    urls.append(a["href"])

        # Catalog 'assets' array
        if isinstance(doc.get("assets"), list):
            for a in doc["assets"]:
                if isinstance(a, Mapping) and _is_url(a.get("href")):
                    urls.append(a["href"])

        # Catalog 'urls' array
        if isinstance(doc.get("urls"), list):
            for u in doc["urls"]:
                if _is_url(u):
                    urls.append(u)

    # Allow top-level list of URLs
    if isinstance(doc, list):
        for u in doc:
            if _is_url(u):
                urls.append(u)

    # de-dup, stable order
    seen = set()
    out = []
    for u in urls:
        if u not in seen:
            out.append(u)
            seen.add(u)
    return out


# ---------------------------
# Minimal STAC checks
# ---------------------------
STAC_REQUIRED = ["stac_version", "id", "type", "geometry", "bbox", "properties", "links", "assets"]


def _minimal_stac_check(item: Mapping[str, Any]) -> List[str]:
    errs: List[str] = []
    for k in STAC_REQUIRED:
        if k not in item:
            errs.append(f"missing key: {k}")
    if item.get("type") != "Feature":
        errs.append("type must be 'Feature'")
    bbox = item.get("bbox")
    if not (isinstance(bbox, (list, tuple)) and len(bbox) >= 4):
        errs.append("bbox must be an array [west, south, east, north, ...]")
    props = item.get("properties")
    if not isinstance(props, Mapping):
        errs.append("properties must be an object")
    assets = item.get("assets")
    if not isinstance(assets, Mapping) or not assets:
        errs.append("assets must be a non-empty object")
    return errs


# ---------------------------
# URL checking (HEAD/GET)
# ---------------------------

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
        # Try HEAD first
        req = Request(url, method="HEAD", headers={"User-Agent": "kfm-validate/1.0"})
        with urlopen(req, timeout=timeout) as resp:
            code = getattr(resp, "status", 200)
            return UrlStatus(url, code < 400, int(code), time.time() - t0, None)
    except Exception as e:
        # Fallback to GET (some servers reject HEAD)
        try:
            req = Request(url, method="GET", headers={"User-Agent": "kfm-validate/1.0"})
            with urlopen(req, timeout=timeout) as resp:
                code = getattr(resp, "status", 200)
                return UrlStatus(url, code < 400, int(code), time.time() - t0, None)
        except Exception as e2:
            return UrlStatus(url, False, None, time.time() - t0, f"{type(e2).__name__}: {e2}")


# ---------------------------
# Validation entry points
# ---------------------------

@dataclass
class FileReport:
    path: str
    kind: str           # "stac" | "catalog" | "unknown"
    valid: bool
    errors: List[str]
    urls_checked: int
    urls_bad: int
    url_samples_bad: List[UrlStatus]


def validate_file(p: Path, *, check_urls: bool, timeout: float, jobs: int, schema_path_opt: Optional[Path]) -> FileReport:
    errors: List[str] = []
    kind = "unknown"
    urls: List[str] = []
    bad_statuses: List[UrlStatus] = []

    # Load JSON
    try:
        doc = _read_json(p)
    except Exception as e:
        return FileReport(str(p), kind, False, [f"JSON parse failed: {e}"], 0, 0, [])

    # Decide kind + structural checks
    if isinstance(doc, Mapping) and doc.get("type") == "Feature" and "assets" in doc:
        kind = "stac"
        # Strict JSON Schema if available
        if HAS_JSONSCHEMA:
            try:
                if schema_path_opt is not None:
                    with open(schema_path_opt, "r", encoding="utf-8") as f:
                        schema = json.load(f)
                elif KGT_HAS_SCHEMA:
                    schema = load_json_schema("stac_item.schema.json")
                else:
                    schema = None

                if schema:
                    validator = jsonschema.Draft202012Validator(schema)  # type: ignore[attr-defined]
                    errs = sorted(validator.iter_errors(doc), key=lambda e: e.path)
                    for e in errs:
                        where = "/".join(str(x) for x in e.path)
                        errors.append(f"{where}: {e.message}")
            except Exception as e:
                errors.append(f"schema validation failed: {e}")
        else:
            errors.extend(_minimal_stac_check(doc))

        urls = _collect_urls_from_doc(doc)

    else:
        # Treat as catalog-ish; lenient checks
        kind = "catalog"
        if not isinstance(doc, (Mapping, list)):
            errors.append("expected object or array")
        urls = _collect_urls_from_doc(doc)
        if not urls:
            errors.append("no URLs discovered (assets/urls)")

        # Helpful warnings for license/provenance fields (non-fatal)
        if isinstance(doc, Mapping):
            lic = doc.get("license")
            if lic is None:
                errors.append("warn: license not declared")
            prov = doc.get("providers") or doc.get("source") or doc.get("citation")
            if prov is None:
                errors.append("warn: provider/citation not declared")

    # URL checks
    urls_bad = 0
    if check_urls and urls:
        with cf.ThreadPoolExecutor(max_workers=max(1, jobs)) as ex:
            futs = [ex.submit(_head_or_get, u, timeout) for u in urls]
            for fut in cf.as_completed(futs):
                st = fut.result()
                if not st.ok:
                    urls_bad += 1
                    bad_statuses.append(st)

    valid = (len([e for e in errors if not e.startswith("warn:")]) == 0) and (urls_bad == 0)
    # Clip sample of bad URLs (not to flood logs)
    bad_sample = bad_statuses[:10]
    return FileReport(str(p), kind, valid, errors, len(urls), urls_bad, bad_sample)


# ---------------------------
# CLI / Report
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
        prog="validate_sources.py",
        description="Validate source catalogs and/or STAC Items; optional URL reachability checks."
    )
    ap.add_argument("inputs", nargs="+", help="JSON files/dirs/globs to validate")
    ap.add_argument("--check-urls", action="store_true", help="Perform HTTP HEAD/GET on discovered URLs")
    ap.add_argument("--jobs", type=int, default=8, help="Concurrency for URL checks (default: 8)")
    ap.add_argument("--timeout", type=float, default=8.0, help="HTTP timeout seconds (default: 8.0)")
    ap.add_argument("--schema", type=Path, default=None, help="Path to STAC Item schema (optional).")
    ap.add_argument("--report", type=Path, default=Path("data/validation/validate_sources.report.json"), help="Write JSON report to this path")
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
    totals = Summary(0, 0, 0, 0, 0, 0.0)

    for p in files:
        rep = validate_file(p, check_urls=args.check_urls, timeout=args.timeout, jobs=args.jobs, schema_path_opt=args.schema)
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

        print(f"[{tag}] {p}  kind={rep.kind}  urls={rep.urls_checked}  bad={rep.urls_bad}")
        if rep.errors:
            for e in rep.errors:
                level = "WARN" if e.startswith("warn:") else "ERR"
                print(f"   - {level}: {e}")
        if rep.url_samples_bad:
            for st in rep.url_samples_bad:
                print(f"   - URL BAD {st.code or '?'} {st.url} ({st.elapsed_s:.2f}s) {st.error or ''}")

    totals.elapsed_s = time.time() - t0

    # Emit report
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
          f"{totals.urls_bad}/{totals.urls_checked} bad URLs; "
          f"{totals.elapsed_s:.2f}s")

    # Non-zero exit if any invalid file or bad URL
    return 0 if (totals.files_invalid == 0 and totals.urls_bad == 0) else 2


if __name__ == "__main__":
    raise SystemExit(main())

