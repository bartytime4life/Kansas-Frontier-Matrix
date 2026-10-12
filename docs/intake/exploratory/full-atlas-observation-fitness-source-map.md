<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/full-atlas-observation-fitness-source-map
title: Full Atlas Confounder Exclusion and Observation Fitness Source Map
type: source-map
version: v0.1.0
status: proposed; exploratory; non-authoritative
owners: OWNER_TBD — intake steward; evidence steward; analysis steward
created: 2026-08-09
updated: 2026-08-09
policy_label: repository-facing; provenance; implementation-intake
owning_root: docs/
responsibility: Record the evidence chain and repository-gap decision for the proposed ObservationFitnessAssessment profile.
truth_posture: cite-or-abstain
[/KFM_META_BLOCK_V2] -->

# Full Atlas confounder exclusion and observation fitness source map

## Selected idea

| Item | Evidence reference | Use |
|---|---|---|
| Full Atlas triad | `gdrive://1whGonKzHVBe5FOU5ovDBakNU4Nf-30tQr09R_UNeBho#KFM-TRIAD-053` | Requires use-specific fitness decisions that retain excluded observations and correction reasons. |
| Programming card | `gdrive://1whGonKzHVBe5FOU5ovDBakNU4Nf-30tQr09R_UNeBho#KFM-CAND-0159` | Names observation decisions, context snapshots, exclusion receipts, and synthetic confounder/correction cases. |
| Repository mirror | `docs/kfm_full_atlas_seed_cards.md` (`sha256:07c7765576df1997e0be88141bd3cd213930e7281d490a8ae62afd78abe8f445`) | Locally reviewable copy of the same seed cards. |
| Packet adaptation | `docs/intake/exploratory/new-ideas-4-30-source-map.md` | Records confounder fitness as an unresolved reusable seam and requires synthetic vegetation observations. |
| Directory authority | `docs/doctrine/directory-rules.md` (`sha256:44f7e94344cb42b630008eb0bc03a13fcb97dbdfba6f3e56579693a272571e6e`) | Governs placement and prevents parallel authority. |
| Adoption decision | `docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md` | Establishes the accepted Directory Rules baseline. |

The atlas lists `SRC-NEW430`, `SRC-ATM`, `SRC-AIREF`, and `SRC-ENCYC` as synthesis inputs. They motivate the proposal but do not authorize scientific thresholds or real-source activation.

## Repository-gap check

The implementation base is `7335ed9ea0f81342ae0b1c7828a21ac74711c78b`. Current-tree and open-PR searches found representation-fitness, temporal-support, non-detection, and domain quality documentation, but no common machine-enforced observation-level confounder exclusion, retained-evidence, or corrected-mask decision profile. The new profile composes those concerns without changing their authority.

## Decision and boundaries

Status: `REPO_GAP`. The smallest dependency-closed continuation is one synthetic observation assessment that derives a finite use-specific decision and proves evidence-retention and correction-lineage invariants. It deliberately avoids universal vegetation thresholds, real coordinates, source activation, observation deletion, scientific truth, analysis authorization, policy, review, release, and publication.

## Collision and rollback note

Current main through `7335ed9e` and the repository's open pull-request set were inspected before implementation. Revert the bounded implementation commit to remove the proposal; no migration or runtime rollback is required.
