"""PRISM feed: new and revised 4 km and 800 m grids, kept as Kansas county summaries.

PRISM serves whole-US grids only. Each download is cut to the Kansas window at once: a clipped BIL
(with its header and PRISM's version notes) is the kept raw copy, the US file is recorded by size
and SHA-256 and discarded. County summaries use the same rule as the archived summaries: the cells
whose centers fall inside each 2025 TIGER county, NODATA excluded. A grid PRISM later revises is
loaded again as a new version (``#sha256=`` path suffix); the local-data API serves the newest.

Schedule, per run: each day is fetched when new, again at 8 and 35 days (PRISM's provisional
revisions), at most ``MAX_NEW_DAYS`` new days per run while catching up; each month when it has
ended and again two months later; each year in January and again in July. PRISM asks that a file
be downloaded at most twice a day; a run fetches each file at most once.
"""
from __future__ import annotations

from array import array
from datetime import date, timedelta
import io
import json
import math
import sqlite3
import struct
import sys
import tarfile
import time
import zipfile

from tools.local_data import sql_feeds as core
from tools.local_data.sql_feeds import FeedError

SERVICE = "https://services.nacse.org/prism/data/get/us/{res}/{var}/{key}?format=bil"
VARIABLES = ("ppt", "tmax", "tmin", "tmean", "tdmean", "vpdmin", "vpdmax", "soltotal", "solslope")
RESOLUTIONS = {"4km": "25m", "800m": "30s"}
UNITS = {"ppt": "Millimeters", "tmax": "Degrees C", "tmin": "Degrees C", "tmean": "Degrees C", "tdmean": "Degrees C",
         "vpdmin": "hPa", "vpdmax": "hPa", "soltotal": "MJm-2day-1", "solslope": "MJm-2day-1"}
KANSAS = (-102.0518, 36.993, -94.5884, 40.0032)
MAX_NEW_DAYS = 7
DAILY_THROUGH = date(2026, 9, 23)
MONTHLY_THROUGH = "2026-08"
CHECKS = (("new", 0), ("week", 8), ("month", 35))


# --- Geometry --------------------------------------------------------------------------------------

def _wkb_polygons(blob: bytes):
    """Rings of every polygon in a GeoPackage geometry blob (Polygon or MultiPolygon)."""
    flags = blob[3]
    offset = 8 + (0, 32, 48, 48, 64)[(flags >> 1) & 7]

    def read():
        nonlocal offset
        order = "<" if blob[offset] == 1 else ">"
        kind = struct.unpack_from(order + "I", blob, offset + 1)[0]
        offset += 5

        def count():
            nonlocal offset
            value = struct.unpack_from(order + "I", blob, offset)[0]
            offset += 4
            return value

        if kind == 3:
            rings = []
            for _ in range(count()):
                n = count()
                coords = struct.unpack_from(order + "d" * (2 * n), blob, offset)
                offset += 16 * n
                rings.append(list(zip(coords[0::2], coords[1::2])))
            return [rings]
        if kind == 6:
            return [polygon for _ in range(count()) for polygon in read()]
        raise FeedError("COUNTY_GEOMETRY_TYPE")
    return read()


def county_cells(tiger_path, grid: dict) -> dict:
    """{geoid: (name, [flat cell indices in the Kansas window])} for cell centers inside each county."""
    db = sqlite3.connect(f"file:{tiger_path}?mode=ro", uri=True)
    try:
        counties = db.execute("SELECT GEOID, NAME, geom FROM us_county ORDER BY GEOID").fetchall()
    finally:
        db.close()
    x0, y0, dx, dy, cols, rows = grid["x0"], grid["y0"], grid["dx"], grid["dy"], grid["cols"], grid["rows"]
    out = {}
    for geoid, name, blob in counties:
        edges = []
        for polygon in _wkb_polygons(bytes(blob)):
            for ring in polygon:
                edges.extend(zip(ring, ring[1:]))
        ys = [y for (_, y), _ in edges]
        cells = []
        top, bottom = max(0, int((y0 - max(ys)) / dy) - 1), min(rows - 1, int((y0 - min(ys)) / dy) + 1)
        for r in range(top, bottom + 1):
            cy = y0 - r * dy
            # Even-odd crossings of the row's center line: inside between alternate crossings.
            xs = sorted(x1 + (cy - y1) * (x2 - x1) / (y2 - y1) for (x1, y1), (x2, y2) in edges if (y1 > cy) != (y2 > cy))
            for a, b in zip(xs[0::2], xs[1::2]):
                first, last = math.ceil((a - x0) / dx), math.floor((b - x0) / dx)
                if x0 + last * dx == b:
                    last -= 1
                for c in range(max(first, 0), min(last, cols - 1) + 1):
                    cells.append(r * cols + c)
        out[geoid] = (name, cells)
    return out


