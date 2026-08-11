from __future__ import annotations
import argparse
import copy
import hashlib
import json
import math
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Mapping, Sequence
import yaml
from jsonschema import Draft202012Validator, FormatChecker
REPO_ROOT = Path(__file__).resolve().parents[3]
SCHEMA_PATH = REPO_ROOT / 'schemas/contracts/v1/governance/domain_context_map_assessment.schema.json'
FIXTURE_PATH = REPO_ROOT / 'fixtures/contracts/v1/governance/domain_context_map_assessment/cases.json'
DOMAIN_REGISTER_PATH = REPO_ROOT / 'control_plane/domain_lane_register.yaml'
SEAM_REGISTER_PATH = REPO_ROOT / 'control_plane/cross_domain_seam_register.yaml'
MAX_FILE_BYTES = 1048576
DIRECTIONAL = {'CUSTOMER_SUPPLIER', 'CONFORMIST', 'ANTICORRUPTION_LAYER', 'OPEN_HOST_SERVICE'}
NON_DIRECTIONAL = {'PARTNERSHIP', 'SHARED_KERNEL', 'PUBLISHED_LANGUAGE', 'SEPARATE_WAYS'}
ABSTAIN_CODES = {'CONTEXT_MAP_PATTERN_UNRESOLVED'}

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
    outcome: str
    findings: tuple[Finding, ...]
    assessment_state: str | None = None

    @property
    def codes(self) -> list[str]:
        return sorted({item.code for item in self.findings})

def _pairs(items: list[tuple[str, object]]) -> dict[str, object]:
    result: dict[str, object] = {}
    for key, value in items:
        if key in result:
            raise DuplicateKeyError
        result[key] = value
    return result

def _nonfinite(_value: str) -> object:
    raise NonFiniteNumberError

def _finite_float(value: str) -> float:
    parsed = float(value)
    if not math.isfinite(parsed):
        raise NonFiniteNumberError
    return parsed

def load_json_object(path: Path) -> tuple[dict[str, object] | None, list[Finding]]:
    try:
        if path.is_symlink():
            return (None, [Finding('INPUT_SYMLINK_DENIED', '/')])
        if not path.is_file():
            return (None, [Finding('FILE_NOT_FOUND', '/')])
        if path.stat().st_size > MAX_FILE_BYTES:
            return (None, [Finding('FILE_TOO_LARGE', '/')])
        value = json.loads(path.read_text(encoding='utf-8'), object_pairs_hook=_pairs, parse_constant=_nonfinite, parse_float=_finite_float)
    except DuplicateKeyError:
        return (None, [Finding('JSON_DUPLICATE_KEY', '/')])
    except NonFiniteNumberError:
        return (None, [Finding('JSON_NONFINITE_NUMBER', '/')])
    except (OSError, UnicodeError, json.JSONDecodeError, RecursionError, ValueError):
        return (None, [Finding('JSON_INVALID', '/')])
    if not isinstance(value, dict):
        return (None, [Finding('ROOT_NOT_OBJECT', '/')])
    return (value, [])

def canonical_hash(value: object) -> str:
    payload = json.dumps(value, ensure_ascii=False, allow_nan=False, sort_keys=True, separators=(',', ':')).encode('utf-8')
    return 'sha256:' + hashlib.sha256(payload).hexdigest()

def compute_profile_hash(candidate: Mapping[str, object]) -> str:
    subject = copy.deepcopy(dict(candidate))
    subject.pop('profile_spec_hash', None)
    return canonical_hash(subject)

def _schema_findings(candidate: object) -> list[Finding]:
    try:
        schema = json.loads(SCHEMA_PATH.read_text(encoding='utf-8'))
        Draft202012Validator.check_schema(schema)
        validator = Draft202012Validator(schema, format_checker=FormatChecker())
        errors = sorted(validator.iter_errors(candidate), key=lambda error: (list(error.absolute_path), str(error.validator)))
    except (OSError, UnicodeError, json.JSONDecodeError, ValueError, RecursionError):
        return [Finding('SCHEMA_UNAVAILABLE', '/')]
    return [Finding('SCHEMA_INVALID', '/' + '/'.join((str(x) for x in error.absolute_path))) for error in errors[:100]]

