#!/usr/bin/env python3
import hashlib, json, sys
from pathlib import Path
from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[3]
SCHEMA = ROOT / 'schemas/contracts/v1/source/official_source_snapshot_lineage_assessment.schema.json'
EXPECTED_REASON = {
    'CURRENT': 'SINGLE_CURRENT_CANDIDATE',
    'SUPERSEDED': 'NEWER_SNAPSHOT_SUPERSEDES_PRIOR',
    'CORRECTED': 'SOURCE_CORRECTION_RECORDED',
    'CONFLICTED': 'SOURCE_CONFLICT_UNRESOLVED',
    'WITHDRAWN': 'SOURCE_WITHDRAWAL_RECORDED',
}

def canonical_payload(obj):
    x = dict(obj); x.pop('assessment_id', None)
    return json.dumps(x, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()

def expected_id(obj):
    return 'kfm:source-snapshot-lineage:' + hashlib.sha256(canonical_payload(obj)).hexdigest()

def validate(obj):
    schema = json.loads(SCHEMA.read_text())
    errors = sorted(Draft202012Validator(schema, format_checker=FormatChecker()).iter_errors(obj), key=lambda e: list(e.path))
    if errors:
        return False, 'SCHEMA_INVALID'
    refs = obj['snapshot_refs']
    if refs != sorted(refs): return False, 'SNAPSHOT_REFS_NOT_SORTED'
    if obj['assessment_id'] != expected_id(obj): return False, 'ASSESSMENT_ID_MISMATCH'
    for key in ('supersedes','correction_refs','withdrawal_refs'):
        if any(r not in refs for r in obj[key]): return False, 'LINEAGE_REF_OUTSIDE_SET'
    state, preferred = obj['lineage_state'], obj['preferred_snapshot_ref']
    if obj['reason_codes'] != [EXPECTED_REASON[state]]: return False, 'REASON_CODE_MISMATCH'
    if state == 'CURRENT' and not (len(refs)==1 and preferred==refs[0] and not obj['supersedes'] and not obj['correction_refs'] and not obj['withdrawal_refs']): return False, 'CURRENT_RULE'
    if state == 'SUPERSEDED' and not (preferred in refs and obj['supersedes'] and preferred not in obj['supersedes'] and not obj['correction_refs'] and not obj['withdrawal_refs']): return False, 'SUPERSEDED_RULE'
    if state == 'CORRECTED' and not (preferred in refs and obj['correction_refs'] and preferred not in obj['correction_refs'] and not obj['supersedes'] and not obj['withdrawal_refs']): return False, 'CORRECTED_RULE'
    if state == 'CONFLICTED' and not (len(refs)>=2 and preferred is None and not obj['supersedes'] and not obj['correction_refs'] and not obj['withdrawal_refs']): return False, 'CONFLICTED_RULE'
    if state == 'WITHDRAWN' and not (preferred is None and obj['withdrawal_refs'] and not obj['supersedes'] and not obj['correction_refs']): return False, 'WITHDRAWN_RULE'
    return True, 'PASS'

def main(path):
    try: obj=json.loads(Path(path).read_text())
    except Exception: print('ERROR'); return 2
    ok, reason=validate(obj)
    print('PASS' if ok else f'DENY:{reason}')
    return 0 if ok else 1

if __name__ == '__main__':
    if len(sys.argv)!=2: print('ERROR'); raise SystemExit(2)
    raise SystemExit(main(sys.argv[1]))