# --- Grids -----------------------------------------------------------------------------------------

def read_bil(body: bytes) -> dict:
    """Header, Kansas-window values and the files to keep, from one PRISM BIL zip."""
    with zipfile.ZipFile(io.BytesIO(body)) as archive:
        names = archive.namelist()
        pick = lambda suffix: next((n for n in names if n.endswith(suffix)), None)
        bil, hdr = pick(".bil"), pick(".hdr")
        if not bil or not hdr:
            raise FeedError("PRISM_ZIP_WITHOUT_BIL")
        header = dict(line.split(None, 1) for line in archive.read(hdr).decode("ascii").splitlines() if line.strip())
        header = {k.upper(): v.strip() for k, v in header.items()}
        if header.get("NBITS") != "32" or header.get("PIXELTYPE", "FLOAT") != "FLOAT" or header.get("NBANDS", "1") != "1":
            raise FeedError("PRISM_FORMAT")
        raw = archive.read(bil)
        info = {n: archive.read(n) for n in names if n.endswith((".info.txt", ".prj"))}
    nrows, ncols = int(header["NROWS"]), int(header["NCOLS"])
    if len(raw) != nrows * ncols * 4:
        raise FeedError("PRISM_SIZE")
    x0, y0, dx, dy = float(header["ULXMAP"]), float(header["ULYMAP"]), float(header["XDIM"]), float(header["YDIM"])
    c0, c1 = max(0, int((KANSAS[0] - x0) / dx) - 2), min(ncols - 1, int((KANSAS[2] - x0) / dx) + 2)
    r0, r1 = max(0, int((y0 - KANSAS[3]) / dy) - 2), min(nrows - 1, int((y0 - KANSAS[1]) / dy) + 2)
    window = array("f")
    for r in range(r0, r1 + 1):
        start = (r * ncols + c0) * 4
        window.frombytes(raw[start:start + (c1 - c0 + 1) * 4])
    if (header.get("BYTEORDER", "I").upper() in ("M", "MSBFIRST")) == (sys.byteorder == "little"):
        window.byteswap()
    grid = {"x0": x0 + c0 * dx, "y0": y0 - r0 * dy, "dx": dx, "dy": dy, "cols": c1 - c0 + 1, "rows": r1 - r0 + 1,
            "nodata": float(header.get("NODATA", -9999))}
    clip_header = (f"BYTEORDER I\nLAYOUT BIL\nNROWS {grid['rows']}\nNCOLS {grid['cols']}\nNBANDS 1\nNBITS 32\nPIXELTYPE FLOAT\n"
                   f"ULXMAP {grid['x0']!r}\nULYMAP {grid['y0']!r}\nXDIM {dx!r}\nYDIM {dy!r}\nNODATA {header.get('NODATA', '-9999')}\n")
    return {"grid": grid, "values": window, "clip_header": clip_header, "info": info}


def summarize(values, cells: dict, nodata: float):
    for geoid, (name, indices) in cells.items():
        kept = [v for v in (values[i] for i in indices) if v != nodata and not math.isnan(v)]
        yield (geoid, name, (math.fsum(kept) / len(kept)) if kept else None, min(kept) if kept else None,
               max(kept) if kept else None, len(kept))


def _clip_tar(parsed: dict, stem: str) -> bytes:
    """The kept raw copy: byte-identical for the same grid, so an interrupted load can be retried."""
    out = io.BytesIO()
    with tarfile.open(fileobj=out, mode="w", format=tarfile.PAX_FORMAT) as tar:
        files = {f"{stem}.bil": parsed["values"].tobytes() if sys.byteorder == "little" else _swapped(parsed["values"]),
                 f"{stem}.hdr": parsed["clip_header"].encode(), **{name.split("/")[-1]: body for name, body in parsed["info"].items()}}
        for name, body in sorted(files.items()):
            item = tarfile.TarInfo(name)
            item.size, item.mtime, item.mode = len(body), 0, 0o600
            tar.addfile(item, io.BytesIO(body))
    return core.gz(out.getvalue())


