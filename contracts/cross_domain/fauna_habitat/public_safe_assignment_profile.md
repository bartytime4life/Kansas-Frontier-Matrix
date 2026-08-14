<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/cross-domain/fauna-habitat/public-safe-assignment-profile
title: Fauna–Habitat Public-Safe Assignment Candidate Profile
type: contract; cross-domain assessment profile
version: v0.1.0
status: proposed; fixture-first; no-network; non-authoritative
created: 2026-08-14
updated: 2026-08-14
policy_label: repository-facing; public-safe; sensitivity-aware; non-publisher
owning_root: contracts/
responsibility: Define pair-specific meaning and finite outcomes for a synthetic Fauna-to-Habitat assignment candidate without creating relationship truth, policy approval, release, or publication authority.
truth_posture: cite-or-abstain
related:
  - ../../../joins/cross_lane_join_assessment.md
  - ../../../../tools/validators/cross_domain/fauna_habitat/validate_public_safe_assignment.py
  - ../../../../fixtures/contracts/v1/joins/fauna_habitat_public_safe_assignment/cases.json
  - ../../../../tests/cross_domain/fauna_habitat/test_public_safe_assignment.py
  - ../../../../docs/adr/ADR-habitat-fauna-thin-slice.md
  - ../../../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
notes:
  - "ALLOW means only that the generic join helper emitted a reviewable candidate and this pair profile accepted its declared public-safe fixture posture."
  - "No coordinate or geometry bytes, live source, lifecycle write, EvidenceBundle creation, policy decision, review decision, release decision, public route, or publication is in scope."
[/KFM_META_BLOCK_V2] -->

# Fauna–Habitat Public-Safe Assignment Candidate Profile

## Status and purpose

**PROPOSED.** This contract closes one verified implementation gap: KFM already has a generic, fixture-first `CrossLaneJoinAssessment`, but the Fauna–Habitat lane has no executable pair-specific profile. The profile checks only whether a synthetic, already-generalized Fauna occurrence reference and a synthetic Habitat patch reference may become a **review candidate**. It never establishes an occurrence, habitat assignment, ecological relationship, EvidenceBundle, policy permission, review approval, release, or public claim.

## Source provenance

The pair-specific profile is derived from proposal sources and reconciled against current repository authority:

- `KFM_Pass_20_Part_2_Idea_Index_Category_Atlas_and_Expansion_Dossier.md`, Part II, `KFM-IDX-APP-002` — start with a synthetic non-sensitive occurrence and a sensitive occurrence; exact sensitive geometry must fail closed.
- `KFM_Domains_v1_1_plus_Pass23_Pass32_Consolidated_Atlas.pdf`, `KFM-P1-IDEA-0071` — test sensitivity, habitat assignment, source roles, evidence presentation, and redacted output without live-source activation.
- `kfm_encyclopedia.pdf`, page 11 — relate one non-sensitive occurrence to one habitat patch while retaining generalized public geometry and documented redaction behavior.
- `KFM_Living_Compass_Working_Edition_1.0`, Trail 13 Mission 3 and Trails 5/20 — prefer a small complete, synthetic, no-network proof and leave release/publication outside the implementation slice.
- Current repository evidence — `CrossLaneJoinAssessment` supplies deterministic identity, finite outcomes, source-role preservation, sensitivity inheritance, and non-publisher effects. The unassigned Habitat–Fauna ADR remains proposed and therefore constrains claims but does not authorize release or canonical relationship truth.

## Directory Rules basis

Accepted ADR-0029 adopts Directory Governance Standard v2. Under its cross-domain seam placement rule:

- pair semantics belong under `contracts/cross_domain/fauna_habitat/`;
- the shared pair validator belongs under `tools/validators/cross_domain/fauna_habitat/`;
- pair tests belong under `tests/cross_domain/fauna_habitat/`;
- synthetic contract fixtures follow the existing join-assessment fixture family under `fixtures/contracts/v1/joins/`.

No new root, domain-owned authority, schema authority, policy authority, proof lane, or release lane is created.

## Required endpoint roles

| Side | Required domain | Permitted fixture meaning |
|---|---|---|
| Left | `fauna` | A synthetic occurrence **reference**, not occurrence truth. |
| Right | `habitat` | A synthetic habitat-patch **reference**, not habitat truth. |
| Output | `CANDIDATE_RELATION` | Reviewable candidate only; never a canonical join. |

Both endpoints retain independent source descriptors, source roles, EvidenceRefs, sensitivity, geometry precision, and valid-time intervals. The output cannot rewrite either endpoint.

## Pair-specific rules

1. The relation profile must be `kfm:relation-profile:fauna-habitat-public-safe-assignment:v1`.
2. The candidate must use `SPATIAL_TEMPORAL`; an exact-key match is insufficient for this profile.
3. Fauna is the left endpoint and Habitat is the right endpoint so fixtures and findings remain deterministic. This ordering is an execution convention, not an authority transfer.
4. Object, source, evidence, and spatial-cell references must be synthetic `kfm:fixture:` references. A missing EvidenceRef is allowed only so the generic finite outcome can return `ABSTAIN`.
5. No living-person state is permitted.
6. `ALLOW` requires both endpoints to be `PUBLIC_SAFE`, `GENERALIZED`, evidence-bearing, temporally/spatially matched, and non-publishing.
7. Restricted exact geometry must remain `DENY`; restricted generalized context must remain `ABSTAIN` for sensitivity review.
8. A modeled/observed source-role conflict must remain `ABSTAIN` for source-role review.
9. All generic effects must remain false: no lifecycle write, evidence creation, policy/review/release decision, publication, or public-use authorization.

## Finite outcomes

| Generic outcome | Pair interpretation |
|---|---|
| `ALLOW / JOIN_CANDIDATE` | The synthetic, generalized, public-safe fixture is eligible for later pair-specific human/evidence/policy review. |
| `ABSTAIN / EVIDENCE_REF_MISSING` | Evidence support is incomplete. |
| `ABSTAIN / SOURCE_ROLE_REVIEW_REQUIRED` | Modeled, aggregate, or candidate role differences require review. |
| `ABSTAIN / SENSITIVITY_REVIEW_REQUIRED` | Restricted generalized context requires review. |
| `DENY / GEOMETRY_PRECISION_BLOCKED` | Exact restricted/prohibited geometry is not admissible. |
| `ERROR / VALIDATOR_SYSTEM_ERROR` | A declared dependency is unavailable; no candidate is asserted. |

## Non-effects

This profile does not:

- activate or retrieve a source;
- ingest, transform, generalize, or emit geometry;
- resolve an EvidenceRef to an EvidenceBundle;
- evaluate a live policy bundle or record reviewer approval;
- write RAW, WORK, QUARANTINE, PROCESSED, CATALOG/TRIPLET, or PUBLISHED state;
- create a proof pack, PromotionDecision, ReleaseManifest, correction notice, or rollback card;
- authorize a governed API, MapLibre layer, Evidence Drawer response, Focus Mode answer, export, release, deployment, or publication.

## Acceptance and rollback

Acceptance requires the ten-case fixture matrix, pair-specific tests, generic join-assessment regression tests, generated-receipt integrity, and the path-scoped workflow to pass at the exact PR head. Rollback is a single-commit revert of this profile, validator, fixtures, tests, workflow, and receipt. Existing generic join assessment behavior remains unchanged.
