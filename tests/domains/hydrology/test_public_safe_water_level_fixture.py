#!/usr/bin/env python3
"""Deterministic tests for the synthetic Hydrology water-level profile."""

from __future__ import annotations

import copy
import json
import socket
import unittest
import urllib.request
from pathlib import Path
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in __import__("sys").path:
    __import__("sys").path.insert(0, str(REPO_ROOT))

from tools.validators.domains.hydrology.validate_public_safe_water_level_fixture import (  # noqa: E402
    FORBIDDEN_LOCATION_ALIASES,
    Finding,
    MAX_EVIDENCE_REFS,
    validate_candidate,
    validate_file,
)


FIXTURE_ROOT = REPO_ROOT / "fixtures/domains/hydrology/public_safe_water_level"
VALID_FIXTURE = FIXTURE_ROOT / "valid/public_safe_water_level.json"
INVALID_FIXTURE = (
    FIXTURE_ROOT / "invalid/datum_role_location_governance_collapse.json"
)
EXPECTED_ERROR = INVALID_FIXTURE.with_suffix(".expected_error.txt")


def _load_candidate() -> dict[str, object]:
    return json.loads(VALID_FIXTURE.read_text(encoding="utf-8"))


def _load_expected() -> list[Finding]:
    findings: list[Finding] = []
    for line in EXPECTED_ERROR.read_text(encoding="utf-8").splitlines():
        code, separator, path = line.partition("\t")
        if not separator:
            raise AssertionError(f"malformed expected-error sidecar: {line!r}")
        findings.append(Finding(code, path))
    return findings


