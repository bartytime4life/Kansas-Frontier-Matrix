"""
kansas_geo_timeline.utils
=========================

Lightweight helpers for I/O, STAC item handling, path/glob ops, and small
geospatial/time utilities used across the Kansas Geo Timeline toolchain.

Design goals
------------
- Pure stdlib (no heavy GIS/ML deps).
- Safe, explicit error handling for CI.
- Reusable by CLI, tests, and notebooks.
"""

from __future__ import annotations

import glob
import json
import os
import re
import sys
import tempfile
import hashlib
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Any, Dict, Iterable, Iterator, List, Mapping, Optional, Sequence, Tuple, Union

Json = Dict[str, Any]
PathLike = Union[str, os.PathLike[str]]
BBox = Tuple[float, float, float, float]


# -----------------------------------------------------------------------------
# Filesystem / JSON
# -----------------------------------------------------------------------------

def read_json(path: PathLike) -> Json:
    """Read a JSON file (UTF-8) into a dict."""
    p = Path(path)
    with p.open("r", encoding="utf-8") as f:
        return json.load(f)


def try_read_json(path: PathLike) -> Optional[Json]:
    """Best-effort JSON load; returns None and prints a warning on failure."""
    try:
        return read_json(path)
    except Exception as e:
        warn(f"failed reading JSON {path}: {e}")
        return None


def write_json(
    path: PathLike,
    obj: Mapping[str, Any],
    *,
    indent: int = 2,
    sort_keys: bool = True,
    atomic: bool = True,
) -> None:
    """
    Write a dict to a JSON file (UTF-8), ensuring parent dir exists.
    Uses an atomic temp-file swap by default (best for CI).
    """
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    if not atomic:
        with p.open("w", encoding="utf-8") as f:
            json.dump(obj, f, indent=indent, sort_keys=sort_keys, ensure_ascii=False)
            f.write("\n")
        return

    # Atomic write: write to temp then replace
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=str(p.parent), delete=False) as tf:
        tmp_name = tf.name
        json.dump(obj, tf, indent=indent, sort_keys=sort_keys, ensure_ascii=False)
        tf.write("\n")
    os.replace(tmp_name, p)


def read_jsonl(path: PathLike) -> List[Json]:
    """Read JSON Lines (one JSON object per line)."""
    out: List[Json] = []
    p = Path(path)
    with p.open("r", encoding="utf-8") as f:
        for ln in f:
            ln = ln.strip()
            if ln:
                out.append(json.loads(ln))
    return out


