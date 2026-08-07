# Directory Governance Validators

Deterministic, no-network validators for the machine projections and decision records required by adopted KFM Directory Rules v2.

## Root Registry

`validate_root_registry.py` validates:

- strict JSON-compatible YAML parsing;
- Draft 2020-12 schema conformance;
- the exact adopted Directory Rules digest and `ADR-0029` binding;
- canonical ordering and unique root identities/paths;
- class, status, target, activation, exit, and single-write invariants;
- canonical-root parity;
- top-level repository-root coverage at a pinned checkout;
- reviewed valid/invalid fixture polarity.

## Path Decision Record

`validate_path_decision_record.py` validates reviewable `PLACE`, `SPLIT`, `MIGRATE`, `MIRROR`, `HOLD`, and `DENY` placement records against the pinned Root Registry. It checks responsibility signatures, evidence/rule references, hard placement exclusions, and outcome-specific companion evidence.

## Path Alias Register

`validate_path_alias_register.py` validates accepted compatibility path and identity mappings. It checks:

- exact Directory Rules and Root Registry binding;
- unique old paths, alias IDs, and identity aliases;
- active canonical targets and object-family/root compatibility;
- dual-read/single-write behavior with no alias writers;
- class-specific legacy, mirror, external-export, transitional, and deprecated semantics;
- exposure/mutation non-escalation;
- expiry, consumer, parity, exit, and rollback requirements;
- repository path, legacy Git blob, and canonical digest parity;
- reviewed valid/invalid fixture polarity.

Finite outcomes are `PASS`, `FAIL_NEW_DRIFT`, `FAIL_INVARIANT`, `HOLD_UNRESOLVED`, and `ERROR_VALIDATOR`.

## Boundary

A green validator result is conformance evidence for a projection or decision record. It does not create or activate roots, authorize compatibility writes, amend Directory Rules, approve an ADR, migrate or delete paths, close consumers, grant evidence or policy authority, or authorize release, deployment, promotion, or publication.

## Commands

```bash
python tools/validators/directory_governance/validate_root_registry.py --fixtures
python tools/validators/directory_governance/validate_root_registry.py
python tools/validators/directory_governance/validate_path_decision_record.py --fixtures
python tools/validators/directory_governance/validate_path_alias_register.py --fixtures
python tools/validators/directory_governance/validate_path_alias_register.py
python -m unittest discover \
  --start-directory tests/validators/directory_governance \
  --pattern 'test_validate_path_alias_register.py' \
  --verbose
```
