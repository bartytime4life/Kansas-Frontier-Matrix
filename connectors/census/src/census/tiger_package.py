"""Offline TIGER/Line package content inspection; never fetches or extracts to disk.

``tools/validators/source/tiger_line_kansas_core_reference.py`` proves the
committed manifest and, optionally, the exact bytes of an operator payload.
This module goes one step further for a single supplied package: it checks the
bytes against the manifest entry, then reads the zip in memory with bounds and
inspects the shapefile header, shape index, projection, and dBASE attributes
to establish structure, feature counts, identity uniqueness, and state/county
scope. It uses only the standard library and does not decode geometry.

TIGER/Line geometry is reference geometry, not legal-boundary, cadastral,
road-authority, or demographic authority. Nothing here admits a package.
"""
from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import io
import json
import math
from pathlib import Path
import re
import struct
import zipfile

MANIFEST_PATH = (Path(__file__).resolve().parents[2]
                 / "tiger-line-2025-kansas-core.source-reference.json")
FILE_NAME = re.compile(r"tl_(\d{4})_(us|\d{2}|\d{5})_([a-z0-9]+)\.zip\Z")
KANSAS_FIPS = "20"
# Context envelope, not the legal Kansas boundary.
KANSAS_CONTEXT = (-102.1, 36.9, -94.5, 40.1)
POLYGON, POLYLINE = 5, 3
PRODUCTS = {
    # file token: (manifest product, expected shape type, identity field)
    "areawater": ("AREAWATER", POLYGON, "HYDROID"),
    "linearwater": ("LINEARWATER", POLYLINE, "LINEARID"),
    "roads": ("ROADS", POLYLINE, "LINEARID"),
    "primaryroads": ("PRIMARYROADS", POLYLINE, "LINEARID"),
    "prisecroads": ("PRISECROADS", POLYLINE, "LINEARID"),
    "rails": ("RAILS", POLYLINE, "LINEARID"),
    "bg": ("BG", POLYGON, "GEOID"),
    "county": ("COUNTY", POLYGON, "GEOID"),
    "cousub": ("COUSUB", POLYGON, "GEOID"),
    "place": ("PLACE", POLYGON, "GEOID"),
    "state": ("STATE", POLYGON, "GEOID"),
    "tract": ("TRACT", POLYGON, "GEOID"),
    "tabblock20": ("TABBLOCK20", POLYGON, "GEOID20"),
    "zcta520": ("ZCTA520", POLYGON, "GEOID20"),
}
REQUIRED_SUFFIXES = (".shp", ".shx", ".dbf", ".prj")
OPTIONAL_SUFFIXES = (".cpg", ".shp.iso.xml", ".shp.ea.iso.xml")
MAX_TEXT_MEMBER = 256 * 1024
MAX_RATIO = 200


class TigerPackageError(ValueError):
    """Bounded, non-payload-bearing diagnostic for rejected package input."""


def load_manifest(path: Path = MANIFEST_PATH) -> dict[str, object]:
    return json.loads(path.read_text(encoding="utf-8"))


def manifest_entry(manifest: dict[str, object], file_name: str) -> dict[str, object]:
    """Return the manifest package entry for a file name, or fail closed."""
    inventory = manifest.get("inventory") if isinstance(manifest, dict) else None
    packages = inventory.get("packages") if isinstance(inventory, dict) else None
    if not isinstance(packages, list):
        raise TigerPackageError("MANIFEST_SHAPE")
    matches = [p for p in packages if isinstance(p, dict) and p.get("file_name") == file_name]
    if len(matches) != 1:
        raise TigerPackageError("NOT_IN_MANIFEST")
    return matches[0]


@dataclass(frozen=True)
class PackageName:
    vintage: int
    scope: str
    scope_code: str
    token: str
    product: str
    shape_type: int
    identity_field: str


