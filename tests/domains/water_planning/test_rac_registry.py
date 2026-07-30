"""No-network regression tests for the canonical RAC registry slice."""

from __future__ import annotations

import copy
import hashlib
import json
import socket
import unittest
import urllib.request
from collections import Counter
from pathlib import Path
from unittest.mock import patch

from tools.validators.domains.water_planning.validate_rac_registry import (
    CROSSWALK_RECORD_PATH,
    CENSUS_SOURCE_RECORD_PATH,
    DATASET_RECORD_PATH,
    EXPECTED_COUNTY_GEOIDS,
    EXPECTED_MAPPING_COUNT,
    EXPECTED_OVERLAP_CLASS_COUNTS,
    EXPECTED_REGION_IDS,
    GEOMETRY_PATH,
    KWO_SOURCE_RECORD_PATH,
    canonical_json_bytes,
    validate_documents,
    validate_repository,
)


REPO_ROOT = Path(__file__).resolve().parents[3]


def _unexpected_network(*_args, **_kwargs):
    raise AssertionError("RAC registry validation attempted network access")


def _load():
    dataset = json.loads((REPO_ROOT / DATASET_RECORD_PATH).read_text("utf-8"))
    crosswalk = json.loads((REPO_ROOT / CROSSWALK_RECORD_PATH).read_text("utf-8"))
    geometry_path = REPO_ROOT / GEOMETRY_PATH
    geometry_bytes = geometry_path.read_bytes()
    geometry = json.loads(geometry_bytes)
    kwo_source = json.loads(
        (REPO_ROOT / KWO_SOURCE_RECORD_PATH).read_text("utf-8")
    )
    census_source = json.loads(
        (REPO_ROOT / CENSUS_SOURCE_RECORD_PATH).read_text("utf-8")
    )
    return (
        dataset,
        crosswalk,
        geometry,
        geometry_bytes,
        kwo_source,
        census_source,
    )


def _pairs(findings):
    return {(finding.code, finding.path) for finding in findings}


def _validate(loaded):
    return validate_documents(*loaded)


def _redigest_mappings(crosswalk):
    crosswalk["mapping_digest"] = "sha256:" + hashlib.sha256(
        canonical_json_bytes(crosswalk["mappings"])
    ).hexdigest()