class HydrologyWaterLevelFixtureTests(unittest.TestCase):
    def setUp(self) -> None:
        denied = RuntimeError("network access is forbidden in Hydrology tests")
        for patcher in (
            mock.patch.object(socket.socket, "connect", side_effect=denied),
            mock.patch.object(socket, "create_connection", side_effect=denied),
            mock.patch.object(socket, "getaddrinfo", side_effect=denied),
            mock.patch.object(urllib.request, "urlopen", side_effect=denied),
        ):
            patcher.start()
            self.addCleanup(patcher.stop)

    def test_fixture_inventory_is_explicit_and_polarized(self) -> None:
        self.assertEqual(list((FIXTURE_ROOT / "valid").glob("*.json")), [VALID_FIXTURE])
        self.assertEqual(
            list((FIXTURE_ROOT / "invalid").glob("*.json")), [INVALID_FIXTURE]
        )
        self.assertEqual(validate_file(VALID_FIXTURE), [])
        expected = _load_expected()
        self.assertEqual(expected, sorted(expected))
        self.assertEqual(validate_file(INVALID_FIXTURE), expected)

    def test_datum_reference_is_required_and_fixture_bound(self) -> None:
        candidate = _load_candidate()
        self.assertEqual(
            candidate["measurement"]["datum_ref"],  # type: ignore[index]
            "fixture://hydrology/datum/synthetic-local-reference",
        )
        self.assertEqual(validate_candidate(candidate), [])

        missing = Finding("DATUM_REF_MISSING", "$.measurement.datum_ref")
        for value in ("", "   ", None, 0, False):
            mutated = copy.deepcopy(candidate)
            mutated["measurement"]["datum_ref"] = value  # type: ignore[index]
            self.assertIn(missing, validate_candidate(mutated))
        mutated = copy.deepcopy(candidate)
        mutated["measurement"].pop("datum_ref")  # type: ignore[index]
        self.assertIn(missing, validate_candidate(mutated))

        unsupported = Finding("DATUM_REF_NOT_FIXTURE", "$.measurement.datum_ref")
        for value in (
            "https://example.invalid/live-datum",
            "fixture://hydrology/gauge/generalized/99999",
            "NAVD88",
        ):
            mutated = copy.deepcopy(candidate)
            mutated["measurement"]["datum_ref"] = value  # type: ignore[index]
            self.assertIn(unsupported, validate_candidate(mutated))

        invalid_identifier = Finding(
            "DATUM_REF_IDENTIFIER_INVALID", "$.measurement.datum_ref"
        )
        for value in (
            "fixture://hydrology/datum/",
            "fixture://hydrology/datum/   ",
            "fixture://hydrology/datum/NAVD88",
            "fixture://hydrology/datum/synthetic/local-reference",
            "fixture://hydrology/datum/-synthetic-reference",
            "fixture://hydrology/datum/synthetic-reference-",
            "fixture://hydrology/datum/synthetic--reference",
            "fixture://hydrology/datum/" + ("a" * 129),
        ):
            mutated = copy.deepcopy(candidate)
            mutated["measurement"]["datum_ref"] = value  # type: ignore[index]
            self.assertIn(invalid_identifier, validate_candidate(mutated))

    def test_record_identity_binds_gauge_datum_and_observation_time(self) -> None:
        candidate = _load_candidate()
        self.assertEqual(
            candidate["record_id"],
            "fixture:hydrology:water-level:99999:synthetic-local-reference:"
            "20260802T120000Z",
        )
        self.assertEqual(validate_candidate(candidate), [])

        invalid = Finding("RECORD_ID_NOT_CANONICAL", "$.record_id")
        for value in (
            "fixture:hydrology:water-level:88888:synthetic-local-reference:"
            "20260802T120000Z",
            "fixture:hydrology:water-level:99999:synthetic-local-reference:"
            "20260802T120001Z",
            "fixture:hydrology:water-level:99999:alternate-local-reference:"
            "20260802T120000Z",
            "https://example.invalid/water-level/99999",
        ):
            mutated = copy.deepcopy(candidate)
            mutated["record_id"] = value
            self.assertIn(invalid, validate_candidate(mutated))

        changed_datum = copy.deepcopy(candidate)
        changed_datum["measurement"]["datum_ref"] = (  # type: ignore[index]
            "fixture://hydrology/datum/alternate-local-reference"
        )
        self.assertIn(invalid, validate_candidate(changed_datum))
        changed_datum["record_id"] = (
            "fixture:hydrology:water-level:99999:alternate-local-reference:"
            "20260802T120000Z"
        )
        self.assertIn(
            Finding("EVIDENCE_REF_DATUM_MISMATCH", "$.evidence_refs"),
            validate_candidate(changed_datum),
        )
        changed_datum["evidence_refs"] = [
            "fixture://evidence/hydrology/water-level/99999/"
            "20260802T120000Z/alternate-local-reference/"
            "synthetic-water-level-gauge"
        ]
        self.assertEqual(validate_candidate(changed_datum), [])

    def test_fixture_references_identify_concrete_synthetic_resources(self) -> None:
        candidate = _load_candidate()
        self.assertEqual(validate_candidate(candidate), [])

        source_invalid = Finding(
            "SOURCE_DESCRIPTOR_REF_IDENTIFIER_INVALID", "$.source_descriptor_ref"
        )
        for value in (
            "fixture://sources/hydrology/",
            "fixture://sources/hydrology/   ",
            "fixture://sources/hydrology/Synthetic-Gauge",
            "fixture://sources/hydrology/synthetic/gauge",
            "fixture://sources/hydrology/-synthetic-gauge",
            "fixture://sources/hydrology/" + ("a" * 129),
        ):
            mutated = copy.deepcopy(candidate)
            mutated["source_descriptor_ref"] = value
            self.assertIn(source_invalid, validate_candidate(mutated))

        gauge_invalid = Finding(
            "GAUGE_SITE_REF_IDENTIFIER_INVALID", "$.gauge_site_ref"
        )
        for value in (
            "fixture://hydrology/gauge/generalized/",
            "fixture://hydrology/gauge/generalized/   ",
            "fixture://hydrology/gauge/generalized/GAUGE-99999",
            "fixture://hydrology/gauge/generalized/99999/site",
            "fixture://hydrology/gauge/generalized/-99999",
            "fixture://hydrology/gauge/generalized/" + ("9" * 129),
        ):
            mutated = copy.deepcopy(candidate)
            mutated["gauge_site_ref"] = value
            self.assertIn(gauge_invalid, validate_candidate(mutated))

        evidence_invalid = Finding(
            "EVIDENCE_REF_IDENTIFIER_INVALID", "$.evidence_refs"
        )
        for value in (
            "fixture://evidence/hydrology/",
            "fixture://evidence/hydrology/   ",
            "fixture://evidence/hydrology/Water-Level/99999/receipt-1",
            "fixture://evidence/hydrology/water-level/99999/Receipt-1",
            "fixture://evidence/hydrology/water-level/20260802t120000z/receipt-1",
            "fixture://evidence/hydrology/water-level/20260802t120000Z/receipt-1",
            "fixture://evidence/hydrology/water-level/20260802T120000z/receipt-1",
            "fixture://evidence/hydrology/water-level/٢٠٢٦٠٨٠٢T١٢٠٠٠٠Z/receipt-1",
            "fixture://evidence/hydrology/water-level/２０２６０８０２T１２００００Z/receipt-1",
            "fixture://evidence/hydrology/water-level/20261302T120000Z/receipt-1",
            "fixture://evidence/hydrology/water-level/20260230T120000Z/receipt-1",
            "fixture://evidence/hydrology/water-level/20260802T240000Z/receipt-1",
            "fixture://evidence/hydrology/water-level/20260802T126000Z/receipt-1",
            "fixture://evidence/hydrology/water-level/20260802T120060Z/receipt-1",
            "fixture://evidence/hydrology/water-level//receipt",
            "fixture://evidence/hydrology/water-level/../receipt",
            "fixture://evidence/hydrology/-water-level/receipt",
            "fixture://evidence/hydrology/" + ("a" * 257),
        ):
            mutated = copy.deepcopy(candidate)
            mutated["evidence_refs"] = [value]
            self.assertIn(evidence_invalid, validate_candidate(mutated))

    def test_evidence_references_are_unique(self) -> None:
        candidate = _load_candidate()
        evidence_ref = candidate["evidence_refs"][0]  # type: ignore[index]

        candidate["evidence_refs"] = [  # type: ignore[index]
            evidence_ref,
            "fixture://evidence/hydrology/water-level/99999/"
            "20260802T120000Z/synthetic-local-reference/"
            "synthetic-water-level-gauge/receipt-2",
        ]
        self.assertEqual(validate_candidate(candidate), [])

        candidate["evidence_refs"] = [evidence_ref, evidence_ref]  # type: ignore[index]
        self.assertIn(
            Finding("EVIDENCE_REFS_DUPLICATE", "$.evidence_refs"),
            validate_candidate(candidate),
        )

    def test_evidence_references_bind_family_and_gauge_identity(self) -> None:
        candidate = _load_candidate()
        self.assertEqual(validate_candidate(candidate), [])

        mismatch = Finding("EVIDENCE_REF_IDENTITY_MISMATCH", "$.evidence_refs")
        for value in (
            "fixture://evidence/hydrology/flow/99999/20260802T120000Z/"
            "synthetic-local-reference/synthetic-water-level-gauge",
            "fixture://evidence/hydrology/water-level/88888/20260802T120000Z/"
            "synthetic-local-reference/synthetic-water-level-gauge",
        ):
            mutated = copy.deepcopy(candidate)
            mutated["evidence_refs"] = [value]
            self.assertIn(mismatch, validate_candidate(mutated))

    def test_evidence_references_bind_observation_time(self) -> None:
        candidate = _load_candidate()
        self.assertEqual(validate_candidate(candidate), [])

        mismatch = Finding("EVIDENCE_REF_TIME_MISMATCH", "$.evidence_refs")
        for value in (
            "fixture://evidence/hydrology/water-level/99999/20260802T120001Z/"
            "synthetic-local-reference/synthetic-water-level-gauge",
            "fixture://evidence/hydrology/water-level/99999/receipt-1/"
            "synthetic-local-reference/synthetic-water-level-gauge",
        ):
            mutated = copy.deepcopy(candidate)
            mutated["evidence_refs"] = [value]
            self.assertIn(mismatch, validate_candidate(mutated))

    def test_evidence_references_bind_datum_identity(self) -> None:
        candidate = _load_candidate()
        self.assertEqual(validate_candidate(candidate), [])

        mismatch = Finding("EVIDENCE_REF_DATUM_MISMATCH", "$.evidence_refs")
        for value in (
            "fixture://evidence/hydrology/water-level/99999/20260802T120000Z",
            "fixture://evidence/hydrology/water-level/99999/20260802T120000Z/"
            "alternate-local-reference/synthetic-water-level-gauge",
        ):
            mutated = copy.deepcopy(candidate)
            mutated["evidence_refs"] = [value]
            self.assertIn(mismatch, validate_candidate(mutated))

    def test_evidence_references_bind_source_identity(self) -> None:
        candidate = _load_candidate()
        self.assertEqual(validate_candidate(candidate), [])

        mismatch = Finding("EVIDENCE_REF_SOURCE_MISMATCH", "$.evidence_refs")
        for value in (
            "fixture://evidence/hydrology/water-level/99999/20260802T120000Z/"
            "synthetic-local-reference",
            "fixture://evidence/hydrology/water-level/99999/20260802T120000Z/"
            "synthetic-local-reference/alternate-water-level-gauge",
        ):
            mutated = copy.deepcopy(candidate)
            mutated["evidence_refs"] = [value]
            self.assertIn(mismatch, validate_candidate(mutated))

        changed_source = copy.deepcopy(candidate)
        changed_source["source_descriptor_ref"] = (
            "fixture://sources/hydrology/alternate-water-level-gauge"
        )
        self.assertIn(mismatch, validate_candidate(changed_source))
        changed_source["evidence_refs"] = [
            "fixture://evidence/hydrology/water-level/99999/20260802T120000Z/"
            "synthetic-local-reference/alternate-water-level-gauge"
        ]
        self.assertEqual(validate_candidate(changed_source), [])

    def test_evidence_references_use_canonical_order(self) -> None:
        candidate = _load_candidate()
        first = (
            "fixture://evidence/hydrology/water-level/99999/"
            "20260802T120000Z/synthetic-local-reference/"
            "synthetic-water-level-gauge/receipt-1"
        )
        second = (
            "fixture://evidence/hydrology/water-level/99999/"
            "20260802T120000Z/synthetic-local-reference/"
            "synthetic-water-level-gauge/receipt-2"
        )

        candidate["evidence_refs"] = [first, second]
        self.assertEqual(validate_candidate(candidate), [])

        candidate["evidence_refs"] = [second, first]
        self.assertIn(
            Finding("EVIDENCE_REFS_NOT_CANONICAL_ORDER", "$.evidence_refs"),
            validate_candidate(candidate),
        )

    def test_evidence_reference_count_is_bounded(self) -> None:
        candidate = _load_candidate()
        candidate["evidence_refs"] = [  # type: ignore[index]
            "fixture://evidence/hydrology/water-level/99999/"
            "20260802T120000Z/synthetic-local-reference/"
            f"synthetic-water-level-gauge/receipt-{index:02d}"
            for index in range(MAX_EVIDENCE_REFS)
        ]
        self.assertEqual(validate_candidate(candidate), [])

        candidate["evidence_refs"].append(  # type: ignore[union-attr]
            "fixture://evidence/hydrology/water-level/99999/"
            "20260802T120000Z/synthetic-local-reference/"
            "synthetic-water-level-gauge/receipt-overflow"
        )
        self.assertIn(
            Finding("EVIDENCE_REFS_TOO_MANY", "$.evidence_refs"),
            validate_candidate(candidate),
        )

    def test_observation_family_role_parameter_and_unit_are_closed(self) -> None:
        cases = (
            ("object_family", "FlowObservation", Finding("OBJECT_FAMILY_INVALID", "$.object_family")),
            ("source_role", "modeled", Finding("SOURCE_ROLE_INVALID", "$.source_role")),
        )
        for field, value, expected in cases:
            candidate = _load_candidate()
            candidate[field] = value
            self.assertIn(expected, validate_candidate(candidate))

        for field, value, expected in (
            ("parameter_code", "00060", Finding("PARAMETER_CODE_INVALID", "$.measurement.parameter_code")),
            ("unit", "ft3/s", Finding("MEASUREMENT_UNIT_INVALID", "$.measurement.unit")),
        ):
            candidate = _load_candidate()
            candidate["measurement"][field] = value  # type: ignore[index]
            self.assertIn(expected, validate_candidate(candidate))

    def test_measurement_bounds_keep_booleans_separate(self) -> None:
        for value in (-10_000, 10_000):
            candidate = _load_candidate()
            candidate["measurement"]["value"] = value  # type: ignore[index]
            self.assertEqual(validate_candidate(candidate), [])
        expected = Finding("MEASUREMENT_VALUE_OUT_OF_RANGE", "$.measurement.value")
        for value in (-10_001, 10_001, True, False, float("nan"), float("inf")):
            candidate = _load_candidate()
            candidate["measurement"]["value"] = value  # type: ignore[index]
            self.assertIn(expected, validate_candidate(candidate))

    def test_temporal_provenance_is_canonical_and_monotonic(self) -> None:
        candidate = _load_candidate()
        candidate["temporal_scope"]["source_time"] = "2026-08-02T11:59:59Z"  # type: ignore[index]
        self.assertIn(
            Finding("SOURCE_TIME_BEFORE_OBSERVED", "$.temporal_scope"),
            validate_candidate(candidate),
        )

        candidate = _load_candidate()
        candidate["temporal_scope"]["retrieved_at"] = "2026-08-02T12:00:30Z"  # type: ignore[index]
        self.assertIn(
            Finding("RETRIEVAL_TIME_BEFORE_SOURCE", "$.temporal_scope"),
            validate_candidate(candidate),
        )

        candidate = _load_candidate()
        candidate["temporal_scope"]["observed_at"] = "2026-08-02T12:00:00+00:00"  # type: ignore[index]
        self.assertIn(
            Finding("OBSERVED_TIME_INVALID", "$.temporal_scope.observed_at"),
            validate_candidate(candidate),
        )

    def test_precise_location_aliases_are_forbidden(self) -> None:
        for alias in sorted(FORBIDDEN_LOCATION_ALIASES):
            candidate = _load_candidate()
            candidate["spatial_support"][alias] = "synthetic-forbidden"  # type: ignore[index]
            self.assertIn(
                Finding(
                    "PRECISE_LOCATION_FIELD_FORBIDDEN",
                    f"$.spatial_support.{alias}",
                ),
                validate_candidate(candidate),
            )

    def test_shapes_are_closed_and_findings_are_deterministic(self) -> None:
        candidate = _load_candidate()
        candidate["unexpected"] = "value"
        candidate["measurement"]["unexpected"] = "value"  # type: ignore[index]
        first = validate_candidate(candidate)
        second = validate_candidate(copy.deepcopy(candidate))
        self.assertEqual(first, second)
        self.assertEqual(first, sorted(first))
        self.assertIn(Finding("UNDECLARED_TOP_LEVEL_FIELD", "$.unexpected"), first)
        self.assertIn(
            Finding("UNDECLARED_MEASUREMENT_FIELD", "$.measurement.unexpected"),
            first,
        )

    def test_no_data_must_be_boolean_false(self) -> None:
        expected = Finding("NO_DATA_STATE_INVALID", "$.measurement.no_data")
        for value in (0, "false", None, True):
            candidate = _load_candidate()
            candidate["measurement"]["no_data"] = value  # type: ignore[index]
            self.assertIn(expected, validate_candidate(candidate))


if __name__ == "__main__":
    unittest.main()