def _swapped(values):
    copy = array("f", values)
    copy.byteswap()
    return copy.tobytes()


# --- Schedule --------------------------------------------------------------------------------------

def _logical_path(res: str, var: str, step: str, key: str) -> str:
    folder = key[:4]
    return f"time_series/us/an/{res}/{var}/{'daily' if step == 'daily' else 'monthly'}/{folder}/prism_{var}_us_{RESOLUTIONS[res]}_{key}.zip"


def due_targets(state: dict, today: date) -> list[tuple[str, str, str]]:
    """[(step, key, check)] to fetch this run, oldest first."""
    # Targets a run left incomplete (a grid not yet posted) come first, until they complete.
    targets = [(step, key, "new") for step, key in (k.split("|") for k in sorted(state.get("retry", {})))]
    checks = state.get("daily_checks", {})
    through = date.fromisoformat(state.get("daily_through", str(DAILY_THROUGH)))
    new_days = 0
    day = through + timedelta(days=1)
    while day <= today - timedelta(days=1) and new_days < MAX_NEW_DAYS:
        targets.append(("daily", day.strftime("%Y%m%d"), "new"))
        new_days, day = new_days + 1, day + timedelta(days=1)
    for key, done in sorted(checks.items()):
        age = (today - date(int(key[:4]), int(key[4:6]), int(key[6:]))).days
        for check, min_age in CHECKS[1:]:
            if age >= min_age and check not in done:
                targets.append(("daily", key, check))
                break
    # Months: a month is fetched once it has ended (from the 3rd of the next month), and revised at 3 months.
    index = lambda y, m: y * 12 + m - 1
    last_complete = index(today.year, today.month) - (1 if today.day >= 3 else 2)
    y, m = map(int, state.get("monthly_through", MONTHLY_THROUGH).split("-"))
    for i in range(index(y, m) + 1, last_complete + 1):
        targets.append(("monthly", f"{i // 12}{i % 12 + 1:02d}", "new"))
    for key, done in sorted(state.get("monthly_checks", {}).items()):
        if index(today.year, today.month) - index(int(key[:4]), int(key[4:])) >= 3 and "revision" not in done:
            targets.append(("monthly", key, "revision"))
    # Last year's annual grid from January 5, revised from July.
    year = str(today.year - 1)
    annual = state.get("annual_checks", {}).get(year, [])
    if today >= date(today.year, 1, 5) and "new" not in annual:
        targets.append(("annual", year, "new"))
    elif today.month >= 7 and "revision" not in annual:
        targets.append(("annual", year, "revision"))
    seen, unique = set(), []
    for t in targets:
        if t[:2] not in seen:
            seen.add(t[:2])
            unique.append(t)
    return unique


def _mark(state: dict, step: str, key: str, check: str, today: date) -> dict:
    state = json.loads(json.dumps(state))
    state.get("retry", {}).pop(f"{step}|{key}", None)
    if step == "daily":
        checks = state.setdefault("daily_checks", {})
        age = (today - date(int(key[:4]), int(key[4:6]), int(key[6:]))).days
        # A first fetch made late already covers the earlier revision checks.
        checks[key] = sorted(set(checks.get(key, [])) | {c for c, min_age in CHECKS if age >= min_age or c == check})
        if check == "new":
            state["daily_through"] = max(state.get("daily_through", str(DAILY_THROUGH)), f"{key[:4]}-{key[4:6]}-{key[6:]}")
        for old in [k for k, v in checks.items() if set(v) >= {"new", "week", "month"}]:
            del checks[old]
    elif step == "monthly":
        checks = state.setdefault("monthly_checks", {})
        months = (today.year * 12 + today.month) - (int(key[:4]) * 12 + int(key[4:]))
        checks[key] = sorted(set(checks.get(key, [])) | {check} | ({"revision"} if months >= 3 else set()))
        if check == "new":
            state["monthly_through"] = max(state.get("monthly_through", MONTHLY_THROUGH), f"{key[:4]}-{key[4:]}")
        for old in [k for k, v in checks.items() if "revision" in v]:
            del checks[old]
    else:
        checks = state.setdefault("annual_checks", {})
        checks[key] = sorted(set(checks.get(key, [])) | {check})
    return state


