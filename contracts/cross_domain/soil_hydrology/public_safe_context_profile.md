<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/cross-domain/soil-hydrology/public-safe-context-profile
title: Soil–Hydrology Public-Safe Context Candidate Profile
type: contract; cross-domain assessment profile
version: v0.1.0
status: proposed; fixture-first; no-network; non-authoritative
created: 2026-08-14
updated: 2026-08-14
policy_label: repository-facing; public-safe; non-emergency; non-publisher
owning_root: contracts/
truth_posture: cite-or-abstain
related:
  - ../../../joins/cross_lane_join_assessment.md
  - ../../../../tools/validators/cross_domain/soil_hydrology/validate_public_safe_context.py
  - ../../../../fixtures/contracts/v1/joins/soil_hydrology_public_safe_context/cases.json
  - ../../../../tests/cross_domain/soil_hydrology/test_public_safe_context.py
  - ../../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
[/KFM_META_BLOCK_V2] -->

# Soil–Hydrology Public-Safe Context Candidate Profile

## Status and purpose

**PROPOSED.** KFM has a generic deterministic `CrossLaneJoinAssessment` but no executable Soil–Hydrology pair profile in `contracts/cross_domain/`. This slice checks only whether synthetic, generalized Soil context and synthetic public Hydrology context may become a **review candidate**. `ALLOW` remains `CANDIDATE_RELATION`; it does not establish runoff, infiltration, flood risk, stream condition, watershed causation, an EvidenceBundle, policy approval, release, or publication.

## Source provenance

- `kfm_encyclopedia.pdf`, Soil domain entry — Soil owns SSURGO/gSSURGO/SDA-derived map units, components, horizons, hydrologic soil groups and soil-moisture observations; it links to Hydrology but does not own watersheds.
- `KFM_Full_Atlas_seed_cards.md`, Soil Evidence Lane — expose soil lineage and cross-domain links to Hydrology while preventing derived soil surfaces from becoming unqualified truth.
- `KFM Unified Doctrine Synthesis`, sensitivity matrix — public SSURGO/gNATSGO and Hydrology HUC12/flowline context are public-safe T0 examples; source-role preservation and release gates still apply.
- `Kansas Frontier Matrix — Connected-Dots Architecture Brief`, domain-lane doctrine — Soil and Hydrology reuse one trust spine while retaining separate domain ownership and EvidenceBundle support.

Current repository authority wins where proposals differ: accepted ADR-0029, current Directory Rules, current Soil/Hydrology domain policy surfaces, and the generic join contract/schema/helper/test family.

## Directory Rules basis

Accepted ADR-0029 assigns cross-domain pair semantics to `contracts/cross_domain/<pair>/`, shared pair validation to `tools/validators/cross_domain/<pair>/`, pair tests to `tests/cross_domain/<pair>/`, and synthetic join fixtures to the existing `fixtures/contracts/v1/joins/` family. No new root, domain authority, schema authority, policy authority, proof lane, release lane, or publication path is introduced.

## Pair rules

1. `relation_profile_ref` is `kfm:relation-profile:soil-hydrology-public-safe-context:v1`.
2. The predicate is `SPATIAL_TEMPORAL` with zero tolerance.
3. Soil is the left endpoint and Hydrology is the right endpoint for deterministic fixture behavior; ordering transfers no authority.
4. All object/source/evidence/cell references are synthetic `kfm:fixture:` references; missing EvidenceRef is allowed only so the generic finite outcome can abstain.
5. Living-person state is denied.
6. `ALLOW` requires both endpoints `PUBLIC_SAFE`, `GENERALIZED`, evidence-bearing, spatial-temporally matched, and all generic effects false.
7. Restricted exact geometry remains `DENY`; restricted generalized context remains `ABSTAIN`.
8. Modeled/aggregate/candidate source-role conflict remains `ABSTAIN`.
9. A candidate cannot be described or treated as flood-warning, emergency-alert, causal-runoff, or regulatory truth; this profile is context-only and non-emergency.

## Finite outcomes and non-effects

The generic outcomes remain authoritative: `ALLOW/JOIN_CANDIDATE`, evidence/source-role/sensitivity `ABSTAIN`, exact-sensitive or living-person `DENY`, and dependency `ERROR`. Pair validation can fail a contradictory profile declaration; such a failure creates no relation.

This profile does not activate/retrieve sources; ingest or emit geometry; resolve EvidenceRefs; evaluate live policy; create hydrologic model results, alerts, review, proof, promotion, release, correction, rollback, API, MapLibre, Evidence Drawer, Focus Mode, deployment, or publication state; or write any KFM lifecycle stage.

## Acceptance and rollback

Acceptance requires the frozen fixture matrix, pair tests, generic join regression tests, and path-scoped exact-head workflow to pass. Rollback is a revert of this bounded slice; generic join behavior remains unchanged.