def _load_projections(repo_root: Path) -> tuple[set[str] | None, dict[str, tuple[str, ...]] | None, Finding | None]:
    try:
        domain_path = repo_root / DOMAIN_REGISTER_PATH.relative_to(REPO_ROOT)
        seam_path = repo_root / SEAM_REGISTER_PATH.relative_to(REPO_ROOT)
        if domain_path.is_symlink() or seam_path.is_symlink():
            raise OSError
        domains_doc = yaml.safe_load(domain_path.read_text(encoding='utf-8'))
        seams_doc = json.loads(seam_path.read_text(encoding='utf-8'), object_pairs_hook=_pairs)
        domains = {entry['lane_id'] for entry in domains_doc['entries']}
        seams = {entry['seam_id']: tuple(entry['participants']) for entry in seams_doc['entries']}
    except (OSError, UnicodeError, yaml.YAMLError, json.JSONDecodeError, DuplicateKeyError, KeyError, TypeError, ValueError):
        return (None, None, Finding('CONTEXT_MAP_PROJECTION_UNAVAILABLE', '/projection_refs'))
    return (domains, seams, None)

def _canonical_strings(value: object) -> bool:
    return isinstance(value, list) and all((isinstance(x, str) for x in value)) and (value == sorted(set(value)))

def _semantic_findings(candidate: Mapping[str, object], *, repo_root: Path) -> tuple[list[Finding], bool]:
    findings: set[Finding] = set()
    if candidate.get('profile_spec_hash') != compute_profile_hash(candidate):
        findings.add(Finding('PROFILE_SPEC_HASH_MISMATCH', '/profile_spec_hash'))
    domains, seams, projection_error = _load_projections(repo_root)
    if projection_error is not None:
        return ([projection_error], True)
    assert domains is not None and seams is not None
    binding = candidate['seam_binding']
    relation = candidate['relationship']
    assert isinstance(binding, Mapping) and isinstance(relation, Mapping)
    seam_id = binding['seam_id']
    participants = binding['participant_contexts']
    assert isinstance(seam_id, str) and isinstance(participants, list)
    if not _canonical_strings(participants):
        findings.add(Finding('CONTEXT_MAP_PARTICIPANTS_NOT_CANONICAL', '/seam_binding/participant_contexts'))
    for index, context_id in enumerate(participants):
        if context_id not in domains:
            findings.add(Finding('CONTEXT_MAP_CONTEXT_UNKNOWN', f'/seam_binding/participant_contexts/{index}'))
    expected = seams.get(seam_id)
    if expected is None:
        findings.add(Finding('CONTEXT_MAP_SEAM_UNKNOWN', '/seam_binding/seam_id'))
    elif tuple(sorted(participants)) != tuple(expected):
        findings.add(Finding('CONTEXT_MAP_PARTICIPANTS_MISMATCH', '/seam_binding/participant_contexts'))
    state = relation['mapping_state']
    pattern = relation['pattern']
    upstream = relation['upstream_context']
    downstream = relation['downstream_context']
    rationale = relation['rationale_summary']
    assert isinstance(state, str) and isinstance(pattern, str)
    if state == 'UNRESOLVED' or pattern == 'UNRESOLVED':
        if not (state == 'UNRESOLVED' and pattern == 'UNRESOLVED' and (upstream is None) and (downstream is None) and (rationale is None)):
            findings.add(Finding('CONTEXT_MAP_UNRESOLVED_FIELDS_INVALID', '/relationship'))
        else:
            findings.add(Finding('CONTEXT_MAP_PATTERN_UNRESOLVED', '/relationship/pattern'))
    elif state != 'PROPOSED_MAPPING':
        findings.add(Finding('CONTEXT_MAP_MAPPING_STATE_INVALID', '/relationship/mapping_state'))
    elif pattern in DIRECTIONAL:
        if upstream is None or downstream is None:
            findings.add(Finding('CONTEXT_MAP_DIRECTION_REQUIRED', '/relationship'))
        elif upstream == downstream or upstream not in participants or downstream not in participants:
            findings.add(Finding('CONTEXT_MAP_DIRECTION_ENDPOINTS_INVALID', '/relationship'))
    elif pattern in NON_DIRECTIONAL:
        if upstream is not None or downstream is not None:
            findings.add(Finding('CONTEXT_MAP_DIRECTION_PROHIBITED', '/relationship'))
    else:
        findings.add(Finding('CONTEXT_MAP_PATTERN_INVALID', '/relationship/pattern'))
    return (sorted(findings), False)

