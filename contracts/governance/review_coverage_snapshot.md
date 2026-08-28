<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/review-coverage-snapshot
title: ReviewCoverageSnapshot Contract
type: semantic-contract; fixture-first; non-authoritative
version: v1.0.0
status: proposed-inactive
owners: OWNER_TBD — governance steward · validation steward · release steward
created: 2026-08-14
updated: 2026-08-14
policy_label: internal; fixture-only; no-authority
related:
  - ./ReviewRecord.md
  - ./review_authority_binding.md
  - ../../schemas/contracts/v1/governance/review_coverage_snapshot.schema.json
  - ../../tools/validators/governance/validate_review_coverage_snapshot.py
  - ../../fixtures/contracts/v1/governance/review_coverage_snapshot/cases.json
  - ../../tests/validators/governance/test_review_coverage_snapshot.py
  - ../../docs/doctrine/directory-rules.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, governance, review, exact-head, review-coverage, fixture-only, no-authority]
[/KFM_META_BLOCK_V2] -->

# ReviewCoverageSnapshot

> A deterministic review-coverage observation for one pull-request head. It records who reviewed what head, the review state, required-role coverage, and declared independence limits without creating approval, merge, promotion, release, or publication authority.

## Purpose

A `ReviewCoverageSnapshot` closes one narrow repository-control ambiguity: a review that was valid for an earlier pull-request head must not be silently treated as review of later bytes.

The snapshot binds review observations to the currently observed pull-request `head_sha` and derives a finite posture from:

- each review's `reviewed_head_sha`;
- review state;
- required reviewer-role coverage; and
- declared reviewer independence where independence is required.

It is an observation and validation artifact only. It does not authenticate a GitHub identity and it does not decide whether repository settings require or accept a review.

## Source lineage

This object family is derived from the supplied **KFM Briefing-to-System Integration Architecture, v1.0, PROPOSED DESIGN**, Lane A §12.1 (page 22 of 61), which describes `ReviewCoverageSnapshot` as recording who reviewed what, the exact head SHA, review state, and independence limits. §12.2 and §12.3 further require exact-head matching and surface exact-head review coverage in the governance dashboard.

That briefing remains proposal lineage, not repository authority. This slice therefore remains `PROPOSED_INACTIVE` and `FIXTURE_ONLY`.

## Relationship to existing governance objects

| Object | Relationship |
|---|---|
| `ReviewRecord` | Records semantic review events and reviewer posture. `ReviewCoverageSnapshot` observes whether review projections cover one exact repository head. |
| `ReviewAuthorityBinding` | Checks declared reviewer/assignment/subject agreement. It does not bind repository review coverage to a pull-request head. |
| `PromotionDecision` / release objects | May consume review evidence in later governed flows, but this snapshot never promotes or releases. |
| GitHub review / CODEOWNERS / branch protection | May supply observations or requirements, but host state remains separate and must be independently verified. |

## Machine shape

The companion schema is `schemas/contracts/v1/governance/review_coverage_snapshot.schema.json`.

Required semantic groups are:

- repository and pull-request identity;
- currently observed exact `head_sha`;
- required reviewer roles and independence posture;
- individual review observations with `reviewed_head_sha` and review state;
- recomputed coverage checks;
- finite outcome and reason codes; and
- explicit no-authority permissions/non-effects.

## Finite outcomes

| Outcome | Meaning |
|---|---|
| `CURRENT` | Every counted review is bound to the observed head, required roles are covered by approving reviews, and declared independence requirements are satisfied. |
| `HOLD` | Head binding is current, but required role coverage or independence is incomplete. |
| `STALE` | One or more counted reviews apply to a different head SHA than the currently observed pull-request head. |
| `DENY` | The document is structurally invalid or claims derived checks/outcome that do not match recomputation. |

`CURRENT` is review-coverage evidence only. It is not approval or authorization.

## Counted review states

`APPROVED`, `CHANGES_REQUESTED`, and `SUBMITTED` are counted as review observations for exact-head freshness. `DISMISSED` and `PENDING` do not satisfy required-role coverage. Only `APPROVED` satisfies a required reviewer role.

A stale counted review causes `STALE` even when another review is current. The safe posture is to refresh review against the new head rather than infer carry-forward approval.

## Independence semantics

When `independence_required` is true, each approving review used to satisfy a required role must declare `independent: true`. This is a structural declaration only; the validator does not authenticate employment, organizational independence, GitHub account ownership, or host review policy.

## Non-effects

A valid snapshot:

- does not authenticate reviewer identity;
- does not prove CODEOWNERS routing or branch-protection requirements;
- does not authorize merge or write operations;
- does not create policy, promotion, release, deployment, or publication authority;
- does not mutate a pull request, branch, repository setting, lifecycle state, or public product.

## Validation and proof

The fixture-first validator recomputes exact-head freshness, required-role coverage, independence satisfaction, outcome, and reason codes. Focused fixtures/tests cover a current snapshot, stale review head, missing required role, failed independence, and forged derived state.

Hosted exact-head CI coupling and live GitHub review ingestion remain **NEEDS VERIFICATION** and out of scope for this slice.

## Directory Rules basis

`ReviewCoverageSnapshot` is a governance semantic object, so its meaning belongs under the existing `contracts/governance/` responsibility lane; machine shape belongs under the existing governance schema lane; executable validation belongs under `tools/validators/governance/`; examples belong under `fixtures/`; and proof belongs under `tests/`. No new root or parallel authority is introduced. This follows adopted Directory Rules v2 through ADR-0029.

## Rollback

Close the draft pull request before merge or revert the implementation commit(s) after merge. No external state, repository setting, release, deployment, or public product is changed by this fixture-only slice.
