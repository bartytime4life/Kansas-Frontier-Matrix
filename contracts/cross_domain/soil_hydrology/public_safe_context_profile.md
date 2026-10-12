<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/cross-domain/soil-hydrology/public-safe-context-profile
title: Soil–Hydrology Public-Safe Context Candidate Profile
type: contract; cross-domain assessment profile
version: v0.2.0
status: proposed; fixture-first; no-network; non-authoritative
created: 2026-08-14
updated: 2026-09-08
policy_label: repository-facing; public-safe; non-emergency; sensitivity-aware; non-publisher
owning_root: contracts/
responsibility: Define the pair-specific meaning, coherence checks, and finite outcomes for a synthetic Soil–Hydrology context candidate without creating hydrologic truth, policy approval, release, or publication authority.
truth_posture: cite-or-abstain
related:
  - ../../joins/cross_lane_join_assessment.md
  - ../../../tools/validators/cross_domain/soil_hydrology/validate_public_safe_context.py
  - ../../../fixtures/contracts/v1/joins/soil_hydrology_public_safe_context/cases.json
  - ../../../tests/cross_domain/soil_hydrology/test_public_safe_context.py
  - ../../../.github/workflows/soil-hydrology-public-safe-context.yml
  - ../../../docs/adr/ADR-0009-hydrology-is-the-first-proof-bearing-lane.md
  - ../../../docs/adr/ADR-0026-hydrology-source-spine-starts-with-wbd-huc12.md
  - ../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
notes:
  - "ALLOW means only that the generic join helper emitted a reviewable candidate and this pair profile accepted its declared synthetic, generalized, public-safe fixture posture."
  - "The v1 fixture uses equal OBSERVED roles to exercise the generic candidate lane; it does not classify production HSG interpretation or WBD/HUC12 boundary context as observation truth."
  - "No coordinate or geometry bytes, live source, lifecycle write, EvidenceBundle creation, policy decision, review decision, release decision, public route, emergency use, or publication is in scope."
[/KFM_META_BLOCK_V2] -->

# Soil–Hydrology Public-Safe Context Candidate Profile

## Status and purpose

**PROPOSED.** KFM has an executable, deterministic, fixture-first Soil–Hydrology pair profile layered over the generic `CrossLaneJoinAssessment`. This contract defines what that bounded implementation means. It checks only whether a synthetic, already-generalized Soil context reference and a synthetic Hydrology context reference may become a **review candidate**. `ALLOW` remains `CANDIDATE_RELATION`; it never establishes infiltration, runoff, recharge, flood risk, stream condition, watershed causation, an EvidenceBundle, policy permission, review approval, release, or a public claim.

## Source provenance

The pair-specific profile is derived from proposal sources and reconciled against current repository authority:

- `KFM Soil Architecture Extended Pro PDF-Only Planning Report` — keeps soil interpretations, source roles, limitations, EvidenceBundle support, and public-safe delivery distinct; it does not prove mounted implementation or source admission.
- `KFM Hydrology Extended Pro PDF-Only Reference Report` — separates boundary context, observations, regulatory flood context, modeled output, and event evidence; it forbids treating NFHL context as observed inundation and keeps simulation non-authoritative without model evidence and review.
- `kfm_encyclopedia.pdf`, Soil domain entry — Soil owns map units, components, horizons, hydrologic soil groups, and soil-moisture observations; it may link to Hydrology but does not own watersheds or water truth.
- `KFM_Full_Atlas_seed_cards.md`, Soil Evidence Lane — exposes soil lineage and governed cross-domain links without turning derived soil surfaces into unqualified truth.

Current repository authority wins where proposal material differs: accepted ADR-0029 and Directory Rules govern placement; the generic join contract/schema/helper govern shared behavior; the pair validator, seven-case fixture matrix, six focused tests, and path-scoped workflow define the implemented pair boundary. ADR-0009 and ADR-0026 remain proposed and provide hydrology planning context, not source-admission, release, or publication authority.

## Directory Rules basis

Accepted ADR-0029 assigns cross-domain pair semantics to `contracts/cross_domain/<pair>/`, shared pair validation to `tools/validators/cross_domain/<pair>/`, pair tests to `tests/cross_domain/<pair>/`, and synthetic join fixtures to the existing `fixtures/contracts/v1/joins/` family. This update remains in the established Soil–Hydrology seam and introduces no new root, domain authority, schema authority, policy authority, proof lane, release lane, or publication path.

## Required endpoint roles

| Side | Required domain | Permitted fixture meaning | Excluded meaning |
|---|---|---|---|
| Left | `soil` | A synthetic, generalized Soil context reference, currently represented by an HSG-context fixture. | Measured infiltration, runoff causation, parcel suitability, or complete soil truth. |
| Right | `hydrology` | A synthetic, generalized Hydrology context reference, currently represented by a WBD/HUC12-context fixture. | Observed inundation, flood warning, emergency alert, forecast, or complete water truth. |
| Output | `CANDIDATE_RELATION` | A reviewable context candidate produced by the generic helper. | Canonical relation, EvidenceBundle, policy decision, release decision, or public-use authorization. |

Both endpoints retain their independent object, source-descriptor, source-role, EvidenceRef, sensitivity, geometry-precision, spatial-cell, and valid-time fields. Endpoint ordering and candidate creation cannot transfer or collapse authority between Soil and Hydrology.

