<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/full-atlas-coverage-priority-source-map
title: Full Atlas Coverage-Aware Prioritization Source Map
type: source-map
version: v0.1.0
status: proposed; exploratory; non-authoritative
owners: OWNER_TBD — intake steward; analytics steward; governance steward
created: 2026-08-09
updated: 2026-08-09
policy_label: repository-facing; provenance; implementation-intake
owning_root: docs/
responsibility: Record the evidence chain and repository-gap decision for the proposed CoveragePriorityScorecard profile.
truth_posture: cite-or-abstain
[/KFM_META_BLOCK_V2] -->

# Full Atlas coverage-aware prioritization source map

## Selected idea

| Item | Evidence reference | Use |
|---|---|---|
| Full Atlas triad | `gdrive://1whGonKzHVBe5FOU5ovDBakNU4Nf-30tQr09R_UNeBho#KFM-TRIAD-047` | Separates data richness from coverage gaps and warns about self-reinforcing exploration bias. |
| Programming card | `gdrive://1whGonKzHVBe5FOU5ovDBakNU4Nf-30tQr09R_UNeBho#KFM-CAND-0141` | Calls for versioned weights, source-role caps, missingness, costs, counterfactual rankings, stability, and non-authorizing receipts. |
| Repository mirror | `docs/kfm_full_atlas_seed_cards.md` (`sha256:07c7765576df1997e0be88141bd3cd213930e7281d490a8ae62afd78abe8f445`) | Locally reviewable seed cards and Slice J acceptance goal. |
| Packet adaptation | `docs/intake/exploratory/new-ideas-4-30-source-map.md` | Records county record-density prioritization as `REPO_GAP` and requires synthetic aggregates and a non-authoritative scorecard. |
| Directory authority | `docs/doctrine/directory-rules.md` (`sha256:44f7e94344cb42b630008eb0bc03a13fcb97dbdfba6f3e56579693a272571e6e`) | Governs placement and prevents parallel authority. |
| Adoption decision | `docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md` | Establishes the accepted Directory Rules baseline. |

The atlas lists `SRC-NEW430`, `SRC-AIREF`, `SRC-ENCYC`, and `SRC-URBAN` as synthesis sources. They motivate the proposal but do not authorize weights, thresholds, or real work selection.

## Repository-gap check

The implementation base is `4e4eb979caae21922af2217247ade970bd70cf82`. Current-tree and open-PR searches found analytics and planning governance, but no common machine-enforced `CoveragePriorityProfile`, `PriorityScorecard`, density-versus-gap counterfactual, or source-role-cap validator. Recent PRs `#2375`–`#2381` were inspected and excluded as non-overlapping.

## Decision and boundary

Status: `REPO_GAP`. The smallest dependency-closed continuation is a synthetic scorecard that derives both rankings and exposes their disagreement. It deliberately avoids real county identifiers, ecological observations, universal weights, source activation, job scheduling, funding allocation, work assignment, policy, review, release, and publication.

## Rollback

Revert the bounded implementation commit. The proposal adds no runtime, data migration, scheduled job, or external side effect.
