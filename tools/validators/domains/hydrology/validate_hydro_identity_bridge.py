#!/usr/bin/env python3
"""Validate one deterministic, no-network HydroIdentityBridge packet."""
from __future__ import annotations
import argparse
import hashlib
import json
import math
import sys
from dataclasses import dataclass
from itertools import islice
from pathlib import Path
from typing import Any, Iterable, Mapping, Sequence
from jsonschema import Draft202012Validator, FormatChecker
REPO_ROOT = Path(__file__).resolve().parents[4]
SCHEMA_PATH = REPO_ROOT / 'schemas/contracts/v1/domains/hydrology/hydro_identity_bridge.schema.json'
MAX_BYTES = 1048576
MAX_SCHEMA_FINDINGS = 100
SCOPE = 'hydro-identity-bridge-only'

class DuplicateKeyError(ValueError):
    pass

class NonFiniteNumberError(ValueError):
    pass

@dataclass(frozen=True, order=True)
class Finding:
    code: str
    field: str

@dataclass(frozen=True)
class ValidationResult:
    findings: tuple[Finding, ...]
    packet_outcome: str | None = None

    @property
    def ok(self) -> bool:
        return not self.findings

    @property
    def operational_error(self) -> bool:
        prefixes = ('FILE_', 'INPUT_', 'JSON_', 'SCHEMA_UNAVAILABLE')
        return any((item.code.startswith(prefixes) for item in self.findings))

def _unique_object(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise DuplicateKeyError(key)
        result[key] = value
    return result

def _reject_nonfinite(_value: str) -> None:
    raise NonFiniteNumberError

def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed

def _read(path: Path) -> tuple[dict[str, Any] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return (None, [Finding('INPUT_SYMLINK_DENIED', '/')])
        if not path.is_file():
            return (None, [Finding('FILE_NOT_FOUND', '/')])
        if path.stat().st_size > MAX_BYTES:
            return (None, [Finding('FILE_TOO_LARGE', '/')])
        value = json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=_unique_object, parse_constant=_reject_nonfinite, parse_float=_finite_float)
    except UnicodeDecodeError:
        return (None, [Finding('JSON_NOT_UTF8', '/')])
    except DuplicateKeyError:
        return (None, [Finding('JSON_DUPLICATE_KEY', '/')])
    except NonFiniteNumberError:
        return (None, [Finding('JSON_NONFINITE_NUMBER', '/')])
    except json.JSONDecodeError:
        return (None, [Finding('JSON_INVALID', '/')])
    except OSError:
        return (None, [Finding('FILE_READ_ERROR', '/')])
    except (RecursionError, ValueError):
        return (None, [Finding('JSON_COMPLEXITY_LIMIT', '/')])
    if not isinstance(value, dict):
        return (None, [Finding('ROOT_NOT_OBJECT', '/')])
    return (value, [])

def _pointer(parts: Iterable[Any]) -> str:
    encoded = [str(part).replace('~', '~0').replace('/', '~1') for part in parts]
    return '/' + '/'.join(encoded) if encoded else '/'

def _schema_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding='utf-8'))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        errors = list(islice(validator.iter_errors(candidate), MAX_SCHEMA_FINDINGS + 1))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding('SCHEMA_UNAVAILABLE', '/')]
    findings = [Finding('SCHEMA_INVALID', _pointer(error.absolute_path)) for error in sorted(errors[:MAX_SCHEMA_FINDINGS], key=lambda item: (_pointer(item.absolute_path), str(item.validator)))]
    if len(errors) > MAX_SCHEMA_FINDINGS:
        findings.append(Finding('SCHEMA_FINDINGS_TRUNCATED', '/'))
    return findings

def canonical_spec_hash(candidate: Mapping[str, Any]) -> str:
    projected = dict(candidate)
    projected.pop('bridge_id', None)
    projected.pop('spec_hash', None)
    encoded = json.dumps(projected, sort_keys=True, separators=(',', ':'), ensure_ascii=False, allow_nan=False).encode('utf-8')
    return 'sha256:' + hashlib.sha256(encoded).hexdigest()

def expected_bridge_id(candidate: Mapping[str, Any]) -> str:
    return 'hydro-bridge:' + canonical_spec_hash(candidate).removeprefix('sha256:')[:24]

def _mapping(value: Any) -> dict[str, Any]:
    return value if isinstance(value, dict) else {}

def _array(value: Any) -> list[Any]:
    return value if isinstance(value, list) else []

