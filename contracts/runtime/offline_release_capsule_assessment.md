<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/runtime/offline-release-capsule-assessment
title: OfflineReleaseCapsuleAssessment Candidate Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-only; non-authoritative
owners: OWNER_TBD — Map runtime steward · Release steward · Evidence steward
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; runtime; offline; release-capsule; fail-closed
owning_root: contracts/
responsibility: Assess the declared closure and trust freshness of one synthetic offline public-release capsule without installing, reading, verifying, purging, synchronizing, or rendering it.
truth_posture: CONFIRMED synthetic fixture behavior / PROPOSED semantic contract pending steward review / NEEDS VERIFICATION hosted exact-head execution and any future runtime integration
related:
  - ../release/map_release_manifest.md
  - ./pmtiles_release_cache.md
  - ../../schemas/contracts/v1/runtime/offline_release_capsule_assessment.schema.json
  - ../../fixtures/contracts/v1/runtime/offline_release_capsule_assessment/cases.json
  - ../../tools/validators/runtime/validate_offline_release_capsule_assessment.py
  - ../../tests/validators/test_validate_offline_release_capsule_assessment.py
  - ../../docs/intake/exploratory/offline-release-capsule-assessment-source-map.md
tags: [kfm, runtime, offline, pmtiles, cache, trust-freshness, fixture]
notes:
  - "Adapts Full Atlas KFM-TRIAD-051 / KFM-CAND-0151..0153 as one bounded closure-assessment candidate."
  - "A PASS is declaration consistency only; it never permits install, cache mutation, rendering, release, or public use."
[/KFM_META_BLOCK_V2] -->

# OfflineReleaseCapsuleAssessment Candidate Contract

`OfflineReleaseCapsuleAssessmentCandidate` composes declarations already owned by the map-release manifest and PMTiles cache boundaries. It asks whether one synthetic, public-safe offline capsule inventory is complete, bound to the expected release, and current enough for a separate install or rendering review.

## Authority boundary

This packet does not define a second release manifest, cache writer, installer, verifier, correction service, or withdrawal service. It never resolves artifact bytes, checks a digest or signature, loads trust material, contacts a source, mutates browser storage, purges a cache, rolls back a release, or renders a map.

The candidate keeps four concerns distinct:

- `capsule` declares release identity, manifest digest, required public artifact roles, freshness, and optional correction, withdrawal, or rollback lineage;
- `observation` declares a synthetic local inventory and install state without reading a device;
- `capsule_assessment` is deterministically reproduced from those declarations; and
- `governance` fixes every operational and authority effect to false.

## Required inventory roles

The fixture profile requires exactly these sorted public-release roles: `CITATION_SUMMARY`, `EVIDENCE_SUMMARY`, `GLYPH_MANIFEST`, `PMTILES`, `POLICY_SNAPSHOT`, `SPRITE_MANIFEST`, `STYLE`, and `VERIFICATION_MATERIAL`. Role presence does not prove artifact integrity, rights, evidence support, or release fitness.

## Finite states

| State | Meaning | Required follow-up |
|---|---|---|
| `READY_FOR_SEPARATE_INSTALL_REVIEW` | The declaration is complete, release-bound, unexpired, and has no pending delta. | A separate governed verifier and installer must still run. |
| `UPDATE_PENDING` | A correction delta is declared but not applied. | Keep rendering disallowed and route the update for review. |
| `STALE` | The declared trust-validity time is earlier than assessment time. | Renew trust through a separate verifier; do not infer freshness. |
| `INCOMPLETE` | Required roles or release/manifest bindings do not close. | Restore or replace the capsule without partial use. |
| `ROLLBACK_REQUIRED` | The declared atomic install was interrupted. | Use separately governed rollback and purge behavior. |
| `WITHDRAWN` | A withdrawal delta applies to the capsule. | Keep use blocked and route a separately authorized purge/sync. |

Withdrawal outranks interrupted install, which outranks incomplete closure, stale trust, and a pending correction. Every valid state can accompany validator `PASS` because `PASS` means only that the report matches the declarations.

## Deterministic identity and validation

The validator requires canonical sorted role arrays, coherent time order, valid correction/withdrawal/rollback bindings, exact finite-state derivation, and RFC 8785 JCS plus SHA-256 identity. `spec_hash` excludes only `assessment_id` and `spec_hash`; the identifier uses the first 24 digest characters.

## Directory Rules basis

The release manifest remains under `contracts/release/`; bounded process composition belongs under `contracts/runtime/`. Machine shape, reusable fixtures, deterministic validation, executable evidence, CI orchestration, source adaptation, and authoring provenance stay in their established roots. No new cache, release, evidence, policy, or publication authority is created.

## Non-effects and rollback

A green result cannot approve a release, assert cryptographic verification, permit stale content, authorize install or rendering, mutate or purge a cache, synchronize over a network, resolve evidence, evaluate policy, approve review, deploy, publish, or permit public use. Before merge, close the draft PR and retire its branch. After an authorized merge, revert the additive packet; it has no live consumer or external state.
