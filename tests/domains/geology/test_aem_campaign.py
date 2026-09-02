#!/usr/bin/env python3
"""Focused no-network tests for the GMD 3 announcement candidate profile."""

from __future__ import annotations

from contextlib import redirect_stderr, redirect_stdout
import hashlib
from io import StringIO
import json
from pathlib import Path
import socket
import sys
import tempfile
import unittest
from unittest import mock
import urllib.request


REPO_ROOT = Path(__file__).resolve().parents[3]
if str(REPO_ROOT) not in sys.path:
    sys.path.insert(0, str(REPO_ROOT))

from tools.validators.domains.geology.validate_aem_campaign import (  # noqa: E402
    ALLOWED_TOP_LEVEL_FIELDS,
    DEFAULT_SOURCE_DESCRIPTOR_PATH,
    EXPECTED_CAMPAIGN_ID,
    EXPECTED_REFERENCE_CANDIDATES,
    EXPECTED_SOURCE_DESCRIPTOR_REF,
    EXPECTED_SOURCE_DESCRIPTOR_SHA256,
    FORBIDDEN_AMBIGUOUS_FIELDS,
    FORBIDDEN_DOWNSTREAM_STAGE_FIELDS,
    PROFILE_ID,
    Finding,
    main,
    validate_candidate,
    validate_file,
    validate_source_descriptor,
)


FIXTURE_ROOT = REPO_ROOT / "fixtures/domains/geology/aem_survey_campaign"
VALID_FIXTURE_DIR = FIXTURE_ROOT / "valid"
INVALID_FIXTURE_DIR = FIXTURE_ROOT / "invalid"
INVALID_FIXTURE_NAMES = (
    "invalid_acquisition_claim.json",
    "invalid_campaign_state_completed.json",
    "invalid_correction_ref_scheme.json",
    "invalid_downstream_stage_field.json",
    "invalid_false_release_state.json",
    "invalid_missing_supporting_reference.json",
    "invalid_non_fixture_reference.json",
    "invalid_required_limitation_missing.json",
    "invalid_self_supersession.json",
    "invalid_silent_supersession.json",
    "invalid_unscoped_planning_field.json",
)


def _load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def _valid_fixture() -> Path:
    return VALID_FIXTURE_DIR / "valid_1.json"


def _invalid_fixture(name: str) -> Path:
    return INVALID_FIXTURE_DIR / name


def _read_expected(path: Path) -> tuple[Finding, ...]:
    findings = []
    for line in path.read_text(encoding="utf-8").splitlines():
        code, json_path = line.split("\t", maxsplit=1)
        findings.append(Finding(code, json_path))
    return tuple(findings)