def _canonical_strings(values: list[Any]) -> bool:
    return all((isinstance(item, str) for item in values)) and values == sorted(set(values))

def _canonical_current(values: list[Any]) -> bool:
    tuples = [(item.get('id_type'), item.get('value')) for item in values if isinstance(item, dict)]
    return len(tuples) == len(values) and tuples == sorted(set(tuples))

def _semantic_findings(candidate: Mapping[str, Any]) -> list[Finding]:
    findings: list[Finding] = []
    try:
        if candidate.get('spec_hash') != canonical_spec_hash(candidate):
            findings.append(Finding('SPEC_HASH_MISMATCH', '/spec_hash'))
        if candidate.get('bridge_id') != expected_bridge_id(candidate):
            findings.append(Finding('BRIDGE_ID_MISMATCH', '/bridge_id'))
    except (TypeError, ValueError, RecursionError):
        findings.append(Finding('IDENTITY_COMPUTATION_ERROR', '/'))
    versions = _mapping(candidate.get('source_versions'))
    crosswalk = _mapping(versions.get('crosswalk'))
    temporal = _mapping(candidate.get('temporal_basis'))
    if temporal.get('crosswalk_release_id') != crosswalk.get('release_id'):
        findings.append(Finding('CROSSWALK_RELEASE_BASIS_MISMATCH', '/temporal_basis/crosswalk_release_id'))
    request = _mapping(candidate.get('request'))
    resolution = _mapping(candidate.get('resolution'))
    current = _array(resolution.get('current_identifiers'))
    legacy = _array(resolution.get('legacy_comids'))
    reasons = _array(resolution.get('reason_codes'))
    evidence = _array(resolution.get('evidence_refs'))
    if not _canonical_current(current):
        findings.append(Finding('CURRENT_IDENTIFIERS_NOT_CANONICAL', '/resolution/current_identifiers'))
    for values, code, field in ((legacy, 'LEGACY_COMIDS_NOT_CANONICAL', '/resolution/legacy_comids'), (reasons, 'REASON_CODES_NOT_CANONICAL', '/resolution/reason_codes'), (evidence, 'EVIDENCE_REFS_NOT_CANONICAL', '/resolution/evidence_refs')):
        if not _canonical_strings(values):
            findings.append(Finding(code, field))
    current_values = {item.get('value') for item in current if isinstance(item, dict) and isinstance(item.get('value'), str)}
    legacy_values = {item for item in legacy if isinstance(item, str)}
    outcome = resolution.get('outcome')
    relationship = resolution.get('relationship_type')
    reason_set = {item for item in reasons if isinstance(item, str)}
    receipt = resolution.get('join_receipt_ref')
    overlap = current_values & legacy_values
    relabel_denied = outcome == 'DENY' and relationship == 'UNRESOLVED' and ('LEGACY_ID_RELABELED_AS_CURRENT' in reason_set)
    if overlap and (not relabel_denied):
        findings.append(Finding('LEGACY_ID_RELABEL_NOT_DENIED', '/resolution/current_identifiers'))
    kind = request.get('identifier_kind')
    identifier = request.get('identifier')
    if kind == 'LEGACY_COMID' and outcome != 'ERROR' and (identifier not in legacy_values):
        findings.append(Finding('REQUEST_NOT_BOUND_TO_LEGACY_ID', '/request/identifier'))
    if kind in {'CURRENT_PERMANENT_IDENTIFIER', 'CURRENT_NHDPLUSID'} and relationship != 'UNRESOLVED':
        expected_type = 'PERMANENT_IDENTIFIER' if kind.endswith('PERMANENT_IDENTIFIER') else 'NHDPLUSID'
        if not any((isinstance(item, dict) and item.get('id_type') == expected_type and (item.get('value') == identifier) for item in current)):
            findings.append(Finding('REQUEST_NOT_BOUND_TO_CURRENT_ID', '/request/identifier'))
    abstain_reasons = {'SPLIT': 'AMBIGUOUS_SPLIT', 'MERGE': 'AMBIGUOUS_MERGE', 'RETIRED': 'LEGACY_RETIRED', 'NO_LEGACY': 'NO_LEGACY_MAPPING', 'UNRESOLVED': 'IDENTIFIER_UNRESOLVED'}
    if outcome == 'ANSWER':
        if relationship != 'EXACT':
            findings.append(Finding('OUTCOME_RELATIONSHIP_MISMATCH', '/resolution/relationship_type'))
        if len(current) != 1 or len(legacy) != 1:
            findings.append(Finding('ANSWER_NOT_ONE_TO_ONE', '/resolution'))
        if not isinstance(receipt, str):
            findings.append(Finding('ANSWER_JOIN_RECEIPT_REQUIRED', '/resolution/join_receipt_ref'))
        if 'EXACT_ONE_TO_ONE' not in reason_set:
            findings.append(Finding('ANSWER_REASON_REQUIRED', '/resolution/reason_codes'))
    elif outcome == 'ABSTAIN':
        expected = abstain_reasons.get(relationship)
        if expected is None:
            findings.append(Finding('OUTCOME_RELATIONSHIP_MISMATCH', '/resolution/relationship_type'))
        elif expected not in reason_set:
            findings.append(Finding('ABSTAIN_REASON_MISMATCH', '/resolution/reason_codes'))
        if not isinstance(receipt, str):
            findings.append(Finding('ABSTAIN_JOIN_RECEIPT_REQUIRED', '/resolution/join_receipt_ref'))
    elif outcome == 'DENY':
        if relationship != 'UNRESOLVED':
            findings.append(Finding('OUTCOME_RELATIONSHIP_MISMATCH', '/resolution/relationship_type'))
        allowed = {'LEGACY_ID_RELABELED_AS_CURRENT', 'SOURCE_VERSION_MISMATCH', 'UNTRUSTED_BRIDGE_INPUT'}
        if not reason_set & allowed:
            findings.append(Finding('DENY_REASON_REQUIRED', '/resolution/reason_codes'))
        if not isinstance(receipt, str):
            findings.append(Finding('DENY_JOIN_RECEIPT_REQUIRED', '/resolution/join_receipt_ref'))
    elif outcome == 'ERROR':
        if relationship != 'UNRESOLVED':
            findings.append(Finding('OUTCOME_RELATIONSHIP_MISMATCH', '/resolution/relationship_type'))
        if 'OPERATIONAL_ERROR' not in reason_set:
            findings.append(Finding('ERROR_REASON_REQUIRED', '/resolution/reason_codes'))
        if receipt is not None:
            findings.append(Finding('ERROR_JOIN_RECEIPT_FORBIDDEN', '/resolution/join_receipt_ref'))
    governance = _mapping(candidate.get('governance'))
    if governance.get('source_native_ids_preserved') is not True or governance.get('legacy_relabel_denied') is not True:
        findings.append(Finding('SOURCE_NATIVE_ID_BOUNDARY_VIOLATION', '/governance'))
    for name in ('geometry_equality_assumed', 'authority_created', 'source_data_mutated', 'policy_evaluated', 'promotion_authorized', 'release_authorized', 'publication_authorized'):
        if governance.get(name) is not False:
            findings.append(Finding('GOVERNANCE_BOUNDARY_VIOLATION', f'/governance/{name}'))
    return findings