def parse_file_name(file_name: object) -> PackageName:
    match = FILE_NAME.fullmatch(file_name) if isinstance(file_name, str) else None
    if match is None or match.group(3) not in PRODUCTS:
        raise TigerPackageError("FILE_NAME")
    code = match.group(2)
    scope = "national" if code == "us" else "state" if len(code) == 2 else "county"
    product, shape_type, identity = PRODUCTS[match.group(3)]
    return PackageName(int(match.group(1)), scope, code, match.group(3), product, shape_type,
                       identity)


def _read_member(archive: zipfile.ZipFile, info: zipfile.ZipInfo, limit: int) -> bytes:
    if info.file_size > limit:
        raise TigerPackageError("MEMBER_BOUND")
    with archive.open(info) as stream:
        data = stream.read(limit + 1)
    if len(data) > limit or len(data) != info.file_size:
        raise TigerPackageError("MEMBER_BOUND")
    return data


def _shape_header(data: bytes) -> tuple[int, int, tuple[float, float, float, float]]:
    if len(data) < 100:
        raise TigerPackageError("SHAPE_HEADER")
    code, = struct.unpack(">i", data[0:4])
    words, = struct.unpack(">i", data[24:28])
    version, shape_type = struct.unpack("<ii", data[28:36])
    bbox = struct.unpack("<4d", data[36:68])
    if code != 9994 or version != 1000 or words < 50:
        raise TigerPackageError("SHAPE_HEADER")
    if not all(math.isfinite(v) for v in bbox):
        raise TigerPackageError("SHAPE_BBOX")
    return shape_type, words * 2, bbox


@dataclass(frozen=True)
class DbfField:
    name: str
    kind: str
    length: int
    decimals: int


def _dbf(stream: io.BufferedIOBase, declared_size: int, wanted: tuple[str, ...]
         ) -> tuple[tuple[DbfField, ...], int, int, dict[str, list[str]]]:
    header = stream.read(32)
    if len(header) != 32 or header[0] not in (0x03, 0x83, 0x8B):
        raise TigerPackageError("DBF_HEADER")
    count, header_len, record_len = struct.unpack("<IHH", header[4:12])
    if header_len < 33 or (header_len - 33) % 32 or record_len < 1:
        raise TigerPackageError("DBF_HEADER")
    descriptors = stream.read(header_len - 32)
    if len(descriptors) != header_len - 32 or descriptors[-1:] != b"\r":
        raise TigerPackageError("DBF_HEADER")
    fields: list[DbfField] = []
    for offset in range(0, len(descriptors) - 1, 32):
        raw = descriptors[offset:offset + 32]
        name = raw[:11].split(b"\x00", 1)[0].decode("ascii", "strict")
        fields.append(DbfField(name, chr(raw[11]), raw[16], raw[17]))
    names = [field.name for field in fields]
    if len(set(names)) != len(names) or not names:
        raise TigerPackageError("DBF_FIELDS")
    if 1 + sum(field.length for field in fields) != record_len:
        raise TigerPackageError("DBF_RECORD_LENGTH")
    expected = header_len + count * record_len
    if declared_size not in (expected, expected + 1):  # optional 0x1A terminator
        raise TigerPackageError("DBF_SIZE")
    slices: dict[str, slice] = {}
    position = 1
    for field in fields:
        if field.name in wanted:
            slices[field.name] = slice(position, position + field.length)
        position += field.length
    values: dict[str, list[str]] = {name: [] for name in slices}
    deleted = 0
    for _ in range(count):
        record = stream.read(record_len)
        if len(record) != record_len:
            raise TigerPackageError("DBF_TRUNCATED")
        if record[:1] == b"*":
            deleted += 1
        elif record[:1] != b" ":
            raise TigerPackageError("DBF_RECORD_FLAG")
        for name, cut in slices.items():
            try:
                values[name].append(record[cut].decode("utf-8").strip())
            except UnicodeDecodeError:
                raise TigerPackageError("DBF_ENCODING") from None
    return tuple(fields), count, deleted, values


