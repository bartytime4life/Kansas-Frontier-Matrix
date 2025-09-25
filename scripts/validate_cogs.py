#!/usr/bin/env python3
"""
validate_cogs.py — Validate all candidate COGs under a path.

Primary validator:  rio cogeo validate
Fallback:           gdalinfo --json  (checks IMAGE_STRUCTURE.LAYOUT == "COG")

Features
--------
- Parallel validation (configurable jobs + timeout)
- Include/exclude filename patterns and directory filters
- JSON report with per-file results and a summary (CI-friendly)
- Fail-fast mode, quiet mode
- Optional: treat warnings as failures

Examples
--------
# Basic
python scripts/validate_cogs.py data/cogs

# Multiple patterns, exclude temp/ and *_thumb.tif, JSON report
python scripts/validate_cogs.py data/cogs \
  --pattern "*.tif" --pattern "*.tiff" \
  --exclude-pattern "*_thumb.tif" --exclude-dir "temp" \
  --jobs 8 --timeout 60 \
  --report data/validation/cog_validate.report.json

# Fallback-only (skip rio if you want to test GDAL path)
python scripts/validate_cogs.py data/cogs --no-rio

# Fail fast on first error
python scripts/validate_cogs.py data/cogs --fail-fast
"""
from __future__ import annotations

import argparse
import fnmatch
import json
import os
import shutil
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

RIO = shutil.which("rio")
GDALINFO = shutil.which("gdalinfo")


# ----------------------------
# Data structures
# ----------------------------
@dataclass
class FileResult:
    path: str
    ok: bool
    tool: str
    duration_s: float
    error: Optional[str] = None
    warnings: List[str] = None
    details: Dict[str, object] = None


# ----------------------------
# Utils
# ----------------------------
def _now() -> float:
    return time.perf_counter()


def _iso(ts: Optional[float] = None) -> str:
    return time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(ts or time.time()))


def _atomic_write_text(path: Path, text: str) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp.write_text(text, encoding="utf-8")
    os.replace(tmp, path)


def _walk_candidates(
    root: Path,
    include_patterns: List[str],
    exclude_patterns: List[str],
    exclude_dirs: List[str],
) -> List[Path]:
    incs = include_patterns or ["*.tif", "*.tiff"]
    excs = exclude_patterns or []
    exdirs = set(d.strip("/\\") for d in (exclude_dirs or []))
    out: List[Path] = []
    for dirpath, dirnames, filenames in os.walk(root):
        # prune excluded directories
        pruned = [d for d in dirnames if d in exdirs]
        for d in pruned:
            dirnames.remove(d)
        for fn in filenames:
            fpath = Path(dirpath) / fn
            if not any(fnmatch.fnmatch(fn.lower(), p.lower()) for p in incs):
                continue
            if any(fnmatch.fnmatch(fn.lower(), p.lower()) for p in excs):
                continue
            # final extension check
            if fpath.suffix.lower() not in {".tif", ".tiff"}:
                continue
            out.append(fpath)
    return out


# ----------------------------
# Validators
# ----------------------------
def validate_with_rio(path: Path, timeout: int) -> Tuple[bool, List[str], Dict[str, object], Optional[str]]:
    """Use `rio cogeo validate` (returns ok, warnings, details, error)."""
    cmd = [RIO, "cogeo", "validate", str(path)]
    try:
        t0 = _now()
        proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, timeout=timeout, text=True)
        dt = _now() - t0
        out = proc.stdout or ""
        ok = (proc.returncode == 0)
        warn: List[str] = []
        # rio-cogeo prints human text; scrape a few typical notes
        if "WARNING" in out.upper():
            warn.append("rio warning(s) present")
        details = {"stdout": out.strip(), "elapsed_s": round(dt, 3)}
        return ok, warn, details, None if ok else out.strip()
    except subprocess.TimeoutExpired:
        return False, [], {"timeout_s": timeout}, f"rio validate timed out after {timeout}s"
    except Exception as e:
        return False, [], {}, f"rio validate failed: {e!r}"


def validate_with_gdal(path: Path, timeout: int) -> Tuple[bool, List[str], Dict[str, object], Optional[str]]:
    """Use `gdalinfo --json` to check IMAGE_STRUCTURE.LAYOUT == 'COG'."""
    if not GDALINFO:
        return False, [], {}, "gdalinfo not available"
    cmd = [GDALINFO, "--json", str(path)]
    try:
        t0 = _now()
        proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout, text=True)
        dt = _now() - t0
        if proc.returncode != 0:
            return False, [], {"stderr": proc.stderr.strip(), "elapsed_s": round(dt, 3)}, proc.stderr.strip()
        info = json.loads(proc.stdout)
        # Typical locations:
        #  - info["metadata"]["IMAGE_STRUCTURE"]["LAYOUT"] == "COG"
        #  - or a driver metadata "COG": "YES" in newer GDALs
        layout = (
            info.get("metadata", {})
                .get("IMAGE_STRUCTURE", {})
                .get("LAYOUT")
        )
        driver_md = info.get("metadata", {}).get("", {})
        is_cog = (str(layout).upper() == "COG") or (str(driver_md.get("COG", "")).upper() in {"1", "YES", "TRUE"})
        # Heuristics: block size + overviews presence can be sanity checks
        warnings: List[str] = []
        if not is_cog:
            return False, warnings, {"gdalinfo": info, "elapsed_s": round(dt, 3)}, "LAYOUT is not COG"
        return True, warnings, {"elapsed_s": round(dt, 3)}, None
    except subprocess.TimeoutExpired:
        return False, [], {"timeout_s": timeout}, f"gdalinfo timed out after {timeout}s"
    except json.JSONDecodeError:
        return False, [], {}, "gdalinfo returned non-JSON output"
    except Exception as e:
        return False, [], {}, f"gdal validation failed: {e!r}"


