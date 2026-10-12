from __future__ import annotations
import argparse
import copy
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Mapping, Sequence
from jsonschema import Draft202012Validator, FormatChecker
REPO_ROOT = Path(__file__).resolve().parents[3]
PACKAGE_SRC = REPO_ROOT / 'packages/hashing/src'
for path in (REPO_ROOT, PACKAGE_SRC):
    if str(path) not in sys.path:
        sys.path.insert(0, str(path))
from hashing import CanonicalizationFailure, JsonInputError, canonicalize_json, compute_spec_hash, load_json_file
SCHEMA_PATH = REPO_ROOT / 'schemas/contracts/v1/governance/ai_change_proposal.schema.json'
FIXTURE_ROOT = REPO_ROOT / 'fixtures/contracts/v1/governance/ai_change_proposal'
MANIFEST_PATH = FIXTURE_ROOT / 'expected_findings_manifest.json'
SCOPE = 'governance.ai_change_proposal'
NON_EFFECTS = ['no_repository_mutation', 'no_canonical_write', 'no_evidence_resolution', 'no_policy_evaluation', 'no_human_approval_creation', 'no_promotion_release_or_publication']
_SCHEMA = json.loads(SCHEMA_PATH.read_text(encoding='utf-8'))
_SCHEMA_VALIDATOR = Draft202012Validator(_SCHEMA, format_checker=FormatChecker())

@dataclass(frozen=True, order=True)
class Finding:
    code: str
    path: str

@dataclass(frozen=True)
class ValidationResult:
    outcome: str
    findings: tuple[Finding, ...]
    proposal_id: str | None = None
    patch_spec_hash: str | None = None
    input_spec_hash: str | None = None
    output_spec_hash: str | None = None

def _json_path(parts: Sequence[object]) -> str:
    result = '$'
    for part in parts:
        if isinstance(part, int):
            result += f'[{part}]'
        else:
            result += f'.{part}'
    return result

def _pointer_path(index: int, suffix: str='') -> str:
    base = f'$.patch.operations[{index}]'
    return base + suffix

def _decode_pointer(pointer: str) -> tuple[str, ...]:
    return tuple((token.replace('~1', '/').replace('~0', '~') for token in pointer[1:].split('/')))

def _patch_projection(candidate: Mapping[str, Any]) -> dict[str, object]:
    patch = candidate['patch']
    return {'algorithm': patch['algorithm'], 'operations': patch['operations']}

def _proposal_identity_projection(candidate: Mapping[str, Any]) -> dict[str, object]:
    patch = candidate['patch']
    return {'schema_version': candidate['schema_version'], 'profile': candidate['profile'], 'producer': candidate['producer'], 'evidence_refs': candidate['evidence_refs'], 'subject': candidate['subject'], 'patch': {'algorithm': patch['algorithm'], 'operations': patch['operations'], 'patch_spec_hash': patch['patch_spec_hash'], 'claims': patch['claims']}}

def _expected_proposal_id(candidate: Mapping[str, Any]) -> str:
    digest = compute_spec_hash(_proposal_identity_projection(candidate))
    return 'kfm:ai-change-proposal:' + digest.removeprefix('sha256:')

def _state_matches(*, present: bool, value: object, expected: Mapping[str, Any]) -> bool:
    if present != expected['present']:
        return False
    return not present or value == expected.get('value')

def _operation_state_is_valid(operation: Mapping[str, Any]) -> bool:
    before = operation['before']
    after = operation['after']
    op = operation['op']
    if op == 'add':
        return before['present'] is False and after['present'] is True
    if op == 'remove':
        return before['present'] is True and after['present'] is False
    if op == 'replace':
        return before['present'] is True and after['present'] is True and (before.get('value') != after.get('value'))
    return False

