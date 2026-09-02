<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/release/release-alias-verification
title: ReleaseAliasVerification Contract
type: semantic-contract; release preflight; fixture-only
version: v0.1.0
status: proposed; inactive; fixture-only; non-mutating
owners: OWNER_TBD — Release steward · Correction steward · Integrity steward
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; release; alias; rollback; immutable-target
related:
  - ../../schemas/contracts/v1/release/release_alias_verification.schema.json
[/KFM_META_BLOCK_V2] -->

# ReleaseAliasVerification

A `ReleaseAliasVerification` is a deterministic, non-mutating preflight record for an immutable release-alias transition. It compares the observed alias binding with the expected prior release, manifest digest, `spec_hash`, and revision; then checks the proposed immutable target and rollback/correction references.

It exists to prevent current aliases from being repointed on stale assumptions, reused release identifiers, mismatched digests, non-monotonic revisions, missing correction lineage, or missing rollback targets. It never writes an alias, assembles a release, approves promotion, changes a cache, deploys, or publishes.

## Actions

- `INITIAL_BIND`: bind an unbound alias to revision 1.
- `ADVANCE`: move a bound alias to a new immutable release after exact prior-state comparison.
- `CORRECTION`: issue a superseding release with an explicit correction reference.
- `ROLLBACK`: restore a prior immutable release through an explicit rollback reference.

## Finite outcomes

| Outcome | Meaning | Validator result |
|---|---|---|
| `READY` | Declaration is internally coherent for later steward-controlled execution. | `PASS` |
| `HOLD` | Observed alias state is unknown. | `ABSTAIN` |
| `DENY` | Prior state, revision, immutability, correction, or rollback closure fails. | `DENY` |
| `ERROR` | Explicit evaluation failure. | `ERROR` |

A `PASS` is not execution authority. A separate conditional-write, policy, review, promotion, release, and publication flow remains required.

## Directory Rules basis

Meaning belongs in `contracts/release/`; shape in `schemas/contracts/v1/release/`; synthetic cases in `fixtures/contracts/v1/release/`; validation in `tools/validators/release/`; tests in `tests/validators/`; CI in `.github/workflows/`; source adaptation in `docs/intake/exploratory/`; and generated authoring provenance in `data/receipts/generated/`.

## Rollback

Revert the additive fixture-only packet. No alias, release, cache, deployment, or public artifact is changed.