class RacRegistryTests(unittest.TestCase):
    def setUp(self):
        patchers = (
            patch.object(socket.socket, "connect", _unexpected_network),
            patch.object(socket, "create_connection", _unexpected_network),
            patch.object(urllib.request, "urlopen", _unexpected_network),
        )
        for patcher in patchers:
            patcher.start()
            self.addCleanup(patcher.stop)

    def test_canonical_registry_passes_non_vacuously(self):
        loaded = _load()
        dataset, crosswalk, geometry, _, kwo_source, census_source = loaded
        self.assertEqual(_validate(loaded), ())
        self.assertEqual(validate_repository(REPO_ROOT), ())
        self.assertEqual(
            tuple(feature["properties"]["region_id"] for feature in geometry["features"]),
            EXPECTED_REGION_IDS,
        )
        self.assertEqual(len(geometry["features"]), 14)
        self.assertEqual(crosswalk["mapping_count"], EXPECTED_MAPPING_COUNT)
        self.assertEqual(
            tuple(sorted({row["county_geoid"] for row in crosswalk["mappings"]})),
            EXPECTED_COUNTY_GEOIDS,
        )
        self.assertEqual(
            dict(Counter(row["overlap_class"] for row in crosswalk["mappings"])),
            EXPECTED_OVERLAP_CLASS_COUNTS,
        )
        self.assertEqual(dataset["release_status"], "not-released")
        self.assertEqual(crosswalk["release_status"], "not-released")
        self.assertEqual(kwo_source["connectors"]["activation_state"], "disabled")
        self.assertEqual(
            census_source["connectors"]["activation_state"], "disabled"
        )

    def test_geometry_digest_is_locked(self):
        loaded = list(_load())
        dataset = loaded[0]
        dataset["payload"]["sha256"] = "sha256:" + ("0" * 64)
        findings = _pairs(_validate(loaded))
        self.assertIn(
            ("GEOMETRY_DIGEST_MISMATCH", "$.dataset.payload.sha256"), findings
        )
        self.assertIn(
            ("GEOMETRY_BASELINE_DIGEST_INVALID", "$.dataset.payload.sha256"),
            findings,
        )

    def test_mapping_order_and_digest_are_locked(self):
        loaded = list(_load())
        crosswalk = loaded[1]
        crosswalk["mappings"][0], crosswalk["mappings"][1] = (
            crosswalk["mappings"][1],
            crosswalk["mappings"][0],
        )
        _redigest_mappings(crosswalk)
        findings = _pairs(_validate(loaded))
        self.assertIn(("MAPPING_ORDER_INVALID", "$.crosswalk.mappings"), findings)
        self.assertIn(
            ("CROSSWALK_METADATA_INVALID", "$.crosswalk.mapping_digest"),
            findings,
        )

    def test_overlap_class_cannot_overstate_a_sliver(self):
        loaded = list(_load())
        crosswalk = loaded[1]
        sliver = next(
            row
            for row in crosswalk["mappings"]
            if row["overlap_class"] == "boundary-sliver"
        )
        index = crosswalk["mappings"].index(sliver)
        crosswalk["mappings"][index]["overlap_class"] = "dominant"
        _redigest_mappings(crosswalk)
        findings = _pairs(_validate(loaded))
        self.assertIn(
            (
                "OVERLAP_CLASS_MISMATCH",
                f"$.crosswalk.mappings[{index}].overlap_class",
            ),
            findings,
        )
        self.assertIn(
            ("OVERLAP_CLASS_COUNTS_INVALID", "$.crosswalk.mappings"), findings
        )

    def test_geometry_identity_cannot_be_renamed(self):
        loaded = list(_load())
        dataset, geometry = loaded[0], loaded[2]
        geometry["features"][0]["properties"]["name"] = "Invented Region"
        geometry_bytes = canonical_json_bytes(geometry, trailing_newline=True)
        dataset["payload"]["sha256"] = (
            "sha256:" + hashlib.sha256(geometry_bytes).hexdigest()
        )
        dataset["payload"]["byte_count"] = len(geometry_bytes)
        loaded[3] = geometry_bytes
        findings = _pairs(_validate(loaded))
        self.assertIn(
            (
                "FEATURE_NAME_INVALID",
                "$.geometry.features[0].properties.name",
            ),
            findings,
        )
        self.assertIn(
            ("GEOMETRY_BASELINE_DIGEST_INVALID", "$.dataset.payload.sha256"),
            findings,
        )

    def test_registry_record_cannot_claim_release(self):
        loaded = list(_load())
        dataset, crosswalk = loaded[0], loaded[1]
        dataset["release_status"] = "released"
        crosswalk["release_status"] = "released"
        findings = _pairs(_validate(loaded))
        self.assertIn(
            ("RELEASE_STATUS_INVALID", "$.dataset.release_status"), findings
        )
        self.assertIn(
            ("CROSSWALK_METADATA_INVALID", "$.crosswalk.release_status"),
            findings,
        )

    def test_duplicate_mapping_key_is_rejected(self):
        loaded = list(_load())
        crosswalk = loaded[1]
        crosswalk["mappings"][1] = copy.deepcopy(crosswalk["mappings"][0])
        _redigest_mappings(crosswalk)
        findings = _pairs(_validate(loaded))
        self.assertIn(("MAPPING_KEY_DUPLICATE", "$.crosswalk.mappings"), findings)

    def test_source_descriptors_remain_unreleased_and_disabled(self):
        loaded = list(_load())
        kwo_source = loaded[4]
        kwo_source["connectors"]["activation_state"] = "live_active"
        kwo_source["public_release"]["allowed"] = True
        findings = _pairs(_validate(loaded))
        self.assertIn(
            (
                "SOURCE_CONNECTOR_MUST_BE_DISABLED",
                "$.sources.kwo.connectors.activation_state",
            ),
            findings,
        )
        self.assertIn(
            (
                "SOURCE_PUBLIC_RELEASE_MUST_BE_FALSE",
                "$.sources.kwo.public_release.allowed",
            ),
            findings,
        )


if __name__ == "__main__":
    unittest.main()
