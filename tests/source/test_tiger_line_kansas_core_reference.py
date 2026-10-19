"""Deterministic no-network tests for the TIGER/Line Kansas reference manifest."""

from __future__ import annotations

import copy
import hashlib
import io
import json
import socket
import tempfile
import unittest
import urllib.request
import zipfile
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
from unittest.mock import patch

from tools.validators.source import tiger_line_kansas_core_reference as reference
from tools.validators.source.tiger_line_kansas_core_reference import (
    EXPECTED_KANSAS_COUNTY_GEOIDS,
    EXPECTED_PACKAGE_INDEX_SHA256,
    ReferenceValidationError,
    validate_manifest,
    validation_summary,
    verify_payload_root,
)


REPO_ROOT = Path(__file__).resolve().parents[2]
MANIFEST_PATH = (
    REPO_ROOT
    / "connectors/census/tiger-line-2025-kansas-core.source-reference.json"
)


def _unexpected_network(*_args, **_kwargs):
    raise AssertionError("TIGER/Line reference validation attempted network access")


def _manifest() -> dict[str, object]:
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


class TigerLineKansasCoreReferenceTests(unittest.TestCase):
    def test_committed_reference_is_exact_and_non_authoritative(self) -> None:
        document = _manifest()
        with (
            patch.object(socket.socket, "connect", _unexpected_network),
            patch.object(socket, "create_connection", _unexpected_network),
            patch.object(urllib.request, "urlopen", _unexpected_network),
        ):
            self.assertEqual(validate_manifest(document), [])
            first = validation_summary(document)
            second = validation_summary(document)

        self.assertEqual(first, second)
        self.assertEqual(first["status"], "PASS")
        self.assertEqual(first["package_count"], 326)
        self.assertEqual(first["total_bytes"], 991_516_458)
        self.assertEqual(
            first["package_index_sha256"], EXPECTED_PACKAGE_INDEX_SHA256
        )
        governance = first["governance"]
        self.assertIsInstance(governance, dict)
        self.assertTrue(all(value is False for value in governance.values()))
        self.assertNotIn("drive.google.com", json.dumps(document).lower())

    def test_each_county_product_has_all_105_kansas_counties(self) -> None:
        packages = _manifest()["inventory"]["packages"]
        for product, suffix in {
            "AREAWATER": "areawater",
            "LINEARWATER": "linearwater",
            "ROADS": "roads",
        }.items():
            with self.subTest(product=product):
                expected = {
                    f"tl_2025_{geoid}_{suffix}.zip"
                    for geoid in EXPECTED_KANSAS_COUNTY_GEOIDS
                }
                observed = {
                    package["file_name"]
                    for package in packages
                    if package["product"] == product
                }
                self.assertEqual(observed, expected)

    def test_reference_mutations_fail_closed(self) -> None:
        cases = [
            ("missing_county", "PACKAGE_COUNT_MISMATCH"),
            ("wrong_county_fips", "PRODUCT_PACKAGE_SET_MISMATCH"),
            ("duplicate_file", "DUPLICATE_FILE_NAME"),
            ("altered_digest", "PACKAGE_INDEX_SHA256_MISMATCH"),
            ("wrong_host", "SOURCE_URL_INVALID"),
            ("authority_escalation", "GOVERNANCE_ESCALATION"),
            ("total_mismatch", "TOTAL_BYTES_MISMATCH"),
            ("private_locator", "PRIVATE_LOCATOR_PRESENT"),
        ]
        for mutation, expected_code in cases:
            with self.subTest(mutation=mutation):
                document = copy.deepcopy(_manifest())
                inventory = document["inventory"]
                packages = inventory["packages"]

                if mutation == "missing_county":
                    packages.pop(0)
                elif mutation == "wrong_county_fips":
                    package = packages[0]
                    package["file_name"] = "tl_2025_20002_areawater.zip"
                    package["source_url"] = (
                        "https://www2.census.gov/geo/tiger/TIGER2025/AREAWATER/"
                        "tl_2025_20002_areawater.zip"
                    )
                elif mutation == "duplicate_file":
                    packages[1]["file_name"] = packages[0]["file_name"]
                    packages[1]["source_url"] = packages[0]["source_url"]
                elif mutation == "altered_digest":
                    packages[0]["sha256"] = "0" * 64
                elif mutation == "wrong_host":
                    packages[0]["source_url"] = (
                        "https://example.com/geo/tiger/TIGER2025/AREAWATER/"
                        "tl_2025_20001_areawater.zip"
                    )
                elif mutation == "authority_escalation":
                    document["governance"]["publication_authorized"] = True
                elif mutation == "total_mismatch":
                    inventory["total_bytes"] += 1
                elif mutation == "private_locator":
                    document["capture"]["operator_drive_url"] = (
                        "https://drive.google.com/drive/folders/private"
                    )
                else:  # pragma: no cover - cases and branch table stay aligned.
                    raise AssertionError(f"unknown mutation: {mutation}")

                self.assertIn(expected_code, validate_manifest(document))

    def test_malformed_values_are_findings_and_identity_is_type_exact(self) -> None:
        cases = {
            "product is a list": (lambda d: d["inventory"]["packages"][0].update(product=["ROADS"]), "PRODUCT_INVALID"),
            "capture flag is 0": (lambda d: d["capture"].update(private_locator_committed=0), "CAPTURE_IDENTITY_INVALID"),
            "scope count is a float": (lambda d: d["scope"].update(county_count=105.0), "SCOPE_INVALID"),
            "source vintage is a string": (lambda d: d["source"].update(vintage="2025"), "SOURCE_IDENTITY_INVALID"),
            "product count is a float": (lambda d: d["inventory"]["product_counts"].update(BG=1.0), "PRODUCT_COUNTS_MISMATCH"),
            "package count is a float": (lambda d: d["inventory"].update(package_count=326.0), "PACKAGE_COUNT_MISMATCH"),
            "total bytes is a float": (lambda d: d["inventory"].update(total_bytes=float(d["inventory"]["total_bytes"])),
                                       "TOTAL_BYTES_MISMATCH"),
            "governance flag is 0": (lambda d: d["governance"].update(release_authorized=0), "GOVERNANCE_ESCALATION"),
        }
        for name, (change, code) in cases.items():
            with self.subTest(name):
                document = copy.deepcopy(_manifest())
                change(document)
                self.assertIn(code, validate_manifest(document))
        self.assertEqual(validate_manifest(["not", "an", "object"]), ["DOCUMENT_NOT_OBJECT"])

    def test_cli_reports_pass_and_failures(self) -> None:
        def run(*argv: str) -> tuple[int, str, str]:
            out, err = io.StringIO(), io.StringIO()
            with patch("sys.argv", ["reference", *argv]), redirect_stdout(out), redirect_stderr(err):
                code = reference.main()
            return code, out.getvalue(), err.getvalue()

        code, out, _ = run()
        self.assertEqual((code, json.loads(out)["status"]), (0, "PASS"))
        self.assertEqual(run("--check-zip-crc")[::2], (2, "PAYLOAD_ROOT_REQUIRED_FOR_ZIP_CRC\n"))
        with tempfile.TemporaryDirectory() as directory:
            broken = Path(directory) / "manifest.json"
            broken.write_text("{", encoding="utf-8")
            self.assertEqual(run("--manifest", str(broken))[::2], (1, "MANIFEST_READ_INVALID\n"))
            broken.write_text(json.dumps({**_manifest(), "status": "ACTIVE"}), encoding="utf-8")
            self.assertEqual(run("--manifest", str(broken))[::2], (1, "STATUS_INVALID\n"))
            self.assertEqual(run("--payload-root", directory)[::2], (1, "PAYLOAD_FILE_INVALID\n"))


