# ReleaseAliasVerification source and adaptation map

## Status

**PROPOSED_INACTIVE.** This packet provides a fixture-only alias-transition preflight. It does not create or update an alias.

## Source basis

- Pass 32 immutable `spec_hash` publish-path and rollback-token cards;
- the briefing integration correction cascade and rollback classes;
- KFM release, correction, promotion, and rollback doctrine;
- accepted Directory Rules v2 through ADR-0029;
- existing conditional-write, promotion, release-manifest, correction, and rollback repository families.

## Adaptation decision

A distinct verification object is justified because an alias comparison is evidence for a later write, not the write itself. The profile checks:

- exact prior release, manifest digest, `spec_hash`, and revision;
- initial-bind shape;
- monotonic revision;
- immutable release-target identity;
- correction reference requirements; and
- rollback closure.

It remains separate from `ConditionalWritePreflight`, `PromotionDecision`, `PromotionReceipt`, `ReleaseManifest`, `CorrectionNotice`, and `RollbackCard`.

## Follow-on queue

1. Connect the verification output to a separately authorized conditional-write executor.
2. Bind actual release-manifest and rollback-card resolution in a no-network fixture integration test.
3. Add cache/search/tile invalidation completion evidence after correction propagation is proven.
4. Keep alias mutation, release, and publication outside validator authority.

## Non-effects

No alias is changed; no release is issued; no cache is invalidated; no deployment, promotion, or publication authority is created.
