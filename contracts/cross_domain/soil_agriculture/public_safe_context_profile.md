<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/cross-domain/soil-agriculture/public-safe-context-profile
title: Soil–Agriculture Public-Safe Context Candidate Profile
type: contract; cross-domain assessment profile
version: v0.1.0
status: proposed; fixture-first; no-network; non-authoritative
created: 2026-08-14
updated: 2026-08-14
policy_label: repository-facing; public-safe; sensitivity-aware; non-publisher
owning_root: contracts/
truth_posture: cite-or-abstain
related:
  - ../../../joins/cross_lane_join_assessment.md
  - ../../../../tools/validators/cross_domain/soil_agriculture/validate_public_safe_context.py
  - ../../../../fixtures/contracts/v1/joins/soil_agriculture_public_safe_context/cases.json
  - ../../../../tests/cross_domain/soil_agriculture/test_public_safe_context.py
  - ../../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

# Soil–Agriculture Public-Safe Context Candidate Profile

## Status and purpose

**PROPOSED.** KFM already has a deterministic, fixture-first `CrossLaneJoinAssessment`, but current `contracts/cross_domain/` has no executable pair-specific Soil–Agriculture context profile. This slice checks only whether synthetic, already-generalized Soil and aggregated Agriculture references may become a **review candidate**. `ALLOW` remains `CANDIDATE_RELATION`; it never establishes crop suitability, yield causation, farm ownership, an EvidenceBundle, policy permission, review approval, release, or a public claim.

## Source provenance

- `KFM Unified Doctrine Synthesis`, §17 Cross-lane relations: Soil × Agriculture is aggregation-governed and a public farm/operator × parcel × yield join is denied.
- `KFM Unified Doctrine Synthesis`, sensitivity matrix: public SSURGO/gNATSGO is T0; agriculture county summaries are T0/T1, while private farm/operator × parcel joins deny.
- `KFM_Full_Atlas_seed_cards.md`, Soil Evidence Lane: expose soil lineage and cross-domain links to agriculture without treating derived soil surfaces as unqualified truth.
- `kfm_encyclopedia.pdf`, Soil domain entry: soil links to agriculture but does not own crop/agriculture truth.

Current repository authority wins where proposal documents differ: accepted ADR-0029, current Directory Rules, and the generic join contract/schema/helper/test family.

## Directory Rules basis

Accepted ADR-0029 assigns cross-domain pair semantics to `contracts/cross_domain/<pair>/`, shared pair validation to `tools/validators/cross_domain/<pair>/`, pair tests to `tests/cross_domain/<pair>/`, and synthetic join fixtures to the existing `fixtures/contracts/v1/joins/` family. No new root, domain authority, schema authority, policy authority, proof lane, release lane, or publication path is introduced.

## Pair rules

1. `relation_profile_ref` is `kfm:relation-profile:soil-agriculture-public-safe-context:v1`.
2. The predicate is `SPATIAL_TEMPORAL` with zero tolerance.
3. Soil is the left endpoint and Agriculture is the right endpoint for deterministic fixture behavior; ordering transfers no authority.
4. All object/source/evidence/cell references are synthetic `kfm:fixture:` references; missing EvidenceRef is allowed only so the generic finite outcome can abstain.
5. Living-person state is denied.
6. `ALLOW` requires both endpoints `PUBLIC_SAFE`, `GENERALIZED`, evidence-bearing, spatial-temporally matched, and all generic effects false.
7. Restricted exact geometry remains `DENY`; restricted generalized context remains `ABSTAIN`.
8. Modeled/aggregate/candidate source-role conflicts remain `ABSTAIN` unless both endpoint roles are the declared profile baseline.
9. Agriculture context must remain aggregate/public-safe; a `private-farm`, `operator`, or `parcel` reference cannot appear in an `ALLOW` candidate.

## Finite outcomes and non-effects

The generic outcomes remain authoritative for this candidate assessment: `ALLOW/JOIN_CANDIDATE`, evidence/source-role/sensitivity `ABSTAIN`, exact-sensitive or living-person `DENY`, and dependency `ERROR`. Pair validation may additionally fail a contradictory profile declaration; such a failure creates no relation.

This profile does not activate or retrieve sources; ingest or emit geometry; resolve EvidenceRefs; evaluate live policy; create review, proof, promotion, release, correction, rollback, API, MapLibre, Evidence Drawer, Focus Mode, deployment, or publication state; or write any KFM lifecycle stage.

## Acceptance and rollback

Acceptance requires the frozen fixture matrix, pair tests, generic join regression tests, and path-scoped exact-head workflow to pass. Rollback is a revert of this bounded slice; existing generic join behavior remains unchanged.
