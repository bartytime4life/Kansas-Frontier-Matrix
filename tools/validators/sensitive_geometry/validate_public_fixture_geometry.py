#!/usr/bin/env python3
"""Fail closed when a positive fixture carries precise coordinates publicly.

Scans JSON and GeoJSON fixtures for coordinate-bearing values: GeoJSON
``coordinates`` and ``bbox`` arrays, paired latitude/longitude fields, WKT
strings, and JSON documents embedded in string values. A location is precise
when either axis literal carries more decimal places than the coarse synthetic
fixtures in this repository use. A precise location passes only when an
enclosing record explicitly declares it non-public and no enclosing record
declares it public.

Expected-negative fixture lanes (``invalid``, ``*_invalid``, ``negative``,
``deny`` and similar) are skipped because they deliberately carry defects.

The validator is deterministic and no-network. Findings name files and JSON
paths only; coordinate values are never echoed.
"""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from collections.abc import Iterator, Sequence
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
DEFAULT_ROOT = REPO_ROOT / "fixtures"
FIXTURE_SUFFIXES = frozenset({".json", ".geojson"})
MAX_FIXTURE_BYTES = 5_000_000
MAX_EMBEDDED_JSON_DEPTH = 4

# Literals with this many decimal places resolve below roughly 110 m.
PRECISE_DECIMAL_PLACES = 3

NEGATIVE_DIR_NAMES = frozenset({"invalid", "negative", "deny"})
NEGATIVE_DIR_PATTERN = re.compile(r"^invalid_|_(?:invalid|deny)$")

LAT_LON_KEY_PAIRS = (
    ("latitude", "longitude"),
    ("lat", "lon"),
    ("lat", "lng"),
    ("decimallatitude", "decimallongitude"),
)
EXPOSURE_KEYS = frozenset({"coordinate_exposure", "geometry_exposure"})
NON_PUBLIC_EXPOSURE_VALUES = frozenset({"RESTRICTED", "STEWARD_ONLY", "WITHHELD"})

WKT_VALUE = re.compile(
    r"^\s*(?:SRID=\d+\s*;\s*)?(?:POINT|LINESTRING|POLYGON|MULTIPOINT|"
    r"MULTILINESTRING|MULTIPOLYGON|GEOMETRYCOLLECTION)\s*(?:Z|M|ZM)?\s*\(",
    re.IGNORECASE,
)
NUMBER_LITERAL = re.compile(r"-?\d+(?:\.(\d+))?")

SCOPE = "public-fixture-precise-geometry"

# Reviewed, repository-relative exceptions for source-native inputs whose wire
# format cannot carry a KFM posture field. Each entry must keep matching: an
# exempt file that disappears or stops carrying precise geometry is reported
# as stale so the list cannot silently outlive its reason.
EXEMPTIONS: dict[str, str] = {
    "fixtures/domains/flora/flora_occurrence_candidate/input/gbif_big_bluestem.json": (
        "Synthetic GBIF Darwin Core source-native input; the normalizer emits "
        "the derived candidate as INTERNAL_EXACT with public_use_allowed false."
    ),
}


@dataclass(frozen=True, order=True)
class Finding:
    """A stable machine-readable finding without candidate values."""

    file: str
    code: str
    path: str


@dataclass(frozen=True)
class _Posture:
    non_public: bool = False
    public: bool = False

    def merge(self, other: _Posture) -> _Posture:
        return _Posture(
            non_public=self.non_public or other.non_public,
            public=self.public or other.public,
        )


def _decimal_places(value: object) -> int:
    if isinstance(value, float) and math.isfinite(value):
        value = Decimal(repr(value))
    if isinstance(value, Decimal):
        exponent = value.as_tuple().exponent
        return max(0, -exponent) if isinstance(exponent, int) else 0
    return 0


def _is_number(value: object) -> bool:
    return isinstance(value, (int, float, Decimal)) and not isinstance(value, bool)