@dataclass(frozen=True)
class PackageCandidate:
    file_name: str
    product: str
    vintage: int
    scope: str
    package_sha256: str
    byte_length: int
    shape_type: int
    feature_count: int
    deleted_count: int
    bbox: tuple[float, float, float, float]
    crs: str
    fields: tuple[DbfField, ...]
    identity_field: str | None
    identity_digest: str | None
    kansas_feature_count: int | None
    members: tuple[str, ...]
    route: str
    reasons: tuple[str, ...]
    source_role: str = "REFERENCE_GEOMETRY_CANDIDATE"
    admission: str = "NOT_ADMITTED"


def inspect_package(source: bytes | Path, *, file_name: str, entry: dict[str, object],
                    max_bytes: int = 1024 * 1024 * 1024,
                    max_member_bytes: int = 2 * 1024 * 1024 * 1024) -> PackageCandidate:
    """Inspect one supplied package against its manifest entry; reject structural failure."""
    name = parse_file_name(file_name)
    if entry.get("file_name") != file_name or entry.get("product") != name.product:
        raise TigerPackageError("MANIFEST_ENTRY_MISMATCH")
    if isinstance(source, Path):
        if source.is_symlink() or not source.is_file():
            raise TigerPackageError("SOURCE_PATH")
        size = source.stat().st_size
        opener = lambda: source.open("rb")  # noqa: E731
    elif isinstance(source, bytes):
        size = len(source)
        opener = lambda: io.BytesIO(source)  # noqa: E731
    else:
        raise TigerPackageError("SOURCE_TYPE")
    if size > max_bytes:
        raise TigerPackageError("PACKAGE_BOUND")
    if size != entry.get("byte_length"):
        raise TigerPackageError("SIZE_MISMATCH")
    digest = sha256()
    with opener() as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    if digest.hexdigest() != entry.get("sha256"):
        raise TigerPackageError("SHA256_MISMATCH")

    reasons: list[str] = []
    stem = file_name[:-4]
    try:
        with opener() as stream, zipfile.ZipFile(stream) as archive:
            infos = archive.infolist()
            by_name: dict[str, zipfile.ZipInfo] = {}
            for info in infos:
                if ("/" in info.filename or "\\" in info.filename or info.is_dir()
                        or info.filename in by_name):
                    raise TigerPackageError("MEMBER_PATH")
                if info.file_size > max_member_bytes or (
                        info.compress_size and info.file_size / info.compress_size > MAX_RATIO):
                    raise TigerPackageError("MEMBER_BOUND")
                by_name[info.filename] = info
            for suffix in REQUIRED_SUFFIXES:
                if stem + suffix not in by_name:
                    raise TigerPackageError("MEMBER_MISSING")
            known = {stem + s for s in REQUIRED_SUFFIXES + OPTIONAL_SUFFIXES}
            if set(by_name) - known:
                reasons.append("UNEXPECTED_MEMBER")
            # Only the 100-byte headers are read; geometry records are never decoded.
            with archive.open(by_name[stem + ".shp"]) as shp:
                shape_type, shp_len, bbox = _shape_header(shp.read(100))
            if shp_len != by_name[stem + ".shp"].file_size:
                raise TigerPackageError("SHAPE_LENGTH")
            with archive.open(by_name[stem + ".shx"]) as shx:
                shx_type, shx_len, _ = _shape_header(shx.read(100))
            if shx_len != by_name[stem + ".shx"].file_size or (shx_len - 100) % 8:
                raise TigerPackageError("SHAPE_INDEX_LENGTH")
            if shx_type != shape_type:
                raise TigerPackageError("SHAPE_TYPE_MISMATCH")
            index_count = (shx_len - 100) // 8
            prj = _read_member(archive, by_name[stem + ".prj"], MAX_TEXT_MEMBER)
            if stem + ".cpg" in by_name:
                cpg = _read_member(archive, by_name[stem + ".cpg"], 64).strip().upper()
                if cpg not in (b"UTF-8", b"UTF8"):
                    reasons.append("ENCODING_NOT_UTF8")
            wanted = (name.identity_field, "STATEFP", "STATEFP20", "COUNTYFP", "COUNTYFP20")
            with archive.open(by_name[stem + ".dbf"]) as dbf_stream:
                fields, count, deleted, values = _dbf(
                    dbf_stream, by_name[stem + ".dbf"].file_size, wanted)
    except zipfile.BadZipFile:
        raise TigerPackageError("ZIP_INVALID") from None
    except (EOFError, OSError, struct.error, UnicodeDecodeError):
        raise TigerPackageError("ZIP_MEMBER_CORRUPT") from None

    if count != index_count:
        raise TigerPackageError("FEATURE_COUNT_MISMATCH")
    if deleted:
        reasons.append("DELETED_RECORDS_PRESENT")
    if shape_type != name.shape_type:
        reasons.append("SHAPE_TYPE_UNEXPECTED")
    west, south, east, north = bbox
    if count and not (-180 <= west <= east <= 180 and -90 <= south <= north <= 90):
        reasons.append("BBOX_NOT_GEOGRAPHIC")
    text = prj.decode("ascii", "replace")
    crs = ("NAD83_GEOGRAPHIC" if text.startswith("GEOGCS[") and "North_American_1983" in text
           else "UNRECOGNIZED")
    if crs == "UNRECOGNIZED":
        reasons.append("CRS_UNRECOGNIZED")

    identity_digest = None
    identity_field = name.identity_field if name.identity_field in values else None
    if identity_field is None:
        reasons.append("IDENTITY_FIELD_ABSENT")
    else:
        ids = values[identity_field]
        if any(not item for item in ids):
            reasons.append("IDENTITY_EMPTY")
        if len(set(ids)) != len(ids):
            reasons.append("IDENTITY_DUPLICATE")
        identity_digest = "sha256:" + sha256("\n".join(sorted(ids)).encode()).hexdigest()

    state_values = values.get("STATEFP") or values.get("STATEFP20")
    county_values = values.get("COUNTYFP") or values.get("COUNTYFP20")
    kansas_count = None
    if state_values is not None:
        kansas_count = sum(1 for value in state_values if value == KANSAS_FIPS)
    if name.scope in ("state", "county"):
        if name.scope_code[:2] != KANSAS_FIPS:
            reasons.append("STATE_OUTSIDE_KANSAS_SCOPE")
        if state_values is not None and kansas_count != len(state_values):
            reasons.append("STATE_SCOPE_MISMATCH")
        if (name.scope == "county" and county_values is not None
                and any(value != name.scope_code[2:] for value in county_values)):
            reasons.append("COUNTY_SCOPE_MISMATCH")
        k_west, k_south, k_east, k_north = KANSAS_CONTEXT
        if count and (east < k_west or west > k_east or north < k_south or south > k_north):
            reasons.append("BBOX_OUTSIDE_KANSAS_CONTEXT")
    elif state_values is None:
        reasons.append("NATIONAL_PACKAGE_REQUIRES_SPATIAL_SELECTION")
    else:
        reasons.append("NATIONAL_PACKAGE_ATTRIBUTE_SELECTION_ONLY")

    flags = {"NATIONAL_PACKAGE_REQUIRES_SPATIAL_SELECTION",
             "NATIONAL_PACKAGE_ATTRIBUTE_SELECTION_ONLY"}
    blocking = [reason for reason in reasons if reason not in flags]
    return PackageCandidate(
        file_name, name.product, name.vintage, name.scope, "sha256:" + digest.hexdigest(), size,
        shape_type, count, deleted, bbox, crs, fields, identity_field, identity_digest,
        kansas_count, tuple(sorted(by_name)),
        "QUARANTINE_CANDIDATE" if blocking else "RAW_CANDIDATE", tuple(reasons))