def _validate_operation_set(operations: list[Mapping[str, Any]]) -> set[Finding]:
    findings: set[Finding] = set()
    pointers = [operation['path'] for operation in operations]
    if pointers != sorted(pointers):
        findings.add(Finding('PATCH_PATH_ORDER_INVALID', '$.patch.operations'))
    if len(set(pointers)) != len(pointers):
        findings.add(Finding('PATCH_PATH_DUPLICATE', '$.patch.operations'))
    decoded = [_decode_pointer(pointer) for pointer in pointers]
    for index, operation in enumerate(operations):
        if not _operation_state_is_valid(operation):
            findings.add(Finding('PATCH_OPERATION_STATE_INVALID', _pointer_path(index)))
    for left_index, left in enumerate(decoded):
        for right_index in range(left_index + 1, len(decoded)):
            right = decoded[right_index]
            shorter = min(len(left), len(right))
            if left[:shorter] == right[:shorter]:
                findings.add(Finding('PATCH_PATH_OVERLAP', '$.patch.operations'))
    return findings

def _apply_compare_and_set(subject: object, operations: list[Mapping[str, Any]], *, allow_already_applied: bool) -> tuple[object | None, set[Finding]]:
    output = copy.deepcopy(subject)
    findings: set[Finding] = set()
    for index, operation in enumerate(operations):
        tokens = _decode_pointer(operation['path'])
        parent = output
        for token in tokens[:-1]:
            if isinstance(parent, list):
                findings.add(Finding('PATCH_ARRAY_PATH_UNSUPPORTED', _pointer_path(index, '.path')))
                return (None, findings)
            if not isinstance(parent, dict):
                findings.add(Finding('PATCH_CONTAINER_NOT_OBJECT', _pointer_path(index, '.path')))
                return (None, findings)
            if token not in parent:
                findings.add(Finding('PATCH_PARENT_MISSING', _pointer_path(index, '.path')))
                return (None, findings)
            parent = parent[token]
        if isinstance(parent, list):
            findings.add(Finding('PATCH_ARRAY_PATH_UNSUPPORTED', _pointer_path(index, '.path')))
            return (None, findings)
        if not isinstance(parent, dict):
            findings.add(Finding('PATCH_CONTAINER_NOT_OBJECT', _pointer_path(index, '.path')))
            return (None, findings)
        key = tokens[-1]
        present = key in parent
        current = parent.get(key)
        before = operation['before']
        after = operation['after']
        if allow_already_applied and _state_matches(present=present, value=current, expected=after):
            continue
        if not _state_matches(present=present, value=current, expected=before):
            findings.add(Finding('PATCH_PREIMAGE_MISMATCH', _pointer_path(index, '.before')))
            return (None, findings)
        if after['present']:
            parent[key] = copy.deepcopy(after['value'])
        else:
            del parent[key]
    return (output, findings)

def _canonical_items(values: list[object]) -> list[bytes]:
    return [canonicalize_json(value) for value in values]

def _expected_readiness(candidate: Mapping[str, Any]) -> tuple[str, list[str], bool]:
    policy = candidate['policy_projection']
    review = candidate['human_attestation']
    required = set(_canonical_items(policy['required_obligations']))
    satisfied = set(_canonical_items(policy['satisfied_obligations']))
    obligations_complete = required.issubset(satisfied)
    if policy['outcome'] == 'DENY' or review['state'] == 'REJECTED':
        disposition = 'DENY'
    elif policy['outcome'] == 'HOLD' or not obligations_complete or review['state'] == 'PENDING':
        disposition = 'HOLD'
    else:
        disposition = 'READY_FOR_STEWARD_APPLY'
    codes = {'PATCH_VERIFIED'}
    codes.add({'ALLOW': 'POLICY_ALLOWED', 'HOLD': 'POLICY_HELD', 'DENY': 'POLICY_DENIED'}[policy['outcome']])
    codes.add('OBLIGATIONS_SATISFIED' if obligations_complete else 'OBLIGATIONS_PENDING')
    codes.add({'APPROVED': 'HUMAN_APPROVED', 'PENDING': 'HUMAN_PENDING', 'REJECTED': 'HUMAN_REJECTED'}[review['state']])
    codes.add({'READY_FOR_STEWARD_APPLY': 'READY_FOR_STEWARD_APPLY', 'HOLD': 'READINESS_HELD', 'DENY': 'READINESS_DENIED'}[disposition])
    return (disposition, sorted(codes), obligations_complete)

