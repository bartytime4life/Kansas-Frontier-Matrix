"""Deterministic no-network tests for the Census county archive inspector."""

from __future__ import annotations

import io
import re
import socket
import struct
import tempfile
import unittest
import urllib.request
import zipfile
from pathlib import Path
from unittest.mock import patch

import yaml

from tools.validators.source.census_cartographic_boundary_counties import (
    ARCHIVE_BASENAME,
    EXPECTED_FIELDS,
    ArchiveExpectations,
    ArchiveValidationError,
    inspect_archive,
)


KANSAS_GEOIDS = tuple(f"20{county:03d}" for county in range(1, 210, 2))
SYNTHETIC_BBOX = (-102.1, 36.9, -94.5, 40.1)
FIELD_WIDTHS = {
    "STATEFP": 2,
    "COUNTYFP": 3,
    "COUNTYNS": 8,
    "GEOIDFQ": 14,
    "GEOID": 5,
    "NAME": 16,
    "NAMELSAD": 20,
    "STUSPS": 2,
    "STATE_NAME": 6,
    "LSAD": 2,
    "ALAND": 12,
    "AWATER": 12,
}
NO_AUTHORITY_FLAGS = (
    "source_payload_committed",
    "source_activation_authorized",
    "evidence_bundle_emitted",
    "public_release_allowed",
    "map_runtime_binding_allowed",
)
REPO_ROOT = Path(__file__).resolve().parents[2]
WORKFLOW_PATH = REPO_ROOT / ".github/workflows/census-county-reference-candidate.yml"
AUTHORING_MERGE_REF = "648f6fc0abaed6b787bb60f669f89b9e38162ec9"


def _unexpected_network(*_args, **_kwargs):
    raise AssertionError("Census archive validation attempted network access")


