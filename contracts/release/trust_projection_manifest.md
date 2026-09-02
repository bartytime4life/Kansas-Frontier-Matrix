<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/release/trust-projection-manifest
title: Trust Projection Manifest Contract
type: contract
version: v1.0.0
status: implemented; fixture-first; local-only; non-authoritative
owners: OWNER_TBD — release steward; review steward; integrity steward; governance steward; validation steward
created: 2026-08-07
updated: 2026-08-07
policy_label: repository-facing; release-support; integrity; time; review; governance
owning_root: contracts/
responsibility: Define bounded read-side integrity, time-slice, review-packet, and governance-change projections without creating release or approval authority.
truth_posture: cite-or-abstain
related:
  - ../../schemas/contracts/v1/release/trust_projection_manifest.schema.json
  - ../../tools/validators/release/validate_trust_projection_manifest.py
  - ../../fixtures/contracts/v1/release/trust_projection_manifest/
  - ../../tests/release/test_trust_projection_manifest.py
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
notes:
  - "These objects project trust state; they do not replace EvidenceBundle, ReviewRecord, ReleaseManifest, PromotionDecision, CorrectionNotice, or rollback authority."
[/KFM_META_BLOCK_V2] -->

# Trust projection manifests

> **Purpose.** Supply deterministic, fixture-first contracts for four missing support surfaces: local PMTiles/COG integrity results, renderer-neutral time slices, expiring read-only review packets, and append-only governance change records.

## Object families

| Object | Meaning | Non-authority boundary |
|---|---|---|
| `AssetIntegrityResult` | Compares a declared SHA-256 with locally observed bytes for PMTiles or COG assets. | Digest equality is integrity evidence only; it is not signature, policy, EvidenceBundle, or release verification. |
| `TimeSliceManifest` | Binds one valid-time interval to digest-addressed PMTiles/COG assets plus evidence, release, correction, and rollback references. | It is renderer-neutral and cannot release or publish assets. |
| `ReviewPacketReference` | Read-only, expiring, revocable navigation to existing review/release records. | It cannot grant approval authority, mutate review, or expose restricted evidence. |
| `GovernanceChangeRecord` | Append-only record of policy, waiver, milestone, vocabulary, or register changes with decision and rollback references. | It records a change; it does not approve or amend governance by itself. |

## Finite outcomes and checks

- Asset integrity: `VERIFIED | MISMATCH | MISSING_DECLARATION | INTERRUPTED | ERROR`.
- Time slices require ordered UTC intervals, at least one digest-bound asset, EvidenceBundle and ReleaseManifest references, and a rollback reference. Corrected/withdrawn slices require correction lineage.
- Review packet state is derived from `evaluated_at`, expiry, and revocation declarations; `approval_authority` is always false.
- Governance records are append-only; normative policy/vocabulary changes require at least one decision reference, and every record requires rollback support.

## Directory Rules basis

Release-support meaning belongs in `contracts/release/`; shapes in `schemas/contracts/v1/release/`; validators in `tools/validators/release/`; fixtures in `fixtures/contracts/v1/release/`; tests in `tests/release/`; orchestration in `.github/workflows/`.

## Non-effects and rollback

These fixture-only objects neither read public clients nor write release state. Revert the bounded commit to remove them; no release, review authority, governance decision, cache, deployment, or public artifact is changed.
