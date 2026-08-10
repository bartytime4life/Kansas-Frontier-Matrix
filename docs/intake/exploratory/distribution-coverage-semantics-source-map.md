<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://doc/intake/distribution-coverage-semantics-source-map
title: Distribution and Coverage Semantics Source Map
type: exploratory-source-map
version: v0.1.0
status: exploratory; implementation-mapped; non-authoritative
owners: OWNER_TBD — intake steward; evidence steward; biodiversity steward
created: 2026-08-10
updated: 2026-08-10
policy_label: internal; exploratory-intake; distribution; coverage
owning_root: docs/
responsibility: Preserve source-to-repository reasoning for the bounded distribution coverage assessment candidate.
truth_posture: CONFIRMED repository evidence; PROPOSED candidate semantics
related:
  - ../../../docs/kfm_full_atlas_seed_cards.md
  - ../../../docs/intake/exploratory/new-ideas-4-30-source-map.md
  - ../../../contracts/evidence/distribution_coverage_assessment.md
  - ../../../contracts/domains/flora/usda_plants_distribution_snapshot.md
  - ../../../contracts/evidence/non_detection_support_assessment.md
  - ../../../contracts/source/source_record_absence_assessment.md
notes:
  - "This map preserves exploratory lineage and does not promote the source packet to repository authority."
[/KFM_META_BLOCK_V2] -->

# Distribution and Coverage Semantics Source Map

## Goal

Implement the common interpretation seam from Full Atlas `KFM-TRIAD-046` / `KFM-CAND-0138`: source-native distribution status, declared coverage, geography version, valid time, explicit absence support, and finite missing, suppressed, disputed, stale, and out-of-scope states.

## Collision and evidence review

| Evidence | Current-session observation | Disposition |
|---|---|---|
| Google Drive `KFM_Full_Atlas_seed_cards` | Calls for a reusable distribution/coverage vocabulary and negative fixtures. | PROPOSAL LINEAGE |
| `docs/kfm_full_atlas_seed_cards.md` | Repository copy carries the same triad and programming card. | CONFIRMED on authoring base `main@9e76413313b8529091d01be6132d6e987e3f9fae` |
| `docs/intake/exploratory/new-ideas-4-30-source-map.md` | Names the contract-only distribution/coverage slice as the smallest safe next action. | CONFIRMED |
| `contracts/domains/flora/usda_plants_distribution_snapshot.md` | Already owns one USDA PLANTS matrix, including explicit source rows and missing-row behavior. | PRESERVE; do not replace |
| `contracts/evidence/non_detection_support_assessment.md` | Already owns effort-bounded event non-detection. | PRESERVE; distribution is not event sampling |
| `contracts/source/source_record_absence_assessment.md` | Already owns absence of a previously seen source record across captures. | PRESERVE; row disappearance is not distribution absence |
| Repository and open-PR search | No common `DistributionCoverageAssessment` implementation or open PR was found at authoring start. | CONFIRMED |

## Bounded implementation

The candidate adds one closed schema, an exact synthetic fixture matrix, a local deterministic validator, focused tests, read-only CI, and an authoring receipt under established responsibility roots. It does not change the USDA PLANTS normalizer, Flora domain contracts, source admission, geography authority, evidence resolution, policy, runtime, map, or release behavior.

## Proof claims

The fixture matrix proves only that the proposed profile distinguishes eight finite states; missing rows cannot validate as explicit absence; complete coverage evidence is required for explicit absence; geography crosswalk posture is coherent; first-observed invention is denied; identity is deterministic; and governance flags remain false. It does not prove any real distribution fact.

## Rollback

Revert the isolated candidate commit. No external state, migration, source, or public compatibility obligation is created.
