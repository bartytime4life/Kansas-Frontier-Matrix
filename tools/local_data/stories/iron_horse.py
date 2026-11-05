"""Iron Horse: railroads across Kansas as Jeremy Atack's GIS file dates them."""
from __future__ import annotations

from collections import defaultdict

from tools.local_data.stories import geojson_lines, grid_path, line_length, rounded, simplify

STORY = {
    "id": "iron-horse",
    "version": 1,
    "db": "observations",
    "tables": ["kfm_atack_railroads"],
    "sources": [{
        "name": "Jeremy Atack, Historical GIS database of U.S. Railroads for 1826-1911",
        "license": "No licence stated; the author suggests a citation and asks for corrections",
        "url": "https://my.vanderbilt.edu/jeremyatack/data-downloads/",
        "citation": 'Atack, Jeremy. "Historical Geographic Information Systems (GIS) database of U.S. Railroads '
                    'for 1826-1911."',
    }],
}

GRID_ORIGIN = (-103.0, 36.0)
GRID_UNIT = 0.001       # degrees; about 100 m, finer than a full-window map of Kansas can show
TOLERANCE = 0.0015
STANDARD_GAUGE = 56.5


def _chains(pieces: list[tuple[list[tuple[float, float]], float]]) -> list[tuple[list[tuple[float, float]], float]]:
    """Join two-point pieces into polylines where exactly two pieces meet. Each piece brings its share of miles."""
    key = lambda point: (round(point[0], 6), round(point[1], 6))
    ends = defaultdict(list)
    for index, (line, _) in enumerate(pieces):
        ends[key(line[0])].append(index)
        ends[key(line[-1])].append(index)
    used = [False] * len(pieces)
    chains = []

    def walk(index: int, start) -> None:
        points, miles, at = [], 0.0, start
        while True:
            used[index] = True
            line, share = pieces[index]
            ordered = line if key(line[0]) == at else line[::-1]
            points += ordered if not points else ordered[1:]
            miles += share
            at = key(ordered[-1])
            others = [i for i in ends[at] if i != index]
            if len(ends[at]) != 2 or not others or used[others[0]]:
                break
            index = others[0]
        chains.append((points, miles))

    # Open ends first, in input order, so that the result does not depend on hashing.
    for index, (line, _) in enumerate(pieces):
        if used[index]:
            continue
        for point in (line[0], line[-1]):
            if not used[index] and len(ends[key(point)]) != 2:
                walk(index, key(point))
    for index, (line, _) in enumerate(pieces):   # closed loops
        if not used[index]:
            walk(index, key(line[0]))
    return chains


def build(db) -> dict | None:
    rows = db.execute("SELECT in_op_by, statenam, rrname, gauge, exact_date, miles, geometry_geojson "
                      "FROM kfm_atack_railroads WHERE in_op_by IS NOT NULL AND geometry_geojson IS NOT NULL "
                      "ORDER BY in_op_by, statenam, rrname, gauge, file_id, row_number").fetchall()
    if not rows:
        return None
    groups: dict[tuple, list] = defaultdict(list)
    added: dict[tuple[int, bool], float] = defaultdict(float)
    segments: dict[tuple[int, bool], int] = defaultdict(int)
    dated = gauged = named = 0
    for year, state, name, gauge, exact, miles, geometry in rows:
        state, name, gauge = state or "", (name or "").strip(), float(gauge or 0)
        in_kansas = state == "Kansas"
        added[year, in_kansas] += float(miles or 0)
        segments[year, in_kansas] += 1
        dated += 1 if exact else 0
        gauged += 1 if gauge > 0 else 0
        named += 1 if name else 0
        lines = geojson_lines(geometry)
        whole = sum(line_length(line) for line in lines) or 1.0
        pieces = groups[year, state, name, gauge]
        for line in lines:
            pieces.append((line, float(miles or 0) * line_length(line) / whole))
    years = sorted({key[0] for key in groups})
    states = sorted({key[1] for key in groups})
    names = sorted({key[2] for key in groups})
    gauges = sorted({key[3] for key in groups})
    lines = []
    for (year, state, name, gauge) in sorted(groups):
        for points, miles in _chains(groups[year, state, name, gauge]):
            path = grid_path(simplify(points, TOLERANCE), GRID_ORIGIN, GRID_UNIT)
            if len(path) >= 4:
                lines.append([years.index(year), states.index(state), names.index(name), gauges.index(gauge),
                              rounded(miles, 2), path])
    miles_by_year, kansas_total, neighbour_total = [], 0.0, 0.0
    for year in years:
        kansas, neighbours = added[year, True], added[year, False]
        kansas_total += kansas
        neighbour_total += neighbours
        miles_by_year.append({"year": year, "kansas": rounded(kansas, 1), "neighbours": rounded(neighbours, 1),
                              "kansasTotal": rounded(kansas_total, 1), "neighboursTotal": rounded(neighbour_total, 1),
                              "kansasSegments": segments[year, True], "neighbourSegments": segments[year, False]})
    total = len(rows)
    first_kansas = next((row["year"] for row in miles_by_year if row["kansas"]), None)
    return {
        "_observed": {"from": years[0], "to": years[-1]},
        "grid": {"origin": list(GRID_ORIGIN), "unit": GRID_UNIT},
        "years": years, "states": states, "names": names, "gauges": gauges,
        "kansasState": states.index("Kansas") if "Kansas" in states else None,
        "firstKansasYear": first_kansas,
        "lines": lines,
        "milesByYear": miles_by_year,
        "counts": {"segments": total, "dated": dated, "gauged": gauged, "named": named,
                   "standardGauge": sum(1 for r in rows if r[3] == STANDARD_GAUGE)},
        "limits": [
            f"Years are Atack's in-operation-by benchmarks, {len(years)} of them here, not construction dates: "
            f"{total - dated:,} of {total:,} segments carry no exact date, so a line may have opened any time after "
            "the previous benchmark.",
            f"Atack's national file starts in 1826. In this cut, the first segment near Kansas is {years[0]} and the "
            f"first tagged Kansas is {first_kansas}.",
            "The file records no abandonment, so a line stays lit after any later removal.",
            f"Railroad names are recorded for {named:,} of {total:,} segments and gauge for {gauged:,}; the rest are "
            "blank in the source.",
            "Miles are the file's per-segment figures, counted whole under the state the file tags. Neighbouring "
            "states appear only where a segment touches Kansas, so their totals are not those states' networks.",
            "Lines are simplified to about 150 m for display.",
        ],
    }
