# Directory Governance Validators

Deterministic, no-network validators for the machine projections and decision records required by adopted KFM Directory Rules v2.

## Current slice

`validate_root_registry.py` validates:

- strict JSON-compatible YAML parsing;
- Draft 2020-12 schema conformance;
- the exact adopted Directory Rules digest and `ADR-0029` binding;
- canonical ordering and unique root identities/paths;
- class, status, target, activation, exit, and single-write invariants;
- canonical-root parity;
- top-level repository-root coverage at a pinned checkout;
- reviewed valid/invalid fixture polarity.

Finite outcomes are `PASS`, `FAIL_NEW_DRIFT`, `FAIL_INVARIANT`, `HOLD_UNRESOLVED`, and `ERROR_VALIDATOR`.

## Boundary

A green validator result is conformance evidence for a projection. It does not create or activate roots, authorize compatibility writes, amend Directory Rules, approve an ADR, migrate or delete paths, grant evidence or policy authority, or authorize release, deployment, promotion, or publication.

## Commands

```bash
python tools/validators/directory_governance/validate_root_registry.py --fixtures
python tools/validators/directory_governance/validate_root_registry.py
python -m unittest discover \
  --start-directory tests/validators/directory_governance \
  --pattern 'test_validate_root_registry.py' \
  --verbose
```