def validate_payload(candidate: Mapping[str, Any]) -> ValidationResult:
    findings = _schema_findings(candidate)
    if not findings:
        findings.extend(_semantic_findings(candidate))
    resolution = candidate.get('resolution')
    packet_outcome = resolution.get('outcome') if isinstance(resolution, dict) else None
    return ValidationResult(tuple(sorted(set(findings))), packet_outcome if isinstance(packet_outcome, str) else None)

def validate_file(path: Path) -> ValidationResult:
    candidate, findings = _read(path)
    if candidate is None:
        return ValidationResult(tuple(sorted(set(findings))))
    return validate_payload(candidate)

def _display(path: Path) -> str:
    try:
        return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()
    except (OSError, ValueError):
        return path.name

def main(argv: Sequence[str] | None=None) -> int:
    parser = argparse.ArgumentParser(description='Validate one HydroIdentityBridge packet.')
    parser.add_argument('path', type=Path)
    args = parser.parse_args(argv)
    result = validate_file(args.path)
    outcome = 'PASS' if result.ok else 'ERROR' if result.operational_error else 'FAIL'
    print(json.dumps({'file': _display(args.path), 'findings': [{'code': item.code, 'field': item.field} for item in result.findings], 'outcome': outcome, 'packet_outcome': result.packet_outcome, 'scope': SCOPE, 'authority': {'network_fetch': False, 'source_activation': False, 'source_data_mutation': False, 'policy_evaluation': False, 'promotion': False, 'release': False, 'publication': False}}, sort_keys=True, separators=(',', ':')))
    return 0 if result.ok else 1
if __name__ == '__main__':
    sys.exit(main())