def validate_candidate(candidate: object, *, repo_root: Path=REPO_ROOT) -> ValidationResult:
    schema_findings = _schema_findings(candidate)
    if schema_findings:
        return ValidationResult('ERROR', tuple(schema_findings), None)
    assert isinstance(candidate, dict)
    findings, system_error = _semantic_findings(candidate, repo_root=repo_root)
    codes = {item.code for item in findings}
    if system_error:
        outcome = 'ERROR'
    elif not codes:
        outcome = 'PASS'
    elif codes <= ABSTAIN_CODES:
        outcome = 'ABSTAIN'
    else:
        outcome = 'DENY'
    return ValidationResult(outcome, tuple(findings), 'REVIEW_REQUIRED' if outcome == 'PASS' else None)

def _merge_patch(base: object, patch: object) -> object:
    if not isinstance(patch, dict):
        return copy.deepcopy(patch)
    target = copy.deepcopy(base) if isinstance(base, dict) else {}
    for key, value in patch.items():
        target[key] = _merge_patch(target.get(key), value)
    return target

def materialize_fixture_case(manifest: Mapping[str, object], entry: Mapping[str, object]) -> dict[str, object]:
    candidate = _merge_patch(manifest['base_candidate'], entry.get('patch', {}))
    assert isinstance(candidate, dict)
    candidate['profile_spec_hash'] = compute_profile_hash(candidate)
    if entry.get('tamper') == 'profile_hash':
        candidate['profile_spec_hash'] = 'sha256:' + 'f' * 64
    return candidate

def load_fixtures() -> dict[str, object]:
    value, findings = load_json_object(FIXTURE_PATH)
    if value is None:
        raise ValueError(findings)
    return value

def validate_fixture_manifest() -> list[dict[str, object]]:
    manifest = load_fixtures()
    results: list[dict[str, object]] = []
    for entry in manifest['cases']:
        candidate = materialize_fixture_case(manifest, entry)
        result = validate_candidate(candidate)
        observed = {'outcome': result.outcome, 'codes': result.codes}
        expected = entry['expected']
        results.append({'name': entry['name'], 'ok': observed == expected, 'expected': expected, 'observed': observed})
    return results

def _serialize(result: ValidationResult) -> str:
    return json.dumps({'assessment_state': result.assessment_state, 'authority': {'writes_register': False, 'authorizes_join': False, 'authorizes_mutation': False, 'authorizes_release': False, 'publishes': False}, 'codes': result.codes, 'outcome': result.outcome}, sort_keys=True, separators=(',', ':'))

def main(argv: Sequence[str] | None=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--fixtures', action='store_true')
    group.add_argument('--input', type=Path)
    args = parser.parse_args(argv)
    if args.fixtures:
        results = validate_fixture_manifest()
        print(json.dumps(results, indent=2, sort_keys=True))
        return 0 if all((item['ok'] for item in results)) else 1
    candidate, load_findings = load_json_object(args.input)
    result = ValidationResult('ERROR', tuple(load_findings), None) if candidate is None else validate_candidate(candidate)
    print(_serialize(result))
    return 0 if result.outcome == 'PASS' else 1
if __name__ == '__main__':
    raise SystemExit(main())
