"""Qualify one exact Newberry Kansas archive offline; never publish or export geometry.

Requires Python 3.10+ and pyshp==2.3.1. See docs/county-history-qualification.md.
A successful check still reports HOLD: neither source rights nor release are approved.
"""
import argparse
import collections
import csv
import datetime as dt
import hashlib
import io
import json
import math
import os
from pathlib import PurePosixPath
import re
import stat
import sys
import zipfile

ARCHIVE_SHA256 = "a233b4b3bcf3f3d7a52a4c18de76017f0d4f1f421086f95312df4c59a0aa5f02"
SOURCE_URL = "https://publications.newberry.org/ahcb/downloads/gis/KS_AtlasHCB.zip"
FIRST = dt.date(1804, 10, 1)
LAST = dt.date(2000, 12, 31)
ROOT = "KS_AtlasHCB/"
SHAPE = ROOT + "KS_Historical_Counties/KS_Historical_Counties."
EVENTS = ROOT + "KS_Comprehensive_Database/KS_Comprehensive_Database.txt"
LICENSE = ROOT + "zCreativeCommonsLicense/CreativeCommonsDeed.htm"
MAX_ARCHIVE = 8 * 1024 * 1024
MAX_EXPANDED = 16 * 1024 * 1024
FIELDS = ["NAME", "ID", "STATE", "FIPS", "VERSION", "START_DATE", "END_DATE",
          "CHANGE", "CITATION", "START_N", "END_N", "AREA_SQMI", "DATASET",
          "CNTY_TYPE", "FULL_NAME"]
EVENT_FIELDS = ["FIPS", "STATE", "NAME", "ID", "VERSION", "START_DATE", "END_DATE",
                "CREATION_OR_CHANGE", "CITATION", "START_N", "END_N", "DATASET"]


def require(condition, code):
    if not condition:
        raise ValueError(code)


def source_date(value):
    require(type(value) in (int, str), "DATE_TYPE")
    text = str(value)
    require(bool(re.fullmatch(r"[0-9]{8}", text)), "DATE_FORMAT")
    day = dt.date(int(text[:4]), int(text[4:6]), int(text[6:]))
    return day


def interval(row):
    start, last = source_date(row["START_N"]), source_date(row["END_N"])
    require(FIRST <= start <= LAST and FIRST <= last <= LAST, "DATE_COVERAGE")
    require(start <= last, "REVERSED_INTERVAL")
    # END_N means the LAST included day. KFM endExclusive is the following day.
    return start, last + dt.timedelta(days=1)


def select_rows(rows, day):
    require(type(day) is dt.date and FIRST <= day <= LAST, "DATE_COVERAGE")
    return [row for row in rows if interval(row)[0] <= day < interval(row)[1]]


def version_key(row):
    require(bool(row["ID"]) and str(row["VERSION"]).isdigit(), "VERSION_IDENTITY")
    return (row["ID"], int(row["VERSION"]), *interval(row))


def chronology_kind(row):
    if row["END_N"]:
        version_key(row)
        require(bool(row["CITATION"] and row["CREATION_OR_CHANGE"]), "VERSION_EVIDENCE")
        return "mapped_version"
    if row["START_N"]:
        source_date(row["START_N"])
        require(bool(row["CITATION"] and row["CREATION_OR_CHANGE"]), "EVENT_EVIDENCE")
        # An undated end does not make an event an open-ended polygon.
        return "event_only"
    require(bool(row["ID"] and re.search(r"\(see .+\)", row["NAME"])), "UNDATED_RECORD")
    require(not any(row[k] for k in ["VERSION", "START_DATE", "END_DATE",
                                    "CREATION_OR_CHANGE", "CITATION"]), "ALIAS_EVENT_CONFLICT")
    return "name_cross_reference"


def continuity(rows):
    groups = collections.defaultdict(list)
    keys = set()
    for row in rows:
        key = version_key(row)
        require(key not in keys, "DUPLICATE_VERSION")
        keys.add(key)
        groups[row["ID"]].append(row)
    gaps = []
    for identity, group in sorted(groups.items()):
        group.sort(key=lambda row: interval(row)[0])
        require(len({int(row["VERSION"]) for row in group}) == len(group), "REUSED_VERSION")
        for before, after in zip(group, group[1:]):
            end, start = interval(before)[1], interval(after)[0]
            require(end <= start, "SAME_INSTITUTION_OVERLAP")
            if end < start:
                gaps.append({"id": identity, "fromInclusive": end.isoformat(),
                             "toExclusive": start.isoformat(), "days": (start - end).days})
    return gaps


