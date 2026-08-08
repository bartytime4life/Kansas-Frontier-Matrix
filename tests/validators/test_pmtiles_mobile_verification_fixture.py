from __future__ import annotations

import json
import socket
import tempfile
import unittest
from pathlib import Path
from unittest import mock

from tools.validators.pmtiles.validate_mobile_verification_fixture import (
    FIXTURE_PATH,
    MAX_FIXTURE_BYTES,
    apply_mutation,
    main,
    validate_bundle,
    validate_file,
    validate_fixture_suite,
)


class PMTilesMobileVerificationFixtureTests(unittest.TestCase):
    def setUp(self) -> None:
        self.fixture = json.loads(FIXTURE_PATH.read_text(encoding="utf-8"))

    def test_declared_fixture_polarity_is_exact(self) -> None:
        results = validate_fixture_suite(self.fixture)
        self.assertEqual(len(results), 8)
        self.assertTrue(all(result["matches_expected"] for result in results))
        self.assertEqual(
            [result["case_id"] for result in results],
            [case["case_id"] for case in self.fixture["cases"]],
        )

    def test_valid_bundle_is_deterministic_and_retains_holds(self) -> None:
        base = self.fixture["base"]
        first = validate_bundle(apply_mutation(base, "NONE"))
        second = validate_bundle(apply_mutation(base, "NONE"))
        self.assertEqual(first, [])
        self.assertEqual(first, second)
        self.assertEqual(
            set(base["holds"]),
            {
                "CRYPTOGRAPHIC_VERIFICATION_UNWIRED",
                "MAPLIBRE_RUNTIME_UNADMITTED",
                "RELEASE_AUTHORIZATION_NOT_EVALUATED",
            },
        )
        self.assertEqual(base["maplibre_boot_state"], "HOLD")
        self.assertTrue(all(value is False for value in base["authority"].values()))

    def test_cli_fixture_mode_and_argument_contract(self) -> None:
        self.assertEqual(main(["--fixtures"]), 0)
        self.assertEqual(main([str(FIXTURE_PATH)]), 0)
        self.assertEqual(main([]), 2)
        self.assertEqual(main(["--fixtures", str(FIXTURE_PATH)]), 2)

    def test_validation_is_no_network(self) -> None:
        def deny(*_args: object, **_kwargs: object) -> None:
            raise AssertionError("network access is forbidden")

        with (
            mock.patch.object(socket, "socket", side_effect=deny),
            mock.patch.object(socket, "create_connection", side_effect=deny),
            mock.patch.object(socket, "getaddrinfo", side_effect=deny),
        ):
            results, findings = validate_file(FIXTURE_PATH)
        self.assertEqual(findings, [])
        self.assertTrue(all(result["matches_expected"] for result in results))

    def test_parser_rejects_duplicate_keys_and_oversize_input(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            duplicate = Path(temp_dir) / "duplicate.json"
            duplicate.write_text('{"profile":"a","profile":"b"}', encoding="utf-8")
            _results, findings = validate_file(duplicate)
            self.assertEqual(
                [finding.code for finding in findings],
                ["MOBILE_PMTILES_FIXTURE_DUPLICATE_KEY"],
            )

            oversized = Path(temp_dir) / "oversized.json"
            oversized.write_bytes(b" " * (MAX_FIXTURE_BYTES + 1))
            _results, findings = validate_file(oversized)
            self.assertEqual(
                [finding.code for finding in findings],
                ["MOBILE_PMTILES_FIXTURE_TOO_LARGE"],
            )


if __name__ == "__main__":
    unittest.main()
