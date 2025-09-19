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
import hashlib
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Iterable, Iterator, List, Mapping, Optional, Sequence, Tuple, Union

Json = Dict[str, Any]
PathLike = Union[str, os.PathLike[str]]


# -----------------------------------------------------------------------------
# Filesystem / JSON
# -----------------------------------------------------------------------------

def read_json(path: PathLike) -> Json:
    """Read a JSON file (UTF-8) into a dict."""
    p = Path(path)
    with p.open("r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path: PathLike, obj: Mapping[str, Any], *, indent: int = 2, sort_keys: bool = True) -> None:
    """Write a dict to a JSON file (UTF-8), ensuring parent dir exists."""
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("w", encoding="utf-8") as f:
        json.dump(obj, f, indent=indent, sort_keys=sort_keys, ensure_ascii=False)
        f.write("\n")


def sha256_file(path: PathLike, *, chunk: int = 1024 * 1024) -> str:
    """Compute SHA-256 for a file (streamed)."""
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        while True:
            b = fh.read(chunk)
            if not b:
                break
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
    """
    for pat in patterns:
        p = Path(pat)
        if p.is_dir():
            it = p.rglob("*")
        else:
            it = (Path(m) for m in glob.glob(pat))
        for f in sorted(it):
            if f.is_file():
                if exts:
                    if f.suffix.lower() not in {e.lower() for e in exts}:
                        continue
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
            print(f"[WARN] failed reading STAC item {p}: {e}", file=sys.stderr)
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


def extract_year_from_properties(props: Mapping[str, Any]) -> Optional[int]:
    """
    Extract an approximate year from STAC temporal properties:
    - properties.datetime
    - or start_datetime/end_datetime (use whichever yields a year first)
    """
    def _year_from_iso(val: Any) -> Optional[int]:
        if isinstance(val, str) and len(val) >= 4 and val[:4].isdigit():
            try:
                return int(val[:4])
            except Exception:
                return None
        return None

    dt = _year_from_iso(props.get("datetime"))
    if dt is not None:
        return dt
    # try range
    for k in ("start_datetime", "end_datetime"):
        y = _year_from_iso(props.get(k))
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
    if key in assets and isinstance(assets[key], Mapping):
        return assets[key]  # preferred
    # first asset
    for _, a in assets.items():
        if isinstance(a, Mapping):
            return a
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
    """
    def _key(it: Mapping[str, Any]) -> Tuple[int, str]:
        props = it.get("properties") or {}
        # Get earliest time string we can compare
        t_candidates = [
            props.get("datetime"),
            props.get("start_datetime"),
            props.get("end_datetime"),
        ]
        t = next((t for t in t_candidates if isinstance(t, str)), None)
        # unknowns: sort at the end
        if t is None:
            return (1, "9999-12-31T23:59:59Z")
        return (0, t)

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
# Small predicates / parsing
# -----------------------------------------------------------------------------

_RX_ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z$")


def is_iso8601_utc(s: str) -> bool:
    """Cheap ISO-8601 (UTC, 'Z') check."""
    return bool(_RX_ISO_DATE.match(s))


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
    except Exception:
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
    "write_json",
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
    "group_by_year",
    "sort_items_by_time",
    # Template ctx
    "build_template_context",
    # Logging
    "info",
    "warn",
    "error",
    # Parsing / misc
    "is_iso8601_utc",
    "coerce_year",
    # Dataclass
    "ItemIndex",
]

