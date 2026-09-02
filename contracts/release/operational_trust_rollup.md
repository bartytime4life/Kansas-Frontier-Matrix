<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/release/operational-trust-rollup
title: OperationalTrustRollup Contract
type: semantic-contract; read-only trust projection
version: v1.0.0
status: proposed-inactive; fixture-only; no-network; non-authoritative
created: 2026-08-09
updated: 2026-08-09
owning_root: contracts/
policy_label: internal; release-candidate; observability; trust-rollup
related:
  - ../../schemas/contracts/v1/release/operational_trust_rollup.schema.json
  - ../../fixtures/contracts/v1/release/operational_trust_rollup/cases.json
  - ../../tools/validators/release/validate_operational_trust_rollup.py
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

# OperationalTrustRollup

`OperationalTrustRollup` is a read-only release-candidate projection that makes evidence resolution, policy posture, signature state, validation, human review, catalog closure, correction readiness, and rollback readiness visible in one deterministic envelope.

## Boundary

The rollup consumes declared references and status values only. It does not resolve those references, authenticate review, verify signatures, execute policy, promote, release, deploy, publish, or authorize public use. `READY` means the declaration is internally complete under this inactive profile; it is not a `PromotionDecision` or `ReleaseManifest`.

## Finite outcomes

- `READY` — every component is declared complete and reference-bearing;
- `HOLD` — evidence, policy, signature, review, or catalog state is pending or open;
- `DENY` — an explicit denial, failed validation/signature, missing correction path, missing rollback, or integrity mismatch is present;
- `ERROR` — a component reports operational error or the input is malformed.

Successful component states require immutable supporting references. Every authority claim is fixed to `false`, and mutable `latest` references are rejected by schema.

## Directory Rules basis

Meaning belongs in `contracts/release/`; shape in `schemas/contracts/v1/release/`; synthetic cases in `fixtures/contracts/v1/release/`; validation in `tools/validators/release/`; tests in `tests/validators/`; CI in `.github/workflows/`; and generated authoring accountability in `data/receipts/generated/`. The packet adds a read-only profile inside existing responsibility roots and creates no parallel observability, proof, release, or publication authority.

## Validation

```bash
python -m unittest tests.validators.test_validate_operational_trust_rollup -v
python tools/validators/release/validate_operational_trust_rollup.py --fixtures
```

## Rollback

Revert the additive packet. It performs no lifecycle, source, catalog, policy, review, signature, release, cache, API, or public-route mutation.