## Pair-specific rules

1. `relation_profile_ref` must equal `kfm:relation-profile:soil-hydrology-public-safe-context:v1`.
2. The request must use `SPATIAL_TEMPORAL` with zero temporal tolerance. The generic helper owns interval matching; this pair profile cannot weaken it.
3. Soil is the left endpoint and Hydrology is the right endpoint so fixtures and findings remain deterministic. This is an execution convention, not an authority transfer.
4. Object, source-descriptor, evidence, and spatial-cell references must be synthetic `kfm:fixture:` references. An EvidenceRef may be `null` only so the generic evaluator can return `ABSTAIN / EVIDENCE_REF_MISSING`.
5. Both endpoints must declare `living_person: false`; any other state fails pair-profile coherence.
6. `ALLOW / JOIN_CANDIDATE` requires both endpoints to be `PUBLIC_SAFE`, `GENERALIZED`, evidence-bearing, spatial-temporally matched, and non-publishing, with every generic effect set to `false`.
7. Restricted exact geometry remains `DENY / GEOMETRY_PRECISION_BLOCKED`; restricted generalized context remains `ABSTAIN / SENSITIVITY_REVIEW_REQUIRED`.
8. An unequal endpoint source-role vector remains `ABSTAIN / SOURCE_ROLE_REVIEW_REQUIRED`. The output role must remain `CANDIDATE_RELATION`; the candidate cannot rewrite either endpoint role.
9. When the generic outcome is `ALLOW`, public exact geometry fails pair coherence. A Hydrology object reference containing `flood-warning`, `emergency-alert`, or `causal-runoff` also fails with `OPERATIONAL_OR_CAUSAL_CLAIM_DENIED`.
10. Regulatory flood context, observed flood evidence, model output, warnings, and emergency operations remain distinct Hydrology responsibilities. This profile neither evaluates nor authorizes any of them.

## v1 fixture compatibility boundary

The base fixture currently declares `OBSERVED` on both endpoints so the generic equal-role rule can exercise the candidate path. That is a synthetic compatibility choice, not a production source-role classification. In particular:

- an HSG-context reference remains a Soil interpretation/classification context, not direct measurement of infiltration or runoff;
- a WBD/HUC12 reference remains Hydrology boundary context, not a gauge observation, observed flood extent, forecast, warning, or regulatory determination;
- a future production role taxonomy or changed baseline requires an explicit versioned contract, fixture, validator, and test update. It cannot be inferred from this candidate.

## Finite outcomes and pair coherence

| Result | Implemented interpretation |
|---|---|
| `ALLOW / JOIN_CANDIDATE` | The synthetic generalized fixture is eligible for later evidence, policy, sensitivity, and human review. |
| `ABSTAIN / EVIDENCE_REF_MISSING` | At least one endpoint lacks declared evidence support. |
| `ABSTAIN / SOURCE_ROLE_REVIEW_REQUIRED` | Endpoint roles differ and require pair/domain-owned compatibility review. |
| `ABSTAIN / SENSITIVITY_REVIEW_REQUIRED` | Generalized restricted context requires sensitivity review. |
| `DENY / GEOMETRY_PRECISION_BLOCKED` | Restricted exact geometry is not admissible. |
| `ERROR / VALIDATOR_SYSTEM_ERROR` | A declared generic dependency is unavailable or invalid; no candidate is asserted. |
| Pair validator `FAIL` | The generic assessment and pair declaration conflict, including wrong profile/predicate/domain, non-fixture references, unsafe `ALLOW` precision/effects, living-person state, or an operational/causal Hydrology claim token. No relation is created. |

The finite decision belongs to the generic assessment. Pair `FAIL` is a coherence result about the submitted document; it is not a second decision vocabulary and cannot upgrade a generic `ABSTAIN`, `DENY`, or `ERROR` to `ALLOW`.

## Non-effects

This profile does not:

- activate, retrieve, admit, or version a Soil or Hydrology source;
- ingest, transform, generalize, join, or emit coordinate or geometry bytes;
- resolve an EvidenceRef to an EvidenceBundle or validate rights, freshness, lineage, limitations, or catalog closure;
- infer infiltration, runoff, recharge, connectivity, flood probability, observed inundation, stream condition, causation, suitability, or regulatory status;
- create a hydrologic model result, forecast, warning, alert, emergency decision, engineering determination, insurance determination, or life-safety advice;
- evaluate a live policy bundle or record reviewer approval;
- write RAW, WORK, QUARANTINE, PROCESSED, CATALOG/TRIPLET, or PUBLISHED state;
- create a proof pack, PromotionDecision, ReleaseManifest, correction notice, or rollback card;
- authorize a governed API, MapLibre layer, Evidence Drawer response, Focus Mode answer, export, release, deployment, or publication.

## Acceptance and rollback

Acceptance requires the seven-case pair fixture matrix, six focused pair tests, generic join regression tests, and the path-scoped `soil-hydrology-public-safe-context` workflow to pass at the exact PR head. Those checks prove only the encoded synthetic/no-network boundary; they do not prove a live source, real geometry, hydrologic inference, policy admission, review approval, release, or publication.

Rollback is a revert of this documentation update. The generic helper, pair validator, fixture matrix, tests, workflow, and all lifecycle/publication state remain unchanged by this revision.
