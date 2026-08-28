#!/usr/bin/env python3
"""Deterministic tests for the consent-safe genealogy-overlay fixture profile."""

from __future__ import annotations

import contextlib
import copy
import importlib.util
import io
import json
import socket
import sys
import tempfile
import unittest
import urllib.request
from pathlib import Path
from unittest import mock


REPO_ROOT = Path(__file__).resolve().parents[5]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators._common.public_safe_fixture import (  # noqa: E402
    MAX_FIXTURE_BYTES,
    Finding,
    serialize_result,
)

VALIDATOR_PATH = (
    REPO_ROOT
    / "tools/validators/domains/people-dna-land/validate_consent_overlay.py"
)
SPEC = importlib.util.spec_from_file_location(
    "kfm_validate_consent_overlay",
    VALIDATOR_PATH,
)
if SPEC is None or SPEC.loader is None:
    raise RuntimeError(f"unable to load validator: {VALIDATOR_PATH}")
VALIDATOR = importlib.util.module_from_spec(SPEC)
sys.modules[SPEC.name] = VALIDATOR
SPEC.loader.exec_module(VALIDATOR)

FIXTURE_ROOT = REPO_ROOT / "fixtures/domains/people-dna-land/consent_overlay"
VALID_FIXTURE_DIR = FIXTURE_ROOT / "valid"
INVALID_FIXTURE_DIR = FIXTURE_ROOT / "invalid"
MANIFEST_PATH = FIXTURE_ROOT / "revocation_manifest.json"
OVERLAY_SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/domains/people-dna-land/"
    "consented_genealogy_overlay.schema.json"
)
MANIFEST_SCHEMA_PATH = (
    REPO_ROOT
    / "schemas/contracts/v1/domains/people-dna-land/"
    "genealogy_overlay_revocation_manifest.schema.json"
)

VALID_FIXTURE_NAMES = (
    "historical_documentary_context.json",
    "restricted_active_consent.json",
)
INVALID_FIXTURE_NAMES = (
    "expired_consent.json",
    "high_score_weak_evidence.json",
    "identifying_kit_field.json",
    "living_person_without_active_consent.json",
    "missing_evidence.json",
    "non_synthetic_county.json",
    "precise_location.json",
    "public_release_claim.json",
    "raw_genomic_material.json",
    "recent_time_overprecision.json",
    "revocation_root_mismatch.json",
    "revoked_consent.json",
    "spec_hash_mismatch.json",
)


def _valid_fixture(name: str = "restricted_active_consent.json") -> Path:
    return VALID_FIXTURE_DIR / name


def _invalid_fixture(name: str) -> Path:
    return INVALID_FIXTURE_DIR / name


def _sidecar_for(fixture: Path) -> Path:
    return fixture.with_suffix(".expected_error.txt")


def _load_json(path: Path) -> dict[str, object]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise AssertionError(f"expected JSON object: {path}")
    return value


def _load_expected_findings(sidecar: Path) -> tuple[Finding, ...]:
    findings: list[Finding] = []
    for line_number, raw_line in enumerate(
        sidecar.read_text(encoding="utf-8").splitlines(), start=1
    ):
        if not raw_line:
            continue
        code, separator, path = raw_line.partition("\t")
        if not separator or not code or not path:
            raise AssertionError(
                f"malformed expected-error sidecar line {line_number}: {sidecar}"
            )
        findings.append(Finding(code=code, path=path))
    return tuple(findings)