# ----------------------------
# Worker
# ----------------------------
def _validate_one(
    f: Path,
    use_rio: bool,
    timeout: int,
    treat_warn_as_fail: bool,
) -> FileResult:
    t0 = _now()
    tool_used = None
    ok = False
    err = None
    warns: List[str] = []
    details: Dict[str, object] = {}

    if use_rio and RIO:
        tool_used = "rio-cogeo"
        ok, warns, details, err = validate_with_rio(f, timeout)
        if not ok and GDALINFO:
            # Try gdal fallback for a second opinion
            _ok2, _warn2, _det2, _err2 = validate_with_gdal(f, timeout)
            details["gdal_fallback"] = {"ok": _ok2, "error": _err2}
    else:
        tool_used = "gdalinfo"
        ok, warns, details, err = validate_with_gdal(f, timeout)

    if treat_warn_as_fail and warns and ok:
        ok = False
        err = "warnings present and --warnings-are-errors set"

    dt = _now() - t0
    return FileResult(
        path=str(f),
        ok=ok,
        tool=tool_used or ("rio-cogeo" if use_rio else "gdalinfo"),
        duration_s=round(dt, 3),
        error=err,
        warnings=warns or [],
        details=details or {},
    )


# ----------------------------
# Main
# ----------------------------
def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("root", type=Path, help="Root directory to scan")
    ap.add_argument("--pattern", action="append", default=["*.tif", "*.tiff"], help="Include glob (repeatable)")
    ap.add_argument("--exclude-pattern", action="append", default=[], help="Exclude glob (repeatable)")
    ap.add_argument("--exclude-dir", action="append", default=[], help="Directory name to skip entirely (repeatable)")
    ap.add_argument("--jobs", type=int, default=os.cpu_count() or 4, help="Parallel workers")
    ap.add_argument("--timeout", type=int, default=120, help="Per-file validator timeout (seconds)")
    ap.add_argument("--fail-fast", action="store_true", help="Stop on first failure")
    ap.add_argument("--report", type=Path, help="Write JSON report here")
    ap.add_argument("--quiet", action="store_true", help="Reduce stdout noise")
    ap.add_argument("--warnings-are-errors", action="store_true", help="Treat warnings as failures")
    ap.add_argument("--no-rio", action="store_true", help="Do not use rio-cogeo even if available")
    args = ap.parse_args()

    if not args.root.exists():
        print(f"[ERR] root not found: {args.root}", file=sys.stderr)
        return 2

    use_rio = (not args.no_rio) and (RIO is not None)
    if not use_rio and not GDALINFO:
        print("[WARN] Neither rio-cogeo nor gdalinfo is available; cannot validate.", file=sys.stderr)
        return 0

    files = _walk_candidates(args.root, args.pattern, args.exclude_pattern, args.exclude_dir)
    if not files:
        if not args.quiet:
            print("[INFO] no rasters found")
        # still produce an empty report if requested
        if args.report:
            rep = {
                "generated": _iso(),
                "root": str(args.root),
                "tool": "rio-cogeo" if use_rio else "gdalinfo",
                "summary": {"total": 0, "ok": 0, "failed": 0, "duration_s": 0.0},
                "results": [],
            }
            _atomic_write_text(args.report, json.dumps(rep, indent=2) + "\n")
        return 0

    if not args.quiet:
        tool_msg = "rio-cogeo" if use_rio else "gdalinfo"
        print(f"[INFO] validating {len(files)} file(s) with {tool_msg} — jobs={args.jobs}, timeout={args.timeout}s")

    t0 = _now()
    results: List[FileResult] = []
    failed = 0

    with ThreadPoolExecutor(max_workers=max(1, args.jobs)) as ex:
        fut_map = {ex.submit(_validate_one, f, use_rio, args.timeout, args.warnings_are_errors): f for f in files}
        for fut in as_completed(fut_map):
            res = fut.result()
            results.append(res)
            if not args.quiet:
                status = "OK " if res.ok else "FAIL"
                print(f"[{status}] {res.path}  ({res.tool}, {res.duration_s:.2f}s)")
                if res.error and not res.ok:
                    print(f"       error: {res.error}", file=sys.stderr)
            if not res.ok:
                failed += 1
                if args.fail_fast:
                    break

    duration = round(_now() - t0, 3)
    total = len(results)
    ok_count = sum(1 for r in results if r.ok)

    if args.report:
        rep = {
            "generated": _iso(),
            "root": str(args.root),
            "tool": "rio-cogeo" if use_rio else "gdalinfo",
            "summary": {
                "total": total,
                "ok": ok_count,
                "failed": failed,
                "duration_s": duration,
            },
            "results": [asdict(r) for r in results],
        }
        _atomic_write_text(args.report, json.dumps(rep, indent=2) + "\n")
        if not args.quiet:
            print(f"[INFO] report → {args.report}")

    if failed:
        print(f"[WARN] {failed} file(s) failed COG validation.", file=sys.stderr)
        return 1
    if not args.quiet:
        print(f"[OK] all COGs valid ({total}/{total}) in {duration:.2f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
