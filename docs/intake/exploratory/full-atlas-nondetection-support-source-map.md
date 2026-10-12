<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://intake/exploratory/full-atlas-nondetection-support-source-map
title: Full Atlas Sampling Effort and Non-Detection Support Source Map
type: source-map
version: v0.1.0
status: proposed; exploratory; non-authoritative
owners: OWNER_TBD — intake steward; evidence steward
created: 2026-08-09
updated: 2026-08-09
policy_label: repository-facing; provenance; implementation-intake
owning_root: docs/
responsibility: Record the evidence chain and repository-gap decision for the proposed NonDetectionSupportAssessment profile.
truth_posture: cite-or-abstain
[/KFM_META_BLOCK_V2] -->

# Full Atlas sampling effort and non-detection support source map

## Selected idea

| Item | Evidence reference | Use |
|---|---|---|
| Full Atlas triad | `gdrive://1whGonKzHVBe5FOU5ovDBakNU4Nf-30tQr09R_UNeBho#KFM-TRIAD-045` | Calls for sampling-effort and non-detection support with pair-coherence checks. |
| Programming card | `gdrive://1whGonKzHVBe5FOU5ovDBakNU4Nf-30tQr09R_UNeBho#KFM-CAND-0135` | Names `SamplingEvent`, `DetectionOpportunity`, `EffortProfile`, `NonDetectionAssertion`, and required negative fixtures. |
| Repository mirror | `docs/kfm_full_atlas_seed_cards.md` (`sha256:07c7765576df1997e0be88141bd3cd213930e7281d490a8ae62afd78abe8f445`) | Locally reviewable copy of the same seed cards. |
| Directory authority | `docs/doctrine/directory-rules.md` (`sha256:44f7e94344cb42b630008eb0bc03a13fcb97dbdfba6f3e56579693a272571e6e`) | Governs placement and prevents parallel authority. |
| Adoption decision | `docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md` | Establishes the accepted Directory Rules baseline. |

The atlas lists `SRC-NEW430`, `SRC-FAUNA`, and `SRC-ENCYC` as the underlying synthesis sources. Those identifiers motivate the proposal; they are not treated as implementation authority.

## Repository-gap check

The implementation base is `4e4eb979caae21922af2217247ade970bd70cf82`. Searches of current paths and open pull requests found domain-oriented sampling references, but no common machine-enforced `SamplingEvent`, `DetectionOpportunity`, `NonDetectionAssertion`, or equivalent pair-coherence validator. Existing `docs/standards/STAC_DWC_PROFILE.md` and `docs/sources/catalog/ebird/sampling-event-data.md` are corroborative documentation only; this change does not alter them or claim source activation.

## Decision and boundaries

Status: `REPO_GAP`, implemented as one proposed composite rather than four unbound object families. The composite is fixture-only, uses synthetic references, returns fail-closed finite decisions, and makes “within declared effort” mandatory. It cannot establish biological absence, source trust, evidence acceptance, work priority, policy, review, release, or publication.

## Collision and rollback note

Recent work through PRs `#2375`–`#2380` was inspected and excluded as non-overlapping. Revert the bounded implementation commit to remove this proposal; no migration or runtime rollback is required.
