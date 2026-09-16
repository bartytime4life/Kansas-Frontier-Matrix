"""Review-only Atlas profile proof; no operational verification is issued."""

from copy import deepcopy
import json
import socket
import subprocess
import unittest
from unittest import mock

from evidence_resolver.atlas_fixture_lookup import CANDIDATE_ID, lookup_atlas_fixture
from evidence_resolver.core import evaluate_resolution_candidate, loads_bounded
from evidence_resolver.runtime_projection import project_runtime_posture
from evidence_resolver.verification_history import (
    ATLAS_FIXTURE_PROFILE,
    ATLAS_FIXTURE_SUBJECT,
    LEGACY_PROFILE,
    canonical_spec_hash,
    replay_state,
    validate_history,
)
from tools.validators.validate_verification_state_history import (
    FIXTURES_ROOT,
    REPO_ROOT,
    validate_document,
)


class AtlasVerificationProfileTests(unittest.TestCase):
    def setUp(self):
        self.history = json.loads(
            (FIXTURES_ROOT / "valid/valid_atlas_fixture_profile.json").read_bytes()
        )
        self.request = json.loads(
            (REPO_ROOT / "fixtures/packages/evidence_resolver/v1alpha1/valid/resolved.json")
            .read_bytes()
        )["request"]
        self.lookup = lookup_atlas_fixture(CANDIDATE_ID)
        packet = self.lookup.packet
        self.assertIsNotNone(packet)
        self.request["bundle_candidate"] = loads_bounded(packet.bundle_bytes)
        self.request["evidence_ref"] = {
            "ref": packet.subject_ref, "kind": "artifact", "bundle_ref": packet.evidence_ref
        }
        self.request["lookup_context"]["bundle_id"] = packet.evidence_ref
        self.request["verification_history"] = self.history
        self.query("2026-04-13T00:05:00Z", "2026-04-13T00:05:00Z")

    def query(self, effective, recorded):
        self.request["verification_as_of"] = {
            "effective_as_of": effective, "recorded_as_of": recorded
        }

    def assert_parity(self, history, valid):
        schema_codes = {x.code for x in validate_document(history)}
        parser_codes = {x.code for x in validate_history(history)}
        self.assertEqual(schema_codes, parser_codes)
        self.assertEqual(not schema_codes, valid)

    def test_closed_version_profile_subject_matrix(self):
        versions = ("1.0.0", "1.1.0", "1.2.0", None, [])
        profiles = (LEGACY_PROFILE, ATLAS_FIXTURE_PROFILE, "unknown", None, {})
        subjects = ("kfm://synthetic/evidence/legacy", ATLAS_FIXTURE_SUBJECT)
        for version in versions:
            for profile in profiles:
                for subject in subjects:
                    with self.subTest(version=version, profile=profile, subject=subject):
                        history = deepcopy(self.history)
                        history.update(schema_version=version, profile_id=profile, subject_ref=subject)
                        history["spec_hash"] = canonical_spec_hash(history)
                        valid = (
                            version == "1.0.0" and profile == LEGACY_PROFILE
                            and subject.startswith("kfm://")
                        ) or (
                            version == "1.1.0" and profile == ATLAS_FIXTURE_PROFILE
                            and subject == ATLAS_FIXTURE_SUBJECT
                        )
                        self.assert_parity(history, valid)

    def test_atlas_subject_is_literal_without_alias_or_normalization(self):
        for subject in (
            ATLAS_FIXTURE_SUBJECT + "-2", ATLAS_FIXTURE_SUBJECT.upper(),
            ATLAS_FIXTURE_SUBJECT + "\n", " " + ATLAS_FIXTURE_SUBJECT,
            "overlay:synthetic-kansas-promotion-pro\u043ef",
            "overlay%3Asynthetic-kansas-promotion-proof",
            "kfm://synthetic/atlas/alias", "https://example.invalid/atlas",
            "../atlas", "overlay:other", "", None, {},
        ):
            with self.subTest(subject=subject):
                history = deepcopy(self.history)
                history["subject_ref"] = subject
                history["spec_hash"] = canonical_spec_hash(history)
                self.assert_parity(history, False)

    def test_event_references_keep_the_legacy_grammar(self):
        for index, field in ((0, "basis_refs"), (1, "revocation_ref"),
                             (3, "correction_ref"), (5, "replacement_ref")):
            with self.subTest(field=field):
                history = deepcopy(self.history)
                history["events"][index][field] = (
                    [ATLAS_FIXTURE_SUBJECT] if field == "basis_refs" else ATLAS_FIXTURE_SUBJECT
                )
                history["spec_hash"] = canonical_spec_hash(history)
                self.assert_parity(history, False)

    def test_profile_and_identity_are_covered_by_the_original_hash_rule(self):
        history = deepcopy(self.history)
        original_hash = history["spec_hash"]
        history.update(schema_version="1.0.0", profile_id=LEGACY_PROFILE,
                       subject_ref="kfm://synthetic/atlas/alias")
        self.assertNotEqual(canonical_spec_hash(history), original_hash)
        self.assertEqual({"VERIFICATION_HISTORY_HASH_MISMATCH"},
                         {x.code for x in validate_history(history)})
        self.assert_parity(history, False)

    def test_unknown_corrected_revoked_reverified_and_superseded_replay(self):
        cases = (
            ("2026-04-12T00:00:00Z", "2026-04-13T01:05:00Z", "UNKNOWN"),
            ("2026-04-13T01:05:00Z", "2026-04-12T00:00:00Z", "UNKNOWN"),
            ("2026-04-13T00:05:00Z", "2026-04-13T01:05:00Z", "ACTIVE"),
            ("2026-04-13T00:15:00Z", "2026-04-13T00:19:59Z", "ACTIVE"),
            ("2026-04-13T00:15:00Z", "2026-04-13T00:20:00Z", "REVOKED"),
            ("2026-04-13T00:30:00Z", "2026-04-13T00:39:59Z", "REVOKED"),
            ("2026-04-13T00:30:00Z", "2026-04-13T00:40:00Z", "ACTIVE"),
            ("2026-04-13T00:45:00Z", "2026-04-13T00:50:00Z", "CORRECTED"),
            ("2026-04-13T00:55:00Z", "2026-04-13T01:00:00Z", "ACTIVE"),
            ("2026-04-13T01:00:00Z", "2026-04-13T01:05:00Z", "SUPERSEDED"),
        )
        for effective, recorded, state in cases:
            with self.subTest(effective=effective, recorded=recorded):
                replay = replay_state(self.history, effective_as_of=effective,
                                      recorded_as_of=recorded)
                self.assertEqual(state, replay.state)
                self.assertEqual(state != "ACTIVE", replay.answer_blocked)
                self.query(effective, recorded)
                result = evaluate_resolution_candidate(self.request)
                self.assertEqual("RESOLVED" if state == "ACTIVE" else "UNRESOLVED",
                                 result.status)
                if state != "ACTIVE":
                    self.assertIsNone(result.bundle_id)
                    self.assertIn("verification/" + state.lower(),
                                  {x.code for x in result.issues})

    def test_same_original_bundle_can_only_continue_governed_checks(self):
        original = deepcopy(self.request)
        result = evaluate_resolution_candidate(self.request)
        self.assertEqual("RESOLVED", result.status)
        self.assertFalse(result.as_dict()["authoritative"])
        posture = project_runtime_posture(result).as_dict()
        self.assertEqual("CONTINUE_GOVERNED_CHECKS", posture["disposition"])
        self.assertFalse(posture["authoritative"])
        self.assertFalse(posture["renderable"])
        self.assertIn("review", posture["required_next_checks"])
        self.assertIn("release", posture["required_next_checks"])
        self.assertIn("citation", posture["required_next_checks"])
        self.assertEqual(original, self.request)
        self.assertEqual(ATLAS_FIXTURE_SUBJECT, self.lookup.packet.subject_ref)
        self.assertEqual("atlas-lookup/verification-profile-review-required",
                         self.lookup.as_dict()["resolution_hold"])

    def test_policy_and_currentness_still_fail_closed(self):
        for updates, expected in (
            ({"policy_outcome": "DENY"}, "DENIED"),
            ({"policy_outcome": "ERROR"}, "ERROR"),
            ({"policy_outcome": "ABSTAIN"}, "UNRESOLVED"),
            ({"policy_decision_ref": None}, "UNRESOLVED"),
            ({"current_head": False}, "UNRESOLVED"),
            ({"bundle_id": "bundle:synthetic:wrong"}, "UNRESOLVED"),
        ):
            with self.subTest(updates=updates):
                request = deepcopy(self.request)
                request["lookup_context"].update(updates)
                result = evaluate_resolution_candidate(request)
                self.assertEqual(expected, result.status)
                self.assertIsNone(result.bundle_id)
                self.assertFalse(project_runtime_posture(result).as_dict()["renderable"])

    def test_stale_member_and_missing_history_cannot_resolve(self):
        request = deepcopy(self.request)
        request["evidence_ref"]["ref"] = "overlay:synthetic-kansas-promotion-proof-2"
        result = evaluate_resolution_candidate(request)
        self.assertEqual("UNRESOLVED", result.status)
        self.assertIn("verification/subject-mismatch", {x.code for x in result.issues})
        del request["verification_history"]
        self.assertEqual("ERROR", evaluate_resolution_candidate(request).status)

    def test_extra_approval_input_is_not_part_of_the_profile(self):
        for key in ("approved", "release", "policy_outcome", "alias", "subject_binding"):
            with self.subTest(key=key):
                history = deepcopy(self.history)
                history[key] = True
                history["spec_hash"] = canonical_spec_hash(history)
                self.assert_parity(history, False)

    def test_no_network_or_process_dependency(self):
        deny = AssertionError("unexpected external operation")
        with mock.patch.object(socket, "socket", side_effect=deny), \
                mock.patch.object(socket, "create_connection", side_effect=deny), \
                mock.patch.object(socket, "getaddrinfo", side_effect=deny), \
                mock.patch.object(subprocess, "Popen", side_effect=deny):
            self.assert_parity(self.history, True)
            self.assertEqual("RESOLVED", evaluate_resolution_candidate(self.request).status)


if __name__ == "__main__":
    unittest.main()