def _is_position(value: object) -> bool:
    return (
        isinstance(value, list)
        and len(value) in (2, 3)
        and all(_is_number(item) for item in value)
    )


def _positions_are_precise(value: object) -> bool:
    if _is_position(value):
        return any(
            _decimal_places(axis) >= PRECISE_DECIMAL_PLACES for axis in value[:2]
        )
    if isinstance(value, list):
        return any(_positions_are_precise(item) for item in value)
    return False


def _bbox_is_precise(value: object) -> bool:
    return (
        isinstance(value, list)
        and len(value) in (4, 6)
        and all(_is_number(item) for item in value)
        and any(_decimal_places(item) >= PRECISE_DECIMAL_PLACES for item in value)
    )


def _wkt_is_precise(value: str) -> bool:
    if not WKT_VALUE.match(value):
        return False
    return any(
        len(match.group(1) or "") >= PRECISE_DECIMAL_PLACES
        for match in NUMBER_LITERAL.finditer(value)
    )


def _own_posture(record: dict) -> _Posture:
    posture = _Posture()
    for key, value in record.items():
        if not isinstance(key, str):
            continue
        normalized = key.casefold()
        if normalized == "public_use_allowed":
            if value is False:
                posture = posture.merge(_Posture(non_public=True))
            elif value is True:
                posture = posture.merge(_Posture(public=True))
        elif normalized in EXPOSURE_KEYS and isinstance(value, str):
            exposure = value.upper()
            if exposure.startswith("INTERNAL") or exposure in NON_PUBLIC_EXPOSURE_VALUES:
                posture = posture.merge(_Posture(non_public=True))
            elif exposure.startswith("PUBLIC"):
                posture = posture.merge(_Posture(public=True))
    return posture


def _record_posture(record: dict) -> _Posture:
    posture = _own_posture(record)
    governance = record.get("governance")
    if isinstance(governance, dict):
        posture = posture.merge(_own_posture(governance))
    return posture


def _parse_number(raw: str) -> Decimal:
    value = Decimal(raw)
    if not value.is_finite():
        raise ValueError("JSON number is not finite")
    return value


def _reject_constant(_raw: str) -> None:
    raise ValueError("non-standard JSON numeric constant")


def _loads(text: str) -> object:
    return json.loads(
        text,
        parse_float=_parse_number,
        parse_int=_parse_number,
        parse_constant=_reject_constant,
    )


def _try_embedded_json(value: str) -> object | None:
    stripped = value.lstrip()
    if not stripped.startswith(("{", "[")):
        return None
    try:
        return _loads(value)
    except (ValueError, InvalidOperation, RecursionError):
        return None


def _scan(
    value: object,
    path: str,
    posture: _Posture,
    embedded_depth: int,
) -> Iterator[tuple[str, _Posture]]:
    """Yield the path and inherited posture of every precise location."""

    if isinstance(value, dict):
        posture = posture.merge(_record_posture(value))
        if "coordinates" in value and _positions_are_precise(value["coordinates"]):
            yield f"{path}.coordinates", posture
        if "bbox" in value and _bbox_is_precise(value["bbox"]):
            yield f"{path}.bbox", posture
        folded = {
            key.casefold(): key for key in value if isinstance(key, str)
        }
        for lat_key, lon_key in LAT_LON_KEY_PAIRS:
            if lat_key in folded and lon_key in folded:
                lat = value[folded[lat_key]]
                lon = value[folded[lon_key]]
                if (
                    _is_number(lat)
                    and _is_number(lon)
                    and max(_decimal_places(lat), _decimal_places(lon))
                    >= PRECISE_DECIMAL_PLACES
                ):
                    yield f"{path}.{folded[lat_key]}", posture
        for key, child in value.items():
            yield from _scan(child, f"{path}.{key}", posture, embedded_depth)
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from _scan(child, f"{path}[{index}]", posture, embedded_depth)
    elif isinstance(value, str):
        if _wkt_is_precise(value):
            yield path, posture
        elif embedded_depth < MAX_EMBEDDED_JSON_DEPTH:
            embedded = _try_embedded_json(value)
            if embedded is not None:
                yield from _scan(embedded, path, posture, embedded_depth + 1)