class GeologyAemCampaignFixtureTests(unittest.TestCase):
    def setUp(self) -> None:
        denied = RuntimeError(
            "network access is forbidden in Geology AEM candidate tests"
        )
        self.network_mocks: list[mock.Mock] = []
        for patcher in (
            mock.patch.object(socket.socket, "connect", side_effect=denied),
            mock.patch.object(socket.socket, "connect_ex", side_effect=denied),
            mock.patch.object(socket, "create_connection", side_effect=denied),
            mock.patch.object(socket, "getaddrinfo", side_effect=denied),
            mock.patch.object(urllib.request, "urlopen", side_effect=denied),
        ):
            self.addCleanup(patcher.stop)
            self.network_mocks.append(patcher.start())

    def test_profile_and_document_binding_are_exact(self) -> None:
        self.assertEqual(
            PROFILE_ID,
            "kfm-geology-gmd3-aem-campaign-candidate-fixture-v1",
        )
        self.assertEqual(
            DEFAULT_SOURCE_DESCRIPTOR_PATH,
            REPO_ROOT
            / "fixtures/contracts/v1/source/source_descriptor/valid/"
            "valid_ku_news_gmd3_aem_announcement_2026_05_11.json",
        )
        self.assertNotIn(
            "data/registry/geology/sources",
            str(DEFAULT_SOURCE_DESCRIPTOR_PATH),
        )

    def test_valid_candidate_is_historical_sparse_and_nonobservational(self) -> None:
        candidate = _load_json(_valid_fixture())
        self.assertEqual(candidate["id"], EXPECTED_CAMPAIGN_ID)
        self.assertEqual(
            candidate["source_descriptor_ref"],
            EXPECTED_SOURCE_DESCRIPTOR_REF,
        )
        self.assertEqual(candidate["announcement_reported_state"], "planned")
        self.assertEqual(candidate["announcement_published_on"], "2026-05-11")
        self.assertEqual(candidate["current_campaign_state"], "unknown")
        self.assertEqual(
            candidate["acquisition_evidence_state"],
            "not_bound_to_profile",
        )
        self.assertEqual(
            candidate["supporting_reference_candidates"],
            EXPECTED_REFERENCE_CANDIDATES,
        )
        self.assertEqual(set(candidate), ALLOWED_TOP_LEVEL_FIELDS - {"correction"})
        self.assertFalse(FORBIDDEN_AMBIGUOUS_FIELDS.intersection(candidate))
        self.assertFalse(FORBIDDEN_DOWNSTREAM_STAGE_FIELDS.intersection(candidate))
        self.assertEqual(validate_file(_valid_fixture()), [])

    def test_valid_inventory_is_exact(self) -> None:
        self.assertEqual(
            set(VALID_FIXTURE_DIR.glob("*.json")),
            {_valid_fixture()},
        )

    def test_invalid_inventory_and_sidecars_are_exact(self) -> None:
        expected = {_invalid_fixture(name) for name in INVALID_FIXTURE_NAMES}
        self.assertEqual(set(INVALID_FIXTURE_DIR.glob("*.json")), expected)
        self.assertEqual(
            set(INVALID_FIXTURE_DIR.glob("*.expected_error.txt")),
            {path.with_suffix(".expected_error.txt") for path in expected},
        )

    def test_invalid_findings_match_exact_sorted_sidecars(self) -> None:
        for name in INVALID_FIXTURE_NAMES:
            fixture = _invalid_fixture(name)
            expected = _read_expected(
                fixture.with_suffix(".expected_error.txt")
            )
            with self.subTest(fixture=name):
                self.assertTrue(expected)
                self.assertEqual(expected, tuple(sorted(expected)))
                self.assertEqual(tuple(validate_file(fixture)), expected)

    def test_claim_identity_mutations_fail_closed(self) -> None:
        cases = (
            (
                "id",
                "kfm:geology:aem-campaign-candidate:unrelated",
                Finding("AEM_CAMPAIGN_ID_INVALID", "$.id"),
            ),
            (
                "source_descriptor_ref",
                "src:unrelated",
                Finding(
                    "AEM_SOURCE_DESCRIPTOR_REF_INVALID",
                    "$.source_descriptor_ref",
                ),
            ),
            (
                "announcement_published_on",
                "2026-08-03",
                Finding(
                    "AEM_ANNOUNCEMENT_DATE_INVALID",
                    "$.announcement_published_on",
                ),
            ),
        )
        for field, value, expected in cases:
            candidate = _load_json(_valid_fixture())
            candidate[field] = value
            with self.subTest(field=field):
                self.assertEqual(validate_candidate(candidate), [expected])

        candidate = _load_json(_valid_fixture())
        candidate["supporting_reference_candidates"] = [
            "fixture://reference-candidate/geology/gmd3-aem/unrelated"
        ]
        self.assertEqual(
            validate_candidate(candidate),
            [
                Finding(
                    "AEM_REFERENCE_CANDIDATE_IDENTITY_INVALID",
                    "$.supporting_reference_candidates",
                )
            ],
        )

    def test_every_ambiguous_and_downstream_field_is_denied(self) -> None:
        for field in sorted(FORBIDDEN_AMBIGUOUS_FIELDS):
            candidate = _load_json(_valid_fixture())
            candidate[field] = "DO_NOT_ECHO_AMBIGUOUS_SENTINEL"
            with self.subTest(field=field):
                self.assertEqual(
                    validate_candidate(candidate),
                    [
                        Finding(
                            "AEM_AMBIGUOUS_ANNOUNCEMENT_FIELD_DENIED",
                            f"$.{field}",
                        )
                    ],
                )
        for field in sorted(FORBIDDEN_DOWNSTREAM_STAGE_FIELDS):
            candidate = _load_json(_valid_fixture())
            candidate[field] = "DO_NOT_ECHO_STAGE_SENTINEL"
            with self.subTest(field=field):
                self.assertEqual(
                    validate_candidate(candidate),
                    [
                        Finding(
                            "AEM_DOWNSTREAM_STAGE_FIELD_DENIED",
                            f"$.{field}",
                        )
                    ],
                )

    def test_correction_namespace_timestamp_and_self_reference_fail_closed(self) -> None:
        candidate = _load_json(_valid_fixture())
        candidate["correction"] = {
            "supersedes_ref": "src:unrelated",
            "reason": "fixture correction",
        }
        self.assertEqual(
            validate_candidate(candidate),
            [
                Finding(
                    "AEM_CORRECTION_REFERENCE_SCHEME_INVALID",
                    "$.correction.supersedes_ref",
                )
            ],
        )
        candidate["correction"] = {
            "supersedes_ref": candidate["id"],
            "reason": "fixture correction",
        }
        self.assertEqual(
            validate_candidate(candidate),
            [
                Finding(
                    "AEM_SELF_SUPERSESSION_DENIED",
                    "$.correction.supersedes_ref",
                )
            ],
        )
        candidate["correction"] = {
            "supersedes_ref": (
                "kfm:geology:aem-campaign-candidate:prior-example"
            ),
            "reason": "fixture correction",
            "correction_time": "2026-02-30T12:00:00Z",
        }
        self.assertEqual(
            validate_candidate(candidate),
            [
                Finding(
                    "AEM_CORRECTION_TIME_INVALID",
                    "$.correction.correction_time",
                )
            ],
        )

    def test_source_descriptor_is_document_specific_candidate_only(self) -> None:
        descriptor = _load_json(DEFAULT_SOURCE_DESCRIPTOR_PATH)
        self.assertEqual(descriptor["source_id"], EXPECTED_SOURCE_DESCRIPTOR_REF)
        self.assertEqual(descriptor["source_role"], "citation_source")
        self.assertEqual(descriptor["authority_rank"], "candidate_only")
        self.assertEqual(validate_source_descriptor(descriptor), [])
        self.assertEqual(
            hashlib.sha256(DEFAULT_SOURCE_DESCRIPTOR_PATH.read_bytes()).hexdigest(),
            EXPECTED_SOURCE_DESCRIPTOR_SHA256,
        )

    def test_descriptor_authority_regressions_fail_closed(self) -> None:
        cases = (
            (
                lambda value: value.update(source_role="authoritative_for_claim"),
                Finding(
                    "AEM_SOURCE_ROLE_UPCAST_DENIED",
                    "$.profile.source_descriptor.source_role",
                ),
            ),
            (
                lambda value: value.update(authority_rank="primary_authority"),
                Finding(
                    "AEM_SOURCE_AUTHORITY_UPCAST_DENIED",
                    "$.profile.source_descriptor.authority_rank",
                ),
            ),
            (
                lambda value: value["rights"].update(
                    rights_status="verified_open"
                ),
                Finding(
                    "AEM_SOURCE_RIGHTS_UNRESOLVED_POSTURE_INVALID",
                    "$.profile.source_descriptor.rights.rights_status",
                ),
            ),
            (
                lambda value: value["public_release"].update(allowed=True),
                Finding(
                    "AEM_PUBLIC_RELEASE_POSTURE_INVALID",
                    "$.profile.source_descriptor.public_release.allowed",
                ),
            ),
        )
        for mutate, expected in cases:
            descriptor = _load_json(DEFAULT_SOURCE_DESCRIPTOR_PATH)
            mutate(descriptor)
            with self.subTest(expected=expected.code):
                self.assertEqual(validate_source_descriptor(descriptor), [expected])

    def test_descriptor_live_access_and_connector_regressions_fail_closed(self) -> None:
        descriptor = _load_json(DEFAULT_SOURCE_DESCRIPTOR_PATH)
        descriptor["access"]["endpoints"] = [
            {
                "label": "live API",
                "uri": "https://example.invalid/data.parquet",
                "purpose": "other",
            }
        ]
        self.assertIn(
            Finding(
                "AEM_LIVE_DATA_ENDPOINT_DENIED",
                "$.profile.source_descriptor.access.endpoints",
            ),
            validate_source_descriptor(descriptor),
        )

        descriptor = _load_json(DEFAULT_SOURCE_DESCRIPTOR_PATH)
        descriptor["access"]["auth"] = {
            "auth_required": True,
            "auth_type": "api_key",
        }
        self.assertIn(
            Finding(
                "AEM_SOURCE_CREDENTIALLED_ACCESS_DENIED",
                "$.profile.source_descriptor.access",
            ),
            validate_source_descriptor(descriptor),
        )

        descriptor = _load_json(DEFAULT_SOURCE_DESCRIPTOR_PATH)
        descriptor["connectors"]["connector_ref"] = "connectors/geology/live"
        self.assertIn(
            Finding(
                "AEM_CONNECTOR_REFERENCE_DENIED",
                "$.profile.source_descriptor.connectors",
            ),
            validate_source_descriptor(descriptor),
        )

        descriptor = _load_json(DEFAULT_SOURCE_DESCRIPTOR_PATH)
        descriptor["source_head"]["method"] = "http_get"
        self.assertIn(
            Finding(
                "AEM_SOURCE_HEAD_LIVE_FETCH_DENIED",
                "$.profile.source_descriptor.source_head.method",
            ),
            validate_source_descriptor(descriptor),
        )

        descriptor = _load_json(DEFAULT_SOURCE_DESCRIPTOR_PATH)
        descriptor["public_release"]["release_conditions"] = []
        self.assertIn(
            Finding(
                "AEM_PUBLIC_RELEASE_CONDITIONS_MISSING",
                "$.profile.source_descriptor.public_release.release_conditions",
            ),
            validate_source_descriptor(descriptor),
        )

    def test_descriptor_prose_drift_is_hash_denied(self) -> None:
        descriptor = _load_json(DEFAULT_SOURCE_DESCRIPTOR_PATH)
        descriptor["description"] = (
            "DO_NOT_ECHO_PROSE_SENTINEL completed flights and products"
        )
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "descriptor.json"
            path.write_text(json.dumps(descriptor), encoding="utf-8")
            findings = validate_file(
                _valid_fixture(),
                source_descriptor_path=path,
            )
        self.assertIn(
            Finding(
                "AEM_SOURCE_DESCRIPTOR_CONTENT_DRIFT",
                "$.profile.source_descriptor",
            ),
            findings,
        )

    def test_closed_shapes_and_deterministic_finding_order(self) -> None:
        candidate = _load_json(_valid_fixture())
        candidate["zzz"] = True
        candidate["aaa"] = True
        self.assertEqual(
            validate_candidate(candidate),
            [
                Finding("AEM_UNDECLARED_TOP_LEVEL_FIELD", "$.aaa"),
                Finding("AEM_UNDECLARED_TOP_LEVEL_FIELD", "$.zzz"),
            ],
        )

    def test_parser_rejects_duplicate_nonfinite_nonobject_and_oversized_json(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            cases = {
                "duplicate.json": '{"id":"a","id":"b"}',
                "nonfinite.json": '{"value":NaN}',
                "nonobject.json": "[]",
            }
            expected = {
                "duplicate.json": "FIXTURE_JSON_INVALID",
                "nonfinite.json": "FIXTURE_JSON_INVALID",
                "nonobject.json": "CANDIDATE_NOT_OBJECT",
            }
            for name, content in cases.items():
                path = root / name
                path.write_text(content, encoding="utf-8")
                with self.subTest(name=name):
                    self.assertEqual(validate_file(path)[0].code, expected[name])
            oversized = root / "oversized.json"
            oversized.write_text(" " * 1_048_577, encoding="utf-8")
            self.assertEqual(
                validate_file(oversized),
                [Finding("FIXTURE_TOO_LARGE", "$")],
            )

    def test_cli_exit_codes_and_output_are_non_echoing(self) -> None:
        output = StringIO()
        stderr = StringIO()
        with redirect_stdout(output), redirect_stderr(stderr):
            self.assertEqual(main([str(_valid_fixture())]), 0)
            self.assertEqual(
                main([str(_invalid_fixture("invalid_downstream_stage_field.json"))]),
                1,
            )
            self.assertEqual(main([]), 2)
        rendered = output.getvalue()
        self.assertIn('"status":"PASS"', rendered)
        self.assertIn('"status":"FAIL"', rendered)
        self.assertNotIn("DO_NOT_ECHO", rendered)
        self.assertIn("at least one fixture file is required", stderr.getvalue())

    def test_validation_never_attempts_network_access(self) -> None:
        self.assertEqual(validate_file(_valid_fixture()), [])
        for name in INVALID_FIXTURE_NAMES:
            self.assertTrue(validate_file(_invalid_fixture(name)))
        for network_mock in self.network_mocks:
            network_mock.assert_not_called()


if __name__ == "__main__":
    unittest.main()