def write_jsonl(path: PathLike, rows: Iterable[Mapping[str, Any]], *, atomic: bool = True) -> None:
    """Write an iterable of dicts as JSON Lines."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    if not atomic:
        with p.open("w", encoding="utf-8") as f:
            for r in rows:
                f.write(json.dumps(r, ensure_ascii=False))
                f.write("\n")
        return
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", dir=str(p.parent), delete=False) as tf:
        tmp_name = tf.name
        for r in rows:
            tf.write(json.dumps(r, ensure_ascii=False))
            tf.write("\n")
    os.replace(tmp_name, p)


def sha256_file(path: PathLike, *, chunk: int = 1024 * 1024) -> str:
    """Compute SHA-256 for a file (streamed)."""
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for b in iter(lambda: fh.read(chunk), b""):
            h.update(b)
    return h.hexdigest()


def ensure_dir(path: PathLike) -> Path:
    """Create directory if needed and return it as Path."""
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p


def iter_paths(patterns: Iterable[str], *, exts: Optional[Sequence[str]] = None) -> Iterator[Path]:
    """
    Iterate over files matching one or more globs or directories.
    If 'exts' is provided, filter by lowercased suffix (e.g., ['.json']).
    Stable, de-duplicated ordering.
    """
    allowed = {e.lower() for e in exts} if exts else None
    seen: set[Path] = set()

    for pat in patterns:
        p = Path(pat)
        # Expand to candidate iterator
        if p.is_dir():
            candidates = (f for f in p.rglob("*") if f.is_file())
        else:
            candidates = (Path(m) for m in glob.glob(pat))

        # Collect sorted for stable output
        for f in sorted(candidates):
            if f in seen or not f.is_file():
                continue
            if allowed and f.suffix.lower() not in allowed:
                continue
            seen.add(f)
            yield f


@contextmanager
def chdir(tmp: PathLike) -> Iterator[None]:
    """
    Context manager to temporarily change the working directory.
    Always returns to the previous cwd.
    """
    prev = Path.cwd()
    try:
        os.chdir(tmp)
        yield
    finally:
        os.chdir(prev)


# -----------------------------------------------------------------------------
# STAC helpers (minimal / tolerant)
# -----------------------------------------------------------------------------

STAC_REQUIRED_TOP = ["stac_version", "id", "type", "geometry", "bbox", "properties", "links", "assets"]


def load_stac_items(paths: Iterable[str]) -> List[Json]:
    """Load many STAC Item JSON files, skipping unreadable files with warnings."""
    items: List[Json] = []
    for p in iter_paths(paths, exts=[".json"]):
        try:
            data = read_json(p)
            items.append(data)
        except Exception as e:
            warn(f"failed reading STAC item {p}: {e}")
    return items


def minimal_validate_stac(item: Json) -> Tuple[bool, List[str]]:
    """
    Perform quick structural checks without jsonschema.
    Returns (is_valid, errors).
    """
    errs: List[str] = []
    for k in STAC_REQUIRED_TOP:
        if k not in item:
            errs.append(f"missing key: {k}")
    if item.get("type") != "Feature":
        errs.append("type must be 'Feature'")
    bbox = item.get("bbox")
    if not (isinstance(bbox, (list, tuple)) and len(bbox) >= 4):
        errs.append("bbox must be an array of at least 4 numbers")
    props = item.get("properties", {})
    if not isinstance(props, dict):
        errs.append("properties must be an object")
    return (len(errs) == 0), errs


def _year_from_iso_prefix(val: Any) -> Optional[int]:
    """Extract YYYY from a string that begins with ISO date/time, else None."""
    if isinstance(val, str) and len(val) >= 4 and val[:4].isdigit():
        try:
            y = int(val[:4])
            if 0 <= y <= 9999:
                return y
        except Exception:
            return None
    return None


def extract_year_from_properties(props: Mapping[str, Any]) -> Optional[int]:
    """
    Extract an approximate year from STAC temporal properties:
    - properties.datetime
    - or start_datetime/end_datetime (use whichever yields a year first)
    """
    dt = _year_from_iso_prefix(props.get("datetime"))
    if dt is not None:
        return dt
    for k in ("start_datetime", "end_datetime"):
        y = _year_from_iso_prefix(props.get(k))
        if y is not None:
            return y
    return None


def stac_asset(item: Mapping[str, Any], key: str = "source") -> Optional[Mapping[str, Any]]:
    """
    Get a preferred asset from a STAC Item.
    - Tries assets['source'] first; otherwise returns the first asset.
    """
    assets = item.get("assets")
    if not isinstance(assets, dict) or not assets:
        return None
    a = assets.get(key)
    if isinstance(a, Mapping):
        return a
    for _, v in assets.items():
        if isinstance(v, Mapping):
            return v
    return None


def compact_bbox(bbox: Any, *, precision: int = 4) -> str:
    """Return a compact string for a bbox or '[]' on failure."""
    try:
        if isinstance(bbox, (list, tuple)) and len(bbox) >= 4:
            fmt = f"%.{precision}f"
            return "[" + ", ".join(fmt % float(v) for v in bbox[:4]) + "]"
    except Exception:
        pass
    return "[]"


def bbox_is_valid(b: Any) -> bool:
    """Basic bbox plausibility: array-like with 4 numbers min; min < max."""
    try:
        if not (isinstance(b, (list, tuple)) and len(b) >= 4):
            return False
        xmin, ymin, xmax, ymax = map(float, b[:4])
        return (xmax > xmin) and (ymax > ymin)
    except Exception:
        return False


def bbox_to_tuple(b: Any) -> Optional[BBox]:
    """Coerce to (xmin, ymin, xmax, ymax) tuple if valid; else None."""
    if not bbox_is_valid(b):
        return None
    xmin, ymin, xmax, ymax = map(float, b[:4])
    return (xmin, ymin, xmax, ymax)


def bbox_center(b: Any) -> Optional[Tuple[float, float]]:
    """Return (cx, cy) for bbox; None if invalid."""
    t = bbox_to_tuple(b)
    if not t:
        return None
    xmin, ymin, xmax, ymax = t
    return ((xmin + xmax) / 2.0, (ymin + ymax) / 2.0)


def bbox_size(b: Any) -> Optional[Tuple[float, float]]:
    """Return (width, height) for bbox; None if invalid."""
    t = bbox_to_tuple(b)
    if not t:
        return None
    xmin, ymin, xmax, ymax = t
    return (xmax - xmin, ymax - ymin)


def bbox_union(a: Any, b: Any) -> Optional[BBox]:
    """Union of two bboxes; None if either invalid."""
    ta, tb = bbox_to_tuple(a), bbox_to_tuple(b)
    if not ta or not tb:
        return None
    return (min(ta[0], tb[0]), min(ta[1], tb[1]), max(ta[2], tb[2]), max(ta[3], tb[3]))


def group_by_year(items: Sequence[Mapping[str, Any]]) -> Dict[Optional[int], List[Mapping[str, Any]]]:
    """
    Group STAC items by extracted year (None if unknown).
    """
    out: Dict[Optional[int], List[Mapping[str, Any]]] = {}
    for it in items:
        props = it.get("properties") or {}
        year = extract_year_from_properties(props) if isinstance(props, Mapping) else None
        out.setdefault(year, []).append(it)
    return out


def sort_items_by_time(items: Sequence[Mapping[str, Any]]) -> List[Mapping[str, Any]]:
    """
    Sort STAC items by datetime (or start/end), with unknowns last.
    Compares using normalized ISO strings (Z).
    """
    def _norm(t: Any) -> str:
        if isinstance(t, str):
            try:
                return to_iso8601_z(parse_iso8601(t))
            except Exception:
                return t  # fallback to raw string ordering
        return "9999-12-31T23:59:59Z"

    def _key(it: Mapping[str, Any]) -> Tuple[int, str]:
        props = it.get("properties") or {}
        t_candidates = [
            props.get("datetime"),
            props.get("start_datetime"),
            props.get("end_datetime"),
        ]
        s = next((c for c in t_candidates if isinstance(c, str)), None)
        if s is None:
            return (1, "9999-12-31T23:59:59Z")
        return (0, _norm(s))

    return sorted(items, key=_key)


# -----------------------------------------------------------------------------
# Template assistance (kept optional by caller)
# -----------------------------------------------------------------------------

def build_template_context(
    stac_items: Sequence[Json],
    *,
    title: str = "Kansas Geo Timeline",
    subtitle: str = "Historical + geological layers over time",
    extra: Optional[Mapping[str, Any]] = None,
) -> Json:
    """
    Build a sane default context dict for app.config.json rendering.
    Injects a convenience 'properties._year' (non-STAC) per item.
    """
    ctx: Json = {
        "title": title,
        "subtitle": subtitle,
        "stac_items": [],
    }
    for it in stac_items:
        it2 = dict(it)
        props = dict(it2.get("properties") or {})
        props["_year"] = extract_year_from_properties(props)
        it2["properties"] = props
        ctx["stac_items"].append(it2)

    if extra:
        ctx.update(dict(extra))
    return ctx


# -----------------------------------------------------------------------------
# Tiny logging helpers
# -----------------------------------------------------------------------------

def info(msg: str) -> None:
    print(f"[INFO] {msg}", file=sys.stderr)


def warn(msg: str) -> None:
    print(f"[WARN] {msg}", file=sys.stderr)


def error(msg: str) -> None:
    print(f"[ERROR] {msg}", file=sys.stderr)


# -----------------------------------------------------------------------------
# ISO-8601 parsing / predicates
# -----------------------------------------------------------------------------

# Permissive ISO-8601 with timezone (Z or ±HH:MM); second fraction optional.
_RX_ISO = re.compile(
    r"^(?P<y>\d{4})-(?P<m>\d{2})-(?P<d>\d{2})"
    r"[T ]"
    r"(?P<H>\d{2}):(?P<M>\d{2}):(?P<S>\d{2})(?P<frac>\.\d+)?"
    r"(?P<tz>Z|[+\-]\d{2}:\d{2})$"
)

def is_iso8601_utc(s: str) -> bool:
    """Check if a string is ISO-8601 UTC (ends with 'Z')."""
    m = _RX_ISO.match(s)
    return bool(m and m.group("tz") == "Z")


def parse_iso8601(s: str) -> datetime:
    """
    Parse ISO-8601 string into an aware datetime (UTC).
    Accepts 'Z' or ±HH:MM offsets; raises ValueError on failure.
    """
    m = _RX_ISO.match(s)
    if not m:
        raise ValueError(f"not ISO-8601: {s!r}")
    y, mo, d = int(m.group("y")), int(m.group("m")), int(m.group("d"))
    H, M, S = int(m.group("H")), int(m.group("M")), int(m.group("S"))
    frac = m.group("frac")
    micro = 0
    if frac:
        # Pad/truncate to microseconds
        frac_digits = (frac[1:] + "000000")[:6]
        micro = int(frac_digits)
    tzs = m.group("tz")
    if tzs == "Z":
        tzinfo = timezone.utc
    else:
        sign = 1 if tzs[0] == "+" else -1
        hh, mm = map(int, tzs[1:].split(":"))
        tzinfo = timezone(sign * timedelta(hours=hh, minutes=mm))
    dt = datetime(y, mo, d, H, M, S, microsecond=micro, tzinfo=tzinfo)
    return dt.astimezone(timezone.utc)


def to_iso8601_z(dt: datetime) -> str:
    """Format an aware datetime as ISO-8601 with 'Z' (UTC)."""
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    else:
        dt = dt.astimezone(timezone.utc)
    # Keep microseconds only if non-zero
    if dt.microsecond:
        return dt.strftime("%Y-%m-%dT%H:%M:%S.%fZ").rstrip("0").rstrip(".") + "Z"
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def coerce_year(value: Any) -> Optional[int]:
    """
    Try to coerce an arbitrary value to a year int, else None.
    Accepts YYYY strings or ints in [0, 9999].
    """
    try:
        if isinstance(value, int) and 0 <= value <= 9999:
            return value
        if isinstance(value, str) and len(value) >= 4 and value[:4].isdigit():
            y = int(value[:4])
            if 0 <= y <= 9999:
                return y
    except (ValueError, TypeError):
        # Expected: value cannot be coerced to a valid year (int/str parse failed)
        pass
    return None


# -----------------------------------------------------------------------------
# Dataclass (optional convenience)
# -----------------------------------------------------------------------------

@dataclass(frozen=True)
class ItemIndex:
    """
    Lightweight index over STAC Items for quick lookups in UI build steps.
    """
    items: Tuple[Json, ...]

    @classmethod
    def from_list(cls, lst: Sequence[Json]) -> "ItemIndex":
        return cls(tuple(lst))

    def by_id(self, item_id: str) -> Optional[Json]:
        for it in self.items:
            if str(it.get("id", "")) == item_id:
                return it
        return None

    def years(self) -> List[Optional[int]]:
        ys = [extract_year_from_properties(it.get("properties", {})) for it in self.items]
        # de-duplicate while preserving order
        seen: set = set()
        out: List[Optional[int]] = []
        for y in ys:
            if y not in seen:
                seen.add(y)
                out.append(y)
        return out

    def group(self) -> Dict[Optional[int], List[Json]]:
        return group_by_year(self.items)


__all__ = [
    # IO
    "read_json",
    "try_read_json",
    "write_json",
    "read_jsonl",
    "write_jsonl",
    "sha256_file",
    "ensure_dir",
    "iter_paths",
    "chdir",
    # STAC
    "load_stac_items",
    "minimal_validate_stac",
    "extract_year_from_properties",
    "stac_asset",
    "compact_bbox",
    "bbox_is_valid",
    "bbox_to_tuple",
    "bbox_center",
    "bbox_size",
    "bbox_union",
    "group_by_year",
    "sort_items_by_time",
    # Template ctx
    "build_template_context",
    # Logging
    "info",
    "warn",
    "error",
    # ISO-8601 / parsing
    "is_iso8601_utc",
    "parse_iso8601",
    "to_iso8601_z",
    "coerce_year",
    # Dataclass
    "ItemIndex",
]
