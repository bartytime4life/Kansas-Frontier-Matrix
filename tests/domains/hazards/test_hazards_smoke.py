#!/usr/bin/env python3
"""Deterministic, no-network proof for the Hazards drought-family fixtures.

This replaces the prior always-passing placeholder. It proves only that the
three committed draft schemas are valid JSON Schema 2020-12 documents and that
their reviewed synthetic valid/invalid fixtures have exact polarity. It does
not validate current drought conditions, resolve source or geometry references,
apply policy, authenticate review, or authorize release or publication.
"""

from __future__ import annotations

import json
import socket
import unittest
import urllib.request
from pathlib import Path
from typing import Any
from unittest import mock

from jsonschema import Draft202012Validator, FormatChecker


REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_ROOT = REPO_ROOT / "schemas/contracts/v1/domains/hazards"
FIXTURE_ROOT = REPO_ROOT / "fixtures/domains/hazards"
MAX_FIXTURE_BYTES = 64 * 1024
NETWORK_DENIAL = "network access is forbidden in Hazards drought fixture tests"

EXPECTED_REJECTIONS: dict[str, dict[str, tuple[tuple[str, str], ...]]] = {
    "drought_observation": {
        "invalid_1_observation_carries_legal_stage.json": (("not", "legal_stage"),),
        "invalid_2_unbound_geometry.json": (("type", "geometry_ref"),),
        "invalid_3_unknown_severity_vocabulary.json": (
            ("enum", "source_native_severity"),
        ),
        "invalid_4_declaration_derived.json": (("not", "declaration_derived"),),
        "invalid_5_undeclared_fields.json": (("additionalProperties", "$"),),
        "invalid_6_wrong_object_type.json": (("const", "object_type"),),
        "invalid_7_missing_source_ref.json": (("required", "$"),),
    },
    "drought_declaration": {
        "invalid_1_declaration_derived_from_usdm.json": (("not", "usdm_derived"),),
        "invalid_2_carries_observation_stage.json": (("not", "observation_stage"),),
        "invalid_3_missing_legal_instrument.json": (("const", "declaration_stage"),),
        "invalid_4_mismatched_effective_time.json": (("type", "effective_at"),),
        "invalid_5_silent_supersession.json": (("additionalProperties", "$"),),
        "invalid_6_wrong_object_type.json": (("const", "object_type"),),
        "invalid_7_abstain_but_stage_asserted.json": (
            ("const", "declaration_stage"),
        ),
    },
    "drought_obs_decl_relationship": {
        "invalid_1_derivation_claimed.json": (("const", "derivation_claimed"),),
    },
}


class DuplicateKeyError(ValueError):
    """Raised when a committed fixture or schema repeats an object member."""


def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    value: dict[str, Any] = {}
    for key, item in pairs:
        if key in value:
            raise DuplicateKeyError(key)
        value[key] = item
    return value


def _load_json(path: Path) -> Any:
    if path.is_symlink() or not path.is_file():
        raise AssertionError(f"fixture input is not a regular file: {path}")
    size = path.stat().st_size
    if size <= 0 or size > MAX_FIXTURE_BYTES:
        raise AssertionError(f"fixture input size is outside the bound: {path}")
    return json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=_unique_object,
    )


def _findings(
    validator: Draft202012Validator,
    candidate: Any,
) -> tuple[tuple[str, str], ...]:
    findings = []
    for error in validator.iter_errors(candidate):
        path = ".".join(str(part) for part in error.absolute_path) or "$"
        findings.append((str(error.validator), path))
    return tuple(sorted(findings))


class HazardsDroughtFixtureTests(unittest.TestCase):
    def setUp(self) -> None:
        denial = AssertionError(NETWORK_DENIAL)
        self.network_mocks: list[mock.Mock] = []
        for patcher in (
            mock.patch.object(socket.socket, "connect", side_effect=denial),
            mock.patch.object(socket, "create_connection", side_effect=denial),
            mock.patch.object(socket, "getaddrinfo", side_effect=denial),
            mock.patch.object(urllib.request, "urlopen", side_effect=denial),
        ):
            self.network_mocks.append(patcher.start())
            self.addCleanup(patcher.stop)

    def test_schema_and_fixture_polarity_is_exact(self) -> None:
        for family, expected_invalid in EXPECTED_REJECTIONS.items():
            with self.subTest(family=family):
                schema_path = SCHEMA_ROOT / f"{family}.schema.json"
                schema = _load_json(schema_path)
                Draft202012Validator.check_schema(schema)
                validator = Draft202012Validator(
                    schema,
                    format_checker=FormatChecker(),
                )

                family_root = FIXTURE_ROOT / family
                valid_paths = sorted((family_root / "valid").glob("*.json"))
                invalid_paths = sorted((family_root / "invalid").glob("*.json"))
                self.assertEqual(["valid_1.json"], [path.name for path in valid_paths])
                self.assertEqual(
                    sorted(expected_invalid),
                    [path.name for path in invalid_paths],
                )

                for path in valid_paths:
                    with self.subTest(family=family, fixture=path.name):
                        self.assertEqual((), _findings(validator, _load_json(path)))
                        metadata = _load_json(path)["_fixture_meta"]
                        self.assertEqual(
                            "no_network_required",
                            metadata["network_status"],
                        )
                        self.assertIs(metadata["sensitive_data"], False)

                for path in invalid_paths:
                    with self.subTest(family=family, fixture=path.name):
                        self.assertEqual(
                            expected_invalid[path.name],
                            _findings(validator, _load_json(path)),
                        )

        for network_mock in self.network_mocks:
            network_mock.assert_not_called()

    def test_network_guard_fails_closed(self) -> None:
        with self.assertRaisesRegex(AssertionError, NETWORK_DENIAL):
            socket.create_connection(("example.invalid", 443))
        with self.assertRaisesRegex(AssertionError, NETWORK_DENIAL):
            urllib.request.urlopen("https://example.invalid")


if __name__ == "__main__":
    unittest.main(verbosity=2)