def validate_document(document: object, file: str = "<memory>") -> list[Finding]:
    findings: set[Finding] = set()
    for path, posture in _scan(document, "$", _Posture(), 0):
        if posture.public:
            findings.add(Finding(file, "PRECISE_GEOMETRY_DECLARED_PUBLIC", path))
        elif not posture.non_public:
            findings.add(
                Finding(file, "PRECISE_GEOMETRY_WITHOUT_NON_PUBLIC_DECLARATION", path)
            )
    return sorted(findings)


def _repo_relative(path: Path) -> str | None:
    try:
        return path.resolve().relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return None


def validate_file(path: Path) -> list[Finding]:
    file = _repo_relative(path) or path.as_posix()
    try:
        if path.stat().st_size > MAX_FIXTURE_BYTES:
            return [Finding(file, "FIXTURE_TOO_LARGE", "$")]
        document = _loads(path.read_text(encoding="utf-8"))
        return validate_document(document, file)
    except (OSError, UnicodeError, ValueError, InvalidOperation, RecursionError):
        return [Finding(file, "FIXTURE_JSON_INVALID", "$")]


def is_expected_negative(relative: Path) -> bool:
    return any(
        part in NEGATIVE_DIR_NAMES or NEGATIVE_DIR_PATTERN.search(part)
        for part in relative.parts[:-1]
    )


def iter_fixture_files(root: Path) -> Iterator[Path]:
    if root.is_file():
        yield root
        return
    for path in sorted(root.rglob("*")):
        if (
            path.suffix in FIXTURE_SUFFIXES
            and path.is_file()
            and not path.is_symlink()
            and not is_expected_negative(path.relative_to(root))
        ):
            yield path


def _is_within(path: Path, root: Path) -> bool:
    resolved_root = root.resolve()
    return path == resolved_root or resolved_root in path.parents


def validate_paths(
    roots: Sequence[Path],
    exemptions: dict[str, str] | None = None,
) -> tuple[int, list[Finding]]:
    exemptions = EXEMPTIONS if exemptions is None else exemptions
    scanned = 0
    findings: list[Finding] = []
    exempt_matched: set[str] = set()
    for root in roots:
        for path in iter_fixture_files(root):
            scanned += 1
            file_findings = validate_file(path)
            relative = _repo_relative(path)
            if relative in exemptions and file_findings:
                exempt_matched.add(relative)
                continue
            findings.extend(file_findings)

    for relative in sorted(exemptions):
        exempt_path = REPO_ROOT / relative
        if relative in exempt_matched:
            continue
        if any(_is_within(exempt_path, root) for root in roots):
            findings.append(Finding(relative, "EXEMPTION_STALE", "$"))
    return scanned, sorted(findings)


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "paths",
        nargs="*",
        type=Path,
        default=[DEFAULT_ROOT],
        help="fixture files or directories to scan (default: repository fixtures/)",
    )
    args = parser.parse_args(argv)

    missing = [path for path in args.paths if not path.exists()]
    if missing:
        for path in missing:
            print(f"path not found: {path}", file=sys.stderr)
        return 2

    scanned, findings = validate_paths(args.paths)
    for finding in findings:
        print(
            json.dumps(
                {"code": finding.code, "file": finding.file, "path": finding.path},
                sort_keys=True,
                separators=(",", ":"),
            )
        )
    print(
        json.dumps(
            {
                "files_scanned": scanned,
                "findings": len(findings),
                "scope": SCOPE,
                "status": "FAIL" if findings else "PASS",
            },
            sort_keys=True,
            separators=(",", ":"),
        )
    )
    return 1 if findings else 0


if __name__ == "__main__":
    raise SystemExit(main())