def _zip_bytes(name: str, content: bytes) -> bytes:
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w", compression=zipfile.ZIP_STORED) as archive:
        archive.writestr(name, content)
    return buffer.getvalue()


class PayloadRootVerificationTests(unittest.TestCase):
    """verify_payload_root over a small synthetic payload; manifest checks are covered above."""

    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name) / "payload"
        self.packages = []
        for product, file_name in (("ROADS", "tl_2025_20001_roads.zip"), ("STATE", "tl_2025_us_state.zip")):
            data = _zip_bytes("member.shp", f"{product} geometry".encode())
            path = self.root / product / file_name
            path.parent.mkdir(parents=True)
            path.write_bytes(data)
            self.packages.append({"product": product, "file_name": file_name, "byte_length": len(data),
                                  "sha256": hashlib.sha256(data).hexdigest()})
        self.document = {"inventory": {"packages": self.packages}}
        for target, value in (("validate_manifest", lambda _doc: []),
                              ("EXPECTED_TOTAL_BYTES", sum(p["byte_length"] for p in self.packages))):
            patcher = patch.object(reference, target, value)
            patcher.start()
            self.addCleanup(patcher.stop)

    def verify(self, **kwargs: object) -> dict[str, object]:
        return verify_payload_root(self.document, self.root, **kwargs)

    def assert_code(self, code: str, **kwargs: object) -> None:
        with self.assertRaises(ReferenceValidationError) as raised:
            self.verify(**kwargs)
        self.assertEqual(raised.exception.code, code)

    def path(self, index: int) -> Path:
        package = self.packages[index]
        return self.root / package["product"] / package["file_name"]

    def test_exact_bytes_and_crc_verify(self) -> None:
        expected = {"payload_package_count": 2, "payload_total_bytes": reference.EXPECTED_TOTAL_BYTES}
        self.assertEqual(self.verify(), {**expected, "zip_crc_checked": False})
        self.assertEqual(self.verify(check_zip_crc=True), {**expected, "zip_crc_checked": True})

    def test_root_and_file_boundaries(self) -> None:
        link = Path(self.temporary.name) / "link"
        link.symlink_to(self.root)
        with self.assertRaises(ReferenceValidationError) as raised:
            verify_payload_root(self.document, link)
        self.assertEqual(raised.exception.code, "PAYLOAD_ROOT_INVALID")
        self.path(0).unlink()
        self.assert_code("PAYLOAD_FILE_INVALID")
        outside = Path(self.temporary.name) / "outside.zip"
        outside.write_bytes(b"x")
        self.path(0).symlink_to(outside)
        self.assert_code("PAYLOAD_FILE_INVALID")

    def test_size_digest_zip_and_total_mismatches(self) -> None:
        original = self.path(0).read_bytes()
        self.path(0).write_bytes(original + b"!")
        self.assert_code("PAYLOAD_SIZE_MISMATCH")
        self.path(0).write_bytes(original[:-1] + bytes([original[-1] ^ 1]))
        self.assert_code("PAYLOAD_SHA256_MISMATCH")
        corrupt = original.replace(b"ROADS geometry", b"ROADS geometrX")
        self.path(0).write_bytes(corrupt)
        self.packages[0]["sha256"] = hashlib.sha256(corrupt).hexdigest()
        self.assertEqual(self.verify()["payload_package_count"], 2, "bytes match the manifest")
        self.assert_code("PAYLOAD_ZIP_CRC_MISMATCH", check_zip_crc=True)
        not_zip = b"x" * len(original)
        self.path(0).write_bytes(not_zip)
        self.packages[0]["sha256"] = hashlib.sha256(not_zip).hexdigest()
        self.assert_code("PAYLOAD_ZIP_INVALID", check_zip_crc=True)
        with patch.object(reference, "EXPECTED_TOTAL_BYTES", reference.EXPECTED_TOTAL_BYTES + 1):
            self.assert_code("PAYLOAD_TOTAL_BYTES_MISMATCH")

    def test_invalid_manifest_stops_before_reading_payloads(self) -> None:
        with patch.object(reference, "validate_manifest", lambda _doc: ["STATUS_INVALID", "SCOPE_INVALID"]):
            self.assert_code("STATUS_INVALID")


if __name__ == "__main__":
    unittest.main()