def validate_document(candidate: object, subject: object) -> ValidationResult:
    findings: set[Finding] = set()
    schema_errors = sorted(_SCHEMA_VALIDATOR.iter_errors(candidate), key=lambda error: tuple((str(part) for part in error.absolute_path)))
    for error in schema_errors:
        findings.add(Finding('SCHEMA_INVALID', _json_path(tuple(error.absolute_path))))
    if schema_errors or not isinstance(candidate, dict):
        return ValidationResult('DENY', tuple(sorted(findings)))
    if not isinstance(subject, dict):
        findings.add(Finding('SUBJECT_ROOT_NOT_OBJECT', '$subject'))
        return ValidationResult('DENY', tuple(sorted(findings)))
    evidence_refs = candidate['evidence_refs']
    if evidence_refs != sorted(evidence_refs):
        findings.add(Finding('EVIDENCE_REF_ORDER_INVALID', '$.evidence_refs'))
    operations = candidate['patch']['operations']
    findings.update(_validate_operation_set(operations))
    try:
        actual_patch_hash = compute_spec_hash(_patch_projection(candidate))
        actual_proposal_id = _expected_proposal_id(candidate)
        actual_input_hash = compute_spec_hash(subject)
    except CanonicalizationFailure:
        findings.add(Finding('CANONICALIZATION_ERROR', '$'))
        return ValidationResult('DENY', tuple(sorted(findings)))
    if candidate['patch']['patch_spec_hash'] != actual_patch_hash:
        findings.add(Finding('PATCH_SPEC_HASH_MISMATCH', '$.patch.patch_spec_hash'))
    if candidate['proposal_id'] != actual_proposal_id:
        findings.add(Finding('PROPOSAL_ID_MISMATCH', '$.proposal_id'))
    if candidate['subject']['input_spec_hash'] != actual_input_hash:
        findings.add(Finding('INPUT_SPEC_HASH_MISMATCH', '$.subject.input_spec_hash'))
    structural_codes = {'PATCH_PATH_ORDER_INVALID', 'PATCH_PATH_DUPLICATE', 'PATCH_PATH_OVERLAP', 'PATCH_OPERATION_STATE_INVALID'}
    if not any((finding.code in structural_codes for finding in findings)):
        output, patch_findings = _apply_compare_and_set(subject, operations, allow_already_applied=False)
        findings.update(patch_findings)
        if output is not None:
            actual_output_hash = compute_spec_hash(output)
            if candidate['subject']['expected_output_spec_hash'] != actual_output_hash:
                findings.add(Finding('OUTPUT_SPEC_HASH_MISMATCH', '$.subject.expected_output_spec_hash'))
            replayed, replay_findings = _apply_compare_and_set(output, operations, allow_already_applied=True)
            findings.update(replay_findings)
            if replayed is None or replayed != output:
                findings.add(Finding('PATCH_IDEMPOTENCY_FAILED', '$.patch.claims.idempotent'))
        else:
            actual_output_hash = None
    else:
        actual_output_hash = None
    policy = candidate['policy_projection']
    required_bytes = _canonical_items(policy['required_obligations'])
    satisfied_bytes = _canonical_items(policy['satisfied_obligations'])
    if required_bytes != sorted(required_bytes):
        findings.add(Finding('OBLIGATION_ORDER_INVALID', '$.policy_projection.required_obligations'))
    if satisfied_bytes != sorted(satisfied_bytes):
        findings.add(Finding('OBLIGATION_ORDER_INVALID', '$.policy_projection.satisfied_obligations'))
    required_set = set(required_bytes)
    if not set(satisfied_bytes).issubset(required_set):
        findings.add(Finding('UNDECLARED_SATISFIED_OBLIGATION', '$.policy_projection.satisfied_obligations'))
    expected_disposition, expected_codes, _ = _expected_readiness(candidate)
    readiness = candidate['readiness']
    if readiness['disposition'] != expected_disposition:
        findings.add(Finding('READINESS_DISPOSITION_MISMATCH', '$.readiness.disposition'))
    if readiness['reason_codes'] != expected_codes:
        findings.add(Finding('READINESS_REASON_CODES_MISMATCH', '$.readiness.reason_codes'))
    return ValidationResult('DENY' if findings else 'PASS', tuple(sorted(findings)), proposal_id=actual_proposal_id, patch_spec_hash=actual_patch_hash, input_spec_hash=actual_input_hash, output_spec_hash=actual_output_hash)