def _retry(state: dict, step: str, key: str, today: date, keep_days: int = 60) -> dict:
    """Remember an incomplete new target; give it up (recorded) after keep_days."""
    state = json.loads(json.dumps(state))
    retry = state.setdefault("retry", {})
    first = retry.setdefault(f"{step}|{key}", str(today))
    if (today - date.fromisoformat(first)).days > keep_days:
        del retry[f"{step}|{key}"]
        state["given_up"] = (state.get("given_up", []) + [f"{step}|{key}"])[-50:]
    return state


# --- Feed ------------------------------------------------------------------------------------------

def _grid_known(db, path: str, digest: str) -> tuple[bool, bool]:
    """(this exact grid already loaded, any version of this path loaded)."""
    rows = db.execute("SELECT source_sha256 FROM kfm_prism_grids WHERE source_path=? OR source_path LIKE ?",
                      (path, path + "#sha256=%")).fetchall()
    return any(r[0] == digest for r in rows), bool(rows)


def prism(ctx, resolutions=("4km", "800m")) -> dict:
    if not ctx.tiger:
        raise FeedError("TIGER_GEOPACKAGE_REQUIRED")
    db = core.open_db(ctx)
    cell_maps = {}
    summary = {"downloads": 0, "grids_loaded": 0, "unchanged": 0, "unavailable": 0, "targets": 0}
    try:
        state = core.get_state(db, "prism")
        today = ctx.now().date()
        targets = due_targets(state, today)
        summary["targets"] = len(targets)
        for step, key, check in targets:
            complete = True
            for res in resolutions:
                for var in VARIABLES:
                    url = SERVICE.format(res=res, var=var, key=key)
                    fetched = ctx.fetch(url, limit=400_000_000, timeout=600, missing_ok=True)
                    time.sleep(getattr(ctx, "pause", 1.0))
                    if fetched is None or not fetched.body.startswith(b"PK"):
                        summary["unavailable"] += 1
                        complete = False
                        continue
                    summary["downloads"] += 1
                    digest = core.sha256(fetched.body)
                    path = _logical_path(res, var, step, key)
                    with core.pipeline_lock(ctx):
                        same, any_version = _grid_known(db, path, digest)
                    if same:
                        summary["unchanged"] += 1
                        continue
                    parsed = read_bil(fetched.body)
                    signature = (res, round(parsed["grid"]["x0"], 6), round(parsed["grid"]["y0"], 6), parsed["grid"]["cols"], parsed["grid"]["rows"])
                    if signature not in cell_maps:
                        cell_maps[signature] = county_cells(ctx.tiger, parsed["grid"])
                    stem = path.rsplit("/", 1)[1][:-4] + "_KS"
                    raw_path, raw_digest = core.store_raw(ctx, "prism", f"{res}/{var}/{step}/{key[:4]}/{stem}-{digest[:12]}.tar.gz",
                                                          _clip_tar(parsed, stem), url=url, fetched=fetched, original=fetched.body,
                                                          extra={"clip": "Kansas window, 2 cells of margin", "check": check})
                    rows = list(summarize(parsed["values"], cell_maps[signature], parsed["grid"]["nodata"]))
                    stored_path = path + (f"#sha256={digest[:12]}" if any_version else "")
                    with core.pipeline_lock(ctx):
                        core.guard(ctx)
                        db.execute("BEGIN IMMEDIATE")
                        try:
                            grid_id = db.execute("INSERT INTO kfm_prism_grids(source_path,unit,source_sha256,source_bytes,raster_path,processed_at,county_rows,state) "
                                                 "VALUES (?,?,?,?,?,?,?,?)", (stored_path, UNITS[var], digest, len(fetched.body),
                                                 str(raw_path.relative_to(ctx.root)), ctx.now().strftime("%Y-%m-%dT%H:%M:%SZ"), len(rows), "complete")).lastrowid
                            db.executemany("INSERT INTO kfm_prism_county_stats VALUES (?,?,?,?,?,?,?,?)",
                                           [(grid_id, g, n, mean, lo, hi, count, "") for g, n, mean, lo, hi, count in rows])
                            db.execute("COMMIT")
                        except BaseException:
                            db.execute("ROLLBACK")
                            raise
                    summary["grids_loaded"] += 1
            with core.pipeline_lock(ctx):
                if complete:
                    state = _mark(state, step, key, check, today)
                elif check == "new":
                    state = _retry(state, step, key, today)
                # An incomplete revision check is simply not marked, so it stays due.
                core.set_state(db, ctx, "prism", state)
        return {**summary, "daily_through": state.get("daily_through"), "monthly_through": state.get("monthly_through")}
    finally:
        db.close()