def check_geometry(points, parts):
    require(4 <= len(points) <= 100_000 and 1 <= len(parts) <= 1000, "GEOMETRY_LIMIT")
    require(parts[0] == 0 and list(parts) == sorted(set(parts)), "PART_OFFSETS")
    require(all(type(p) is int and 0 <= p < len(points) for p in parts), "PART_OFFSETS")
    for point in points:
        require(len(point) == 2 and all(type(v) in (int, float) and math.isfinite(v) for v in point), "COORDINATES")
        require(-180 <= point[0] <= 180 and -90 <= point[1] <= 90, "COORDINATE_RANGE")
    for start, end in zip(parts, list(parts[1:]) + [len(points)]):
        ring = points[start:end]
        require(len(ring) >= 4 and ring[0] == ring[-1], "RING_CLOSURE")
        require(len(set(map(tuple, ring[:-1]))) >= 3, "RING_DEGENERATE")
        area2 = sum(a[0]*b[1] - b[0]*a[1] for a, b in zip(ring, ring[1:]))
        require(area2 != 0, "RING_ZERO_AREA")


def checked_members(archive):
    members = archive.infolist()
    require(0 < len(members) <= 100, "ZIP_MEMBER_COUNT")
    names = set()
    total = 0
    for member in members:
        path = PurePosixPath(member.filename)
        require(not path.is_absolute() and ".." not in path.parts and "\\" not in member.filename,
                "ZIP_PATH")
        require(member.filename.startswith(ROOT) and member.filename not in names, "ZIP_IDENTITY")
        require(not member.is_dir() and not stat.S_ISLNK(member.external_attr >> 16), "ZIP_FILE_TYPE")
        require(not member.flag_bits & 1, "ZIP_ENCRYPTED")
        require(0 <= member.file_size <= MAX_ARCHIVE, "ZIP_ENTRY_SIZE")
        total += member.file_size
        require(total <= MAX_EXPANDED, "ZIP_EXPANSION")
        names.add(member.filename)
    require({SHAPE + ext for ext in ("shp", "shx", "dbf", "prj")} | {EVENTS, LICENSE} <= names,
            "ZIP_REQUIRED_MEMBERS")
    return members


def read_pinned_archive(path):
    # Open exactly the named local regular file; do not fetch URLs or extract ZIP paths.
    require(not str(path).startswith(("http:", "https:")), "LOCAL_FILE_REQUIRED")
    flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_NONBLOCK", 0)
    with os.fdopen(os.open(path, flags), "rb") as handle:
        info = os.fstat(handle.fileno())
        require(stat.S_ISREG(info.st_mode) and 0 < info.st_size <= MAX_ARCHIVE, "ARCHIVE_FILE")
        raw = handle.read(MAX_ARCHIVE + 1)
    require(len(raw) <= MAX_ARCHIVE, "ARCHIVE_SIZE")
    require(hashlib.sha256(raw).hexdigest() == ARCHIVE_SHA256, "ARCHIVE_DIGEST")
    return raw