def validate_files(proposal_path: Path, subject_path: Path) -> ValidationResult:
    try:
        candidate = load_json_file(proposal_path)
    except JsonInputError:
        return ValidationResult('ERROR', (Finding('PROPOSAL_JSON_INVALID', '$'),))
    try:
        subject = load_json_file(subject_path)
    except JsonInputError:
        return ValidationResult('ERROR', (Finding('SUBJECT_JSON_INVALID', '$subject'),))
    return validate_document(candidate, subject)

def _serialize_result(result: ValidationResult, *, proposal_path: Path | None=None, subject_path: Path | None=None) -> str:
    payload = {'authority': 'NONE', 'execution_mode': 'FIXTURE_ONLY', 'findings': [{'code': finding.code, 'path': finding.path} for finding in result.findings], 'non_effects': NON_EFFECTS, 'outcome': result.outcome, 'patch_spec_hash': result.patch_spec_hash, 'proposal': str(proposal_path) if proposal_path else None, 'proposal_id': result.proposal_id, 'scope': SCOPE, 'subject': str(subject_path) if subject_path else None, 'subject_input_spec_hash': result.input_spec_hash, 'subject_output_spec_hash': result.output_spec_hash}
    return json.dumps(payload, sort_keys=True, separators=(',', ':'))

def run_fixture_suite() -> tuple[bool, dict[str, object]]:
    try:
        manifest = load_json_file(MANIFEST_PATH)
    except JsonInputError:
        payload = {'authority': 'NONE', 'cases': 0, 'execution_mode': 'FIXTURE_ONLY', 'findings': [{'code': 'FIXTURE_MANIFEST_INVALID', 'path': str(MANIFEST_PATH)}], 'non_effects': NON_EFFECTS, 'outcome': 'ERROR', 'scope': SCOPE}
        return (False, payload)
    suite_findings: list[dict[str, object]] = []
    cases = manifest.get('cases', []) if isinstance(manifest, dict) else []
    for index, case in enumerate(cases):
        if not isinstance(case, dict):
            suite_findings.append({'code': 'FIXTURE_CASE_INVALID', 'case': index, 'path': f'$.cases[{index}]'})
            continue
        proposal_path = FIXTURE_ROOT / str(case.get('proposal', ''))
        subject_path = FIXTURE_ROOT / str(case.get('subject', ''))
        result = validate_files(proposal_path, subject_path)
        actual_findings = [{'code': finding.code, 'path': finding.path} for finding in result.findings]
        if result.outcome != case.get('expected_outcome'):
            suite_findings.append({'actual': result.outcome, 'case': case.get('case_id'), 'code': 'FIXTURE_OUTCOME_MISMATCH', 'expected': case.get('expected_outcome')})
        if actual_findings != case.get('expected_findings'):
            suite_findings.append({'actual': actual_findings, 'case': case.get('case_id'), 'code': 'FIXTURE_FINDINGS_MISMATCH', 'expected': case.get('expected_findings')})
    payload = {'authority': 'NONE', 'cases': len(cases), 'execution_mode': 'FIXTURE_ONLY', 'findings': suite_findings, 'non_effects': NON_EFFECTS, 'outcome': 'DENY' if suite_findings else 'PASS', 'scope': SCOPE}
    return (not suite_findings, payload)

def main(argv: Sequence[str] | None=None) -> int:
    parser = argparse.ArgumentParser(description='Validate fixture-only deterministic AI change proposals.')
    parser.add_argument('--fixtures', action='store_true', help='validate the exact fixture manifest')
    parser.add_argument('--proposal', type=Path, help='proposal JSON path')
    parser.add_argument('--subject', type=Path, help='subject JSON path')
    args = parser.parse_args(argv)
    if args.fixtures:
        if args.proposal or args.subject:
            parser.error('--fixtures cannot be combined with --proposal/--subject')
        ok, payload = run_fixture_suite()
        print(json.dumps(payload, sort_keys=True, separators=(',', ':')))
        return 0 if ok else 1
    if args.proposal is None or args.subject is None:
        parser.error('--proposal and --subject are required together')
    result = validate_files(args.proposal, args.subject)
    print(_serialize_result(result, proposal_path=args.proposal, subject_path=args.subject))
    if result.outcome == 'PASS':
        return 0
    if result.outcome == 'DENY':
        return 1
    return 2
if __name__ == '__main__':
    raise SystemExit(main())
