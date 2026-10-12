"""Deterministic no-network tests for the TIGER/Line Kansas reference manifest."""

from __future__ import annotations

import copy
import json
import socket
import unittest
import urllib.request
from pathlib import Path
from unittest.mock import patch

from tools.validators.source.tiger_line_kansas_core_reference import (
    EXPECTED_KANSAS_COUNTY_GEOIDS,
    EXPECTED_PACKAGE_INDEX_SHA256,
    validate_manifest,
    validation_summary,
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


if __name__ == "__main__":
    unittest.main()