def _shape_header(total_bytes: int) -> bytes:
    header = bytearray(100)
    struct.pack_into(">i", header, 0, 9994)
    struct.pack_into(">i", header, 24, total_bytes // 2)
    struct.pack_into("<i", header, 28, 1000)
    struct.pack_into("<i", header, 32, 5)
    struct.pack_into("<4d", header, 36, *SYNTHETIC_BBOX)
    return bytes(header)


def _shape_members(record_count: int) -> tuple[bytes, bytes]:
    record_payloads: list[bytes] = []
    index_entries: list[bytes] = []
    offset_words = 50
    for index in range(record_count):
        west = -101.9 + index * 0.001
        south = 37.0 + index * 0.001
        bbox = (west, south, west + 0.01, south + 0.01)
        content = struct.pack("<i4d", 5, *bbox)
        content_words = len(content) // 2
        record_payloads.append(struct.pack(">2i", index + 1, content_words) + content)
        index_entries.append(struct.pack(">2i", offset_words, content_words))
        offset_words += 4 + content_words

    shape_body = b"".join(record_payloads)
    index_body = b"".join(index_entries)
    return (
        _shape_header(100 + len(shape_body)) + shape_body,
        _shape_header(100 + len(index_body)) + index_body,
    )


def _dbf_member(geoids: tuple[str, ...]) -> bytes:
    fields = tuple((name, FIELD_WIDTHS[name]) for name in EXPECTED_FIELDS)
    header_length = 32 + 32 * len(fields) + 1
    record_length = 1 + sum(width for _, width in fields)
    header = bytearray(header_length)
    header[0] = 0x03
    header[1:4] = bytes((126, 5, 1))
    struct.pack_into("<I", header, 4, len(geoids))
    struct.pack_into("<H", header, 8, header_length)
    struct.pack_into("<H", header, 10, record_length)

    cursor = 32
    for name, width in fields:
        descriptor = bytearray(32)
        encoded_name = name.encode("ascii")
        descriptor[: len(encoded_name)] = encoded_name
        descriptor[11] = ord("C")
        descriptor[16] = width
        header[cursor : cursor + 32] = descriptor
        cursor += 32
    header[cursor] = 0x0D

    records: list[bytes] = []
    for index, geoid in enumerate(geoids):
        county_code = geoid[-3:]
        values = {
            "STATEFP": "20",
            "COUNTYFP": county_code,
            "COUNTYNS": f"{index + 1:08d}",
            "GEOIDFQ": f"0500000US{geoid}",
            "GEOID": geoid,
            "NAME": f"County {county_code}",
            "NAMELSAD": f"County {county_code}",
            "STUSPS": "KS",
            "STATE_NAME": "Kansas",
            "LSAD": "06",
            "ALAND": str(1_000_000 + index),
            "AWATER": str(index),
        }
        record = bytearray(b" ")
        for name, width in fields:
            encoded = values[name].encode("utf-8")
            if len(encoded) > width:
                raise AssertionError(f"synthetic {name} value exceeds DBF width")
            record.extend(encoded.ljust(width, b" "))
        records.append(bytes(record))
    return bytes(header) + b"".join(records) + b"\x1a"


def _valid_members() -> dict[str, bytes]:
    shp, shx = _shape_members(len(KANSAS_GEOIDS))
    metadata = (
        "<metadata>"
        "2025 Cartographic Boundary File (SHP), County and Equivalent for "
        "United States, 1:500,000"
        "<crs>urn:ogc:def:crs:EPSG::4269</crs>"
        f"<gco:Integer>{len(KANSAS_GEOIDS)}</gco:Integer>"
        "<gco:Date>2026-05</gco:Date>"
        "</metadata>"
    ).encode("utf-8")
    return {
        f"{ARCHIVE_BASENAME}.shp.ea.iso.xml": b"<metadata>synthetic</metadata>",
        f"{ARCHIVE_BASENAME}.shp.iso.xml": metadata,
        f"{ARCHIVE_BASENAME}.shp": shp,
        f"{ARCHIVE_BASENAME}.shx": shx,
        f"{ARCHIVE_BASENAME}.dbf": _dbf_member(KANSAS_GEOIDS),
        f"{ARCHIVE_BASENAME}.prj": (
            b'GEOGCS["GCS_North_American_1983",DATUM["D_North_American_1983",'
            b'SPHEROID["GRS_1980",6378137,298.257222101]]]'
        ),
        f"{ARCHIVE_BASENAME}.cpg": b"UTF-8\n",
    }


def _archive_bytes(
    *,
    overrides: dict[str, bytes] | None = None,
    extra_members: dict[str, bytes] | None = None,
) -> bytes:
    members = _valid_members()
    if overrides:
        members.update(overrides)
    if extra_members:
        members.update(extra_members)

    stream = io.BytesIO()
    with zipfile.ZipFile(stream, "w", compression=zipfile.ZIP_STORED) as archive:
        for name in sorted(members):
            info = zipfile.ZipInfo(name, date_time=(2025, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_STORED
            archive.writestr(info, members[name])
    return stream.getvalue()


class CensusCartographicBoundaryCountiesTests(unittest.TestCase):
    def setUp(self) -> None:
        self._temporary_directory = tempfile.TemporaryDirectory()
        self.addCleanup(self._temporary_directory.cleanup)
        self.root = Path(self._temporary_directory.name)
        self.expectations = ArchiveExpectations(
            national_feature_count=len(KANSAS_GEOIDS),
            kansas_feature_count=len(KANSAS_GEOIDS),
            kansas_geoids=KANSAS_GEOIDS,
        )

        patchers = (
            patch.object(socket.socket, "connect", _unexpected_network),
            patch.object(socket, "create_connection", _unexpected_network),
            patch.object(urllib.request, "urlopen", _unexpected_network),
        )
        for patcher in patchers:
            patcher.start()
            self.addCleanup(patcher.stop)

    def _write(self, payload: bytes, name: str = "synthetic-counties.zip") -> Path:
        path = self.root / name
        path.write_bytes(payload)
        return path

    def _assert_code(self, expected: str, archive_path: Path) -> None:
        with self.assertRaises(ArchiveValidationError) as caught:
            inspect_archive(archive_path, expectations=self.expectations)
        self.assertEqual(caught.exception.code, expected)

    def test_exact_105_kansas_geoids_and_no_authority_flags(self) -> None:
        self.assertEqual(len(KANSAS_GEOIDS), 105)
        archive_path = self._write(_archive_bytes())

        summary = inspect_archive(archive_path, expectations=self.expectations)

        self.assertEqual(summary["archive_member_count"], 7)
        self.assertEqual(summary["national_feature_count"], 105)
        self.assertEqual(summary["kansas_feature_count"], 105)
        self.assertEqual(summary["kansas_unique_geoid_count"], 105)
        self.assertEqual(summary["kansas_first_geoid"], "20001")
        self.assertEqual(summary["kansas_last_geoid"], "20209")
        self.assertEqual(summary["kansas_filter"], "STATEFP=20")
        self.assertEqual(summary["fields"], list(EXPECTED_FIELDS))
        self.assertEqual(
            {name: summary[name] for name in NO_AUTHORITY_FLAGS},
            {name: False for name in NO_AUTHORITY_FLAGS},
        )

        wrong_geoids = KANSAS_GEOIDS[:-1] + ("20999",)
        with self.assertRaises(ArchiveValidationError) as caught:
            inspect_archive(
                archive_path,
                expectations=ArchiveExpectations(
                    national_feature_count=105,
                    kansas_feature_count=105,
                    kansas_geoids=wrong_geoids,
                ),
            )
        self.assertEqual(caught.exception.code, "KANSAS_GEOID_SET_MISMATCH")

    def test_archive_corruption_fails_closed_with_finite_codes(self) -> None:
        corrupt_zip = self._write(b"not a ZIP archive", "corrupt.zip")
        self._assert_code("ARCHIVE_INVALID", corrupt_zip)

        truncated_shape = self._write(
            _archive_bytes(
                overrides={f"{ARCHIVE_BASENAME}.shp": b"truncated"}
            ),
            "truncated-shape.zip",
        )
        self._assert_code("SHP_HEADER_TRUNCATED", truncated_shape)

    def test_archive_paths_fail_closed(self) -> None:
        traversal = self._write(
            _archive_bytes(extra_members={"../escape.txt": b"blocked"}),
            "traversal.zip",
        )
        self._assert_code("ARCHIVE_MEMBER_PATH_INVALID", traversal)

        target = self._write(_archive_bytes(), "target.zip")
        symlink = self.root / "linked.zip"
        symlink.symlink_to(target.name)
        self._assert_code("ARCHIVE_NOT_FILE", symlink)

    def test_inspection_succeeds_while_network_is_denied(self) -> None:
        archive_path = self._write(_archive_bytes(), "no-network.zip")
        summary = inspect_archive(archive_path, expectations=self.expectations)
        self.assertEqual(
            summary["profile"],
            "kfm.census.cartographic-boundary-counties.archive-inspection.v1",
        )


class CensusCountyReferenceWorkflowBindingTests(unittest.TestCase):
    def test_workflow_replays_immutable_receipt_at_exact_merge_ref(self) -> None:
        workflow = yaml.safe_load(WORKFLOW_PATH.read_text(encoding="utf-8"))
        steps = workflow["jobs"]["validate-reference-candidate"]["steps"]

        checkout_steps = [
            step
            for step in steps
            if str(step.get("uses", "")).startswith("actions/checkout@")
        ]
        self.assertEqual(len(checkout_steps), 1)
        self.assertEqual(checkout_steps[0]["with"]["fetch-depth"], 0)
        self.assertFalse(checkout_steps[0]["with"]["persist-credentials"])

        receipt_steps = [
            step
            for step in steps
            if "validate_generated_receipt.py" in str(step.get("run", ""))
            and "genrec-census-county-reference-candidate-20260910.json"
            in str(step.get("run", ""))
        ]
        self.assertEqual(len(receipt_steps), 1)
        receipt_command = receipt_steps[0]["run"]
        artifact_refs = re.findall(
            r"--artifact-git-ref\s+([0-9a-f]{40})", receipt_command
        )
        self.assertEqual(artifact_refs, [AUTHORING_MERGE_REF])


if __name__ == "__main__":
    unittest.main()