class ConsentOverlayFixtureTests(unittest.TestCase):
    def setUp(self) -> None:
        denied = RuntimeError(
            "network access is forbidden in consent-overlay fixture tests"
        )
        self.network_mocks: list[mock.Mock] = []
        for patcher in (
            mock.patch.object(socket.socket, "connect", side_effect=denied),
            mock.patch.object(socket.socket, "connect_ex", side_effect=denied),
            mock.patch.object(socket, "create_connection", side_effect=denied),
            mock.patch.object(socket, "getaddrinfo", side_effect=denied),
            mock.patch.object(urllib.request, "urlopen", side_effect=denied),
        ):
            self.network_mocks.append(patcher.start())
            self.addCleanup(patcher.stop)

        manifest, findings = VALIDATOR.load_revocation_manifest(MANIFEST_PATH)
        self.assertEqual(findings, [])
        self.assertIsNotNone(manifest)
        self.manifest = manifest

    def test_valid_fixture_inventory_is_explicit_and_positive(self) -> None:
        expected = {_valid_fixture(name) for name in VALID_FIXTURE_NAMES}
        self.assertEqual(set(VALID_FIXTURE_DIR.glob("*.json")), expected)
        for fixture in sorted(expected):
            with self.subTest(fixture=fixture.name):
                self.assertEqual(
                    VALIDATOR.validate_file(
                        fixture,
                        revocation_manifest=self.manifest,
                    ),
                    [],
                )

    def test_valid_cases_cover_dna_and_documentary_material(self) -> None:
        observed: set[tuple[object, object, object]] = set()
        for name in VALID_FIXTURE_NAMES:
            candidate = _load_json(_valid_fixture(name))
            observed.add(
                (
                    candidate["material_kind"],
                    candidate["subject_posture"],
                    candidate["consent"]["status"],  # type: ignore[index]
                )
            )
        self.assertEqual(
            observed,
            {
                (
                    "dna_derived_summary",
                    "living_person",
                    "active",
                ),
                (
                    "documentary_genealogy_context",
                    "deceased_or_historical",
                    "not_required",
                ),
            },
        )

    def test_invalid_fixture_inventory_and_sidecars_are_explicit(self) -> None:
        expected = {_invalid_fixture(name) for name in INVALID_FIXTURE_NAMES}
        self.assertEqual(set(INVALID_FIXTURE_DIR.glob("*.json")), expected)
        self.assertEqual(
            set(INVALID_FIXTURE_DIR.glob("*.expected_error.txt")),
            {_sidecar_for(path) for path in expected},
        )

    def test_invalid_findings_match_exact_sorted_sidecars(self) -> None:
        for name in INVALID_FIXTURE_NAMES:
            fixture = _invalid_fixture(name)
            expected = _load_expected_findings(_sidecar_for(fixture))
            with self.subTest(fixture=name):
                self.assertTrue(expected)
                self.assertEqual(expected, tuple(sorted(expected)))
                self.assertEqual(
                    tuple(
                        VALIDATOR.validate_file(
                            fixture,
                            revocation_manifest=self.manifest,
                        )
                    ),
                    expected,
                )

    def test_schema_profiles_are_closed_and_bound_to_validator(self) -> None:
        overlay_schema = _load_json(OVERLAY_SCHEMA_PATH)
        manifest_schema = _load_json(MANIFEST_SCHEMA_PATH)
        self.assertEqual(
            overlay_schema["$schema"],
            "https://json-schema.org/draft/2020-12/schema",
        )
        self.assertFalse(overlay_schema["additionalProperties"])
        self.assertFalse(manifest_schema["additionalProperties"])
        self.assertEqual(
            overlay_schema["x-kfm"]["validator"],  # type: ignore[index]
            "tools/validators/domains/people-dna-land/"
            "validate_consent_overlay.py",
        )
        self.assertIn("spec_hash", overlay_schema["required"])
        self.assertIn("revocation_root", overlay_schema["required"])
        self.assertIn("revoked_overlay_ids", manifest_schema["required"])

    def test_manifest_hash_and_shape_are_deterministic(self) -> None:
        manifest = _load_json(MANIFEST_PATH)
        self.assertEqual(
            VALIDATOR.validate_revocation_manifest(manifest),
            [],
        )
        expected = VALIDATOR.revocation_manifest_spec_hash(manifest)
        self.assertEqual(manifest["spec_hash"], expected)
        reordered = dict(reversed(list(copy.deepcopy(manifest).items())))
        self.assertEqual(
            VALIDATOR.revocation_manifest_spec_hash(reordered),
            expected,
        )

    def test_manifest_membership_revokes_overlay(self) -> None:
        candidate = _load_json(_valid_fixture())
        manifest = _load_json(MANIFEST_PATH)
        manifest["revoked_overlay_ids"] = [candidate["overlay_id"]]
        manifest["spec_hash"] = VALIDATOR.revocation_manifest_spec_hash(manifest)
        self.assertEqual(
            VALIDATOR.validate_revocation_manifest(manifest),
            [],
        )
        self.assertEqual(
            VALIDATOR.validate_candidate(
                candidate,
                revocation_manifest=manifest,
            ),
            [Finding("REVOCATION_ACTIVE", "$.overlay_id")],
        )

    def test_missing_manifest_fails_closed(self) -> None:
        candidate = _load_json(_valid_fixture())
        self.assertEqual(
            VALIDATOR.validate_candidate(
                candidate,
                revocation_manifest=None,
            ),
            [Finding("REVOCATION_MANIFEST_REQUIRED", "$.revocation_root")],
        )

    def test_overlay_hash_is_order_independent_and_mutation_sensitive(self) -> None:
        candidate = _load_json(_valid_fixture())
        expected = candidate["spec_hash"]
        self.assertEqual(VALIDATOR.overlay_spec_hash(candidate), expected)
        reordered = dict(reversed(list(copy.deepcopy(candidate).items())))
        self.assertEqual(VALIDATOR.overlay_spec_hash(reordered), expected)

        candidate["disclosure_level"] = "internal"
        self.assertNotEqual(VALIDATOR.overlay_spec_hash(candidate), expected)

    def test_active_consent_expires_at_evaluation_boundary(self) -> None:
        candidate = _load_json(_valid_fixture())
        consent = candidate["consent"]
        self.assertIsInstance(consent, dict)
        consent["expires_at"] = candidate["evaluation_time"]
        candidate["spec_hash"] = VALIDATOR.overlay_spec_hash(candidate)
        self.assertEqual(
            VALIDATOR.validate_candidate(
                candidate,
                revocation_manifest=self.manifest,
            ),
            [Finding("CONSENT_EXPIRED", "$.consent.expires_at")],
        )

    def test_every_forbidden_key_family_is_denied_without_values(self) -> None:
        cases = (
            ("vendor_kit_id", "IDENTIFYING_KIT_FIELD_DENIED"),
            ("raw_genotype", "RAW_GENOMIC_MATERIAL_DENIED"),
            ("coordinates", "SENSITIVE_LOCATION_DENIED"),
            ("email", "IDENTIFYING_FIELD_DENIED"),
        )
        for key, code in cases:
            candidate = _load_json(_valid_fixture())
            candidate[key] = "SENSITIVE_SENTINEL"
            candidate["spec_hash"] = VALIDATOR.overlay_spec_hash(candidate)
            findings = VALIDATOR.validate_candidate(
                candidate,
                revocation_manifest=self.manifest,
            )
            with self.subTest(key=key):
                self.assertIn(Finding(code, f"$.{key}"), findings)
                rendered = "\n".join(
                    f"{finding.code}\t{finding.path}" for finding in findings
                )
                self.assertNotIn("SENSITIVE_SENTINEL", rendered)

    def test_parser_rejects_duplicate_nonfinite_and_nonobject_json(self) -> None:
        cases = (
            b'{"fixture_id":"first","fixture_id":"second"}',
            b'{"non_identifying_match_score":NaN}',
            b"[]",
        )
        expected = (
            [Finding("FIXTURE_JSON_INVALID", "$")],
            [Finding("FIXTURE_JSON_INVALID", "$")],
            [Finding("CANDIDATE_NOT_OBJECT", "$")],
        )
        with tempfile.TemporaryDirectory() as directory:
            for index, (content, wanted) in enumerate(zip(cases, expected, strict=True)):
                path = Path(directory) / f"case-{index}.json"
                path.write_bytes(content)
                self.assertEqual(
                    VALIDATOR.validate_file(
                        path,
                        revocation_manifest=self.manifest,
                    ),
                    wanted,
                )

    def test_file_size_is_bounded(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "large.json"
            path.write_bytes(b" " * (MAX_FIXTURE_BYTES + 1))
            self.assertEqual(
                VALIDATOR.validate_file(
                    path,
                    revocation_manifest=self.manifest,
                ),
                [Finding("FIXTURE_TOO_LARGE", "$")],
            )

    def test_cli_exit_codes_and_output_are_non_echoing(self) -> None:
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.assertEqual(
                VALIDATOR.main(
                    [
                        "--revocation-manifest",
                        str(MANIFEST_PATH),
                        str(_valid_fixture()),
                    ]
                ),
                0,
            )
            self.assertEqual(
                VALIDATOR.main(
                    [
                        "--revocation-manifest",
                        str(MANIFEST_PATH),
                        str(_invalid_fixture("raw_genomic_material.json")),
                    ]
                ),
                1,
            )
        output = stdout.getvalue()
        self.assertIn('"status":"PASS"', output)
        self.assertIn('"status":"FAIL"', output)
        self.assertNotIn("SENSITIVE_RAW_GENOMIC_SENTINEL", output)

    def test_serialized_result_is_stable_and_value_free(self) -> None:
        path = _invalid_fixture("identifying_kit_field.json")
        findings = VALIDATOR.validate_file(
            path,
            revocation_manifest=self.manifest,
        )
        first = serialize_result("fixture-profile", path, findings)
        second = serialize_result("fixture-profile", path, list(reversed(findings)))
        self.assertEqual(first, second)
        self.assertNotIn("SENSITIVE_VENDOR_KIT_SENTINEL", first)

    def test_validation_never_attempts_network_access(self) -> None:
        for name in VALID_FIXTURE_NAMES:
            self.assertEqual(
                VALIDATOR.validate_file(
                    _valid_fixture(name),
                    revocation_manifest=self.manifest,
                ),
                [],
            )
        for name in INVALID_FIXTURE_NAMES:
            self.assertTrue(
                VALIDATOR.validate_file(
                    _invalid_fixture(name),
                    revocation_manifest=self.manifest,
                )
            )
        for network_mock in self.network_mocks:
            network_mock.assert_not_called()


if __name__ == "__main__":
    unittest.main(verbosity=2)
