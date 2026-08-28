<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/offline-release-capsule-assessment-source-map
title: Offline Release Capsule Assessment - Source Map and Implementation Boundary
type: exploratory-intake-source-map
version: v0.1.0
status: promoted-to-fixture-candidate; non-authoritative; repository-grounded
owners: OWNER_TBD — Intake steward · Map runtime steward · Release steward
created: 2026-08-09
updated: 2026-08-09
policy_label: public; intake; map; offline; release-capsule; cite-or-abstain
owning_root: docs/
responsibility: Preserve traceability from supplied offline-release proposals to one bounded runtime assessment without duplicating release, verification, cache, policy, review, or publication authority.
truth_posture: CONFIRMED source-card traceability and inspected-tree collision review / PROPOSED bounded adaptation / NEEDS VERIFICATION steward review, future runtime integration, and later-main collisions
related:
  - ../../kfm_full_atlas_seed_cards.md
  - ../../doctrine/directory-rules.md
  - ../../adr/ADR-0029-adopt-directory-governance-standard-v2.md
  - ../../../contracts/runtime/offline_release_capsule_assessment.md
  - ../../../contracts/runtime/pmtiles_release_cache.md
  - ../../../contracts/release/map_release_manifest.md
tags: [kfm, intake, full-atlas, offline, pmtiles, cache, trust-freshness]
notes:
  - "Repository collision review was refreshed against main@169ac1946812b6452a28c38ee57bc78ee41901b8."
  - "The supplied MapLibre operating manual was text-extracted and rendered at pages 11, 12, and 21 for boundary and rollback QA."
[/KFM_META_BLOCK_V2] -->

# Offline release capsule assessment - source map

> **Outcome:** `KFM-TRIAD-051` and programming card `KFM-CAND-0153` are adapted into a synthetic, no-network closure assessment that composes existing release and cache authorities without implementing an offline product.

## Source lineage

| Source | Relevant proposal | Posture used here |
|---|---|---|
| Supplied/Drive `KFM_Full_Atlas_seed_cards.md` | `KFM-TRIAD-051`, `KFM-CAND-0151`, `KFM-CAND-0152`, and `KFM-CAND-0153` | Design lineage for capsule inventory, trust freshness, atomic update, correction, withdrawal, and reconnect cases. |
| Supplied `KFM MapLibre Operating Architecture, Governed UI, and AI Interaction Manual - Revised Working Edition` | Released-only browser assets, manifest hashes, cache invalidation, rollback, and resource-bound trust display | Supporting architecture; rendered pages were inspected, but the working edition does not become repository policy. |
| Existing `MapReleaseManifest` contract | Release artifact, policy, evidence, correction, cache, and rollback bindings | Canonical release meaning retained without modification. |
| Existing PMTiles cache projection | Release-scoped cache key and no-network first-run, offline, stale, partial, withdrawal, and internal-source cases | Canonical browser-cache boundary retained without modification. |
| Directory Rules plus accepted ADR-0029 | Responsibility-root placement and no-parallel-authority rules | Placement authority. |

## Current-main collision review

At `main@169ac1946812b6452a28c38ee57bc78ee41901b8`, the repository already defines the release manifest and a no-side-effect PMTiles cache-policy projection. Those families own release closure and cache-decision meaning. No common executable candidate was found that merely composes their declared identities with offline inventory, trust expiry, correction, withdrawal, and atomic-install state. This is **CONFIRMED for the inspected tree**, not a timeless repository claim.

## Bounded adaptation

The candidate keeps exact release and manifest identity, a sorted public artifact-role inventory, install and last-verified times, trust validity, optional correction/withdrawal/rollback lineage, finite assessment states, deterministic identity, and fixed-false authority flags.

It deliberately excludes artifact bytes, restricted geometry, live storage, service workers, network access, cryptography, signer or policy decisions, installation, cache mutation or purge, rollback execution, synchronization, rendering, review approval, release, deployment, publication, and public use.

## Why this is not `OfflineReleaseCapsule`

Creating a second capsule manifest would overlap the existing `MapReleaseManifest`; creating an installer or cache writer would cross the runtime boundary without an accepted consumer. The safe first slice is therefore named an assessment candidate. It can expose missing closure and stale or withdrawn declarations while every consequential effect remains false.

## Directory Rules placement

| Artifact responsibility | Path |
|---|---|
| Bounded runtime-composition meaning | `contracts/runtime/offline_release_capsule_assessment.md` |
| Canonical machine shape | `schemas/contracts/v1/runtime/offline_release_capsule_assessment.schema.json` |
| Reusable synthetic cases | `fixtures/contracts/v1/runtime/offline_release_capsule_assessment/cases.json` |
| Repository validator | `tools/validators/runtime/validate_offline_release_capsule_assessment.py` |
| Executable evidence | `tests/validators/test_validate_offline_release_capsule_assessment.py` |
| Hosted read-only orchestration | `.github/workflows/offline-release-capsule-assessment.yml` |
| Human source adaptation | This file under `docs/intake/exploratory/` |
| AI-authoring process memory | `data/receipts/generated/` |

No new root or parallel release, cache, verification, policy, review, receipt, proof, or publication home is created.

## Validation and rollback

Validation covers Draft 2020-12 schema validity, all six finite states, exact fixture polarity, canonical roles, time order, delta bindings, deterministic identity, parser bounds, no-network behavior, adjacent PMTiles/cache and map-release boundaries, workflow parsing, documentation metadata, and generated-receipt hashes.

Rollback is an ordinary revert of the additive packet. No live capsule, cache, device, network, release, or public state is created.
