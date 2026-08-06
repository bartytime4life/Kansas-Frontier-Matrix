from __future__ import annotations
import copy
import json
import os
import socket
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock
REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_SRC = REPO_ROOT / 'packages/hashing/src'
for path in (REPO_ROOT, PACKAGE_SRC):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))
from hashing import compute_spec_hash, load_json_file
from tools.validators.governance.validate_ai_change_proposal import FIXTURE_ROOT, Finding, _apply_compare_and_set, _expected_proposal_id, _patch_projection, run_fixture_suite, validate_document, validate_files

class AIChangeProposalTests(unittest.TestCase):

    def setUp(self) -> None:
        self.subject_path = FIXTURE_ROOT / 'subjects/base.json'
        self.subject = load_json_file(self.subject_path)

    def _proposal(self, relative: str) -> dict[str, object]:
        candidate = load_json_file(FIXTURE_ROOT / relative)
        self.assertIsInstance(candidate, dict)
        return candidate

    def test_fixture_manifest_has_exact_polarity(self) -> None:
        ok, payload = run_fixture_suite()
        self.assertTrue(ok, payload)
        self.assertEqual(payload['outcome'], 'PASS')
        self.assertEqual(payload['cases'], 13)
        self.assertEqual(payload['findings'], [])

    def test_valid_ready_proposal_is_conformant(self) -> None:
        proposal = self._proposal('valid/valid_ready.json')
        result = validate_document(proposal, self.subject)
        self.assertEqual(result.outcome, 'PASS', result.findings)
        self.assertEqual(proposal['readiness']['disposition'], 'READY_FOR_STEWARD_APPLY')
        self.assertFalse(proposal['permissions']['may_mutate_repository'])

    def test_pending_review_remains_hold(self) -> None:
        proposal = self._proposal('valid/valid_hold_pending_review.json')
        result = validate_document(proposal, self.subject)
        self.assertEqual(result.outcome, 'PASS', result.findings)
        self.assertEqual(proposal['human_attestation']['state'], 'PENDING')
        self.assertEqual(proposal['readiness']['disposition'], 'HOLD')

    def test_policy_denial_remains_deny(self) -> None:
        proposal = self._proposal('valid/valid_deny_policy.json')
        result = validate_document(proposal, self.subject)
        self.assertEqual(result.outcome, 'PASS', result.findings)
        self.assertEqual(proposal['policy_projection']['outcome'], 'DENY')
        self.assertEqual(proposal['readiness']['disposition'], 'DENY')

    def test_add_replace_and_remove_are_compare_and_set(self) -> None:
        operations = [{'op': 'add', 'path': '/new', 'before': {'present': False}, 'after': {'present': True, 'value': 'created'}}, {'op': 'remove', 'path': '/settings/labels/status', 'before': {'present': True, 'value': 'draft'}, 'after': {'present': False}}, {'op': 'replace', 'path': '/thresholds/minimum', 'before': {'present': True, 'value': 10}, 'after': {'present': True, 'value': 20}}]
        output, findings = _apply_compare_and_set(self.subject, operations, allow_already_applied=False)
        self.assertEqual(findings, set())
        self.assertIsInstance(output, dict)
        self.assertEqual(output['new'], 'created')
        self.assertNotIn('status', output['settings']['labels'])
        self.assertEqual(output['thresholds']['minimum'], 20)

    def test_replay_is_idempotent(self) -> None:
        proposal = self._proposal('valid/valid_ready.json')
        operations = proposal['patch']['operations']
        first, first_findings = _apply_compare_and_set(self.subject, operations, allow_already_applied=False)
        second, second_findings = _apply_compare_and_set(first, operations, allow_already_applied=True)
        self.assertEqual(first_findings, set())
        self.assertEqual(second_findings, set())
        self.assertEqual(first, second)

    def test_unexpected_preimage_denies_without_mutation(self) -> None:
        proposal = self._proposal('valid/valid_ready.json')
        changed_subject = copy.deepcopy(self.subject)
        changed_subject['settings']['enabled'] = 'unexpected'
        snapshot = copy.deepcopy(changed_subject)
        result = validate_document(proposal, changed_subject)
        self.assertEqual(result.outcome, 'DENY')
        self.assertIn(Finding('INPUT_SPEC_HASH_MISMATCH', '$.subject.input_spec_hash'), result.findings)
        self.assertIn(Finding('PATCH_PREIMAGE_MISMATCH', '$.patch.operations[0].before'), result.findings)
        self.assertEqual(changed_subject, snapshot)

    def test_proposal_identity_excludes_review_transition(self) -> None:
        proposal = self._proposal('valid/valid_ready.json')
        transitioned = copy.deepcopy(proposal)
        transitioned['created_at'] = '2030-01-01T00:00:00Z'
        transitioned['policy_projection']['outcome'] = 'HOLD'
        transitioned['human_attestation'] = {'required': True, 'state': 'PENDING', 'review_record_ref': None}
        transitioned['readiness'] = {'disposition': 'HOLD', 'reason_codes': ['HUMAN_PENDING', 'OBLIGATIONS_SATISFIED', 'PATCH_VERIFIED', 'POLICY_HELD', 'READINESS_HELD']}
        self.assertEqual(_expected_proposal_id(proposal), _expected_proposal_id(transitioned))

    def test_patch_hash_covers_only_algorithm_and_operations(self) -> None:
        proposal = self._proposal('valid/valid_ready.json')
        expected = compute_spec_hash(_patch_projection(proposal))
        self.assertEqual(proposal['patch']['patch_spec_hash'], expected)
        changed_claims = copy.deepcopy(proposal)
        changed_claims['patch']['claims']['minimal'] = False
        self.assertEqual(compute_spec_hash(_patch_projection(changed_claims)), expected)

    def test_validation_does_not_mutate_inputs(self) -> None:
        proposal = self._proposal('valid/valid_ready.json')
        proposal_snapshot = copy.deepcopy(proposal)
        subject_snapshot = copy.deepcopy(self.subject)
        validate_document(proposal, self.subject)
        self.assertEqual(proposal, proposal_snapshot)
        self.assertEqual(self.subject, subject_snapshot)

    def test_duplicate_json_keys_fail_as_error(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            proposal_path = Path(directory) / 'duplicate.json'
            proposal_path.write_text('{"schema_version":"1.0.0","schema_version":"1.0.0"}', encoding='utf-8')
            result = validate_files(proposal_path, self.subject_path)
        self.assertEqual(result.outcome, 'ERROR')
        self.assertEqual(result.findings, (Finding('PROPOSAL_JSON_INVALID', '$'),))

    def test_schema_closes_authority_overreach(self) -> None:
        result = validate_files(FIXTURE_ROOT / 'invalid/invalid_permission_overreach.json', self.subject_path)
        self.assertEqual(result.outcome, 'DENY')
        self.assertEqual(result.findings, (Finding('SCHEMA_INVALID', '$.permissions.may_mutate_repository'),))

    def test_fixture_suite_is_no_network(self) -> None:
        with mock.patch.object(socket, 'socket', side_effect=AssertionError('network access denied')):
            ok, payload = run_fixture_suite()
        self.assertTrue(ok, payload)

    def test_cli_output_is_deterministic(self) -> None:
        command = [sys.executable, str(REPO_ROOT / 'tools/validators/governance/validate_ai_change_proposal.py'), '--proposal', str(FIXTURE_ROOT / 'valid/valid_ready.json'), '--subject', str(self.subject_path)]
        environment = dict(os.environ)
        environment['KFM_NO_NETWORK'] = '1'
        first = subprocess.run(command, cwd=REPO_ROOT, env=environment, check=False, capture_output=True, text=True)
        second = subprocess.run(command, cwd=REPO_ROOT, env=environment, check=False, capture_output=True, text=True)
        self.assertEqual(first.returncode, 0, first.stderr)
        self.assertEqual(first.stdout, second.stdout)
        payload = json.loads(first.stdout)
        self.assertEqual(payload['outcome'], 'PASS')
        self.assertEqual(payload['authority'], 'NONE')
if __name__ == '__main__':
    unittest.main()
