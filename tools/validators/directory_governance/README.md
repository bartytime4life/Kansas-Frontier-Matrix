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

`validate_repository_topology.py` adds a twenty-rule, standard-library,
no-network ratchet over the tracked Git index. It covers root admission and root
files, safe path grammar and collisions, compatibility-root expansion,
collection spellings, speculative leaves, data and release lane placement,
policy-source singularity, trust-shaped artifacts, public/internal-store
separation, schema and document identities, generated-output provenance,
boundary READMEs, adopted-authority binding, and active-alias closure.

At the pinned `main@c259404…` baseline it records 141 exact inherited finding
groups. Those are warnings, not conformance claims: any addition or changed
fingerprint fails as new drift, any removed finding requires the baseline to
shrink in the same change, and invariant rules cannot be baselined.
In pull-request CI the proposed baseline is also compared with the trusted base
commit: waiver additions, waiver mutation, metadata changes, and deadline
extensions fail. The current file is a one-time bootstrap from `main@c259404…`;
future ordinary changes may only remove entries or shorten its deadline.

Finite outcomes are `PASS`, `FAIL_NEW_DRIFT`, `FAIL_INVARIANT`, `HOLD_UNRESOLVED`, and `ERROR_VALIDATOR`.

## Boundary

A green validator result is conformance evidence for a projection. It does not create or activate roots, authorize compatibility writes, amend Directory Rules, approve an ADR, migrate or delete paths, grant evidence or policy authority, or authorize release, deployment, promotion, or publication.

## Commands

```bash
python tools/validators/directory_governance/validate_root_registry.py --fixtures
python tools/validators/directory_governance/validate_root_registry.py
python tools/validators/directory_governance/validate_repository_topology.py --format text
python -m unittest discover \
  --start-directory tests/validators/directory_governance \
  --pattern 'test_validate_*topology.py' \
  --verbose
```