def qualify(path):
    raw = read_pinned_archive(path)
    try:
        import shapefile
    except ImportError as error:
        raise ValueError("REQUIRES_PYSHP_2_3_1") from error
    require(shapefile.__version__ == "2.3.1", "PYSHP_VERSION")
    with zipfile.ZipFile(io.BytesIO(raw)) as archive:
        members = checked_members(archive)
        # Reading also verifies each member's CRC. Content is kept in memory only.
        content = {member.filename: archive.read(member) for member in members}
    member_receipts = [{"path": name, "bytes": len(value), "sha256": hashlib.sha256(value).hexdigest()}
                       for name, value in sorted(content.items())]
    with shapefile.Reader(shp=io.BytesIO(content[SHAPE+"shp"]),
                          shx=io.BytesIO(content[SHAPE+"shx"]),
                          dbf=io.BytesIO(content[SHAPE+"dbf"]), encoding="cp1252") as reader:
        require([field[0] for field in reader.fields[1:]] == FIELDS, "DBF_FIELDS")
        require(reader.numRecords == 341, "DBF_COUNT")
        rows = [row.as_dict() for row in reader.records()]
        shapes = reader.shapes()
        require(len(rows) == len(shapes) == 341, "SHAPE_RECORD_COUNT")
        for row, shape in zip(rows, shapes):
            start, end = interval(row)
            require(row["START_DATE"] == start and row["END_DATE"] == end-dt.timedelta(days=1), "DATE_COLUMN_MISMATCH")
            require(row["DATASET"] == "KS_Historical_Counties" and bool(row["CITATION"]), "BOUNDARY_EVIDENCE")
            require(not row["FIPS"] or bool(re.fullmatch(r"[0-9]{5}", row["FIPS"])), "FIPS_FORMAT")
            require(shape.shapeType == shapefile.POLYGON, "SHAPE_TYPE")
            check_geometry(shape.points, shape.parts)
        # This is a source extent, intentionally NOT restricted to modern Kansas.
        bbox = list(reader.bbox)
    tsv = csv.DictReader(io.StringIO(content[EVENTS].decode("cp1252")), delimiter="\t")
    require(tsv.fieldnames == EVENT_FIELDS, "CHRONOLOGY_FIELDS")
    events = list(tsv)
    require(len(events) == 945 and all(set(row) == set(EVENT_FIELDS) and None not in row.values() for row in events), "CHRONOLOGY_ROWS")
    for row in events:
        for number, text in [("START_N", "START_DATE"), ("END_N", "END_DATE")]:
            require(bool(row[number]) == bool(row[text]), "CHRONOLOGY_DATE_PRESENCE")
            if row[number]:
                require(dt.datetime.strptime(row[text], "%d %m %Y %H:%M:%S").date() == source_date(row[number]), "CHRONOLOGY_DATE_MISMATCH")
    kinds = collections.Counter(chronology_kind(row) for row in events)
    mapped = [row for row in events if chronology_kind(row) == "mapped_version"]
    require(collections.Counter(map(version_key, rows)) == collections.Counter(map(version_key, mapped)), "CHRONOLOGY_VERSION_JOIN")
    require(all(row["ID"] in {r["ID"] for r in rows} for row in events if chronology_kind(row) == "name_cross_reference"), "ALIAS_TARGET")
    gaps = continuity(rows)
    frames = {}
    for value in (18041001, 18540530, 18550825, 18610129, 18800101, 19000101, 20001231):
        day = source_date(value)
        frames[day.isoformat()] = len(select_rows(rows, day))
    return {
        "status": "HOLD", "qualification": "offline_structure_passed", "releaseEligible": False,
        "source": {"url": SOURCE_URL, "archiveSha256": ARCHIVE_SHA256, "bytes": len(raw),
                   "coverageStart": FIRST.isoformat(), "coverageLastDay": LAST.isoformat(),
                   "sourceKind": "historical_reconstruction", "libraryVersion": shapefile.__version__,
                   "decodingUsed": "cp1252", "projectionWkt": content[SHAPE+"prj"].decode("ascii")},
        "rights": {"bundledLicense": "CC-BY-NC-SA-2.5", "publicReuseDecision": "unresolved",
                   "reason": "Source-specific terms and general open-access footer need a recorded reuse determination."},
        "counts": {"boundaryVersions": len(rows), "institutions": len({r["ID"] for r in rows}),
                   "versionsWithoutFips": sum(not r["FIPS"] for r in rows), "chronologyRows": len(events),
                   "chronologyKinds": dict(sorted(kinds.items())), "parts": sum(len(s.parts) for s in shapes),
                   "vertices": sum(len(s.points) for s in shapes), "maxFeatureVertices": max(len(s.points) for s in shapes),
                   "sourceCountyTypes": dict(sorted(collections.Counter(r["CNTY_TYPE"] for r in rows).items())),
                   "uniqueVersionStartDates": len({r["START_N"] for r in rows}),
                   "firstChronologyEvent": min(source_date(r["START_N"]) for r in events if r["START_N"]).isoformat()},
        "sourceExtentNad83": bbox, "selectedDateFeatureCounts": frames, "institutionGaps": gaps,
        "notEstablished": ["topology", "legal_or_sovereignty_authority", "current_boundaries_after_2000",
                           "encoding_declared_by_provider", "datum_transformation", "source_admission",
                           "public_redistribution_rights", "browser_rendering", "performance"],
        "members": member_receipts,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("archive", help="Path to the exact local KS_AtlasHCB.zip; no network acquisition")
    args = parser.parse_args()
    try:
        result = qualify(args.archive)
    except (ValueError, OSError, zipfile.BadZipFile, csv.Error) as error:
        print(json.dumps({"status": "ERROR", "releaseEligible": False, "error": str(error)}))
        return 1
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0  # Successful qualification is explicitly NOT a release decision.


if __name__ == "__main__":
    sys.exit(main())
