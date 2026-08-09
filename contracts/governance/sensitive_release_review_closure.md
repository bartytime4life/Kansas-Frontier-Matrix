<!-- [KFM_META_BLOCK_V2]
doc_id: kfm://contract/governance/sensitive-release-review-closure
title: Sensitive Release Review Closure Contract
type: semantic-contract
version: v1.0.0
status: proposed-inactive; fixture-first; no-authority
owners: OWNER_TBD — Governance steward · Sensitivity steward · Release steward · Validation steward
created: 2026-08-09
updated: 2026-08-09
policy_label: internal; governance; sensitive-release; separation-of-duties; fixture-only
owning_root: contracts/
responsibility: Define fixture-only T3/T4 independent-review closure semantics over the existing ReviewAuthorityBinding without creating policy or release authority.
truth_posture: "CONFIRMED repository dependencies; PROPOSED inactive contract; UNKNOWN operational state; NEEDS VERIFICATION human review"
related:
  - ./review_authority_binding.md
  - ./ReviewRecord.md
  - ../../schemas/contracts/v1/governance/sensitive_release_review_closure.schema.json
  - ../../fixtures/contracts/v1/governance/sensitive_release_review_closure/cases.json
  - ../../tools/validators/governance/validate_sensitive_release_review_closure.py
  - ../../tests/validators/governance/test_sensitive_release_review_closure.py
  - ../../docs/intake/exploratory/full-atlas-sensitive-release-review-source-map.md
  - ../../docs/adr/ADR-0029-adopt-directory-governance-standard-v2.md
tags: [kfm, governance, review, t3, t4, separation-of-duties, release-candidate, no-authority]
notes:
  - "Adapts the Full Atlas Two-Person Rule for T3/T4 Release as a bounded closure profile over the existing ReviewAuthorityBinding contract."
  - "CLOSED_FOR_SEPARATE_RELEASE_GATE is not a PromotionDecision, ReleaseManifest, policy decision, signature, approval, or publication permission."
[/KFM_META_BLOCK_V2] -->

# Sensitive Release Review Closure

> **PROPOSED:** `SensitiveReleaseReviewClosure` records whether one T3/T4 release candidate has a structurally valid, independent review binding and the minimum evidence, policy, correction, and rollback references needed to proceed to a separate release gate. It grants no authority.

## Source-derived gap

The Google Drive Full Atlas seed card titled **Two-Person Rule for T3/T4 Release** proposes that sensitive promotion candidates cannot self-approve and must carry an auditable reviewer identity outside the author's role chain. Current repository evidence already defines `ReviewRecord`, `StewardshipAssignment`, and `ReviewAuthorityBinding`. This profile reuses the complete existing binding object and adds only T3/T4 release-candidate closure rules.

The source card is proposal evidence, not proof that the repository already implemented the rule. This profile intentionally stops before executable policy, authenticated signatures, release authorization, Evidence Drawer projection, or publication.

## Directory Rules basis

Accepted ADR-0029 assigns semantic object meaning to `contracts/`, machine shape to `schemas/contracts/v1/`, synthetic cases to `fixtures/`, reusable validators to `tools/validators/`, executable evidence to `tests/`, hosted orchestration to `.github/workflows/`, source adaptation to `docs/intake/exploratory/`, and authoring accountability to `data/receipts/generated/`.

The profile therefore lives in the existing governance family. It creates no policy source, review registry, release decision, signature collection, proof store, lifecycle lane, or public surface.

## Closure inputs

The record binds:

- the exact candidate subject, `spec_hash`, T3/T4 tier, author, and declared author role-chain actors;
- one complete `ReviewAuthorityBinding` object;
- promotion-decision, policy-decision, and release-manifest **candidate** references and digests;
- EvidenceBundle references; and
- explicit correction-path and rollback-card references.

The validator invokes the existing review-binding validator. It then requires the review subject and author to match, the reviewer to be distinct and outside the declared author role chain, the assignment to include `RELEASE_REVIEW`, and all arrays to be sorted and unique.

## Finite outcomes

| Outcome | Local meaning |
|---|---|
| `CLOSED_FOR_SEPARATE_RELEASE_GATE` | Structural review closure is complete for this fixture; a separate policy/release authority must still act. |
| `HOLD` | Review or policy projection is unresolved or conditional. |
| `DENY` | Policy denies, the embedded binding denies, or a separation/binding invariant fails. |

A validator `PASS` means the document coherently reports one of these finite outcomes. It never means the candidate is approved, signed, released, or publishable.

## Deterministic identity

```text
spec_hash  = SHA-256(RFC8785-JCS(record excluding closure_id and spec_hash))
closure_id = "kfm:sensitive-release-review-closure:" + hex(spec_hash)
```

The embedded `ReviewAuthorityBinding` retains its own independently recomputed identity.

## Fail-closed rules

- Only `T3` and `T4` candidates are in profile.
- The author must appear in `author_role_chain_actor_refs`.
- The reviewer must differ from the author and every actor in the author role chain.
- The embedded review binding must validate against its canonical schema and validator.
- A closed result requires embedded outcome `BOUND`, assignment action `RELEASE_REVIEW`, approved review, active assignment, and `policy_outcome=ALLOW`.
- Evidence, correction, rollback, promotion-decision, policy-decision, and release-manifest candidate references are mandatory.
- Every repository, lifecycle, policy, promotion, release, deployment, publication, and public-use permission is fixed `false`.

## Validation

```bash
python -m pytest -q tests/validators/governance/test_sensitive_release_review_closure.py
python tools/validators/governance/validate_sensitive_release_review_closure.py --fixtures
```

All fixtures are synthetic and no-network. Diagnostics contain stable codes and JSON paths, not candidate values.

## Non-effects

This profile does not authenticate an actor, verify a signature, evaluate a real policy bundle, resolve evidence, approve a review, create a PromotionDecision or ReleaseManifest, write lifecycle state, release, deploy, publish, or expose T3/T4 material.

## Rollback

Close the draft before merge or revert the additive commit after an authorized merge. No live review, policy, release, deployment, public artifact, or sensitive payload requires restoration.
