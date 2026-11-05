"""Story-bundle builders for the start page's "The Kansas record" cards.

One module per story, ``tools/local_data/stories/<id_with_underscores>.py``, is found by
``tools/local_data/sql_feed_stories.py`` without any registration. Standard library only, Python 3.11.

    STORY = {"id": "iron-horse", "version": 1, "db": "observations",   # or "bulk"
             "tables": ["kfm_atack_railroads"],                        # every one must exist and have rows
             "sources": [{"name": "...", "license": "...", "url": "...", "citation": "..."}]}

    def build(db) -> dict | None: ...

The contract:

- ``db`` is a read-only ``sqlite3.Connection`` to the database STORY names; TIGER, when the runner was given
  it, is attached as ``tiger``. A builder never writes, never fetches and never reads the clock.
- A story that spans both databases names its main one in ``db``, lists the tables it needs from the other in
  ``other_tables``, and reads them as ``other.<table>``.
- ``build`` returns the story's data, JSON-able and deterministic (same rows, same bytes: the runner keeps a
  stored bundle unless its SHA-256 changes), or ``None`` when the data cannot make a story yet. Every query
  needs a stable ``ORDER BY`` or a sort in Python.
- Put the observed range in the result as ``"_observed": {"from": ..., "to": ...}``; the runner lifts it out.
  Carry each source's own limitations as strings in ``"limits"``, with counts computed from the rows.
- The runner wraps the result as ``{"format": "kfm-story-bundle-v1", "story", "version", "built_at", "sources",
  "observed", "data"}``. The serialized bundle must fit ``MAX_BUNDLE_BYTES``; aim for about 300 KB. Simplify
  geometry, quantize, aggregate.
- Raise ``version`` when the data's shape changes, so that the site can tell old bundles apart.
- A builder may take a few minutes but must finish within about 10 minutes and 1 GB of RAM. Do not repeatedly
  scan the 50M-row tables.
"""
from __future__ import annotations

import json
import math
from typing import Iterable, Sequence

MAX_BUNDLE_BYTES = 900_000
_IDENTIFIER_SAFE = frozenset("abcdefghijklmnopqrstuvwxyz0123456789_")


def has_rows(db, table: str, schema: str = "main") -> bool:
    """True when the table exists in the schema and holds a row. Never scans."""
    if not table or not set(table) <= _IDENTIFIER_SAFE or not set(schema) <= _IDENTIFIER_SAFE:
        raise ValueError(f"unsafe table name {schema}.{table}")
    if not db.execute(f"SELECT 1 FROM {schema}.sqlite_master WHERE type IN ('table','view') AND name=?", (table,)).fetchone():
        return False
    return db.execute(f"SELECT 1 FROM {schema}.{table} LIMIT 1").fetchone() is not None


def rounded(value: float | None, digits: int = 1) -> float | int | None:
    """A compact JSON number. NULL stays None; a whole value loses its ``.0``."""
    if value is None:
        return None
    result = round(float(value), digits)
    return int(result) if result == int(result) else result


def scaled(values: Iterable[float | None], factor: int) -> list[int | None]:
    """Values as integers times factor, the smallest JSON form for a long series. NULL stays None."""
    return [None if v is None else int(round(float(v) * factor)) for v in values]


def geojson_lines(text: str) -> list[list[tuple[float, float]]]:
    """The lines of a GeoJSON LineString or MultiLineString."""
    shape = json.loads(text)
    if shape.get("type") == "LineString":
        lines = [shape["coordinates"]]
    elif shape.get("type") == "MultiLineString":
        lines = shape["coordinates"]
    else:
        raise ValueError(f"not a line geometry: {shape.get('type')}")
    return [[(float(x), float(y)) for x, y, *_ in line] for line in lines if len(line) >= 2]


def line_length(points: Sequence[tuple[float, float]]) -> float:
    """Planar length with longitude scaled for the line's latitude. For proportions, not for reported distances."""
    total = 0.0
    for (x0, y0), (x1, y1) in zip(points, points[1:]):
        total += math.hypot((x1 - x0) * math.cos(math.radians((y0 + y1) / 2)), y1 - y0)
    return total


def simplify(points: Sequence[tuple[float, float]], tolerance: float) -> list[tuple[float, float]]:
    """Douglas-Peucker, iterative. Keeps both ends; tolerance is in the coordinates' units."""
    count = len(points)
    if count <= 2:
        return list(points)
    keep = [False] * count
    keep[0] = keep[-1] = True
    stack = [(0, count - 1)]
    limit = tolerance * tolerance
    while stack:
        first, last = stack.pop()
        (ax, ay), (bx, by) = points[first], points[last]
        dx, dy = bx - ax, by - ay
        span = dx * dx + dy * dy
        worst, worst_distance = -1, limit
        for index in range(first + 1, last):
            px, py = points[index]
            if span == 0:
                distance = (px - ax) ** 2 + (py - ay) ** 2
            else:
                t = max(0.0, min(1.0, ((px - ax) * dx + (py - ay) * dy) / span))
                distance = (px - ax - t * dx) ** 2 + (py - ay - t * dy) ** 2
            if distance > worst_distance:
                worst, worst_distance = index, distance
        if worst >= 0:
            keep[worst] = True
            stack += [(first, worst), (worst, last)]
    return [point for point, kept in zip(points, keep) if kept]


def grid_path(points: Sequence[tuple[float, float]], origin: tuple[float, float], unit: float) -> list[int]:
    """Coordinates as a flat ``[x0, y0, dx1, dy1, ...]`` of integer grid steps. Repeated grid points are dropped.

    The site's ``decodeGridPath(path, origin, unit)`` in ``story-kit.mjs`` reverses it.
    """
    flat: list[int] = []
    last_x = last_y = None
    for x, y in points:
        gx, gy = round((x - origin[0]) / unit), round((y - origin[1]) / unit)
        if last_x is None:
            flat += [gx, gy]
        elif gx != last_x or gy != last_y:
            flat += [gx - last_x, gy - last_y]
        else:
            continue
        last_x, last_y = gx, gy
    return flat
